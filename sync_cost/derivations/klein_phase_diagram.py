#!/usr/bin/env python3
"""
Klein bottle phase diagram: mode occupation vs coupling K.

Sweeps K₀ from 0.05 to 3.0, solves the 2D field equation (D11 × D19)
for torus and Klein bottle (XOR + twist), tracks:
  - |r| order parameter
  - Population fraction in each (q₁,q₂) sector
  - Number of effectively occupied modes (participation ratio)
  - Top mode identity

Output: klein_phase_diagram.png (4-panel figure)

Usage:
    python sync_cost/derivations/klein_phase_diagram.py
"""

import math
import sys
import numpy as np
from fractions import Fraction

sys.path.insert(0, "sync_cost/derivations")
from circle_map_utils import PHI, INV_PHI

# ── Stern-Brocot tree ───────────────────────────────────────────────────────

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


# ── Tongue width ─────────────────────────────────────────────────────────────

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

def solve_2d(pairs, K0, g_func, twist=False, n_iter=400, damping=0.3,
             self_consistent=True):
    """Solve field equation, return (populations, r_final, r_history).

    If self_consistent=False, use K_eff = K0 directly (external drive).
    """
    N_total = len(pairs)
    if N_total == 0:
        return {}, 0.0, []

    populations = {(f1, f2): 1.0 for f1, f2 in pairs}
    r_history = []

    for _ in range(n_iter):
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

        if self_consistent:
            K_eff = K0 * max(r_abs, 1e-15)
        else:
            K_eff = K0

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

        for f1, f2 in pairs:
            populations[(f1, f2)] = ((1 - damping) * populations[(f1, f2)]
                                     + damping * new_pop[(f1, f2)])

    # Final |r|
    total_pop = sum(populations.values())
    r_final = 0j
    for (f1, f2), pop in populations.items():
        phase = 2 * math.pi * (float(f1) + float(f2))
        sign = ((-1) ** f1.denominator) if twist else 1
        r_final += pop * sign * (math.cos(phase) + 1j * math.sin(phase))
    if total_pop > 0:
        r_final /= total_pop

    return populations, abs(r_final), r_history


def sector_order_parameter(populations, q1_t, q2_t):
    """Order parameter restricted to a single (q1,q2) sector."""
    r = 0j
    total = 0.0
    for (f1, f2), pop in populations.items():
        if f1.denominator == q1_t and f2.denominator == q2_t:
            phase = 2 * math.pi * (float(f1) + float(f2))
            r += pop * (math.cos(phase) + 1j * math.sin(phase))
            total += pop
    if total == 0:
        return 0.0
    return abs(r / total)


# ── Sector analysis ──────────────────────────────────────────────────────────

def sector_fractions(populations, sectors):
    """Return fraction of total population in each (q1,q2) sector."""
    total = sum(populations.values())
    if total == 0:
        return {s: 0.0 for s in sectors}
    result = {}
    for (q1_t, q2_t) in sectors:
        pop = sum(p for (f1, f2), p in populations.items()
                  if f1.denominator == q1_t and f2.denominator == q2_t)
        result[(q1_t, q2_t)] = pop / total
    return result


def participation_ratio(populations):
    """Effective number of occupied modes: (Σ p)² / Σ p²."""
    vals = list(populations.values())
    s1 = sum(vals)
    s2 = sum(v * v for v in vals)
    if s2 == 0:
        return 0.0
    return s1 * s1 / s2


def top_mode_label(populations):
    """Return string label of the most populated mode."""
    if not populations:
        return "none"
    (f1, f2), _ = max(populations.items(), key=lambda x: x[1])
    return f"{f1.numerator}/{f1.denominator},{f2.numerator}/{f2.denominator}"


# ── Main sweep ───────────────────────────────────────────────────────────────

