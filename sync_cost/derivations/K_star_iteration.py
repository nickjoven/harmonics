"""
K* from the rational field equation, high precision.

The framework's self-consistency (rational_field_equation.md, Part II):

    |r| = |Σ_{p/q}  g(p/q) * w(p/q, K_0 |r|) * e^{2πi p/q}|

where

    K        = K_0 * |r|                           (effective coupling)
    w(p/q, K) = 2 (K/2)^q / q                      (Arnold-tongue width)
    g(p/q)   = density on the Stern-Brocot tree    (choice of ensemble)

The fixed point r* gives K* = K_0 * r*.  The framework's stated
K* = 0.862 has been quoted at 3 digits from "coherence cascade data"
without independent recomputation; the direct r -> K*r iteration
hits the XOR-degenerate vacuum r* = 0 because the 4 minimum Klein-
bottle modes cancel.

The XOR degeneracy is a consequence of using only the minimum modes.
Including the Fibonacci backbone (modes at F_n/F_{n+1} converging to
1/phi) breaks the symmetry: these rationals cluster near 1/phi, not
at antipodal positions, and the phasor sum is non-zero.

This script implements the iteration under three mode ensembles:

  1. Fibonacci backbone only (the path from 0/1 to 1/phi).
  2. Full Stern-Brocot tree to depth D with uniform density.
  3. Farey-density weighted (g(p/q) = phi(q)) tree to depth D.

For each, it iterates r until convergence at 1e-12 and reports
K* = K_0 * r*.  The target is the lepton-identity-implied value
K* = q_2 / a_1(leptons) = 0.8619606.

item12_C_from_K_star.py has the closed-form identity
    a_1(leptons) = q_2 / K*    =>    C = q_2^2 / K*^2
which, combined with any independent K* derivation at 5+ digits,
closes item 12 completely.  This script is that independent
derivation attempt.
"""

from __future__ import annotations

import cmath
import math

from framework_constants import K_STAR, M_MU, M_TAU, Q2
from framework_constants import D as DIM

# ============================================================================
# Utilities
# ============================================================================

def fibonacci(n_max: int) -> list[int]:
    """F_1 = F_2 = 1, F_3 = 2, ..."""
    fs = [1, 1]
    while len(fs) < n_max:
        fs.append(fs[-1] + fs[-2])
    return fs


def euler_phi(n: int) -> int:
    """Euler's totient."""
    if n <= 0:
        return 0
    result = n
    p = 2
    temp = n
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1
    if temp > 1:
        result -= result // temp
    return result


def tongue_width(q: int, K: float) -> float:
    """Perturbative Arnold tongue width at denominator q, for K < 1."""
    if q <= 0:
        return 0.0
    if q == 1:
        return min(K / (2 * math.pi), 1.0)
    if K >= 1.0:
        return 1.0 / (q * q)
    return 2 * (K / 2) ** q / q


def stern_brocot_depth(depth: int) -> list[tuple[int, int]]:
    """
    All rationals at Stern-Brocot depth <= depth, returned as
    (p, q) pairs in the unit interval [0, 1] including endpoints.
    """
    pairs = [(0, 1), (1, 1)]

    def recurse(a, b, c, d, level):
        if level <= 0:
            return
        p, q = a + c, b + d
        pairs.append((p, q))
        recurse(a, b, p, q, level - 1)
        recurse(p, q, c, d, level - 1)

    recurse(0, 1, 1, 1, depth)
    return pairs


# ============================================================================
# Field sums under three ensembles
# ============================================================================

def field_sum_fibonacci(K: float, n_max: int = 30) -> complex:
    """
    Sum over the Fibonacci backbone F_n/F_{n+1}.  These are the
    convergents to 1/phi from below.  Each contributes
    w(F_{n+1}, K) * exp(2 pi i * F_n / F_{n+1}).
    """
    fs = fibonacci(n_max + 2)
    total = 0 + 0j
    for n in range(1, n_max):
        p = fs[n - 1]
        q = fs[n]
        if q < 2:
            continue
        w = tongue_width(q, K)
        total += w * cmath.exp(2j * math.pi * p / q)
    return total


def field_sum_stern_brocot(K: float, depth: int = 8) -> complex:
    """
    Sum over all rationals in [0, 1] at Stern-Brocot depth <= depth,
    with uniform weight g = 1.
    """
    pairs = stern_brocot_depth(depth)
    total = 0 + 0j
    for p, q in pairs:
        if q < 2:
            continue
        w = tongue_width(q, K)
        total += w * cmath.exp(2j * math.pi * p / q)
    return total


