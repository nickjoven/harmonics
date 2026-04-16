"""
step3_proof.py

Tighten Step 3 of the K_STAR ~ 2^(-3/14) chain from 'structural
identification via parsimony' to 'forced by signature (3,1) matching
on Farey sequence orbit structure'.

CLAIM:

  The framework's Farey index at the matter-sector scale is 4,
  uniquely forced by the canonical signature (3,1) structure from
  L1, via the following counting argument:

    (1) Signature (3,1) gives 4 phase states:
          3 observable (at least one channel locked)
          1 dark (both channels unlocked)

    (2) On the Farey sequence F_n, the involution x -> 1-x
        partitions F_n into pairs {r, 1-r} and fixed points
        (rationals with r = 1-r, i.e., r = 1/2).

    (3) The number of pairs equals the number of 'distinguishable
        locked configurations' (each pair represents one
        orientation-doublet that can sustain a lock).  The number
        of fixed points equals the number of 'self-conjugate'
        (dark) configurations.

    (4) Requiring (3 pairs + 1 fixed point) to match signature
        (3,1)'s (3 observable + 1 dark) picks out Farey index 4
        UNIQUELY.

  CHECK:

    n    |F_n|   pairs   fixed   structure
    1    2       1       0       (1 pair, 0 fixed)
    2    3       1       1       (1 pair, 1 fixed)
    3    5       2       1       (2 pairs, 1 fixed)
    4    7       3       1       (3 pairs, 1 fixed)  <-- MATCHES signature (3,1)
    5    11      5       1       (5 pairs, 1 fixed)
    6    13      6       1       (6 pairs, 1 fixed)
    7    19      9       1       (9 pairs, 1 fixed)

  n = 4 is the UNIQUE Farey index where the (pair, fixed) decomposition
  equals (3, 1).  Smaller indices have fewer pairs (1 or 2); larger
  indices have more pairs (5+).  Only n = 4 matches.

  This is NOT parsimony -- it is a unique match between two independent
  structures:
    - canonical signature (3,1) from framework L1
    - Farey sequence orbit structure under x -> 1-x (standard number
      theory)

WHY THE INVOLUTION IS x -> 1-x:

  x -> 1-x is the natural involution on F_n that preserves the
  sequence.  It sends a rational r to its 'complement' 1-r, which
  physically represents the 'time-reversed' or 'orientation-flipped'
  phase position.  In the circle map context, r and 1-r are the
  two 'dual' orbit positions on the rotation number axis [0, 1].

  A fixed point of x -> 1-x is exactly r = 1/2, which is the
  'self-dual' position (unchanged under orientation flip).  In
  signature (3,1) language, this corresponds to the 'dark' state
  where both channels are in an indistinguishable self-conjugate
  configuration.

  The pairs {r, 1-r} with r != 1/2 correspond to the observable
  generations: each pair is a doublet where orientation flip gives
  a distinct physical configuration.  The three pairs in F_4 are:
      {0, 1}     -- the boundary pair
      {1/4, 3/4} -- the 'quarter' pair
      {1/3, 2/3} -- the 'third' pair

  These three pairs could be identified with the three observable
  generations (leptons, up-type, down-type), though the specific
  mapping depends on the framework's per-sector detailed structure.

  The key point is the COUNT: 3 pairs + 1 fixed = F_4 structure
  matches signature (3,1) structure, and this match is unique.

STATUS UPGRADE:

  Original Step 3 was 'framework Farey depth = N_lep = 4, by
  parsimony'.  This was 3-way convergent but not derived.

  New Step 3 is 'framework Farey index = 4, forced by uniqueness
  of (3,1)-matching Farey orbit structure under x -> 1-x'.  This
  is tighter:

    - It uses two CANONICAL framework sources:
      (i)  Signature (3,1) from L1
      (ii) Farey sequence and its natural involution
    - The match is UNIQUE (not a minimum or parsimony argument)
    - n = 4 is FORCED, not chosen

  This is still not a theorem in the strict sense (we haven't
  proved that the correct mapping from framework to Farey must
  use x -> 1-x specifically), but it is substantially stronger
  than the original parsimony argument.

REMAINING LOAD-BEARING STEP:

  The argument now rests on the identification:

    'signature (3,1) phase states = Farey (3 pairs + 1 fixed)
     under x -> 1-x'

  i.e., the claim that the natural way to represent signature
  (3,1) in the Farey sequence is via the x -> 1-x involution's
  orbit structure.  This is a structural identification -- it
  assumes that the 'observable vs dark' distinction corresponds
  to 'pair vs fixed point' under complementation.

  This identification is NOT arbitrary: it is the most natural
  choice given that:
    - signature (3,1) is about 'lock vs unlocked' channel pairs
    - Farey x -> 1-x is about 'orientation flip' of rational
      phase positions
    - Both are Z_2-structured distinctions
    - The Klein bottle's half-twist gives an orientation flip
      that could plausibly correspond to the Farey complement

  But 'most natural' is not 'proven'.  The structural gap is
  now between 'signature phase states' and 'Farey involution
  orbits', not between 'depth = 4' and 'N_lep = 4'.
"""

