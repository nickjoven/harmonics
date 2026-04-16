"""
klein_topology_phantoms.py

Attempt to derive the three phantom fixed points from
twin_swap_formalization.py -- {13/9, 21/10, -6} -- from Klein
topology / Stern-Brocot primitives rather than as linear-algebra
outputs of the harmonic-range condition.

Results are MIXED -- partial pattern with a cross-link, not a clean
derivation.  Specifically:

  (A) phantom_N = -6 can be written as a weighted arithmetic mean of
      N_lep and N_dn with weight -q_3:

          phantom_N = (-q_3 * N_lep + 1 * N_dn) / (-q_3 + 1)
                    = (-12 + 24) / -2
                    = -6        (CLEAN weight: -q_3)

  (B) phantom_b_2 = 21/10 can be written as a weighted mediant of
      b_2_lep and b_2_dn with weight = phantom_N:

          phantom_b_2 = (phantom_N * 5 + 1 * 9) / (phantom_N * 3 + 1 * 8)
                      = (-30 + 9) / (-18 + 8)
                      = -21 / -10
                      = 21/10   (CROSS-LINK: weight is phantom_N)

      This is a genuine cross-coordinate dependency.  The N phantom
      is derived first, and its value becomes the weight in the b_2
      phantom derivation.

  (C) phantom_b_1 = 13/9 can be written as a SIMPLE mediant of
      up.b_1 and dn.b_1:

          phantom_b_1 = mediant(8/5, 5/4) = (8+5)/(5+4) = 13/9

      but this uses (up, dn) as the base pair rather than (lep, dn),
      so it does NOT fit the same pattern as A and B.  The weighted
      mediant of (lep.b_1, dn.b_1) that gives 13/9 has weight 7, which
      is not obviously framework (7 is not Fibonacci, not q_2, not q_3).

What this establishes:

  - N and b_2 phantoms follow a two-stage hierarchical derivation:
    N first (with weight -q_3), then b_2 (with weight = phantom_N).
    This is clean, interlocking, and uses only framework primitives.

  - b_1's phantom does NOT fit this hierarchy.  It has a separate
    derivation: simple mediant(up.b_1, dn.b_1).  Two different rules
    for three phantoms is not a unified topology.

What this does NOT establish:

  - A SINGLE Klein-topology principle that produces all three phantoms.
  - Why b_1 follows a different rule.
  - A formal derivation from Klein bottle fundamental group or from
    the Stern-Brocot tree's SL(2, Z) action.

Status: partial derivation.  Stronger than 'observational coincidence',
weaker than 'theorem from first principles'.
"""

from __future__ import annotations

import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))

from fractions import Fraction

from framework_constants import Q2, Q3

B1 = {'lep': Fraction(3, 2), 'up': Fraction(8, 5), 'dn': Fraction(5, 4)}
B2 = {'lep': Fraction(5, 3), 'up': Fraction(3, 2), 'dn': Fraction(9, 8)}
N  = {'lep': 4, 'up': 9, 'dn': 24}

PHANTOM_B1 = Fraction(13, 9)
PHANTOM_B2 = Fraction(21, 10)
PHANTOM_N  = -6

def header(text: str) -> None:
    print()
    print("-" * 78)
    print(f"  {text}")
    print("-" * 78)
    print()

def weighted_mediant(a: Fraction, b: Fraction, p, r) -> Fraction:
    """Weighted mediant: (p * a.num + r * b.num) / (p * a.den + r * b.den)"""
    return Fraction(
        p * a.numerator + r * b.numerator,
        p * a.denominator + r * b.denominator,
    )

def weighted_mean(a, b, p, r) -> Fraction:
    """Weighted arithmetic mean: (p*a + r*b)/(p+r)"""
    return Fraction(p * a + r * b, p + r)

# ============================================================================
# (A) phantom_N from weighted mean with weight -q_3
# ============================================================================

