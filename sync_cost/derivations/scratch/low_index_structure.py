"""
low_index_structure.py

Probe the framework's low-index structure: which Fibonacci indices are
load-bearing, what the harmonic series first crossings produce, and
where the Pythagorean comma sits structurally.

Motivation: at the scale we have been working, the high-index Fibonacci
numbers feel noisy.  The structurally interesting content seems to live
in the low indices {F_0 = 0, F_1 = F_2 = 1, F_3 = 2, F_4 = 3, F_5 = 5},
which are exactly the framework primitives {0, 1, q_2, q_3, F_5}.

Three concrete probes:

  (A) Harmonic series partial sums starting from 1/2.  When does the
      sum first exceed 1, 2, 3?  What are the framework-alphabet
      content of those crossings?

  (B) Pythagorean comma: (3/2)^12 / 2^7 = 3^12 / 2^19.  Both exponents
      (12, 19) are framework alphabet.  Is this the BEST near-1 of
      the form q_3^n / q_2^m, and is the framework-alphabet pairing
      a coincidence?

  (C) Fibonacci low-index audit.  Which F_k actually appear in the
      framework's load-bearing equations, and which are downstream?
      What is the structural meaning of the F_1 = F_2 = 1 doubling?

Findings:

  (A) The first harmonic crossing of 1 is at depth 4 (1/2 + 1/3 + 1/4
      = 13/12), with both numerator and denominator in the framework
      alphabet:  13/12 = F_7 / (q_2^2 * q_3).  Depth 4 = N_lep = q_2^2.
      The first crossing of 2 is at depth 11 = |F_5| (framework Farey
      count at depth 5).

  (B) The Pythagorean comma 3^12/2^19 IS the unique tightest near-1
      of q_3^n/q_2^m in the explored range, and (12, 19) are both
      framework alphabet:
        12 = q_2^2 * q_3  (Higgs correction denominator factor)
        19 = |F_7|        (Farey mode count at depth 7)
      The next-best near-1 (3^29/2^46) is twice as far.

  (C) The framework's load-bearing constants come from low Fibonacci
      indices F_0 through F_7, which are {0, 1, 1, 2, 3, 5, 8, 13}.
      Higher indices appear only as derived correction terms.  The
      F_1 = F_2 = 1 boundary doubling corresponds to the matter
      sector's two-step base pair (b_1, b_2) per sector.

These are exploratory observations, not derivations.  They sharpen
the framing 'low indices are primary, high indices are downstream'
and identify specific structural objects (the harmonic crossing 13/12
and the Pythagorean comma 3^12/2^19) that sit at the framework's
natural depth without being explicitly invoked.
"""

from __future__ import annotations

import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))

import math
from fractions import Fraction

# ============================================================================
# (A) Harmonic series partial sums and first crossings
# ============================================================================

def section_harmonic() -> None:
    print()
    print("-" * 78)
    print("  (A) Harmonic partial sums from 1/2 and first integer crossings")
    print("-" * 78)
    print()
    print("  Compute S(k) = 1/2 + 1/3 + ... + 1/k for k = 2, 3, 4, ...")
    print("  Find the smallest depth k at which S(k) first exceeds an integer.")
    print()
    print(f"  {'k':>3}  {'S(k) as fraction':<22}  {'decimal':<10}  {'crosses':<10}")
    print("  " + "-" * 60)
    total = Fraction(0)
    integers_crossed = set()
    crossings = {}
    for k in range(2, 35):
        total += Fraction(1, k)
        crossed_now = ""
        for tgt in [1, 2, 3]:
            if tgt not in integers_crossed and total > tgt:
                integers_crossed.add(tgt)
                crossings[tgt] = (k, total)
                crossed_now = f"crosses {tgt}"
        if k <= 5 or crossed_now or k in [10, 11, 12, 30, 31, 32]:
            print(f"  {k:>3}  {str(total):<22}  {float(total):<10.4f}  {crossed_now}")
    print()

    print("  First crossings:")
    for tgt, (k, val) in crossings.items():
        excess = val - tgt
        print(f"    crosses {tgt} at depth k = {k}, value = {val} ({float(val):.6f})")
        print(f"      excess = {excess} = {float(excess):.6f}")
    print()

    print("  STRUCTURAL READING of crossing 1 at depth 4:")
    print("    depth k = 4 = q_2^2 = N_lep")
    print("    value = 13/12 = F_7 / (q_2^2 * q_3)")
    print("       (numerator F_7 = 13, denominator 12 = q_2^2 * q_3)")
    print("    excess = 1/12 = 1/(q_2^2 * q_3)")
    print("       (same denominator pattern as Higgs correction 1/228 =")
    print("        1/(q_2^2 * q_3 * F_7))")
    print()
    print("  The first time the harmonic sum (excluding 1/1) reaches 'one")
    print("  whole', it does so at depth equal to N_lep = q_2^2, with")
    print("  value 13/12 (framework alphabet) and excess 1/12 (framework")
    print("  alphabet).  This is a clean structural fact: the boundary of")
    print("  '0 to 1' in harmonic partials lives at the lepton's depth.")
    print()
    print("  STRUCTURAL READING of crossing 2 at depth 11:")
    print("    depth k = 11 = |F_5| (framework mode count at Farey depth 5)")
    print("    The first time the harmonic sum exceeds 'two whole', it")
    print("    does so at depth equal to the framework's depth-5 mode")
    print("    count.  This is the 'minimum self-predicting universe'")
    print("    depth from MINIMUM_SELF_PREDICTING_UNIVERSE.md.")
    print()
    print("  Crossing 3 at depth 31: 31 has no clean framework reading.")
    print()

