"""
D21-C depth sweep v2: WITHIN-sector asymmetry vs tree depth.

The Klein bottle field equation (XOR + twist) with golden-peaked g(ω)
produces 4 surviving modes in two conjugate pairs:

  Sector A (higher pop):  (1/2, 2/3) and (2/3, 1/2)  ~29.9% each
  Sector B (lower pop):   (1/3, 1/2) and (1/2, 1/3)  ~20.1% each

The BETWEEN-sector ratio N(2,3)/N(3,2) = 1 by symmetry (trivial).
The WITHIN-sector ratio  N(1/3, 1/2) / N(1/2, 2/3) ≈ 0.675 ≈ 2/3.

Question: does this within-sector ratio depend on tree depth d?

Physics: at the Klein bottle's combined fixed point |r| = 0, so
K_eff = K₀ × |r| = 0, and all tongue widths collapse via the
perturbative formula w(p/q, 0) → 0 for q ≥ 2. Populations are then
set by g(f₁,f₂) × w(f₁, 0) × w(f₂, 0), with the golden peak
g = exp(-5((f₁ - 1/φ)² + (f₂ - 1/φ)²)) breaking the symmetry.

Usage:
    python sync_cost/derivations/depth_sweep_v2.py
"""

import math
import sys
from fractions import Fraction

sys.path.insert(0, "sync_cost/derivations")
from circle_map_utils import PHI, INV_PHI


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


# ── 2D field equation (Klein combined: XOR + twist) ──────────────────────────

def solve_klein_combined(tree, K0, g_func, n_iter=500, damping=0.3):
    """
    Solve the 2D field equation on the Klein bottle (XOR filter + twist).
    Returns populations dict, final r, and convergence history.
    """
    # Build pair list: XOR filter — opposite parity only
    pairs = []
    for f1 in tree:
        for f2 in tree:
            if (f1.denominator % 2) != (f2.denominator % 2):
                pairs.append((f1, f2))

    N_total = len(pairs)
    if N_total == 0:
        return {}, 0j, []

    populations = {(f1, f2): 1.0 for f1, f2 in pairs}
    r_history = []

    for it in range(n_iter):
        # Order parameter with twist: (-1)^{q₁}
        total_pop = sum(populations.values())
        if total_pop == 0:
            r = 0j
        else:
            r = 0j
            for (f1, f2), pop in populations.items():
                phase = 2 * math.pi * (float(f1) + float(f2))
                sign = (-1) ** f1.denominator
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
        for f1, f2 in pairs:
            k = (f1, f2)
            populations[k] = (1 - damping) * populations[k] + damping * new_pop[k]

    # Final order parameter
    total_pop = sum(populations.values())
    r_final = 0j
    for (f1, f2), pop in populations.items():
        phase = 2 * math.pi * (float(f1) + float(f2))
        sign = (-1) ** f1.denominator
        r_final += pop * sign * (math.cos(phase) + 1j * math.sin(phase))
    if total_pop > 0:
        r_final /= total_pop

    return populations, r_final, r_history


# ── Target modes ──────────────────────────────────────────────────────────────

