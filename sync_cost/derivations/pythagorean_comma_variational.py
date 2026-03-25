"""
The Pythagorean comma in the variational staircase.

The comma is (3/2)^12 / 2^7 = 531441/524288 ≈ 1.01364.
Twelve perfect fifths don't close into seven octaves.

In the staircase-as-brachistochrone picture:
- The 1/2 tongue (octave) and 2/3 tongue (fifth) are the two widest
  non-trivial tongues (denominators 2 and 3 — the Klein bottle modes)
- Trying to tile frequency space with only these two tongues
  leaves a gap: the comma
- This gap is irreducible synchronization cost

Questions:
1. Does the comma appear in the tongue widths?
2. Does it appear in the variational cost?
3. Is the comma the minimum irreducible cost of the Klein bottle path?
"""

import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# The Pythagorean comma
# ============================================================

comma = (3/2)**12 / 2**7
print(f"Pythagorean comma: (3/2)^12 / 2^7 = {comma:.6f}")
print(f"  = 531441/524288")
print(f"  = 1 + {comma - 1:.6f}")
print(f"  In cents: {1200 * np.log2(comma):.2f}")
print()

# ============================================================
# Part 1: Tongue widths at q=2 and q=3
# ============================================================

print("=== Tongue widths and the comma ===")
print()

for K in [0.5, 0.7, 0.9, 0.95, 0.99]:
    w2 = (K/2)**2  # tongue width at q=2
    w3 = (K/2)**3  # tongue width at q=3

    # Total coverage by octaves (q=2 modes): there are phi(2)=1 mode at q=2
    # which is 1/2. Coverage = w2.
    # Total coverage by fifths (q=3 modes): there are phi(3)=2 modes at q=3
    # which are 1/3 and 2/3. Coverage = 2*w3.

    # If we try to tile [0,1] with only q=2 and q=3 tongues:
    # Available: w2 (from 1/2) + 2*w3 (from 1/3 and 2/3)
    total_23 = w2 + 2 * w3
    gap = 1.0 - total_23  # what's left uncovered

    # The Pythagorean attempt: 12 fifths to span 7 octaves
    # Cost of 12 fifths: 12 transitions at q=3 cost
    cost_12_fifths = 12 * (1 - w3)  # 12 transitions through q=3 tongue boundaries
    # Cost of 7 octaves: 7 transitions at q=2 cost
    cost_7_octaves = 7 * (1 - w2)
    # The extra cost of the Pythagorean path vs the octave path:
    cost_comma = cost_12_fifths - cost_7_octaves

    print(f"K = {K:.2f}:")
    print(f"  w(q=2) = {w2:.4f},  w(q=3) = {w3:.4f}")
    print(f"  Coverage by q=2,3 only: {total_23:.4f}  (gap: {gap:.4f})")
    print(f"  Cost(12 fifths) = {cost_12_fifths:.4f}")
    print(f"  Cost(7 octaves) = {cost_7_octaves:.4f}")
    print(f"  Cost difference (comma) = {cost_comma:.4f}")
    print(f"  Ratio: {cost_12_fifths/cost_7_octaves:.6f}")
    print()

# ============================================================
# Part 2: The comma as a ratio of tongue widths
# ============================================================

print("=== The comma from tongue width ratio ===")
print()

# w(1/2, K) = (K/2)^2
# w(1/3, K) = (K/2)^3
# Ratio: w(1/2)/w(1/3) = (K/2)^{-1} = 2/K
# But the Pythagorean comma involves 12 fifths vs 7 octaves.
# In tongue language: the total tongue measure along the "fifth path" vs "octave path"
#
# Fifth path: visit 12 tongue boundaries at q=3
# Octave path: visit 7 tongue boundaries at q=2
# For these to be equivalent: 12 * w3 should equal 7 * w2
# Ratio: 12*w3 / (7*w2) = 12*(K/2)^3 / (7*(K/2)^2) = (12/7)*(K/2)

print("For 12 fifths to equal 7 octaves in tongue measure:")
print("  12 * w(q=3) = 7 * w(q=2)")
print("  12 * (K/2)^3 = 7 * (K/2)^2")
print("  K/2 = 7/12")
print(f"  K = 7/6 = {7/6:.6f}")
print()
print(f"But the Pythagorean comma says (3/2)^12 ≠ 2^7.")
print(f"The frequency ratio is 531441/524288 = {comma:.6f}")
print()

# The tongue-width version:
# At q=2: the tongue at 1/2 has width (K/2)^2
# At q=3: the tongue at 2/3 has width (K/2)^3
# The "fifth" in the staircase is the step from one level to the next
# via the 2/3 mode. Twelve such steps should return to the start
# (7 octaves higher), but they overshoot by the comma.
#
# In the staircase, this means: following the path
# 1/2 → 2/3 → 2/3 → ... (12 steps of 2/3) does NOT land on
# the same tongue as 7 steps of 1/2.

# The deficit per step in the Stern-Brocot tree:
# Each "fifth" step multiplies by 3/2.
# Each "octave" step multiplies by 2.
# After 12 fifths: (3/2)^12 = 129.746
# After 7 octaves: 2^7 = 128
# Overshoot: 129.746 - 128 = 1.746
# Fractional: 1.746/128 = 0.01364 = comma - 1

print("=== The comma in the Stern-Brocot tree ===")
print()
print("The Stern-Brocot tree has no loops. 12 fifths and 7 octaves")
print("are two different PATHS through the tree that end at different")
print("nodes. The comma is the DISTANCE between these nodes.")
print()

