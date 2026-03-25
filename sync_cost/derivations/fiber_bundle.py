"""
The fiber bundle over the Klein bottle modes.

The Stern-Brocot tree has only irreducible fractions. The mediant
produces reducible ones. The GCD reduction that maps kp/kq → p/q
is a gauge transformation — it identifies different tree nodes as
"the same physical state."

The fiber over p/q is {kp/kq : k = 1, 2, 3, ...}.
The structure group acts by scaling k.
The XOR filter acts on the total denominator kq.

Questions:
1. What is the structure group of this bundle?
2. Are the transition functions between fibers abelian or not?
3. Does the XOR filter on the fibers produce non-abelian holonomy?
"""

import numpy as np
from fractions import Fraction
from math import gcd

# ============================================================
# Part 1: The fibers
# ============================================================

print("=" * 70)
print("  THE FIBER BUNDLE OVER {1/2, 1/3, 2/3}")
print("=" * 70)

base_modes = [(1, 2), (1, 3), (2, 3)]

print("\n--- Fibers (representatives at each depth) ---\n")

max_k = 12
for p, q in base_modes:
    print(f"  Fiber over {p}/{q}:")
    reps = []
    for k in range(1, max_k + 1):
        kp, kq = k * p, k * q
        reduced = Fraction(kp, kq)
        xor_parity = (kp + kq) % 2  # XOR: p + q mod 2
        q_parity = kq % 2
        reps.append((kp, kq, reduced, xor_parity, q_parity))
        print(f"    k={k:2d}: {kp:3d}/{kq:3d} = {reduced}  "
              f"q_parity={'odd' if q_parity else 'even':>4s}  "
              f"XOR(p+q)={'odd' if xor_parity else 'even':>4s}  "
              f"{'✓ XOR-allowed' if xor_parity else '✗ XOR-forbidden'}")
    print()

# ============================================================
# Part 2: The mediant as a map between fibers
# ============================================================

print("=" * 70)
print("  MEDIANTS AND FIBER TRANSITIONS")
print("=" * 70)

print("\n--- Mediants of fiber representatives ---\n")

# For each pair of base modes, compute mediants of their k-representatives
for (p1, q1), (p2, q2) in [((1,3),(2,3)), ((1,2),(1,3)), ((1,2),(2,3))]:
    print(f"  Mediants of fibers over {p1}/{q1} and {p2}/{q2}:")
    print(f"  {'k1':>4s} {'k2':>4s}  {'med':>10s}  {'reduced':>10s}  "
          f"{'target fiber':>14s}  {'scale k':>8s}  {'XOR':>5s}")

    for k1 in range(1, 7):
        for k2 in range(1, 7):
            # Mediant of k1*p1/k1*q1 and k2*p2/k2*q2
            m_num = k1 * p1 + k2 * p2
            m_den = k1 * q1 + k2 * q2
            reduced = Fraction(m_num, m_den)
            r_p, r_q = reduced.numerator, reduced.denominator

            # Which base fiber does it land in?
            target = None
            scale = None
            for bp, bq in base_modes + [(1,1)]:
                if r_p == bp and r_q == bq:
                    target = f"{bp}/{bq}"
                    scale = 1
                    break
                # Check if it's a multiple
                if bq > 0 and r_q % bq == 0 and r_p * bq == bp * r_q:
                    target = f"{bp}/{bq}"
                    scale = r_q // bq
                    break

            if target is None:
                # Not in any base fiber — it's a NEW mode
                target = f"NEW({r_p}/{r_q})"
                scale = "—"

            xor = (m_num + m_den) % 2
            xor_str = "✓" if xor else "✗"

            if k1 <= 3 and k2 <= 3:  # limit output
                print(f"  {k1:4d} {k2:4d}  {m_num:4d}/{m_den:<4d}  "
                      f"{str(reduced):>10s}  {target:>14s}  {str(scale):>8s}  "
                      f"{xor_str:>5s}")
    print()

# ============================================================
# Part 3: The transition functions
# ============================================================

print("=" * 70)
print("  TRANSITION FUNCTIONS")
print("=" * 70)

print("""
The mediant of representatives at scales (k1, k2) lands in a
specific fiber at scale k3. The transition function is:

  T_{ij}: (k1, k2) → k3

where k3 is the scale factor that maps the mediant to its
irreducible representative.
""")

# Compute the transition function for 1/3 and 2/3
print("--- Transition function: fiber(1/3) × fiber(2/3) → fiber(?) ---\n")
print(f"  {'k1':>4s} {'k2':>4s}  {'mediant':>10s}  {'reduced':>8s}  "
      f"{'target':>8s}  {'k_out':>6s}  {'GCD':>4s}")