def section_N() -> None:
    header("(A) phantom_N from (lep.N, dn.N) weighted mean with weight -q_3")
    print(f"  N_lep = {N['lep']},  N_dn = {N['dn']},  N_up = {N['up']}")
    print(f"  target phantom_N = {PHANTOM_N}")
    print()
    print("  Candidate: weighted mean of (N_lep, N_dn) with some weight p:")
    print("      (p * N_lep + 1 * N_dn) / (p + 1) = phantom_N")
    print()
    print("  Solve: (4p + 24) / (p + 1) = -6")
    print("         4p + 24 = -6p - 6")
    print("         10p = -30")
    print("         p = -3")
    print()
    p = -Q3
    result = weighted_mean(N['lep'], N['dn'], p, 1)
    print(f"  Verify: weighted_mean({N['lep']}, {N['dn']}, p={p}, r=1)")
    print(f"          = ({p} * {N['lep']} + {N['dn']}) / ({p} + 1)")
    print(f"          = {p * N['lep'] + N['dn']} / {p + 1}")
    print(f"          = {result}")
    print(f"  target = {PHANTOM_N}")
    print(f"  match: {result == PHANTOM_N}")
    print()
    print("  Weight p = -q_3 = -3 is a FRAMEWORK PRIMITIVE.")
    print("  phantom_N is the weighted mean of lep and dn cell counts with a")
    print("  weight equal to -q_3.  Physical reading: 'tilt the lep-dn mean")
    print("  by -q_3 and the result is -q_2*q_3, the negative of the prime")
    print("  product.'")
    print()

# ============================================================================
# (B) phantom_b_2 uses phantom_N as weight (cross-link!)
# ============================================================================

def section_b2() -> None:
    header("(B) phantom_b_2 from weighted mediant with weight = phantom_N")
    print(f"  b_2_lep = {B2['lep']},  b_2_dn = {B2['dn']},  b_2_up = {B2['up']}")
    print(f"  target phantom_b_2 = {PHANTOM_B2}")
    print()
    print("  Candidate: weighted mediant of (b_2_lep, b_2_dn) with weight p:")
    print("      (p * b_2_lep_num + r * b_2_dn_num) /")
    print("      (p * b_2_lep_den + r * b_2_dn_den) = phantom_b_2")
    print()
    print("  Solve: (5p + 9r) / (3p + 8r) = 21/10")
    print("         10(5p + 9r) = 21(3p + 8r)")
    print("         50p + 90r = 63p + 168r")
    print("         -13p = 78r")
    print("         p/r = -6")
    print()
    p, r = PHANTOM_N, 1     # use phantom_N as weight!
    result = weighted_mediant(B2['lep'], B2['dn'], p, r)
    print(f"  Verify: weighted_mediant(b_2_lep={B2['lep']}, b_2_dn={B2['dn']}, p={p}, r={r})")
    print(f"          = ({p}*5 + {r}*9) / ({p}*3 + {r}*8)")
    print(f"          = {p*5 + r*9} / {p*3 + r*8}")
    print(f"          = {result}")
    print(f"  target = {PHANTOM_B2}")
    print(f"  match: {result == PHANTOM_B2}")
    print()
    print("  *** CROSS-LINK: the weight used here is exactly phantom_N. ***")
    print()
    print("  This is a HIERARCHICAL derivation:")
    print("    1. Start from sector data (lep, up, dn) with N = (4, 9, 24)")
    print("    2. Compute phantom_N via weight -q_3 on (lep, dn): -> -6")
    print("    3. Use phantom_N as the weight to compute phantom_b_2 via")
    print("       weighted mediant on (lep.b_2, dn.b_2): -> 21/10")
    print()
    print("  The derivation uses only: {q_2, q_3, sector data}.")
    print()

# ============================================================================
# (C) phantom_b_1 breaks the pattern
# ============================================================================

