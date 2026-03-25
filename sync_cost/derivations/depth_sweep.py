"""
Depth sweep: population ratio between (q1=2,q2=3) and (q1=3,q2=2) sectors
as a function of Stern-Brocot tree depth.

D21 item C: does the population ratio run with depth in a way consistent
with the SM beta function ratio |b3|/|b2| = 42/19 ~ 2.21?

Uses the Klein bottle field equation (XOR filter + twist) from
field_equation_klein.py.
"""

import math
import sys
from fractions import Fraction

sys.path.insert(0, "sync_cost/derivations")
try:
    from circle_map_utils import PHI, INV_PHI
except ImportError:
    PHI = (1 + math.sqrt(5)) / 2
    INV_PHI = 1.0 / PHI


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


# ── 2D field equation solver ─────────────────────────────────────────────────

def solve_2d(tree_x, tree_y, K0, g_func, xor_filter=False, twist=False,
             n_iter=400, damping=0.3):
    pairs = []
    for f1 in tree_x:
        for f2 in tree_y:
            if xor_filter:
                if (f1.denominator % 2) == (f2.denominator % 2):
                    continue
            pairs.append((f1, f2))

    N_total = len(pairs)
    if N_total == 0:
        return {}, 0j, []

    populations = {(f1, f2): 1.0 for f1, f2 in pairs}
    r_history = []

    for it in range(n_iter):
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

        new_pop = {}
        for f1, f2 in pairs:
            g = g_func(float(f1), float(f2))
            w1 = tongue_width(f1.numerator, f1.denominator, K_eff)
            w2 = tongue_width(f2.numerator, f2.denominator, K_eff)
            new_pop[(f1, f2)] = N_total * g * w1 * w2

        total = sum(new_pop.values())
        if total > 0:
            for key in new_pop:
                new_pop[key] *= N_total / total

        for key in pairs:
            k = (key[0], key[1])
            populations[k] = (1 - damping) * populations[k] + damping * new_pop[k]

    total_pop = sum(populations.values())
    r_final = 0j
    for (f1, f2), pop in populations.items():
        phase = 2 * math.pi * (float(f1) + float(f2))
        sign = ((-1) ** f1.denominator) if twist else 1
        r_final += pop * sign * (math.cos(phase) + 1j * math.sin(phase))
    if total_pop > 0:
        r_final /= total_pop

    return populations, r_final, r_history


# ── Sector population extraction ─────────────────────────────────────────────

def sector_population(populations, q1_target, q2_target):
    """Sum population over all modes with given (q1, q2) denominator pair."""
    total = 0.0
    count = 0
    for (f1, f2), pop in populations.items():
        if f1.denominator == q1_target and f2.denominator == q2_target:
            total += pop
            count += 1
    return total, count


