"""
a_s_phase0.py

Numerical companion to `a_s_phase0.md`.  Derives A_s from the
framework's Lagrangian (framework_lagrangian.py) instead of from
sigma_squared.py's heuristic.

Chain:

  m       = (1 - phi^{-4}) / lambda_unlock           (Madelung, PROOF_B Q4)
  R       = sqrt(m) * delta_theta                    (canonical normalization)
  <R^2>   = m * sigma^2_kernel * bracket_width
          = m * (1/4) * 1/(phi q^2)
  A_s     = (1 - phi^{-4}) / (4 lambda_unlock * phi * q_pivot^2)

At q_pivot = F_21 = 10946:  A_s_pred = 2.33e-9 vs A_s_obs = 2.10e-9
                            Relative deviation ~ 11% (%-only, NOT sigma-closed)

Run:
    python3 sync_cost/derivations/a_s_phase0.py
"""

from __future__ import annotations

import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from framework_constants import LAMBDA_UNLOCK

PHI = (1 + math.sqrt(5)) / 2
A_S_OBS = 2.10e-9
A_S_OBS_ERR = 0.03e-9       # Planck 2018 1-sigma
SIGMA_SQ_KERNEL = 0.25      # ADM closure; continuum_limits.md Sec 5a


def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def m_in_planck_units(lambda_value: float = LAMBDA_UNLOCK) -> float:
    """m / m_P = (1 - phi^{-4}) / lambda_unlock."""
    return (1 - 1 / PHI ** 4) / lambda_value


def a_s_canonical(q_pivot: int,
                  lambda_value: float = LAMBDA_UNLOCK) -> float:
    """A_s_predicted = (1 - phi^{-4}) / (4 lambda phi q^2).

    Equivalent: m * sigma^2_kernel * bracket_width with
    bracket_width = 1/(phi q^2), m = (1 - phi^{-4})/lambda.
    """
    return (1 - 1 / PHI ** 4) / (4 * lambda_value * PHI * q_pivot ** 2)


def main() -> None:
    print("=" * 72)
    print("  A_s PHASE 0: derived from the framework Lagrangian")
    print("=" * 72)

    # --- Step 1: derive m from Madelung
    m = m_in_planck_units()
    m_asymp = m_in_planck_units(2 * 0.9159655942 / math.pi)

    print()
    print("Step 1: m from PROOF_B Q4 (Madelung identification)")
    print("-" * 72)
    print(f"  hbar = 2 m D_eff,  D_eff = D_0 / (1 - phi^{{-4}})")
    print(f"  D_0 = (lambda/2) ell_P^2 / t_P")
    print(f"  =>  m / m_P = (1 - phi^{{-4}}) / lambda_unlock")
    print()
    print(f"  With lambda_unlock = {LAMBDA_UNLOCK} (K=1 numerical, framework canonical):")
    print(f"    m / m_P = {(1 - 1/PHI**4):.6f} / {LAMBDA_UNLOCK} = {m:.4f}")
    print(f"  With lambda_asymp = 2 Catalan/pi = 0.5829 (large-K limit):")
    print(f"    m / m_P = {(1 - 1/PHI**4):.6f} / 0.5829 = {m_asymp:.4f}")
    print()

    # --- Step 2: variance per pivot bracket
    q_pivot = fib(21)
    bracket = 1 / (PHI * q_pivot ** 2)
    var_per_bracket = SIGMA_SQ_KERNEL * bracket

    print("Step 2: phase variance per pivot bracket")
    print("-" * 72)
    print(f"  q_pivot = F_21 = {q_pivot}")
    print(f"  bracket_width = 1/(phi q^2) = {bracket:.4e}")
    print(f"  sigma^2_kernel = 1/4")
    print(f"  <delta_theta^2>_bracket = sigma^2_kernel * bracket = {var_per_bracket:.4e}")
    print()

    # --- Step 3: canonical R
    R_sq_per_bracket = m * var_per_bracket
    print("Step 3: canonical R = sqrt(m) * delta_theta")
    print("-" * 72)
    print(f"  <R^2>_bracket = m * <delta_theta^2>_bracket")
    print(f"                = {m:.4f} * {var_per_bracket:.4e}")
    print(f"                = {R_sq_per_bracket:.4e}")
    print()

    # --- Step 4: A_s prediction
    A_s_pred = a_s_canonical(q_pivot, LAMBDA_UNLOCK)
    A_s_pred_asymp = a_s_canonical(q_pivot, 2 * 0.9159655942 / math.pi)

    print("Step 4: A_s prediction")
    print("-" * 72)
    print(f"  A_s = (1-phi^-4) / (4 lambda phi q^2)")
    print(f"      = {A_s_pred:.4e}    [lambda = {LAMBDA_UNLOCK}, K=1]")
    print(f"      = {A_s_pred_asymp:.4e}    [lambda = 0.5829, asymptotic]")
    print()

    # --- Comparison
    print("=" * 72)
    print("  COMPARISON")
    print("=" * 72)
    rel_dev = abs(A_s_pred - A_S_OBS) / A_S_OBS * 100
    rel_dev_asymp = abs(A_s_pred_asymp - A_S_OBS) / A_S_OBS * 100
    sigma_K1 = abs(A_s_pred - A_S_OBS) / A_S_OBS_ERR
    sigma_asymp = abs(A_s_pred_asymp - A_S_OBS) / A_S_OBS_ERR

    print(f"\n  A_s_observed (Planck 2018) = ({A_S_OBS:.2e} +/- {A_S_OBS_ERR:.2e})")
    print()
    print(f"  Reading                 A_s_pred       rel.dev.   z-score")
    print("  " + "-" * 64)
    print(f"  lambda = 0.473  (K=1)   {A_s_pred:9.3e}    {rel_dev:5.1f}%    {sigma_K1:6.1f} sigma")
    print(f"  lambda = 0.583  (asy.)  {A_s_pred_asymp:9.3e}    {rel_dev_asymp:5.1f}%    {sigma_asymp:6.1f} sigma")
    print()
    print(f"  Status: %-only (NOT sigma-closed); same level as PMNS theta_12")
    print(f"  (per mixing_angle_audit.md / statistical_conventions.md).")
    print()
    print(f"  Prior heuristic (sigma_squared.py) was 4.4x off (~330% rel.dev).")
    print(f"  This Phase 0 reduces to ~10% with all factors derived from")
    print(f"  framework axioms (Madelung, ADM, Stern-Brocot, CMB pivot).")


if __name__ == "__main__":
    main()