# ============================================================================
# (B) Pythagorean comma and the q_3^n / q_2^m near-1 lattice
# ============================================================================

def section_pythagorean() -> None:
    print()
    print("-" * 78)
    print("  (B) Pythagorean comma and q_3^n / q_2^m near-1 lattice")
    print("-" * 78)
    print()
    print("  The Pythagorean comma is the inevitable mismatch between iterated")
    print("  3/2 (perfect fifths) and 2 (octaves):")
    print()
    print("      (3/2)^12 / 2^7 = 3^12 / 2^19 = 531441/524288")
    print()
    pcomma = Fraction(3) ** 12 / Fraction(2) ** 19
    print(f"      = {pcomma}")
    print(f"      = {float(pcomma):.10f}")
    print(f"      ~ 23.46 cents (the standard Pythagorean comma)")
    print()
    print("  Both exponents are framework-alphabet:")
    print("    12 = q_2^2 * q_3 = 4 * 3 (Higgs correction denominator factor)")
    print("    19 = |F_7|             (framework Farey count at depth 7)")
    print()
    print("  So the Pythagorean comma is")
    print()
    print("      q_3^(q_2^2 * q_3) / q_2^|F_7|")
    print()
    print("  Is (12, 19) just one of many near-1 candidates, or the unique")
    print("  best?  Sweep all q_3^n / q_2^m with n in [1, 30], m in [1, 50]:")
    print()
    best = []
    for n in range(1, 31):
        for m in range(1, 51):
            val = (3 ** n) / (2 ** m)
            if 0.9 < val < 1.1:
                best.append((abs(val - 1), n, m, val))
    best.sort()
    print(f"    {'|gap|':<10}  {'n':>3}  {'m':>3}  {'q_3^n / q_2^m':<14}")
    print("    " + "-" * 40)
    for diff, n, m, val in best[:8]:
        marker = " <-- Pythagorean comma" if (n, m) == (12, 19) else ""
        print(f"    {diff:<10.6f}  {n:>3}  {m:>3}  {val:<14.6f}{marker}")
    print()
    print("  The Pythagorean comma (12, 19) IS the unique tightest near-1")
    print("  in the whole range.  The next-best, (29, 46), is roughly")
    print("  twice as far from 1.  And (29, 46) has no clean framework")
    print("  reading.")
    print()
    print("  Reading: at the framework's natural depth (around 6-7 in")
    print("  Farey terms), the q_2 and q_3 iterations are MAXIMALLY")
    print("  COMMENSURATE -- they come closer to matching than at any")
    print("  shallower depth.  Beyond depth 7, the next match (3^29/2^46)")
    print("  is much further from 1.  So 'depth 7' is the framework's")
    print("  unique resonance depth between q_2 and q_3 iteration.")
    print()
    print("  Music interpretation: the Pythagorean comma is why we need")
    print("  equal temperament.  The 12-tone scale exists because 12 fifths")
    print("  ALMOST equal 7 octaves but not quite.  In framework terms, the")
    print("  matter sector's three generations exist because q_2^|F_7| ALMOST")
    print("  equals q_3^(q_2^2 q_3) but not quite.  The 'mismatch' is the")
    print("  generation hierarchy.")
    print()