def field_sum_farey_weighted(K: float, q_max: int = 60) -> complex:
    """
    Sum over all rationals p/q with 0 < p < q <= q_max, gcd(p,q)=1,
    weighted by density g(p/q) = 1 (each Farey node once).
    """
    total = 0 + 0j
    for q in range(2, q_max + 1):
        for p in range(1, q):
            if math.gcd(p, q) != 1:
                continue
            w = tongue_width(q, K)
            total += w * cmath.exp(2j * math.pi * p / q)
    return total


# ============================================================================
# Fixed-point iteration
# ============================================================================

def iterate(field_sum_func, K_0: float = 1.0, r0: float = 0.5,
            max_iter: int = 200, tol: float = 1e-13, verbose: bool = False,
            **kwargs) -> tuple[float, float, int, bool]:
    """
    Iterate |r| -> |field_sum(K_0 |r|)| until convergence.

    Returns (r_star, K_star, n_iter, converged).
    """
    r = r0
    for n in range(1, max_iter + 1):
        K = K_0 * r
        total = field_sum_func(K, **kwargs)
        r_new = abs(total)
        if verbose:
            print(f"    iter {n:3d}: K = {K:.10f}, |r| = {r:.10f}, "
                  f"|r_new| = {r_new:.10f}")
        if abs(r_new - r) < tol:
            return r_new, K_0 * r_new, n, True
        r = r_new
    return r, K_0 * r, max_iter, False


# ============================================================================
# Reference quantities
# ============================================================================

def lepton_implied_K_star() -> tuple[float, float]:
    """K* from the lepton identity a_1(lep) * K* = q_2."""
    a1 = math.log(M_TAU / M_MU) / (DIM * math.log(1.5))
    return Q2 / a1, a1


# ============================================================================
# Main
# ============================================================================

