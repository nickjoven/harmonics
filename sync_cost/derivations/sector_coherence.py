#!/usr/bin/env python3
"""
The population-to-coupling dictionary: coherence, not headcount.

A gauge coupling measures the strength of the interaction, which
corresponds to the COHERENCE of the sector (how well the oscillators
are phase-aligned), not the raw population (how many oscillators).

The sector order parameter:
    r_sector = |Σ N_i × e^{2πi(f₁+f₂)} × BC_weight| / Σ N_i

This can differ dramatically from the population fraction because:
  - Modes within a sector may interfere constructively or destructively
  - The BC weight (winding compatibility) affects phase alignment
  - The twist sign (-1)^q₁ modulates the contribution

Three candidate dictionaries:
  A. α_q⁻¹ ∝ N(sector)          — headcount (failed: 686% error)
  B. α_q⁻¹ ∝ |r_sector|         — coherence
  C. α_q⁻¹ ∝ N × |r_sector|     — weighted coherence (population × alignment)

Usage:
    python3 sync_cost/derivations/sector_coherence.py
"""

import math
import sys
import numpy as np
from fractions import Fraction

sys.path.insert(0, "sync_cost/derivations")
from circle_map_utils import INV_PHI


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


def winding_compatibility(p, q):
    if q % 2 == 0:
        return 1.0
    best = float('inf')
    for n in range(-q, q + 1):
        dist = abs(float(p) / q - (2 * n + 1) / 2)
        if dist < best:
            best = dist
    return math.exp(-math.pi * q * best)


def compute_sector(tree, q1_target, q2_target, K_eff, g_func):
    """Compute population, coherence, and weighted coherence for a sector."""
    modes = [(f1, f2) for f1 in tree for f2 in tree
             if f1.denominator == q1_target and f2.denominator == q2_target
             and (f1.denominator % 2) != (f2.denominator % 2)]

    if not modes:
        return {"pop": 0, "r": 0, "Nr": 0, "n_modes": 0, "modes": []}

    populations = []
    phases = []
    mode_data = []

    for f1, f2 in modes:
        g = g_func(float(f1), float(f2))
        w1 = tongue_width(f1.numerator, f1.denominator, K_eff)
        w2 = tongue_width(f2.numerator, f2.denominator, K_eff)
        bc = winding_compatibility(f1.numerator, f1.denominator)
        twist = (-1) ** f1.denominator

        pop = g * w1 * w2 * bc
        phase = 2 * math.pi * (float(f1) + float(f2))

        populations.append(pop)
        phases.append(phase)
        mode_data.append({
            "f1": f1, "f2": f2, "g": g, "w1": w1, "w2": w2,
            "bc": bc, "twist": twist, "pop": pop, "phase": phase,
        })

    total_pop = sum(populations)

    # Sector order parameter (no twist)
    r_plain = 0j
    for pop, phase in zip(populations, phases):
        r_plain += pop * (math.cos(phase) + 1j * math.sin(phase))
    r_plain_abs = abs(r_plain) / total_pop if total_pop > 0 else 0

    # Sector order parameter (with twist)
    r_twist = 0j
    for md in mode_data:
        r_twist += md["pop"] * md["twist"] * (
            math.cos(md["phase"]) + 1j * math.sin(md["phase"]))
    r_twist_abs = abs(r_twist) / total_pop if total_pop > 0 else 0

    # Phase variance (how spread the phases are within the sector)
    if total_pop > 0:
        mean_phase = np.angle(r_plain)
        phase_var = sum(
            pop * (((phase - mean_phase + math.pi) % (2 * math.pi) - math.pi) ** 2)
            for pop, phase in zip(populations, phases)) / total_pop
    else:
        phase_var = 0

    return {
        "pop": total_pop,
        "r_plain": r_plain_abs,
        "r_twist": r_twist_abs,
        "Nr_plain": total_pop * r_plain_abs,
        "Nr_twist": total_pop * r_twist_abs,
        "phase_var": phase_var,
        "n_modes": len(modes),
        "modes": mode_data,
    }


