#!/usr/bin/env python3
"""
Gate duty cycle as coupling constant dictionary.

D31 identifies the speed of light as the gate propagation speed.
The coupling constant α should be the gate DUTY CYCLE — the fraction
of time a sector's gate is open for information exchange:

    duty(q) = w(q, K) / T(q)

where w is the tongue width (gate duration) and T = q is the orbit
period (gate repetition).

At K=1 (critical):  w = 1/q²,  T = q  →  duty = 1/q³

Bare ratio:  duty(2)/duty(3) = 27/8 = 3.375
Observed:    α_s/α_W at M_Z  ≈ 0.118/0.034 ≈ 3.47

This script:
  1. Computes duty cycles on the Stern-Brocot tree at various K
  2. Solves the Klein bottle field equation and extracts sector duties
  3. Compares duty ratios to gauge coupling ratios
  4. Tests whether exp(π/2) topological correction explains the running

Usage:
    python3 sync_cost/derivations/gate_duty_cycle.py
"""

import math
import os
import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(__file__))
from framework_constants import ALPHA_EM_MZ, ALPHA_S_MZ, SIN2_TW_MZ
from circle_map_utils import PHI, INV_PHI, PHI_SQ, LN_PHI_SQ, tongue_width


# ── Physical constants ────────────────────────────────────────────────────────

ALPHA_W_MZ = 1 / 29.587    # α₂ = g²/(4π), sin²θ_W = 0.2312
SIN2_TW = SIN2_TW_MZ       # sin²θ_W at M_Z

# Derived
ALPHA_2_MZ = ALPHA_EM_MZ / SIN2_TW       # SU(2) coupling
ALPHA_1_MZ = ALPHA_EM_MZ / (1 - SIN2_TW) # U(1) coupling (GUT normalized: 5/3 × this)

RATIO_32_MZ = ALPHA_S_MZ / ALPHA_2_MZ    # α₃/α₂ at M_Z


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


# ── Gate duty cycle ───────────────────────────────────────────────────────────

def gate_duty(p, q, K):
    """
    Duty cycle = tongue_width / period.

    The gate opens once per orbit (period = q iterations).
    The gate duration is proportional to the tongue width.
    """
    w = tongue_width(p, q, K)
    if q == 0:
        return 0.0
    return w / q


# ── Klein bottle field equation ───────────────────────────────────────────────

def solve_klein_field_equation(tree_1d, K0, g_func, n_iter=300,
                                symmetric_coupling=True):
    """
    2D field equation on the Klein bottle with XOR parity filter.

    Modes (f1, f2) survive iff q1%2 != q2%2 (XOR on denominator parity).

    If symmetric_coupling: K_eff = K0/2 in both directions (non-orientable).
    The asymmetry comes from antiperiodic BC suppression of odd-q modes.
    """
    # Build 2D mode space with XOR filter
    modes = []
    for f1 in tree_1d:
        for f2 in tree_1d:
            q1, q2 = f1.denominator, f2.denominator
            if (q1 % 2) != (q2 % 2):  # XOR filter
                modes.append((f1, f2))

    populations = {m: 1.0 for m in modes}
    N_total = len(modes)

    for it in range(n_iter):
        # Order parameter with twist
        r = 0.0 + 0j
        total_pop = sum(populations.values())
        for (f1, f2), pop in populations.items():
            twist = (-1) ** f1.denominator  # antiperiodic direction
            r += pop * math.e ** (2j * math.pi * (float(f1) + float(f2))) * twist
        r /= max(total_pop, 1e-15)
        r_abs = abs(r)

        if symmetric_coupling:
            K_eff = K0 / 2 * max(r_abs, 1e-15)
        else:
            K_eff = K0 * max(r_abs, 1e-15)

        # Update populations
        new_pop = {}
        for (f1, f2) in modes:
            p1, q1 = f1.numerator, f1.denominator
            p2, q2 = f2.numerator, f2.denominator
            g = g_func(float(f1), float(f2))
            w1 = tongue_width(p1, q1, K_eff)
            w2 = tongue_width(p2, q2, K_eff)

            # Antiperiodic BC suppression for odd-q in twist direction
            bc_factor = 1.0
            if q1 % 2 == 1:  # odd q in antiperiodic direction
                delta = min(abs(float(f1) - (n + 0.5))
                            for n in range(q1 + 1))
                bc_factor = math.exp(-math.pi * q1 * delta)

            new_pop[(f1, f2)] = N_total * g * w1 * w2 * bc_factor

        # Normalize
        total = sum(new_pop.values())
        if total > 0:
            for m in new_pop:
                new_pop[m] *= N_total / total
        populations = new_pop

    return populations, r


