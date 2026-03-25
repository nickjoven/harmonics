"""
2D rational field equation on the Klein bottle.

The field equation (Derivation 11) extended to a product of two
Stern-Brocot trees, with the Klein bottle XOR selection rule:
only mode pairs (p₁/q₁, p₂/q₂) where q₁ and q₂ have opposite
parity are allowed.

The order parameter carries the x-direction twist:
    r = Σ N(f₁,f₂) × exp(2πi(f₁+f₂)) × (-1)^{q₁} / Σ N

Four variants compared:
  1. Torus: full product tree, standard order parameter
  2. Klein bottle XOR filter: restrict to opposite-parity pairs
  3. Klein bottle twist: (-1)^{q₁} in order parameter, full tree
  4. Klein bottle combined: XOR filter + twist

Usage:
    python sync_cost/derivations/field_equation_klein.py
"""

import math
import sys
from fractions import Fraction

sys.path.insert(0, "sync_cost/derivations")
from circle_map_utils import PHI, INV_PHI, fibonacci_sequence


# ── Stern-Brocot tree ────────────────────────────────────────────────────────

def stern_brocot_tree(max_depth):
    fracs = [Fraction(0, 1), Fraction(1, 1)]
    for _ in range(max_depth):
        new = [fracs[0]]
        for i in range(len(fracs) - 1):
            a, b = fracs[i], fracs[i + 1]
            med = Fraction(a.numerator + b.numerator,
                           a.denominator + b.denominator)
            new.append(med)
            new.append(b)
        fracs = new
    return sorted(f for f in set(fracs) if Fraction(0) < f < Fraction(1))


# ── Tongue width ──────────────────────────────────────────────────────────────

def tongue_width(p, q, K):
    if q == 1:
        return min(K / (2 * math.pi), 1.0)
    w_pert = 2 * (K / 2) ** q / q
    w_crit = 1.0 / (q * q)
    if K <= 0.5:
        return w_pert
    elif K >= 1.0:
        return w_crit
    else:
        t = (K - 0.5) / 0.5
        t = t * t * (3 - 2 * t)
        return w_pert * (1 - t) + w_crit * t


# ── 2D field equation ─────────────────────────────────────────────────────────

def solve_2d(tree_x, tree_y, K0, g_func, xor_filter=False, twist=False,
             n_iter=400, damping=0.3):
    """
    Solve the 2D field equation on the product tree.

    N(f₁,f₂) = N_total × g(f₁,f₂) × w(f₁, K_eff) × w(f₂, K_eff)

    with self-consistent K_eff = K0 × |r|.
    """
    # Build pair list
    pairs = []
    for f1 in tree_x:
        for f2 in tree_y:
            if xor_filter:
                if (f1.denominator % 2) == (f2.denominator % 2):
                    continue  # same parity → forbidden
            pairs.append((f1, f2))

    N_total = len(pairs)
    if N_total == 0:
        return {}, 0j, []

    populations = {(f1, f2): 1.0 for f1, f2 in pairs}
    r_history = []

    for it in range(n_iter):
        # Order parameter
        total_pop = sum(populations.values())
        if total_pop == 0:
            r = 0j
        else:
            r = 0j
            for (f1, f2), pop in populations.items():
                phase = 2 * math.pi * (float(f1) + float(f2))
                sign = ((-1) ** f1.denominator) if twist else 1
                r += pop * sign * (math.cos(phase) + 1j * math.sin(phase))
            r /= total_pop

        r_abs = abs(r)
        r_history.append(r_abs)
        K_eff = K0 * max(r_abs, 1e-15)

        # Update populations
        new_pop = {}
        for f1, f2 in pairs:
            g = g_func(float(f1), float(f2))
            w1 = tongue_width(f1.numerator, f1.denominator, K_eff)
            w2 = tongue_width(f2.numerator, f2.denominator, K_eff)
            new_pop[(f1, f2)] = N_total * g * w1 * w2

        # Normalize
        total = sum(new_pop.values())
        if total > 0:
            for key in new_pop:
                new_pop[key] *= N_total / total

        # Damped update
        for key in pairs:
            k = (key[0], key[1]) if isinstance(key, tuple) and len(key) == 2 else key
            populations[k] = (1 - damping) * populations[k] + damping * new_pop[k]

    # Final r
    total_pop = sum(populations.values())
    r_final = 0j
    for (f1, f2), pop in populations.items():
        phase = 2 * math.pi * (float(f1) + float(f2))
        sign = ((-1) ** f1.denominator) if twist else 1
        r_final += pop * sign * (math.cos(phase) + 1j * math.sin(phase))
    if total_pop > 0:
        r_final /= total_pop

    return populations, r_final, r_history


# ── Analysis ──────────────────────────────────────────────────────────────────