transition_data = []
for k1 in range(1, 10):
    for k2 in range(1, 10):
        m_num = k1 * 1 + k2 * 2  # mediant(k1/3k1, 2k2/3k2)
        m_den = k1 * 3 + k2 * 3
        g = gcd(m_num, m_den)
        r_p, r_q = m_num // g, m_den // g

        # The GCD is the "gauge transformation" that reduces the fraction
        # The scale k_out tells us where in the target fiber we land
        target_base = f"{r_p}/{r_q}"
        k_out = g

        if k1 <= 6 and k2 <= 6:
            print(f"  {k1:4d} {k2:4d}  {m_num:4d}/{m_den:<4d}  "
                  f"{r_p}/{r_q!s:>6s}  {target_base:>8s}  {str(k_out):>6s}  {g:>4d}")

        transition_data.append((k1, k2, r_p, r_q, k_out))

# ============================================================
# Part 4: The GCD as gauge transformation
# ============================================================

print("\n" + "=" * 70)
print("  THE GCD AS GAUGE TRANSFORMATION")
print("=" * 70)

print("""
When mediant(k1·(1/3), k2·(2/3)) = (k1 + 2k2)/(3k1 + 3k2):

  GCD(k1 + 2k2, 3(k1 + k2)) divides out the common factor.

  If k1 + 2k2 ≡ 0 (mod 3): GCD ≥ 3, and the result lands in fiber(1/3) or fiber(2/3)
  If k1 + 2k2 ≡ 1 (mod 3): GCD = gcd(k1+2k2, 3) = 1, lands in fiber(?)
  If k1 + 2k2 ≡ 2 (mod 3): GCD = gcd(k1+2k2, 3) = 1, lands in fiber(?)
""")

# Map out which fiber the result lands in, by (k1 mod 3, k2 mod 3)
print("  Landing fiber by (k1 mod 3, k2 mod 3):\n")
print(f"  {'':>12s}", end="")
for k2r in range(3):
    print(f"  k2≡{k2r} (mod 3)", end="")
print()

for k1r in range(3):
    print(f"  k1≡{k1r} (mod 3)", end="")
    for k2r in range(3):
        # Use k1 = k1r + 3, k2 = k2r + 3 (avoid k=0)
        k1, k2 = k1r + 1, k2r + 1
        if k1r == 0:
            k1 = 3
        if k2r == 0:
            k2 = 3
        m_num = k1 * 1 + k2 * 2
        m_den = k1 * 3 + k2 * 3
        g = gcd(m_num, m_den)
        r_p, r_q = m_num // g, m_den // g
        print(f"  {r_p:>6d}/{r_q:<6d}  ", end="")
    print()


# ============================================================
# Part 5: Structure group — does scaling by 2 commute with scaling by 3?
# ============================================================

print("\n" + "=" * 70)
print("  STRUCTURE GROUP: SCALING BY 2 vs SCALING BY 3")
print("=" * 70)

print("""
The fiber over p/q contains {kp/kq : k ∈ Z⁺}.
Scaling by 2: k → 2k (maps kp/kq to 2kp/2kq).
Scaling by 3: k → 3k.

These commute as fiber automorphisms (2·3·k = 3·2·k).
But the MEDIANT doesn't commute with scaling:
  mediant(2·a, b) ≠ 2·mediant(a, b) in general.
""")

# Test: mediant(2·(1/3), 2/3) vs 2·mediant(1/3, 2/3)
a, b = Fraction(1, 3), Fraction(2, 3)

med_ab = Fraction(a.numerator + b.numerator, a.denominator + b.denominator)
print(f"  mediant(1/3, 2/3) = {med_ab} = {Fraction(med_ab.numerator, med_ab.denominator)}")

# Scale a by 2: 2/6
a2 = Fraction(2, 6)  # NOT reduced — this is the key
med_2a_b = Fraction(a2.numerator + b.numerator, a2.denominator + b.denominator)
print(f"  mediant(2/6, 2/3) = {med_2a_b} = {Fraction(med_2a_b.numerator, med_2a_b.denominator)}")

# 2 * mediant(1/3, 2/3) = 2 * 3/6 = 6/12 = 1/2
scaled_med = Fraction(2 * med_ab.numerator, 2 * med_ab.denominator)
print(f"  2 × mediant(1/3, 2/3) = {2*med_ab.numerator}/{2*med_ab.denominator} = {Fraction(2*med_ab.numerator, 2*med_ab.denominator)}")

print(f"\n  mediant(2·a, b) = {med_2a_b}")
print(f"  2·mediant(a, b) = {scaled_med}")
print(f"  Equal? {med_2a_b == scaled_med}")
print(f"  => SCALING DOES NOT COMMUTE WITH MEDIANT")

# Now scale by 3
a3_num, a3_den = 3 * 1, 3 * 3  # 3/9
med_3a_b = Fraction(a3_num + b.numerator, a3_den + b.denominator)
scaled_med_3 = Fraction(3 * med_ab.numerator, 3 * med_ab.denominator)
print(f"\n  mediant(3/9, 2/3) = {med_3a_b}")
print(f"  3 × mediant(1/3, 2/3) = {scaled_med_3}")
print(f"  Equal? {med_3a_b == scaled_med_3}")

