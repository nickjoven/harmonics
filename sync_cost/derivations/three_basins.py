#!/usr/bin/env python3
"""
The three basins at q=3: where probability is invited.

At q=2: two basins with Z₂ symmetry → equal weights → deterministic.
At q=3: three basins with BROKEN symmetry → unequal weights → probability.

The three period-3 orbits of the circle map visit different parts of
the circle where sin(2πθ) has different curvature. This breaks the
symmetry and gives each basin a different width.

The Born rule: P_i ∝ Δθ_i² ∝ (basin width)².
The mass: m_i ∝ 1/Δθ_i² (more massive = harder to resolve = narrower basin).

If the three generation masses are the inverse Born weights at the
moment probability is invited, the mass ratios come from the circle
map geometry at the 1/3 tongue boundary.

Usage:
    python3 sync_cost/derivations/three_basins.py
"""

import math


# ── Circle map ────────────────────────────────────────────────────────────────

def f(theta, omega, K):
    return theta + omega - K / (2 * math.pi) * math.sin(2 * math.pi * theta)


def f3(theta, omega, K):
    """Third iterate: f∘f∘f."""
    t = f(theta, omega, K)
    t = f(t, omega, K)
    t = f(t, omega, K)
    return t


def f_prime(theta, K):
    return 1 - K * math.cos(2 * math.pi * theta)


def f3_prime(theta, omega, K):
    """Derivative of third iterate (chain rule)."""
    t0 = theta
    t1 = f(t0, omega, K)
    t2 = f(t1, omega, K)
    return f_prime(t0, K) * f_prime(t1, K) * f_prime(t2, K)


# ── Find period-3 orbits ─────────────────────────────────────────────────────

def find_period3_fixed_points(omega, K, n_search=2000):
    """
    Find fixed points of f³(θ) - θ - 1 = 0 by scanning.

    Period-3 orbits with winding number 1/3 satisfy:
    f³(θ) = θ + 1 (one full cycle in 3 steps).
    """
    fixed_points = []
    for i in range(n_search):
        theta = i / n_search
        val = f3(theta, omega, K) - theta - 1.0

        # Check for sign change
        theta_next = (i + 1) / n_search
        val_next = f3(theta_next, omega, K) - theta_next - 1.0

        if val * val_next < 0:
            # Bisect to find the root
            lo, hi = theta, theta_next
            for _ in range(60):
                mid = (lo + hi) / 2
                v = f3(mid, omega, K) - mid - 1.0
                if v * val < 0:
                    hi = mid
                else:
                    lo = mid
                    val = v
            root = (lo + hi) / 2

            # Classify: stable (|f3'| < 1) or unstable (|f3'| > 1)
            deriv = f3_prime(root, omega, K)
            stable = abs(deriv) < 1.0

            # Check it's genuinely period-3 (not period-1)
            # f(root) should NOT equal root + 1/3 within period-1 tolerance
            t1 = f(root, omega, K)
            is_period1 = abs((t1 - root) % 1 - 1/3) < 1e-6 and abs(f_prime(root, K)) < 1

            if not is_period1:
                fixed_points.append((root % 1.0, deriv, stable))

    # Remove duplicates
    unique = []
    for pt in fixed_points:
        is_dup = False
        for upt in unique:
            if abs(pt[0] - upt[0]) < 1e-6 or abs(pt[0] - upt[0] - 1) < 1e-6:
                is_dup = True
                break
        if not is_dup:
            unique.append(pt)

    return sorted(unique, key=lambda x: x[0])


