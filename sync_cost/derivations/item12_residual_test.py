"""
Item 12, chunk 3a: explain the 0.033% residual on C.

Observed C    = 5.38375497
5 + 1/phi^2   = 5.38196601
Residual delta = +0.00178896 (+0.0332% of observed)

This script tests a handful of natural small-correction candidates
for delta one by one:

  (A) Fibonacci reciprocal squares 1/F_k^2
  (B) Golden-ratio inverse powers 1/phi^k
  (C) Finite-K Kuramoto corrections (1-K*)^k
  (D) Order-parameter corrections (1-|r|)^k

Each candidate is evaluated as both an ADDITIVE correction
(C = 5 + 1/phi^2 + delta) and a MULTIPLICATIVE correction
(C = (5 + 1/phi^2)(1 + epsilon)), because we don't know which
structural form the correction should take.

Goal: find the candidate that matches the observed residual to
within PDG uncertainty on C (about 0.01%) and has a structural
reading in the framework's vocabulary.
"""

import math


# ============================================================================
# Observed values
# ============================================================================

PHI = (1 + math.sqrt(5)) / 2
INV_PHI_SQ = 1 / (PHI * PHI)

C_OBS = 2.320292 ** 2                   # 5.38375497
BASE = 5 + INV_PHI_SQ                   # 5.38196601
DELTA_ABS = C_OBS - BASE                # 0.00178896 (additive)
EPS_REL = DELTA_ABS / BASE              # 0.00033239 (multiplicative)

# Framework constants
K_STAR = 0.862
R_STAR = 0.83
Q2, Q3 = 2, 3


def fib(k):
    a, b = 1, 1
    for _ in range(k - 1):
        a, b = b, a + b
    return a


# ============================================================================
# Candidate correction families
# ============================================================================

def test_fibonacci_reciprocal_squares():
    """1/F_k^2 for k from 3 to 15."""
    print("  Fibonacci reciprocal squares 1/F_k^2:")
    print()
    print(f"    {'k':>3} {'F_k':>6} {'1/F_k^2':>14} "
          f"{'additive res':>14} {'mult res':>14}")
    print("    " + "-" * 58)
    best_add_k, best_add_err = None, float('inf')
    best_mul_k, best_mul_err = None, float('inf')
    for k in range(3, 16):
        Fk = fib(k)
        corr = 1 / (Fk * Fk)
        add_err = abs(corr - DELTA_ABS)
        mul_err = abs(corr - EPS_REL)
        add_rel = add_err / DELTA_ABS * 100
        mul_rel = mul_err / EPS_REL * 100
        add_flag = "*" if add_rel < 5 else ""
        mul_flag = "*" if mul_rel < 5 else ""
        if add_err < best_add_err:
            best_add_err = add_err
            best_add_k = k
        if mul_err < best_mul_err:
            best_mul_err = mul_err
            best_mul_k = k
        print(f"    {k:>3} {Fk:>6} {corr:>14.8f} "
              f"{add_err:>14.8f}{add_flag} {mul_err:>14.8f}{mul_flag}")
    print()
    print(f"  Best additive: k = {best_add_k}, F_{best_add_k} = {fib(best_add_k)}, "
          f"err = {best_add_err:.2e}")
    print(f"  Best multiplicative: k = {best_mul_k}, F_{best_mul_k} = {fib(best_mul_k)}, "
          f"err = {best_mul_err:.2e}")
    print()


def test_golden_powers():
    """1/phi^k for k from 5 to 20."""
    print("  Golden-ratio inverse powers 1/phi^k:")
    print()
    print(f"    {'k':>3} {'1/phi^k':>14} {'additive res':>14} {'mult res':>14}")
    print("    " + "-" * 52)
    best_add_k, best_add_err = None, float('inf')
    best_mul_k, best_mul_err = None, float('inf')
    for k in range(5, 21):
        corr = 1 / (PHI ** k)
        add_err = abs(corr - DELTA_ABS)
        mul_err = abs(corr - EPS_REL)
        add_rel = add_err / DELTA_ABS * 100
        mul_rel = mul_err / EPS_REL * 100
        add_flag = "*" if add_rel < 5 else ""
        mul_flag = "*" if mul_rel < 5 else ""
        if add_err < best_add_err:
            best_add_err = add_err
            best_add_k = k
        if mul_err < best_mul_err:
            best_mul_err = mul_err
            best_mul_k = k
        print(f"    {k:>3} {corr:>14.8f} "
              f"{add_err:>14.8f}{add_flag} {mul_err:>14.8f}{mul_flag}")
    print()
    print(f"  Best additive: k = {best_add_k}, err = {best_add_err:.2e}")
    print(f"  Best multiplicative: k = {best_mul_k}, err = {best_mul_err:.2e}")
    print()


def test_kuramoto_corrections():
    """(1 - K*)^k and (1 - r*)^k for k = 2 to 6."""
    print(f"  Finite-K Kuramoto corrections (K* = {K_STAR}, r* = {R_STAR}):")
    print()
    ks = [2, 3, 4, 5, 6]
    print(f"    {'form':<20} {'value':>14} {'additive res':>14} {'mult res':>14}")
    print("    " + "-" * 64)
    for k in ks:
        val = (1 - K_STAR) ** k
        add_err = abs(val - DELTA_ABS) / DELTA_ABS * 100
        mul_err = abs(val - EPS_REL) / EPS_REL * 100
        add_flag = "*" if add_err < 5 else ""
        mul_flag = "*" if mul_err < 5 else ""
        print(f"    {f'(1-K*)^{k}':<20} {val:>14.8f} "
              f"{val - DELTA_ABS:>+14.8f}{add_flag} "
              f"{val - EPS_REL:>+14.8f}{mul_flag}")
    for k in ks:
        val = (1 - R_STAR) ** k
        add_err = abs(val - DELTA_ABS) / DELTA_ABS * 100
        mul_err = abs(val - EPS_REL) / EPS_REL * 100
        add_flag = "*" if add_err < 5 else ""
        mul_flag = "*" if mul_err < 5 else ""
        print(f"    {f'(1-r*)^{k}':<20} {val:>14.8f} "
              f"{val - DELTA_ABS:>+14.8f}{add_flag} "
              f"{val - EPS_REL:>+14.8f}{mul_flag}")
    print()


# ============================================================================
# Main
# ============================================================================

def main():
    print("=" * 78)
    print("  EXPLAIN THE RESIDUAL ON C")
    print("=" * 78)
    print()
    print(f"  Observed  C            = {C_OBS:.8f}")
    print(f"  Base      5 + 1/phi^2  = {BASE:.8f}")
    print(f"  Additive  delta        = {DELTA_ABS:.8f}")
    print(f"  Multiplicative epsilon = {EPS_REL:.8f}")
    print(f"                         = 1 + {EPS_REL:.6e}")
    print()
    print("  Test candidate corrections against delta (additive) and")
    print("  epsilon (multiplicative). Flagging matches within 5%.")
    print()

    test_fibonacci_reciprocal_squares()
    test_golden_powers()
    test_kuramoto_corrections()

    print("=" * 78)
    print("  VERDICT")
    print("=" * 78)
    print()


if __name__ == "__main__":
    main()
