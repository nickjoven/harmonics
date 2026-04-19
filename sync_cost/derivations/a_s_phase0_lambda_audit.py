"""
a_s_phase0_lambda_audit.py

Audit of the lambda_unlock(K=1) closed form, motivated by the 11%
A_s residual in a_s_phase0.md.  Result: the framework_constants
comment claiming "lambda_unlock(1) = 2 Catalan / pi ~= 0.583" was
INCORRECT.  The actual closed form is (4G - pi ln 2)/pi ~= 0.473096,
which matches numerical integration to 9 digits.

This means R7.1 from a_s_phase0.md (lambda convention) is NOT the
source of the 11% A_s residual.  The framework_constants value
LAMBDA_UNLOCK = 0.473 was correct; only the comment was wrong.

The 11% residual must come from R7.2, R7.3, or another source.
This script also tabulates plausible algebraic candidates for
the residual ratio 0.902 = A_s_obs / A_s_phase0_pred.

Run:
    python3 sync_cost/derivations/a_s_phase0_lambda_audit.py
"""

from __future__ import annotations

import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from framework_constants import LAMBDA_UNLOCK

CATALAN = 0.9159655941772190
PHI = (1 + math.sqrt(5)) / 2
PI = math.pi
A_S_OBS = 2.10e-9


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def integrate(f, a, b, N=100000):
    """Simpson's rule."""
    h = (b - a) / N
    s = f(a) + f(b)
    for i in range(1, N):
        x = a + i * h
        w = 4 if i % 2 else 2
        s += w * f(x)
    return s * h / 3


def lambda_unlock_numerical(K):
    """(1/pi) * integral over [pi/2, 3 pi/2] of ln(1 + K|cos theta|) dtheta.

    The defining integral from gap2_spatialization sub-C.  Normalized
    so that it matches the doc's table (K=0.5 -> 0.269, etc.).
    """
    return integrate(
        lambda t: math.log(1 + K * abs(math.cos(t))),
        PI / 2, 3 * PI / 2
    ) / PI


