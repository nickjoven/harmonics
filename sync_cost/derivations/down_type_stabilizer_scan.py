"""
down_type_stabilizer_scan.py

Route 1 from `down_type_double_cover_phase_b.md`:
act the 6 elements of Z_6 = Z_2 x Z_3 on the four XOR modes
{A, B, C, D} from `gap3_principal_bundle.py` and tabulate
stabilizers.

Phase B halts on the Attempt 5 claim:
    |stab_{Z_6}(lepton orbit)| / |stab_{Z_6}(down-type orbit)| = 6 / 1

This script tests whether any natural action of Z_6 on the base
modes or on sector walks produces that ratio. If one does, Route 1
closes; if none does, the halt is deeper than a missing theorem.
"""

from fractions import Fraction
from itertools import product


# ============================================================
# 1. The setup (from gap3_principal_bundle.py)
# ============================================================

MODES = {
    'A': (Fraction(1, 3), Fraction(1, 2)),   # denoms (3, 2)
    'B': (Fraction(1, 2), Fraction(1, 3)),   # denoms (2, 3)
    'C': (Fraction(1, 2), Fraction(2, 3)),   # denoms (2, 3)
    'D': (Fraction(2, 3), Fraction(1, 2)),   # denoms (3, 2)
}

Z6 = [(a, b) for a in range(2) for b in range(3)]

def mul(g1, g2):
    return ((g1[0] + g2[0]) % 2, (g1[1] + g2[1]) % 3)

def order(g):
    e = (0, 0)
    if g == e:
        return 1
    h = g
    k = 1
    while h != e:
        h = mul(h, g)
        k += 1
    return k


def subgroup_generated(g):
    e = (0, 0)
    if g == e:
        return frozenset({e})
    elems = {e}
    h = g
    while h != e:
        elems.add(h)
        h = mul(h, g)
    return frozenset(elems)


# The three sector base pairs (from item12_cross_sector_ratios.md)
SECTORS = {
    'lepton':   (Fraction(3, 2), Fraction(5, 3)),   # denoms (2, 3), parity -1
    'up-type':  (Fraction(8, 5), Fraction(3, 2)),   # denoms (5, 2), parity -1
    'down-type': (Fraction(5, 4), Fraction(9, 8)),  # denoms (4, 8), parity +1
}


def klein_parity(pair):
    q1 = pair[0].denominator
    q2 = pair[1].denominator
    odd = sum(1 for q in (q1, q2) if q % 2 == 1)
    return (-1) ** odd


# ============================================================
# 2. Candidate action 1: Z_6 on fiber labels (trivial on base)
# ============================================================

def stabilizer_fiber_action(pair):
    """
    Z_6 acts on fiber labels (k_1 mod 2, k_2 mod 3) by translation.
    For any base mode, the stabilizer is the elements that fix the
    fiber-label (q_a mod 2, q_b mod 3).

    Translation action on an abelian group is free, so stabilizer
    is always trivial.
    """
    q1, q2 = pair[0].denominator, pair[1].denominator
    label = (q1 % 2, q2 % 3)
    # translation: stab = elements with (k_1, k_2) + label = label mod (2,3)
    stab = [(k1, k2) for (k1, k2) in Z6
            if ((k1 + label[0]) % 2, (k2 + label[1]) % 3) == label]
    return stab, label


# ============================================================
# 3. Candidate action 2: Z_6 on (q_a mod 2, q_b mod 3) by negation
# ============================================================

def stabilizer_negation_action(pair):
    """
    Action: (k_1, k_2) . (a, b) = (k_1 + a mod 2, k_2 - b mod 3)
    mimicking the deck-action on fiber labels from Phase A.
    Stabilizer = elements fixing (q_a mod 2, q_b mod 3).
    """
    q1, q2 = pair[0].denominator, pair[1].denominator
    label = (q1 % 2, q2 % 3)
    stab = [(k1, k2) for (k1, k2) in Z6
            if ((k1 + label[0]) % 2, (-k2 + label[1]) % 3) == label]
    return stab, label


# ============================================================
# 4. Candidate action 3: Z_6 via walk holonomy (stern-brocot)
# ============================================================