def classify_sectors(populations):
    """Group populations by (q1, q2) denominator class."""
    sectors = {}
    for (f1, f2), pop in populations.items():
        q1, q2 = f1.denominator, f2.denominator
        key = (q1, q2)
        if key not in sectors:
            sectors[key] = {"pop": 0.0, "count": 0, "modes": [],
                            "duty_sum": 0.0}
        sectors[key]["pop"] += pop
        sectors[key]["count"] += 1
        sectors[key]["modes"].append((f1, f2, pop))
    return sectors


def sector_duty_cycle(sectors, K_eff):
    """Compute aggregate gate duty cycle per sector."""
    result = {}
    for (q1, q2), data in sectors.items():
        total_duty = 0.0
        for f1, f2, pop in data["modes"]:
            p1 = f1.numerator
            p2 = f2.numerator
            d1 = gate_duty(p1, q1, K_eff)
            d2 = gate_duty(p2, q2, K_eff)
            # Combined duty: both gates must be open simultaneously
            # For independent gates: duty_combined = d1 × d2
            # Weighted by population (how many oscillators use this gate)
            total_duty += pop * d1 * d2
        result[(q1, q2)] = total_duty
    return result


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("=" * 80)
    print("  GATE DUTY CYCLE AS COUPLING CONSTANT")
    print("  Testing α_q ∝ duty(q) = w(q,K)/q")
    print("=" * 80)

    # ── Part 1: Bare duty cycle ratios ────────────────────────────────────
    print(f"\n{'─' * 80}")
    print("  1. BARE DUTY CYCLES (single mode, no Klein bottle)")
    print(f"{'─' * 80}\n")

    print(f"  {'q':>4s}  {'w(1/q, K=1)':>14s}  {'T = q':>6s}  "
          f"{'duty = w/q':>14s}  {'1/q³':>14s}  {'match':>8s}")
    print("  " + "-" * 68)

    for q in range(1, 8):
        p = 1
        w = tongue_width(p, q, 1.0)
        T = q
        duty = w / T
        bare = 1.0 / (q ** 3)
        match = abs(duty - bare) / max(bare, 1e-15)
        print(f"  {q:4d}  {w:14.6e}  {T:6d}  {duty:14.6e}  "
              f"{bare:14.6e}  {match:8.2%}")

    duty_2 = tongue_width(1, 2, 1.0) / 2
    duty_3 = tongue_width(1, 3, 1.0) / 3
    bare_ratio = duty_2 / duty_3
    print(f"\n  duty(q=2) / duty(q=3) = {bare_ratio:.6f}")
    print(f"  27/8                   = {27/8:.6f}")
    print(f"  α_s/α₂ at M_Z         = {RATIO_32_MZ:.6f}")
    print(f"  Δ(bare vs observed)    = {abs(bare_ratio - RATIO_32_MZ)/RATIO_32_MZ:.1%}")

    # ── Part 2: Duty cycle vs K ───────────────────────────────────────────
    print(f"\n{'─' * 80}")
    print("  2. DUTY CYCLE RATIO vs COUPLING K")
    print(f"{'─' * 80}\n")

    print(f"  {'K':>8s}  {'duty(2)':>14s}  {'duty(3)':>14s}  "
          f"{'ratio':>10s}  {'vs α_s/α₂':>10s}")
    print("  " + "-" * 62)

    K_vals = [0.3, 0.5, 0.7, 0.8, 0.9, 0.95, 1.0]
    for K in K_vals:
        d2 = tongue_width(1, 2, K) / 2
        d3 = tongue_width(1, 3, K) / 3
        if d3 > 0:
            ratio = d2 / d3
            delta = abs(ratio - RATIO_32_MZ) / RATIO_32_MZ
        else:
            ratio = float('inf')
            delta = float('inf')
        print(f"  {K:8.3f}  {d2:14.6e}  {d3:14.6e}  "
              f"{ratio:10.4f}  {delta:10.1%}")

    # ── Part 3: Klein bottle field equation ───────────────────────────────
    print(f"\n{'─' * 80}")
    print("  3. KLEIN BOTTLE: SECTOR DUTY CYCLES AT FIXED POINT")
    print(f"{'─' * 80}")

    DEPTH = 6
    tree = stern_brocot_tree(DEPTH)
    print(f"\n  Tree depth: {DEPTH}, nodes: {len(tree)}")

    g_golden = lambda o1, o2: math.exp(-5 * ((o1 + o2) / 2 - INV_PHI) ** 2)
    g_uniform = lambda o1, o2: 1.0

    for g_name, g_func in [("uniform", g_uniform), ("golden-peaked", g_golden)]:
        print(f"\n  ── g = {g_name} ──")
        populations, r = solve_klein_field_equation(
            tree, K0=1.0, g_func=g_func, n_iter=400, symmetric_coupling=True
        )
        K_eff = abs(r) / 2  # symmetric coupling: K0/2 × |r|

        sectors = classify_sectors(populations)
        duties = sector_duty_cycle(sectors, K_eff)

        print(f"  |r| = {abs(r):.6f},  K_eff = {K_eff:.6f}")
        print(f"\n  {'sector':>10s}  {'pop':>12s}  {'modes':>6s}  "
              f"{'duty':>14s}  {'duty/mode':>14s}")
        print("  " + "-" * 65)

        for key in sorted(sectors.keys()):
            pop = sectors[key]["pop"]
            cnt = sectors[key]["count"]
            duty = duties.get(key, 0)
            dpm = duty / cnt if cnt > 0 else 0
            print(f"  ({key[0]},{key[1]}){' ':>5s}  {pop:12.4f}  {cnt:6d}  "
                  f"{duty:14.6e}  {dpm:14.6e}")

        # Extract key sector duties
        d_23 = duties.get((2, 3), 0)
        d_32 = duties.get((3, 2), 0)
        d_25 = duties.get((2, 5), 0)
        d_52 = duties.get((5, 2), 0)

        if d_32 > 0 and d_23 > 0:
            ratio_23_32 = d_23 / d_32
            print(f"\n  duty(2,3) / duty(3,2) = {ratio_23_32:.6f}")
            print(f"  exp(π/2)              = {math.exp(math.pi/2):.6f}")
            print(f"  α_s/α₂ at M_Z         = {RATIO_32_MZ:.6f}")

        # Total duty by denominator class
        duty_even_first = sum(v for (q1, q2), v in duties.items() if q1 % 2 == 0)
        duty_odd_first = sum(v for (q1, q2), v in duties.items() if q1 % 2 == 1)
        if duty_odd_first > 0:
            print(f"\n  Total duty (even-q₁) / (odd-q₁) = "
                  f"{duty_even_first / duty_odd_first:.6f}")

    # ── Part 4: The 1/q³ prediction ──────────────────────────────────────
    print(f"\n{'─' * 80}")
    print("  4. THE 1/q³ PREDICTION: COUPLING RATIOS FROM DUTY CYCLES")
    print(f"{'─' * 80}\n")

    print("  If α_q ∝ 1/q³ (gate duty cycle at K=1):")
    print()

    alpha_ratios = {
        "α₃/α₂": (2, 3),
        "α₅/α₂": (2, 5),
        "α₅/α₃": (3, 5),
        "α₇/α₂": (2, 7),
    }

    print(f"  {'ratio':>10s}  {'1/q_a³ / 1/q_b³':>18s}  {'= q_b³/q_a³':>14s}")
    print("  " + "-" * 48)

    for name, (qa, qb) in alpha_ratios.items():
        val = (qb ** 3) / (qa ** 3)
        print(f"  {name:>10s}  {qa}³/{qb}³ = {qa**3}/{qb**3}  "
              f"{'':>4s}{val:10.4f}")

    print(f"\n  Observed coupling ratios at M_Z:")
    print(f"    α_s(M_Z)  = {ALPHA_S_MZ:.4f}")
    print(f"    α₂(M_Z)   = {ALPHA_2_MZ:.6f}")
    print(f"    α₁(M_Z)   = {ALPHA_1_MZ:.6f}  (not GUT-normalized)")
    print(f"    α_s/α₂    = {RATIO_32_MZ:.4f}")
    print(f"    27/8       = {27/8:.4f}  (bare duty ratio)")
    print(f"    Δ          = {abs(27/8 - RATIO_32_MZ)/RATIO_32_MZ:.1%}")

    # ── Part 5: What exp(π/2) would mean ─────────────────────────────────
    print(f"\n{'─' * 80}")
    print("  5. TOPOLOGICAL CORRECTION: exp(π/2)")
    print(f"{'─' * 80}\n")

    ep2 = math.exp(math.pi / 2)
    emp2 = math.exp(-math.pi / 2)

    print(f"  exp(π/2)  = {ep2:.6f}")
    print(f"  exp(-π/2) = {emp2:.6f}")
    print()
    print("  Possible roles of exp(π/2) = 4.8105:")
    print()

    # Test: is the population ratio (exp(π/2)) related to the duty ratio (27/8)?
    print(f"  A. Population ratio exp(π/2) IS the coupling ratio:")
    print(f"     α_s/α₂ = exp(π/2) = {ep2:.4f}  vs observed {RATIO_32_MZ:.4f}"
          f"  Δ = {abs(ep2 - RATIO_32_MZ)/RATIO_32_MZ:.1%}")
    print()
    print(f"  B. Duty ratio (27/8) corrected by topological suppression:")
    print(f"     α_s/α₂ = (27/8) × exp(-π/2) × exp(π/2)")
    print(f"     [The suppression and enhancement cancel for the RATIO]")
    print(f"     → still 27/8 = {27/8:.4f}")
    print()
    print(f"  C. Duty cycle WITH topological modulation:")
    print(f"     duty(q=2, even) = (1/8)  [no suppression, even-q]")
    print(f"     duty(q=3, odd)  = (1/27) × exp(-π/2)  [suppressed by twist]")
    ratio_c = (1/8) / ((1/27) * emp2)
    print(f"     ratio = (1/8) / [(1/27) × exp(-π/2)]")
    print(f"           = (27/8) × exp(π/2)")
    print(f"           = {27/8 * ep2:.4f}")
    print(f"     vs observed {RATIO_32_MZ:.4f}  Δ = {abs(27/8 * ep2 - RATIO_32_MZ)/RATIO_32_MZ:.0%}")
    print(f"     [Too large — the topological factor amplifies, not corrects]")
    print()
    print(f"  D. Inverse: α ∝ 1/duty (coupling = inverse availability):")
    print(f"     α_q ∝ q³  [more complex modes couple MORE strongly]")
    print(f"     α₃/α₂ = 8/27 = {8/27:.4f}  vs observed {RATIO_32_MZ:.4f}")
    print(f"     [Wrong direction — strong coupling is STRONGER, not weaker]")
    print()
    print(f"  E. Mixed: α ∝ duty × coherence:")
    print(f"     If coherence(q=2)/coherence(q=3) ≈ {RATIO_32_MZ / (27/8):.4f}")
    print(f"     then duty × coherence reproduces α_s/α₂.")
    print(f"     This factor = {RATIO_32_MZ / (27/8):.4f} ≈ 1 + 3%")
    print(f"     [Coherence correction is small — duty does most of the work]")

    # ── Part 6: sin²θ_W prediction ───────────────────────────────────────
    print(f"\n{'─' * 80}")
    print("  6. sin²θ_W FROM DUTY CYCLES")
    print(f"{'─' * 80}\n")

    # In GUT normalization: α₁_GUT = (5/3) × α₁
    # sin²θ_W = α₁_GUT / (α₁_GUT + α₂) at unification
    # If α₁ comes from q=1 (the root, the mean field):
    # duty(q=1) = w(1,1,K=1)/1 = 1/(2π) ≈ 0.159 (from tongue_width formula)

    d1 = tongue_width(1, 1, 1.0)  # q=1 tongue width at K=1
    d2_bare = tongue_width(1, 2, 1.0) / 2
    d3_bare = tongue_width(1, 3, 1.0) / 3

    print(f"  duty(q=1) = {d1:.6f}  [= K/(2π) = 1/(2π) at K=1]")
    print(f"  duty(q=2) = {d2_bare:.6f}  [= 1/8]")
    print(f"  duty(q=3) = {d3_bare:.6f}  [= 1/27]")
    print()

    # sin²θ_W = α₁/(α₁ + α₂) at tree scale
    # If α ∝ duty: sin²θ_W = duty(1) / (duty(1) + duty(2))
    s2tw_tree = d1 / (d1 + d2_bare)
    print(f"  sin²θ_W (tree scale, α ∝ duty):")
    print(f"    = duty(1) / [duty(1) + duty(2)]")
    print(f"    = {d1:.4f} / [{d1:.4f} + {d2_bare:.4f}]")
    print(f"    = {s2tw_tree:.6f}")
    print(f"  Observed at M_Z: {SIN2_TW:.6f}")
    print(f"  Δ = {abs(s2tw_tree - SIN2_TW)/SIN2_TW:.1%}")

    # Alternative: GUT normalization with factor 5/3
    s2tw_gut = (5/3 * d1) / (5/3 * d1 + d2_bare)
    print(f"\n  With GUT normalization (5/3 × α₁):")
    print(f"    = {5/3 * d1:.4f} / [{5/3 * d1:.4f} + {d2_bare:.4f}]")
    print(f"    = {s2tw_gut:.6f}")
    print(f"  GUT prediction: 3/8 = {3/8:.6f}")
    print(f"  Δ from 3/8 = {abs(s2tw_gut - 3/8)/(3/8):.1%}")

    # Alternative: duty ratio directly
    # sin²θ_W = 1 / (1 + α₂/α₁) = 1 / (1 + duty(2)/duty(1))
    s2tw_direct = 1 / (1 + d2_bare / d1)
    print(f"\n  Direct: sin²θ_W = 1/(1 + duty(2)/duty(1))")
    print(f"    = 1/(1 + {d2_bare/d1:.4f})")
    print(f"    = {s2tw_direct:.6f}")

    # ── Summary ───────────────────────────────────────────────────────────
    print(f"\n{'=' * 80}")
    print("  SUMMARY")
    print(f"{'=' * 80}")
    print(f"""
  Gate duty cycle: duty(q) = w(q, K) / q = 1/q³ at K=1.

  COUPLING RATIO TEST:
    duty(q=2)/duty(q=3) = 27/8 = 3.375
    α_s/α₂ at M_Z       = {RATIO_32_MZ:.3f}
    Δ                    = {abs(27/8 - RATIO_32_MZ)/RATIO_32_MZ:.1%}

  WEINBERG ANGLE TEST:
    duty(q=1)/[duty(q=1)+duty(q=2)] = {s2tw_tree:.4f}
    sin²θ_W at M_Z                   = {SIN2_TW:.4f}
    Δ                                 = {abs(s2tw_tree - SIN2_TW)/SIN2_TW:.1%}

  The duty cycle dictionary (α ∝ 1/q³) reproduces the strong/weak
  coupling ratio to 3% without any free parameters. The residual
  may come from:
    - Coherence correction (sector phase alignment)
    - Running from tree scale to M_Z
    - Klein bottle topological modulation

  The Weinberg angle test ({abs(s2tw_tree - SIN2_TW)/SIN2_TW:.1%} off) depends on whether
  the q=1 sector maps to U(1), which requires the root mode to
  participate as a gauge coupling rather than as the background medium.
""")


if __name__ == "__main__":
    main()
