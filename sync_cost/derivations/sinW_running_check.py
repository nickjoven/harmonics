#!/usr/bin/env python3
"""
sin^2(theta_W) running compatibility check.

Framework claim:
    sin^2(theta_W) = 8/35 = 0.22857 at the tree scale (K = 1)
                     0.23121           at M_Z (observed)
    1.1% residual attributed to RG running from tree scale down to M_Z.

This script tests that claim with pure SM 1-loop RG running, using
only topologically-derived inputs (no free parameters):

    1. Tree-scale boundary conditions from the duty-cycle dictionary
       (duty_cycle_dictionary.md, gate_duty_predictions.py):
           alpha_2(tree) = duty(q_2) = 1/q_2^3 = 1/8
           alpha_Y(tree) = duty(q_3) = 1/q_3^3 = 1/27
           1/alpha_em(tree) = q_2^3 + q_3^3 = 35
           sin^2(theta_W, tree) = q_2^3/(q_2^3+q_3^3) = 8/35

    2. SM 1-loop beta functions (topologically determined by SU(3)x
       SU(2)xU(1), three generations, and one Higgs doublet):
           b_2 = -19/6
           b_Y = 41/6        (non-GUT normalized U(1)_Y)
           b_1 = 41/10       (GUT-normalized, b_1 = (3/5) b_Y)

    3. Identification of the tree scale with the Planck scale, per
       gate_duty_predictions.py line 268 ("K = 1.000 -> Planck scale
       (tree root)") and the hierarchy formula R = 6 x 13^54 from
       hierarchy.md (Planck/Hubble ratio).

The 1-loop running is:
    1/alpha_i(mu) = 1/alpha_i(mu_0) - (b_i/(2 pi)) ln(mu/mu_0)

Written out:
    sin^2(theta_W, mu) = alpha_Y(mu) / (alpha_Y(mu) + alpha_2(mu))

Usage:
    python3 sync_cost/derivations/sinW_running_check.py
"""

import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from framework_constants import ALPHA_EM_MZ, SIN2_TW_MZ


# ============================================================================
# Observed values at M_Z (PDG 2024)
# ============================================================================

M_Z = 91.1876                       # GeV
ALPHA_2_MZ_OBS = ALPHA_EM_MZ / SIN2_TW_MZ
ALPHA_Y_MZ_OBS = ALPHA_EM_MZ / (1 - SIN2_TW_MZ)
ALPHA_1_MZ_OBS = (5/3) * ALPHA_Y_MZ_OBS   # GUT normalization

# ============================================================================
# SM 1-loop beta coefficients (with 3 generations, 1 Higgs doublet)
# ============================================================================
#
# Convention: d(1/alpha_i)/d(ln mu) = -b_i / (2 pi).
# Equivalently: alpha_i^{-1}(mu_2) = alpha_i^{-1}(mu_1) - (b_i/(2 pi)) ln(mu_2/mu_1).
#
# SU(3)_c:      b_3 = -11 + (4/3) n_g               = -7        (asymptotically free)
# SU(2)_L:      b_2 = -22/3 + (4/3) n_g + 1/6        = -19/6    (asymptotically free)
# U(1)_Y:       b_Y = (4/3) n_g (Tr Y^2 per gen)/k_Y
#                 + (1/6)(Y_H^2)/k_Y
# In non-GUT normalization (k_Y = 1): b_Y = 41/6
# In GUT normalization (k_Y = 5/3):   b_1 = (3/5) * 41/6 = 41/10
#
B_Y = 41.0 / 6.0      # non-GUT-normalized U(1)_Y
B_2 = -19.0 / 6.0     # SU(2)_L
B_1 = 41.0 / 10.0     # GUT-normalized U(1)_1
B_3 = -7.0            # SU(3)_c


# ============================================================================
# Framework: tree-scale boundary conditions (K = 1, duty-cycle dictionary)
# ============================================================================

