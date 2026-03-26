#!/usr/bin/env python3
"""
Mass hierarchy from amplitude contraction rates.

Mass is depth in the Stern-Brocot tree.  Each Fibonacci level deeper,
the amplitude (distance between gate crossings) shrinks by phi^2.
The three generations correspond to three basins (B, C, A) whose
phase-state weights set different contraction rates.

Phase states (from duty/gap factorisation at q=2, q=3):
    B = duty(2) * gap(3) = (1/8)(26/27) = 26/216   (heaviest)
    C = gap(2) * duty(3) = (7/8)(1/27)  =  7/216   (middle)
    A = duty(2) * duty(3) = (1/8)(1/27) =  1/216   (lightest)

Contraction rate = 1 / width  =>  rate_B : rate_C : rate_A = 1/26 : 1/7 : 1/1
(or equivalently 216/26 : 216/7 : 216/1).

Mass ratio m_i/m_j = (rate_i / rate_j)^exponent,
or equivalently m_i/m_j = (w_j / w_i)^exponent   since rate ~ 1/width.

This script:
  1. Scans exponents for lepton mass ratio fit
  2. Tests direct weight-power model
  3. Predicts quark mass ratios from best-fit exponent
  4. Tests the phi^(2*Delta_n) amplitude picture

Usage:
    python3 sync_cost/derivations/mass_contraction.py
"""

import math
import sys
from fractions import Fraction

sys.path.insert(0, "sync_cost/derivations")
from circle_map_utils import PHI, PHI_SQ, LN_PHI_SQ


# ── Constants ─────────────────────────────────────────────────────────────────

SQRT5 = math.sqrt(5)

# Phase-state weights (numerators; common denominator 216 cancels in ratios)
W_B = 26      # heaviest generation
W_C = 7       # middle generation
W_A = 1       # lightest generation

# Contraction rates (proportional to 1/weight)
R_B = 216 / W_B   # 8.3077
R_C = 216 / W_C   # 30.857
R_A = 216 / W_A   # 216

# Observed lepton masses (MeV, PDG 2024)
M_TAU   = 1776.86
M_MU    = 105.658
M_E     = 0.51100

# Observed lepton ratios
RATIO_TAU_E = M_TAU / M_E    # 3477.4
RATIO_MU_E  = M_MU / M_E     # 206.8
RATIO_TAU_MU = M_TAU / M_MU  # 16.82

# Observed quark masses (MeV, MS-bar at 2 GeV for light quarks, PDG 2024)
M_B_QUARK = 4180.0    # bottom
M_S_QUARK = 93.4      # strange
M_D_QUARK = 4.67      # down

M_T_QUARK = 172500.0  # top (pole mass)
M_C_QUARK = 1270.0    # charm
M_U_QUARK = 2.16      # up

# Observed quark ratios
RATIO_B_D = M_B_QUARK / M_D_QUARK    # ~895
RATIO_S_D = M_S_QUARK / M_D_QUARK    # ~20
RATIO_B_S = M_B_QUARK / M_S_QUARK    # ~44.8

RATIO_T_U = M_T_QUARK / M_U_QUARK    # ~79861
RATIO_C_U = M_C_QUARK / M_U_QUARK    # ~588
RATIO_T_C = M_T_QUARK / M_C_QUARK    # ~135.8


# ── Helpers ───────────────────────────────────────────────────────────────────

def mass_ratio_from_weights(w_heavy, w_light, exponent):
    """Mass ratio = (w_light / w_heavy)^(-exponent) = (w_heavy/w_light)^exponent?

    No — heavier basin has LARGER weight but SMALLER contraction rate.
    rate ~ 1/weight, so rate_heavy < rate_light.
    Mass ~ rate^exponent would give lighter = higher rate => wrong.

    The correct mapping: mass ~ (1/width)^exponent  is wrong because
    wider basin = more phase space = heavier particle.

    Actually: mass proportional to weight^exponent directly.
    B is heaviest and has largest weight (26).  That works.
    """
    return (w_heavy / w_light) ** exponent


def mass_ratio_from_rates(r_heavy, r_light, exponent):
    """Mass ratio using contraction rates.

    Heavier particle has SLOWER contraction (wider basin, more amplitude
    before next crossing).  So mass ~ 1/rate^exponent = width^exponent.
    Equivalently: m_heavy/m_light = (rate_light/rate_heavy)^exponent.
    """
    return (r_light / r_heavy) ** exponent