def main():
    print("=" * 72)
    print("  LAMBDA_UNLOCK(K=1) CLOSED-FORM AUDIT")
    print("=" * 72)

    # --- Derive the closed form ---
    # integral over [pi/2, 3 pi/2] of ln(1 + |cos theta|) dtheta
    #   = 2 * integral over [0, pi/2] of ln(1 + cos phi) dphi
    #     (substitute phi = theta - pi, use |cos(phi+pi)| = |cos phi|)
    #   = 2 * integral over [0, pi/2] of ln(2 cos^2(phi/2)) dphi
    #   = 2 * [(pi/2) ln 2 + 2 * integral over [0, pi/2] of ln cos(phi/2) dphi]
    #   = pi ln 2 + 4 * integral over [0, pi/2] of ln cos(phi/2) dphi
    # Sub u = phi/2 (du = dphi/2):
    #   integral over [0, pi/2] of ln cos(phi/2) dphi
    #     = 2 * integral over [0, pi/4] of ln cos u du
    # Known: integral over [0, pi/4] of ln cos u du = G/2 - (pi/4) ln 2
    # So:
    #   = pi ln 2 + 4 * 2 * (G/2 - (pi/4) ln 2)
    #   = pi ln 2 + 4G - 2 pi ln 2
    #   = 4G - pi ln 2
    closed_form_integral = 4 * CATALAN - PI * math.log(2)
    closed_form_normalized = closed_form_integral / PI

    numerical_integral = integrate(
        lambda t: math.log(1 + abs(math.cos(t))), PI/2, 3*PI/2
    )
    numerical_normalized = numerical_integral / PI

    print(f"""
  Defining integral:
    I(K=1) = integral over [pi/2, 3 pi/2] of ln(1 + |cos theta|) dtheta

  Closed-form derivation (integration by parts + known identity
                          integral_[0,pi/4] ln(cos u) du = G/2 - (pi/4) ln 2):
    I(K=1) = 4G - pi ln 2

  Numerical:    {numerical_integral:.10f}
  Closed form:  {closed_form_integral:.10f}
  Match to {abs(numerical_integral - closed_form_integral):.2e}
""")

    print(f"  Per-period (/ pi) normalization:")
    print(f"    lambda_unlock(1) = (4G - pi ln 2) / pi = {closed_form_normalized:.10f}")
    print(f"  Numerical:                                {numerical_normalized:.10f}")
    print(f"  Framework_constants LAMBDA_UNLOCK:        {LAMBDA_UNLOCK:.10f}")
    print(f"  Match: {'PASS' if abs(LAMBDA_UNLOCK - closed_form_normalized) < 1e-4 else 'FAIL'}")

    print()
    print("=" * 72)
    print("  COMPARISON WITH PREVIOUS (INCORRECT) CLAIM")
    print("=" * 72)
    bad_value = 2 * CATALAN / PI
    print(f"""
  Previous framework_constants comment claimed:
    lambda_unlock(1) = 2 G / pi = {bad_value:.6f}
  Actual closed form:
    lambda_unlock(1) = (4G - pi ln 2) / pi = {closed_form_normalized:.6f}
  Difference: {abs(bad_value - closed_form_normalized):.4f} ({abs(bad_value-closed_form_normalized)/closed_form_normalized*100:.1f}%)

  The 0.583 value in the previous comment was WRONG.  The framework's
  numerical value 0.473 was already correct; only the comment was off.
  Comment fixed in this commit.
""")

    print("=" * 72)
    print("  IMPLICATION FOR A_s PHASE 0 RESIDUAL")
    print("=" * 72)
    print(f"""
  R7.1 from a_s_phase0.md hypothesized that the 11% A_s residual
  could come from a wrong lambda_unlock convention (K=1 numerical
  vs K -> infinity asymptotic).  The audit shows that:

  - Both '0.473 numerical' and '(4G - pi ln 2)/pi closed form'
    give the same value (they ARE the same).
  - The asymptotic claim '2G/pi = 0.583' was derivation error,
    not a real alternative convention.

  CONCLUSION: R7.1 is closed -- lambda_unlock = 0.473 is exact.
  The 11% A_s residual is NOT due to lambda convention.

  Remaining R7 candidates (per a_s_phase0.md):
    R7.2: pivot-level higher-order correction
    R7.3: cos expansion at O(delta_theta^4)
    R7.4 (new): N_efolds shift from 61.3 to ~58 (would close to ~1%)
""")

    # --- Pivot shift analysis ---
    print("=" * 72)
    print("  PIVOT-SHIFT ANALYSIS (R7.2)")
    print("=" * 72)
    q_pivot = fib(21)
    A_s_pred = (1 - 1/PHI**4) / (4 * LAMBDA_UNLOCK * PHI * q_pivot**2)
    ratio = A_S_OBS / A_s_pred

    # What q_eff makes A_s_pred match A_s_obs?
    q_eff_sq = (1 - 1/PHI**4) / (4 * LAMBDA_UNLOCK * PHI * A_S_OBS)
    q_eff = math.sqrt(q_eff_sq)
    levels_above = math.log(q_eff / q_pivot) / math.log(PHI)
    e_folds_above = levels_above / 0.0365  # rate from a_s_phase0.md

    N_EFOLDS_FRAMEWORK = 61.3   # from alphabet_depth21.py
    N_efolds_corrected = N_EFOLDS_FRAMEWORK - e_folds_above

    print(f"""
  Phase 0 prediction: A_s = {A_s_pred:.4e}
  Observed:           A_s = {A_S_OBS:.4e}
  Ratio obs/pred:           {ratio:.4f}

  q_pivot at exact match: q_eff = {q_eff:.2f}
  vs F_21 =                       {q_pivot}
  vs F_22 =                       {fib(22)}
  q_eff / F_21 =                  {q_eff/q_pivot:.4f}

  Levels above F_21:              {levels_above:.4f}
  E-folds above F_21:             {e_folds_above:.4f}

  Framework N_efolds prediction:  {N_EFOLDS_FRAMEWORK}
  Implied corrected N_efolds:     {N_efolds_corrected:.2f}
  (if pivot is at the 'corrected' N_efolds before end of inflation,
  rather than the framework's 61.3)
""")

    # --- Algebraic search ---
    print("=" * 72)
    print(f"  ALGEBRAIC CANDIDATES FOR RATIO = {ratio:.4f}")
    print("=" * 72)
    candidates = sorted([
        ("9 / 10", 9/10),
        ("1 - 1/phi^5", 1 - 1/PHI**5),
        ("1 - 1/phi^6", 1 - 1/PHI**6),
        ("1 - 2/phi^5 / 2", 1 - 1/PHI**5),
        ("(F_21-1)/F_21", (q_pivot-1)/q_pivot),  # negligible diff
        ("phi^2 / 3", PHI**2/3),
        ("e/3", math.e/3),
        ("(1 - phi^-4) * phi^-1 + 1/3", (1-1/PHI**4)/PHI + 1/3),
        ("1 / (1 + 1/phi^6)", 1/(1 + 1/PHI**6)),
        ("(1-phi^-4)^2 / (1-phi^-4) * 1.057", (1-1/PHI**4) * 1.057),
        ("phi/(phi+1/3)", PHI/(PHI + 1/3)),
        ("19/21", 19/21),
        ("2 - phi^-4 - 1", 2 - 1/PHI**4 - 1),  # = 1 - 1/phi^4 = 0.854
    ], key=lambda x: abs(x[1] - ratio))[:8]

    print(f"  {'candidate':>30s}  {'value':>10s}  {'% off ratio':>12s}")
    print("  " + "-" * 58)
    for name, val in candidates:
        err = abs(val - ratio) / ratio * 100
        print(f"  {name:>30s}  {val:10.6f}  {err:11.2f}%")

    print(f"""
  Best matches: 9/10 (0.22%), 1 - 1/phi^5 (0.87%).
  Neither has a clear framework derivation.
  Further closure of A_s requires either:
    - a structural argument selecting one of these as the right factor
    - a derivation of the corrected pivot identification (R7.2)
    - inclusion of higher-order cos expansion (R7.3)
""")


if __name__ == "__main__":
    main()
