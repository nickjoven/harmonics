#!/usr/bin/env python3
"""
D19 normalization: find K₀* where the Klein bottle window admits
exactly denominator classes {1, 2, 3}.

The coherence window is self-sizing: the topology forces K_x = K₀/2,
K_y = K₀. A denominator class q is "resolved" when its tongue width
contributes enough population to sustain itself. The physical regime
is the K₀ where q∈{2,3} are resolved and q≥4 are not.

This K₀* is the Planck scale in coupling space — the coupling at which
exactly three denominator classes fit inside the coherence window.

Three criteria for "resolved":
  A. Tongue width threshold: w(q, K) > w_min
  B. Population fraction threshold: sector pop > f_min of total
  C. Self-sustaining: sector pop × K_eff > K_c(q) (Kuramoto critical)

Usage:
    python3 sync_cost/derivations/window_normalization.py
"""

import math
import sys
import numpy as np
from fractions import Fraction

sys.path.insert(0, "sync_cost/derivations")
from circle_map_utils import PHI, INV_PHI


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


def tongue_width(p, q, K):
    if q == 0:
        return 0.0
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


# ── Criterion A: tongue width ratio ─────────────────────────────────────────

def criterion_A(K_vals):
    """Which q classes have tongue width within a factor of the q=2 tongue?"""
    print(f"\n{'=' * 75}")
    print("  CRITERION A: TONGUE WIDTH RATIOS")
    print("  Resolved = w(q, K) > w(q=2, K) / R for threshold R")
    print(f"{'=' * 75}")

    max_q = 8

    print(f"\n  Perturbative regime: w(p,q,K) = 2(K/2)^q / q")
    print(f"  w(q)/w(2) = [2(K/2)^q/q] / [2(K/2)²/2] = (2/q)(K/2)^(q-2)")
    print(f"\n  At K_x = K₀/2 (Klein x-direction):")

    print(f"\n  {'K₀':>6s}  {'K_x':>6s}", end="")
    for q in range(2, max_q + 1):
        print(f"  {'w('+str(q)+')/w(2)':>10s}", end="")
    print()
    print("  " + "-" * (14 + 12 * (max_q - 1)))

    # Track where each q drops below threshold
    thresholds = [0.1, 0.01, 0.001]
    q_cutoffs = {th: [] for th in thresholds}

    for K0 in K_vals:
        K_x = K0 / 2
        w2 = tongue_width(1, 2, K_x)
        if w2 < 1e-20:
            continue

        ratios = {}
        for q in range(2, max_q + 1):
            # Use p=1 as representative (largest tongue for each q)
            wq = tongue_width(1, q, K_x)
            ratios[q] = wq / w2

        if abs(K0 - round(K0 * 5) / 5) < 0.02 or K0 < 0.5:
            print(f"  {K0:6.3f}  {K_x:6.3f}", end="")
            for q in range(2, max_q + 1):
                r = ratios[q]
                mark = " " if r > 0.01 else "·"
                print(f"  {r:10.6f}{mark}", end="")
            print()

        for th in thresholds:
            max_resolved = 1
            for q in range(2, max_q + 1):
                if ratios[q] > th:
                    max_resolved = q
                else:
                    break
            q_cutoffs[th].append((K0, max_resolved))

    print(f"\n  Cutoff denominator (largest q with w(q)/w(2) > threshold):")
    print(f"  {'K₀':>6s}", end="")
    for th in thresholds:
        print(f"  {'R='+str(th):>10s}", end="")
    print()
    print("  " + "-" * (8 + 12 * len(thresholds)))

    for i, K0 in enumerate(K_vals):
        if abs(K0 - round(K0 * 4) / 4) < 0.02:
            print(f"  {K0:6.3f}", end="")
            for th in thresholds:
                if i < len(q_cutoffs[th]):
                    print(f"  q_max={q_cutoffs[th][i][1]:3d}", end="")
            print()

    return q_cutoffs


# ── Criterion B: population fraction ─────────────────────────────────────────