def top_modes(populations, label, n=20):
    """Print the top populated mode pairs."""
    sorted_pops = sorted(populations.items(), key=lambda x: -x[1])
    total = sum(v for _, v in sorted_pops)

    print(f"\n  Top {n} mode pairs [{label}]:")
    print(f"  {'(f₁, f₂)':>20s}  {'N':>10s}  {'frac':>8s}  "
          f"{'q₁':>4s}  {'q₂':>4s}  {'q₁%2':>5s}  {'q₂%2':>5s}  "
          f"{'f₁+f₂':>8s}")
    print("  " + "-" * 75)

    for (f1, f2), pop in sorted_pops[:n]:
        frac = pop / total if total > 0 else 0
        print(f"  ({str(f1):>5s},{str(f2):>5s})  {pop:10.4f}  {frac:8.5f}  "
              f"{f1.denominator:4d}  {f2.denominator:4d}  "
              f"{f1.denominator % 2:5d}  {f2.denominator % 2:5d}  "
              f"{float(f1)+float(f2):8.5f}")


def population_by_q_pair(populations, label, max_q=8):
    """Aggregate by (q₁, q₂)."""
    by_qq = {}
    for (f1, f2), pop in populations.items():
        q1, q2 = f1.denominator, f2.denominator
        if q1 <= max_q and q2 <= max_q:
            key = (q1, q2)
            by_qq[key] = by_qq.get(key, 0) + pop

    total = sum(populations.values())

    print(f"\n  Population by (q₁,q₂) [{label}]:")
    print(f"  {'':>6s}", end="")
    for q2 in range(2, max_q + 1):
        print(f" q₂={q2:<4d}", end="")
    print()

    for q1 in range(2, max_q + 1):
        print(f"  q₁={q1:<3d}", end="")
        for q2 in range(2, max_q + 1):
            val = by_qq.get((q1, q2), 0)
            if val > 0.01:
                frac = val / total
                print(f" {frac:7.4f}", end="")
            else:
                print(f"    ·   ", end="")
        print()

    return by_qq


def population_ratios(populations, label):
    """Extract the population ratios between top modes — the computable."""
    sorted_pops = sorted(populations.items(), key=lambda x: -x[1])
    total = sum(v for _, v in sorted_pops)

    if len(sorted_pops) < 2:
        return

    top_pop = sorted_pops[0][1]
    print(f"\n  Population ratios relative to top mode [{label}]:")
    print(f"  Top mode: {sorted_pops[0][0]} = {top_pop:.4f}")
    print(f"  {'(f₁, f₂)':>20s}  {'ratio':>10s}  {'1/ratio':>10s}  "
          f"{'nearest':>10s}")
    print("  " + "-" * 55)

    # Simple rationals to compare against
    simple = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
              (2, 3), (2, 5), (3, 4), (3, 5), (3, 8), (4, 5),
              (5, 6), (5, 8), (7, 8)]

    for (f1, f2), pop in sorted_pops[1:15]:
        ratio = pop / top_pop if top_pop > 0 else 0
        inv = top_pop / pop if pop > 0 else float('inf')

        # Find nearest simple rational
        best = None
        best_dist = 1.0
        for p, q in simple:
            for val in [p / q, q / p]:
                dist = abs(ratio - val)
                if dist < best_dist:
                    best_dist = dist
                    best = f"{p}/{q}" if val == p / q else f"{q}/{p}"

        near = f"≈ {best} (Δ={best_dist:.4f})" if best_dist < 0.05 else ""
        print(f"  ({str(f1):>5s},{str(f2):>5s})  {ratio:10.6f}  "
              f"{inv:10.4f}  {near:>10s}")


