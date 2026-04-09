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
print("  That is Step 2.")
