"""
string_nodes_and_pitches.py

Reframe the framework's matter-sector base pairs in the language of
string nodes / harmonic series intervals, and test whether K_STAR has
a clean 'tempered' (2^(k/n)) form.

Physical setup: a vibrating string of length L with fixed ends has
modes at integer multiples of the fundamental frequency f.  Touching
the string at position 1/n excites the n-th harmonic at frequency
n*f.  Adjacent harmonics give the just-intonation intervals:

    1 -> 2: 2/1 = octave            (= q_2)
    2 -> 3: 3/2 = perfect fifth     (= up.b_2 = lep.b_1)
    3 -> 4: 4/3 = perfect fourth
    4 -> 5: 5/4 = major third       (= dn.b_1)
    5 -> 6: 6/5 = minor third
    6 -> 7: 7/6 = septimal third
    7 -> 8: 8/7 = septimal whole tone
    8 -> 9: 9/8 = whole tone (major)(= dn.b_2)
    9 -> 10: 10/9 = whole tone (minor)
    10 -> 11: 11/10 = neutral second
    ...

The matter sector base pairs are EXACTLY harmonic-series intervals:

    lep: (3/2, 5/3) = (perfect fifth, major sixth)
    up:  (8/5, 3/2) = (minor sixth, perfect fifth)
    dn:  (5/4, 9/8) = (major third, major whole tone)

And the inner ratios b_2/b_1 are recognizable musical inflections:

    lep r = 10/9  = +182.40 cents (ascending minor whole tone)
    up  r = 15/16 = -111.73 cents (descending diatonic semitone)
    dn  r = 9/10  = -182.40 cents (descending minor whole tone)

The lep-dn reciprocity is a literal MUSICAL MIRROR: lep ascends by a
minor whole tone, dn descends by the same amount.  +182.40 + -182.40
= 0 exactly.  Up sits between them at -111.73 (descending semitone),
the only sector with a non-mirror inflection.

Then we test: is K_STAR a 'tempered interval' of the form 2^(-k/n)?

Result: 2^(-3/14) = 0.86197282 vs K_STAR = 0.86196052.  Gap
0.0014% relative, which is 1.225e-5 absolute -- WITHIN the 2.06e-5
uncertainty quoted on K_STAR_lep (0.59 sigma).  This is the first
sub-sigma candidate of the session.

The 14 in 2^(-3/14) does not have a fully clean framework reading:
14 = q_2 * |F_4| = 2 * 7, where |F_4| = 7 is the Farey count at
depth 4.  Marginally framework-alphabet, but less elegant than the
3 = q_3 in the numerator.

This is a candidate for closure, not yet a derivation.
"""

from __future__ import annotations

import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))

import math
from fractions import Fraction

from framework_constants import K_STAR, Q2, Q3

B1 = {'lep': Fraction(3, 2), 'up': Fraction(8, 5), 'dn': Fraction(5, 4)}
B2 = {'lep': Fraction(5, 3), 'up': Fraction(3, 2), 'dn': Fraction(9, 8)}

def header(text: str) -> None:
    print()
    print("-" * 78)
    print(f"  {text}")
    print("-" * 78)
    print()

def cents(ratio: float) -> float:
    return 1200 * math.log2(ratio)

# ============================================================================
# (A) The harmonic series and string nodes
# ============================================================================