Q2 = 2                # Klein-bottle denominator (SU(2))
Q3 = 3                # Klein-bottle denominator (SU(3))

ALPHA_2_TREE = 1.0 / Q2**3              # 1/8 = duty(q_2)
ALPHA_Y_TREE = 1.0 / Q3**3              # 1/27 = duty(q_3)
ALPHA_EM_TREE = 1.0 / (Q2**3 + Q3**3)   # 1/35
SIN2_TW_TREE = Q2**3 / (Q2**3 + Q3**3)  # 8/35 = 0.228571...

# Tree-scale identified with Planck scale per gate_duty_predictions.py
# and hierarchy.md (R = 6 x 13^54 = Planck/Hubble).
M_PL = 1.221e19       # GeV (reduced Planck mass)

# Also try GUT scale for comparison
M_GUT = 2.0e16        # GeV (typical GUT scale)


# ============================================================================
# RG running
# ============================================================================

def alpha_inv_run(alpha_inv_0, b, mu, mu_0):
    """1-loop running: 1/alpha(mu) = 1/alpha(mu_0) - (b/2pi) ln(mu/mu_0)."""
    return alpha_inv_0 - (b / (2 * math.pi)) * math.log(mu / mu_0)


def sin2_from_couplings(alpha_Y, alpha_2):
    """sin^2(theta_W) = alpha_Y / (alpha_Y + alpha_2)."""
    return alpha_Y / (alpha_Y + alpha_2)


def sin2_sm_from_MZ(mu):
    """Standard-Model sin^2(theta_W) at mu, 1-loop, using M_Z boundary."""
    a2_inv = alpha_inv_run(1/ALPHA_2_MZ_OBS, B_2, mu, M_Z)
    aY_inv = alpha_inv_run(1/ALPHA_Y_MZ_OBS, B_Y, mu, M_Z)
    if a2_inv <= 0 or aY_inv <= 0:
        return float('nan')
    return sin2_from_couplings(1/aY_inv, 1/a2_inv)


def run_tree_to_MZ(alpha_2_tree, alpha_Y_tree, mu_tree, mu_end=M_Z):
    """Run tree-scale absolute values DOWN to mu_end. Returns (1/a2, 1/aY, sin2)."""
    a2_inv_end = alpha_inv_run(1/alpha_2_tree, B_2, mu_end, mu_tree)
    aY_inv_end = alpha_inv_run(1/alpha_Y_tree, B_Y, mu_end, mu_tree)
    if a2_inv_end <= 0 or aY_inv_end <= 0:
        return a2_inv_end, aY_inv_end, float('nan')
    sw = sin2_from_couplings(1/aY_inv_end, 1/a2_inv_end)
    return a2_inv_end, aY_inv_end, sw


def dsin2_dlnmu(alpha_Y, alpha_2):
    """d(sin^2)/d(ln mu) analytic at 1-loop.

    Using dalpha_i/d(ln mu) = b_i alpha_i^2/(2 pi), the quotient gives:
        d(sin^2)/d(ln mu) = alpha_Y alpha_2 (b_Y alpha_Y - b_2 alpha_2)
                            / [2 pi (alpha_Y + alpha_2)^2]
    """
    num = alpha_Y * alpha_2 * (B_Y * alpha_Y - B_2 * alpha_2)
    den = 2 * math.pi * (alpha_Y + alpha_2) ** 2
    return num / den


def bisect_scale(target, mu_lo, mu_hi, sin2_fn, n=200):
    """Find mu in [mu_lo, mu_hi] where sin2_fn(mu) = target."""
    lo = math.log(mu_lo)
    hi = math.log(mu_hi)
    for _ in range(n):
        mid = 0.5 * (lo + hi)
        s = sin2_fn(math.exp(mid))
        # sin^2 increases with mu in SM: higher mu -> higher sin^2
        if s > target:
            hi = mid
        else:
            lo = mid
    return math.exp(0.5 * (lo + hi))