def fit_exponent_weights(w_heavy, w_light, target_ratio):
    """Find exponent a such that (w_heavy/w_light)^a = target_ratio."""
    return math.log(target_ratio) / math.log(w_heavy / w_light)


def chi2_lepton(exponent):
    """Sum of squared log-residuals for lepton ratios."""
    pred_tau_e  = mass_ratio_from_weights(W_B, W_A, exponent)
    pred_mu_e   = mass_ratio_from_weights(W_C, W_A, exponent)
    r1 = (math.log(pred_tau_e) - math.log(RATIO_TAU_E)) ** 2
    r2 = (math.log(pred_mu_e)  - math.log(RATIO_MU_E))  ** 2
    return r1 + r2


# ── Part 1: mass ratios for fixed exponents ──────────────────────────────────

def part1_fixed_exponents():
    print("=" * 78)
    print("PART 1: Mass ratios m_i/m_j = (weight_i / weight_j)^exponent")
    print("        Weights:  B=26 (heavy)   C=7 (middle)   A=1 (light)")
    print("=" * 78)

    exponents = {
        "sqrt(5)":      SQRT5,
        "5/2":          2.5,
        "ln(phi^2)":    LN_PHI_SQ,
        "d=3":          3.0,
        "phi":          PHI,
        "2":            2.0,
    }

    # Header
    fmt = "{:<14s} {:>10s}   {:>12s} {:>12s} {:>12s}"
    print()
    print(fmt.format("exponent", "value",
                     "B/A (tau/e)", "C/A (mu/e)", "B/C (tau/mu)"))
    print(fmt.format("", "",
                     f"obs={RATIO_TAU_E:.1f}", f"obs={RATIO_MU_E:.1f}",
                     f"obs={RATIO_TAU_MU:.2f}"))
    print("-" * 78)

    for name, a in exponents.items():
        ba = mass_ratio_from_weights(W_B, W_A, a)
        ca = mass_ratio_from_weights(W_C, W_A, a)
        bc = mass_ratio_from_weights(W_B, W_C, a)
        print(f"{name:<14s} {a:10.4f}   {ba:12.1f} {ca:12.2f} {bc:12.2f}")

    print()


# ── Part 2: best-fit exponent for leptons ─────────────────────────────────────

def part2_best_fit():
    print("=" * 78)
    print("PART 2: Best-fit exponent for lepton mass ratios")
    print("=" * 78)

    # Analytic fit to each ratio independently
    a_tau_e  = fit_exponent_weights(W_B, W_A, RATIO_TAU_E)
    a_mu_e   = fit_exponent_weights(W_C, W_A, RATIO_MU_E)
    a_tau_mu = fit_exponent_weights(W_B, W_C, RATIO_TAU_MU)

    print(f"\n  Exponent from tau/e  = ln({RATIO_TAU_E:.1f})/ln(26) = {a_tau_e:.6f}")
    print(f"  Exponent from mu/e   = ln({RATIO_MU_E:.1f})/ln(7)   = {a_mu_e:.6f}")
    print(f"  Exponent from tau/mu = ln({RATIO_TAU_MU:.2f})/ln(26/7) = {a_tau_mu:.6f}")

    # Numerical best fit (minimise chi2 over exponent)
    best_a = a_tau_e  # start
    step = 0.001
    for _ in range(5):
        while chi2_lepton(best_a + step) < chi2_lepton(best_a):
            best_a += step
        while chi2_lepton(best_a - step) < chi2_lepton(best_a):
            best_a -= step
        step /= 10.0

    pred_tau_e = mass_ratio_from_weights(W_B, W_A, best_a)
    pred_mu_e  = mass_ratio_from_weights(W_C, W_A, best_a)
    pred_tau_mu = mass_ratio_from_weights(W_B, W_C, best_a)

    print(f"\n  Best-fit exponent (min chi2 on log ratios): a = {best_a:.6f}")
    print(f"    Predicted tau/e  = {pred_tau_e:.1f}   (observed {RATIO_TAU_E:.1f},"
          f"  error {100*(pred_tau_e/RATIO_TAU_E - 1):+.1f}%)")
    print(f"    Predicted mu/e   = {pred_mu_e:.2f}  (observed {RATIO_MU_E:.1f},"
          f"  error {100*(pred_mu_e/RATIO_MU_E - 1):+.1f}%)")
    print(f"    Predicted tau/mu = {pred_tau_mu:.2f}  (observed {RATIO_TAU_MU:.2f},"
          f"  error {100*(pred_tau_mu/RATIO_TAU_MU - 1):+.1f}%)")

    # Check proximity to notable values
    print(f"\n  Notable comparisons:")
    for name, val in [("sqrt(5)", SQRT5), ("5/2", 2.5), ("ln(phi^2)", LN_PHI_SQ),
                      ("d=3", 3.0), ("phi", PHI), ("e", math.e),
                      ("phi+1=phi^2", PHI_SQ), ("2*ln(phi^2)", 2*LN_PHI_SQ)]:
        print(f"    {name:20s} = {val:.6f}   delta = {best_a - val:+.6f}")

    print()
    return best_a


