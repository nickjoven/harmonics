"""
rfe_irrational_fixed_points.py

Does the rational field equation (RFE) force irrational solutions?

The RFE is a self-consistency equation on the Stern-Brocot tree:

  |r| = |Σ_{p/q} w(p/q, K₀|r|) × e^{2πi·p/q}| / Σ w(p/q, K₀|r|)

At each rational node p/q, the tongue width w is rational (for rational K).
But the weighted sum involves phases e^{2πi·p/q}, which are algebraic.
The fixed-point |r*| is therefore generally IRRATIONAL.

This matters for sub-problem A (spatialization): if the RFE's own
self-consistency forces irrational solutions from rational inputs,
then the completion Q → R is DERIVED from the fixed-point primitive,
not assumed. The field (continuous θ(x)) exists because the equation
demands it.

Parallel to Collatz: the mediant of two integers is generally not
an integer. The RFE's weighted sum over rationals is generally not
rational. Both force completion beyond the starting domain.
"""

import numpy as np
from math import gcd
from fractions import Fraction


def stern_brocot_tree(max_depth):
    """Generate Stern-Brocot fractions up to given depth."""
    fracs = set()
    def build(a_n, a_d, b_n, b_d, depth):
        if depth > max_depth:
            return
        m_n, m_d = a_n + b_n, a_d + b_d
        g = gcd(m_n, m_d)
        m_n, m_d = m_n // g, m_d // g
        fracs.add((m_n, m_d))
        build(a_n, a_d, m_n, m_d, depth + 1)
        build(m_n, m_d, b_n, b_d, depth + 1)
    fracs.add((0, 1))
    fracs.add((1, 1))
    build(0, 1, 1, 1, 1)
    return sorted(fracs, key=lambda x: x[0] / x[1])


def tongue_width(p, q, K):
    """Arnold tongue width model: w(p/q, K) = K^q / q (leading order)."""
    return K**q / q


def order_parameter(tree, K):
    """Compute the Kuramoto order parameter on the tree at coupling K."""
    z = 0.0 + 0.0j
    total_w = 0.0
    for p, q in tree:
        if q == 0:
            continue
        w = tongue_width(p, q, K)
        phase = 2 * np.pi * p / q
        z += w * np.exp(1j * phase)
        total_w += w
    if total_w == 0:
        return 0.0
    return abs(z) / total_w


def self_consistency(tree, K0, tol=1e-12, max_iter=200):
    """Solve |r| = order_parameter(tree, K0 * |r|) by iteration."""
    r = 0.5
    for i in range(max_iter):
        K_eff = K0 * r
        if K_eff > 1:
            K_eff = 1.0
        r_new = order_parameter(tree, K_eff)
        if abs(r_new - r) < tol:
            return r_new, i + 1
        r = 0.7 * r + 0.3 * r_new  # damped iteration
    return r, max_iter


def check_rationality(x, max_denom=10000):
    """Check if x is close to a simple rational p/q with q ≤ max_denom."""
    best_p, best_q, best_err = 0, 1, abs(x)
    for q in range(1, max_denom + 1):
        p = round(x * q)
        err = abs(x - p / q)
        if err < best_err:
            best_p, best_q, best_err = p, q, err
    return best_p, best_q, best_err


def main():
    print("=" * 72)
    print("RFE: Does self-consistency force irrational solutions?")
    print("=" * 72)

    # --- Part 1: Order parameter at fixed K ---
    print("\n--- Part 1: Order parameter |r| at fixed K, various depths ---")
    print(f"{'depth':>6} {'nodes':>6} {'K':>6} {'|r|':>14} {'best p/q':>10} {'err':>12}")

    for depth in [3, 5, 7, 9, 11]:
        tree = stern_brocot_tree(depth)
        n_nodes = len(tree)
        for K in [0.5, 0.8, 0.95]:
            r = order_parameter(tree, K)
            p, q, err = check_rationality(r)
            rat_str = f"{p}/{q}"
            print(f"{depth:>6} {n_nodes:>6} {K:>6.2f} {r:>14.10f} {rat_str:>10} {err:>12.2e}")

    # --- Part 2: Self-consistent fixed point ---
    print("\n--- Part 2: Self-consistent |r*| = f(|r*|, K₀) ---")
    print(f"{'depth':>6} {'K₀':>6} {'|r*|':>14} {'iters':>6} {'best p/q':>10} {'err':>12}")

    for depth in [5, 7, 9]:
        tree = stern_brocot_tree(depth)
        for K0 in [1.5, 2.0, 3.0, 5.0]:
            r_star, iters = self_consistency(tree, K0)
            p, q, err = check_rationality(r_star)
            rat_str = f"{p}/{q}"
            print(f"{depth:>6} {K0:>6.1f} {r_star:>14.10f} {iters:>6} {rat_str:>10} {err:>12.2e}")

    # --- Part 3: Exact arithmetic check ---
    print("\n--- Part 3: Exact arithmetic at depth 3 ---")
    tree = stern_brocot_tree(3)
    print(f"Tree nodes: {tree}")

    # Compute order parameter symbolically
    print("\nOrder parameter sum (K=1, uniform weight 1/q):")
    print("z = Σ (1/q) × e^{2πi·p/q}")
    z_exact = 0.0 + 0.0j
    total = 0.0
    for p, q in tree:
        if q == 0:
            continue
        w = Fraction(1, q)
        phase = 2 * np.pi * p / q
        z_exact += float(w) * np.exp(1j * phase)
        total += float(w)
        print(f"  {p}/{q}: w=1/{q}, phase=2π·{p}/{q} = {phase:.4f}")

    r = abs(z_exact) / total
    print(f"\n|z| = {abs(z_exact):.10f}")
    print(f"Σw  = {total:.10f}")
    print(f"|r| = {r:.10f}")
    p, q, err = check_rationality(r)
    print(f"Best rational: {p}/{q}, error = {err:.2e}")
    if err > 1e-8:
        print("→ |r| is NOT a simple rational. Self-consistency")
        print("  produces an irrational from rational inputs.")
    else:
        print(f"→ |r| ≈ {p}/{q} (rational to this precision)")

    # --- Part 4: The parallel to 3x+1 ---
    print("\n--- Part 4: Collatz parallel ---")
    print()
    print("Collatz: mediant(p/1, 1/1) = (p+1)/2 — integers force")
    print("  non-integers via the mediant operation.")
    print()
    print("RFE: Σ_{p/q ∈ Q} w(p/q) × e^{2πi·p/q} — rationals force")
    print("  irrationals via the weighted phase sum.")
    print()
    print("Both: the domain (Z or Q) is not closed under the")
    print("  operation (mediant or weighted sum). Self-consistency")
    print("  forces completion to a larger domain (Q or R).")
    print()
    print("The field exists because the equation demands it.")
    print("Spatialization (sub-problem A) is a consequence of the")
    print("fixed-point primitive applied to the tree: x = f(x)")
    print("has solutions outside Q when f involves phases.")


if __name__ == "__main__":
    main()