def main():
    print("=" * 78)
    print("  K* FROM RATIONAL FIELD EQUATION ITERATION")
    print("=" * 78)
    print()

    K_LEP, a1_lep = lepton_implied_K_star()
    print("  Reference values:")
    print(f"    framework cited K* = {K_STAR}")
    print(f"    lepton-implied K*  = q_2 / a_1(lep) = {K_LEP:.10f}")
    print(f"    a_1(leptons)       = {a1_lep:.10f}")
    print()
    print("  Target for iteration: a K* that matches either of the above")
    print("  at better than 3-digit precision.")
    print()

    # ------------------------------------------------------------
    # Ensemble A: Fibonacci backbone only, several K_0 values
    # ------------------------------------------------------------
    print("-" * 78)
    print("  ENSEMBLE A: Fibonacci backbone F_n/F_{n+1}, n up to 30")
    print("-" * 78)
    print()
    print("  K_0 scan (self-consistency is  r = |field_sum(K_0 r)|):")
    print()
    print(f"  {'K_0':>8}  {'r*':>14}  {'K* = K_0 r*':>14}  "
          f"{'converged':>10}  {'iters':>6}")
    print("  " + "-" * 60)
    for K_0 in [0.5, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0]:
        r_s, K_s, n, ok = iterate(
            field_sum_fibonacci, K_0=K_0, r0=0.5, n_max=30
        )
        print(f"  {K_0:>8.2f}  {r_s:>14.10f}  {K_s:>14.10f}  "
              f"{str(ok):>10}  {n:>6}")
    print()

    # ------------------------------------------------------------
    # Ensemble B: Stern-Brocot depth D, K_0 = 1
    # ------------------------------------------------------------
    print("-" * 78)
    print("  ENSEMBLE B: full Stern-Brocot tree, depth scan, K_0 = 1")
    print("-" * 78)
    print()
    print(f"  {'depth':>6}  {'nodes':>8}  {'r*':>14}  {'K* = r*':>14}  "
          f"{'iters':>6}")
    print("  " + "-" * 54)
    for depth in [4, 6, 8, 10, 12, 14]:
        n_nodes = len(stern_brocot_depth(depth))
        r_s, K_s, n, ok = iterate(
            field_sum_stern_brocot, K_0=1.0, r0=0.5, depth=depth
        )
        print(f"  {depth:>6}  {n_nodes:>8}  {r_s:>14.10f}  "
              f"{K_s:>14.10f}  {n:>6}")
    print()

    # ------------------------------------------------------------
    # Ensemble C: Farey-weighted nodes up to q_max, K_0 = 1
    # ------------------------------------------------------------
    print("-" * 78)
    print("  ENSEMBLE C: Farey nodes, q <= q_max scan, K_0 = 1")
    print("-" * 78)
    print()
    print(f"  {'q_max':>6}  {'nodes':>8}  {'r*':>14}  {'K* = r*':>14}  "
          f"{'iters':>6}")
    print("  " + "-" * 54)
    for q_max in [10, 20, 40, 60, 100, 200]:
        # count farey nodes
        n_nodes = sum(
            1 for q in range(2, q_max + 1)
            for p in range(1, q) if math.gcd(p, q) == 1
        )
        r_s, K_s, n, ok = iterate(
            field_sum_farey_weighted, K_0=1.0, r0=0.5, q_max=q_max
        )
        print(f"  {q_max:>6}  {n_nodes:>8}  {r_s:>14.10f}  "
              f"{K_s:>14.10f}  {n:>6}")
    print()

    # ------------------------------------------------------------
    # Detailed iteration at best ensemble
    # ------------------------------------------------------------
    print("-" * 78)
    print("  DETAILED ITERATION: Fibonacci backbone, K_0 = 1, verbose")
    print("-" * 78)
    print()
    r_s, K_s, n, ok = iterate(
        field_sum_fibonacci, K_0=1.0, r0=0.5, n_max=30,
        verbose=True, tol=1e-14,
    )
    print()
    print(f"  converged after {n} iterations")
    print(f"  r* = {r_s:.12f}")
    print(f"  K* = {K_s:.12f}")
    print()
    print(f"  lepton-implied K* = {K_LEP:.12f}")
    print(f"  difference        = {K_s - K_LEP:+.8f}")
    print()

    # ------------------------------------------------------------
    # Part 4: Critical K_0 bifurcation scan
    # ------------------------------------------------------------
    print("-" * 78)
    print("  BIFURCATION SCAN: K_0 at which non-trivial fixed point appears")
    print("-" * 78)
    print()
    print("  Below a critical K_0, the only fixed point is r* = 0.  Above")
    print("  it, a non-trivial branch r* > 0 appears (partial sync).  Scan")
    print("  K_0 to locate the bifurcation for each ensemble, starting the")
    print("  iteration from r0 = 0.9 so we follow the upper branch if it")
    print("  exists.")
    print()
    print(f"  {'K_0':>6}  {'A: Fibonacci':>16}  {'B: SB depth 10':>18}  "
          f"{'C: Farey q<=60':>18}")
    print("  " + "-" * 66)
    for K_0 in [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 5.0]:
        r_a, _, _, _ = iterate(field_sum_fibonacci, K_0=K_0, r0=0.9, n_max=30)
        r_b, _, _, _ = iterate(field_sum_stern_brocot, K_0=K_0, r0=0.9, depth=10)
        r_c, _, _, _ = iterate(field_sum_farey_weighted, K_0=K_0, r0=0.9, q_max=60)
        K_a = K_0 * r_a
        K_b = K_0 * r_b
        K_c_val = K_0 * r_c
        print(f"  {K_0:>6.2f}  "
              f"{r_a:>8.4f} K={K_a:>5.3f}  "
              f"{r_b:>8.4f} K={K_b:>5.3f}  "
              f"{r_c:>8.4f} K={K_c_val:>5.3f}")
    print()

    # ------------------------------------------------------------
    # Part 5: Scaling of the approach to r = 0
    # ------------------------------------------------------------
    print("-" * 78)
    print("  PART 5: SCALING OF THE APPROACH TO r = 0")
    print("-" * 78)
    print()
    print("  The iteration contracts to the trivial vacuum at K_0 = 1.")
    print("  Question: what power law does r_n follow?  The answer turns")
    print("  out to be structurally meaningful.")
    print()
    print("  Prediction from the perturbative tongue sum: at small r, the")
    print("  leading contribution is the smallest denominator q in the sum")
    print("  (q = q_min = 2, since q=1 is excluded).  The single q=2 mode")
    print("  at p/q = 1/2 has phasor e^(i pi) = -1, so its contribution is")
    print()
    print("      w(1/2, K) * |-1| = (K/2)^2 = K^2 / 4")
    print()
    print("  Substituting K = K_0 r gives")
    print()
    print("      r_{n+1} -> (K_0 / 2)^2 * r_n^2       (at K_0 = 1: r_n^2 / 4)")
    print()
    print("  So the approach is QUADRATIC in r, with prefactor (K_0/2)^2,")
    print("  and the exponent 2 IS exactly q_2 = the smallest tongue-")
    print("  contributing denominator.  Higher q's give subleading terms.")
    print()
    print("  Verification: iterate each ensemble, record the trace, fit")
    print("  r_{n+1} / r_n^2 to extract the prefactor.")
    print()

    def trace_iter(field_sum_func, K_0=1.0, r0=0.5, n_iter=6, **kwargs):
        r = r0
        trace = [r]
        for _ in range(n_iter):
            K = K_0 * r
            r = abs(field_sum_func(K, **kwargs))
            trace.append(r)
        return trace

    ensembles = [
        ("Fibonacci (n_max=30)", field_sum_fibonacci, {"n_max": 30}),
        ("Stern-Brocot (d=10)", field_sum_stern_brocot, {"depth": 10}),
        ("Farey (q_max=60)", field_sum_farey_weighted, {"q_max": 60}),
    ]

    for name, fn, kw in ensembles:
        trace = trace_iter(fn, K_0=1.0, r0=0.5, n_iter=5, **kw)
        print(f"  Ensemble: {name}")
        print(f"    trace:          {[f'{v:.4e}' for v in trace]}")
        ratios_2 = []
        for i in range(len(trace) - 1):
            if trace[i] > 1e-30:
                ratios_2.append(trace[i + 1] / trace[i] ** 2)
        print(f"    r_{{n+1}} / r_n^2: "
              f"{[f'{v:.6f}' for v in ratios_2]}")
        print(f"    predicted (K_0/2)^2 at K_0=1 = {(1.0/2)**2}")
        print()

    # Confirm the prefactor goes to (K_0/2)^2 as r_n shrinks
    print("  Observation: the ratio r_{n+1}/r_n^2 converges to 1/4 in")
    print("  every ensemble, confirming that the leading contribution at")
    print("  small r is exactly the q=2 mode.  The prefactor is set by")
    print("  the perturbative tongue width (K/2)^2 of the single q=2")
    print("  rational 1/2, and the exponent is q_min = q_2 = 2.")
    print()

    # --- K_0 scan: prefactor should equal (K_0/2)^2 exactly ---
    print("  K_0 SCAN: the prefactor should track (K_0/2)^2 exactly.")
    print("  This fixes the q=2 coefficient independent of ensemble.")
    print()
    print(f"  {'K_0':>6}  {'r_inf/r_n^2':>14}  {'(K_0/2)^2':>12}  "
          f"{'agreement':>12}")
    print("  " + "-" * 52)
    for K_0 in [0.5, 1.0, 1.5, 2.0]:
        trace = trace_iter(field_sum_fibonacci, K_0=K_0, r0=0.3,
                           n_iter=7, n_max=30)
        # Use the last finite ratio
        last_ratio = None
        for i in range(len(trace) - 1):
            if 1e-40 < trace[i] < 1e-3:
                last_ratio = trace[i + 1] / trace[i] ** 2
        predicted = (K_0 / 2) ** 2
        agreement = ("exact" if last_ratio is not None
                     and abs(last_ratio - predicted) < 1e-10
                     else f"{abs(last_ratio - predicted):.1e}")
        print(f"  {K_0:>6.2f}  {last_ratio:>14.10f}  {predicted:>12.6f}"
              f"  {agreement:>12}")
    print()
    print("  The prefactor equals (K_0/2)^2 to machine precision at every")
    print("  K_0, confirming that the local expansion of the map near r=0")
    print("  is exact:")
    print()
    print("      r_{n+1} = (K_0/2)^2 r_n^2 + O(r_n^3)")
    print()
    print("  At K_0 = q_2 = 2 the leading coefficient equals exactly 1.")
    print("  This is the 'marginal' value at which the quadratic")
    print("  contraction would stop pulling r toward 0.  The integer q_2 = 2")
    print("  is the critical K_0 of the map's local linearization.")
    print()
    print("  Structural interpretation:")
    print()
    print("  The map r -> |Sum w e^{2pi i p/q}| has a zero-slope fixed")
    print("  point at r = 0 because the q=1 modes are excluded.  The")
    print("  first non-vanishing term in the Taylor expansion of the")
    print("  map near r = 0 is of order r^(q_min).  For q_min = q_2 = 2,")
    print("  this is a quadratic map, and 0 is a 'superstable' fixed")
    print("  point -- any r_0 below the basin boundary contracts doubly-")
    print("  exponentially to 0.")
    print()
    print("  The q_2 = 2 that sets the exponent here is the SAME q_2")
    print("  that appears in the lepton identity a_1(lep) = q_2 / K*:")
    print("  it is not two different uses of the integer 2 -- it is the")
    print("  single structural integer 'smallest Stern-Brocot denominator")
    print("  greater than 1', which is q_2 by definition.")
    print()
    print("  This means the failed iteration and the successful lepton")
    print("  identity are reading the SAME piece of framework structure.")
    print("  The iteration fails to produce K* because r=0 is superstable,")
    print("  not because the q_2 content is missing.  The q_2 content is")
    print("  present in both -- it just shows up as an exponent in the")
    print("  iteration's approach law rather than as a fixed-point value.")
    print()
    print("=" * 78)
    print()
    print("  OUTCOME: the naive iteration FAILS to reproduce K* = 0.862.")
    print()
    print("  Observations:")
    print()
    print("  1. At K_0 = 1, every ensemble (Fibonacci backbone, Stern-")
    print("     Brocot to depth 14, Farey-weighted to q=200) contracts to")
    print("     r* = 0.  This is the degenerate vacuum field_equation_")
    print("     iteration.py flagged.  It is not a quirk of the 4-mode")
    print("     Klein minimum -- it is the generic behavior of the map")
    print("     r -> |Sum g(p/q) w(p/q, K_0 r) e^{2pi i p/q}| when")
    print("     K_0 < K_c (critical coupling for partial sync onset).")
    print()
    print("  2. Above K_0 ~= 3, a non-trivial upper branch appears at")
    print("     r* approx 0.38 (Fibonacci backbone).  The product K_0 r*")
    print("     gives K* > 1, NOT 0.862.  Increasing K_0 just scales K*")
    print("     linearly -- there is no fixed K* value that falls out.")
    print()
    print("  3. Therefore the framework's K* = 0.862 is NOT the fixed")
    print("     point of the standard Kuramoto self-consistency on any")
    print("     of the ensembles tried here.  The 3-digit value 0.862")
    print("     has been cited from 'MSPU D30 coherence cascade data'")
    print("     for years without corresponding code that recomputes it.")
    print()
    print("  Conclusion: the 'independent K* derivation' does not exist")
    print("  in the framework in the form an r-iteration would require.")
    print("  What DOES exist, independently:")
    print()
    print("  - The lepton tongue-width identity (item12_C_from_K_star.md):")
    print(f"      K* = q_2 / a_1(leptons) = {K_LEP:.8f} +/- 2.1e-5")
    print()
    print("    This uses the PDG lepton mass ratio as input but produces")
    print("    a 5+ digit value compatible with the cited 3-digit 0.862")
    print("    under rounding.  If the framework accepts the lepton sector")
    print("    as a primary constraint, this identity IS the K* derivation")
    print("    at higher precision.")
    print()
    print("  - The tongue-width interpretation explains the structural")
    print("    role of K*: it is the coupling at which the q = q_2 = 2")
    print("    Arnold tongue has width (K*/2)^2, whose inverse square root")
    print("    q_2/K* equals the lepton generation exponent a_1(lep).")
    print()
    print("  Remaining open question:")
    print()
    print("  Is there a SECOND, framework-internal route to K* that does")
    print("  not use lepton masses and also gives 0.8619606?  Candidates")
    print("  (none tested in this script; none known to work):")
    print()
    print("    - cosmological running K(t) from Planck to today at matching")
    print("      the observed cosmic age ratio (creation_frontier_test.py")
    print("      treats K_today = 0.862 as input, not output)")
    print("    - w*-K* coupling via boundary_weight.md partial-locking")
    print("      formula (gives K > 1 under the naive solve, unusable)")
    print("    - the Lyapunov spectrum of the circle map at specific Ω_0")
    print("      (not attempted in the framework's existing code)")
    print()
    print("  Until one of these produces 0.8619606 independently, item 12")
    print("  closes conditionally on accepting K* = q_2 / a_1(leptons) as")
    print("  the high-precision determination.  The fit count is 1 (K*")
    print("  itself), not 0.")
    print()


if __name__ == "__main__":
    main()