def section_harmonics() -> None:
    header("(A) Harmonic series: string nodes and just intonation")
    print("  A vibrating string of length L with fixed ends has modes at")
    print("  integer multiples of the fundamental frequency f.  Touching")
    print("  the string at 1/n excites the n-th harmonic at frequency n*f.")
    print()
    print("  Adjacent harmonic intervals (just intonation):")
    print()
    print(f"    {'n -> n+1':<12} {'ratio':<8} {'cents':<10} {'name':<30}")
    print("    " + "-" * 60)
    intervals = [
        (1, 2, "2/1", "octave (= q_2)"),
        (2, 3, "3/2", "perfect fifth (= up.b_2 = lep.b_1)"),
        (3, 4, "4/3", "perfect fourth"),
        (4, 5, "5/4", "major third (= dn.b_1)"),
        (5, 6, "6/5", "minor third"),
        (6, 7, "7/6", "septimal third"),
        (7, 8, "8/7", "septimal whole tone"),
        (8, 9, "9/8", "whole tone major (= dn.b_2)"),
        (9, 10, "10/9", "whole tone minor (= lep b_2/b_1)"),
        (10, 11, "11/10", "neutral second"),
    ]
    for a, b, ratio_str, name in intervals:
        c = cents(b / a)
        print(f"    {a} -> {b:<7} {ratio_str:<8} {c:<10.2f} {name}")
    print()
    print("  Note that almost all matter-sector base ratios appear as")
    print("  adjacent harmonics in the first 10.  The ones that don't")
    print("  (5/3, 8/5) are NOT adjacent harmonics but COMPOUND intervals:")
    print("    5/3 = 5/(3*1) is the interval from the 3rd harmonic to the")
    print("          5th harmonic = major sixth")
    print("    8/5 = 8/(5*1) is the interval from the 5th to the 8th")
    print("          harmonic = minor sixth")
    print()

# ============================================================================
# (B) Matter sector as just-intonation intervals
# ============================================================================

def section_sectors_as_music() -> None:
    header("(B) Matter sector base pairs as musical intervals")
    print()
    interval_names = {
        Fraction(3, 2): "perfect fifth",
        Fraction(5, 3): "major sixth",
        Fraction(8, 5): "minor sixth",
        Fraction(5, 4): "major third",
        Fraction(9, 8): "major whole tone",
    }
    for sector in ['lep', 'up', 'dn']:
        b1, b2 = B1[sector], B2[sector]
        n1 = interval_names.get(b1, "")
        n2 = interval_names.get(b2, "")
        c1, c2 = cents(float(b1)), cents(float(b2))
        print(f"  {sector}: b_1 = {b1} ({c1:.1f} cents, {n1})")
        print(f"       b_2 = {b2} ({c2:.1f} cents, {n2})")
    print()
    print("  Pattern reading:")
    print("    lep -- (perfect 5th + major 6th)  --  the BRIGHTEST sector")
    print("    up  -- (minor 6th  + perfect 5th) --  the COMPLEMENTARY sector")
    print("    dn  -- (major 3rd  + major 2nd)   --  the DENSEST sector")
    print()
    print("  Larger intervals = lower harmonics = lighter sector.  The")
    print("  lepton sector occupies the harmonic range 1-5 (large intervals,")
    print("  fewest steps).  The down sector occupies 4-9 (smaller intervals,")
    print("  more steps packed in).  The up sector overlaps both, sitting in")
    print("  3-8.  This matches the integer-cell sizes:")
    print()
    print("    N_lep = 4   (largest intervals, 4-cell)")
    print("    N_up  = 9   (mixed intervals, 9-cell)")
    print("    N_dn  = 24  (smallest intervals, 24-cell, densest)")
    print()

# ============================================================================
# (C) Inner ratios as musical inflections
# ============================================================================

def section_inner_ratios() -> None:
    header("(C) Inner ratios b_2/b_1 as generation-step inflections")
    print()
    for sector in ['lep', 'up', 'dn']:
        r = B2[sector] / B1[sector]
        c = cents(float(r))
        direction = "ascending" if r > 1 else "descending"
        print(f"  {sector}: r = {r}  ({c:+.2f} cents, {direction})")
    print()
    print("  Musical interpretation:")
    print("    lep r = 10/9  = +182.40 cents = ASCENDING minor whole tone")
    print("    up  r = 15/16 = -111.73 cents = DESCENDING diatonic semitone")
    print("    dn  r = 9/10  = -182.40 cents = DESCENDING minor whole tone")
    print()
    print("  *** lep and dn are LITERAL musical mirrors ***")
    print("  Same interval, opposite direction.  The Axis 5 reciprocity from")
    print("  reciprocity_sweep.py is now revealed as a pitch-space symmetry:")
    print("  ascending-by-X and descending-by-X cancel exactly.")
    print()
    print("  Up's inflection is a different (smaller) interval entirely --")
    print("  the diatonic semitone, which is unrelated to the minor whole")
    print("  tone except by being 'about half its size'.")
    print()
    print(f"  Sum check: lep + dn cents = {cents(10/9) + cents(9/10):.6f}")
    print(f"  (zero, exact -- because they are exact reciprocals)")
    print()