# ============================================================================
# (C) Fibonacci low-index audit
# ============================================================================

def section_fibonacci_audit() -> None:
    print()
    print("-" * 78)
    print("  (C) Fibonacci low-index audit: which indices carry framework load")
    print("-" * 78)
    print()
    fibs = [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5),
            (6, 8), (7, 13), (8, 21), (9, 34), (10, 55), (11, 89)]
    print(f"  {'index':<6}  {'F_k':<6}  {'framework role':<55}")
    print("  " + "-" * 75)
    roles = {
        0: ('0', 'additive identity, the empty / null state'),
        1: ('1', 'multiplicative identity, the atomic unit'),
        2: ('1', 'second 1 -- the BOUNDARY DOUBLING (see section D)'),
        3: ('2', '= q_2, framework prime (the 2-tongue)'),
        4: ('3', '= q_3, framework prime (the 3-tongue)'),
        5: ('5', '= F_5, used in 1/(F_5^k) corrections; |F_5| = 11 modes'),
        6: ('8', '= q_2^3, used in sin^2 theta_W tree (8/35) and as N_dn term'),
        7: ('13', '= F_6_COUNT, harmonic 13/12, phantom_b_1 numerator'),
        8: ('21', 'phantom_b_2 numerator (= 21/10)'),
        9: ('34', 'not directly used in core closures'),
        10: ('55', 'sin^2 theta_W correction term (8/F_10^2 = 8/3025)'),
        11: ('89', 'not directly used'),
    }
    for i, f in fibs:
        val, role = roles[i]
        print(f"  F_{i:<3}    {val:<6}  {role}")
    print()
    print("  Load-bearing index range: F_0 through F_7, with F_8 and F_10")
    print("  appearing as derived correction terms.  F_9, F_11 do not carry")
    print("  framework load.")
    print()
    print("  The framework's primitive alphabet is essentially")
    print("    {F_0=0, F_1=1, F_3=q_2=2, F_4=q_3=3, F_5=5}")
    print("  with F_6=8 = q_2^3 (composite), F_7=13 = |F_6| (Farey count),")
    print("  and higher indices being downstream.")
    print()
    print("  The 'noise' the user noticed at higher indices is real: F_8")
    print("  through F_11 are mostly absent from core derivations, and the")
    print("  occurrences of F_10 = 55 (sin^2 theta_W correction) and F_8 =")
    print("  21 (phantom_b_2 numerator) are downstream consequences, not")
    print("  primary framework facts.")
    print()

# ============================================================================
# (D) The F_1 = F_2 = 1 boundary doubling
# ============================================================================

def section_doubling() -> None:
    print()
    print("-" * 78)
    print("  (D) The F_1 = F_2 = 1 boundary doubling")
    print("-" * 78)
    print()
    print("  Fibonacci has TWO consecutive 1s at indices 1 and 2:")
    print()
    print("      F_0 = 0,  F_1 = 1,  F_2 = 1,  F_3 = 2,  F_4 = 3,  ...")
    print()
    print("  The recurrence F_n = F_{n-1} + F_{n-2} requires TWO initial")
    print("  values to bootstrap.  The choice F_1 = F_2 = 1 (rather than")
    print("  F_1 = 1, F_2 = 2, which gives Lucas-style sequences) is what")
    print("  makes the sequence start at the multiplicative identity TWICE")
    print("  before any growth occurs.")
    print()
    print("  Structural reading of F_2 = F_1:")
    print("    F_2 = F_1 + F_0 = 1 + 0 = 1")
    print("    The recurrence applied to (F_1, F_0) = (1, 0) gives 1.")
    print("    F_2 is a 'boundary fixed point' of the recurrence: it equals")
    print("    F_1 because F_0 = 0 contributes nothing to the sum.")
    print()
    print("  Equivalent reading via convergents:")
    print("    F_1/F_0 = 1/0 = infinity   (the boundary of Q_+)")
    print("    F_2/F_1 = 1/1 = 1          (the unique fixed point of x -> 1/x)")
    print("    F_3/F_2 = 2/1 = 2 = q_2    (first non-trivial growth)")
    print("    F_4/F_3 = 3/2 = q_3/q_2    (= up.b_2 = lep.b_1, framework!)")
    print()
    print("  So the Fibonacci convergents START at the inversion fixed point")
    print("  (1/1) and then grow.  The 'two 1s' are the ONE-STEP rest at")
    print("  the inversion fixed point before growth begins.")
    print()
    print("  Framework parallel: in the matter sector, Axis 5 reciprocity")
    print("  showed that lep and dn are exact reciprocals (10/9 and 9/10),")
    print("  fixed under x -> 1/x as a pair, while UP sits closest to 1")
    print("  (15/16 = 0.9375).  The 'self-twin sector' up plays the same")
    print("  structural role as the 'F_1 = F_2 = 1' doubling: it is the")
    print("  boundary near the inversion fixed point.")
    print()
    print("  The framework's two-step base pair (b_1, b_2) per sector is the")
    print("  structural analog of the Fibonacci sequence's two-step boundary")
    print("  layer (F_1, F_2).  Both encode the 'two seeds needed to start")
    print("  a recurrence', and both have a special pair-sector (matter")
    print("  sector's lep-dn / Fibonacci's F_1-F_2) at the inversion fixed")
    print("  point.")
    print()

