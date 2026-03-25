"""
D21-B + D30 synthesis: Tongue overlap as interaction vertex.

D21 asked: do Arnold tongue overlaps at denominator classes 2 and 3
reproduce gauge theory vertex structure?

D30 showed: the mediant resolves degeneracy. The mediants of the
Klein bottle modes {(2,3), (3,2)} are the INTERACTION modes — the
channels through which the two denominator classes communicate.

New framing: the tongue overlap integral between two parent modes
IS the coupling constant of the mediant that resolves them. The
"vertex" isn't a perturbative diagram — it's a mediant.

Tests:
1. Compute tongue overlap for all Klein bottle mode pairs
2. Check whether overlap ratios match the structure constant ratios
   of SU(2) and SU(3)
3. Check whether the mediant population ratios from mediant_test.py
   encode vertex weights
"""

import math
import sys
import numpy as np
from fractions import Fraction

sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[2]))

# ============================================================
# Tongue overlap integral
# ============================================================

def tongue_width_circle_map(p, q, K):
    """Arnold tongue width at p/q for coupling K."""
    if q == 0:
        return 0.0
    return (K / 2) ** q


def tongue_center(p, q):
    """Center of the p/q tongue in Omega space."""
    return p / q


def tongue_overlap(p1, q1, p2, q2, K):
    """
    Overlap of tongues p1/q1 and p2/q2 in Omega space.

    Each tongue occupies [center - w/2, center + w/2].
    Overlap = max(0, min(r1, r2) - max(l1, l2)).
    """
    w1 = tongue_width_circle_map(p1, q1, K)
    w2 = tongue_width_circle_map(p2, q2, K)
    c1 = tongue_center(p1, q1)
    c2 = tongue_center(p2, q2)
    l1, r1 = c1 - w1/2, c1 + w1/2
    l2, r2 = c2 - w2/2, c2 + w2/2
    return max(0.0, min(r1, r2) - max(l1, l2))


def three_tongue_overlap(modes, K):
    """
    Three-point overlap: region where all three tongues overlap.
    This is the vertex — the coupling between three modes.
    """
    intervals = []
    for p, q in modes:
        w = tongue_width_circle_map(p, q, K)
        c = tongue_center(p, q)
        intervals.append((c - w/2, c + w/2))

    lo = max(l for l, r in intervals)
    hi = min(r for l, r in intervals)
    return max(0.0, hi - lo)


# ============================================================
# Klein bottle modes and their mediants
# ============================================================

# The 4 surviving Klein bottle modes (winding numbers)
kb_modes = [
    (1, 2),   # 1/2
    (1, 3),   # 1/3
    (2, 3),   # 2/3
]

# Mediants of adjacent pairs
mediants = {
    ((1,3), (1,2)): (2, 5),   # mediant of 1/3 and 1/2
    ((1,2), (2,3)): (3, 5),   # mediant of 1/2 and 2/3
    ((1,3), (2,3)): (3, 6),   # but 3/6 = 1/2, which is already a mode!
}

print("=" * 70)
print("  TONGUE OVERLAP STRUCTURE: Klein bottle modes")
print("=" * 70)

# ============================================================
# Test 1: Pairwise overlaps at various K
# ============================================================

print("\n--- Pairwise tongue overlaps ---\n")
print(f"{'K':>6}  {'1/2 ∩ 1/3':>12}  {'1/2 ∩ 2/3':>12}  {'1/3 ∩ 2/3':>12}  "
      f"{'ratio 12/13':>12}")

for K in [0.5, 0.7, 0.8, 0.9, 0.95, 0.99]:
    o_12_13 = tongue_overlap(1, 2, 1, 3, K)
    o_12_23 = tongue_overlap(1, 2, 2, 3, K)
    o_13_23 = tongue_overlap(1, 3, 2, 3, K)
    ratio = o_12_13 / o_12_23 if o_12_23 > 0 else float('inf')
    print(f"{K:6.2f}  {o_12_13:12.6f}  {o_12_23:12.6f}  {o_13_23:12.6f}  "
          f"{ratio:12.6f}")


# ============================================================
# Test 2: Three-point overlaps (vertices)
# ============================================================

