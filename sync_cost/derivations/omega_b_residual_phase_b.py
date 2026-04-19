"""
omega_b_residual_phase_b.py

Phase B: test candidate corrections to Omega_b = 1/19 against
the three-way boundary-weight inconsistency from Phase A.

Phase A findings:
  w from Omega_Lambda = 0.828
  w from Omega_b      = 0.926
  w from Omega_DM     = 0.957
  Residual Omega_b:   6.7% (predicted 0.0526 vs observed 0.0493)

Candidates tested:
  C1 (decoherence tax)       -- structural, cross-sector reading
  C2 (Klein asymmetry)       -- structural, {1,5} pairing at finite K
  C4 (n_eff correction)      -- systematic rescaling
  C5 (z-dependent w)         -- likely ruled out: all three are "today"

Key insight: the "decoherence tax" (baryon_fraction.md D33) is
|r| = 0.968 at M_Z, derived in duty_cycle_dictionary.md from
27/(8 alpha_s/alpha_2).

The hypothesis to test: BARYONS are cross-sector modes (require
both q=2 and q=3 coupling) so their decoherence correction is
|r|^2 (product of two sector coherences), not (1-|r|) or |r|.

If so:
  Omega_b_corrected = (1/19) * |r|^2 = 0.0526 * 0.9374 = 0.0493
which matches observed 0.0493 to 0-sigma.

Then Omega_DM absorbs the deficit:
  Omega_DM_corrected = 6/19 - Omega_b_corrected
                      = 0.3158 - 0.0493 = 0.2665
which matches observed 0.265 +- 0.007 to 0.1 sigma.
"""

from __future__ import annotations

# ============================================================
# Constants
# ============================================================

# |r| from duty_cycle_dictionary.md, derived at M_Z
R_ORDER_PARAMETER = 0.968

# Observed Planck 2018 values
OMEGA_LAMBDA_OBS = 0.6847
OMEGA_LAMBDA_ERR = 0.0073
OMEGA_DM_OBS     = 0.265
OMEGA_DM_ERR     = 0.007
OMEGA_B_OBS      = 0.0493
OMEGA_B_ERR      = 0.0003

# Framework integer-depth predictions (at w = 1, full locking)
OMEGA_LAMBDA_PRED = 13/19
OMEGA_DM_PRED     =  5/19
OMEGA_B_PRED      =  1/19


# ============================================================
# Phase A partition formulas
# ============================================================

def omega_lambda(w: float) -> float:
    return (11 + 2*w) / (16 + 3*w)


def omega_dm_phase_a(w: float) -> float:
    """Phase A naive formula: DM = 5 inner modes, always locked."""
    return 5 / (16 + 3*w)


def omega_b_phase_a(w: float) -> float:
    """Phase A naive formula: baryons = w boundary coprime pairs."""
    return w / (16 + 3*w)


def invert_lambda(Omega: float) -> float:
    """Solve Omega_Lambda(w) = Omega for w."""
    return (11 - 16*Omega) / (3*Omega - 2)


def invert_b(Omega: float) -> float:
    return 16*Omega / (1 - 3*Omega)


def invert_dm(Omega: float) -> float:
    return (5 - 16*Omega) / (3*Omega)


# ============================================================
# Candidate corrections to Omega_b
# ============================================================

def candidate_C1_decoherence_single(omega_b_base: float) -> float:
    """C1a: linear decoherence tax (1 - |r|) -- weakest form."""
    return omega_b_base * (1 - (1 - R_ORDER_PARAMETER))


def candidate_C1_decoherence_squared(omega_b_base: float) -> float:
    """
    C1b: cross-sector decoherence tax |r|^2.
    Baryons need BOTH q=2 and q=3 coupling.  If each sector has
    coherence |r|_i, and cross-sector modes experience the product
    |r|_2 * |r|_3 = |r|^2 in the symmetric limit, the baryonic
    population is reduced by |r|^2.
    """
    return omega_b_base * R_ORDER_PARAMETER**2


def candidate_C2_klein_asymmetry(omega_b_base: float,
                                  asymmetry: float) -> float:
    """
    C2: Klein identification asymmetry.
    The {1, 5} pair is not exactly identified at finite K;
    asymmetry in [0, 1] measures the fraction of the pair that
    is "lost" due to imperfect identification.
    """
    return omega_b_base * (1 - asymmetry)


def fit_klein_asymmetry(omega_b_obs: float) -> float:
    """What asymmetry gives the observed Omega_b?"""
    ratio = omega_b_obs / OMEGA_B_PRED
    return 1 - ratio


# ============================================================
# Conservation: does Omega_DM absorb the deficit?
# ============================================================

