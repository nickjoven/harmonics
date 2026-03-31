"""
Rational field equation (Derivation 11) on the Möbius domain.

The antiperiodic boundary condition θ(wrap) = θ(start) + π modifies
the self-consistency equation. The order parameter sum picks up a
topological phase factor from oscillators whose coupling path crosses
the twist.

Three variants compared:
  1. Periodic (original D11): r = Σ N(p/q) exp(2πi p/q) / Σ N
  2. Möbius twist: r = Σ N(p/q) exp(2πi p/q) × (-1)^q / Σ N
     (odd-denominator modes acquire sign flip from the half-twist —
      after q cycles through the strip, the accumulated twist is qπ;
      odd q gives net sign reversal)
  3. Möbius filter: restrict tree to rationals compatible with the
     antiperiodic BC (odd winding: (2n+1)/2 total phase per traversal)

Usage:
    python sync_cost/derivations/field_equation_mobius.py
"""

import math
import sys
from fractions import Fraction

sys.path.insert(0, "sync_cost/derivations")
from circle_map_utils import (
    PHI, INV_PHI, PHI_SQ, LN_PHI_SQ,
    fibonacci_sequence, tongue_width,
)


# ── Stern-Brocot tree ────────────────────────────────────────────────────────

def stern_brocot_tree(max_depth):
    """Build the Stern-Brocot tree on (0,1) using exact rationals."""
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


# ── Order parameter variants ─────────────────────────────────────────────────

def order_parameter_periodic(populations, tree):
    """Standard order parameter: r = <exp(2πi p/q)>."""
    total = sum(populations[f] for f in tree)
    if total == 0:
        return 0j
    return sum(populations[f] * math.e ** (2j * math.pi * float(f))
               for f in tree) / total


def order_parameter_mobius(populations, tree):
    """Möbius order parameter: exp(2πi p/q) × (-1)^q.

    The half-twist means an oscillator locked to p/q accumulates
    q traversals of the strip per q cycles. Each traversal picks up
    a phase π. After q cycles: phase = qπ. For odd q, net sign = -1.
    """
    total = sum(populations[f] for f in tree)
    if total == 0:
        return 0j
    return sum(populations[f]
               * math.e ** (2j * math.pi * float(f))
               * ((-1) ** f.denominator)
               for f in tree) / total


# ── Field equation solver ─────────────────────────────────────────────────────

def solve_field_equation(tree, K0, g_func, order_param_func,
                         n_iter=500, damping=0.3):
    """
    Solve N(p/q) = N_total × g(p/q) × w(p/q, K_eff) by damped
    fixed-point iteration.

    order_param_func: callable(populations, tree) -> complex
    """
    N_total = len(tree)
    populations = {f: 1.0 for f in tree}  # uniform start
    r_history = []

    for it in range(n_iter):
        r = order_param_func(populations, tree)
        r_abs = abs(r)
        r_history.append(r_abs)
        K_eff = K0 * max(r_abs, 1e-15)

        new_pop = {}
        for f in tree:
            p, q = f.numerator, f.denominator
            g = g_func(float(f))
            w = tongue_width(p, q, K_eff)
            new_pop[f] = N_total * g * w

        # Normalize
        total = sum(new_pop.values())
        if total > 0:
            for f in new_pop:
                new_pop[f] *= N_total / total

        # Damped update for stability
        for f in tree:
            populations[f] = (1 - damping) * populations[f] + damping * new_pop[f]

    r_final = order_param_func(populations, tree)
    return populations, r_final, r_history


# ── Möbius filter: restrict to compatible rationals ───────────────────────────

def mobius_compatible(p, q):
    """Is p/q compatible with the antiperiodic boundary condition?

    On a Möbius ring, the total phase winding must be (2n+1)π for
    integer n — an odd multiple of π. In frequency units, the
    winding number p/q contributes phase 2πp per q cycles. The
    Möbius twist adds π per traversal.

    Compatibility condition: 2πp + qπ ≡ 0 (mod 2π) at the fixed point.
    Simplifying: p + q/2 must be integer, i.e., q must be even.

    OR: the total winding 2πp/q per cycle plus π/q per cycle from the
    twist gives (2p+1)π/q per cycle. For this to produce a standing
    wave, we need (2p+1)/q to be rational (it already is) and
    compatible with the boundary return. The simplest filter: keep
    rationals where (2p+1) and q share no destructive interference.

    In practice, the strongest topological constraint is: the parity
    of the spatial winding selects modes. We keep ALL rationals but
    modify the order parameter (variant 2), and ALSO run the filtered
    variant where we keep only rationals with odd (p+q) — these
    produce half-integer total winding, compatible with the Möbius twist.
    """
    return (p + q) % 2 == 1  # p+q odd ↔ opposite parity


# ── Analysis ──────────────────────────────────────────────────────────────────