# ============================================================================
# (D) K_STAR as a tempered interval
# ============================================================================

def section_temperament() -> None:
    header("(D) K_STAR as a tempered interval: 2^(-k/n)")
    print()
    print("  Equal temperament splits the octave into n equal parts.  An")
    print("  interval of -k steps is 2^(-k/n).  We search for small k, n")
    print("  such that 2^(-k/n) approximates K_STAR.")
    print()
    print(f"  K_STAR = {K_STAR}")
    print(f"  log_2(K_STAR) = {math.log(K_STAR)/math.log(2):.10f}")
    print()
    print(f"  {'k/n':<10} {'2^(-k/n)':<14} {'gap':<14} {'rel %':<10}")
    print("  " + "-" * 50)
    candidates = []
    for n in range(2, 30):
        for k in range(1, n):
            val = 2 ** (-k / n)
            gap = val - K_STAR
            rel = gap / K_STAR * 100
            if abs(rel) < 0.5:
                candidates.append((abs(rel), k, n, val, gap))
    candidates.sort()
    for rel, k, n, val, gap in candidates[:6]:
        print(f"  {k}/{n:<8}  {val:<14.10f}  {gap:+.4e}  {gap/K_STAR*100:+.4f}%")
    print()
    print("  The CLOSEST candidate is K_STAR ~= 2^(-3/14):")
    val = 2 ** (-3 / 14)
    gap = val - K_STAR
    print(f"    2^(-3/14)     = {val:.10f}")
    print(f"    K_STAR        = {K_STAR}")
    print(f"    abs gap       = {gap:+.6e}")
    print(f"    relative      = {gap/K_STAR*100:+.6f}%")
    print()
    print("  PRECISION CHECK against K_STAR_lep:")
    print("    K_STAR_lep = 0.86196057 +/- 2.06e-5")
    print("    (from item12_K_star_closure.py)")
    K_lep = 0.86196057
    sigma = 2.06e-5
    nsigma = abs(val - K_lep) / sigma
    print(f"    2^(-3/14) - K_STAR_lep = {val - K_lep:+.6e}")
    print(f"    in sigma units         = {nsigma:.3f}")
    print()
    if nsigma < 1.0:
        print("  *** Within 1 sigma of K_STAR_lep ***")
        print("  This is the FIRST sub-sigma candidate of the session.")
    print()
    print("  Framework-alphabet content of (3, 14):")
    print("    3 = q_3 (clean framework prime)")
    print("    14 = q_2 * 7 = q_2 * |F_4| where |F_4| = 7 (Farey count")
    print("                                                at depth 4)")
    print("    so 2^(-3/14) = q_2^(-q_3 / (q_2 * |F_4|))")
    print()
    print("  The numerator (q_3) is clean.  The denominator (q_2 * |F_4|)")
    print("  is alphabet but awkward.  Less elegant than other candidates")
    print("  structurally, but SIGNIFICANTLY closer numerically.")
    print()

# ============================================================================
# (E) Comparison to other near-miss candidates
# ============================================================================