def holonomy_transition(pair_a, pair_b):
    """
    Holonomy of transition from mode with denominators (q_1, q_2)
    to mode with (q_1', q_2'), as in gap3_principal_bundle.py line 281:
        h = ((q_1' - q_1) mod 2, (q_2' - q_2) mod 3)
    """
    q1a, q2a = pair_a[0].denominator, pair_a[1].denominator
    q1b, q2b = pair_b[0].denominator, pair_b[1].denominator
    return ((q1b - q1a) % 2, (q2b - q2a) % 3)


def walk_holonomy_from_reference(pair, reference):
    """Total Z_6 holonomy of the trivial walk reference -> pair."""
    return holonomy_transition(reference, pair)


# ============================================================
# 5. Candidate action 4: Z_6 conjugation / permutation on {A,B,C,D}
# ============================================================

def permutation_action():
    """
    Look for subgroups of the symmetric group on {A,B,C,D} that
    are isomorphic to Z_6. Z_6 is cyclic of order 6; it embeds in
    S_4 only if S_4 has an element of order 6, which it does not
    (max order in S_4 is 4). So no Z_6-action on {A,B,C,D} exists
    via permutations of base modes.
    """
    from math import factorial
    # S_4 has 24 elements, cycle types:
    #   (1,1,1,1): 1 element, order 1
    #   (2,1,1): 6 elements, order 2
    #   (2,2): 3 elements, order 2
    #   (3,1): 8 elements, order 3
    #   (4): 6 elements, order 4
    # No order-6 elements, so S_4 has no cyclic subgroup of order 6.
    return None


# ============================================================
# 6. Run and tabulate
# ============================================================

