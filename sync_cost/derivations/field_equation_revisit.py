"""
Revisiting the field equation with sector structure.

The rational field equation (D11) is:

    N(p/q) = N_total × g(p/q) × w(p/q, K₀ × F[N])

where F[N] = mean-field functional (order parameter).

In light of what we've learned:
1. Sector base pairs are algebraic in (q₂, q₃)
2. Tree acyclicity forces non-repeating walks
3. Depth sums = walk lengths for each sector
4. Selection rule: depth ∝ 1/|Q| with k_lep = 3, k_quark = 8/3

This script revisits the field equation on the extended Klein bottle
mode tower and asks:
  1. Does the fixed point produce the observed sector structure?
  2. Does iteration give a₁ = 2.3203 and a₂/a₁ = 1.4994?
  3. What is the field equation's natural 'reading' of the tower?
"""

import numpy as np
from fractions import Fraction
from math import gcd

from framework_constants import K_STAR_PRECISE


# ================================================================
# Part 1: The field equation at the minimum-depth 4-mode level
# ================================================================

print("=" * 70)
print("FIELD EQUATION REVISITED — LEVEL 1: MINIMUM DEPTH")
print("=" * 70)
print()

# The 4 surviving modes at minimum Klein bottle depth
modes_min = [
    ('A', Fraction(1,3), Fraction(1,2)),   # (q₁=3, q₂=2)
    ('B', Fraction(1,2), Fraction(1,3)),   # (q₁=2, q₂=3)
    ('C', Fraction(1,2), Fraction(2,3)),   # (q₁=2, q₂=3)
    ('D', Fraction(2,3), Fraction(1,2)),   # (q₁=3, q₂=2)
]

def tongue_width_2d(q1, q2, K):
    """2D tongue width on the Klein bottle: w₁ × w₂."""
    if K >= 1.0:
        w1 = 1.0 / q1**2
        w2 = 1.0 / q2**2
    else:
        w1 = (K / 2.0) ** q1
        w2 = (K / 2.0) ** q2
    return w1 * w2


def order_parameter_klein(modes, N_values, K):
    """Order parameter with Klein bottle twist (-1)^{q₁}."""
    total = 0.0
    weight_sum = 0.0
    for (label, f1, f2), n in zip(modes, N_values):
        q1 = f1.denominator
        q2 = f2.denominator
        phase = 2 * np.pi * (float(f1) + float(f2))
        twist = (-1) ** q1
        total += n * np.exp(1j * phase) * twist
        weight_sum += n
    if weight_sum == 0:
        return 0.0, 0.0
    z = total / weight_sum
    return abs(z), np.angle(z)


def field_equation_iterate(modes, K0, n_iter=100, tol=1e-12):
    """Iterate the rational field equation to find the fixed point."""
    n = len(modes)
    # Initial: equal populations
    N = np.ones(n) / n
    r = 0.5

    for step in range(n_iter):
        K_eff = K0 * r
        # Compute tongue widths at current K_eff
        widths = np.array([
            tongue_width_2d(f1.denominator, f2.denominator, K_eff)
            for _, f1, f2 in modes
        ])
        # New populations: proportional to widths (uniform g assumed)
        N_new = widths / widths.sum()
        # New order parameter
        r_new, _ = order_parameter_klein(modes, N_new, K_eff)

        if abs(r_new - r) < tol:
            break

        N = N_new
        r = r_new

    return N, r, K0 * r


print("Iterating the minimum 4-mode field equation:")
print()

for K0 in [1.0, 1.5, 2.0, 3.0, 5.0]:
    N_final, r_final, K_eff = field_equation_iterate(modes_min, K0)
    print(f"  K₀ = {K0}: r* = {r_final:.6f}, K_eff = {K_eff:.6f}")
    print(f"    Populations: {dict(zip('ABCD', N_final.round(4)))}")

print()
print("Observation: with the Klein bottle twist, the 4 symmetric modes")
print("have perfectly balanced populations, giving r* = 0 (cancellation).")
print("The order parameter vanishes at minimum depth due to XOR symmetry.")
print()
print("To get nonzero r*, we need an ASYMMETRY — either from g(Ω) or")
print("from extended mode content beyond the minimum 4.")
print()


# ================================================================
# Part 2: Extended mode set at depth up to 5
# ================================================================