def section_b1() -> None:
    header("(C) phantom_b_1: does NOT follow the same rule")
    print(f"  b_1_lep = {B1['lep']},  b_1_dn = {B1['dn']},  b_1_up = {B1['up']}")
    print(f"  target phantom_b_1 = {PHANTOM_B1}")
    print()
    print("  First try: apply the same weighted-mediant pattern as b_2,")
    print("  using phantom_N as the weight on (lep.b_1, dn.b_1):")
    print()
    p, r = PHANTOM_N, 1
    result = weighted_mediant(B1['lep'], B1['dn'], p, r)
    print(f"    weighted_mediant({B1['lep']}, {B1['dn']}, p={p}, r={r}) = {result}")
    print(f"    target phantom_b_1 = {PHANTOM_B1}")
    print(f"    match: {result == PHANTOM_B1}")
    print()
    print("  NO match for 13/9 -- but the result 13/8 is itself structurally")
    print("  significant: 13/8 = F_7/F_6, the NEXT Fibonacci convergent of")
    print("  phi BEYOND up.b_1 = 8/5 = F_6/F_5.  That is:")
    print()
    print("      up.b_1         = F_6/F_5 = 8/5       (current convergent)")
    print("      weighted mediant (phantom_N) = F_7/F_6 = 13/8   (next!)")
    print()
    print("  So the weighted-mediant rule with weight = phantom_N produces")
    print("  the NEXT Fibonacci convergent of up.b_1 at coordinate b_1.")
    print("  This is different from the Mobius phantom 13/9.  The 13/8 is")
    print("  cleaner structurally (a canonical Fibonacci position) but does")
    print("  NOT form a Mobius involution that fixes up and swaps lep <-> dn.")
    print()
    print("  Side note: the next Fibonacci convergent after up.b_2 = 3/2 =")
    print("  F_4/F_3 is 5/3 = F_5/F_4 = lep.b_2, which is ALREADY in the")
    print("  matter sector.  So for b_2, the 'Fibonacci-next' candidate")
    print("  collapses onto lep (not usable as a phantom).  For b_1 the")
    print("  next convergent 13/8 is NOT in the sector, so it is available.")
    print("  This asymmetry may explain why the two constructions disagree")
    print("  on b_1 but agree on b_2.")
    print()

    print("  Second try: solve for weight p that makes the weighted mediant")
    print("  of (lep.b_1, dn.b_1) equal to 13/9:")
    print()
    print("    (3p + 5r)/(2p + 4r) = 13/9")
    print("    9(3p + 5r) = 13(2p + 4r)")
    print("    27p + 45r = 26p + 52r")
    print("    p = 7r")
    print()
    result = weighted_mediant(B1['lep'], B1['dn'], 7, 1)
    print(f"  Verify with p = 7: {result}")
    print(f"  target = {PHANTOM_B1}")
    print(f"  match: {result == PHANTOM_B1}")
    print()
    print("  Required weight is 7.  What is 7 in the framework?")
    print(f"    7 = 2 + 5 = q_2 + F_5      (natural-ish)")
    print(f"    7 = F_4 + q_2^2 = 3 + 4     (contrived)")
    print(f"    7 = 13 - 6 = |phantom_b_1 num| - |phantom_N|")
    print(f"    7 = 21/3 = phantom_b_2 num / q_3")
    print(f"    7 is NOT F_k for any k       (not Fibonacci)")
    print()
    print("  None of these feel structurally clean.  7 does not naturally")
    print("  arise from the framework alphabet, though it can be forced.")
    print()

    print("  Third try: a DIFFERENT construction -- simple mediant of up and dn:")
    print()
    simple_med = Fraction(
        B1['up'].numerator + B1['dn'].numerator,
        B1['up'].denominator + B1['dn'].denominator,
    )
    print(f"    mediant(b_1_up, b_1_dn) = mediant(8/5, 5/4)")
    print(f"                            = (8+5)/(5+4)")
    print(f"                            = {simple_med}")
    print(f"    target = {PHANTOM_B1}")
    print(f"    match: {simple_med == PHANTOM_B1}")
    print()
    print("  YES -- the simple mediant of up.b_1 and dn.b_1 equals 13/9.")
    print("  But this is a DIFFERENT construction than what worked for N")
    print("  and b_2.  It uses (up, dn) instead of (lep, dn), and takes a")
    print("  simple mediant (weight 1:1) instead of a phantom-valued weight.")
    print()
    print("  Caveat: 8/5 and 5/4 are NOT Farey neighbors in the Stern-Brocot")
    print("  tree (|8*4 - 5*5| = 7 != 1), so mediant(8/5, 5/4) is just")
    print("  arithmetic -- it is NOT the canonical tree operation on")
    print("  neighbors.  This weakens the 'mediant' reading for b_1.")
    print()

# ============================================================================
# (D) Unification attempts
# ============================================================================

def section_unify() -> None:
    header("(D) Attempts at a unified rule")
    print("  We have THREE derivations that don't match each other:")
    print()
    print("    phantom_N   = weighted mean of (lep.N, dn.N) with weight -q_3")
    print("    phantom_b_2 = weighted mediant of (lep.b_2, dn.b_2) with weight")
    print("                  = phantom_N = -q_2*q_3")
    print("    phantom_b_1 = simple mediant of (up.b_1, dn.b_1)")
    print("                = weighted mediant of (lep.b_1, dn.b_1) w/ weight 7")
    print()
    print("  Candidate unifications:")
    print()
    print("  (i)  'All phantoms are weighted means/mediants of (lep, dn).'")
    print("       Weights: -q_3, -q_2*q_3, 7.  First two are clean, third")
    print("       is not.  Rejected as a unified rule.")
    print()
    print("  (ii) 'Each phantom uses the previous as its weight.'")
    print("       N first (weight -q_3), then b_2 (weight phantom_N = -q_2*q_3),")
    print("       then b_1 (weight phantom_b_2 = 21/10)?")
    print()
    # Check (ii)
    p = PHANTOM_B2.numerator
    r = PHANTOM_B2.denominator
    result = weighted_mediant(B1['lep'], B1['dn'], p, r)
    print(f"       Try: weighted_mediant(b_1_lep, b_1_dn, p=21, r=10) = {result}")
    if result == PHANTOM_B1:
        print("       MATCH")
    else:
        print(f"       NO MATCH -- expected {PHANTOM_B1}")
    print()
    print("       The chain doesn't close: using phantom_b_2 = 21/10 as the")
    print("       weight on (lep.b_1, dn.b_1) does not give 13/9.")
    print()
    print("  (iii) 'phantom_b_1 uses (up, dn) because b_1 has the Fibonacci")
    print("        shift up.b_1 = F_6/F_5 (non-consecutive), while b_2 and N")
    print("        use (lep, dn) because those are the reciprocity pair.'")
    print("        This is a speculative distinction -- it explains why b_1")
    print("        is different but does not rigorously derive the choice.")
    print()
    print("  None of these is a clean Klein-topology first principle.  The")
    print("  best we have is PARTIAL structure:")
    print()
    print("    - The N and b_2 phantoms form a clean two-stage hierarchy")
    print("      using framework primitives (q_3, q_2).")
    print("    - The b_1 phantom has a separate ad-hoc derivation.")
    print()