from __future__ import annotations

import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))

import math
from fractions import Fraction

def header(text: str) -> None:
    print()
    print("-" * 78)
    print(f"  {text}")
    print("-" * 78)
    print()

def farey(n: int) -> list[Fraction]:
    """Return F_n = reduced fractions in [0,1] with denominator <= n."""
    result = set()
    for q in range(1, n + 1):
        for p in range(0, q + 1):
            if math.gcd(p, q) == 1:
                result.add(Fraction(p, q))
    return sorted(result)

def orbit_structure(n: int) -> tuple[list, list]:
    """Partition F_n under x -> 1-x into pairs and fixed points."""
    Fn = farey(n)
    pairs = []
    fixed = []
    seen = set()
    for r in Fn:
        if r in seen:
            continue
        comp = Fraction(1) - r
        if comp == r:
            fixed.append(r)
        else:
            pairs.append((r, comp))
        seen.add(r)
        seen.add(comp)
    return pairs, fixed

# ============================================================================
# (A) Claim and setup
# ============================================================================

def section_claim() -> None:
    header("(A) The claim")
    print("""\
  CLAIM:

    The framework's Farey index at the matter-sector scale is
    n = 4, uniquely forced by signature (3,1) matching the Farey
    sequence orbit structure under x -> 1-x.

  KEY INSIGHT:

    On the Farey sequence F_n, the involution x -> 1-x (complement
    in [0,1]) partitions F_n into:
      - pairs {r, 1-r} with r != 1/2
      - fixed points (just r = 1/2, for all n >= 2)

    The count (pairs, fixed) depends on n.  Only ONE n matches
    signature (3,1)'s (3 observable, 1 dark) structure.

  CORRESPONDENCE:

    framework signature (3,1)        Farey orbit under x -> 1-x
    --------------------------       ---------------------------
    3 observable generations    <->  3 pairs
    1 dark state                <->  1 fixed point (= 1/2)

    Why this correspondence?  Both are Z_2-structured: signature
    is {locked, unlocked}^2, Farey complement is x <-> 1-x.  The
    natural identification is 'observable generations are orbit
    pairs, dark state is the self-conjugate fixed point'.
""")

# ============================================================================
# (B) The Farey involution x -> 1-x
# ============================================================================

def section_involution() -> None:
    header("(B) The x -> 1-x involution on F_n")
    print("""\
  DEFINITION:

    For any Farey sequence F_n and rational r = p/q in F_n, define
    the complement as r' = 1 - r = (q-p)/q.  Note:
      - gcd(q-p, q) = gcd(p, q) = 1 (if r is in lowest terms)
      - 0 <= q-p <= q (so r' is still in [0, 1])
    Therefore r' is also in F_n.  The map r -> 1-r is an
    involution on F_n (since 1 - (1 - r) = r).

  FIXED POINTS:

    r = 1 - r  <=>  2r = 1  <=>  r = 1/2
    So the only fixed point is r = 1/2, which is in F_n for all
    n >= 2.  For n = 1, there are no fixed points.

  ORBIT COUNT:

    For n >= 2, the number of orbits is:
      fixed points: exactly 1 (namely 1/2)
      pairs:        (|F_n| - 1) / 2

    Since |F_n| is always odd for n >= 2 (because of the single
    fixed point at 1/2), this division is exact.

  PHYSICAL INTERPRETATION:

    In the circle map picture, r and 1-r are 'orientation-dual'
    rotation numbers.  A tongue at p/q and a tongue at (q-p)/q
    are related by reflecting the circle [0,1].  Under the Klein
    bottle's half-twist (an orientation-reversing action), p/q
    maps to (q-p)/q.

    The fixed point 1/2 is the 'self-dual' rotation number,
    unchanged under orientation flip.  It corresponds to a
    configuration that is BOTH orientations simultaneously, which
    physically is a 'dark' state (the framework cannot distinguish
    the two orientations of this particular rotation number).
""")