def analyze_populations(populations, tree, label):
    """Extract and print Fibonacci backbone statistics."""
    fibs = fibonacci_sequence(25)
    backbone = []
    for i in range(1, len(fibs) - 1):
        f = Fraction(fibs[i], fibs[i + 1])
        if f in populations and populations[f] > 0:
            q = fibs[i + 1]
            w = 1.0 / (q * q)
            density = populations[f] / w
            backbone.append((i, f, populations[f], w, density))

    print(f"\n  Fibonacci backbone [{label}]:")
    print(f"  {'level':>5s}  {'p/q':>10s}  {'N(p/q)':>12s}  "
          f"{'density':>12s}  {'ln(dens)':>10s}")
    print("  " + "-" * 60)

    ln_densities = []
    levels = []
    for idx, f, pop, w, dens in backbone:
        ln_d = math.log(dens) if dens > 0 else float('-inf')
        print(f"  {idx:5d}  {str(f):>10s}  {pop:12.6e}  "
              f"{dens:12.6e}  {ln_d:10.4f}")
        if dens > 0:
            ln_densities.append(ln_d)
            levels.append(idx)

    # Density slope
    slope = None
    if len(ln_densities) >= 3:
        n = len(ln_densities)
        mx = sum(levels) / n
        my = sum(ln_densities) / n
        vx = sum((x - mx) ** 2 for x in levels) / n
        if vx > 0:
            cov = sum((x - mx) * (y - my)
                      for x, y in zip(levels, ln_densities)) / n
            slope = cov / vx
    return backbone, slope


def population_by_denominator(populations, tree, label, max_q=20):
    """Aggregate population by denominator q to see which modes dominate."""
    by_q = {}
    for f in tree:
        q = f.denominator
        if q <= max_q:
            by_q[q] = by_q.get(q, 0) + populations[f]

    total = sum(populations[f] for f in tree)
    print(f"\n  Population by denominator q [{label}]:")
    print(f"  {'q':>4s}  {'N(q)':>12s}  {'fraction':>10s}  {'parity':>8s}")
    print("  " + "-" * 42)
    for q in sorted(by_q.keys()):
        frac = by_q[q] / total if total > 0 else 0
        parity = "odd" if q % 2 == 1 else "even"
        print(f"  {q:4d}  {by_q[q]:12.4f}  {frac:10.6f}  {parity:>8s}")
    return by_q