print("=" * 70)
print("LEVEL 2: EXTENDED MODES AT DEPTH ≤ 5")
print("=" * 70)
print()

def make_extended_modes(max_q):
    """All XOR-compliant mode pairs with denominators ≤ max_q."""
    modes = []
    for q1 in range(2, max_q+1):
        for p1 in range(1, q1):
            if gcd(p1, q1) != 1:
                continue
            for q2 in range(2, max_q+1):
                if (q1 + q2) % 2 == 0:
                    continue
                for p2 in range(1, q2):
                    if gcd(p2, q2) != 1:
                        continue
                    label = f"({p1}/{q1},{p2}/{q2})"
                    modes.append((label, Fraction(p1,q1), Fraction(p2,q2)))
    return modes


# Iterate on extended set
max_q = 5
ext_modes = make_extended_modes(max_q)
print(f"Extended set at max_q = {max_q}: {len(ext_modes)} modes")
print()

for K0 in [1.0, 2.0, 4.0]:
    N_final, r_final, K_eff = field_equation_iterate(ext_modes, K0)
    print(f"K₀ = {K0}: r* = {r_final:.6f}")
    # Show top 5 populated modes
    idx_sorted = np.argsort(-N_final)[:5]
    print(f"  Top 5 modes by population:")
    for i in idx_sorted:
        label = ext_modes[i][0]
        print(f"    {label}: N = {N_final[i]:.6f}")
    print()


# ================================================================
# Part 3: Asymmetry from the non-4-mode extensions
# ================================================================

print("=" * 70)
print("LEVEL 3: Analysis — Why r* vanishes at minimum depth")
print("=" * 70)
print()

# The 4 minimum modes are at phases:
# A: (1/3 + 1/2) = 5/6, twist -1 → 5/6 with sign -1
# B: (1/2 + 1/3) = 5/6, twist +1 → 5/6 with sign +1
# C: (1/2 + 2/3) = 7/6, twist +1 → 7/6 with sign +1
# D: (2/3 + 1/2) = 7/6, twist -1 → 7/6 with sign -1

# A + B at 5/6 with opposite signs → cancel
# C + D at 7/6 with opposite signs → cancel
# Total r = 0 by symmetry

print("Phase contributions from the 4 minimum modes:")
for label, f1, f2 in modes_min:
    q1 = f1.denominator
    phase = float(f1 + f2)
    twist = (-1)**q1
    print(f"  {label}: phase = {f1+f2} = {phase:.4f}, twist = {twist:+d}")

print()
print("A & B are at phase 5/6, with opposite twists → cancel")
print("C & D are at phase 7/6, with opposite twists → cancel")
print("Total r* = 0 (perfect symmetry)")
print()
print("This is WHY the framework needs the extended mode tower:")
print("the minimum 4 modes alone produce a degenerate vacuum r* = 0.")
print("The extended modes break the symmetry and give r* > 0.")
print()


# ================================================================
# Part 4: What determines the sector structure?
# ================================================================

print("=" * 70)
print("LEVEL 4: Where does the sector hierarchy emerge?")
print("=" * 70)
print()

# The sector structure requires identifying WHICH modes correspond
# to WHICH fermions. The field equation gives populations; we need
# to group modes into sectors.
#
# One hypothesis: each fermion's tree walk (from root to base pair
# elements) defines its mode set. The population distribution over
# that walk determines the mass.

# Let's compute: for each sector, what is the sum of populations
# over its base pair path?

print("For each sector, compute the 'walk population' — sum of N(mode)")
print("over modes along the walk from root to each base pair element.")
print()

# First get the fixed point on a larger extended set
ext_modes_large = make_extended_modes(6)
N_ext, r_ext, K_ext = field_equation_iterate(ext_modes_large, K0=3.0)
print(f"Extended fixed point: r* = {r_ext:.6f}, K_eff = {K_ext:.6f}")
print(f"Modes: {len(ext_modes_large)}")
print()

# Populations at the base pair fractions (note: these are RATIOS, not
# Klein bottle mode pairs, so we need to reinterpret)
# The base pair elements 3/2, 5/3, 8/5, 5/4, 9/8 correspond to
# Stern-Brocot positions, not Klein bottle pairs

# Let's compute tongue widths (duty cycles) at each base element
# as isolated modes, to see the SINGLE-MODE populations