def fibonacci_backbone_2d(populations, tree_x, tree_y, label):
    """Check which Fibonacci convergent pairs are populated."""
    fibs = fibonacci_sequence(15)
    print(f"\n  Fibonacci backbone [{label}]:")
    print(f"  {'(Fₘ/Fₘ₊₁, Fₙ/Fₙ₊₁)':>25s}  {'N':>10s}  {'frac':>8s}  "
          f"{'present':>8s}")
    print("  " + "-" * 55)

    total = sum(populations.values())
    for m in range(1, 8):
        for n in range(1, 8):
            f1 = Fraction(fibs[m], fibs[m + 1])
            f2 = Fraction(fibs[n], fibs[n + 1])
            pop = populations.get((f1, f2), 0)
            frac = pop / total if total > 0 else 0
            present = "✓" if pop > 0.001 else "✗"
            if pop > 0.001:
                print(f"  ({fibs[m]}/{fibs[m+1]:>2d}, {fibs[n]}/{fibs[n+1]:>2d})"
                      f"  {pop:10.4f}  {frac:8.5f}  {present:>8s}")


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 80)
    print("  2D FIELD EQUATION ON THE KLEIN BOTTLE")
    print("  Derivation 11 × Derivation 19")
    print("=" * 80)

    DEPTH = 6
    tree = stern_brocot_tree(DEPTH)
    print(f"\n  Tree depth: {DEPTH}")
    print(f"  Nodes per axis: {len(tree)}")
    print(f"  Max denominator: {max(f.denominator for f in tree)}")

    n_torus = len(tree) ** 2
    n_klein = sum(1 for f1 in tree for f2 in tree
                  if (f1.denominator % 2) != (f2.denominator % 2))
    print(f"  Torus pairs: {n_torus}")
    print(f"  Klein pairs (XOR): {n_klein} ({100*n_klein/n_torus:.1f}%)")

    g_uniform = lambda f1, f2: 1.0
    g_golden = lambda f1, f2: math.exp(
        -5 * ((f1 - INV_PHI) ** 2 + (f2 - INV_PHI) ** 2))

    for g_name, g_func in [("uniform", g_uniform),
                            ("golden-peaked", g_golden)]:
        print(f"\n{'=' * 80}")
        print(f"  g(Ω₁,Ω₂) = {g_name}")
        print(f"{'=' * 80}")

        results = {}

        # 1. Torus
        print(f"\n{'─' * 80}")
        print(f"  TORUS (periodic × periodic)")
        print(f"{'─' * 80}")
        pop_t, r_t, _ = solve_2d(tree, tree, K0=1.0, g_func=g_func,
                                  xor_filter=False, twist=False)
        print(f"  |r| = {abs(r_t):.6f}")
        results["torus"] = (pop_t, r_t)
        top_modes(pop_t, "Torus")
        population_by_q_pair(pop_t, "Torus")
        population_ratios(pop_t, "Torus")
        fibonacci_backbone_2d(pop_t, tree, tree, "Torus")

        # 2. Klein XOR filter
        print(f"\n{'─' * 80}")
        print(f"  KLEIN BOTTLE (XOR filter only)")
        print(f"{'─' * 80}")
        pop_k, r_k, _ = solve_2d(tree, tree, K0=1.0, g_func=g_func,
                                  xor_filter=True, twist=False)
        print(f"  |r| = {abs(r_k):.6f}")
        results["klein_filter"] = (pop_k, r_k)
        top_modes(pop_k, "Klein filter")
        population_by_q_pair(pop_k, "Klein filter")
        population_ratios(pop_k, "Klein filter")
        fibonacci_backbone_2d(pop_k, tree, tree, "Klein filter")

        # 3. Klein twist
        print(f"\n{'─' * 80}")
        print(f"  KLEIN BOTTLE (twist in order parameter)")
        print(f"{'─' * 80}")
        pop_tw, r_tw, _ = solve_2d(tree, tree, K0=1.0, g_func=g_func,
                                    xor_filter=False, twist=True)
        print(f"  |r| = {abs(r_tw):.6f}")
        results["klein_twist"] = (pop_tw, r_tw)
        top_modes(pop_tw, "Klein twist")
        population_by_q_pair(pop_tw, "Klein twist")
        population_ratios(pop_tw, "Klein twist")

        # 4. Klein combined
        print(f"\n{'─' * 80}")
        print(f"  KLEIN BOTTLE (XOR filter + twist)")
        print(f"{'─' * 80}")
        pop_c, r_c, _ = solve_2d(tree, tree, K0=1.0, g_func=g_func,
                                  xor_filter=True, twist=True)
        print(f"  |r| = {abs(r_c):.6f}")
        results["klein_combined"] = (pop_c, r_c)
        top_modes(pop_c, "Klein combined")
        population_by_q_pair(pop_c, "Klein combined")
        population_ratios(pop_c, "Klein combined")
        fibonacci_backbone_2d(pop_c, tree, tree, "Klein combined")

        # Summary
        print(f"\n{'─' * 80}")
        print(f"  COMPARISON [{g_name}]")
        print(f"{'─' * 80}")
        print(f"\n  {'Variant':>25s}  {'|r|':>8s}  {'pairs':>6s}  {'top mode':>20s}")
        print("  " + "-" * 65)
        for name, key in [("Torus", "torus"),
                          ("Klein filter", "klein_filter"),
                          ("Klein twist", "klein_twist"),
                          ("Klein combined", "klein_combined")]:
            pop, r = results[key]
            top = max(pop.items(), key=lambda x: x[1])
            f1, f2 = top[0]
            print(f"  {name:>25s}  {abs(r):8.4f}  {len(pop):6d}  "
                  f"({str(f1):>5s},{str(f2):>5s})")

    print(f"\n{'=' * 80}")
    print("  DONE")
    print(f"{'=' * 80}")
