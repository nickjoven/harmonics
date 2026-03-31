#!/usr/bin/env python3
"""
Within-sector mode asymmetry on the Klein bottle.

The field equation has exact (f₁,f₂)↔(f₂,f₁) symmetry because:
  - g(f₁,f₂) is radially symmetric about (1/φ, 1/φ)
  - tongue widths w(p,q,K) depend only on (p,q), not direction
  - the twist (-1)^{q₁} affects |r| but not population updates

This script:
  1. Confirms the symmetry analytically
  2. Shows that asymmetry MUST come from the Kuramoto dynamics
     (lattice geometry breaks x↔y via the x-direction twist)
  3. Computes the within-sector mode structure at each K

Usage:
    python3 sync_cost/derivations/klein_within_sector.py
"""

import math
import sys
import numpy as np
from fractions import Fraction

sys.path.insert(0, "sync_cost/derivations")
from circle_map_utils import PHI, INV_PHI, tongue_width


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


def main():
    DEPTH = 6
    tree = stern_brocot_tree(DEPTH)
    pairs_klein = [(f1, f2) for f1 in tree for f2 in tree
                   if (f1.denominator % 2) != (f2.denominator % 2)]

    g_golden = lambda f1, f2: math.exp(
        -5 * ((f1 - INV_PHI) ** 2 + (f2 - INV_PHI) ** 2))

    print("=" * 75)
    print("  WITHIN-SECTOR ASYMMETRY ANALYSIS")
    print("=" * 75)

    # ── Step 1: Confirm symmetry ────────────────────────────────────────────
    print("\n  Step 1: Testing (f₁,f₂)↔(f₂,f₁) symmetry in field equation")
    print("  " + "-" * 60)

    max_asym = 0.0
    for f1, f2 in pairs_klein:
        g12 = g_golden(float(f1), float(f2))
        g21 = g_golden(float(f2), float(f1))
        asym = abs(g12 - g21)
        if asym > max_asym:
            max_asym = asym

    print(f"  Max |g(f₁,f₂) - g(f₂,f₁)| = {max_asym:.2e}")

    # Check tongue width symmetry
    for K in [0.3, 0.7, 1.0, 2.0]:
        max_tw_asym = 0.0
        for f1, f2 in pairs_klein:
            w_prod_12 = (tongue_width(f1.numerator, f1.denominator, K) *
                         tongue_width(f2.numerator, f2.denominator, K))
            w_prod_21 = (tongue_width(f2.numerator, f2.denominator, K) *
                         tongue_width(f1.numerator, f1.denominator, K))
            a = abs(w_prod_12 - w_prod_21)
            if a > max_tw_asym:
                max_tw_asym = a
        print(f"  Max |w₁w₂(12) - w₁w₂(21)| at K={K}: {max_tw_asym:.2e}")

    print("\n  → Field equation is EXACTLY symmetric under swap.")
    print("  → Sector asymmetry N(2,3)/N(3,2) ≡ 1 at all K.")
    print("  → Asymmetry must come from DYNAMICS (Kuramoto lattice).")

    # ── Step 2: Within-sector mode structure ────────────────────────────────
    print(f"\n{'=' * 75}")
    print("  Step 2: Within-sector mode populations vs K")
    print("=" * 75)

    # Key modes
    key_modes = {
        "(2,3)": [(Fraction(1, 2), Fraction(1, 3)),
                   (Fraction(1, 2), Fraction(2, 3))],
        "(3,2)": [(Fraction(1, 3), Fraction(1, 2)),
                   (Fraction(2, 3), Fraction(1, 2))],
        "(2,5)": [(Fraction(1, 2), Fraction(1, 5)),
                   (Fraction(1, 2), Fraction(2, 5)),
                   (Fraction(1, 2), Fraction(3, 5)),
                   (Fraction(1, 2), Fraction(4, 5))],
        "(5,2)": [(Fraction(1, 5), Fraction(1, 2)),
                   (Fraction(2, 5), Fraction(1, 2)),
                   (Fraction(3, 5), Fraction(1, 2)),
                   (Fraction(4, 5), Fraction(1, 2))],
    }

    K_vals = [0.1, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0]

    for K0 in K_vals:
        print(f"\n  K = {K0}")
        print(f"  {'mode':>15s}  {'g':>10s}  {'w₁':>10s}  {'w₂':>10s}  "
              f"{'g·w₁·w₂':>12s}  {'sector':>8s}")
        print("  " + "-" * 70)

        for sector, modes in key_modes.items():
            sector_total = 0.0
            mode_data = []
            for f1, f2 in modes:
                g = g_golden(float(f1), float(f2))
                w1 = tongue_width(f1.numerator, f1.denominator, K0)
                w2 = tongue_width(f2.numerator, f2.denominator, K0)
                product = g * w1 * w2
                sector_total += product
                mode_data.append((f1, f2, g, w1, w2, product))

            for f1, f2, g, w1, w2, product in mode_data:
                frac = product / sector_total if sector_total > 0 else 0
                print(f"  ({str(f1):>4s},{str(f2):>4s})  {g:10.6f}  "
                      f"{w1:10.6f}  {w2:10.6f}  {product:12.8f}  {sector:>8s}")

    # ── Step 3: Where asymmetry lives ───────────────────────────────────────
    print(f"\n{'=' * 75}")
    print("  Step 3: WHY the Kuramoto lattice breaks the symmetry")
    print("=" * 75)
    print("""
  The field equation treats x and y as independent product axes.
  But on the Klein bottle lattice:

    x-direction: θ_{N+1,j} = θ_{1,N-j} + π   (twist + REFLECT)
    y-direction: θ_{i,N+1} = θ_{i,1}           (periodic)

  The x-direction has:
    1. Antiperiodic BC (π shift) — selects odd winding numbers
    2. y-REFLECTION (j → N-j) — couples x-gradients to y-structure

  The y-direction has:
    1. Periodic BC — allows all winding numbers

  This x≠y asymmetry means:
    - Modes with gradient primarily in x see antiperiodic + reflect
    - Modes with gradient primarily in y see periodic only
    - A mode (p₁/q₁, p₂/q₂) is NOT equivalent to (p₂/q₂, p₁/q₁)

  The REFLECTION is the key: it mixes spatial directions.
  A q₁=2 gradient in x must be compatible with the y-reflection,
  while a q₁=3 gradient in x faces a different constraint.

  This is why the Kuramoto simulation shows:
    - Torus locks to 1/1 (59%) at K=3
    - Klein locks to 1/3 (48%) at K=3
    - 100× broader acceleration on Klein (from D19 session)

  The field equation misses this because it factorizes w₁×w₂.
  The coupling term sin(θ_neighbor - θ_self) is NOT factorizable
  when the neighbor map involves y-reflection.
""")

    # ── Step 4: Predicted asymmetry from BC analysis ────────────────────────
    print(f"{'=' * 75}")
    print("  Step 4: Predicted asymmetry from boundary conditions")
    print("=" * 75)

    print("""
  Antiperiodic BC in x: allowed winding = n + 1/2 (half-integer)
  Periodic BC in y: allowed winding = m (integer)

  For a mode (p₁/q₁, p₂/q₂):
    x-winding ∝ p₁/q₁ must be compatible with half-integer
    y-winding ∝ p₂/q₂ must be compatible with integer

  Half-integer condition: p₁/q₁ = (2k+1)/2 for some k
    → q₁ must be even (specifically q₁=2 satisfies at lowest order)

  Integer condition: p₂/q₂ = m for some m
    → q₂ = 1 at lowest order, but ANY q₂ works (p₂/q₂ is a frequency,
      not a winding number — the periodic BC imposes no constraint)

  BUT the y-reflection at x-boundary mixes the directions:
    θ_{N+1,j} = θ_{1,N-j} + π

  This means x-winding at row j couples to x-winding at row (N-j).
  For odd N (e.g., N=3): the middle row j=1 maps to itself → fixed point
  For even N: no fixed row → all rows pair up

  The middle-row fixed point for odd N means:
    q₁=2 (even) oscillators at the fixed row see themselves shifted by π
    q₁=3 (odd) oscillators at the fixed row see themselves shifted by π

  Self-consistency at the fixed row:
    θ + π ≡ θ (mod 2π/q₁)
    → π must be a multiple of 2π/q₁
    → q₁ must be even (q₁=2: π = π ✓; q₁=3: π ≠ 2π/3 ✗)

  This is the XOR asymmetry from D19!
  The lattice dynamics enforce it; the field equation doesn't.
""")

    print("=" * 75)
    print("  DONE")
    print("=" * 75)


if __name__ == "__main__":
    main()
