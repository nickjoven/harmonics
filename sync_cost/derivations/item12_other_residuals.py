"""
Item 12 continuation: test Higgs lambda and alpha_s/alpha_2 residuals.

The sin^2(theta_W) residual was found to equal 8/F_10^2 (additive),
where 8 = q_2^3 and F_10 = 55. The lepton C residual was found to
equal (5 + 1/phi^2) * 1/F_10^2 (multiplicative). Both use F_10.

This script checks:
  (1) Higgs quartic lambda: framework 1/8, observed ~0.129
  (2) alpha_s/alpha_2: framework 27/8, observed ~3.49

For each, compute the additive residual and search for
(integer_prefactor)/F_k^2 forms with small integer prefactors and
small Fibonacci indices k. Report the cleanest match per observable.
"""

import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from framework_constants import ALPHA_S_MZ, V_GEV

PHI = (1 + math.sqrt(5)) / 2
Q2, Q3 = 2, 3


def fib(k):
    a, b = 1, 1
    for _ in range(k - 1):
        a, b = b, a + b
    return a


# ============================================================================
# Observed values
# ============================================================================

# Higgs: m_H = 125.25 GeV, v = 246.22 GeV (PDG 2024; framework_constants V_GEV)
M_H = 125.25
LAMBDA_OBS = M_H ** 2 / (2 * V_GEV ** 2)       # ~0.12936
LAMBDA_TREE = 1 / (2 * Q2 ** 2)                 # 1/8 = 0.125

# alpha_s(M_Z), alpha_2(M_Z) from PDG 2024
ALPHA_S = ALPHA_S_MZ                             # PDG 2024 (framework_constants)
ALPHA_2_INV = 29.57                              # sqrt(1/alpha_em) = 137.04, alpha_2 from weak coupling
ALPHA_2 = 1 / ALPHA_2_INV
RATIO_OBS = ALPHA_S / ALPHA_2                    # ~3.487
RATIO_TREE = Q3 ** 3 / Q2 ** 3                    # 27/8 = 3.375


# ============================================================================
# Search for (integer_prefactor)/F_k^2 forms
# ============================================================================

def find_best_simple_form(target, max_k=15, max_prefactor=40):
    """
    Find integer prefactor p and Fibonacci index k such that
    p/F_k^2 is closest to target.
    Returns (p, k, F_k, predicted, rel_err).
    """
    best = None
    for k in range(3, max_k + 1):
        Fk = fib(k)
        for p in range(1, max_prefactor + 1):
            pred = p / (Fk * Fk)
            err = abs(pred - target)
            rel = err / abs(target) if target != 0 else err
            if best is None or rel < best[4]:
                best = (p, k, Fk, pred, rel)
    return best