# ============================================================================
# (E) What we learned
# ============================================================================

def section_summary() -> None:
    header("(E) What this script establishes")
    print("""\
  RIGOROUSLY ESTABLISHED:

    (a) phantom_N = -6 is the weighted arithmetic mean of (lep.N, dn.N)
        with weight -q_3.  Framework-primitive expression.

    (b) phantom_b_2 = 21/10 is the weighted mediant of (lep.b_2, dn.b_2)
        with weight equal to phantom_N.  This is a true cross-link: the
        N phantom becomes the weight for the b_2 phantom.

    (c) Together (a) and (b) form a clean two-stage hierarchical
        derivation:

            stage 1:  phantom_N from sector N with weight -q_3
            stage 2:  phantom_b_2 from sector b_2 with weight = phantom_N

        This uses only {q_2, q_3, lep-dn pair data} and produces
        phantom_N and phantom_b_2 as structural consequences.

    (c') Extending the weighted mediant rule to b_1 with weight =
         phantom_N gives 13/8 = F_7/F_6, which is the NEXT Fibonacci
         convergent of phi beyond up.b_1 = 8/5 = F_6/F_5.  This is a
         clean structural object but it is NOT the Mobius phantom 13/9.
         For b_1 the two constructions DIVERGE.

  PARTIALLY ESTABLISHED:

    (d) phantom_b_1 = 13/9 can be written as a simple mediant of
        (up.b_1, dn.b_1), which is arithmetically correct but uses a
        different construction than (a) and (b).  The 'mediant' is
        not a canonical tree operation here because 8/5 and 5/4 are
        not Farey neighbors.

    (e) Alternative: phantom_b_1 as a weighted mediant of
        (lep.b_1, dn.b_1) requires weight 7, which is not a clean
        framework primitive.

  NOT ESTABLISHED:

    (f) A single Klein-topology principle from which all three
        phantoms emerge.  The hierarchy (a)->(b) is clean but does
        not extend to (c).

    (g) A first-principles derivation of the weight -q_3 in the
        N-phantom formula.  Why that specific weight?  No topology
        argument given.

    (h) A formal connection to Klein bottle fundamental group,
        Stern-Brocot tree, or SL(2, Z) action.

  READING:

  The framework has a PARTIAL Klein-topology structure for the phantom
  fixed points.  The N and b_2 phantoms follow a clean hierarchical
  rule that uses only framework primitives.  The b_1 phantom does not
  fit this hierarchy and has an alternative arithmetic-mediant form.

  One interpretation: b_2 and N are the 'additive' coordinates of the
  matter sector (where phantoms come from weighted means), while b_1
  is the 'Fibonacci-shift' coordinate (where up has non-consecutive
  Fibonacci convergents and the phantom structure is different).

  Another interpretation: the derivation we found is actually the
  wrong frame, and the 'right' Klein-topology derivation would
  treat b_1, b_2, and N symmetrically.  If that derivation exists,
  it is not this one.

  Either way: the twin swap formalization from twin_swap_formalization.py
  remains valid as a Mobius involution construction.  What is still
  missing is a clean topological justification for WHY the phantom
  fixed points have their specific framework-alphabet values.
""")

def main() -> None:
    print("=" * 78)
    print("  KLEIN TOPOLOGY PHANTOMS: partial structural derivation")
    print("=" * 78)
    section_N()
    section_b2()
    section_b1()
    section_unify()
    section_summary()

if __name__ == "__main__":
    main()