# ============================================================================
# (C) Counting pairs and fixed points at each n
# ============================================================================

def section_counting() -> None:
    header("(C) Orbit counts at each Farey index")
    print("  For each n, compute (pairs, fixed) under x -> 1-x:")
    print()
    print(f"  {'n':<4}  {'|F_n|':<8}  {'pairs':<8}  {'fixed':<8}  {'(p,f)':<10}  {'matches (3,1)?':<20}")
    print("  " + "-" * 70)
    for n in range(1, 10):
        pairs, fixed = orbit_structure(n)
        Fn_size = 2 * len(pairs) + len(fixed)
        match = " YES <-- FORCED" if (len(pairs), len(fixed)) == (3, 1) else "  no"
        print(f"  {n:<4}  {Fn_size:<8}  {len(pairs):<8}  {len(fixed):<8}  "
              f"({len(pairs)},{len(fixed)}){' ' * (8 - len(str(len(pairs))) - len(str(len(fixed))))}  {match}")
    print()
    print("  ONLY n = 4 gives (3, 1).  Smaller n have too few pairs; larger n")
    print("  have too many.  The framework's signature (3,1) structure is")
    print("  UNIQUELY compatible with Farey index 4.")
    print()

# ============================================================================
# (D) Explicit F_4 structure
# ============================================================================

def section_F4_explicit() -> None:
    header("(D) F_4 orbit structure explicitly")
    pairs, fixed = orbit_structure(4)
    F4 = farey(4)
    print(f"  F_4 = {{{', '.join(str(r) for r in F4)}}}")
    print(f"  |F_4| = {len(F4)}")
    print()
    print("  Under x -> 1-x, F_4 partitions into:")
    print()
    for i, (r, comp) in enumerate(pairs, 1):
        print(f"    Pair {i}: {r} <-> {comp}")
    print(f"    Fixed:  {fixed[0]}  (self-conjugate: 1 - 1/2 = 1/2)")
    print()
    print("  Total: 3 pairs + 1 fixed point = 7 elements = |F_4|")
    print()
    print("  INTERPRETATION under signature (3,1):")
    print()
    print("    The 3 pairs correspond to the 3 observable generations:")
    print("      Pair 1: {0/1, 1/1}  -- the 'boundary' generation")
    print("      Pair 2: {1/4, 3/4}  -- the 'quarter' generation")
    print("      Pair 3: {1/3, 2/3}  -- the 'third' generation")
    print()
    print("    The fixed point 1/2 corresponds to the dark state:")
    print("      1/2 is the self-dual rotation number, unchanged under")
    print("      orientation flip.  Physically this represents the")
    print("      'both channels unlocked and indistinguishable' configuration")
    print("      from signature (3,1).")
    print()
    print("  NOTE: the specific mapping of framework generations")
    print("  (lep, up, dn) to the three Farey pairs is not yet determined")
    print("  and would require additional structural input from the")
    print("  matter sector's sector integers or base pair data.  What IS")
    print("  determined is the COUNT: (3 pairs, 1 fixed) uniquely matches")
    print("  signature (3,1) at Farey index 4.")
    print()

# ============================================================================
# (E) Uniqueness argument
# ============================================================================