MODE_A1 = (Fraction(1, 2), Fraction(2, 3))   # Sector A
MODE_A2 = (Fraction(2, 3), Fraction(1, 2))   # Sector A (conjugate)
MODE_B1 = (Fraction(1, 3), Fraction(1, 2))   # Sector B
MODE_B2 = (Fraction(1, 2), Fraction(1, 3))   # Sector B (conjugate)


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 80)
    print("  DEPTH SWEEP v2: WITHIN-SECTOR ASYMMETRY")
    print("  Klein bottle (XOR + twist) + golden-peaked g(ω)")
    print("=" * 80)

    # Golden-peaked frequency distribution
    g_golden = lambda f1, f2: math.exp(
        -5 * ((f1 - INV_PHI) ** 2 + (f2 - INV_PHI) ** 2))

    depths = [4, 5, 6, 7, 8]
    K0 = 1.0

    results = []

    for d in depths:
        print(f"\n{'─' * 80}")
        print(f"  Depth d = {d}")
        print(f"{'─' * 80}")

        tree = stern_brocot_tree(d)
        n_nodes = len(tree)
        max_q = max(f.denominator for f in tree)
        n_klein = sum(1 for f1 in tree for f2 in tree
                      if (f1.denominator % 2) != (f2.denominator % 2))

        print(f"  Nodes: {n_nodes}, max q: {max_q}, Klein pairs: {n_klein}")

        pop, r, r_hist = solve_klein_combined(tree, K0, g_golden,
                                               n_iter=500, damping=0.3)

        total = sum(pop.values())
        r_abs = abs(r)
        print(f"  |r| = {r_abs:.8f}")
        print(f"  Final 5 |r| values: {[f'{x:.2e}' for x in r_hist[-5:]]}")

        # Extract the 4 target mode populations
        pop_A1 = pop.get(MODE_A1, 0.0)
        pop_A2 = pop.get(MODE_A2, 0.0)
        pop_B1 = pop.get(MODE_B1, 0.0)
        pop_B2 = pop.get(MODE_B2, 0.0)

        frac_A1 = pop_A1 / total if total > 0 else 0
        frac_A2 = pop_A2 / total if total > 0 else 0
        frac_B1 = pop_B1 / total if total > 0 else 0
        frac_B2 = pop_B2 / total if total > 0 else 0

        # Within-sector ratio: B / A
        ratio = frac_B1 / frac_A1 if frac_A1 > 0 else float('inf')

        # Also compute sector totals
        frac_A = frac_A1 + frac_A2
        frac_B = frac_B1 + frac_B2
        four_mode_total = frac_A + frac_B

        print(f"\n  4-mode populations (fraction of total):")
        print(f"    (1/2, 2/3) = {frac_A1:.6f}   [Sector A]")
        print(f"    (2/3, 1/2) = {frac_A2:.6f}   [Sector A]")
        print(f"    (1/3, 1/2) = {frac_B1:.6f}   [Sector B]")
        print(f"    (1/2, 1/3) = {frac_B2:.6f}   [Sector B]")
        print(f"    4-mode sum = {four_mode_total:.6f}")
        print(f"\n  Sector A total: {frac_A:.6f}")
        print(f"  Sector B total: {frac_B:.6f}")
        print(f"  Within-sector ratio N(1/3,1/2) / N(1/2,2/3) = {ratio:.8f}")
        print(f"  2/3 reference = {2/3:.8f}")
        print(f"  Deviation from 2/3: {abs(ratio - 2/3):.2e}")

        results.append({
            'depth': d,
            'n_nodes': n_nodes,
            'max_q': max_q,
            'n_klein': n_klein,
            'r_abs': r_abs,
            'frac_A1': frac_A1,
            'frac_A2': frac_A2,
            'frac_B1': frac_B1,
            'frac_B2': frac_B2,
            'ratio': ratio,
            'four_mode_sum': four_mode_total,
        })

    # ── Summary table ─────────────────────────────────────────────────────────

    print(f"\n\n{'=' * 80}")
    print("  SUMMARY: WITHIN-SECTOR RATIO vs DEPTH")
    print(f"{'=' * 80}")
    print(f"\n  {'d':>3s}  {'nodes':>6s}  {'max_q':>6s}  {'Klein':>7s}  "
          f"{'|r|':>10s}  {'A1':>8s}  {'A2':>8s}  {'B1':>8s}  {'B2':>8s}  "
          f"{'ratio':>10s}  {'Δ(2/3)':>10s}")
    print("  " + "-" * 95)

    for r in results:
        delta = r['ratio'] - 2/3
        print(f"  {r['depth']:3d}  {r['n_nodes']:6d}  {r['max_q']:6d}  "
              f"{r['n_klein']:7d}  {r['r_abs']:10.2e}  "
              f"{r['frac_A1']:8.5f}  {r['frac_A2']:8.5f}  "
              f"{r['frac_B1']:8.5f}  {r['frac_B2']:8.5f}  "
              f"{r['ratio']:10.8f}  {delta:+10.2e}")

    # ── Slope analysis ────────────────────────────────────────────────────────

    print(f"\n\n{'=' * 80}")
    print("  SLOPE ANALYSIS: d(ratio)/d(depth)")
    print(f"{'=' * 80}")

    if len(results) >= 2:
        for i in range(1, len(results)):
            dd = results[i]['depth'] - results[i-1]['depth']
            dr = results[i]['ratio'] - results[i-1]['ratio']
            slope = dr / dd if dd != 0 else 0
            print(f"  d={results[i-1]['depth']}→{results[i]['depth']}:  "
                  f"Δratio = {dr:+.8f},  slope = {slope:+.8f}")

        # Overall slope (linear fit: just endpoints for simplicity)
        d_range = results[-1]['depth'] - results[0]['depth']
        r_range = results[-1]['ratio'] - results[0]['ratio']
        overall_slope = r_range / d_range if d_range != 0 else 0
        print(f"\n  Overall slope (d={results[0]['depth']}→{results[-1]['depth']}): "
              f"{overall_slope:+.8f}")
        print(f"  Total Δratio over range: {r_range:+.8f}")

        # Check if ratio is converging
        ratios = [r['ratio'] for r in results]
        final = ratios[-1]
        print(f"\n  Converged value (d={results[-1]['depth']}): {final:.8f}")
        print(f"  2/3 = {2/3:.8f}")
        print(f"  Deviation from 2/3: {abs(final - 2/3):.2e}")

        # Weinberg angle comparison
        sin2_w = 0.23122  # sin²θ_W at M_Z
        print(f"\n  ── SM comparison ──")
        print(f"  sin²θ_W = {sin2_w:.5f}")
        print(f"  1 - 3×sin²θ_W = {1 - 3*sin2_w:.5f}")
        print(f"  ratio / (2/3) - 1 = {(final/(2/3)) - 1:.6f}")

    print(f"\n{'=' * 80}")
    print("  DONE")
    print(f"{'=' * 80}")
