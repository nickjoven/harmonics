#!/usr/bin/env python3
"""
Pin K₀* by applying the half-twist to the self-sustaining criterion.

On a periodic domain, a mode must sustain coherence over the full
circumference: K_eff × w² ≥ 2/π.

On the Klein bottle, the antiperiodic identification carries the
mode across half the domain. The mode only needs to sustain itself
over HALF the circumference — the topology provides the other half.

Corrected threshold: K_eff × w² ≥ 1/π  (half of 2/π)

With K_eff = K₀/2 (half-twist on coupling):
    (K₀/2) × w(q, K₀/2)² ≥ 1/π

Find K₀* where q=3 just meets this threshold and q=4 does not.

Usage:
    python3 sync_cost/derivations/window_pinning.py
"""

import math
import sys
import numpy as np

sys.path.insert(0, "sync_cost/derivations")


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


def self_sustaining_product(q, K0):
    """K_eff × w(q, K_eff)² where K_eff = K₀/2."""
    K_eff = K0 / 2
    w = tongue_width(1, q, K_eff)
    return K_eff * w * w


def find_threshold_crossing(q, threshold, K_range):
    """Find K₀ where self-sustaining product first exceeds threshold."""
    for K0 in K_range:
        if self_sustaining_product(q, K0) >= threshold:
            return K0
    return None