def population_top_modes(populations, label, top_n=15):
    """Show the top N most populated modes."""
    sorted_pops = sorted(populations.items(), key=lambda x: -x[1])
    total = sum(v for _, v in sorted_pops)

    print(f"\n  Top {top_n} modes [{label}]:")
    print(f"  {'p/q':>10s}  {'N(p/q)':>12s}  {'fraction':>10s}  "
          f"{'q':>4s}  {'p+q':>5s}  {'p+q mod2':>8s}")
    print("  " + "-" * 60)
    for f, pop in sorted_pops[:top_n]:
        frac = pop / total if total > 0 else 0
        pq_sum = f.numerator + f.denominator
        print(f"  {str(f):>10s}  {pop:12.4f}  {frac:10.6f}  "
              f"{f.denominator:4d}  {pq_sum:5d}  {pq_sum % 2:>8d}")


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 80)
    print("  FIELD EQUATION ON THE MÖBIUS DOMAIN")
    print("  Derivation 11 × Derivation 18")
    print("=" * 80)

    DEPTH = 8
    tree = stern_brocot_tree(DEPTH)
    print(f"\n  Tree depth: {DEPTH}")
    print(f"  Nodes: {len(tree)}")
    print(f"  Max denominator: {max(f.denominator for f in tree)}")

    # Count parity classes
    odd_pq = [f for f in tree if (f.numerator + f.denominator) % 2 == 1]
    even_pq = [f for f in tree if (f.numerator + f.denominator) % 2 == 0]
    print(f"  Nodes with p+q odd (Möbius-compatible): {len(odd_pq)}")
    print(f"  Nodes with p+q even: {len(even_pq)}")

    g_uniform = lambda omega: 1.0
    g_golden = lambda omega: math.exp(-5 * (omega - INV_PHI) ** 2)

    for g_name, g_func in [("uniform", g_uniform), ("golden-peaked", g_golden)]:
        print(f"\n{'=' * 80}")
        print(f"  g(Ω) = {g_name}")
        print(f"{'=' * 80}")

        # ── 1. Periodic (baseline) ────────────────────────────────────────
        print(f"\n{'─' * 80}")
        print(f"  VARIANT 1: PERIODIC (baseline)")
        print(f"{'─' * 80}")

        pop_per, r_per, hist_per = solve_field_equation(
            tree, K0=1.0, g_func=g_func,
            order_param_func=order_parameter_periodic
        )
        print(f"\n  |r| = {abs(r_per):.6f}")
        print(f"  arg(r) = {math.atan2(r_per.imag, r_per.real):.4f}")

        bb_per, slope_per = analyze_populations(pop_per, tree, "Periodic")
        by_q_per = population_by_denominator(pop_per, tree, "Periodic")
        population_top_modes(pop_per, "Periodic")

        # ── 2. Möbius twist (modified order parameter) ────────────────────
        print(f"\n{'─' * 80}")
        print(f"  VARIANT 2: MÖBIUS TWIST ((-1)^q in order parameter)")
        print(f"{'─' * 80}")

        pop_mob, r_mob, hist_mob = solve_field_equation(
            tree, K0=1.0, g_func=g_func,
            order_param_func=order_parameter_mobius
        )
        print(f"\n  |r| = {abs(r_mob):.6f}")
        print(f"  arg(r) = {math.atan2(r_mob.imag, r_mob.real):.4f}")

        bb_mob, slope_mob = analyze_populations(pop_mob, tree, "Möbius twist")
        by_q_mob = population_by_denominator(pop_mob, tree, "Möbius twist")
        population_top_modes(pop_mob, "Möbius twist")

        # ── 3. Möbius filter (restrict tree) ──────────────────────────────
        print(f"\n{'─' * 80}")
        print(f"  VARIANT 3: MÖBIUS FILTER (p+q odd only)")
        print(f"{'─' * 80}")

        tree_filtered = [f for f in tree if mobius_compatible(f.numerator, f.denominator)]
        print(f"\n  Filtered nodes: {len(tree_filtered)} / {len(tree)}")

        pop_filt, r_filt, hist_filt = solve_field_equation(
            tree_filtered, K0=1.0, g_func=g_func,
            order_param_func=order_parameter_periodic  # standard r on restricted tree
        )
        print(f"\n  |r| = {abs(r_filt):.6f}")
        print(f"  arg(r) = {math.atan2(r_filt.imag, r_filt.real):.4f}")

        bb_filt, slope_filt = analyze_populations(pop_filt, tree_filtered, "Möbius filter")
        by_q_filt = population_by_denominator(pop_filt, tree_filtered, "Möbius filter")
        population_top_modes(pop_filt, "Möbius filter")

        # ── 4. Möbius twist + filter combined ─────────────────────────────
        print(f"\n{'─' * 80}")
        print(f"  VARIANT 4: MÖBIUS TWIST + FILTER (both constraints)")
        print(f"{'─' * 80}")

        pop_both, r_both, hist_both = solve_field_equation(
            tree_filtered, K0=1.0, g_func=g_func,
            order_param_func=order_parameter_mobius
        )
        print(f"\n  |r| = {abs(r_both):.6f}")
        print(f"  arg(r) = {math.atan2(r_both.imag, r_both.real):.4f}")

        bb_both, slope_both = analyze_populations(pop_both, tree_filtered, "Twist+Filter")
        by_q_both = population_by_denominator(pop_both, tree_filtered, "Twist+Filter")
        population_top_modes(pop_both, "Twist+Filter")

        # ── Comparison ────────────────────────────────────────────────────
        print(f"\n{'─' * 80}")
        print(f"  COMPARISON [{g_name}]")
        print(f"{'─' * 80}")

        print(f"\n  {'Variant':>25s}  {'|r|':>8s}  {'slope':>10s}  {'top mode':>12s}")
        print("  " + "-" * 60)

        for name, r_val, slope, pops in [
            ("Periodic", r_per, slope_per, pop_per),
            ("Möbius twist", r_mob, slope_mob, pop_mob),
            ("Möbius filter", r_filt, slope_filt, pop_filt),
            ("Twist + filter", r_both, slope_both, pop_both),
        ]:
            top = max(pops.items(), key=lambda x: x[1])
            sl = f"{slope:.6f}" if slope is not None else "N/A"
            print(f"  {name:>25s}  {abs(r_val):8.4f}  {sl:>10s}  {str(top[0]):>12s}")

        # ── Population redistribution ─────────────────────────────────────
        print(f"\n  Population fraction in odd-q vs even-q modes:")
        print(f"  {'Variant':>25s}  {'odd-q':>10s}  {'even-q':>10s}  {'ratio':>10s}")
        print("  " + "-" * 60)

        for name, pops, tr in [
            ("Periodic", pop_per, tree),
            ("Möbius twist", pop_mob, tree),
            ("Möbius filter", pop_filt, tree_filtered),
            ("Twist + filter", pop_both, tree_filtered),
        ]:
            total = sum(pops[f] for f in tr)
            odd_q = sum(pops[f] for f in tr if f.denominator % 2 == 1)
            even_q = sum(pops[f] for f in tr if f.denominator % 2 == 0)
            r = odd_q / even_q if even_q > 0 else float('inf')
            print(f"  {name:>25s}  {odd_q/total:10.4f}  {even_q/total:10.4f}  {r:10.4f}")

    print(f"\n{'=' * 80}")
    print("  DONE")
    print(f"{'=' * 80}")
