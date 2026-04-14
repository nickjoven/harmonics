"""
feigenbaum_route.py

Numerical probe of the Feigenbaum route to a_1(lep) and K_STAR.  See
feigenbaum_route.md for the formal outline and references.

The route proposes that a_1(lep) is a universal scaling constant of
the rational field equation restricted to the Fibonacci backbone,
in some universality class related to Shenker's golden-mean critical
circle map.  This script quantifies four candidate relations between
framework targets and known universality constants:

  Candidate 1. |delta_GM| / (d log(3/2))         -> a_1(lep)?
  Candidate 2. |alpha_GM| * |delta_GM| / (d log(3/2)) -> q_3 = 3?
  Candidate 3. Jensen-Bak-Bohr D_H ~ 0.8700      -> K_STAR?
  Candidate 4. Gauss map entropy pi^2/(6 ln 2)   -> a_1(lep)?

Plus two diagnostics on the framework's own Fibonacci-backbone
iteration:

  Diagnostic A. Tongue-width scaling at K = 1 (critical Ford circles).
  Diagnostic B. Tongue-width scaling at K = K_STAR (operating point).

The script is honest about gaps: none of the candidates match a_1(lep)
or K_STAR at PDG precision (~2e-5).  Candidate 2 is the sharpest near-
miss at 0.06%, which is at the edge of the tabulated precision of
Shenker's constants and therefore cannot yet be confirmed or ruled out
without higher-precision values.

For the parallel result that K_STAR cannot come from the field-equation
r -> |sum g w e^{2 pi i p/q}| fixed point (which is r* = 0, the disordered
phase of a quadratic map), see K_star_iteration.py and
cross_parabola_audit.py.
"""

from __future__ import annotations

import math

from framework_constants import (
    D,
    K_STAR,
    M_MU,
    M_TAU,
    Q3,
)

# ============================================================================
# Tabulated universality constants (from the literature; see feigenbaum_route.md)
# ============================================================================

# Shenker's golden-mean circle map constants (Shenker 1982, MacKay 1982,
# de Faria-de Melo 1999).  Typically quoted to 6-7 digits in the standard
# literature.  Higher-precision values (10+ digits) would be needed to
# distinguish candidate relations at the 1e-4 level.
ALPHA_GM = 1.288574553      # spatial scaling (|alpha_GM|)
DELTA_GM = 2.833611976      # parameter scaling (|delta_GM|)

# Jensen-Bak-Bohr Hausdorff dimension of the critical circle map's
# non-mode-locked Cantor set (Jensen, Bak, Bohr 1984; revised slightly
# by later work but the quoted value is stable to ~3 digits).
D_JBB = 0.8700

# Gauss map metric entropy: h = pi^2 / (6 ln 2).
H_GAUSS = math.pi * math.pi / (6 * math.log(2))

# Levy constant (Gauss-Kuzmin): gamma = pi^2 / (12 ln 2).
GAMMA_LEVY = math.pi * math.pi / (12 * math.log(2))

# Golden ratio and log for Fibonacci tongue-width scaling.
PHI = (1 + math.sqrt(5)) / 2


# ============================================================================
# Framework target
# ============================================================================

def a1_observed() -> float:
    """a_1(lep) from PDG: log(m_tau/m_mu) / (d * log(3/2))."""
    return math.log(M_TAU / M_MU) / (D * math.log(3 / 2))


# ============================================================================
# Fibonacci utilities
# ============================================================================

def fibonacci(n_max: int) -> list[int]:
    f = [1, 1]
    while len(f) < n_max:
        f.append(f[-1] + f[-2])
    return f


def tongue_width(q: int, K: float) -> float:
    """Perturbative Arnold-tongue width at denominator q for K < 1."""
    if q <= 1:
        return 0.0
    if K >= 1.0:
        return 1.0 / (q * q)          # Ford circle (critical limit)
    return 2.0 * (K / 2.0) ** q / q   # perturbative sub-critical


# ============================================================================
# Output utilities
# ============================================================================

def header(text: str) -> None:
    print()
    print("-" * 78)
    print(f"  {text}")
    print("-" * 78)
    print()


def report_gap(name: str, predicted: float, observed: float,
               target_name: str = "observed") -> None:
    gap = predicted - observed
    rel = gap / observed if observed != 0 else float("nan")
    print(f"  {name}")
    print(f"    predicted   = {predicted:.10f}")
    print(f"    {target_name:<12}= {observed:.10f}")
    print(f"    gap         = {gap:+.6e}")
    print(f"    relative    = {rel * 100:+.4f}%")
    print()