def main():
    print("=" * 70)
    print("  DOWN-TYPE STABILIZER SCAN (Route 1 from Phase B)")
    print("=" * 70)
    print()

    # Element orders in Z_6
    print("Element orders in Z_6:")
    for g in Z6:
        print(f"  {g}  order {order(g)}  generates {sorted(subgroup_generated(g))}")
    print()

    print("Sectors:")
    for name, pair in SECTORS.items():
        q1, q2 = pair[0].denominator, pair[1].denominator
        par = klein_parity(pair)
        print(f"  {name:<10} ({pair[0]}, {pair[1]})   denoms ({q1}, {q2})   "
              f"Klein parity {par:+d}")
    print()

    # Action 1: fiber translation (free)
    print("-" * 70)
    print("  Candidate 1: Z_6 acts on fiber labels by translation")
    print("  (the principal-bundle action from gap3_principal_bundle.py)")
    print("-" * 70)
    for name, pair in SECTORS.items():
        stab, label = stabilizer_fiber_action(pair)
        print(f"  {name:<10} fiber label {label}   "
              f"stabilizer size {len(stab)}  elements {stab}")
    print()
    print("  Result: all stabilizers trivial (action is free).")
    print("  Ratio |stab(lep)| / |stab(dn)| = 1 / 1 = 1.")
    print("  Does NOT produce 6.")
    print()

    # Action 2: with negation in Z_3 (deck-like)
    print("-" * 70)
    print("  Candidate 2: Z_6 acts with negation in Z_3")
    print("  (x -> x, y -> -y mimics the orientable-lift deck action)")
    print("-" * 70)
    for name, pair in SECTORS.items():
        stab, label = stabilizer_negation_action(pair)
        print(f"  {name:<10} label {label}   "
              f"stab size {len(stab)}  elements {stab}")
    print()
    lepton_stab, _ = stabilizer_negation_action(SECTORS['lepton'])
    downtype_stab, _ = stabilizer_negation_action(SECTORS['down-type'])
    ratio = len(lepton_stab) / len(downtype_stab)
    print(f"  Ratio |stab(lep)| / |stab(dn)| = "
          f"{len(lepton_stab)} / {len(downtype_stab)} = {ratio}")
    print()

    # Action 3: walk holonomies from each reference mode
    print("-" * 70)
    print("  Candidate 3: walk holonomy subgroup")
    print("  For each sector base pair, compute its Z_6 holonomy from")
    print("  each of the four reference modes A,B,C,D and report the")
    print("  order of the cyclic subgroup generated.")
    print("-" * 70)
    print(f"  {'sector':<10} {'reference':>10} {'holonomy':>12} "
          f"{'subgroup size':>14}")
    for name, pair in SECTORS.items():
        for ref_label, ref in MODES.items():
            h = walk_holonomy_from_reference(pair, ref)
            sg_size = order(h)
            print(f"  {name:<10} {ref_label:>10} {str(h):>12} {sg_size:>14}")
        print()
    print("  Observation: the cyclic subgroup generated by the walk")
    print("  holonomy depends strongly on the choice of reference.")
    print("  No single reference yields subgroup-size 6 for leptons and")
    print("  1 for down-type.  The reference-free structural reading")
    print("  would need an intrinsic anchor, not present in this data.")
    print()

    # Action 4: permutation on base
    print("-" * 70)
    print("  Candidate 4: Z_6 as a permutation of {A, B, C, D}")
    print("-" * 70)
    print("  The symmetric group S_4 has no element of order 6.")
    print("  The maximum element order in S_4 is 4 (a 4-cycle).")
    print("  Therefore Z_6 does NOT embed in Sym(A,B,C,D) as a cyclic")
    print("  subgroup.  There is no Z_6-action on the base by")
    print("  permutations of the four modes.")
    print()

    # Count of XOR-admissible modes and the V_4 symmetry
    print("-" * 70)
    print("  Base symmetry actually present: V_4 = Z_2 x Z_2")
    print("-" * 70)
    print("  Swap slots: A=(1/3,1/2) <-> B=(1/2,1/3), D=(2/3,1/2) <-> C=(1/2,2/3)")
    print("  Conjugate (p/q -> (q-p)/q) in both slots: A <-> D, B <-> C")
    print("  Generate V_4 = {e, swap, conjugate, swap*conjugate}")
    print("  Order 4, not 6.  The base's natural symmetry is NOT Z_6.")
    print()

    print("=" * 70)
    print("  VERDICT: Route 1 as proposed in Phase B does not close.")
    print("=" * 70)
    print()
    print("""\
  Phase B's Attempt 5 hypothesized that leptons have Z_6 stabilizer
  and down-type has trivial stabilizer, producing the 6:1 ratio.
  This scan tests four candidate actions:

    1. Fiber translation      -- free, all stabs trivial   ratio = 1
    2. Deck-like action       -- see output                ratio != 6
    3. Walk holonomy subgroup -- reference-dependent       no anchor
    4. Base permutation       -- impossible (|S_4| bars order 6)

  None of the four candidate Z_6-actions produces the required 6:1
  stabilizer ratio for the lepton / down-type split.  The base's
  actual symmetry group is V_4 = Z_2 x Z_2, not Z_6.

  Consequence for Phase B:
  - Attempt 5 is not salvageable by a natural Z_6 stabilizer
    computation on the four base modes.
  - The target factor q_2 * q_3 = 6 is NOT |Z_6| interpreted as
    a stabilizer count.  The |Z_6| reading from the hierarchy
    coefficient `R = 6 * 13^54` is therefore a different
    structural appearance of the integer 6, not the same one.
  - The Phase B halt is deeper than "missing representation-
    assignment theorem."  The factor 6 does not come from any
    Z_6 action on the base modes; it must come from a COUNT
    attached to the walk dynamics (e.g. the Stern-Brocot walk
    length, or the orbit enumeration on the universal cover R^2
    of K^2), not from the gauge-bundle structure group.

  Corrected route forward:
    - Look for an object of cardinality 6 that is naturally
      attached to down-type walks and has cardinality 1 for
      lepton walks.  Candidates: the number of Farey steps in
      the Stern-Brocot walk to reach (5/4, 9/8) from a canonical
      anchor; the genus or Euler characteristic difference between
      K^2 and T^2; the number of homotopy classes of closed loops
      on T^2 modulo orientation.
    - The Z_2 x Z_3 = Z_6 of the gauge bundle is NOT the source
      of the 6.  Phase A section 6's suggestion that down-type
      inherits from the hierarchy coefficient is incorrect.
""")


if __name__ == "__main__":
    main()