def main():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    DEPTH = 6
    tree = stern_brocot_tree(DEPTH)
    print(f"Tree depth {DEPTH}: {len(tree)} nodes, "
          f"max q = {max(f.denominator for f in tree)}")

    # Build pair lists
    pairs_torus = [(f1, f2) for f1 in tree for f2 in tree]
    pairs_klein = [(f1, f2) for f1 in tree for f2 in tree
                   if (f1.denominator % 2) != (f2.denominator % 2)]
    print(f"Torus pairs: {len(pairs_torus)}, Klein pairs: {len(pairs_klein)}")

    g_golden = lambda f1, f2: math.exp(
        -5 * ((f1 - INV_PHI) ** 2 + (f2 - INV_PHI) ** 2))

    # Sectors to track
    sectors = [(2, 3), (3, 2), (2, 5), (5, 2), (3, 4), (4, 3),
               (2, 1), (1, 2), (3, 5), (5, 3), (1, 1)]

    # K sweep
    K_vals = np.concatenate([
        np.linspace(0.05, 0.5, 20),
        np.linspace(0.5, 1.5, 40),
        np.linspace(1.5, 3.0, 20),
    ])

    # Three variants:
    #   torus:      self-consistent K_eff = K₀|r|, no XOR, no twist
    #   klein_sc:   self-consistent K_eff = K₀|r|, XOR + twist (|r|→0)
    #   klein_ext:  external drive K_eff = K₀, XOR + twist (real dynamics)
    variants = ["torus", "klein_sc", "klein_ext"]
    data = {v: {
        "r": [], "pr": [], "top": [],
        "sectors": {s: [] for s in sectors},
        "sector_r": {s: [] for s in sectors},
    } for v in variants}

    print(f"Sweeping K over {len(K_vals)} values...")

    for idx, K0 in enumerate(K_vals):
        if idx % 10 == 0:
            print(f"  K = {K0:.3f} ({idx+1}/{len(K_vals)})")

        # Torus (self-consistent)
        pop_t, r_t, _ = solve_2d(pairs_torus, K0, g_golden,
                                   twist=False, n_iter=300, damping=0.3,
                                   self_consistent=True)
        sf_t = sector_fractions(pop_t, sectors)
        data["torus"]["r"].append(r_t)
        data["torus"]["pr"].append(participation_ratio(pop_t))
        data["torus"]["top"].append(top_mode_label(pop_t))
        for s in sectors:
            data["torus"]["sectors"][s].append(sf_t[s])
            data["torus"]["sector_r"][s].append(
                sector_order_parameter(pop_t, s[0], s[1]))

        # Klein self-consistent (shows cancellation)
        pop_ks, r_ks, _ = solve_2d(pairs_klein, K0, g_golden,
                                     twist=True, n_iter=300, damping=0.3,
                                     self_consistent=True)
        sf_ks = sector_fractions(pop_ks, sectors)
        data["klein_sc"]["r"].append(r_ks)
        data["klein_sc"]["pr"].append(participation_ratio(pop_ks))
        data["klein_sc"]["top"].append(top_mode_label(pop_ks))
        for s in sectors:
            data["klein_sc"]["sectors"][s].append(sf_ks[s])
            data["klein_sc"]["sector_r"][s].append(
                sector_order_parameter(pop_ks, s[0], s[1]))

        # Klein external drive (real dynamics)
        pop_ke, r_ke, _ = solve_2d(pairs_klein, K0, g_golden,
                                     twist=True, n_iter=300, damping=0.3,
                                     self_consistent=False)
        sf_ke = sector_fractions(pop_ke, sectors)
        data["klein_ext"]["r"].append(r_ke)
        data["klein_ext"]["pr"].append(participation_ratio(pop_ke))
        data["klein_ext"]["top"].append(top_mode_label(pop_ke))
        for s in sectors:
            data["klein_ext"]["sectors"][s].append(sf_ke[s])
            data["klein_ext"]["sector_r"][s].append(
                sector_order_parameter(pop_ke, s[0], s[1]))

    # ── Plot ─────────────────────────────────────────────────────────────────

    fig, axes = plt.subplots(3, 2, figsize=(14, 14))
    fig.suptitle("Klein Bottle Phase Diagram: Mode Occupation vs K",
                 fontsize=14, fontweight="bold", y=0.98)

    K = K_vals

    colors_sec = {
        (2, 3): "#e41a1c", (3, 2): "#377eb8",
        (2, 5): "#ff7f00", (5, 2): "#984ea3",
        (3, 4): "#4daf4a", (4, 3): "#a65628",
        (1, 2): "#999999", (2, 1): "#666666",
    }
    sec_show = [(2, 3), (3, 2), (2, 5), (5, 2), (3, 4), (4, 3), (1, 2), (2, 1)]

    # Panel A: Order parameter |r|
    ax = axes[0, 0]
    ax.plot(K, data["torus"]["r"], "b-", lw=2, label="Torus (SC)")
    ax.plot(K, data["klein_sc"]["r"], "r--", lw=1.5, label="Klein SC (≡0)")
    ax.plot(K, data["klein_ext"]["r"], "r-", lw=2, label="Klein ext")
    ax.set_ylabel("|r|  (order parameter)")
    ax.set_title("A. Global order parameter")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.axvline(1.0, color="gray", ls="--", alpha=0.5)

    # Panel B: Participation ratio
    ax = axes[0, 1]
    ax.semilogy(K, data["torus"]["pr"], "b-", lw=2, label="Torus")
    ax.semilogy(K, data["klein_sc"]["pr"], "r--", lw=1.5, label="Klein SC")
    ax.semilogy(K, data["klein_ext"]["pr"], "r-", lw=2, label="Klein ext")
    ax.set_ylabel("Participation ratio")
    ax.set_title("B. Effective mode count")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.axvline(1.0, color="gray", ls="--", alpha=0.5)

    # Panel C: Klein ext sector populations (the main result)
    ax = axes[1, 0]
    for s in sec_show:
        vals = data["klein_ext"]["sectors"][s]
        if max(vals) > 0.005:
            ax.plot(K, vals, color=colors_sec.get(s, "gray"), lw=1.5,
                    label=f"q=({s[0]},{s[1]})")
    ax.set_ylabel("Population fraction")
    ax.set_title("C. Klein ext: sector populations")
    ax.legend(fontsize=7, ncol=2)
    ax.grid(True, alpha=0.3)
    ax.axvline(1.0, color="gray", ls="--", alpha=0.5)

    # Panel D: Torus sector populations
    ax = axes[1, 1]
    for s in sec_show:
        vals = data["torus"]["sectors"][s]
        if max(vals) > 0.005:
            ax.plot(K, vals, color=colors_sec.get(s, "gray"), lw=1.5,
                    label=f"q=({s[0]},{s[1]})")
    ax.set_ylabel("Population fraction")
    ax.set_title("D. Torus: sector populations")
    ax.legend(fontsize=7, ncol=2)
    ax.grid(True, alpha=0.3)
    ax.axvline(1.0, color="gray", ls="--", alpha=0.5)

    # Panel E: Klein ext sector order parameters
    ax = axes[2, 0]
    for s in [(2, 3), (3, 2), (2, 5), (5, 2)]:
        vals = data["klein_ext"]["sector_r"][s]
        if max(vals) > 0.001:
            ax.plot(K, vals, color=colors_sec.get(s, "gray"), lw=1.5,
                    label=f"|r|_({s[0]},{s[1]})")
    ax.set_xlabel("K₀")
    ax.set_ylabel("Sector |r|")
    ax.set_title("E. Klein ext: sector order parameters")
    ax.legend(fontsize=7, ncol=2)
    ax.grid(True, alpha=0.3)
    ax.axvline(1.0, color="gray", ls="--", alpha=0.5)

    # Panel F: (2,3) vs (3,2) asymmetry ratio on Klein ext
    ax = axes[2, 1]
    ratio_23_32 = []
    ratio_25_52 = []
    for i in range(len(K)):
        p23 = data["klein_ext"]["sectors"][(2, 3)][i]
        p32 = data["klein_ext"]["sectors"][(3, 2)][i]
        ratio_23_32.append(p23 / p32 if p32 > 1e-10 else 1.0)
        p25 = data["klein_ext"]["sectors"][(2, 5)][i]
        p52 = data["klein_ext"]["sectors"][(5, 2)][i]
        ratio_25_52.append(p25 / p52 if p52 > 1e-10 else 1.0)
    ax.plot(K, ratio_23_32, "r-", lw=2, label="N(2,3)/N(3,2)")
    ax.plot(K, ratio_25_52, color="#ff7f00", lw=2, label="N(2,5)/N(5,2)")
    ax.axhline(1.0, color="gray", ls=":", alpha=0.5)
    ax.set_xlabel("K₀")
    ax.set_ylabel("Population ratio")
    ax.set_title("F. Klein ext: sector asymmetry")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.axvline(1.0, color="gray", ls="--", alpha=0.5)

    plt.tight_layout()
    out_path = "sync_cost/derivations/klein_phase_diagram.png"
    fig.savefig(out_path, dpi=150)
    print(f"\nSaved: {out_path}")

    # ── Text summary ─────────────────────────────────────────────────────────

    print(f"\n{'=' * 70}")
    print(f"  PHASE DIAGRAM SUMMARY")
    print(f"{'=' * 70}")

    # Find transitions
    for label, vkey in [("Torus", "torus"), ("Klein SC", "klein_sc"),
                         ("Klein ext", "klein_ext")]:
        r_arr = np.array(data[vkey]["r"])
        pr_arr = np.array(data[vkey]["pr"])

        idx_r = np.argmax(r_arr > 0.1)
        if r_arr[idx_r] > 0.1:
            print(f"  {label}: |r| > 0.1 at K ≈ {K[idx_r]:.3f}")
        else:
            print(f"  {label}: |r| never exceeds 0.1 (max = {r_arr.max():.6f})")

        pr_max = pr_arr.max()
        idx_pr = np.argmax(pr_arr < 0.5 * pr_max)
        if pr_arr[idx_pr] < 0.5 * pr_max and idx_pr > 0:
            print(f"  {label}: modes collapse (PR < 50% of {pr_max:.1f}) "
                  f"at K ≈ {K[idx_pr]:.3f}")

    # Snapshots at key K values
    for K_snap in [0.5, 1.0, 2.0, 3.0]:
        k_idx = np.argmin(np.abs(K - K_snap))
        print(f"\n  At K = {K[k_idx]:.3f}:")
        for label, vkey in [("Torus", "torus"), ("Klein ext", "klein_ext")]:
            svals = {s: data[vkey]["sectors"][s][k_idx] for s in sectors}
            top_s = max(svals, key=svals.get)
            print(f"    {label}: top q=({top_s[0]},{top_s[1]}) "
                  f"= {svals[top_s]:.4f}, |r| = {data[vkey]['r'][k_idx]:.4f}, "
                  f"PR = {data[vkey]['pr'][k_idx]:.1f}, "
                  f"top = {data[vkey]['top'][k_idx]}")

        # (2,3)/(3,2) asymmetry on Klein ext
        k23 = data["klein_ext"]["sectors"][(2, 3)][k_idx]
        k32 = data["klein_ext"]["sectors"][(3, 2)][k_idx]
        if k32 > 1e-10 and k23 > 1e-10:
            print(f"    Klein ext (2,3)/(3,2) = {k23/k32:.4f}")

    print(f"\n{'=' * 70}")
    print(f"  DONE")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()