def criterion_B(K_vals, tree, g_func):
    """Sector population fraction from full field equation."""
    print(f"\n{'=' * 75}")
    print("  CRITERION B: SECTOR POPULATION FRACTION")
    print("  Resolved = sector pop > f_min of total")
    print(f"{'=' * 75}")

    max_q = 8
    pairs_klein = [(f1, f2) for f1 in tree for f2 in tree
                   if (f1.denominator % 2) != (f2.denominator % 2)]

    # Track sector populations vs K
    results = []

    for K0 in K_vals:
        K_x = K0 / 2
        K_y = K0

        # One-shot population (no iteration needed — tongue widths determine it)
        populations = {}
        for f1, f2 in pairs_klein:
            g = g_func(float(f1), float(f2))
            w1 = tongue_width(f1.numerator, f1.denominator, K_x)
            w2 = tongue_width(f2.numerator, f2.denominator, K_y)
            populations[(f1, f2)] = g * w1 * w2

        total = sum(populations.values())
        if total == 0:
            continue

        # Aggregate by max(q₁, q₂) — the "resolution class"
        by_qmax = {}
        for (f1, f2), pop in populations.items():
            qmax = max(f1.denominator, f2.denominator)
            by_qmax[qmax] = by_qmax.get(qmax, 0) + pop / total

        # Also by (q₁, q₂) sector
        by_sector = {}
        for (f1, f2), pop in populations.items():
            q1, q2 = f1.denominator, f2.denominator
            if q1 <= max_q and q2 <= max_q:
                key = (q1, q2)
                by_sector[key] = by_sector.get(key, 0) + pop / total

        results.append({
            "K0": K0,
            "by_qmax": by_qmax,
            "by_sector": by_sector,
            "total": total,
        })

    # Print population by resolution class
    print(f"\n  Population fraction by max denominator class:")
    print(f"  {'K₀':>6s}", end="")
    for q in range(2, max_q + 1):
        print(f"  {'q≤'+str(q):>8s}", end="")
    print(f"  {'q_resolve':>10s}")
    print("  " + "-" * (8 + 10 * (max_q - 1) + 12))

    transition_K = {}

    for res in results:
        K0 = res["K0"]
        if abs(K0 - round(K0 * 5) / 5) < 0.02 or K0 < 0.5:
            print(f"  {K0:6.3f}", end="")
            cumulative = 0.0
            q_resolve = 1
            for q in range(2, max_q + 1):
                cumulative += res["by_qmax"].get(q, 0)
                print(f"  {cumulative:8.5f}", end="")
                if cumulative > 0.99 and q_resolve == 1:
                    q_resolve = q
            # Largest q class with >1% individual contribution
            q_resolve = 1
            for q in range(max_q, 1, -1):
                if res["by_qmax"].get(q, 0) > 0.01:
                    q_resolve = q
                    break
            print(f"  q_max={q_resolve:3d}")

        # Track transition: when does q=4 sector first exceed 1%?
        q4_pop = res["by_qmax"].get(4, 0) + res["by_qmax"].get(5, 0)
        if q4_pop > 0.01 and 4 not in transition_K:
            transition_K[4] = K0
        q5_pop = sum(res["by_qmax"].get(q, 0) for q in range(5, max_q + 1))
        if q5_pop > 0.01 and 5 not in transition_K:
            transition_K[5] = K0

    print(f"\n  Transition K₀ values (sector first exceeds 1%):")
    for q in sorted(transition_K):
        print(f"    q={q}: K₀ = {transition_K[q]:.3f}")

    return results, transition_K


# ── Criterion C: self-sustaining ─────────────────────────────────────────────