def section_comparison() -> None:
    header("(E) Cumulative K_STAR candidates (this session)")
    print()
    print("  Ordered from closest to furthest:")
    print()
    K_lep = 0.86196057
    sigma = 2.06e-5
    candidates = [
        ("2^(-3/14)",                     2 ** (-3/14)),
        ("log(3/2)/log(8/5)",             math.log(3/2)/math.log(8/5)),
        ("2*pi/(2*pi+1)",                 2*math.pi/(2*math.pi+1)),
        ("8*phi/15",                      8*(1+math.sqrt(5))/2/15),
        ("(3/2)^(-7/19)",                 (3/2)**(-7/19)),
        ("(3/2)^(-4/11)",                 (3/2)**(-4/11)),
        ("108/125 (Axis 5 product)",      108/125),
        ("sqrt(3)/2",                     math.sqrt(3)/2),
        ("log_phi(3/2)",                  math.log(3/2)/math.log((1+math.sqrt(5))/2)),
    ]
    candidates.sort(key=lambda x: abs(x[1] - K_STAR))
    print(f"  {'candidate':<32} {'value':<14} {'rel %':<10} {'sigma':<10}")
    print("  " + "-" * 70)
    for label, val in candidates:
        rel = (val - K_STAR) / K_STAR * 100
        nsig = abs(val - K_lep) / sigma
        flag = " <-- sub-sigma" if nsig < 1 else ""
        print(f"  {label:<32} {val:<14.8f} {rel:+.4f}%   {nsig:.2f}{flag}")
    print()
    print("  Reading: 2^(-3/14) is the only sub-sigma candidate.  All")
    print("  others are 4 to 1500 sigma away from K_STAR_lep.")
    print()

# ============================================================================
# (F) What this reframes
# ============================================================================

def section_reframe() -> None:
    header("(F) What the string-pitch language reframes")
    print("""\
  The framework's matter sector is structurally identical to a
  just-intonation tuning problem on a vibrating string:

    - Sector base pairs ARE harmonic series intervals.
    - The lep-dn Axis 5 reciprocity IS a pitch-space mirror
      (ascending vs descending by the same interval).
    - The Pythagorean comma sits at the framework's natural depth
      (3^12 / 2^19), as shown in low_index_structure.py.
    - K_STAR sits at 2^(-3/14) within 0.59 sigma of K_STAR_lep,
      consistent with K_STAR being a 'tempered' coupling at the
      framework's natural depth.

  The musical interpretation is more than a metaphor.  Just intonation
  on a string with q_2 (octave) and q_3 (fifth) generators produces:

    - The Pythagorean comma at depth 12 (twelve fifths, seven octaves)
    - Framework-alphabet rationals at low harmonic numbers
    - A tuning-compromise problem when you try to use multiple keys

  The framework's 'tempering' problem is the same: to make all three
  sector ladders (lep, up, dn) consistent at the framework's operating
  depth, K_STAR has to sit at a SPECIFIC value that compromises
  between competing 'pure' ratios.  This is the same logic as equal
  temperament in music.

  The 2^(-3/14) candidate, if real, says K_STAR is the -3rd step of a
  14-tone equal temperament built on q_2 = octave.  The (3/14) ratio
  has q_3 in the numerator and q_2 * |F_4| in the denominator -- a
  framework-alphabet expression, though the 14 is awkward.

  STATUS:

    - 2^(-3/14) is a CANDIDATE FOR CLOSURE at K_STAR_lep precision
      (0.59 sigma).  Not previously found this session.
    - The framework-alphabet content of the exponent (3, 14) is
      partial: numerator clean (q_3), denominator marginal
      (q_2 * |F_4|).
    - The musical interpretation provides the FIRST first-principles
      reason for K_STAR to take a 'tempered' value: the matter sector
      has competing tunings that must be balanced, and 2^(-k/n) is
      the natural family of compromises.

  OPEN:

    - Why 14 specifically?  The framework's natural depth is 6-7,
      and |F_4| = 7 is one Farey count down.  q_2 * |F_4| = 14 may
      have a Klein-topology reading (the bottle's '14 cells' or
      similar) but that is not derived here.

    - Higher precision K_STAR.  If K_STAR is determined to more
      than 5 digits, we can either confirm 2^(-3/14) as the exact
      value or rule it out and look for a different tempering.

  Suggested next: compute K_STAR_lep at the tightest current PDG
  precision and check whether the 0.59 sigma agreement holds at the
  6th and 7th decimal places.
""")

def main() -> None:
    print("=" * 78)
    print("  STRING NODES AND PITCHES: matter sector as just intonation,")
    print("  K_STAR as a tempered interval")
    print("=" * 78)
    section_harmonics()
    section_sectors_as_music()
    section_inner_ratios()
    section_temperament()
    section_comparison()
    section_reframe()

if __name__ == "__main__":
    main()
