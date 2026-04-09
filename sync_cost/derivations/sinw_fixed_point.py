"""
sin^2(theta_W) fixed-point test.

Hypothesis: the two branches from sinW_running_check.py are BOTH true
simultaneously, and their simultaneous truth is a fixed point.

  Branch (i):  Tree scale ≠ M_Pl. The K=1 "tree scale" corresponds to
               some μ_tree determined self-consistently, not to the
               reduced Planck mass.

  Branch (ii): The framework's running is the K→μ duty-cycle mapping,
               not SM 1-loop RG. Observed couplings at M_Z are
               duty(q, K*) evaluated at some K* < 1.

  Fixed-point reading: K* and μ_tree (or equivalently K* and M_Z via
  the K→μ map) are determined jointly by requiring the framework's
  duty-cycle identities to match ALL observed coupling ratios at M_Z
  simultaneously. If a single K* reproduces both α_s/α_2 AND sin²θ_W,
  the fixed point is real. Otherwise, the two branches are
  incompatible and one must be dropped.

This script runs in small, verifiable steps:
  Step 1 (this script): build the K-grid and compute numerical tongue
                         widths at each K via circle_map_utils.
  Step 2: solve for K_α such that duty(2, K)/duty(3, K) = α_s/α_2(M_Z).
  Step 3: solve for K_θ such that sin²θ_W(K) = sin²θ_W(M_Z).
  Step 4: compare K_α with K_θ. If |K_α - K_θ| is small, the fixed
          point holds. If not, it doesn't.

Step 1 only needs to validate that we can compute duty(q, K) reliably
near K = 1. The numerical tongue-width computation is expensive for
K close to 1 (critical slowing), so we build a modest grid and sanity-
check it against the known K=1 values.

Usage:
    python sync_cost/derivations/sinw_fixed_point.py
"""

import math
import sys
from pathlib import Path

# Make circle_map_utils importable
sys.path.insert(0, str(Path(__file__).parent))
from circle_map_utils import tongue_width, tongue_width_numerical  # noqa: E402


# ============================================================================
# Observed values at M_Z (PDG 2024)
# ============================================================================

M_Z = 91.1876
ALPHA_EM_MZ = 1 / 127.95
SIN2_TW_MZ = 0.23121
ALPHA_S_MZ = 0.1179
ALPHA_2_MZ = ALPHA_EM_MZ / SIN2_TW_MZ       # ≈ 0.0338
ALPHA_Y_MZ = ALPHA_EM_MZ / (1 - SIN2_TW_MZ)  # ≈ 0.0102

RATIO_S_2_OBS = ALPHA_S_MZ / ALPHA_2_MZ
print(f"Observed ratios at M_Z:")
print(f"  α_s/α_2       = {RATIO_S_2_OBS:.6f}")
print(f"  sin²θ_W       = {SIN2_TW_MZ}")
print(f"  1/α_em        = {1/ALPHA_EM_MZ:.4f}")
print()


# ============================================================================
# Step 1: duty(q, K) via numerical tongue widths
# ============================================================================

def duty_analytic(q, K):
    """Analytic duty cycle: tongue_width / period."""
    return tongue_width(1, q, K) / q


def duty_numerical(q, K, fast=True):
    """Measure duty cycle by actually running the circle map.

    Slow near K=1 (critical slowing). fast=True reduces iteration counts
    for quick scans; fast=False for publication-grade values.
    """
    if fast:
        w = tongue_width_numerical(1, q, K, n_trans=2000, n_meas=5000, n_bisect=25)
    else:
        w = tongue_width_numerical(1, q, K)
    return w / q


# Sanity check: at K=1, analytic duty = 1/q^3
print("=" * 70)
print("STEP 1: duty(q, K) sanity check")
print("=" * 70)
print()
print(f"{'q':>3} {'K':>6} {'analytic':>12} {'expected':>12} {'check':>8}")
print("-" * 50)
for q in [2, 3]:
    d_analytic = duty_analytic(q, 1.0)
    expected = 1.0 / (q ** 3)
    check = "OK" if abs(d_analytic - expected) < 1e-10 else "FAIL"
    print(f"{q:>3} {1.0:>6.3f} {d_analytic:>12.6f} {expected:>12.6f} {check:>8}")