# In the tree, 3/2 is a child of 1/1 and 2/1.
# Iterating: (3/2)^n as a fraction gives Stern-Brocot addresses.
# Let's trace the path.

from fractions import Fraction

print("Tracing 12 fifths as Stern-Brocot path:")
f = Fraction(1, 1)
for i in range(12):
    f = f * Fraction(3, 2)
    # Reduce to [1,2) by dividing out octaves
    while f >= 2:
        f = f / 2
    print(f"  Step {i+1:2d}: × 3/2 → {float(f):.6f}  (= {f})")

print()
print(f"After 12 fifths (mod octaves): {float(f):.6f}")
print(f"Should be 1.0 if the circle closed.")
print(f"Overshoot: {float(f) - 1:.6f}")
print(f"Pythagorean comma: {comma - 1:.6f}")
print(f"Match: {abs(float(f) - comma) < 1e-10}")

# ============================================================
# Part 3: Variational cost of the comma
# ============================================================

print()
print("=== Variational cost of the comma ===")
print()
print("The staircase's cost function charges (1 - w(p/q, K)) per")
print("transition through tongue p/q. The comma is the cost difference")
print("between the Pythagorean path and the direct path:")
print()

for K in [0.9, 0.95, 0.99]:
    w2 = (K/2)**2
    w3 = (K/2)**3

    # Cost per octave transition (through q=2 tongue)
    c_oct = 1 - w2
    # Cost per fifth transition (through q=3 tongue)
    c_fifth = 1 - w3

    # Pythagorean path: 12 fifths
    C_pyth = 12 * c_fifth
    # Direct path: 7 octaves
    C_direct = 7 * c_oct
    # Comma cost
    C_comma = C_pyth - C_direct

    # The comma as fraction of direct cost
    frac = C_comma / C_direct

    print(f"K = {K:.2f}:")
    print(f"  Cost(12 fifths) = {C_pyth:.4f}")
    print(f"  Cost(7 octaves) = {C_direct:.4f}")
    print(f"  Comma cost      = {C_comma:.4f} ({frac:.1%} of direct)")
    print(f"  Per-step excess = {C_comma/12:.6f}")
    print()

# ============================================================
# Part 4: The comma, the Klein bottle, and Omega_Lambda
# ============================================================

print("=== The comma and the Klein bottle ===")
print()
print("The Klein bottle selects q₂ = 2 and q₃ = 3.")
print("These are the octave and the fifth.")
print("The comma is the irreducible mismatch between these two.")
print()
print("The Farey sequence at n = q₂ × q₃ = 6 has |F₆| = 13 terms.")
print("Ω_Λ = 13/19 = 0.6842 (observed: 0.6847).")
print()
print("The comma is (3/2)¹² / 2⁷ = 3¹² / 2¹⁹.")
print(f"  3^12 = {3**12}")
print(f"  2^19 = {2**19}")
print(f"  Ratio = {3**12 / 2**19:.6f}")
print()
print("Note the denominator: 2^19. And 19 = |F₆| + q₂q₃ = 13 + 6.")
print(f"  2^19 = {2**19}")
print(f"  Ω_Λ denominator = 19")
print()

# The 19 in Omega_Lambda = 13/19 and the 19 in 2^19 (Pythagorean comma denominator)
# Is this a coincidence?

# In the comma: (3/2)^12 / 2^7 = 3^12 / (2^12 * 2^7) = 3^12 / 2^19
# The exponent 12 = 2 * 6 = 2 * q₂q₃
# The base 19 = 12 + 7 = q₂q₃*(q₂-1+q₃-1+...)?
# Actually: 19 = 12 + 7. And 12 fifths span 7 octaves.
# 12 + 7 = 19. The total number of "events" (transitions) in the
# Pythagorean cycle is 19: 12 fifths up and 7 octaves down.

print("The total transitions in the Pythagorean cycle:")
print("  12 fifths (up by 3/2) + 7 octaves (down by 1/2) = 19 transitions")
print(f"  = |F₆| + q₂q₃ = 13 + 6 = 19")
print()
print("12 = 2 × q₂q₃ = 2 × 6 (two complete Farey traversals)")
print("7 = |F₆| - q₂q₃ = 13 - 6 (the excess of states over scale)")
print()
print(f"Check: 12 = 2 × 6 = {2 * 6}")
print(f"Check: 7 = 13 - 6 = {13 - 6}")
print(f"Check: 12 + 7 = {12 + 7} = 19")
print()

# Wait — 7 = 13 - 6? Let's verify.
# |F₆| = 13. q₂q₃ = 6. 13 - 6 = 7. YES.
# And 12 = 2 * 6. So:
# 12 fifths = 2 × (q₂q₃) fifths
# 7 octaves = (|F₆| - q₂q₃) octaves
# Total = 2*q₂q₃ + |F₆| - q₂q₃ = |F₆| + q₂q₃ = 19

print("THE PYTHAGOREAN COMMA IS THE KLEIN BOTTLE'S FAILURE TO CLOSE.")
print()
print("12 fifths = 2 × q₂q₃ steps through the q=3 tongue")
print("7 octaves = (|F₆| - q₂q₃) steps through the q=2 tongue")
print("Total = |F₆| + q₂q₃ = 13 + 6 = 19 = denominator of Ω_Λ")
print()
print("The 19 in Ω_Λ = 13/19 IS the number of transitions in the")
print("Pythagorean cycle. The dark energy fraction is the ratio of")
print("locked modes (13) to total transitions (19) in the cycle that")
print("doesn't close — the comma cycle.")