print("\n--- Three-point tongue overlaps (vertices) ---\n")

# All triples from {1/2, 1/3, 2/3}
triples = [
    [(1,2), (1,3), (2,3)],
]

# Extended: include mediant modes
triples_ext = [
    [(1,2), (1,3), (2,5)],   # parents + mediant
    [(1,2), (2,3), (3,5)],   # parents + mediant
    [(1,3), (2,3), (1,2)],   # mediant(1/3,2/3)=1/2 already a mode
]

print(f"{'Modes':>20}  ", end="")
for K in [0.7, 0.8, 0.9, 0.95]:
    print(f"{'K='+str(K):>10}", end="")
print()

for triple in triples + triples_ext:
    label = "+".join(f"{p}/{q}" for p, q in triple)
    print(f"{label:>20}  ", end="")
    for K in [0.7, 0.8, 0.9, 0.95]:
        v = three_tongue_overlap(triple, K)
        print(f"{v:10.6f}", end="")
    print()


# ============================================================
# Test 3: The mediant IS the vertex
# ============================================================

print("\n--- The mediant as vertex ---\n")
print("When two parents have overlapping tongues, their mediant is")
print("the mode that lives in the overlap region.\n")

for K in [0.8, 0.9, 0.95]:
    print(f"K = {K}:")
    for (p1, q1), (p2, q2) in [((1,3), (1,2)), ((1,2), (2,3))]:
        pm, qm = p1+p2, q1+q2
        overlap = tongue_overlap(p1, q1, p2, q2, K)
        med_width = tongue_width_circle_map(pm, qm, K)
        med_center = tongue_center(pm, qm)

        # Is the mediant tongue contained in the overlap?
        p1_c, p2_c = tongue_center(p1, q1), tongue_center(p2, q2)
        w1, w2 = tongue_width_circle_map(p1, q1, K), tongue_width_circle_map(p2, q2, K)

        print(f"  {p1}/{q1} ∩ {p2}/{q2}: overlap = {overlap:.6f}, "
              f"mediant {pm}/{qm} width = {med_width:.6f}, "
              f"ratio = {med_width/overlap:.3f}" if overlap > 0 else
              f"  {p1}/{q1} ∩ {p2}/{q2}: no overlap, "
              f"mediant {pm}/{qm} width = {med_width:.6f}")
    print()


# ============================================================
# Test 4: Structure constant analogy
# ============================================================

print("\n--- Structure constant test ---\n")
print("SU(2) structure constants: f_ijk = epsilon_ijk (fully antisymmetric)")
print("SU(3) structure constants: f_123 = 1, f_458 = sqrt(3)/2, etc.")
print()

# In the Klein bottle, the "structure constants" should be the
# tongue overlap ratios. For SU(2), the vertex is symmetric under
# permutation of the 3 generators. For SU(3), it's not.

K = 0.9
print(f"At K = {K}:")

# The Klein bottle has two denominator classes: q=2 and q=3.
# Within q=2: the 1/2 mode (one mode)
# Within q=3: the 1/3 and 2/3 modes (two modes)
#
# The "SU(2)" should act on the q=3 doublet {1/3, 2/3}
# The "SU(3)" should act on... what?

# Actually: the 4 Klein bottle modes form two pairs:
#   Pair A: (1/3, 1/2) and (2/3, 1/2) — share q₂=2 in second slot
#   Pair B: (1/2, 1/3) and (1/2, 2/3) — share q₁=2 in first slot
#
# Within each pair, the two modes differ by 1/3 ↔ 2/3 in the q=3 slot.
# This is a Z₂ (swap). The mediant of 1/3 and 2/3 is 3/6 = 1/2,
# which is the q=2 mode. So:
#
# mediant(1/3, 2/3) = 1/2

print("mediant(1/3, 2/3) = (1+2)/(3+3) = 3/6 = 1/2")
print("The mediant of the two q=3 modes IS the q=2 mode.")
print()
print("This is the VERTEX: the q=2 mode (1/2) is the mediator")
print("between the two q=3 modes (1/3 and 2/3).")
print()
print("In gauge language: 1/2 is the gauge boson, 1/3 and 2/3")
print("are the matter fields. The coupling is the tongue overlap.")
print()

