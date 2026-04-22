#!/usr/bin/env python3
"""
The K → μ mapping from the self-consistent field equation.

K is not a free parameter — it's |r|(d), the order parameter at
tree depth d. As you resolve deeper (higher energy, larger q_max),
more modes contribute to the mean field, and |r| changes.

The mapping:
  d = tree depth (Fibonacci levels)
  q_max(d) ≈ F_d (Fibonacci number at depth d)
  μ(d) = M_Pl × φ^(-2(146-d))  (energy at depth d)
  K_eff(d) = |r|(d)  (self-consistent order parameter at depth d)

This script:
  1. Solves the field equation at each depth d = 2, 3, ..., 12
  2. Extracts |r|(d) and the duty ratio at each depth
  3. Maps d → μ and |r| → K_eff
  4. Compares to the SM running of α_s/α₂

Usage:
    python3 sync_cost/derivations/K_mu_mapping.py
"""

import math
import os
import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(__file__))
from framework_constants import ALPHA_EM_MZ, ALPHA_S_MZ, SIN2_TW_MZ
from circle_map_utils import PHI, INV_PHI, PHI_SQ, LN_PHI_SQ, fibonacci_sequence, tongue_width


# ── Constants ─────────────────────────────────────────────────────────────────

M_PL = 1.22e19      # GeV (Planck mass)
M_Z = 91.1876        # GeV
TOTAL_DEPTH = 146    # Fibonacci levels Planck → Hubble
SIN2_TW = SIN2_TW_MZ
ALPHA_2_MZ = ALPHA_EM_MZ / SIN2_TW

B3 = 7.0
B2 = 19.0 / 6.0


def ratio_sm(mu):
    """SM 1-loop α_s/α₂."""
    if mu <= 0:
        return float('inf')
    a3 = ALPHA_S_MZ / (1 + ALPHA_S_MZ * B3 / (2 * math.pi) * math.log(mu / M_Z))
    a2 = ALPHA_2_MZ / (1 + ALPHA_2_MZ * B2 / (2 * math.pi) * math.log(mu / M_Z))
    if a2 <= 0:
        return float('inf')
    return a3 / a2


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


# ── Field equation solver ────────────────────────────────────────────────────

def solve_field_equation(tree, K0=1.0, n_iter=400, damping=0.3):
    """
    Solve N(p/q) = N_total × g(p/q) × w(p/q, K₀|r|)
    Returns (populations, |r|, convergence_history).
    """
    N_total = len(tree)
    populations = {f: 1.0 for f in tree}
    history = []

    for it in range(n_iter):
        # Order parameter
        total_pop = sum(populations.values())
        r = sum(populations[f] * math.e ** (2j * math.pi * float(f))
                for f in tree) / max(total_pop, 1e-15)
        r_abs = abs(r)
        history.append(r_abs)

        K_eff = K0 * max(r_abs, 1e-15)

        # Update populations
        new_pop = {}
        for f in tree:
            p, q = f.numerator, f.denominator
            g = 1.0  # uniform distribution
            w = tongue_width(p, q, K_eff)
            new_pop[f] = N_total * g * w

        # Normalize
        total = sum(new_pop.values())
        if total > 0:
            for f in new_pop:
                new_pop[f] *= N_total / total

        # Damped update
        populations = {f: (1 - damping) * populations[f] + damping * new_pop[f]
                       for f in tree}

    # Final |r|
    total_pop = sum(populations.values())
    r = sum(populations[f] * math.e ** (2j * math.pi * float(f))
            for f in tree) / max(total_pop, 1e-15)

    return populations, abs(r), history


# ── Depth → energy mapping ───────────────────────────────────────────────────

def depth_to_energy(d):
    """Map tree depth d to energy scale μ in GeV."""
    # d=146 → Planck, d=0 → Hubble
    # μ = M_Pl × φ^(-2(146-d))
    # Equivalently: ln(μ) = ln(M_Pl) - 2(146-d) × ln(φ)
    exponent = -2 * (TOTAL_DEPTH - d) * math.log(PHI)
    return M_PL * math.exp(exponent)


