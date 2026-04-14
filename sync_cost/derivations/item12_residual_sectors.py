"""
Item 12, chunk 3b: does the 1/F_10^2 correction hold for other sectors?

The leptons match C = (5 + 1/phi^2)(1 + 1/F_10^2) to within 2ppm.
Question: does the same form -- or a sector-analog with a different
F_k -- work for up-type and down-type?

Approach: extract the observed "C per sector" by dividing a_1^2 by
the hypothesis sector scaling s(sector), then compare to 5 + 1/phi^2
and look for small-correction candidates.
"""

import math

PHI = (1 + math.sqrt(5)) / 2
INV_PHI_SQ = 1 / (PHI * PHI)
BASE = 5 + INV_PHI_SQ   # 5.38196601
Q2, Q3 = 2, 3


# ============================================================================
# Observed a_1 per sector
# ============================================================================

a1_lep = 2.320292
a1_up  = 3.484290
a1_dn  = 5.678221

# Sector scaling hypothesis: a_1^2 = C * s(sector)
s_lep = 1
s_up  = (Q3 / Q2) ** 2    # 9/4
s_dn  = Q2 * Q3            # 6


def fib(k):
    a, b = 1, 1
    for _ in range(k - 1):
        a, b = b, a + b
    return a


def best_fib_sq_match(eps):
    """
    Find the k with |1/F_k^2 - eps| smallest (for eps > 0).
    Returns (k, F_k, 1/F_k^2, residual).
    """
    best = None
    for k in range(3, 30):
        Fk = fib(k)
        corr = 1 / (Fk * Fk)
        diff = abs(corr - abs(eps))
        if best is None or diff < best[3]:
            best = (k, Fk, corr, diff)
    return best


def main():
    print("=" * 78)
    print("  PER-SECTOR C RESIDUALS")
    print("=" * 78)
    print()
    print(f"  Base hypothesis: C = 5 + 1/phi^2 = {BASE:.8f}")
    print(f"  Scaling hypothesis: a_1(sector)^2 = C * s(sector)")
    print(f"    s(leptons)  = 1")
    print(f"    s(up-type)  = (q_3/q_2)^2 = 9/4")
    print(f"    s(down-type) = q_2 q_3 = 6")
    print()

    sectors = [
        ("leptons", a1_lep, s_lep),
        ("up-type", a1_up,  s_up),
        ("down-type", a1_dn,  s_dn),
    ]

    print(f"  {'sector':<12} {'a_1^2 (obs)':>14} {'s*BASE (pred)':>16} "
          f"{'mult eps':>14} {'best 1/F_k^2':>16} {'k':>4} {'rel err':>10}")
    print("  " + "-" * 92)

    for name, a1, s in sectors:
        a1sq_obs = a1 * a1
        a1sq_pred = s * BASE
        eps = a1sq_obs / a1sq_pred - 1    # multiplicative residual

        k, Fk, corr, diff = best_fib_sq_match(eps)
        rel_err = diff / abs(eps) * 100 if eps != 0 else 0
        sign = "+" if eps > 0 else "-"
        print(f"  {name:<12} {a1sq_obs:>14.6f} {a1sq_pred:>16.6f} "
              f"{sign}{abs(eps):.6f}  {corr:>14.6e}   F_{k:<2} {rel_err:>9.2f}%")

    print()
    print("-" * 78)
    print("  CANDIDATES FOR k = 10 (the lepton result)")
    print("-" * 78)
    print()
    print("  F_10 = 55.")
    print("  What integer combinations of (q_2, q_3) = (2, 3) give 10?")
    print()
    candidates_for_10 = [
        ("2 * (q_2 + q_3)",        2 * (Q2 + Q3),         "twice the mediant scale"),
        ("q_2 * (q_2 + q_3)",      Q2 * (Q2 + Q3),        "weak * mediant"),
        ("q_2^2 + q_2*q_3",        Q2**2 + Q2*Q3,         "weak^2 + interaction"),
        ("q_2^3 + q_2",            Q2**3 + Q2,            "quark constant + weak"),
        ("q_2 + q_3 + q_2 + q_3",  Q2 + Q3 + Q2 + Q3,     "two mediant sums"),
        ("q_2 + q_2*q_3 + q_2",    Q2 + Q2*Q3 + Q2,       "weak + interaction + weak"),
    ]
    for expr, val, meaning in candidates_for_10:
        mark = " *" if val == 10 else "  "
        print(f"    {expr:<28} = {val:>3}   {meaning}{mark}")
    print()
    print("  Multiple simple combinations give 10. Cleanest reading:")
    print("  'twice the mediant scale' (2 * 5) or equivalently")
    print("  'weak times mediant' (q_2 * (q_2+q_3)). Both interpret the")
    print("  Fibonacci index as a scale-doubling of the mediant structure.")
    print()


if __name__ == "__main__":
    main()