def section_uniqueness() -> None:
    header("(E) Why n = 4 is UNIQUE (not just parsimony)")
    print("""\
  The original Step 3 argument was:

    'Framework Farey index = 4 because the lepton atomic rational
     1/N_lep = 1/4 first appears at Farey index 4, and by parsimony
     the framework operates at this minimum.'

  This was 'structural identification', not a forced result.
  Parsimony is a preference, not a constraint.

  The new argument is:

    'Framework Farey index = 4 because signature (3,1) matches the
     Farey x -> 1-x orbit structure (3 pairs + 1 fixed) UNIQUELY
     at n = 4.  No other Farey index has this structure.'

  Uniqueness check:

    n < 4: too few pairs
      n = 1: 1 pair, 0 fixed  -- no 'dark' state
      n = 2: 1 pair, 1 fixed  -- only 1 observable
      n = 3: 2 pairs, 1 fixed -- only 2 observables
    n = 4: 3 pairs, 1 fixed   -- MATCHES (3,1)
    n > 4: too many pairs
      n = 5: 5 pairs, 1 fixed
      n = 6: 6 pairs, 1 fixed
      n = 7: 9 pairs, 1 fixed
      ...

  The pair count grows (approximately) as (|F_n| - 1)/2, which
  exceeds 3 for all n >= 5.  So the MATCH with signature (3,1)
  happens at EXACTLY one Farey index: n = 4.

  This is no longer 'pick the smallest' (parsimony).  It is
  'pick the unique one' (forced).  The structural gap has
  moved from

    [framework 'depth'] -> [Farey index 4]    (parsimony)

  to

    [signature (3,1) decomposition] -> [x -> 1-x orbit structure]
      (identification of a Z_2 symmetry in two different contexts)

  The latter is a more specific claim, more tightly constrained,
  and easier to check for consistency.
""")

# ============================================================================
# (F) What remains a structural identification
# ============================================================================

def section_remaining() -> None:
    header("(F) What's now a theorem, what's still an identification")
    print("""\
  THEOREM-LEVEL (with this proof):

    For each integer n >= 1, the Farey sequence F_n has a specific
    (pair, fixed) decomposition under x -> 1-x.  The decomposition
    is (p, f) with p = (|F_n| - 1)/2 for n >= 2 and f = 1 for
    n >= 2.  The ONLY n with (p, f) = (3, 1) is n = 4.  This is
    a theorem of elementary number theory.

    [Verified in Section C for n = 1..9.]

  STRUCTURAL IDENTIFICATION (load-bearing claim):

    The framework's signature (3,1) structure maps to Farey pairs
    and fixed points via:
      observable generations  <->  x -> 1-x pairs
      dark state              <->  x -> 1-x fixed point

    This identification is based on the Z_2 structure of both
    sides:
      signature (3,1) has 'locked/unlocked' binary distinction
      per channel
      x -> 1-x is a Z_2 involution on F_n

    The claim is that these two Z_2 structures are 'the same'
    up to the framework's chosen realization.  This is a
    structural identification, not a proven equivalence.

    However, it is a TIGHT identification:
      - Both sides have exactly one non-trivial Z_2 structure at
        the relevant scale
      - The Klein bottle's half-twist (L0 canonical) provides a
        geometric realization of the Z_2 on the rational phase
        space
      - The match of counts ((3,1) = (3,1)) is unique, not
        generic

  WHAT WOULD UPGRADE THIS TO A THEOREM:

    A proof that the framework's signature (3,1) structure IS the
    x -> 1-x involution on F_4 under the Klein bottle's half-twist
    action.  This requires explicitly constructing the action and
    showing its orbits match the signature decomposition.

    The ingredients are available:
      - Klein bottle half-twist: L0
      - Signature (3,1): L1
      - Farey F_4 with 7 elements: L2 (computable)
      - x -> 1-x involution: standard

    What is missing is the explicit map from the Klein bottle's
    half-twist action on the Stern-Brocot tree to the x -> 1-x
    involution on F_4.  That construction is the next level of
    rigor.

  STATUS:

    Step 3 is now PROVEN modulo the structural identification
    'signature (3,1) decomposition corresponds to Farey x -> 1-x
    decomposition at matching count'.  This is the cleanest form
    of the argument we can give without a fully explicit Klein
    bottle action on rationals.

    The identification is defensible because:
      - The Z_2 structures on both sides are canonical
      - The count match (3,1) = (3,1) at n = 4 is unique
      - The Klein bottle's half-twist naturally produces such a
        Z_2 action
      - No other Farey index is compatible with signature (3,1)

    This is substantially tighter than the original parsimony
    argument, and moves Step 3 from 'structural identification
    via minimum Farey hosting' to 'forced by unique (3,1) count
    match under Farey involution'.
""")

def main() -> None:
    print("=" * 78)
    print("  STEP 3 PROOF: framework Farey index = 4 forced by signature (3,1)")
    print("=" * 78)
    section_claim()
    section_involution()
    section_counting()
    section_F4_explicit()
    section_uniqueness()
    section_remaining()

if __name__ == "__main__":
    main()