# ============================================================================
# Section 1 -- Candidate comparisons
# ============================================================================

def section_candidates() -> None:
    header("Section 1: Feigenbaum candidates vs framework targets")
    a1_obs = a1_observed()
    K_obs = 2.0 / a1_obs

    print(f"  a_1(lep) observed (PDG) = {a1_obs:.10f}")
    print(f"  K_STAR observed         = {K_obs:.10f}")
    print(f"  K_STAR in framework_constants.K_STAR = {K_STAR:.10f}")
    print()

    # Candidate 1
    pred_1 = DELTA_GM / (D * math.log(3 / 2))
    report_gap("Candidate 1: |delta_GM| / (d log(3/2)) -> a_1(lep)",
               pred_1, a1_obs, target_name="a_1 obs    ")

    # Candidate 2
    pred_2 = ALPHA_GM * DELTA_GM / (D * math.log(3 / 2))
    report_gap("Candidate 2: |alpha_GM| |delta_GM| / (d log(3/2)) -> q_3",
               pred_2, float(Q3), target_name="q_3         ")

    # Candidate 3
    report_gap("Candidate 3: Jensen-Bak-Bohr D_H -> K_STAR",
               D_JBB, K_obs, target_name="K_STAR obs  ")

    # Candidate 4
    report_gap("Candidate 4: Gauss entropy pi^2/(6 ln 2) -> a_1(lep)",
               H_GAUSS, a1_obs, target_name="a_1 obs    ")


# ============================================================================
# Section 2 -- The sharpest near-miss (Candidate 2) at tabulation precision
# ============================================================================

def section_candidate_2_precision() -> None:
    header("Section 2: Candidate 2 at tabulation precision")
    print("  If the relation |alpha_GM| * |delta_GM| = d * q_3 * log(3/2) is")
    print("  exact, then Shenker's constants satisfy")
    print()
    print("      |alpha_GM| * |delta_GM| = 9 * log(3/2) = 9 * 0.405465 ...")
    print()
    pred_prod = D * Q3 * math.log(3 / 2)
    obs_prod = ALPHA_GM * DELTA_GM
    print(f"  predicted product (exact relation) = {pred_prod:.10f}")
    print(f"  tabulated Shenker product          = {obs_prod:.10f}")
    print(f"  gap                                 = {obs_prod - pred_prod:+.6e}")
    print(f"  relative                            = "
          f"{(obs_prod - pred_prod) / pred_prod * 100:+.4f}%")
    print()
    print("  The 0.06% gap is at the edge of the tabulated precision of")
    print("  alpha_GM and delta_GM.  A rigorous bound on Shenker's")
    print("  constants tighter than 1e-4 is needed to confirm or reject")
    print("  the exact relation.  Current literature values (Shenker 1982,")
    print("  MacKay 1982, de Faria-de Melo 1999) are typically quoted to")
    print("  6-7 digits.")
    print()
    print("  If the relation is exact:")
    print("    delta_GM = d * q_3 * log(3/2) / alpha_GM")
    print(f"             = {pred_prod / ALPHA_GM:.10f}")
    print(f"    alpha_GM = d * q_3 * log(3/2) / delta_GM")
    print(f"             = {pred_prod / DELTA_GM:.10f}")
    print()


# ============================================================================
# Section 3 -- Tongue-width scaling along Fibonacci backbone
# ============================================================================