# The overlap between 1/3 and 2/3 at their mediant 1/2
o_13_23 = tongue_overlap(1, 3, 2, 3, K)
w_12 = tongue_width_circle_map(1, 2, K)
print(f"Overlap(1/3, 2/3) = {o_13_23:.6f}")
print(f"Width(1/2)         = {w_12:.6f}")
print(f"Ratio              = {o_13_23 / w_12:.6f}")
print()

# The reciprocal: mediant of the two q=2 modes (in 2D)
# In the 2D Klein bottle, the modes are pairs.
# The q₁=2 pair is {(1/2, 1/3), (1/2, 2/3)}
# Their "mediant" in the second slot: mediant(1/3, 2/3) = 1/2
# So the mediant pair is (1/2, 1/2) — but this violates the XOR filter!
# q₁=2 (even), q₂=2 (even) → p₁+p₂ = even → violates p₁+p₂ ≡ 1 (mod 2)

print("The mediant of the q₁=2 pair in the second slot:")
print("  mediant((1/2,1/3), (1/2,2/3)) in slot 2 = (1/2, 1/2)")
print("  But (1/2, 1/2) has q₁=2, q₂=2 → EVEN+EVEN → XOR FORBIDS it!")
print()
print("The XOR filter prevents the q=2 sector from self-mediating.")
print("Only the q=3 sector can mediate (via 1/2 = mediant(1/3, 2/3)).")
print()
print("This is ASYMMETRIC: q=3 modes interact through q=2,")
print("but q=2 modes CANNOT interact through q=2.")
print("The interaction is one-directional in denominator space.")
print()
print("In gauge language: the gauge boson (q=2) couples to matter")
print("(q=3) but does not self-couple. This is the structure of")
print("an ABELIAN gauge theory (like U(1)), not non-abelian (like SU(3)).")
print()
print("For SU(3) (non-abelian, self-coupling gauge bosons), we would")
print("need the mediator to mediate ITSELF — which the XOR filter forbids.")
print()

# But wait: in the full 2D Klein bottle, we have PAIRS.
# The (q₁=3, q₂=2) pair is {(1/3, 1/2), (2/3, 1/2)}.
# Their mediant in slot 1: mediant(1/3, 2/3) = 1/2
# → (1/2, 1/2): forbidden by XOR
#
# The (q₁=2, q₂=3) pair is {(1/2, 1/3), (1/2, 2/3)}.
# Same story.
#
# Cross-sector: (1/3, 1/2) and (1/2, 1/3)
# Mediant in both slots: mediant(1/3, 1/2) = 2/5, mediant(1/2, 1/3) = 2/5
# → (2/5, 2/5): q₁=5 (odd), q₂=5 (odd) → EVEN sum → XOR FORBIDS

print("Cross-sector mediant:")
print("  mediant((1/3,1/2), (1/2,1/3)) = (2/5, 2/5)")
print("  q₁=5 (odd), q₂=5 (odd) → p₁+p₂ = 4 → EVEN → XOR FORBIDS")
print()
print("ALL self-mediations of the 4-mode system are XOR-forbidden.")
print("The only allowed mediations are between the two sectors,")
print("through modes that are already present (1/2).")
print()
print("=" * 70)
print("  CONCLUSION")
print("=" * 70)
print()
print("The XOR filter creates an ASYMMETRIC interaction structure:")
print("  - q=3 pairs interact through q=2 (their mediant is 1/2)")
print("  - q=2 pairs CANNOT self-interact (their mediant is forbidden)")
print("  - Cross-sector pairs CANNOT interact (their mediant is forbidden)")
print()
print("This is NOT SU(3) × SU(2) × U(1). It is a simpler structure:")
print("  - One abelian mediator (q=2 = 1/2)")
print("  - Two matter modes (q=3 = 1/3, 2/3)")
print("  - No self-coupling of the mediator")
print()
print("The XOR filter is too restrictive for non-abelian gauge theory.")
print("Non-abelian requires gauge bosons that self-couple — mediants of")
print("mediants — which the XOR parity forbids at every step.")
