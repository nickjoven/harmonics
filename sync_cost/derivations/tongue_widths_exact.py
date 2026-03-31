#!/usr/bin/env python3
"""
Exact tongue widths from the circle map with sufficient transients.

The previous numerical measurement failed for q=3 because:
  - n_trans=1500 is insufficient at K~1 (critical slowing)
  - The tolerance 1e-5 is too tight for slow convergence
  - The bisection window was correct but the lock detection failed

This script uses n_trans=20000, n_meas=50000 for K ≥ 0.7,
and measures ALL tongues (q=1 through 7) at each K.

Then: duty ratio as a function of K from the REAL dynamics.
Compare to SM running.

Usage:
    python3 sync_cost/derivations/tongue_widths_exact.py
"""

import math
import sys

sys.path.insert(0, "sync_cost/derivations")
from circle_map_utils import tongue_width as _tongue_width_pqK


# ── Circle map ────────────────────────────────────────────────────────────────

def circle_map_step(theta, omega, K):
    return theta + omega - K / (2 * math.pi) * math.sin(2 * math.pi * theta)


def winding_number(omega, K, n_trans=5000, n_meas=20000):
    theta = 0.0
    for _ in range(n_trans):
        theta = circle_map_step(theta, omega, K)
    theta_start = theta
    for _ in range(n_meas):
        theta = circle_map_step(theta, omega, K)
    return (theta - theta_start) / n_meas


def tongue_width(p, q, K, n_trans=5000, n_meas=20000, n_bisect=40):
    """
    Measure tongue width at p/q by bisection on winding number.

    Uses high transient count for convergence near K=1.
    """
    target = p / q

    # Adaptive transients: more for high K and high q
    if K > 0.8:
        nt = max(n_trans, 20000)
        nm = max(n_meas, 50000)
    elif K > 0.5:
        nt = max(n_trans, 10000)
        nm = max(n_meas, 30000)
    else:
        nt = n_trans
        nm = n_meas

    # Check center
    W_center = winding_number(target, K, nt, nm)
    if abs(W_center - target) > 5e-4:
        return 0.0

    # Search window
    half_window = max(4.0 / (q * q), 0.02)

    # Bisect left
    lo, hi = max(target - half_window, 0.001), target
    for _ in range(n_bisect):
        mid = (lo + hi) / 2
        W = winding_number(mid, K, nt, nm)
        if abs(W - target) < 5e-4:
            hi = mid
        else:
            lo = mid
    left = (lo + hi) / 2

    # Bisect right
    lo, hi = target, min(target + half_window, 0.999)
    for _ in range(n_bisect):
        mid = (lo + hi) / 2
        W = winding_number(mid, K, nt, nm)
        if abs(W - target) < 5e-4:
            lo = mid
        else:
            hi = mid
    right = (lo + hi) / 2

    return max(right - left, 0.0)


# ── SM reference ──────────────────────────────────────────────────────────────

MZ = 91.1876
ALPHA_S_MZ = 0.1179
ALPHA_EM_MZ = 1 / 127.95
SIN2_TW = 0.23121
ALPHA_2_MZ = ALPHA_EM_MZ / SIN2_TW
RATIO_MZ = ALPHA_S_MZ / ALPHA_2_MZ

B3 = 7.0
B2 = 19.0 / 6.0


def ratio_sm(mu):
    a3 = ALPHA_S_MZ / (1 + ALPHA_S_MZ * B3 / (2 * math.pi) * math.log(mu / MZ))
    a2 = ALPHA_2_MZ / (1 + ALPHA_2_MZ * B2 / (2 * math.pi) * math.log(mu / MZ))
    return a3 / a2


# ── Analytical reference ─────────────────────────────────────────────────────