# ============================================================================
# (E) Synthesis
# ============================================================================

def section_synthesis() -> None:
    print()
    print("-" * 78)
    print("  (E) Synthesis: low-index structure as the framework's primary alphabet")
    print("-" * 78)
    print("""\
  What this audit shows:

    1. The framework's load-bearing primitives are the Fibonacci low
       indices F_0 through F_7, which compose to the alphabet
       {0, 1, q_2 = 2, q_3 = 3, F_5 = 5, F_6 = 8 = q_2^3, F_7 = 13}.
       Higher Fibonacci numbers (F_8 = 21, F_10 = 55) appear in
       correction terms but are downstream.

    2. The harmonic series partial sums starting from 1/2 first
       cross 1 at depth 4 = N_lep, with the crossing value 13/12
       being framework alphabet.  Crossing 2 happens at depth 11 =
       |F_5| (the minimum self-predicting universe mode count).
       Both first crossings hit framework-alphabet values at
       framework-natural depths.

    3. The Pythagorean comma 3^12 / 2^19 is the unique tightest
       near-1 of q_3^n / q_2^m in the explored range, with both
       exponents being framework alphabet (12 = q_2^2 q_3, 19 =
       |F_7|).  Music's '12 fifths almost equal 7 octaves' is the
       same structural fact as the framework's depth-7 Farey
       resonance.

    4. The F_1 = F_2 = 1 boundary doubling encodes the same
       structural pattern as the matter sector's lep-dn reciprocity
       around up: 'two seeds at the inversion fixed point of
       x -> 1/x'.

  What this means for the K_STAR investigation:

    The framework's structural depth is essentially F_7 / |F_7| ~
    13 to 19.  At this depth, q_2 and q_3 iteration are maximally
    commensurate (Pythagorean comma) and harmonic series partial
    sums first exceed integer thresholds with framework-alphabet
    content.  K_STAR is a quantity at this same natural depth, so
    if it is derivable from primitives, it must be expressible in
    the framework alphabet at depth ~7.

    The strongest matter-native candidate found for K_STAR is
    log(3/2)/log(8/5) = 0.8627 at 0.08% off PDG.  Both numerator
    and denominator come from the framework's Fibonacci convergents
    at low indices (F_4/F_3 and F_6/F_5).  This is consistent with
    'K_STAR lives in the low-index structure' but does not close
    the residual.

  Open structural question:

    Why does the framework's natural depth happen to be exactly
    where the Pythagorean comma is tightest?  This is either a
    deep structural fact (the framework's depth IS the resonance
    depth of q_2 and q_3 iteration) or a happy coincidence.  If
    the former, the Pythagorean comma should appear EXPLICITLY in
    some framework derivation -- it would be the natural 'small
    correction' at the framework's operating depth.

    Concretely, the Pythagorean comma 1.01364 is roughly the
    framework's 1.5% scale: similar in magnitude to the gauge
    sector tree-vs-PDG residuals (sin^2 theta_W is 1.1% off raw
    8/35; alpha_s/alpha_2 is 3.2% off raw 27/8).  Worth checking
    whether the gauge correction terms can be rewritten in
    Pythagorean-comma form.
""")

def main() -> None:
    print("=" * 78)
    print("  LOW-INDEX STRUCTURE: harmonic crossings, Pythagorean comma,")
    print("  Fibonacci audit")
    print("=" * 78)
    section_harmonic()
    section_pythagorean()
    section_fibonacci_audit()
    section_doubling()
    section_synthesis()

if __name__ == "__main__":
    main()