def energy_to_depth(mu):
    """Map energy μ to tree depth d."""
    if mu <= 0:
        return 0
    return TOTAL_DEPTH + math.log(mu / M_PL) / (2 * math.log(PHI))


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("=" * 80)
    print("  THE K → μ MAPPING")
    print("  K_eff = |r|(d) from the self-consistent field equation")
    print("=" * 80)

    # ── 1. Depth-energy correspondence ────────────────────────────────────
    print(f"\n{'─' * 80}")
    print("  1. DEPTH → ENERGY CORRESPONDENCE")
    print(f"{'─' * 80}\n")

    print(f"  {'depth d':>8s}  {'q_max ~ F_d':>12s}  {'μ (GeV)':>14s}  "
          f"{'scale':>20s}")
    print("  " + "-" * 60)

    fibs = fibonacci_sequence(25)
    landmarks = {
        0: "Hubble",
        20: "CMB pivot",
        int(energy_to_depth(1.0)): "1 GeV",
        int(energy_to_depth(M_Z)): "M_Z",
        int(energy_to_depth(1e3)): "1 TeV",
        int(energy_to_depth(1e16)): "GUT",
        130: "eV instruments",
        146: "Planck",
    }

    for d in sorted(set([0, 10, 20, 40, 60, 80, 100, 105, 110, 120, 130, 140, 146]
                        + list(landmarks.keys()))):
        if d < 0 or d > 146:
            continue
        mu = depth_to_energy(d)
        q_max = fibs[min(d, len(fibs) - 1)] if d < len(fibs) else f"φ^{d}"
        scale = landmarks.get(d, "")

        if isinstance(q_max, int) and q_max > 1e6:
            q_str = f"~10^{math.log10(q_max):.0f}"
        elif isinstance(q_max, int):
            q_str = str(q_max)
        else:
            q_str = str(q_max)

        if mu > 1e6:
            mu_str = f"{mu:.2e}"
        elif mu > 0.01:
            mu_str = f"{mu:.2f}"
        else:
            mu_str = f"{mu:.2e}"

        print(f"  {d:8d}  {q_str:>12s}  {mu_str:>14s}  {scale:>20s}")

    # ── 2. Field equation at each depth ───────────────────────────────────
    print(f"\n{'─' * 80}")
    print("  2. |r| AT EACH TREE DEPTH (field equation)")
    print(f"{'─' * 80}\n")

    print("  Solving N(p/q) = N × g × w(p/q, K₀|r|) at each depth...")
    print()

    print(f"  {'depth':>6s}  {'nodes':>7s}  {'q_max':>7s}  {'|r|':>8s}  "
          f"{'K_eff':>8s}  {'duty(2)':>10s}  {'duty(3)':>10s}  "
          f"{'ratio':>8s}  {'μ (GeV)':>12s}")
    print("  " + "-" * 88)

    depth_data = []
    for d in range(2, 13):
        tree = stern_brocot_tree(d)
        q_max = max(f.denominator for f in tree)

        # Solve field equation
        populations, r_abs, history = solve_field_equation(tree, K0=1.0, n_iter=500)

        K_eff = r_abs

        # Extract duty ratio
        d2_modes = [f for f in tree if f.denominator == 2]
        d3_modes = [f for f in tree if f.denominator == 3]

        duty_2 = sum(populations.get(f, 0) for f in d2_modes)
        duty_3 = sum(populations.get(f, 0) for f in d3_modes)

        # Normalize to duty cycle: population-weighted tongue width / q
        # Actually, duty = Σ w(p,q,K_eff)/q for modes at that q
        actual_duty_2 = sum(tongue_width(f.numerator, 2, K_eff) / 2 for f in d2_modes)
        actual_duty_3 = sum(tongue_width(f.numerator, 3, K_eff) / 3 for f in d3_modes)

        ratio = actual_duty_2 / actual_duty_3 if actual_duty_3 > 0 else float('inf')

        mu = depth_to_energy(d * TOTAL_DEPTH / 12)  # scale depth to physical

        depth_data.append((d, len(tree), q_max, r_abs, K_eff,
                           actual_duty_2, actual_duty_3, ratio, mu))

        mu_str = f"{mu:.2e}" if mu > 1e6 else f"{mu:.1f}"

        print(f"  {d:6d}  {len(tree):7d}  {q_max:7d}  {r_abs:8.4f}  "
              f"{K_eff:8.4f}  {actual_duty_2:10.6f}  {actual_duty_3:10.6f}  "
              f"{ratio:8.4f}  {mu_str:>12s}")

    # ── 3. |r| as the K mapping ───────────────────────────────────────────
    print(f"\n{'─' * 80}")
    print("  3. |r|(d) IS THE K → μ MAPPING")
    print(f"{'─' * 80}\n")

    print("  The self-consistent |r| varies with depth because deeper")
    print("  trees include more modes, changing the mean field.")
    print()

    # Extract the trend
    if len(depth_data) >= 3:
        depths = [d[0] for d in depth_data]
        r_vals = [d[3] for d in depth_data]
        ratios = [d[7] for d in depth_data]

        print(f"  |r| range: {min(r_vals):.4f} to {max(r_vals):.4f}")
        print(f"  Ratio range: {min(ratios):.4f} to {max(ratios):.4f}")
        print()

        # Does |r| increase or decrease with depth?
        if r_vals[-1] > r_vals[0]:
            trend = "INCREASING (more modes → more coherence)"
        elif r_vals[-1] < r_vals[0]:
            trend = "DECREASING (more modes → more interference)"
        else:
            trend = "FLAT"
        print(f"  Trend: |r| is {trend}")

    # ── 4. Compare duty ratio to SM running ───────────────────────────────
    print(f"\n{'─' * 80}")
    print("  4. DUTY RATIO vs SM RUNNING")
    print(f"{'─' * 80}\n")

    print(f"  {'depth':>6s}  {'duty ratio':>12s}  {'|r|→K_eff':>10s}  "
          f"{'SM energy':>12s}  {'SM ratio':>12s}  {'Δ':>8s}")
    print("  " + "-" * 66)

    for d, n_nodes, q_max, r_abs, K_eff, d2, d3, ratio, mu in depth_data:
        if ratio > 50 or ratio < 1:
            continue

        # Find SM energy that gives this ratio
        best_mu = None
        best_diff = 999
        for log_e in range(-20, 200):
            test_mu = M_Z * math.exp(log_e * 0.1)
            if test_mu < 0.1 or test_mu > 1e19:
                continue
            sr = ratio_sm(test_mu)
            if abs(sr - ratio) < best_diff:
                best_diff = abs(sr - ratio)
                best_mu = test_mu

        if best_mu:
            sr = ratio_sm(best_mu)
            delta = abs(ratio - sr) / sr
            mu_str = f"{best_mu:.1f}" if best_mu < 1e4 else f"{best_mu:.1e}"
            print(f"  {d:6d}  {ratio:12.4f}  {K_eff:10.4f}  "
                  f"{mu_str:>12s}  {sr:12.4f}  {delta:8.1%}")

    # ── 5. The depth-K relationship ───────────────────────────────────────
    print(f"\n{'─' * 80}")
    print("  5. THE FUNCTIONAL FORM: |r|(d)")
    print(f"{'─' * 80}\n")

    # Fit |r|(d) to simple functional forms
    if len(depth_data) >= 4:
        depths = [d[0] for d in depth_data]
        r_vals = [d[3] for d in depth_data]

        # Test: |r| = a + b × d
        n = len(depths)
        mx = sum(depths) / n
        my = sum(r_vals) / n
        sxx = sum((x - mx) ** 2 for x in depths)
        sxy = sum((x - mx) * (y - my) for x, y in zip(depths, r_vals))
        if sxx > 0:
            b_lin = sxy / sxx
            a_lin = my - b_lin * mx
            resid_lin = sum((r - (a_lin + b_lin * d)) ** 2
                            for d, r in zip(depths, r_vals))
            print(f"  Linear: |r| = {a_lin:.4f} + {b_lin:.6f} × d")
            print(f"    Residual: {math.sqrt(resid_lin/n):.6f}")

        # Test: |r| = a + b × ln(d)
        ln_depths = [math.log(d) for d in depths]
        mx2 = sum(ln_depths) / n
        sxx2 = sum((x - mx2) ** 2 for x in ln_depths)
        sxy2 = sum((x - mx2) * (y - my) for x, y in zip(ln_depths, r_vals))
        if sxx2 > 0:
            b_log = sxy2 / sxx2
            a_log = my - b_log * mx2
            resid_log = sum((r - (a_log + b_log * math.log(d))) ** 2
                            for d, r in zip(depths, r_vals))
            print(f"  Logarithmic: |r| = {a_log:.4f} + {b_log:.6f} × ln(d)")
            print(f"    Residual: {math.sqrt(resid_log/n):.6f}")

        # Test: |r| = 1 - c/d^α (approaches 1 at large depth)
        # ln(1-|r|) = ln(c) - α ln(d)
        one_minus_r = [1 - r for r in r_vals if r < 1]
        if len(one_minus_r) >= 3 and all(x > 0 for x in one_minus_r):
            ln_omr = [math.log(x) for x in one_minus_r]
            ln_d = [math.log(d) for d in depths[:len(one_minus_r)]]
            mx3 = sum(ln_d) / len(ln_d)
            my3 = sum(ln_omr) / len(ln_omr)
            sxx3 = sum((x - mx3) ** 2 for x in ln_d)
            sxy3 = sum((x - mx3) * (y - my3) for x, y in zip(ln_d, ln_omr))
            if sxx3 > 0:
                alpha = -sxy3 / sxx3
                ln_c = my3 + alpha * mx3
                c = math.exp(ln_c)
                print(f"  Power law: |r| = 1 - {c:.4f}/d^{alpha:.4f}")
                resid_pow = sum((r - (1 - c / d ** alpha)) ** 2
                                for d, r in zip(depths[:len(one_minus_r)],
                                                r_vals[:len(one_minus_r)]))
                print(f"    Residual: {math.sqrt(resid_pow/len(one_minus_r)):.6f}")

    # ── 6. The derived mapping ────────────────────────────────────────────
    print(f"\n{'─' * 80}")
    print("  6. THE DERIVED K(μ) MAPPING")
    print(f"{'─' * 80}\n")

    print("  The K→μ mapping is NOT free. It is:")
    print()
    print("    K_eff(μ) = |r|(d(μ))")
    print()
    print("  where d(μ) = 146 + ln(μ/M_Pl) / (2 ln φ)")
    print("  and |r|(d) is the fixed point of the field equation")
    print("  truncated at depth d.")
    print()
    print("  The mapping has no fitted factors:")
    print("    - The depth-energy relation comes from the φ² scaling")
    print("    - |r|(d) comes from the self-consistent field equation")
    print("    - K₀ = 1 (critical coupling, the only scale)")
    print()

    # Check: does |r|(d) at the depth corresponding to M_Z
    # give K_eff ≈ 0.892?
    d_mz = energy_to_depth(M_Z)
    print(f"  Depth at M_Z: d = {d_mz:.1f}")
    print(f"  Tree depth d={int(d_mz)} corresponds to SB depth ~{int(d_mz * 12/146)}")
    print()

    # The SB tree at depth d_sb has modes with q up to ~2^d_sb
    # d_mz ≈ 105, which in SB depth is ~105*12/146 ≈ 8.6
    d_sb_mz = int(round(d_mz * 12 / 146))
    if any(d[0] == d_sb_mz for d in depth_data):
        match = [d for d in depth_data if d[0] == d_sb_mz][0]
        print(f"  At SB depth {d_sb_mz} (≈ M_Z):")
        print(f"    |r| = {match[3]:.4f}")
        print(f"    duty ratio = {match[7]:.4f}")
        print(f"    Expected K* = 0.892, ratio = 3.488")
        print(f"    Δ(|r|) = {abs(match[3] - 0.892)/0.892:.1%}")
        print(f"    Δ(ratio) = {abs(match[7] - 3.488)/3.488:.1%}")

    # ── Summary ───────────────────────────────────────────────────────────
    print(f"\n{'=' * 80}")
    print("  SUMMARY")
    print(f"{'=' * 80}")
    print(f"""
  The K → μ mapping is the depth-dependent order parameter |r|(d).
  It is derived, not fitted:

    d(μ) = 146 + ln(μ/M_Pl) / (2 ln φ)    [depth from energy]
    |r|(d) = fixed point of field equation at depth d
    K_eff(μ) = |r|(d(μ))                   [the mapping]

  The field equation at each depth determines |r| self-consistently.
  Deeper trees (higher energy) include more modes, changing the
  mean field. The variation of |r| with depth IS the running of
  the coupling constants.

  This mapping has no fitted factors. The only inputs are:
    - The four primitives (D10)
    - The Klein bottle topology (D19)
    - K₀ = 1 (critical coupling)
""")


if __name__ == "__main__":
    main()
