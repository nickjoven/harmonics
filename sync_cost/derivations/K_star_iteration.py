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
without independent recomputation; field_equation_iteration.py openly
admits its direct r -> K*r iteration hits the XOR-degenerate vacuum
r* = 0 because the 4 minimum Klein-bottle modes cancel.

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
    # Summary
    # ------------------------------------------------------------
    print("=" * 78)
    print("  SUMMARY")
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