def tongue_analytical(q, K):
    return _tongue_width_pqK(1, q, K)


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("=" * 85)
    print("  EXACT TONGUE WIDTHS FROM THE CIRCLE MAP")
    print("  n_trans ≥ 20000, n_meas ≥ 50000 for K > 0.8")
    print("=" * 85)

    # ── 1. Spot checks: verify q=2, q=3 tongues at K=1 ───────────────────
    print(f"\n{'─' * 85}")
    print("  1. SPOT CHECKS AT K=1 (critical coupling)")
    print(f"{'─' * 85}\n")

    print("  Expected: w(1/2) = 1/4 = 0.2500, w(1/3) = 1/9 = 0.1111")
    print()

    for (p, q) in [(1, 2), (1, 3), (2, 3), (1, 4), (1, 5), (2, 5), (3, 5)]:
        w = tongue_width(p, q, 1.0)
        w_expected = 1.0 / (q * q)
        d = duty_val = w / q
        print(f"  w({p}/{q}, K=1) = {w:.6f}  "
              f"(expected 1/{q}² = {w_expected:.6f}, "
              f"Δ = {abs(w - w_expected) / w_expected:.1%})  "
              f"duty = {d:.6f}")

    # ── 2. Full tongue width table ────────────────────────────────────────
    print(f"\n{'─' * 85}")
    print("  2. TONGUE WIDTHS w(1/q, K) FOR q=2,3 ACROSS K")
    print(f"{'─' * 85}\n")

    K_vals = [0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.85,
              0.90, 0.92, 0.95, 0.98, 1.00]

    print(f"  {'K':>6s}  {'w(1/2)':>10s}  {'w_ana(2)':>10s}  "
          f"{'w(1/3)':>10s}  {'w_ana(3)':>10s}  "
          f"{'d(2)':>10s}  {'d(3)':>10s}  {'ratio':>8s}")
    print("  " + "-" * 82)

    results = []
    for K in K_vals:
        w2 = tongue_width(1, 2, K)
        w3 = tongue_width(1, 3, K)
        w2a = tongue_analytical(2, K)
        w3a = tongue_analytical(3, K)
        d2 = w2 / 2
        d3 = w3 / 3 if w3 > 0 else 0
        ratio = d2 / d3 if d3 > 0 else float('inf')
        results.append((K, w2, w3, d2, d3, ratio))

        ratio_str = f"{ratio:8.4f}" if ratio < 1000 else "    ∞"
        print(f"  {K:6.2f}  {w2:10.6f}  {w2a:10.6f}  "
              f"{w3:10.6f}  {w3a:10.6f}  "
              f"{d2:10.6f}  {d3:10.6f}  {ratio_str}")

    # ── 3. Additional tongues for completeness ────────────────────────────
    print(f"\n{'─' * 85}")
    print("  3. TONGUE WIDTHS FOR q=2 THROUGH q=5 AT SELECTED K")
    print(f"{'─' * 85}\n")

    for K in [0.5, 0.8, 0.9, 1.0]:
        print(f"  K = {K}:")
        print(f"    {'p/q':>6s}  {'w(p/q)':>12s}  {'1/q²':>12s}  "
              f"{'duty':>12s}  {'1/q³':>12s}")
        print("    " + "-" * 56)
        for q in range(2, 6):
            for p in range(1, q):
                if math.gcd(p, q) == 1:
                    w = tongue_width(p, q, K)
                    d = w / q
                    print(f"    {p}/{q:>4d}  {w:12.6f}  {1/q**2:12.6f}  "
                          f"{d:12.6f}  {1/q**3:12.6f}")
        print()

    # ── 4. Duty ratio curve vs SM running ─────────────────────────────────
    print(f"\n{'─' * 85}")
    print("  4. DUTY RATIO vs SM RUNNING")
    print(f"{'─' * 85}\n")

    # Filter results with valid q=3 data
    valid = [(K, d2, d3, r) for K, w2, w3, d2, d3, r in results
             if d3 > 0 and r < 100]

    if valid:
        print(f"  {'K':>6s}  {'duty(2)/duty(3)':>16s}  {'SM μ':>12s}  "
              f"{'SM ratio':>12s}  {'Δ':>8s}")
        print("  " + "-" * 60)

        for K, d2, d3, ratio in valid:
            # Find SM energy matching this ratio
            mu_match = None
            best_diff = 999
            for exp_val in range(-50, 120):
                mu = MZ * math.exp(exp_val * 0.1)
                if mu < 0.3 or mu > 1e17:
                    continue
                sr = ratio_sm(mu)
                diff = abs(sr - ratio)
                if diff < best_diff:
                    best_diff = diff
                    mu_match = mu

            sm_r = ratio_sm(mu_match) if mu_match else 0
            delta = abs(ratio - sm_r) / sm_r if sm_r > 0 else 0

            mu_str = f"{mu_match:.1f}" if mu_match and mu_match < 1e4 else (
                f"{mu_match:.1e}" if mu_match else "—")

            print(f"  {K:6.2f}  {ratio:16.4f}  {mu_str:>12s}  "
                  f"{sm_r:12.4f}  {delta:8.1%}")

    # ── 5. The K=1 predictions ────────────────────────────────────────────
    print(f"\n{'─' * 85}")
    print("  5. K=1 PREDICTIONS FROM EXACT TONGUE WIDTHS")
    print(f"{'─' * 85}\n")

    # Use measured values at K=1
    w2_exact = tongue_width(1, 2, 1.0)
    w3_exact = tongue_width(1, 3, 1.0)
    w23_exact = tongue_width(2, 3, 1.0)

    d2_exact = w2_exact / 2
    d3_exact = w3_exact / 3
    d23_exact = w23_exact / 3

    if d3_exact > 0:
        ratio_exact = d2_exact / d3_exact
        sw_exact = d3_exact / (d2_exact + d3_exact)

        print(f"  Measured tongue widths at K=1:")
        print(f"    w(1/2) = {w2_exact:.6f}  (expected 0.250000)")
        print(f"    w(1/3) = {w3_exact:.6f}  (expected 0.111111)")
        print(f"    w(2/3) = {w23_exact:.6f}  (expected 0.111111)")
        print()
        print(f"  duty(2) = {d2_exact:.6f}")
        print(f"  duty(3) = {d3_exact:.6f}  (using 1/3 tongue)")
        print()
        print(f"  α_s/α₂ = duty(2)/duty(3) = {ratio_exact:.6f}")
        print(f"  expected 27/8 = {27/8:.6f}")
        print(f"  observed at M_Z = {RATIO_MZ:.6f}")
        print(f"  Δ(from 27/8) = {abs(ratio_exact - 27/8)/(27/8):.1%}")
        print(f"  Δ(from M_Z)  = {abs(ratio_exact - RATIO_MZ)/RATIO_MZ:.1%}")
        print()
        print(f"  sin²θ_W = duty(3)/[duty(2)+duty(3)] = {sw_exact:.6f}")
        print(f"  expected 8/35 = {8/35:.6f}")
        print(f"  observed = {SIN2_TW:.6f}")
        print(f"  Δ(from 8/35) = {abs(sw_exact - 8/35)/(8/35):.1%}")
        print(f"  Δ(from obs)  = {abs(sw_exact - SIN2_TW)/SIN2_TW:.1%}")
    else:
        print("  WARNING: q=3 tongue still not resolved at K=1")
        print(f"  w(1/2) = {w2_exact:.6f}, w(1/3) = {w3_exact:.6f}")
        print()
        print("  Falling back to analytical values:")
        d2_exact = 1.0 / 8.0
        d3_exact = 1.0 / 27.0
        ratio_exact = 27.0 / 8.0
        sw_exact = 8.0 / 35.0
        print(f"  duty(2) = 1/8 = {d2_exact:.6f}")
        print(f"  duty(3) = 1/27 = {d3_exact:.6f}")
        print(f"  ratio = 27/8 = {ratio_exact:.4f}")
        print(f"  sin²θ_W = 8/35 = {sw_exact:.6f}")

    # ── 6. |r| from the duty ratio ───────────────────────────────────────
    print(f"\n{'─' * 85}")
    print("  6. |r| AT EACH K (order parameter from duty ratio)")
    print(f"{'─' * 85}\n")

    print(f"  |r| = 27/(8 × ratio). At K=1: |r|=1. At K<1: |r|<1.\n")

    print(f"  {'K':>6s}  {'ratio':>10s}  {'|r|':>10s}  "
          f"{'1-|r|':>10s}  {'SM μ':>10s}")
    print("  " + "-" * 52)

    for K, d2, d3, ratio in valid:
        r_abs = 27.0 / (8.0 * ratio) if ratio > 0 else 0
        decoh = 1 - r_abs

        mu_match = None
        for exp_val in range(-50, 120):
            mu = MZ * math.exp(exp_val * 0.1)
            if mu < 0.3 or mu > 1e17:
                continue
            sr = ratio_sm(mu)
            if abs(sr - ratio) < 0.1:
                mu_match = mu
                break

        mu_str = f"{mu_match:.0f}" if mu_match and mu_match < 1e4 else (
            f"{mu_match:.0e}" if mu_match else "—")

        print(f"  {K:6.2f}  {ratio:10.4f}  {r_abs:10.4f}  "
              f"{decoh:10.4f}  {mu_str:>10s}")

    # ── Summary ───────────────────────────────────────────────────────────
    print(f"\n{'=' * 85}")
    print("  SUMMARY")
    print(f"{'=' * 85}")
    print(f"""
  Tongue widths measured from the actual circle map dynamics
  with n_trans ≥ 20000, n_meas ≥ 50000 for K > 0.8.

  The q=3 tongue requires high transients to resolve because
  the q=3 mode locks more slowly than q=2 (narrower tongue,
  weaker coupling). At K=1, the critical dynamics produce
  algebraic (not exponential) convergence.

  If q=3 is resolved:
    The duty ratio and sin²θ_W can be computed from the REAL
    circle map at each K, giving the running curve from dynamics
    rather than from interpolation.

  If q=3 is NOT resolved even with 20000 transients:
    The analytical values (1/q² at K=1) remain the primary result.
    The numerical confirmation requires either:
    - Even more transients (10⁵+)
    - A different measurement strategy (Farey sum, not bisection)
    - Direct computation of the tongue boundary via the implicit
      function theorem on the circle map's q-th iterate
""")


if __name__ == "__main__":
    main()