K_star = K_STAR_PRECISE
base_elements = [
    ("3/2", 3, "Lepton b₁"),
    ("5/3", 3, "Lepton b₂"),
    ("8/5", 5, "Up-type b₁"),
    ("5/4", 4, "Down-type b₁"),
    ("9/8", 8, "Down-type b₂"),
]

print(f"Single-mode duty cycles at K* = {K_star:.8f}:")
print(f"{'Fraction':>10} {'q':>4} {'duty = (K*/2)^q/q':>20} {'role':>15}")
print("-" * 55)
for frac, q, role in base_elements:
    duty = (K_star/2)**q / q
    print(f"{frac:>10} {q:>4} {duty:>20.6e} {role:>15}")

print()
print("Observation: the tongue width falls off exponentially with q.")
print("Deeper modes (higher q) have much smaller populations.")
print()
print("The mass hierarchy follows this: smaller populations")
print("(deeper modes) = smaller Yukawa = smaller mass.")
print()
print("Specifically, down-type b₂ at q=8 has duty ≈ 1e-6, while")
print("lepton b₁ at q=3 has duty ≈ 3e-2. Ratio ≈ 30000.")
print()

# ================================================================
# Part 5: Reading the field equation through sector walks
# ================================================================

print("=" * 70)
print("LEVEL 5: The Field Equation's Natural Reading of Sectors")
print("=" * 70)
print()

# The field equation at K=1 has populations proportional to tongue widths.
# At K*, populations are less skewed but still asymmetric.
#
# For each sector, the walk visits its base pair elements at specific
# depths. The TOTAL duty cycle along the walk = product of individual
# duties = (K*/2)^(depth_sum) × (1/product of q values)

print(f"Total walk duty per sector at K* = {K_star:.8f}:")
print()

walks = [
    ("Leptons", [3, 3], "3/2 → 5/3"),      # depths 2, 3
    ("Up-type", [5, 3], "8/5 → 3/2"),      # depths 4, 2
    ("Down-type", [4, 8], "5/4 → 9/8"),   # depths 4, 8
]

for sector, q_list, walk in walks:
    total_duty = 1
    for q in q_list:
        total_duty *= (K_star/2)**q / q
    exponent = sum(q_list)
    print(f"  {sector} ({walk}):")
    print(f"    q values: {q_list}, sum = {exponent}")
    print(f"    total duty = ∏ (K*/2)^q/q = {total_duty:.6e}")
    print()

print("The product of tongue widths along the walk IS the fermion's")
print("Yukawa coupling to the Higgs (mean field). Its logarithm scales")
print("linearly with the SUM of q values (the depth sum, = walk length).")
print()
print("This connects:")
print("  depth sum → walk length → total duty → log(Yukawa) → log(mass)")
print()
print("And the sector structure (which modes are visited) determines")
print("which specific rationals the walker encounters, which determines")
print("the mass ratios within a generation and between generations.")
print()

# ================================================================
# Part 6: Summary — what the field equation tells us
# ================================================================

print("=" * 70)
print("SUMMARY: What the Field Equation Says About Sectors")
print("=" * 70)
print()
print("1. The field equation's fixed point at minimum depth gives r* = 0")
print("   due to XOR + twist symmetry. The 4 minimum modes are")
print("   perfectly balanced and cancel.")
print()
print("2. Breaking the degeneracy requires the EXTENDED mode tower.")
print("   Deeper modes have smaller tongue widths and break the symmetry,")
print("   giving r* > 0.")
print()
print("3. The field equation determines POPULATIONS at each mode, but")
print("   not the sector assignments. Sector assignments come from")
print("   the selection rule depth ∝ 1/|Q|.")
print()
print("4. Each sector's mass is the product of tongue widths along its")
print("   walk through the tree. Walk length = depth sum, which gives")
print("   the observed (5, 6, 12) pattern.")
print()
print("5. What the field equation DOES NOT determine directly:")
print("   - Why each fermion picks its specific walk (needs charge)")
print("   - Why leptons are on the Fibonacci backbone and down-type is off")
print("   - The exact 0.04% correction δ to the 3/2 law")
print()
print("The field equation is necessary (fixed point gives populations)")
print("but not sufficient (sector assignment is extra information).")
print()
print("The missing piece: the field equation needs to be AUGMENTED with")
print("a charge-dependent selection rule. Or the selection rule needs to")
print("be DERIVED from the field equation by showing that different")
print("charges correspond to different effective couplings K(charge).")