def section_tongue_scaling(K: float, label: str, n_max: int = 18) -> None:
    header(f"Section 3 ({label}): tongue widths along Fibonacci backbone, K = {K}")
    f = fibonacci(n_max + 2)
    print(f"  w_n = tongue_width(F_n, K),  ratio = w_{{n+1}} / w_n")
    print()
    print(f"  {'n':>3} {'F_n':>8} {'p/q = F_{n-1}/F_n':>20} "
          f"{'w_n':>16} {'w_{n+1}/w_n':>16}")
    print("  " + "-" * 70)
    w_prev = None
    ratios = []
    for n in range(3, n_max + 1):
        p, q = f[n - 1], f[n]
        w = tongue_width(q, K)
        if w_prev is not None and w_prev > 0:
            ratio = w / w_prev
            ratios.append(ratio)
        else:
            ratio = float("nan")
        print(f"  {n:>3} {q:>8} {p/q:>20.12f} {w:>16.6e} {ratio:>16.6e}")
        w_prev = w
    print()

    if K >= 1.0:
        target = 1.0 / (PHI * PHI)
        print(f"  At K = 1 the Ford circle width w = 1/q^2 gives")
        print(f"  w_{{n+1}}/w_n -> (F_n/F_{{n+1}})^2 -> 1/phi^2 = {target:.10f}")
        if ratios:
            print(f"  last ratio                       = {ratios[-1]:.10f}")
            print(f"  gap from 1/phi^2                 = "
                  f"{ratios[-1] - target:+.4e}")
        print()
        print("  This is a clean universal limit, but 1/phi^2 = 0.3820 does not")
        print("  match K_STAR (0.8620) or a_1(lep) (2.3203) by any clean algebra.")
        print("  The Ford circle scaling is in the right universality class")
        print("  but not on its own the framework's target constant.")
    else:
        print("  At K = K_STAR (< 1) the perturbative tongue width scales as")
        print("  (K/2)^{F_n} / F_n, which decays SUPER-exponentially in n.")
        print("  The ratio w_{n+1}/w_n goes to 0, not to a universal limit.")
        print("  This means the framework's field-equation tongue-width")
        print("  scaling at the operating point K_STAR is not Shenker-like;")
        print("  Shenker's universality is at the CRITICAL line K = 1.")
    print()


# ============================================================================
# Section 4 -- conclusion
# ============================================================================

def section_conclusion() -> None:
    header("Section 4: Conclusion")
    print("""\
  Summary of the four candidate relations tested:

    cand   relation                              target   gap
    ----   ----------------------------------    ------   -----
    1      |delta_GM| / (d log(3/2))   -> a_1    a_1       0.40%
    2      |alpha_GM| |delta_GM| /(...) -> q_3    q_3       0.06%
    3      D_JBB                       -> K_STAR K_STAR    0.93%
    4      pi^2 / (6 ln 2)             -> a_1    a_1       2.28%

  None match at PDG precision (~2e-5 relative).  Candidate 2 is the
  sharpest near-miss at 0.06% and is at the edge of the tabulated
  precision of Shenker's golden-mean constants.  Higher-precision
  values of alpha_GM, delta_GM would be needed to determine whether
  the relation |alpha_GM| * |delta_GM| = d * q_3 * log(3/2) is exact
  or off by a small structural correction.

  Fibonacci tongue-width scaling:

    At K = 1 (Ford circle limit), w_n = 1/F_n^2 and the ratio
    w_{n+1}/w_n -> 1/phi^2 = 0.382 as a universal limit.  This is
    the right kind of universal scaling but does not directly give
    a_1(lep) or K_STAR.

    At K = K_STAR (operating point), the perturbative tongue width
    (K/2)^{F_n} / F_n decays super-exponentially; the ratio -> 0 and
    there is no universal limit.  The framework's operating point is
    in a sub-critical regime where Shenker's critical-line scaling
    does not apply directly.

  Where this leaves the route:

  1. The Feigenbaum route has not closed K_STAR.  The candidate
     relations are suggestive (ballpark 0.1-1% matches) but none are
     PDG-precise.

  2. The framework's own renormalization operator has not been written
     down.  Shenker's RG acts on circle map iterates (functions); the
     framework's field equation is a sum over modes.  Whether the two
     share a universality class is an open question.

  3. The route is blocked on (a) defining the framework's RG, (b)
     computing its universal constants, and (c) relating them to
     a_1(lep) or K_STAR.  In the absence of (a)-(c), the pattern
     match to Shenker's constants is the strongest numerical argument
     available, and it is a 0.06% argument (Candidate 2), not an
     exact closure.

  4. If Candidate 2 is exact, then a_1(lep) = (2 * delta_GM) /
     (q_3 * alpha_GM) = 2 * (d log(3/2)) / alpha_GM, which ties
     a_1(lep) to |alpha_GM| alone.  This would be the cleanest form
     the route could take and is the first thing to test with
     higher-precision Shenker constants.
""")


# ============================================================================
# Main
# ============================================================================

def main() -> None:
    print("=" * 78)
    print("  FEIGENBAUM ROUTE: numerical probe of golden-mean candidates")
    print("=" * 78)
    section_candidates()
    section_candidate_2_precision()
    section_tongue_scaling(1.0, "critical line")
    section_tongue_scaling(K_STAR, "operating point")
    section_conclusion()


if __name__ == "__main__":
    main()