# ── Part 3: quark predictions ────────────────────────────────────────────────

def part3_quark_predictions(lepton_a):
    print("=" * 78)
    print("PART 3: Quark mass ratio predictions from lepton best-fit exponent")
    print("=" * 78)

    # Down-type quarks
    print(f"\n  Down-type quarks (b, s, d) — using lepton exponent a = {lepton_a:.4f}")
    pred_b_d = mass_ratio_from_weights(W_B, W_A, lepton_a)
    pred_s_d = mass_ratio_from_weights(W_C, W_A, lepton_a)
    pred_b_s = mass_ratio_from_weights(W_B, W_C, lepton_a)

    fmt = "    {:<12s}  predicted = {:>10.1f}   observed = {:>10.1f}   ratio = {:.3f}"
    print(fmt.format("m_b/m_d", pred_b_d, RATIO_B_D, pred_b_d / RATIO_B_D))
    print(fmt.format("m_s/m_d", pred_s_d, RATIO_S_D, pred_s_d / RATIO_S_D))
    print(fmt.format("m_b/m_s", pred_b_s, RATIO_B_S, pred_b_s / RATIO_B_S))

    # Best-fit exponent for down-type quarks
    a_down = fit_exponent_weights(W_B, W_A, RATIO_B_D)
    print(f"\n    Best-fit exponent for down-type: a_down = {a_down:.6f}")

    # Up-type quarks
    print(f"\n  Up-type quarks (t, c, u) — using lepton exponent a = {lepton_a:.4f}")
    pred_t_u = mass_ratio_from_weights(W_B, W_A, lepton_a)
    pred_c_u = mass_ratio_from_weights(W_C, W_A, lepton_a)
    pred_t_c = mass_ratio_from_weights(W_B, W_C, lepton_a)

    print(fmt.format("m_t/m_u", pred_t_u, RATIO_T_U, pred_t_u / RATIO_T_U))
    print(fmt.format("m_c/m_u", pred_c_u, RATIO_C_U, pred_c_u / RATIO_C_U))
    print(fmt.format("m_t/m_c", pred_t_c, RATIO_T_C, pred_t_c / RATIO_T_C))

    a_up = fit_exponent_weights(W_B, W_A, RATIO_T_U)
    print(f"\n    Best-fit exponent for up-type: a_up = {a_up:.6f}")

    # Sector-specific exponents table
    print(f"\n  Sector-specific best-fit exponents (from heaviest/lightest ratio):")
    print(f"    {'Sector':<14s} {'exponent':>10s}   {'ratio ln(26)':>12s}   {'note'}")
    print(f"    {'leptons':<14s} {lepton_a:10.4f}   {lepton_a:.4f}")
    print(f"    {'down quarks':<14s} {a_down:10.4f}   {a_down:.4f}")
    print(f"    {'up quarks':<14s} {a_up:10.4f}   {a_up:.4f}")

    # Check if exponents differ by simple factors
    print(f"\n  Exponent ratios between sectors:")
    print(f"    a_up / a_lepton  = {a_up / lepton_a:.4f}")
    print(f"    a_down / a_lepton = {a_down / lepton_a:.4f}")
    print(f"    a_up / a_down    = {a_up / a_down:.4f}")

    print()
    return a_down, a_up


# ── Part 4: phi^(2*Delta_n) amplitude picture ────────────────────────────────