def compute_basin_widths(stable_pts, unstable_pts):
    """
    Compute basin widths from the arrangement of stable/unstable points.

    Each stable point's basin extends to the nearest unstable points
    on either side (on the circle).
    """
    if not stable_pts or not unstable_pts:
        return []

    # Sort all points on [0, 1)
    s_phases = sorted([p[0] for p in stable_pts])
    u_phases = sorted([p[0] for p in unstable_pts])

    basins = []
    for s in s_phases:
        # Find the unstable points bracketing this stable point
        left = None
        right = None
        for u in u_phases:
            if u < s:
                if left is None or u > left:
                    left = u
            if u > s:
                if right is None or u < right:
                    right = u

        # Handle wraparound
        if left is None:
            left = max(u_phases) - 1.0  # wrap around
        if right is None:
            right = min(u_phases) + 1.0  # wrap around

        width = right - left
        if width < 0:
            width += 1.0
        if width > 1:
            width -= 1.0

        basins.append((s, width, left % 1, right % 1))

    return basins


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("=" * 80)
    print("  THE THREE BASINS: WHERE PROBABILITY IS INVITED")
    print("  Period-3 orbits of the circle map, basin widths, mass ratios")
    print("=" * 80)

    # ── 1. Period-3 fixed points inside the 1/3 tongue ───────────────────
    print(f"\n{'─' * 80}")
    print("  1. PERIOD-3 ORBITS AT VARIOUS K (inside 1/3 tongue)")
    print(f"{'─' * 80}\n")

    # The 1/3 tongue is centered at Ω = 1/3
    omega = 1.0 / 3.0

    for K in [0.5, 0.7, 0.8, 0.9, 0.95, 1.0]:
        pts = find_period3_fixed_points(omega, K)
        stable = [p for p in pts if p[2]]
        unstable = [p for p in pts if not p[2]]

        print(f"  K = {K}:  {len(stable)} stable, {len(unstable)} unstable")
        for theta, deriv, is_stable in pts:
            stype = "STABLE" if is_stable else "unstable"
            print(f"    θ = {theta:.6f}  f³'(θ) = {deriv:+.6f}  {stype}")

        if stable and unstable:
            basins = compute_basin_widths(stable, unstable)
            print(f"    Basin widths:")
            for s, w, l, r in basins:
                print(f"      θ* = {s:.6f}  width = {w:.6f}  "
                      f"[{l:.4f}, {r:.4f}]")
        print()

    # ── 2. Basin widths at the tongue boundary ────────────────────────────
    print(f"\n{'─' * 80}")
    print("  2. BASIN WIDTHS NEAR THE 1/3 TONGUE BOUNDARY")
    print(f"{'─' * 80}\n")

    print("  The tongue boundary is where probability is born.")
    print("  Just inside the boundary: basins narrow, weights diverge.\n")

    # Find the tongue boundary: where the period-3 orbits first appear
    # At the boundary, stable and unstable merge (saddle-node)
    # Scan Ω at the edge of the 1/3 tongue at various K

    for K in [0.8, 0.9, 1.0]:
        print(f"  K = {K}:")

        # Scan Ω from center to edge
        omega_center = 1.0 / 3.0
        best_basins = None
        best_omega = None

        for i_omega in range(50):
            omega_test = omega_center + i_omega * 0.001
            pts = find_period3_fixed_points(omega_test, K, n_search=3000)
            stable = [p for p in pts if p[2]]
            unstable = [p for p in pts if not p[2]]

            if len(stable) >= 3 and len(unstable) >= 3:
                basins = compute_basin_widths(stable, unstable)
                if basins:
                    best_basins = basins
                    best_omega = omega_test
            elif len(stable) < 3 and best_basins is not None:
                # We just passed the boundary
                break

        if best_basins:
            widths = sorted([b[1] for b in best_basins])
            total = sum(widths)
            normalized = [w / total for w in widths]

            print(f"    Near boundary (Ω = {best_omega:.4f}):")
            print(f"    Basin widths: {', '.join(f'{w:.6f}' for w in widths)}")
            print(f"    Normalized:   {', '.join(f'{n:.4f}' for n in normalized)}")

            if min(widths) > 0:
                ratios = [w / min(widths) for w in widths]
                print(f"    Ratios (to smallest): "
                      f"{', '.join(f'{r:.2f}' for r in ratios)}")

                # Born rule: P ∝ width²
                born = [w ** 2 for w in widths]
                born_norm = [b / sum(born) for b in born]
                print(f"    Born weights (P ∝ w²): "
                      f"{', '.join(f'{b:.4f}' for b in born_norm)}")

                # Mass ∝ 1/P (heavier = rarer)
                mass_ratios = [max(born) / b for b in born]
                print(f"    Mass ratios (∝ 1/P): "
                      f"{', '.join(f'{m:.2f}' for m in mass_ratios)}")
        else:
            print(f"    No period-3 orbits found")
        print()

    # ── 3. The asymmetry from sin(2πθ) ───────────────────────────────────
    print(f"\n{'─' * 80}")
    print("  3. WHY THE BASINS ARE UNEQUAL: sin(2πθ) curvature")
    print(f"{'─' * 80}\n")

    print("  The period-3 orbit visits three phases: θ₁, θ₂, θ₃.")
    print("  At each phase, f'(θ) = 1 - K cos(2πθ).")
    print("  The curvature of sin at each visit determines the basin width.")
    print()

    K = 1.0
    omega = 1.0 / 3.0
    pts = find_period3_fixed_points(omega, K)
    stable = [p for p in pts if p[2]]

    if stable:
        print(f"  Stable period-3 orbits at K=1, Ω=1/3:")
        for i, (theta, deriv, _) in enumerate(stable):
            # The orbit visits theta, f(theta), f(f(theta))
            t0 = theta
            t1 = f(t0, omega, K) % 1
            t2 = f(f(t0, omega, K), omega, K) % 1

            fp0 = f_prime(t0, K)
            fp1 = f_prime(t1, K)
            fp2 = f_prime(t2, K)

            # Curvature of sin at each point
            curv0 = -K * (2 * math.pi) ** 2 * math.sin(2 * math.pi * t0)
            curv1 = -K * (2 * math.pi) ** 2 * math.sin(2 * math.pi * t1)
            curv2 = -K * (2 * math.pi) ** 2 * math.sin(2 * math.pi * t2)

            print(f"\n    Orbit {i+1}: θ₁={t0:.4f}, θ₂={t1:.4f}, θ₃={t2:.4f}")
            print(f"      f'(θ₁) = {fp0:+.4f}  f'(θ₂) = {fp1:+.4f}  "
                  f"f'(θ₃) = {fp2:+.4f}")
            print(f"      Π f' = {deriv:+.6f}")
            print(f"      curvature: {curv0:+.1f}, {curv1:+.1f}, {curv2:+.1f}")

    # ── 4. Comparison with lepton masses ──────────────────────────────────
    print(f"\n{'─' * 80}")
    print("  4. COMPARISON WITH LEPTON AND QUARK MASSES")
    print(f"{'─' * 80}\n")

    # SM mass ratios
    m_e, m_mu, m_tau = 0.511, 105.66, 1776.86  # MeV
    m_u, m_c, m_t = 2.16, 1270, 172760  # MeV
    m_d, m_s, m_b = 4.67, 93.4, 4180  # MeV

    print(f"  Lepton mass ratios (to m_e):")
    print(f"    e : μ : τ = 1 : {m_mu/m_e:.1f} : {m_tau/m_e:.1f}")
    print(f"  Up-type quark mass ratios (to m_u):")
    print(f"    u : c : t = 1 : {m_c/m_u:.0f} : {m_t/m_u:.0f}")
    print(f"  Down-type quark mass ratios (to m_d):")
    print(f"    d : s : b = 1 : {m_s/m_d:.1f} : {m_b/m_d:.0f}")

    # ── 5. The q=2 symmetry for contrast ─────────────────────────────────
    print(f"\n{'─' * 80}")
    print("  5. q=2 FOR CONTRAST: EQUAL BASINS (no probability)")
    print(f"{'─' * 80}\n")

    omega2 = 0.5
    for K in [0.8, 0.9, 1.0]:
        pts2 = []
        # Period-2: f²(θ) = θ + 1
        for i in range(2000):
            theta = i / 2000
            t2 = f(f(theta, omega2, K), omega2, K)
            val = t2 - theta - 1.0

            theta_next = (i + 1) / 2000
            t2n = f(f(theta_next, omega2, K), omega2, K)
            val_next = t2n - theta_next - 1.0

            if val * val_next < 0:
                lo, hi = theta, theta_next
                for _ in range(60):
                    mid = (lo + hi) / 2
                    v = f(f(mid, omega2, K), omega2, K) - mid - 1.0
                    if v * val < 0:
                        hi = mid
                    else:
                        lo = mid
                        val = v
                root = (lo + hi) / 2
                d2 = f_prime(root, K) * f_prime(f(root, omega2, K), K)
                stable = abs(d2) < 1
                pts2.append((root % 1, d2, stable))

        # Deduplicate
        unique2 = []
        for pt in pts2:
            is_dup = False
            for upt in unique2:
                if abs(pt[0] - upt[0]) < 1e-5:
                    is_dup = True
                    break
            if not is_dup:
                unique2.append(pt)

        stable2 = [p for p in unique2 if p[2]]
        unstable2 = [p for p in unique2 if not p[2]]

        print(f"  K = {K}: {len(stable2)} stable, {len(unstable2)} unstable")
        if len(stable2) == 2:
            # Basin widths
            s_sorted = sorted(stable2, key=lambda x: x[0])
            w1 = s_sorted[1][0] - s_sorted[0][0]
            w2 = 1.0 - w1
            print(f"    Basin widths: {w1:.6f}, {w2:.6f}")
            print(f"    Ratio: {max(w1,w2)/min(w1,w2):.4f}")
            print(f"    → {'EQUAL (symmetric)' if abs(w1-w2) < 0.01 else 'UNEQUAL'}")
        print()

    # ── Summary ───────────────────────────────────────────────────────────
    print(f"\n{'=' * 80}")
    print("  SUMMARY")
    print(f"{'=' * 80}")
    print(f"""
  q=2: Two basins with Z₂ symmetry → equal weights → no probability.
       Binary choice. Deterministic at the boundary.

  q=3: Three basins with BROKEN Z₃ → unequal weights → probability born.
       The sin(2πθ) coupling has period 1, not 1/3. The three visits
       see different curvatures. Different curvatures → different basins
       → different Born weights → different masses.

  The three generation masses are the inverse Born weights at the
  moment probability is invited: the basin widths of the period-3
  orbits at the 1/3 tongue boundary.

  If the basin ratio matches the lepton mass hierarchy (1:207:3477)
  or the quark hierarchy (1:588:80000), the three generations are
  explained by the geometry of the circle map at q=3.
""")


if __name__ == "__main__":
    main()