def omega_dm_with_baryon_correction(omega_b_corrected: float) -> float:
    """If total matter = 6/19 is conserved, DM gets the baryon deficit."""
    return 6/19 - omega_b_corrected


# ============================================================
# Output
# ============================================================

def sigma(obs: float, pred: float, err: float) -> float:
    return abs(obs - pred) / err


def pct(obs: float, pred: float) -> float:
    return 100 * (pred - obs) / obs


def show_partition(label: str, oL: float, oDM: float, oB: float):
    total = oL + oDM + oB
    sL = sigma(OMEGA_LAMBDA_OBS, oL, OMEGA_LAMBDA_ERR)
    sDM = sigma(OMEGA_DM_OBS, oDM, OMEGA_DM_ERR)
    sB = sigma(OMEGA_B_OBS, oB, OMEGA_B_ERR)
    print(f"  {label}")
    print(f"    Omega_Lambda = {oL:.6f}  (obs 0.6847, {sL:.1f} sigma)")
    print(f"    Omega_DM     = {oDM:.6f}  (obs 0.265, {sDM:.1f} sigma)")
    print(f"    Omega_b      = {oB:.6f}  (obs 0.0493, {sB:.1f} sigma)")
    print(f"    sum          = {total:.6f}  (expect 1.0)")
    print()