print()

# Build a modest K grid for later steps. Only analytic values for Step 1 —
# numerical is too slow for a grid scan. We use the analytic formula
# (perturbative for K<1, exact 1/q^2 at K=1).
K_GRID = [0.70, 0.75, 0.80, 0.85, 0.90, 0.92, 0.94, 0.96, 0.98, 1.00]

print(f"{'K':>6} {'duty(2)':>12} {'duty(3)':>12} {'ratio':>12} "
      f"{'sin²θ_W':>12}")
print("-" * 60)
for K in K_GRID:
    d2 = duty_analytic(2, K)
    d3 = duty_analytic(3, K)
    ratio = d2 / d3 if d3 > 0 else float("inf")
    sin2 = d3 / (d2 + d3)
    print(f"{K:>6.3f} {d2:>12.8f} {d3:>12.8f} {ratio:>12.6f} {sin2:>12.6f}")
print()

print("Observations from the grid (step 1 output):")
print(f"  - At K=1 (critical): ratio = 27/8 = 3.375, sin²θ_W = 8/35 ≈ 0.2286")
print(f"  - At K<1 (perturbative): ratio = 9/K (diverges as K→0)")
print(f"  - The K=1 value is DISCONTINUOUS with the perturbative limit:")
print(f"    lim_{{K→1⁻}} perturbative ratio = 9, not 27/8.")
print(f"  - This is because the perturbative formula w = 2(K/2)^q/q")
print(f"    breaks down as K→1, where the Ford-circle formula w = 1/q²")
print(f"    takes over. The two formulas join at K=1 only in value, not")
print(f"    in K-derivative.")
print()
print("Implication for the fixed-point test:")
print("  The analytic duty(q, K) has no smooth K-dependence through K=1.")
print("  To get a meaningful K→μ running story, we need the NUMERICAL")
print("  tongue widths from actual circle-map dynamics at K near 1.")
print()


# ============================================================================
# Step 2: numerical tongue widths near K=1
# ============================================================================

import numpy as np
from circle_map_utils import winding_number


def scan_tongue_width(p, q, K, om_center, half_window, n_points=200,
                       n_trans=2000, n_meas=6000):
    """Measure actual tongue width by scanning Ω around the tongue center.

    The standard circle map is θ_{n+1} = θ_n + Ω - (K/2π)sin(2π θ_n).
    At K < 1 the p/q tongue is NOT centered at Ω = p/q because the
    sin term introduces an average phase shift. We scan a window, find
    the min and max Ω with winding number exactly p/q, and return the
    extent. If fewer than 2 points lock, return 0.
    """
    target = p / q
    oms = np.linspace(om_center - half_window, om_center + half_window, n_points)
    locked = [om for om in oms
              if abs(winding_number(om, K, n_trans, n_meas) - target) < 5e-4]
    if len(locked) < 2:
        return 0.0
    return max(locked) - min(locked)


def duty_2_3_numerical(K, fast=True):
    """Return (duty(2), duty(3)) at coupling K from actual circle-map scans.

    The 1/2 tongue centers near Ω = 0.5 (the sin term averages to zero
    for period-2). The 1/3 tongue centers shift with K; at K near 1 the
    shift is substantial (Ω ~ 0.34 empirically).
    """
    w2 = scan_tongue_width(1, 2, K, om_center=0.5, half_window=0.25,
                           n_points=180 if fast else 300)
    # 1/3 tongue: the center shifts toward 0.34 at K near 1
    # Scan a wider window to be safe
    w3 = scan_tongue_width(1, 3, K, om_center=0.35, half_window=0.08,
                           n_points=180 if fast else 300)
    return w2 / 2, w3 / 3


print("=" * 70)
print("STEP 2: numerical duty(2, K) and duty(3, K) near K=1")
print("=" * 70)
print()
print("These are measured directly from the circle map at each K,")
print("with the 1/3 tongue center empirically located at Ω ~ 0.34")
print("(shifted from p/q = 0.333 by the sin-term phase average).")
print()

K_NEAR_ONE = [0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99]