def main():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    print("=" * 75)
    print("  WINDOW PINNING: HALF-TWIST ON THE THRESHOLD")
    print("=" * 75)

    # The two thresholds
    th_torus = 2 / math.pi      # full domain
    th_klein = 1 / math.pi      # half domain (Klein bottle)

    print(f"\n  Torus threshold: 2/π = {th_torus:.6f}")
    print(f"  Klein threshold: 1/π = {th_klein:.6f}")

    K_fine = np.linspace(0.01, 200.0, 50000)
    max_q = 8

    # ── Find crossings at both thresholds ────────────────────────────────
    print(f"\n{'─' * 75}")
    print("  Self-sustaining onset: (K₀/2) × w(q, K₀/2)² ≥ threshold")
    print(f"{'─' * 75}")

    print(f"\n  {'q':>4s}  {'K₀ (torus 2/π)':>16s}  {'K₀ (Klein 1/π)':>16s}  "
          f"{'K_eff (Klein)':>14s}")
    print("  " + "-" * 55)

    onset_torus = {}
    onset_klein = {}

    for q in range(2, max_q + 1):
        kt = find_threshold_crossing(q, th_torus, K_fine)
        kk = find_threshold_crossing(q, th_klein, K_fine)
        onset_torus[q] = kt
        onset_klein[q] = kk

        kt_str = f"{kt:.4f}" if kt else "never"
        kk_str = f"{kk:.4f}" if kk else "never"
        keff_str = f"{kk/2:.4f}" if kk else "—"
        print(f"  {q:4d}  {kt_str:>16s}  {kk_str:>16s}  {keff_str:>14s}")

    # ── The window ───────────────────────────────────────────────────────
    print(f"\n{'─' * 75}")
    print("  THE WINDOW: q=3 sustained, q=4 not")
    print(f"{'─' * 75}")

    K_q3 = onset_klein.get(3)
    K_q4 = onset_klein.get(4)

    if K_q3 and K_q4:
        print(f"\n  q=3 sustained at K₀ ≥ {K_q3:.4f}  (K_eff = {K_q3/2:.4f})")
        print(f"  q=4 sustained at K₀ ≥ {K_q4:.4f}  (K_eff = {K_q4/2:.4f})")
        print(f"\n  Window: K₀ ∈ [{K_q3:.4f}, {K_q4:.4f})")
        print(f"  Width: ΔK₀ = {K_q4 - K_q3:.4f}")

        K_star = math.sqrt(K_q3 * K_q4)
        print(f"\n  K₀* (geometric mean) = {K_star:.6f}")
        print(f"  K_eff* = K₀*/2 = {K_star/2:.6f}")

        # What are the tongue widths at K₀*?
        K_eff_star = K_star / 2
        print(f"\n  Tongue widths at K₀* = {K_star:.4f}, K_eff = {K_eff_star:.4f}:")
        for q in range(1, max_q + 1):
            w = tongue_width(1, q, K_eff_star)
            prod = K_eff_star * w * w
            status = "✓" if prod >= th_klein else "✗"
            print(f"    q={q}: w = {w:.6f}, (K/2)w² = {prod:.6f} "
                  f"{'≥' if prod >= th_klein else '<'} 1/π  {status}")

        # The sector ratio at K₀*
        print(f"\n  Sector ratio at K₀*:")
        print(f"    N(2,3)/N(3,2) = exp(π/2) = {math.exp(math.pi/2):.6f}")
        print(f"    (topological, independent of K₀*)")

    elif K_q3 and not K_q4:
        print(f"\n  q=3 sustained at K₀ ≥ {K_q3:.4f}")
        print(f"  q=4 never sustained in range [0, {K_fine[-1]:.1f}]")
        print(f"\n  Window: K₀ ≥ {K_q3:.4f} (open-ended)")
        K_star = K_q3
        K_eff_star = K_star / 2

    else:
        print(f"\n  Neither q=3 nor q=4 sustained. Check range.")
        return

    # ── Connection to physics ────────────────────────────────────────────
    print(f"\n{'─' * 75}")
    print("  CONNECTION TO PHYSICAL SCALES")
    print(f"{'─' * 75}")

    # The tongue width ratio at K₀*
    w2_star = tongue_width(1, 2, K_eff_star)
    w3_star = tongue_width(1, 3, K_eff_star)

    print(f"\n  At K₀* = {K_star:.4f}:")
    print(f"    w(2)/w(3) = {w2_star/w3_star:.6f}")
    print(f"    w(2)²/w(3)² = {(w2_star/w3_star)**2:.6f}")

    # The coupling constant ratio at the matching scale
    # If α_q⁻¹ ∝ w(q)⁻¹ (stronger coupling = narrower tongue at resonance)
    # Then α₂⁻¹/α₃⁻¹ = w(3)/w(2) = 1/(w(2)/w(3))
    # No — if α_q ∝ tongue width (wider tongue = stronger coupling):
    # α₂/α₃ = w(2)/w(3)
    # α₂⁻¹/α₃⁻¹ = w(3)/w(2)

    print(f"\n  Coupling constant predictions at K₀*:")
    print(f"    If α_q ∝ w(q):  α₂/α₃ = w(2)/w(3) = {w2_star/w3_star:.4f}")
    print(f"    If α_q⁻¹ ∝ w(q):  α₂⁻¹/α₃⁻¹ = w(2)/w(3) = {w2_star/w3_star:.4f}")
    print(f"    SM measured: α₂⁻¹/α₃⁻¹ = {29.57/8.50:.4f}")

    # The BC weight gives another ratio
    print(f"\n  BC weight (topological):")
    print(f"    N(2,3)/N(3,2) = exp(π/2) = {math.exp(math.pi/2):.4f}")
    print(f"    SM: α₃/α₂ = α₂⁻¹/α₃⁻¹ (different convention) = {29.57/8.50:.4f}")

    # Combined: the total ratio is tongue width × BC weight
    # N(2,3)/N(3,2) = [w(2)/w(3)]² × exp(π/2)  ... no, this is only for
    # the anisotropic case. In symmetric coupling, tongue widths cancel
    # and only BC weight survives.
    # But wait — within the (2,3) sector, the modes have both q=2 and q=3
    # tongue widths, same as (3,2). The BC weight is the ONLY asymmetry.

    print(f"\n  In symmetric coupling model:")
    print(f"    Tongue widths cancel (both sectors see same K_eff)")
    print(f"    N(2,3)/N(3,2) = exp(π/2) = {math.exp(math.pi/2):.4f} (exact)")
    print(f"\n    This doesn't match α₃/α₂ = {29.57/8.50:.4f} directly.")
    print(f"    But α₃/α₂ is measured at M_Z, not at the Planck/unification scale.")

    # At unification, the couplings are predicted to have ratio:
    # α₂/α₃ at unification = ???
    # The standard SM prediction is near-unification around 10^15 GeV
    # where α₂ ≈ α₃. So at unification, the ratio is ~1.
    # The Klein bottle says the TOPOLOGICAL ratio is exp(π/2) ≈ 4.81.
    # This must be the ratio at the Klein bottle's own scale (Planck),
    # not at M_Z. The running from Planck to M_Z changes it.

    # One-loop running: α_i⁻¹(μ) = α_i⁻¹(M_Pl) - (b_i/2π) ln(μ/M_Pl)
    B_2 = -19.0 / 6
    B_3 = -7.0
    M_Z = 91.2
    M_Pl = 1.221e19

    ln_ratio = math.log(M_Z / M_Pl)

    # At M_Pl: α₂⁻¹/α₃⁻¹ = exp(π/2) ?
    # No — the Klein bottle gives population ratio, not coupling ratio.
    # But if α_q⁻¹ ∝ N(sector with q in antiperiodic direction):
    # α₂⁻¹ ∝ N(2,*), α₃⁻¹ ∝ N(3,*)
    # Then α₂⁻¹/α₃⁻¹ at Planck = exp(π/2) = 4.81

    # Run to M_Z:
    # α₂⁻¹(M_Z) = α₂⁻¹(M_Pl) - (B_2/2π) × ln(M_Z/M_Pl)
    # α₃⁻¹(M_Z) = α₃⁻¹(M_Pl) - (B_3/2π) × ln(M_Z/M_Pl)

    # With α₂⁻¹(M_Pl) = C × exp(π/2) and α₃⁻¹(M_Pl) = C × 1
    # for some normalization C:

    # α₂⁻¹(M_Z) = C × exp(π/2) - (B_2/2π) × ln(M_Z/M_Pl)
    # α₃⁻¹(M_Z) = C × 1       - (B_3/2π) × ln(M_Z/M_Pl)

    # We know α₂⁻¹(M_Z) = 29.57 and α₃⁻¹(M_Z) = 8.50
    # Two equations, one unknown (C):

    delta_2 = -(B_2 / (2 * math.pi)) * ln_ratio
    delta_3 = -(B_3 / (2 * math.pi)) * ln_ratio

    # 29.57 = C × exp(π/2) + delta_2
    # 8.50  = C × 1         + delta_3

    # From equation 2: C = 8.50 - delta_3
    C_from_3 = 8.50 - delta_3
    # Check with equation 1: C × exp(π/2) + delta_2 should = 29.57
    predicted_alpha2_inv = C_from_3 * math.exp(math.pi / 2) + delta_2

    print(f"\n{'─' * 75}")
    print("  ONE-LOOP RUNNING FROM PLANCK SCALE")
    print(f"{'─' * 75}")

    print(f"\n  Hypothesis: α₂⁻¹(M_Pl)/α₃⁻¹(M_Pl) = exp(π/2) = {math.exp(math.pi/2):.4f}")
    print(f"\n  Running corrections (M_Pl → M_Z):")
    print(f"    Δα₂⁻¹ = -(b₂/2π) ln(M_Z/M_Pl) = {delta_2:.4f}")
    print(f"    Δα₃⁻¹ = -(b₃/2π) ln(M_Z/M_Pl) = {delta_3:.4f}")

    print(f"\n  From α₃⁻¹(M_Z) = 8.50:")
    print(f"    C = α₃⁻¹(M_Pl) = 8.50 - ({delta_3:.4f}) = {C_from_3:.4f}")
    print(f"    α₂⁻¹(M_Pl) = C × exp(π/2) = {C_from_3 * math.exp(math.pi/2):.4f}")

    print(f"\n  Predicted α₂⁻¹(M_Z) = {C_from_3 * math.exp(math.pi/2):.4f} + {delta_2:.4f}")
    print(f"                       = {predicted_alpha2_inv:.4f}")
    print(f"  Measured α₂⁻¹(M_Z)  = 29.57")
    print(f"  Difference: {abs(predicted_alpha2_inv - 29.57):.4f} "
          f"({abs(predicted_alpha2_inv - 29.57)/29.57*100:.2f}%)")

    # Also try: α₃⁻¹(M_Pl) = exp(-π/2) × α₂⁻¹(M_Pl)
    # So there's a single unknown: α₂⁻¹(M_Pl) = A
    # 29.57 = A + delta_2
    # 8.50  = A × exp(-π/2) + delta_3
    # From first: A = 29.57 - delta_2
    A = 29.57 - delta_2
    predicted_alpha3_inv = A * math.exp(-math.pi / 2) + delta_3

    print(f"\n  Alternative: fix from α₂⁻¹(M_Z):")
    print(f"    A = α₂⁻¹(M_Pl) = 29.57 - ({delta_2:.4f}) = {A:.4f}")
    print(f"    α₃⁻¹(M_Pl) = A × exp(-π/2) = {A * math.exp(-math.pi/2):.4f}")
    print(f"    Predicted α₃⁻¹(M_Z) = {predicted_alpha3_inv:.4f}")
    print(f"    Measured α₃⁻¹(M_Z)  = 8.50")
    print(f"    Difference: {abs(predicted_alpha3_inv - 8.50):.4f} "
          f"({abs(predicted_alpha3_inv - 8.50)/8.50*100:.2f}%)")

    # ── Plot ─────────────────────────────────────────────────────────────
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Window Pinning: Half-Twist on Threshold",
                 fontsize=14, fontweight="bold")

    K = np.linspace(0.1, 120.0, 500)

    # A: Self-sustaining products
    ax = axes[0, 0]
    colors_q = {2: "red", 3: "blue", 4: "green", 5: "orange", 6: "purple"}
    for q in range(2, 7):
        prods = [self_sustaining_product(q, K0) for K0 in K]
        ax.semilogy(K, prods, color=colors_q[q], lw=2, label=f"q={q}")
    ax.axhline(th_torus, color="black", ls="--", lw=1.5,
               label=f"2/π (torus) = {th_torus:.3f}")
    ax.axhline(th_klein, color="magenta", ls="-.", lw=2,
               label=f"1/π (Klein) = {th_klein:.3f}")
    if K_q3 and K_q4:
        ax.axvspan(K_q3, K_q4, alpha=0.15, color="green",
                   label=f"Window [{K_q3:.2f}, {K_q4:.2f})")
    ax.set_xlabel("K₀")
    ax.set_ylabel("(K₀/2) × w(q, K₀/2)²")
    ax.set_title("A. Self-sustaining with Klein threshold")
    ax.legend(fontsize=7, loc="lower right")
    ax.grid(True, alpha=0.3)
    ax.set_ylim(1e-10, 1)

    # B: Window size (max resolved q)
    ax = axes[1, 0]
    qmax_torus = []
    qmax_klein = []
    for K0 in K:
        qt = 1
        qk = 1
        for q in range(2, 10):
            if self_sustaining_product(q, K0) >= th_torus:
                qt = q
            else:
                break
        for q in range(2, 10):
            if self_sustaining_product(q, K0) >= th_klein:
                qk = q
            else:
                break
        qmax_torus.append(qt)
        qmax_klein.append(qk)

    ax.plot(K, qmax_klein, "r-", lw=2, label="Klein (1/π)")
    ax.plot(K, qmax_torus, "b--", lw=1.5, label="Torus (2/π)")
    ax.axhline(3, color="green", ls="--", lw=2, alpha=0.7, label="Target: q=3")
    ax.fill_between(K, 0, 3, alpha=0.08, color="green")
    if K_q3 and K_q4:
        ax.axvspan(K_q3, K_q4, alpha=0.15, color="green")
        ax.axvline(K_star, color="magenta", ls="-.", lw=2,
                   label=f"K₀* = {K_star:.3f}")
    ax.set_xlabel("K₀")
    ax.set_ylabel("Max resolved q")
    ax.set_title("B. Window size")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 8)

    # C: Running prediction
    ax = axes[0, 1]
    log_mu = np.linspace(2, 19, 200)
    mu_vals = 10**log_mu

    # Use C_from_3 normalization
    a2_run = [C_from_3 * math.exp(math.pi/2) - (B_2/(2*math.pi)) * math.log(mu/M_Pl)
              for mu in mu_vals]
    a3_run = [C_from_3 - (B_3/(2*math.pi)) * math.log(mu/M_Pl)
              for mu in mu_vals]

    ax.plot(log_mu, a2_run, "b-", lw=2, label="α₂⁻¹ (predicted)")
    ax.plot(log_mu, a3_run, "r-", lw=2, label="α₃⁻¹ (predicted)")
    ax.plot([math.log10(M_Z)], [29.57], "bs", ms=10, label="α₂⁻¹ measured")
    ax.plot([math.log10(M_Z)], [8.50], "rs", ms=10, label="α₃⁻¹ measured")
    ax.set_xlabel("log₁₀(μ/GeV)")
    ax.set_ylabel("α⁻¹")
    ax.set_title(f"C. Running from M_Pl (C={C_from_3:.2f})")
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # D: Summary diagram
    ax = axes[1, 1]
    ax.text(0.5, 0.85, "The Klein Bottle Window", fontsize=14,
            fontweight="bold", ha="center", transform=ax.transAxes)
    summary = (
        f"Half-twist on coupling: K_eff = K₀/2\n"
        f"Half-twist on threshold: 1/π (not 2/π)\n"
        f"Half-twist on BC: exp(π/2) asymmetry\n\n"
        f"Window: K₀ ∈ [{K_q3:.3f}, {K_q4:.3f})\n"
        f"K₀* = {K_star:.4f}\n\n"
        f"Topological ratio: exp(π/2) = {math.exp(math.pi/2):.4f}\n"
        f"Predicted α₂⁻¹(M_Z) = {predicted_alpha2_inv:.2f}  (meas: 29.57)\n"
        f"Error: {abs(predicted_alpha2_inv - 29.57)/29.57*100:.1f}%"
    )
    ax.text(0.5, 0.45, summary, fontsize=11, ha="center", va="center",
            transform=ax.transAxes, family="monospace",
            bbox=dict(boxstyle="round", facecolor="lightyellow", alpha=0.8))
    ax.axis("off")

    plt.tight_layout()
    out = "sync_cost/derivations/window_pinning.png"
    fig.savefig(out, dpi=150)
    print(f"\n  Saved: {out}")

    print(f"\n{'=' * 75}")
    print("  DONE")
    print(f"{'=' * 75}")


if __name__ == "__main__":
    main()