# ── Main sweep ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 85)
    print("  DEPTH SWEEP: Klein bottle population ratio (2,3) vs (3,2)")
    print("  D21 item C — comparison with SM beta ratio |b3|/|b2| = 42/19")
    print("=" * 85)

    # SM reference values
    b2 = -19.0 / 6.0
    b3 = -7.0
    ratio_SM = abs(b3) / abs(b2)  # 42/19 ~ 2.21
    ln_ratio_SM = math.log(ratio_SM)  # ~ 0.794

    print(f"\n  SM beta coefficients:")
    print(f"    b2 = -19/6 = {b2:.6f}")
    print(f"    b3 = -7")
    print(f"    |b3|/|b2| = 42/19 = {ratio_SM:.6f}")
    print(f"    ln(|b3/b2|) = ln(42/19) = {ln_ratio_SM:.6f}")

    depths = [4, 5, 6, 7, 8]  # 9-10 too expensive (product tree ~500k pairs)

    g_uniform = lambda f1, f2: 1.0
    g_golden = lambda f1, f2: math.exp(
        -5 * ((f1 - INV_PHI) ** 2 + (f2 - INV_PHI) ** 2))

    for g_name, g_func in [("uniform", g_uniform),
                            ("golden-peaked", g_golden)]:
        print(f"\n{'=' * 85}")
        print(f"  g(f1,f2) = {g_name}")
        print(f"{'=' * 85}")

        results = []

        print(f"\n  {'depth':>5s}  {'nodes':>6s}  {'pairs':>7s}  "
              f"{'|r|':>8s}  "
              f"{'N(2,3)':>10s}  {'#(2,3)':>7s}  "
              f"{'N(3,2)':>10s}  {'#(3,2)':>7s}  "
              f"{'ratio':>10s}  {'ln(ratio)':>10s}")
        print("  " + "-" * 95)

        for d in depths:
            tree = stern_brocot_tree(d)
            n_nodes = len(tree)

            pop, r, _ = solve_2d(tree, tree, K0=1.0, g_func=g_func,
                                  xor_filter=True, twist=True,
                                  n_iter=500, damping=0.3)

            N_23, count_23 = sector_population(pop, 2, 3)
            N_32, count_32 = sector_population(pop, 3, 2)

            n_pairs = len(pop)
            r_abs = abs(r)

            if N_32 > 0:
                ratio = N_23 / N_32
                ln_ratio = math.log(ratio) if ratio > 0 else float('-inf')
            else:
                ratio = float('inf')
                ln_ratio = float('inf')

            results.append((d, n_nodes, n_pairs, r_abs,
                           N_23, count_23, N_32, count_32,
                           ratio, ln_ratio))

            print(f"  {d:5d}  {n_nodes:6d}  {n_pairs:7d}  "
                  f"{r_abs:8.5f}  "
                  f"{N_23:10.4f}  {count_23:7d}  "
                  f"{N_32:10.4f}  {count_32:7d}  "
                  f"{ratio:10.6f}  {ln_ratio:10.6f}")

        # ── Analysis ──────────────────────────────────────────────────────
        print(f"\n  {'─' * 85}")
        print(f"  ANALYSIS [{g_name}]")
        print(f"  {'─' * 85}")

        # Compute slope d(ln(ratio))/d(depth) via linear regression
        valid = [(d, lr) for d, _, _, _, _, _, _, _, _, lr in results
                 if lr != float('inf') and lr != float('-inf')]

        if len(valid) >= 2:
            n = len(valid)
            sum_d = sum(d for d, _ in valid)
            sum_lr = sum(lr for _, lr in valid)
            sum_dd = sum(d * d for d, _ in valid)
            sum_dlr = sum(d * lr for d, lr in valid)

            denom = n * sum_dd - sum_d * sum_d
            if denom != 0:
                slope = (n * sum_dlr - sum_d * sum_lr) / denom
                intercept = (sum_lr - slope * sum_d) / n

                # Residuals
                ss_res = sum((lr - (slope * d + intercept)) ** 2
                             for d, lr in valid)
                ss_tot = sum((lr - sum_lr / n) ** 2 for _, lr in valid)
                R2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0

                print(f"\n  Linear fit: ln(ratio) = {slope:.6f} * depth + {intercept:.6f}")
                print(f"  R^2 = {R2:.6f}")
                print(f"  Slope = {slope:.6f}")
                print(f"  ln(42/19) = {ln_ratio_SM:.6f}")
                print(f"  Slope / ln(42/19) = {slope / ln_ratio_SM:.6f}")
            else:
                slope = 0
                print("  Cannot fit: degenerate data")
        else:
            slope = 0
            print("  Cannot fit: insufficient valid data points")

        # Direct ratio comparison
        print(f"\n  Direct ratio at each depth vs |b3|/|b2| = {ratio_SM:.6f}:")
        for d, _, _, _, _, _, _, _, ratio, _ in results:
            if ratio != float('inf'):
                deviation = (ratio - ratio_SM) / ratio_SM * 100
                print(f"    depth {d}: ratio = {ratio:.6f}, "
                      f"deviation from 42/19 = {deviation:+.2f}%")

        # Check if any depth gives ratio close to 42/19
        closest_d = None
        closest_dev = float('inf')
        for d, _, _, _, _, _, _, _, ratio, _ in results:
            if ratio != float('inf'):
                dev = abs(ratio - ratio_SM)
                if dev < closest_dev:
                    closest_dev = dev
                    closest_d = d

        if closest_d is not None:
            print(f"\n  Closest match: depth {closest_d} "
                  f"(deviation = {closest_dev:.6f})")

        # Check ratio of ratios between consecutive depths
        print(f"\n  Ratio change between consecutive depths:")
        for i in range(1, len(results)):
            d_prev = results[i - 1][0]
            d_curr = results[i][0]
            r_prev = results[i - 1][8]
            r_curr = results[i][8]
            if r_prev > 0 and r_curr > 0 and r_prev != float('inf') and r_curr != float('inf'):
                change = r_curr / r_prev
                ln_change = math.log(change)
                print(f"    depth {d_prev}->{d_curr}: "
                      f"ratio(d+1)/ratio(d) = {change:.6f}, "
                      f"ln(change) = {ln_change:.6f}")

    # ── Final verdict ─────────────────────────────────────────────────────
    print(f"\n{'=' * 85}")
    print("  FINAL VERDICT")
    print(f"{'=' * 85}")
    print(f"""
  Target: |b3|/|b2| = 42/19 = {ratio_SM:.6f}
  Target: ln(42/19) = {ln_ratio_SM:.6f}

  The depth sweep tests whether the population ratio N(2,3)/N(3,2)
  in the Klein bottle field equation (XOR + twist) tracks the SM
  beta function ratio as tree depth (= energy scale proxy) varies.

  Three possible outcomes:
  (a) The ratio is constant ~ 42/19 at all depths (exact match)
  (b) The ratio runs with depth, and the slope matches ln(42/19)
  (c) No match — the population ratio is unrelated to the SM ratio
""")

    print("=" * 85)
    print("  DONE")
    print("=" * 85)