def main():
    print("=" * 78)
    print("  OTHER RESIDUALS: Higgs lambda, alpha_s/alpha_2")
    print("=" * 78)
    print()

    # ------------------------------------------------------------------
    # Higgs lambda
    # ------------------------------------------------------------------
    print("-" * 78)
    print("  HIGGS QUARTIC lambda = m_H^2 / (2 v^2)")
    print("-" * 78)
    print()
    print(f"  m_H = {M_H} GeV (PDG 2024)")
    print(f"  v   = {V_GEV} GeV")
    print()
    print(f"  Observed  lambda = {LAMBDA_OBS:.6f}")
    print(f"  Tree      lambda = 1/(2 q_2^2) = 1/8 = {LAMBDA_TREE:.6f}")
    print()
    delta_lambda = LAMBDA_OBS - LAMBDA_TREE
    print(f"  Additive residual        = {delta_lambda:.6f}")
    print(f"  Multiplicative residual  = {delta_lambda/LAMBDA_TREE:.6f}")
    print()
    # Find best (p, F_k) for additive residual
    p, k, Fk, pred, rel = find_best_simple_form(delta_lambda)
    print(f"  Best additive fit: {p}/F_{k}^2 = {p}/{Fk}^2 = {pred:.6f}")
    print(f"                     rel err from observed = {rel*100:.3f}%")
    print()
    # Also test multiplicative
    p_m, k_m, Fk_m, pred_m, rel_m = find_best_simple_form(delta_lambda / LAMBDA_TREE)
    print(f"  Best multiplicative fit: {p_m}/F_{k_m}^2 = {p_m}/{Fk_m}^2 "
          f"= {pred_m:.6f}")
    print(f"                           rel err = {rel_m*100:.3f}%")
    print()

    # Predict lambda, m_H using the additive fit
    if rel < 0.02:
        predicted_lambda = LAMBDA_TREE + p / (Fk * Fk)
        predicted_mH = math.sqrt(2 * predicted_lambda * V_GEV ** 2)
        print(f"  PREDICTION: lambda = 1/8 + {p}/F_{k}^2 = {predicted_lambda:.6f}")
        print(f"              m_H = {predicted_mH:.4f} GeV")
        print(f"              observed = {M_H} GeV")
        print(f"              rel err  = {abs(predicted_mH - M_H)/M_H * 100:.4f}%")
        print()
        print(f"  Structural reading of {p}: ", end="")
        if p == Q2 + Q3:
            print("q_2 + q_3 (mediant scale)")
        elif p == Q2 * Q3:
            print("q_2 * q_3 (interaction scale)")
        elif p == Q2 ** 3:
            print("q_2^3 (quark sector constant)")
        elif p == Q3 ** 2:
            print("q_3^2 (lepton sector constant)")
        else:
            print(f"unclear ({p})")
        print(f"  Structural reading of k={k}: ", end="")
        if k == Q3 ** 2:
            print("F_{q_3^2} (Fibonacci at lepton k)")
        elif k == Q2 ** 3:
            print("F_{q_2^3} (Fibonacci at quark k)")
        elif k == 2 * (Q2 + Q3):
            print("F_{2(q_2+q_3)} (twice mediant)")
        elif k == Q2 * (Q2 + Q3):
            print("F_{q_2(q_2+q_3)} (weak * mediant)")
        else:
            print(f"unclear ({k})")

    print()

    # ------------------------------------------------------------------
    # alpha_s / alpha_2
    # ------------------------------------------------------------------
    print("-" * 78)
    print("  alpha_s / alpha_2")
    print("-" * 78)
    print()
    print(f"  alpha_s(M_Z) = {ALPHA_S}  (PDG 2024)")
    print(f"  alpha_2(M_Z) = 1/{ALPHA_2_INV} = {ALPHA_2:.6f}")
    print()
    print(f"  Observed  ratio = {RATIO_OBS:.6f}")
    print(f"  Tree      ratio = q_3^3/q_2^3 = 27/8 = {RATIO_TREE:.6f}")
    print()
    delta_ratio = RATIO_OBS - RATIO_TREE
    print(f"  Additive residual       = {delta_ratio:.6f}")
    print(f"  Multiplicative residual = {delta_ratio/RATIO_TREE:.6f}")
    print()
    p, k, Fk, pred, rel = find_best_simple_form(delta_ratio)
    print(f"  Best additive fit: {p}/F_{k}^2 = {p}/{Fk}^2 = {pred:.6f}")
    print(f"                     rel err = {rel*100:.3f}%")
    print()
    p_m, k_m, Fk_m, pred_m, rel_m = find_best_simple_form(delta_ratio / RATIO_TREE)
    print(f"  Best multiplicative fit: {p_m}/F_{k_m}^2 = {p_m}/{Fk_m}^2 "
          f"= {pred_m:.6f}")
    print(f"                           rel err = {rel_m*100:.3f}%")
    print()

    # ------------------------------------------------------------------
    # Summary table
    # ------------------------------------------------------------------
    print("=" * 78)
    print("  SUMMARY: universal residual structure?")
    print("=" * 78)
    print()
    print("  Each observable has a tree value and an additive residual;")
    print("  we ask whether the residual has a clean form p/F_k^2.")
    print()
    print(f"  {'observable':<20} {'tree':>14} {'residual':>14} "
          f"{'best p/F_k^2':>16} {'rel err':>10}")
    print("  " + "-" * 78)

    observables = [
        ("lepton C",   5 + 1/(PHI*PHI), 0.00179),       # delta additive
        ("sin^2 W",    8/35,            0.00265),
        ("Higgs lambda", 1/8,           delta_lambda),
        ("alpha_s/alpha_2", 27/8,       delta_ratio),
    ]
    for name, tree, res in observables:
        p, k, Fk, pred, rel = find_best_simple_form(res)
        print(f"  {name:<20} {tree:>14.6f} {res:>14.6f} "
              f"{f'{p}/F_{k}^2':>16} {rel*100:>9.3f}%")
    print()


if __name__ == "__main__":
    main()