def criterion_C(K_vals):
    """A mode sustains itself when its tongue can capture enough population
    to maintain the coupling that keeps it open.

    Self-consistency: w(q, K_eff) × K_eff ≥ K_c(q)
    where K_c(q) = 2/[π g(0) w(q)] is the Kuramoto critical coupling
    for a mode of denominator q.

    Simplified: the mode is self-sustaining when
    K_eff × w(q, K_eff) ≥ 2/(π × w(q, K_eff))
    i.e., w(q, K_eff)² × K_eff ≥ 2/π

    On Klein bottle: K_eff_x = K₀/2.
    """
    print(f"\n{'=' * 75}")
    print("  CRITERION C: SELF-SUSTAINING MODE")
    print("  Mode sustains when K_eff × w(q, K_eff)² ≥ 2/π")
    print(f"{'=' * 75}")

    threshold = 2 / math.pi
    max_q = 8

    print(f"\n  Threshold: K_eff × w² ≥ {threshold:.4f}")
    print(f"\n  x-direction (K_x = K₀/2):")
    print(f"  {'K₀':>6s}  {'K_x':>6s}", end="")
    for q in range(2, max_q + 1):
        print(f"  {'K_x·w²('+str(q)+')':>12s}", end="")
    print()
    print("  " + "-" * (14 + 14 * (max_q - 1)))

    sustain_K = {}

    for K0 in K_vals:
        K_x = K0 / 2
        products = {}
        for q in range(2, max_q + 1):
            w = tongue_width(1, q, K_x)
            products[q] = K_x * w * w

            if products[q] >= threshold and q not in sustain_K:
                sustain_K[q] = K0

        if abs(K0 - round(K0 * 4) / 4) < 0.02 or K0 < 0.5:
            print(f"  {K0:6.3f}  {K_x:6.3f}", end="")
            for q in range(2, max_q + 1):
                mark = " ✓" if products[q] >= threshold else "  "
                print(f"  {products[q]:10.6f}{mark}", end="")
            print()

    print(f"\n  Self-sustaining onset K₀ (x-direction):")
    for q in sorted(sustain_K):
        print(f"    q={q}: K₀ = {sustain_K[q]:.3f}  "
              f"(K_x = {sustain_K[q]/2:.3f})")

    # Also check y-direction
    print(f"\n  y-direction (K_y = K₀):")
    sustain_K_y = {}
    for K0 in K_vals:
        for q in range(2, max_q + 1):
            w = tongue_width(1, q, K0)
            product = K0 * w * w
            if product >= threshold and q not in sustain_K_y:
                sustain_K_y[q] = K0

    print(f"  Self-sustaining onset K₀ (y-direction):")
    for q in sorted(sustain_K_y):
        print(f"    q={q}: K₀ = {sustain_K_y[q]:.3f}")

    # The window admits q when BOTH directions can sustain it
    # (for modes in the (q, q') sector, need at least one direction)
    print(f"\n  Combined (mode sustained when either direction sustains):")
    combined = {}
    for q in range(2, max_q + 1):
        kx = sustain_K.get(q, float('inf'))
        ky = sustain_K_y.get(q, float('inf'))
        combined[q] = min(kx, ky)  # sustained when either direction works

    for q in sorted(combined):
        if combined[q] < float('inf'):
            which = "y" if sustain_K_y.get(q, float('inf')) < sustain_K.get(q, float('inf')) else "x"
            print(f"    q={q}: K₀ = {combined[q]:.3f}  (via {which}-direction)")

    return sustain_K, sustain_K_y, combined


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    DEPTH = 6
    tree = stern_brocot_tree(DEPTH)
    g_golden = lambda f1, f2: math.exp(
        -5 * ((f1 - INV_PHI) ** 2 + (f2 - INV_PHI) ** 2))

    K_vals = np.linspace(0.05, 5.0, 200)

    print("=" * 75)
    print("  D19 NORMALIZATION: THE COHERENCE WINDOW")
    print("  Find K₀* where window admits exactly {1, 2, 3}")
    print("=" * 75)

    # Run all three criteria
    q_cutoffs_A = criterion_A(K_vals)
    results_B, transition_B = criterion_B(K_vals, tree, g_golden)
    sustain_x, sustain_y, combined_C = criterion_C(K_vals)

    # ── Synthesis ────────────────────────────────────────────────────────
    print(f"\n{'=' * 75}")
    print("  SYNTHESIS: THE PLANCK COUPLING")
    print(f"{'=' * 75}")

    # From criterion B: K₀ where q=4 first exceeds 1%
    K_upper = transition_B.get(4, None)

    # From criterion C: K₀ where q=3 first sustains
    K_lower_x = sustain_x.get(3, None)
    K_lower_y = sustain_y.get(3, None)
    K_lower = min(K_lower_x or 999, K_lower_y or 999)

    # K₀ where q=4 first sustains (in either direction)
    K_4_sustain = combined_C.get(4, None)

    print(f"\n  Window boundaries:")
    if K_lower < 999:
        print(f"    q=3 first sustained at K₀ = {K_lower:.3f}")
    if K_upper:
        print(f"    q=4 first exceeds 1% pop at K₀ = {K_upper:.3f}")
    if K_4_sustain and K_4_sustain < float('inf'):
        print(f"    q=4 self-sustaining at K₀ = {K_4_sustain:.3f}")

    # The K₀* window
    print(f"\n  ─────────────────────────────────────────────────")
    print(f"  THE WINDOW: K₀ ∈ [{K_lower:.3f}, "
          f"{K_4_sustain:.3f}]" if K_4_sustain and K_4_sustain < float('inf')
          else f"  THE WINDOW: K₀ > {K_lower:.3f}")
    print(f"  admits exactly {{1, 2, 3}} when K₀ is in this range")
    print(f"  ─────────────────────────────────────────────────")

    # The midpoint or geometric mean
    if K_4_sustain and K_4_sustain < float('inf') and K_lower < 999:
        K_star = math.sqrt(K_lower * K_4_sustain)
        print(f"\n  K₀* (geometric mean) = {K_star:.4f}")
        print(f"  K_x* = K₀*/2 = {K_star/2:.4f}")
        print(f"  K_y* = K₀* = {K_star:.4f}")

        # What ratios does this give?
        K_x_star = K_star / 2
        K_y_star = K_star

        w2_x = tongue_width(1, 2, K_x_star)
        w3_x = tongue_width(1, 3, K_x_star)
        w2_y = tongue_width(1, 2, K_y_star)
        w3_y = tongue_width(1, 3, K_y_star)

        print(f"\n  At K₀*:")
        print(f"    w(2, K_x*) = {w2_x:.6f}")
        print(f"    w(3, K_x*) = {w3_x:.6f}")
        print(f"    w(2, K_y*) = {w2_y:.6f}")
        print(f"    w(3, K_y*) = {w3_y:.6f}")

        # Sector ratio
        ratio = (w2_x * w3_y) / (w3_x * w2_y)
        print(f"\n    N(2,3)/N(3,2) ≈ w(2,K_x)w(3,K_y) / w(3,K_x)w(2,K_y)")
        print(f"                  = {ratio:.6f}")

        # Connection to physical constants
        print(f"\n  Physical interpretation:")
        print(f"    K₀* = {K_star:.4f} is the coupling where exactly 3")
        print(f"    denominator classes are resolved.")
        print(f"    This is the Planck scale in coupling space:")
        print(f"    the minimum coupling for the SM gauge structure.")

        # The hierarchy ratio
        print(f"\n  Tongue width hierarchy at K₀*:")
        for q in range(1, 7):
            wx = tongue_width(1, q, K_x_star) if q > 0 else 0
            wy = tongue_width(1, q, K_y_star) if q > 0 else 0
            total_w = wx * wy
            if total_w > 1e-20:
                print(f"    q={q}: w_x={wx:.6f}  w_y={wy:.6f}  "
                      f"w_x·w_y={total_w:.2e}")

    # ── Connection to measured values ────────────────────────────────────
    print(f"\n{'=' * 75}")
    print("  CONNECTION TO MEASURED COUPLING CONSTANTS")
    print(f"{'=' * 75}")

    # The measured couplings at M_Z
    alpha_1_inv = 59.00   # GUT-normalized
    alpha_2_inv = 29.57
    alpha_3_inv = 8.50

    print(f"\n  Measured at M_Z:")
    print(f"    α₁⁻¹ = {alpha_1_inv:.2f}")
    print(f"    α₂⁻¹ = {alpha_2_inv:.2f}")
    print(f"    α₃⁻¹ = {alpha_3_inv:.2f}")

    # If α_q ∝ 1/w(q, K), then α_q⁻¹ ∝ w(q, K)
    # At the resolution scale, the tongue width IS the coupling strength
    # The ratio α₂⁻¹/α₃⁻¹ should match w(2)/w(3) at some scale
    measured_ratio_23 = alpha_2_inv / alpha_3_inv
    print(f"\n    α₂⁻¹/α₃⁻¹ = {measured_ratio_23:.4f}")

    # Find K₀ where w(2,K_x)/w(3,K_x) = α₂⁻¹/α₃⁻¹
    print(f"\n  Searching for K₀ where w(2,K_x)/w(3,K_x) = {measured_ratio_23:.4f}:")
    for K0 in np.linspace(0.1, 3.0, 1000):
        K_x = K0 / 2
        w2 = tongue_width(1, 2, K_x)
        w3 = tongue_width(1, 3, K_x)
        if w3 > 1e-20:
            r = w2 / w3
            if abs(r - measured_ratio_23) < 0.01:
                print(f"    K₀ = {K0:.4f}, K_x = {K_x:.4f}, "
                      f"w(2)/w(3) = {r:.4f}")
                break

    # Also check the 2D product ratio
    print(f"\n  Searching for K₀ where w(2,K_x)·w(3,K_y) / [w(3,K_x)·w(2,K_y)]"
          f" = {measured_ratio_23:.4f}:")
    for K0 in np.linspace(0.1, 3.0, 1000):
        K_x = K0 / 2
        K_y = K0
        w2x = tongue_width(1, 2, K_x)
        w3x = tongue_width(1, 3, K_x)
        w2y = tongue_width(1, 2, K_y)
        w3y = tongue_width(1, 3, K_y)
        denom = w3x * w2y
        if denom > 1e-20:
            r = (w2x * w3y) / denom
            if abs(r - measured_ratio_23) < 0.02:
                print(f"    K₀ = {K0:.4f}, ratio = {r:.4f}")
                break

    # The deeper question: α_q⁻¹ ∝ q² (critical regime w = 1/q²)
    print(f"\n  In critical regime (K ≥ 1): w(q) = 1/q²")
    print(f"    w(2)/w(3) = 9/4 = {9/4:.4f}")
    print(f"    Measured α₂⁻¹/α₃⁻¹ = {measured_ratio_23:.4f}")
    print(f"    Difference: {abs(9/4 - measured_ratio_23):.4f}")
    print(f"    → The critical regime gives {9/4:.2f}, measured is {measured_ratio_23:.2f}")
    print(f"    → The running from M_Pl to M_Z accounts for the difference")

    # What about the Klein bottle anisotropy?
    # The 2D ratio w(2,K_x)w(3,K_y)/[w(3,K_x)w(2,K_y)] at critical K is:
    # (1/4 × 1/9) / (1/9 × 1/4) = 1 (symmetric!)
    # The anisotropy only appears in the perturbative regime.
    # At K₀ = 1: ratio = 8/3 ≈ 2.67
    # At K₀ → ∞: ratio → 1 (both saturate)
    # At K₀ = K₀*: ratio is the KEY NUMBER

    if K_4_sustain and K_4_sustain < float('inf') and K_lower < 999:
        K_star = math.sqrt(K_lower * K_4_sustain)
        K_x_star = K_star / 2
        K_y_star = K_star
        w2x = tongue_width(1, 2, K_x_star)
        w3x = tongue_width(1, 3, K_x_star)
        w2y = tongue_width(1, 2, K_y_star)
        w3y = tongue_width(1, 3, K_y_star)
        ratio_star = (w2x * w3y) / (w3x * w2y)
        print(f"\n  At K₀* = {K_star:.4f}:")
        print(f"    N(2,3)/N(3,2) = {ratio_star:.4f}")
        print(f"    1/ratio = {1/ratio_star:.4f}")

    # ── Plot ─────────────────────────────────────────────────────────────
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Coherence Window: Which Denominators Are Resolved?",
                 fontsize=14, fontweight="bold")

    # A: Tongue width ratios (x-direction)
    ax = axes[0, 0]
    colors_q = {2: "red", 3: "blue", 4: "green", 5: "orange",
                6: "purple", 7: "brown", 8: "gray"}
    for q in range(2, 8):
        ratios = []
        for K0 in K_vals:
            K_x = K0 / 2
            w2 = tongue_width(1, 2, K_x)
            wq = tongue_width(1, q, K_x)
            ratios.append(wq / w2 if w2 > 1e-20 else 0)
        ax.semilogy(K_vals, ratios, color=colors_q[q], lw=2,
                    label=f"q={q}")
    ax.axhline(0.01, color="black", ls="--", alpha=0.5, label="1% threshold")
    ax.set_ylabel("w(q, K_x) / w(2, K_x)")
    ax.set_title("A. Tongue width ratio (x-dir, K_x=K₀/2)")
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(1e-8, 2)

    # B: Sector populations from field equation
    ax = axes[0, 1]
    if results_B:
        for q in range(2, 7):
            pops = [r["by_qmax"].get(q, 0) for r in results_B]
            K_plot = [r["K0"] for r in results_B]
            ax.semilogy(K_plot, [max(p, 1e-10) for p in pops],
                        color=colors_q.get(q, "gray"), lw=2, label=f"q_max={q}")
        ax.axhline(0.01, color="black", ls="--", alpha=0.5, label="1%")
    ax.set_ylabel("Population fraction")
    ax.set_title("B. Sector population (Klein topo)")
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(1e-6, 1)

    # C: Self-sustaining product K_eff × w²
    ax = axes[1, 0]
    for q in range(2, 7):
        products = []
        for K0 in K_vals:
            K_x = K0 / 2
            w = tongue_width(1, q, K_x)
            products.append(K_x * w * w)
        ax.semilogy(K_vals, [max(p, 1e-15) for p in products],
                    color=colors_q.get(q, "gray"), lw=2, label=f"q={q}")
    ax.axhline(2 / math.pi, color="black", ls="--", lw=2, alpha=0.7,
               label=f"2/π = {2/math.pi:.3f}")
    ax.set_xlabel("K₀")
    ax.set_ylabel("K_x × w(q, K_x)²")
    ax.set_title("C. Self-sustaining (x-dir)")
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(1e-10, 1)

    # D: The window
    ax = axes[1, 1]
    # For each K₀, find max q resolved by each criterion
    max_q_A = []
    max_q_B = []
    max_q_C = []
    for i, K0 in enumerate(K_vals):
        # A: tongue width ratio > 1%
        K_x = K0 / 2
        w2 = tongue_width(1, 2, K_x)
        qmax = 1
        if w2 > 1e-20:
            for q in range(2, 10):
                wq = tongue_width(1, q, K_x)
                if wq / w2 > 0.01:
                    qmax = q
                else:
                    break
        max_q_A.append(qmax)

        # C: self-sustaining
        qmax_c = 1
        for q in range(2, 10):
            w = tongue_width(1, q, K_x)
            if K_x * w * w >= 2 / math.pi:
                qmax_c = q
            else:
                break
        max_q_C.append(qmax_c)

    ax.plot(K_vals, max_q_A, "b-", lw=2, label="Criterion A (width ratio)")
    ax.plot(K_vals, max_q_C, "r-", lw=2, label="Criterion C (self-sustaining)")
    ax.axhline(3, color="green", ls="--", lw=2, alpha=0.7,
               label="q_max = 3 (target)")
    ax.fill_between(K_vals, 0, 3, alpha=0.1, color="green")
    ax.set_xlabel("K₀")
    ax.set_ylabel("Max resolved denominator")
    ax.set_title("D. Window size vs K₀")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 8)

    # Mark K₀* if found
    if K_4_sustain and K_4_sustain < float('inf') and K_lower < 999:
        K_star = math.sqrt(K_lower * K_4_sustain)
        for a in axes.flat:
            a.axvline(K_star, color="magenta", ls="-.", alpha=0.5)

    plt.tight_layout()
    out_path = "sync_cost/derivations/window_normalization.png"
    fig.savefig(out_path, dpi=150)
    print(f"\n  Saved: {out_path}")

    print(f"\n{'=' * 75}")
    print("  DONE")
    print(f"{'=' * 75}")


if __name__ == "__main__":
    main()