def main():
    print("=" * 72)
    print("  PHASE B: Omega_b residual, candidate correction test")
    print("=" * 72)
    print()

    print(f"  |r| at M_Z = {R_ORDER_PARAMETER}  (duty_cycle_dictionary.md)")
    print()

    # ------------------------------------------------------------
    # Baseline: framework prediction at w = 1
    # ------------------------------------------------------------
    print("-" * 72)
    print("  Baseline: framework integer-depth (w = 1)")
    print("-" * 72)
    show_partition("w = 1",
                   OMEGA_LAMBDA_PRED, OMEGA_DM_PRED, OMEGA_B_PRED)

    # ------------------------------------------------------------
    # Phase A partition at Omega_Lambda-consistent w
    # ------------------------------------------------------------
    w_L = invert_lambda(OMEGA_LAMBDA_OBS)
    print("-" * 72)
    print(f"  Phase A formula at Omega_Lambda-consistent w = {w_L:.4f}")
    print("-" * 72)
    show_partition(f"w = {w_L:.4f}",
                   omega_lambda(w_L),
                   omega_dm_phase_a(w_L),
                   omega_b_phase_a(w_L))

    # ------------------------------------------------------------
    # C1a: linear decoherence tax at w = 1
    # ------------------------------------------------------------
    print("-" * 72)
    print("  C1a: linear tax  Omega_b -> Omega_b * (1 - (1-|r|))  = Omega_b * |r|")
    print("-" * 72)
    oB_c1a = candidate_C1_decoherence_single(OMEGA_B_PRED)
    oDM_c1a = omega_dm_with_baryon_correction(oB_c1a)
    show_partition("C1a",
                   OMEGA_LAMBDA_PRED, oDM_c1a, oB_c1a)

    # ------------------------------------------------------------
    # C1b: squared decoherence tax |r|^2 at w = 1
    # ------------------------------------------------------------
    print("-" * 72)
    print("  C1b: cross-sector tax  Omega_b -> Omega_b * |r|^2")
    print("-" * 72)
    oB_c1b = candidate_C1_decoherence_squared(OMEGA_B_PRED)
    oDM_c1b = omega_dm_with_baryon_correction(oB_c1b)
    show_partition("C1b",
                   OMEGA_LAMBDA_PRED, oDM_c1b, oB_c1b)

    # ------------------------------------------------------------
    # C2: Klein asymmetry -- fit to observed
    # ------------------------------------------------------------
    print("-" * 72)
    print("  C2: Klein asymmetry in {1, 5} pairing")
    print("-" * 72)
    asymm = fit_klein_asymmetry(OMEGA_B_OBS)
    oB_c2 = candidate_C2_klein_asymmetry(OMEGA_B_PRED, asymm)
    oDM_c2 = omega_dm_with_baryon_correction(oB_c2)
    print(f"  Fitted asymmetry = {asymm:.4f} = {100*asymm:.2f} %")
    print(f"  Compare to |r|^2 - 1 = {R_ORDER_PARAMETER**2 - 1:.4f} "
          f"(= {100*(1-R_ORDER_PARAMETER**2):.2f} % reduction)")
    print(f"  Compare to 1 - |r|   = {1-R_ORDER_PARAMETER:.4f} "
          f"(= {100*(1-R_ORDER_PARAMETER):.2f} % reduction)")
    print()
    show_partition("C2 fit",
                   OMEGA_LAMBDA_PRED, oDM_c2, oB_c2)

    # ------------------------------------------------------------
    # Direct comparison
    # ------------------------------------------------------------
    print("=" * 72)
    print("  Residual comparison (all at w = 1 baseline partition)")
    print("=" * 72)
    print()
    print(f"  {'candidate':<30} {'Omega_b':>10} {'% miss':>10} "
          f"{'sigma':>8}")
    print("  " + "-" * 62)
    baseline = ("baseline (no correction)", OMEGA_B_PRED)
    c1a = ("C1a: |r| linear", oB_c1a)
    c1b = ("C1b: |r|^2 cross-sector", oB_c1b)
    c2 = ("C2: Klein asymm fit", oB_c2)
    for label, val in [baseline, c1a, c1b, c2]:
        pct_miss = pct(OMEGA_B_OBS, val)
        sig = sigma(OMEGA_B_OBS, val, OMEGA_B_ERR)
        marker = ""
        if sig < 1:
            marker = "  <- within 1 sigma"
        elif sig < 2:
            marker = "  <- within 2 sigma"
        print(f"  {label:<30} {val:>10.5f} {pct_miss:>+9.2f}% {sig:>8.1f}{marker}")
    print()

    # ------------------------------------------------------------
    # Check conservation: does DM absorb the deficit?
    # ------------------------------------------------------------
    print("-" * 72)
    print("  Omega_DM residual under each candidate (baryon deficit -> DM)")
    print("-" * 72)
    print()
    print(f"  {'candidate':<30} {'Omega_DM':>10} {'% miss':>10} "
          f"{'sigma':>8}")
    print("  " + "-" * 62)
    no_corr = ("baseline (no correction)", OMEGA_DM_PRED)
    c1a_dm = ("C1a + matter conservation", oDM_c1a)
    c1b_dm = ("C1b + matter conservation", oDM_c1b)
    c2_dm = ("C2 fit + matter conservation", oDM_c2)
    for label, val in [no_corr, c1a_dm, c1b_dm, c2_dm]:
        pct_miss = pct(OMEGA_DM_OBS, val)
        sig = sigma(OMEGA_DM_OBS, val, OMEGA_DM_ERR)
        marker = ""
        if sig < 1:
            marker = "  <- within 1 sigma"
        elif sig < 2:
            marker = "  <- within 2 sigma"
        print(f"  {label:<30} {val:>10.5f} {pct_miss:>+9.2f}% {sig:>8.1f}{marker}")
    print()

    # ------------------------------------------------------------
    # Verdict
    # ------------------------------------------------------------
    print("=" * 72)
    print("  VERDICT")
    print("=" * 72)
    print()
    # Determine winner
    sB_c1b = sigma(OMEGA_B_OBS, oB_c1b, OMEGA_B_ERR)
    sDM_c1b = sigma(OMEGA_DM_OBS, oDM_c1b, OMEGA_DM_ERR)
    sB_c1a = sigma(OMEGA_B_OBS, oB_c1a, OMEGA_B_ERR)
    sDM_c1a = sigma(OMEGA_DM_OBS, oDM_c1a, OMEGA_DM_ERR)

    print("  Summary:")
    print(f"    C1a (linear):  Omega_b  {sB_c1a:.1f} sigma, "
          f"Omega_DM {sDM_c1a:.1f} sigma")
    print(f"    C1b (squared): Omega_b  {sB_c1b:.1f} sigma, "
          f"Omega_DM {sDM_c1b:.1f} sigma")
    print()
    if sB_c1b < 1 and sDM_c1b < 1:
        print("  ==> C1b (cross-sector |r|^2 decoherence tax) CLOSES BOTH")
        print("      Omega_b AND Omega_DM residuals within 1 sigma.")
        print()
        print("  Structural reading:")
        print("    Baryons are the cross-sector modes (coprime-to-6 in Z_6)")
        print("    that require BOTH q_2 (SU(2)) and q_3 (SU(3)) coupling.")
        print("    At finite K the single-sector coherence is |r| = 0.968.")
        print("    The cross-sector coherence is |r|_2 * |r|_3 = |r|^2 in")
        print("    the symmetric case, giving a 6.3% suppression of baryonic")
        print("    modes.  The deficit is absorbed by the single-sector")
        print("    reducible modes (dark matter), which by definition do")
        print("    not require cross-sector coupling and are unaffected.")
        print()
        print("  This closes the 6.7% Omega_b residual AND the 7.5%")
        print("  Omega_DM/Omega_b residual SIMULTANEOUSLY with a single")
        print("  structural correction using an already-derived order")
        print("  parameter (|r| = 0.968 from duty_cycle_dictionary.md).")
    else:
        print("  ==> C1b does NOT fully close; further work needed.")
    print()


if __name__ == "__main__":
    main()