def main():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    DEPTH = 7  # deeper tree for better statistics
    tree = stern_brocot_tree(DEPTH)
    g_golden = lambda f1, f2: math.exp(
        -5 * ((f1 - INV_PHI) ** 2 + (f2 - INV_PHI) ** 2))

    print("=" * 75)
    print("  SECTOR COHERENCE: THE POPULATION-TO-COUPLING DICTIONARY")
    print(f"  Tree depth {DEPTH}: {len(tree)} nodes")
    print("=" * 75)

    sectors = [(2, 3), (3, 2), (2, 5), (5, 2), (3, 4), (4, 3)]

    # ── Step 1: Detailed sector structure at K₀ = 1 ─────────────────────
    print(f"\n{'─' * 75}")
    print("  Step 1: Sector structure at K₀ = 1 (K_eff = 0.5)")
    print(f"{'─' * 75}")

    K_eff = 0.5

    for s in [(2, 3), (3, 2)]:
        result = compute_sector(tree, s[0], s[1], K_eff, g_golden)
        print(f"\n  Sector ({s[0]},{s[1]}): {result['n_modes']} modes")
        print(f"    Total population: {result['pop']:.6f}")
        print(f"    |r| (plain):     {result['r_plain']:.6f}")
        print(f"    |r| (twist):     {result['r_twist']:.6f}")
        print(f"    N×|r| (plain):   {result['Nr_plain']:.6f}")
        print(f"    N×|r| (twist):   {result['Nr_twist']:.6f}")
        print(f"    Phase variance:  {result['phase_var']:.6f}")

        # Show top modes
        sorted_modes = sorted(result["modes"], key=lambda m: -m["pop"])
        print(f"\n    Top modes:")
        print(f"    {'(f₁,f₂)':>15s}  {'pop':>10s}  {'phase/2π':>10s}  "
              f"{'bc':>8s}  {'twist':>6s}")
        for md in sorted_modes[:8]:
            ph = md["phase"] / (2 * math.pi)
            print(f"    ({str(md['f1']):>5s},{str(md['f2']):>5s})  "
                  f"{md['pop']:10.6f}  {ph:10.4f}  {md['bc']:8.4f}  "
                  f"{md['twist']:6d}")

    # ── Step 2: K sweep — all three dictionaries ─────────────────────────
    print(f"\n{'─' * 75}")
    print("  Step 2: Dictionary comparison vs K₀")
    print(f"{'─' * 75}")

    K_vals = np.concatenate([
        np.linspace(0.1, 1.0, 20),
        np.linspace(1.0, 3.0, 20),
        np.linspace(3.0, 10.0, 10),
    ])

    data = {s: {"pop": [], "r_plain": [], "r_twist": [],
                "Nr_plain": [], "Nr_twist": []}
            for s in sectors}

    for K0 in K_vals:
        K_eff = K0 / 2
        for s in sectors:
            result = compute_sector(tree, s[0], s[1], K_eff, g_golden)
            data[s]["pop"].append(result["pop"])
            data[s]["r_plain"].append(result["r_plain"])
            data[s]["r_twist"].append(result["r_twist"])
            data[s]["Nr_plain"].append(result["Nr_plain"])
            data[s]["Nr_twist"].append(result["Nr_twist"])

    # Compute ratios
    print(f"\n  {'K₀':>6s}  {'N(2,3)/N(3,2)':>14s}  {'r(2,3)/r(3,2)':>14s}  "
          f"{'Nr(2,3)/Nr(3,2)':>16s}  {'r_tw ratio':>12s}")
    print("  " + "-" * 68)

    ratios_pop = []
    ratios_r = []
    ratios_Nr = []
    ratios_r_tw = []

    for i, K0 in enumerate(K_vals):
        n23 = data[(2, 3)]["pop"][i]
        n32 = data[(3, 2)]["pop"][i]
        r23 = data[(2, 3)]["r_plain"][i]
        r32 = data[(3, 2)]["r_plain"][i]
        nr23 = data[(2, 3)]["Nr_plain"][i]
        nr32 = data[(3, 2)]["Nr_plain"][i]
        rt23 = data[(2, 3)]["r_twist"][i]
        rt32 = data[(3, 2)]["r_twist"][i]

        rp = n23 / n32 if n32 > 1e-15 else float('nan')
        rr = r23 / r32 if r32 > 1e-15 else float('nan')
        rnr = nr23 / nr32 if nr32 > 1e-15 else float('nan')
        rrt = rt23 / rt32 if rt32 > 1e-15 else float('nan')

        ratios_pop.append(rp)
        ratios_r.append(rr)
        ratios_Nr.append(rnr)
        ratios_r_tw.append(rrt)

        if i % 5 == 0 or abs(K0 - 1.0) < 0.05:
            print(f"  {K0:6.3f}  {rp:14.6f}  {rr:14.6f}  "
                  f"{rnr:16.6f}  {rrt:12.6f}")

    # ── Step 3: Match against SM ─────────────────────────────────────────
    print(f"\n{'─' * 75}")
    print("  Step 3: Which dictionary matches the SM?")
    print(f"{'─' * 75}")

    alpha_2_inv = 29.57
    alpha_3_inv = 8.50
    sm_ratio = alpha_3_inv / alpha_2_inv  # α₃/α₂ = α₃⁻¹... no
    # α₂⁻¹/α₃⁻¹ = 29.57/8.50 = 3.479 = α₃/α₂
    # So α₂/α₃ = 8.50/29.57 = 0.2875
    ratio_at_MZ = alpha_2_inv / alpha_3_inv  # = 3.479

    print(f"\n  SM at M_Z: α₂⁻¹/α₃⁻¹ = {ratio_at_MZ:.4f}")
    print(f"  (equivalently α₃/α₂ = {ratio_at_MZ:.4f})")

    # One-loop running: at what scale does each dictionary match?
    B_2 = -19.0 / 6
    B_3 = -7.0
    M_Z = 91.2
    M_Pl = 1.221e19

    # If at Planck: α₂⁻¹/α₃⁻¹ = R (the dictionary ratio)
    # Then at M_Z: (α₂⁻¹(Pl) + Δα₂⁻¹) / (α₃⁻¹(Pl) + Δα₃⁻¹)
    # This is NOT simply R + correction because it's a ratio.

    # Instead: α₂⁻¹(Pl) = R × α₃⁻¹(Pl)
    # At M_Z: α₂⁻¹(Z) = R × C + Δ₂, α₃⁻¹(Z) = C + Δ₃
    # where C = α₃⁻¹(Pl), Δᵢ = -(bᵢ/2π) ln(M_Z/M_Pl)

    ln_ratio = math.log(M_Z / M_Pl)
    delta_2 = -(B_2 / (2 * math.pi)) * ln_ratio
    delta_3 = -(B_3 / (2 * math.pi)) * ln_ratio

    print(f"\n  Running: Δα₂⁻¹ = {delta_2:.4f}, Δα₃⁻¹ = {delta_3:.4f}")

    # For each candidate ratio R at Planck:
    # α₃⁻¹(Z) = C + Δ₃ = 8.50 → C = 8.50 - Δ₃
    C = 8.50 - delta_3
    print(f"  C = α₃⁻¹(M_Pl) = {C:.4f}")

    for label, R in [("headcount exp(π/2)", math.exp(math.pi / 2)),
                      ("coherence (@ K₀=1)", ratios_r[19] if len(ratios_r) > 19 else 0),
                      ("N×r (@ K₀=1)", ratios_Nr[19] if len(ratios_Nr) > 19 else 0),
                      ("r_twist (@ K₀=1)", ratios_r_tw[19] if len(ratios_r_tw) > 19 else 0)]:
        alpha2_Pl = R * C
        alpha2_Z = alpha2_Pl + delta_2
        pred_ratio_Z = alpha2_Z / 8.50
        err = abs(pred_ratio_Z - ratio_at_MZ) / ratio_at_MZ * 100
        print(f"\n  Dictionary: {label}")
        print(f"    R = {R:.6f}")
        print(f"    α₂⁻¹(Pl) = {R:.4f} × {C:.4f} = {alpha2_Pl:.4f}")
        print(f"    α₂⁻¹(Z) = {alpha2_Pl:.4f} + {delta_2:.4f} = {alpha2_Z:.4f}")
        print(f"    Predicted α₂⁻¹/α₃⁻¹ at M_Z = {pred_ratio_Z:.4f}")
        print(f"    Measured: {ratio_at_MZ:.4f}")
        print(f"    Error: {err:.1f}%")

    # ── Step 4: Reverse — what R at Planck gives SM at M_Z? ──────────────
    print(f"\n{'─' * 75}")
    print("  Step 4: Required ratio at Planck scale")
    print(f"{'─' * 75}")

    # 29.57 = R × C + delta_2
    # R = (29.57 - delta_2) / C
    R_required = (29.57 - delta_2) / C
    print(f"\n  Required R = α₂⁻¹(Pl)/α₃⁻¹(Pl) = {R_required:.6f}")
    print(f"  = (29.57 - ({delta_2:.4f})) / {C:.4f}")
    print(f"  = {29.57 - delta_2:.4f} / {C:.4f}")

    # Is this a recognizable number?
    print(f"\n  Is R = {R_required:.6f} recognizable?")
    candidates = [
        ("1", 1.0),
        ("9/4 = (q₃/q₂)²", 9/4),
        ("exp(π/2)", math.exp(math.pi / 2)),
        ("exp(1)", math.e),
        ("φ = (1+√5)/2", (1 + math.sqrt(5)) / 2),
        ("φ²", ((1 + math.sqrt(5)) / 2) ** 2),
        ("π", math.pi),
        ("π/2", math.pi / 2),
        ("2", 2.0),
        ("3", 3.0),
        ("ln(φ²) = 2ln(φ)", 2 * math.log((1 + math.sqrt(5)) / 2)),
        ("√(exp(π/2))", math.sqrt(math.exp(math.pi / 2))),
        ("exp(π/4)", math.exp(math.pi / 4)),
        ("4/3", 4/3),
        ("3/2", 3/2),
    ]
    for name, val in sorted(candidates, key=lambda x: abs(x[1] - R_required)):
        diff = abs(val - R_required) / R_required * 100
        mark = " ←" if diff < 5 else ""
        print(f"    {name:>25s} = {val:.6f}  ({diff:5.1f}%){mark}")

    # ── Plot ─────────────────────────────────────────────────────────────
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Sector Coherence: Population vs Alignment",
                 fontsize=14, fontweight="bold")

    K = K_vals

    # A: Population ratio
    ax = axes[0, 0]
    ax.plot(K, ratios_pop, "r-", lw=2, label="N(2,3)/N(3,2)")
    ax.axhline(math.exp(math.pi / 2), color="magenta", ls="-.",
               label=f"exp(π/2) = {math.exp(math.pi/2):.3f}")
    ax.axhline(R_required, color="green", ls="--", lw=2,
               label=f"Required = {R_required:.3f}")
    ax.set_ylabel("Ratio")
    ax.set_title("A. Population ratio (headcount)")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # B: Coherence ratio
    ax = axes[0, 1]
    ax.plot(K, ratios_r, "b-", lw=2, label="|r|(2,3)/|r|(3,2)")
    ax.plot(K, ratios_r_tw, "r--", lw=1.5, label="|r_twist| ratio")
    ax.axhline(R_required, color="green", ls="--", lw=2,
               label=f"Required = {R_required:.3f}")
    ax.set_ylabel("Ratio")
    ax.set_title("B. Coherence ratio")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # C: Weighted coherence ratio
    ax = axes[1, 0]
    ax.plot(K, ratios_Nr, "purple", lw=2, label="N×|r|(2,3) / N×|r|(3,2)")
    ax.axhline(R_required, color="green", ls="--", lw=2,
               label=f"Required = {R_required:.3f}")
    ax.axhline(math.exp(math.pi / 2), color="magenta", ls="-.",
               label=f"exp(π/2)")
    ax.set_xlabel("K₀")
    ax.set_ylabel("Ratio")
    ax.set_title("C. Weighted coherence (N×|r|)")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # D: Raw coherence values
    ax = axes[1, 1]
    ax.plot(K, data[(2, 3)]["r_plain"], "r-", lw=2, label="|r|(2,3)")
    ax.plot(K, data[(3, 2)]["r_plain"], "b-", lw=2, label="|r|(3,2)")
    ax.plot(K, data[(2, 5)]["r_plain"], "r--", lw=1, label="|r|(2,5)")
    ax.plot(K, data[(5, 2)]["r_plain"], "b--", lw=1, label="|r|(5,2)")
    ax.set_xlabel("K₀")
    ax.set_ylabel("|r_sector|")
    ax.set_title("D. Sector coherence")
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    out = "sync_cost/derivations/sector_coherence.png"
    fig.savefig(out, dpi=150)
    print(f"\n  Saved: {out}")

    print(f"\n{'=' * 75}")
    print("  DONE")
    print(f"{'=' * 75}")


if __name__ == "__main__":
    main()