print(f"{'K':>6} {'duty(2)':>12} {'duty(3)':>12} {'ratio d2/d3':>14} "
      f"{'sin²θ_W':>12} {'resid %':>10}")
print("-" * 72)

results = []
for K in K_NEAR_ONE:
    d2, d3 = duty_2_3_numerical(K)
    if d3 == 0:
        print(f"{K:>6.3f}  (q=3 tongue not resolved)")
        continue
    ratio = d2 / d3
    sin2 = d3 / (d2 + d3)
    resid_sin = (sin2 - SIN2_TW_MZ) / SIN2_TW_MZ * 100
    resid_ratio = (ratio - RATIO_S_2_OBS) / RATIO_S_2_OBS * 100
    results.append((K, d2, d3, ratio, sin2))
    print(f"{K:>6.3f} {d2:>12.6f} {d3:>12.6f} {ratio:>14.4f} "
          f"{sin2:>12.6f} {resid_sin:>+10.2f}")

print()
print("Observations:")
print(f"  - Observed α_s/α_2 at M_Z     = {RATIO_S_2_OBS:.4f}")
print(f"  - Observed sin²θ_W at M_Z     = {SIN2_TW_MZ}")
print()
print("  Look at the numerical ratio and sin²θ_W columns above.")
print()

# Summarize: does any K match α_s/α_2?
print("Step 2 verdict (α_s/α_2 constraint alone):")
ratios = [r[3] for r in results]
if not ratios:
    print("  No K value resolved both tongues — cannot decide.")
else:
    min_ratio, max_ratio = min(ratios), max(ratios)
    if min_ratio <= RATIO_S_2_OBS <= max_ratio:
        # Linear interpolation to find K_alpha
        for i in range(len(results) - 1):
            K1, _, _, r1, _ = results[i]
            K2, _, _, r2, _ = results[i + 1]
            if (r1 - RATIO_S_2_OBS) * (r2 - RATIO_S_2_OBS) <= 0:
                frac = (RATIO_S_2_OBS - r1) / (r2 - r1)
                K_alpha = K1 + frac * (K2 - K1)
                print(f"  Ratio range brackets observed value: "
                      f"K_alpha ≈ {K_alpha:.4f}")
                break
    else:
        print(f"  Numerical ratio ∈ [{min_ratio:.4f}, {max_ratio:.4f}] does")
        print(f"  NOT bracket the observed {RATIO_S_2_OBS:.4f}.")
        if min_ratio > RATIO_S_2_OBS:
            print(f"  All numerical ratios are ABOVE observed; no K_alpha in")
            print(f"  this window reproduces α_s/α_2 from duty cycles.")
        else:
            print(f"  All numerical ratios are BELOW observed; no K_alpha in")
            print(f"  this window reproduces α_s/α_2 from duty cycles.")
print()

# Summarize: does any K match sin²θ_W?
print("Step 2 verdict (sin²θ_W constraint alone):")
sin2s = [r[4] for r in results]
if not sin2s:
    print("  No K value resolved both tongues — cannot decide.")
else:
    min_s, max_s = min(sin2s), max(sin2s)
    if min_s <= SIN2_TW_MZ <= max_s:
        for i in range(len(results) - 1):
            K1, _, _, _, s1 = results[i]
            K2, _, _, _, s2 = results[i + 1]
            if (s1 - SIN2_TW_MZ) * (s2 - SIN2_TW_MZ) <= 0:
                frac = (SIN2_TW_MZ - s1) / (s2 - s1)
                K_theta = K1 + frac * (K2 - K1)
                print(f"  sin²θ_W range brackets observed value: "
                      f"K_theta ≈ {K_theta:.4f}")
                break
    else:
        print(f"  Numerical sin²θ_W ∈ [{min_s:.6f}, {max_s:.6f}] does")
        print(f"  NOT bracket the observed {SIN2_TW_MZ:.6f}.")
        if max_s < SIN2_TW_MZ:
            print(f"  All numerical values are BELOW observed; no K_theta in")
            print(f"  this window reproduces sin²θ_W from duty cycles.")
        else:
            print(f"  All numerical values are ABOVE observed; no K_theta in")
            print(f"  this window reproduces sin²θ_W from duty cycles.")
print()