def part4_amplitude_picture():
    print("=" * 78)
    print("PART 4: Amplitude contraction per Fibonacci level")
    print("        phi^(2*Dn) = mass ratio  =>  Dn = ln(ratio) / (2*ln(phi))")
    print("=" * 78)

    ln_phi = math.log(PHI)

    ratios = {
        "tau/e   (lepton)":   RATIO_TAU_E,
        "mu/e    (lepton)":   RATIO_MU_E,
        "tau/mu  (lepton)":   RATIO_TAU_MU,
        "b/d     (down-q)":   RATIO_B_D,
        "s/d     (down-q)":   RATIO_S_D,
        "b/s     (down-q)":   RATIO_B_S,
        "t/u     (up-q)":     RATIO_T_U,
        "c/u     (up-q)":     RATIO_C_U,
        "t/c     (up-q)":     RATIO_T_C,
    }

    fmt = "  {:<22s}  ratio = {:>10.1f}   Dn = {:>8.4f}   nearest = {:>6s}   error = {:>+7.2f}%"
    print()

    for name, ratio in ratios.items():
        dn = math.log(ratio) / (2 * ln_phi)

        # Find nearest simple fraction (denominator up to 6)
        best_frac = None
        best_err = float('inf')
        for denom in range(1, 7):
            numer = round(dn * denom)
            if numer > 0:
                frac_val = numer / denom
                err = abs(dn - frac_val)
                if err < best_err:
                    best_err = err
                    best_frac = f"{numer}/{denom}" if denom > 1 else str(numer)
                    best_frac_val = frac_val

        pct_err = 100 * (best_frac_val - dn) / dn if dn != 0 else 0
        print(fmt.format(name, ratio, dn, best_frac, pct_err))

    # Direct check: are lepton Dn values separated by integers?
    dn_tau_e = math.log(RATIO_TAU_E) / (2 * ln_phi)
    dn_mu_e  = math.log(RATIO_MU_E) / (2 * ln_phi)
    dn_tau_mu = math.log(RATIO_TAU_MU) / (2 * ln_phi)

    print(f"\n  Lepton Dn values:")
    print(f"    Dn(tau/e)  = {dn_tau_e:.4f}")
    print(f"    Dn(mu/e)   = {dn_mu_e:.4f}")
    print(f"    Dn(tau/mu) = {dn_tau_mu:.4f}")
    print(f"    Check: Dn(tau/e) = Dn(mu/e) + Dn(tau/mu) = {dn_mu_e + dn_tau_mu:.4f}")

    # Alternative: contraction per level is phi^2 but mass ~ phi^(2n * alpha)
    print(f"\n  If mass = phi^(2*n*alpha) for some sector-dependent alpha:")
    for name, ratio, w_ratio in [
        ("lepton", RATIO_TAU_E, W_B / W_A),
        ("down-q", RATIO_B_D,   W_B / W_A),
        ("up-q",   RATIO_T_U,   W_B / W_A),
    ]:
        dn = math.log(ratio) / (2 * ln_phi)
        dn_weight = math.log(w_ratio) / (2 * ln_phi)
        alpha = dn / dn_weight if dn_weight != 0 else 0
        print(f"    {name:<10s}: Dn={dn:.4f}, Dn_weight={dn_weight:.4f}, alpha={alpha:.4f}")

    print()


# ── Part 5: Summary ──────────────────────────────────────────────────────────

def part5_summary(lepton_a, a_down, a_up):
    print("=" * 78)
    print("SUMMARY")
    print("=" * 78)

    print(f"""
  Phase-state weights:  B=26, C=7, A=1  (from duty/gap at q=2,3)

  Model: m_heavy/m_light = (W_heavy / W_light)^a

  Best-fit exponents by sector:
    Leptons:      a = {lepton_a:.4f}
    Down quarks:  a = {a_down:.4f}    (ratio to lepton: {a_down/lepton_a:.3f})
    Up quarks:    a = {a_up:.4f}    (ratio to lepton: {a_up/lepton_a:.3f})

  Key weight ratios:
    B/A = 26    B/C = 26/7    C/A = 7
    ln(26) = {math.log(26):.4f}    ln(7) = {math.log(7):.4f}    ln(26/7) = {math.log(26/7):.4f}

  The exponent increases from leptons to up-quarks, consistent with
  stronger coupling sectors requiring deeper tree traversal.
  The ratio a_up/a_lepton ~ {a_up/lepton_a:.2f} suggests the exponent
  scales with something like the number of color charges (3) or
  the SU(3) Casimir.
""")


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    part1_fixed_exponents()
    lepton_a = part2_best_fit()
    a_down, a_up = part3_quark_predictions(lepton_a)
    part4_amplitude_picture()
    part5_summary(lepton_a, a_down, a_up)
