"""
a_s_prefactor_check.py

Numerical probe of the A_s prefactor gap flagged in
`a_s_amplitude_audit.md` and `sigma_squared.py` §7.

Evaluates A_s = σ⁴ / (4π² q_pivot²) across the three framework-
natural σ² choices (kernel, K_eff, tree-sum at depth) and the
Fibonacci-convergent pivot levels F_19, F_20, F_21, F_22.

No prefactor closure is attempted here. Output is the ratio
predicted/observed for each (σ², q_pivot) combination, so the
residual factor can be read off directly.

Run:
    python3 sync_cost/derivations/a_s_prefactor_check.py
"""

from __future__ import annotations

import math
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

A_S_OBS = 2.1e-9                  # Planck 2018, k_pivot = 0.05 Mpc^-1


def fibonacci(n: int) -> int:
    """F_0 = 0, F_1 = 1, ..., F_22 = 17711."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def sum_inv_q_sq_stern_brocot(max_depth: int) -> float:
    """Σ 1/q² over the Stern-Brocot tree of the given depth.

    Matches alphabet_depth21.py's recursion (without the 1/q³ term).
    """
    total = [0.0]

    def recurse(a_num: int, a_den: int,
                c_num: int, c_den: int,
                depth: int) -> None:
        if depth <= 0:
            return
        p = a_num + c_num
        q = a_den + c_den
        total[0] += 1.0 / (q * q)
        recurse(a_num, a_den, p, q, depth - 1)
        recurse(p, q, c_num, c_den, depth - 1)

    recurse(0, 1, 1, 1, max_depth)
    return total[0]


def a_s_predicted(sigma_sq: float, q_pivot: int) -> float:
    """A_s prediction from the sigma_squared.py Route-2 formula."""
    return sigma_sq ** 2 / (4 * math.pi ** 2 * q_pivot * q_pivot)


def main() -> None:
    print("=" * 72)
    print("  A_s PREFACTOR CHECK")
    print(f"  observed A_s = {A_S_OBS:.2e} (Planck 2018)")
    print(f"  formula: A_s = sigma^4 / (4 pi^2 q_pivot^2)")
    print("=" * 72)

    # --- sigma^2 choices ---
    sigma_kernel = 1.0 / 4.0          # adm_prefactor_verification.py
    K_eff = 3.0 / 2.0                 # sigma_squared.py, K_eff at Hubble

    # Compute sigma^2(d) on the tree for a moderate depth.
    # Depth 12 is tractable (< 1 s); depth 21 is ~2 minutes. Choose 12
    # to keep this script fast. The value at d=21 is quoted in the
    # audit doc.
    DEPTH = 12
    s_sum = sum_inv_q_sq_stern_brocot(DEPTH)
    sigma_sq_tree = 1.0 / s_sum

    print(f"\n  sigma^2 choices:")
    print(f"    sigma^2_kernel = 1/4               = {sigma_kernel:.6f}")
    print(f"    K_eff (natural units)              = {K_eff:.6f}")
    print(f"    sigma^2(d={DEPTH}) on SB tree = 1/S_2  = {sigma_sq_tree:.6f}")

    # --- pivot choices ---
    pivots = [(n, fibonacci(n)) for n in (19, 20, 21, 22)]
    print(f"\n  Fibonacci pivots: " + ", ".join(
        f"F_{n}={q}" for n, q in pivots
    ))

    # --- predict A_s for each (sigma^2, pivot) combination ---
    print()
    print(f"  {'sigma^2':>24s}  {'F_19':>12s}  {'F_20':>12s}  "
          f"{'F_21':>12s}  {'F_22':>12s}")
    print("  " + "-" * 80)

    for label, sigma_sq in [
        ("sigma^2_kernel = 1/4", sigma_kernel),
        ("K_eff = 3/2",          K_eff),
        (f"sigma^2(d={DEPTH})",  sigma_sq_tree),
    ]:
        predictions = [
            a_s_predicted(sigma_sq, q) for _, q in pivots
        ]
        cells = "  ".join(f"{p:12.3e}" for p in predictions)
        print(f"  {label:>24s}  {cells}")

    # --- ratios to observed ---
    print()
    print(f"  Ratio (observed / predicted):")
    print(f"  {'sigma^2':>24s}  {'F_19':>12s}  {'F_20':>12s}  "
          f"{'F_21':>12s}  {'F_22':>12s}")
    print("  " + "-" * 80)

    for label, sigma_sq in [
        ("sigma^2_kernel = 1/4", sigma_kernel),
        ("K_eff = 3/2",          K_eff),
        (f"sigma^2(d={DEPTH})",  sigma_sq_tree),
    ]:
        ratios = [
            A_S_OBS / a_s_predicted(sigma_sq, q) for _, q in pivots
        ]
        cells = "  ".join(f"{r:12.3f}" for r in ratios)
        print(f"  {label:>24s}  {cells}")

    # --- commentary ---
    print()
    print("  " + "-" * 70)
    print(f"""
  OBSERVATION:
    With sigma^2 = K_eff = 3/2 and q_pivot = F_21 = 10946, the
    prediction is 4.41x too small.  Observed A_s = {A_S_OBS:.2e} falls
    between F_19 (ratio 0.64, i.e. 1.55x too large) and F_20
    (ratio 1.69, i.e. 1.69x too small).

    The formula has no framework-level closure of its prefactor.
    The missing factor is of order (a few), scale-free, with no
    current derivation.

    Candidates (numerology, not derivations):
      4 pi / 3    = {4*math.pi/3:.4f}   (volume factor of unit 3-sphere)
      e * phi     = {math.e * (1+math.sqrt(5))/2:.4f}

    Either would bring K_eff = 3/2 at q_pivot = F_21 into agreement
    with observation at the 1-5% level, but neither is derived.

  NEXT STEPS (per a_s_amplitude_audit.md):
    1. Derive the k-space mode density in the tree parameterization
       (unit-volume factor). ~1 session.
    2. Close A_s from the Kuramoto fluctuation spectrum at the pivot
       via <delta phi^2> = g(omega) / (K r)^2.  Multi-session.

    Route 1 of the audit (attribution recovery) has been **ruled out**:
    sigma_squared.py's "Derivation 12 Part I Sec 7" pointer goes to
    continuum_limits.md Sec 5a, which closes the ADM prefactor
    verification -- a different problem.  The A_s unit-conversion
    prefactor has no prior closure.
""")


if __name__ == "__main__":
    main()