# ============================================================================
# Main
# ============================================================================

def main():
    print("=" * 78)
    print("  sin^2(theta_W) RUNNING COMPATIBILITY CHECK")
    print("  Tree-scale 8/35 vs. observed 0.23121 at M_Z")
    print("=" * 78)

    # ----- 1. Framework tree-scale inputs -----
    print(f"\n{'-' * 78}")
    print("  1. TREE-SCALE BOUNDARY CONDITIONS (FROM DUTY-CYCLE DICTIONARY)")
    print(f"{'-' * 78}\n")

    print(f"  From duty(q) = 1/q^d = 1/q^3 with d=3 (spatial dimension):")
    print()
    print(f"    alpha_2(tree) = duty(q_2) = 1/q_2^3 = 1/{Q2**3} = {ALPHA_2_TREE:.10f}")
    print(f"    alpha_Y(tree) = duty(q_3) = 1/q_3^3 = 1/{Q3**3} = {ALPHA_Y_TREE:.10f}")
    print(f"    1/alpha_em(tree) = q_2^3 + q_3^3 = {Q2**3 + Q3**3}")
    print()
    print(f"    sin^2(theta_W, tree) = q_2^3 / (q_2^3 + q_3^3)"
          f" = 8/35 = {SIN2_TW_TREE:.10f}")
    print()
    print(f"  No free parameters. All numbers are q_2=2, q_3=3, d=3 (topology).")

    # ----- 2. SM 1-loop betas -----
    print(f"\n{'-' * 78}")
    print("  2. SM 1-LOOP BETA FUNCTIONS (TOPOLOGICALLY DETERMINED)")
    print(f"{'-' * 78}\n")

    print(f"  b_Y = 41/6  = {B_Y:+.6f}   (U(1)_Y, non-GUT normalized)")
    print(f"  b_2 = -19/6 = {B_2:+.6f}   (SU(2)_L, asymptotically free)")
    print(f"  b_3 = -7    = {B_3:+.6f}   (SU(3)_c)")
    print(f"  (GUT-normalized b_1 = (3/5) b_Y = {B_1:.6f})")

    # ----- 3. Run tree -> M_Z assuming tree = Planck scale -----
    print(f"\n{'-' * 78}")
    print("  3. RUN TREE (= M_Pl) DOWN TO M_Z")
    print(f"{'-' * 78}\n")

    print(f"  Tree scale identified with Planck: mu_tree = M_Pl = {M_PL:.3e} GeV")
    print(f"  ln(M_Z / M_Pl) = {math.log(M_Z/M_PL):.4f}")
    print()

    a2_inv_MZ, aY_inv_MZ, sw_MZ = run_tree_to_MZ(
        ALPHA_2_TREE, ALPHA_Y_TREE, M_PL)

    print(f"  Running tree-scale absolute values down to M_Z:")
    print(f"    1/alpha_2(tree=M_Pl) = {1/ALPHA_2_TREE:.3f}")
    print(f"    b_2/(2pi) ln(M_Z/M_Pl) = "
          f"{(B_2/(2*math.pi))*math.log(M_Z/M_PL):+.3f}")
    print(f"    1/alpha_2(M_Z) = {a2_inv_MZ:+.3f}")
    print()
    print(f"    1/alpha_Y(tree=M_Pl) = {1/ALPHA_Y_TREE:.3f}")
    print(f"    b_Y/(2pi) ln(M_Z/M_Pl) = "
          f"{(B_Y/(2*math.pi))*math.log(M_Z/M_PL):+.3f}")
    print(f"    1/alpha_Y(M_Z) = {aY_inv_MZ:+.3f}")
    print()

    if math.isnan(sw_MZ):
        print(f"  *** 1/alpha_2(M_Z) went NEGATIVE ***")
        print(f"  The tree-scale value 1/alpha_2 = 8 is too small to accommodate")
        print(f"  the asymptotic-freedom running of SU(2) over 17 decades.")
        print(f"  The SM beta function predicts 1/alpha_2(M_Pl) ~ 49 (not 8).")
    else:
        print(f"  sin^2(theta_W, M_Z) predicted from tree = M_Pl: {sw_MZ:.6f}")
        print(f"  Observed:                                       {SIN2_TW_MZ:.6f}")
        print(f"  Delta:                                          "
              f"{abs(sw_MZ - SIN2_TW_MZ)/SIN2_TW_MZ:.2%}")

    print()
    print(f"  Observed 1/alpha_2(M_Z) = {1/ALPHA_2_MZ_OBS:.3f}  "
          f"(vs. tree 1/alpha_2 = 8)")
    print(f"  Observed 1/alpha_Y(M_Z) = {1/ALPHA_Y_MZ_OBS:.3f}  "
          f"(vs. tree 1/alpha_Y = 27)")
    print()
    print(f"  The absolute tree-scale couplings (1/alpha_2=8, 1/alpha_Y=27) are")
    print(f"  NOT the SM couplings at the Planck scale. The tree-scale dictionary")
    print(f"  is a number-theoretic reference point, not a physical SM boundary.")

    # ----- 4. What the framework actually predicts: the ratio sin^2 -----
    print(f"\n{'-' * 78}")
    print("  4. THE RATIO: HOW DOES SM sin^2(theta_W) RUN?")
    print(f"{'-' * 78}\n")

    print(f"  Analytic 1-loop derivative at M_Z:")
    deriv_MZ = dsin2_dlnmu(ALPHA_Y_MZ_OBS, ALPHA_2_MZ_OBS)
    print(f"    d(sin^2 theta_W) / d(ln mu) |_{{M_Z}} = {deriv_MZ:+.6e}")
    print(f"    Sign: POSITIVE  -->  sin^2 theta_W INCREASES with energy in SM.")
    print()

    print(f"  SM 1-loop sin^2(theta_W) vs. scale "
          f"(anchored at observed M_Z value):\n")
    print(f"    {'log10(mu/GeV)':>13s}  {'mu (GeV)':>13s}  "
          f"{'sin^2 theta_W':>14s}  {'delta from 8/35':>16s}")
    print("  " + "-" * 64)

    scales = [-3, -2, -1, 0, 1, math.log10(M_Z), 2, 3, 4, 6, 8,
              10, 12, 14, 16, math.log10(M_PL)]
    for lm in scales:
        mu = 10 ** lm
        sw = sin2_sm_from_MZ(mu)
        d = sw - SIN2_TW_TREE
        label = ""
        if abs(lm - math.log10(M_Z)) < 1e-6:
            label = "  M_Z"
        elif abs(lm - math.log10(M_PL)) < 1e-6:
            label = "  M_Pl"
        print(f"    {lm:13.2f}  {mu:13.3e}  {sw:14.6f}  "
              f"{d:+16.6f}{label}")

    # ----- 5. At what scale does SM give sin^2 = 8/35 ? -----
    print(f"\n{'-' * 78}")
    print("  5. AT WHAT SCALE DOES SM-RUN sin^2 EQUAL THE TREE VALUE 8/35?")
    print(f"{'-' * 78}\n")

    # sin^2 is monotonic in mu in this range; 8/35 < 0.23121 means mu < M_Z.
    mu_star = bisect_scale(SIN2_TW_TREE, 1e-4, M_Z, sin2_sm_from_MZ)
    sw_check = sin2_sm_from_MZ(mu_star)
    print(f"  mu* = {mu_star:.4f} GeV")
    print(f"  sin^2 theta_W (SM, mu*) = {sw_check:.8f}")
    print(f"  tree value 8/35         = {SIN2_TW_TREE:.8f}")
    print(f"  |delta|                 = {abs(sw_check - SIN2_TW_TREE):.2e}")
    print()
    print(f"  log10(mu*/M_Z) = {math.log10(mu_star/M_Z):+.4f}")
    print(f"  log10(mu*/GeV) = {math.log10(mu_star):+.4f}")
    print(f"  (m_W = 80.4, m_Z = 91.2, m_t = 173 GeV for reference)")

    # ----- 6. Compatibility verdict -----
    print(f"\n{'-' * 78}")
    print("  6. VERDICT: IS THE 1.1% RESIDUAL EXPLAINED BY SM RUNNING?")
    print(f"{'-' * 78}\n")

    delta_tree_MZ = SIN2_TW_MZ - SIN2_TW_TREE
    percent = delta_tree_MZ / SIN2_TW_MZ * 100

    print(f"  Tree value:     sin^2 theta_W(tree) = 8/35 = {SIN2_TW_TREE:.6f}")
    print(f"  M_Z observed:   sin^2 theta_W(M_Z)  =       {SIN2_TW_MZ:.6f}")
    print(f"  Raw difference:                     = {delta_tree_MZ:+.6f}"
          f"  ({percent:+.2f}%)")
    print()

    print("  SM 1-loop running direction:")
    print(f"    Observed sin^2 = 0.23121 at M_Z")
    print(f"    Running UP   (M_Z -> M_Pl):  sin^2 increases -> ~"
          f"{sin2_sm_from_MZ(M_PL):.3f}")
    print(f"    Running DOWN (M_Z -> 1 GeV): sin^2 decreases -> ~"
          f"{sin2_sm_from_MZ(1.0):.3f}")
    print()
    print("  The tree value 8/35 = 0.22857 is LOWER than the M_Z observed 0.23121.")
    print("  In SM 1-loop running, sin^2 DECREASES toward the IR. Therefore:")
    print("  the tree value 8/35 is realized in the IR, not the UV.")
    print(f"  Specifically: mu* = {mu_star:.2f} GeV (below M_Z).")
    print()

    print("  THIS MEANS:")
    print()
    print("  (A) If 'tree scale' = Planck (gate_duty_predictions.py:268):")
    print("      - Running with absolute tree values (1/a_2=8, 1/a_Y=27)")
    print(f"        FAILS catastrophically — 1/alpha_2(M_Z) = {a2_inv_MZ:+.2f}")
    print("        (negative, unphysical).")
    print("      - Even running just the RATIO is impossible: in the SM, sin^2")
    print(f"        at M_Pl is {sin2_sm_from_MZ(M_PL):.4f}, NOT 8/35 = 0.2286.")
    print()
    print("  (B) If 'tree scale' is the scale where SM-run sin^2 = 8/35:")
    print(f"      - That scale is mu* = {mu_star:.2f} GeV, just BELOW M_Z.")
    print("      - The 1.1% running is quantitatively consistent with SM betas,")
    print("        but the tree scale is NOT the Planck or GUT scale — it is a")
    print("        near-electroweak scale in the IR.")
    print()

    print("  (C) CONCLUSION:")
    print()
    print("      The tree-scale 8/35 is NUMERICALLY compatible with M_Z at the")
    print("      1% level (it is within one decade of SM running), but the")
    print("      framework's identification of tree scale with the Planck scale")
    print("      is INCOMPATIBLE with SM 1-loop running:")
    print()
    print("        - Sign: sin^2(theta_W) runs UP in the UV, not down. To go")
    print("          from 8/35 at high scale to 0.23121 at M_Z requires sin^2")
    print("          to INCREASE toward the IR, opposite to SM direction.")
    print()
    print("        - Magnitude: the SM prediction at M_Pl is sin^2 ~ 0.47,")
    print(f"          two orders of magnitude off from 8/35 = 0.229.")
    print()
    print("      The 1.1% residual between 8/35 and 0.23121 CANNOT be explained")
    print("      by running 8/35 from the Planck scale down to M_Z using the SM")
    print("      1-loop beta functions. Either:")
    print("        (i)  the tree scale is not the Planck scale (but then the")
    print("             hierarchy formula R = 6 x 13^54 loses its role as the")
    print("             K -> mu mapping endpoint), OR")
    print("        (ii) the framework's running is NOT ordinary SM running —")
    print("             it must come from the K-dependence of the duty cycles")
    print("             themselves (gate_duty_predictions.py sections 5-7),")
    print("             which is a different dynamical law from 1-loop RG.")
    print()
    print("      Option (ii) is consistent with gate_duty_predictions.py, which")
    print("      does NOT run via SM betas — it runs via K, and fits K*(M_Z) to")
    print("      alpha_s/alpha_2. The 1.1% residual there is the decoherence")
    print("      tax |r| at finite K, not an RG running of SM couplings.")
    print()
    print("      The tree-scale 8/35 is a number-theoretic identity (q_2^3 /")
    print("      (q_2^3+q_3^3)), and its 1.1% agreement with M_Z observation is")
    print("      an accidental near-coincidence at the electroweak scale, not a")
    print("      consequence of running from a high energy scale.")

    # ----- 7. Numerical summary table -----
    print(f"\n{'=' * 78}")
    print("  SUMMARY TABLE")
    print(f"{'=' * 78}\n")

    print(f"  {'quantity':>35s}  {'value':>14s}  {'source':>20s}")
    print("  " + "-" * 74)
    print(f"  {'sin^2(theta_W) tree (8/35)':>35s}  "
          f"{SIN2_TW_TREE:14.6f}  {'duty dict':>20s}")
    print(f"  {'sin^2(theta_W) obs (M_Z)':>35s}  "
          f"{SIN2_TW_MZ:14.6f}  {'PDG':>20s}")
    print(f"  {'raw difference':>35s}  "
          f"{delta_tree_MZ:+14.6f}  {'(1.1%)':>20s}")
    print()
    print(f"  {'SM sin^2 at M_Pl (run from M_Z)':>35s}  "
          f"{sin2_sm_from_MZ(M_PL):14.6f}  {'1-loop SM':>20s}")
    print(f"  {'SM sin^2 at M_GUT=2e16':>35s}  "
          f"{sin2_sm_from_MZ(M_GUT):14.6f}  {'1-loop SM':>20s}")
    print(f"  {'SM sin^2 at 1 GeV':>35s}  "
          f"{sin2_sm_from_MZ(1.0):14.6f}  {'1-loop SM':>20s}")
    print()
    print(f"  {'scale where SM sin^2 = 8/35':>35s}  "
          f"{mu_star:14.2f}  {'GeV (1-loop)':>20s}")
    print(f"  {'d(sin^2)/d(lnmu) at M_Z':>35s}  "
          f"{deriv_MZ:+14.6e}  {'1-loop SM':>20s}")
    print()
    print(f"  {'run tree(=M_Pl) -> M_Z: 1/a_2':>35s}  "
          f"{a2_inv_MZ:+14.3f}  {'(unphysical)':>20s}")
    print(f"  {'run tree(=M_Pl) -> M_Z: 1/a_Y':>35s}  "
          f"{aY_inv_MZ:+14.3f}  {'(vs obs 98.4)':>20s}")

    print(f"\n{'=' * 78}")
    print("  BOTTOM LINE: SM 1-loop running does NOT connect tree-scale 8/35")
    print("  (at Planck) to observed 0.23121 at M_Z. The 1.1% residual is NOT")
    print("  a standard RG-running effect. The framework's K-dependence gives")
    print("  a different (non-SM) running that does reproduce M_Z observations")
    print("  (see gate_duty_predictions.py), but this is a K -> mu mapping, not")
    print("  SM 1-loop running. The tree-scale value 8/35 is a number-theoretic")
    print("  identity with near-accidental 1% agreement at the electroweak scale.")
    print(f"{'=' * 78}")


if __name__ == "__main__":
    main()