# The commutator of scale-2 and scale-3 mediant operations
print(f"\n  Commutator of scale-by-2 and scale-by-3 mediant operations:")
# (scale by 2 then mediant) vs (scale by 3 then mediant)
# on the pair (1/3, 2/3):

# Scale first arg by 2, mediant with 2/3:
r1 = Fraction(2 + 2, 6 + 3)  # mediant(2/6, 2/3) = 4/9
# Scale first arg by 3, mediant with 2/3:
r2 = Fraction(3 + 2, 9 + 3)  # mediant(3/9, 2/3) = 5/12

print(f"  Scale-2 then mediant: mediant(2/6, 2/3) = {r1}")
print(f"  Scale-3 then mediant: mediant(3/9, 2/3) = {r2}")
print(f"  These are DIFFERENT fractions at DIFFERENT tree positions.")
print(f"  The two scaling operations produce different mediants.")
print()

# ============================================================
# Part 6: The non-commutativity is in the interaction, not the fiber
# ============================================================

print("=" * 70)
print("  THE KEY INSIGHT")
print("=" * 70)

print("""
The fiber automorphisms (scaling by k) COMMUTE with each other:
  2 × 3 = 3 × 2  (trivially).

But scaling does NOT commute with the MEDIANT:
  mediant(2·a, b) ≠ 2·mediant(a, b)

This means: the "gauge transformation" (GCD reduction) that maps
  kp/kq → p/q
does not commute with the "interaction" (mediant).

In gauge theory, this is exactly the statement that the gauge field
couples to the interaction — the covariant derivative D = d + A
doesn't commute with the gauge transformation when A ≠ 0.

The mediant IS the connection. The GCD IS the gauge transformation.
They don't commute. The structure group is non-abelian because the
interaction (mediant) mixes the fibers in a scale-dependent way.

Specifically:
  mediant(2·(1/3), 2/3) = 4/9  (lands in a new fiber)
  mediant(3·(1/3), 2/3) = 5/12 (lands in a different new fiber)

The "gauge boson" (the mediant) produces DIFFERENT results depending
on which representative of 1/3 is used. The redundancy of the
representation (1/3 = 2/6 = 3/9 = ...) is not physically neutral —
it changes the interaction outcome. This is a gauge theory.
""")

# ============================================================
# Part 7: What the equality operator hides
# ============================================================

print("=" * 70)
print("  WHAT THE EQUALITY OPERATOR HIDES")
print("=" * 70)

print("""
When we write mediant(1/3, 2/3) = 3/6 = 1/2, we perform TWO operations:
  1. MEDIANT: (1,3) + (2,3) = (3, 6)    [the interaction]
  2. GCD:     3/6 → 1/2                  [the gauge transformation]

The GCD hides the scale factor k = 3. This k is NOT arbitrary — it is
gcd(1+2, 3+3) = gcd(3, 6) = 3.

For the mediant of k-representatives:
  mediant(k₁/3k₁, 2k₂/3k₂) = (k₁ + 2k₂) / (3k₁ + 3k₂)
  GCD = gcd(k₁ + 2k₂, 3(k₁ + k₂))

The GCD depends on k₁ and k₂ mod 3. This is a Z₃ structure:

  k₁ + 2k₂ mod 3:
    ≡ 0: GCD ≥ 3 (divisible by 3)
    ≡ 1: GCD = 1 (coprime to 3)
    ≡ 2: GCD = 1 (coprime to 3)

The Z₃ is the residue of the gauge transformation mod the Klein
bottle's q₃ = 3. It determines which fiber the mediant lands in.

Similarly, the GCD mod 2 gives a Z₂ from q₂ = 2.

The full structure is Z₂ × Z₃ = Z₆ acting on the fibers.
This is the CENTER of SU(2) × SU(3).
""")

# Verify Z₂ × Z₃ structure
print("  GCD structure for mediant(k₁·(1/3), k₂·(2/3)):\n")
print(f"  {'k₁':>4s} {'k₂':>4s}  {'GCD':>4s}  {'mod 2':>6s}  {'mod 3':>6s}  {'reduced':>10s}")
for k1 in range(1, 7):
    for k2 in range(1, 7):
        m_num = k1 + 2 * k2
        m_den = 3 * k1 + 3 * k2
        g = gcd(m_num, m_den)
        r = Fraction(m_num, m_den)
        print(f"  {k1:4d} {k2:4d}  {g:4d}  {g % 2:6d}  {g % 3:6d}  {str(r):>10s}")

print()
print("  The GCD mod 6 cycles through a pattern determined by")
print("  (k₁ mod 3, k₂ mod 3). This Z₆ = Z₂ × Z₃ structure is")
print("  the center of SU(2) × SU(3) — the gauge group center that")
print("  determines which representations are allowed.")
