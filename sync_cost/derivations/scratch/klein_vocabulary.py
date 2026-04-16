"""
klein_vocabulary.py

Decompose the overloaded terms in the K_STAR ~ 2^(-3/14) chain into
their canonical framework meanings and reassign each chain step to
precise structures.  This is NOT new physics; it is a cleanup of
which framework concept each step actually uses.

MOTIVATION:

The chain (deriving_14.py + farey_depth_proof.py + octave_doubling.py
+ tau_mass_prediction.py) uses several words that have multiple
canonical meanings in the framework:

  - 'Klein parity' can mean Z_6 = Z_2 x Z_3 (L1 canonical) or the
    {+, -} sign per sector ({-, -, +} for {lep, up, dn}).  These
    are different objects.  The chain uses the Z_2 projection.

  - 'depth' can mean (i) integer-conservation-law depth (lepton = 3)
    from L3, (ii) Farey sequence index n in F_n, (iii) Stern-Brocot
    tree depth (number of L/R steps from 1/1), (iv) tongue-resolution
    q* at K_STAR in the circle map, (v) lepton phase-state count
    N_lep = 4 from signature (3,1).  The chain uses (v) and
    interprets it as Farey index.

  - 'Klein four-group' can mean (a) Z_2 x Z_2 (Signature's 4 phase
    states from {locked,unlocked}^2) or (b) the framework's XOR filter
    acting on Stern-Brocot at (q_2, q_3).  The chain uses (a).

  - 'octave' and 'EDO basis' are music-theory borrowings.  The chain
    identifies 'octave' with the q_2 = 2 doubling (framework primitive)
    and 'EDO basis' with the natural divisor of the q_2 interval at
    the framework's depth.

This script builds a tight vocabulary, then RESTATES the chain steps
using precise framework terms, and identifies which identifications
are strengthened and which remain structural.

RESULT:

  Two of the three soft chain identifications can be tightened by
  grounding in canonical framework vocabulary:

    Step 3 (framework depth = 4):
      Refined: 'the integer 4 enters as N_lep = |Klein four-group
      from signature (3,1)|, the phase-state count of the matter
      sector's atomic Klein structure'.  This is cleaner than
      'framework depth = N_lep by parsimony' but still identifies
      a specific integer (4) across multiple structural roles.

    Step 5 (EDO basis = q_2 * |F_d|):
      Refined: 'the factor q_2 = 2 in 14 = q_2 * |F_4| is the
      harmonic-subharmonic mirror (x -> 1/x) acting on the Farey
      rationals at depth 4, doubling the count from 7 to 14'.
      This is grounded in the Axis 5 reciprocity (lep-dn exact
      mirror) rather than in a claimed Klein parity extension
      to rationals.

  Step 6 (K_STAR^14 = 1/8) remains the unverified closed form,
  testable against future tau mass measurements.

The chain is not rigorously proven end-to-end, but the refined
version uses only canonical framework objects with documented
structural meanings.
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

# ============================================================================
# (A) Glossary: overloaded words in canonical framework
# ============================================================================

def section_glossary() -> None:
    header("(A) Overloaded vocabulary in the K_STAR chain")
    print("""\
  'KLEIN PARITY'

  Canonical (L1 from FRAMEWORK_TOPOLOGY.md):
     Klein parity = Z_2 x Z_3 = Z_6 center
     Origin: XOR filter on Stern-Brocot at (q_2, q_3)
             + GCD fiber as principal Z_6-bundle
     This is a group of order 6 acting on the framework's
     (q_2, q_3) Stern-Brocot structure.

  Sector parity signs (used in Axis 5 / mass_sector_closure):
     sigma(lep) = -1,  sigma(up) = -1,  sigma(dn) = +1
     These are a Z_2 projection of the Z_6 Klein parity.
     The signs come from orientation-reversing vs
     orientation-preserving orbits under the Klein bottle's
     half-twist action.

  'Klein parity Z_2' in our chain (Step 5 old version):
     Refers to the Z_2 PROJECTION of the Z_6 canonical Klein
     parity.  The factor 2 = q_2 = |Z_2| in '14 = q_2 * |F_4|'
     was claimed to come from this Z_2 acting on Farey rationals.
     This is a structural extension, not a theorem.

  ---

  'DEPTH'

  (i)   Integer-conservation-law depth (L3):
         depth * |3Q| = k_sector
         lepton depth = 3, up-type = 4, down-type = 8
         Origin: Stern-Brocot walk length times electric charge.
         This is the CANONICAL framework 'depth' per sector.

  (ii)  Farey sequence index n in F_n:
         |F_n| = 1 + sum_{k=1}^n phi(k)
         This is the 'rational denominator cutoff' interpretation.
         |F_4| = 7, |F_5| = 11, |F_6| = 13, |F_7| = 19.

  (iii) Stern-Brocot tree depth:
         Number of L/R mediant steps from the root 1/1.
         Matter sector b_1 ratios have SB depths {2, 4, 4}.
         Max b_1 SB depth = 4.

  (iv)  Tongue-resolution depth q* at K_STAR:
         Maximum q for which the Arnold tongue at p/q is 'visible'
         (width > some threshold) at coupling K_STAR.
         At K_STAR = 0.862, leading-order tongue widths give q* ~ 4.

  (v)   Lepton phase-state count N_lep:
         N_lep = q_2^2 = 4, from signature (3,1)'s
         {locked, unlocked}^2 = 4 phase states.
         NOT the same as 'lepton depth' from (i).

  In the K_STAR chain, 'framework depth = 4' pins the integer 4
  as the Farey sequence index (ii).  Its justification uses (v)
  N_lep = 4 plus the parsimony claim 'minimum Farey index that
  hosts 1/N_lep'.  But (v) is NOT canonically the 'lepton depth';
  the canonical depth is 3 from (i).  The chain uses N_lep (a
  phase-state count) rather than the canonical depth (a
  conservation-law integer).

  ---

  'KLEIN FOUR-GROUP'

  (a) Z_2 x Z_2 from signature (3,1):
      {(locked, locked), (locked, unlocked), (unlocked, locked),
       (unlocked, unlocked)}
      4 elements: 3 observable (at least one channel locked),
      1 dark (both unlocked, time-averages to zero coupling).
      This is the L1 structure from MINIMUM_SELF_PREDICTING_UNIVERSE
      §10 and minkowski_signature.md.

  (b) XOR filter Klein four-group:
      The Z_2 action from orientation reversal + a second Z_2 from
      filter parity.  Same abstract group as (a), different realization.

  In the chain, 'Klein four-group' = (a) from signature (3,1).
  Its order is 4 = N_lep.

  ---

  'OCTAVE' and 'EDO BASIS'

  Music-theory term 'octave': the interval 2:1 (one note to its
  double-frequency counterpart).  Framework identification:
     octave <-> q_2 = 2 (the primary prime)

  Music-theory term 'EDO (equal division of the octave)':
     n-EDO = {2^(k/n) : k = 0, 1, ..., n-1}
     n distinct frequencies dividing the octave into equal log steps.

  In the chain, 'EDO basis' = n in 2^(k/n) form of K_STAR.
     K_STAR ~ 2^(-3/14) <=> n = 14, k = -3.
     The claim is n = q_2 * |F_d| = 14 for d = 4.

  The q_2 factor in n has two distinct roles in the formula:
    (1) Base of the exponent: K_STAR = q_2^(-3/14) uses q_2 = 2 as
        the log base (the 'octave' we divide).
    (2) Multiplier in the denominator: 14 = q_2 * |F_4|, where q_2
        is a SEPARATE factor in the count.

  Both uses of q_2 are the framework's same primitive prime, but
  they enter in different structural roles (base vs multiplier).
""")

# ============================================================================
# (B) Refined Step 3: framework 'phase-state count' = |Klein four-group| = 4
# ============================================================================

def section_step3_refined() -> None:
    header("(B) Step 3 refined: the integer 4")
    print("""\
  ORIGINAL WORDING:

    Step 3: Framework Farey depth = N_lep = 4
    Justification: 'minimum Farey index that hosts lepton's
    atomic rational 1/N_lep' + parsimony.

  PROBLEM:

    The word 'depth' is overloaded.  Canonical lepton depth from
    integer conservation law is 3, not 4.  Using 'depth = 4'
    requires a non-canonical interpretation.

  REFINED WORDING:

    Step 3': The integer 4 enters the chain as
             N_lep = |Klein four-group from signature (3,1)|
             = |Z_2 x Z_2|
             = 4

    We then identify this integer with the Farey sequence index n
    in F_n for the purposes of counting framework-visible rationals.
    This identification is the load-bearing structural step.

  WHY IS 4 ALSO THE FAREY INDEX?

    Three convergent arguments, each using different framework
    primitives (from farey_depth_proof.py):

    (i)   4 is the smallest Farey index n with 1/4 in F_n, and
          1/N_lep = 1/4 is the lepton sector's atomic rational
          (parsimony).

    (ii)  4 is the maximum Stern-Brocot tree depth of any b_1
          ratio in the matter sector (up.b_1 = 8/5 and dn.b_1 =
          5/4 both at SB depth 4; lep.b_1 at SB depth 2).

    (iii) 4 is the tongue-resolution threshold q* at K_STAR: the
          largest q for which the Arnold tongue at p/q is visible
          (leading-order width > 10^-3) in the framework's circle
          map at coupling K_STAR.

    All three arguments give 4.  None uses the canonical
    integer-conservation-law 'lepton depth' (which is 3).  The
    identification 'framework Farey index = |Klein four-group|'
    is structural, not derived from a single canonical source.

  STATUS:

    The integer 4 is canonically the order of the Klein four-group
    from signature (3,1).  Its identification as the Farey index
    is the load-bearing claim of Step 3.  Three convergent
    arguments support it, none of which is a theorem.
""")

# ============================================================================
# (C) Refined Step 5: q_2 factor from harmonic-subharmonic mirror
# ============================================================================

def section_step5_refined() -> None:
    header("(C) Step 5 refined: q_2 factor from harmonic-subharmonic mirror")
    print("""\
  ORIGINAL WORDING:

    Step 5: EDO basis = q_2 * |F_4| = 14
    Justification: 'Klein parity Z_2 acts on each Farey rational,
    doubling the count from 7 to 14'.

  PROBLEM:

    'Klein parity' is canonically Z_6 (L1), not Z_2.  The 'Klein
    parity Z_2' used in the chain is a projection.  Claiming it
    'acts on Farey rationals' extends a sector-level concept to
    a position-level concept without a bridge.

  REFINED WORDING:

    Step 5': The EDO basis is q_2 * |F_4| because the framework's
             rational phase space has a natural Z_2 symmetry under
             the harmonic-subharmonic mirror x -> 1/x acting on
             the Stern-Brocot tree.  This mirror doubles the count
             of 'distinct rational phase positions' at depth d
             from |F_d| (harmonic positions in [0, 1]) to 2|F_d|
             (harmonic positions in [0, 1] PLUS subharmonic
             positions in [1, infty] via reciprocation).

  WHY THE HARMONIC-SUBHARMONIC MIRROR INSTEAD OF KLEIN PARITY?

    Three reasons:

    (i)   The framework's Axis 5 reciprocity is EXACTLY this
          mirror at the sector level: lep.r = 10/9 and dn.r = 9/10
          are multiplicative inverses, as we found in
          axis5_reciprocity_and_logratio.py and verified in
          reciprocity_sweep.py.  Up is the self-conjugate anchor
          at the inversion fixed point 1/1.

    (ii)  The Stern-Brocot tree is SELF-DUAL under x -> 1/x.  Its
          left subtree (rationals in (0,1)) is the inverse image
          of its right subtree (rationals in (1, infty)).  Any
          counting of 'rational phase positions' naturally
          encompasses both.

    (iii) Kawano et al. 2025 experimentally validates that both
          harmonic (Helmholtz) and subharmonic modes are stable
          solutions of the bowed-string nonlinear oscillator.
          The framework's analog is that phase-space positions
          come in harmonic-subharmonic pairs, doubling any raw
          count of 'rational positions'.

  WHAT THE q_2 MULTIPLIER ACTUALLY MEANS:

    The factor q_2 = 2 in '14 = q_2 * |F_4|' is NOT a Klein parity
    acting on rationals.  It is the 'harmonic and subharmonic
    copy count' -- you count each Farey rational TWICE (once as a
    harmonic position, once as a subharmonic position via
    reciprocation).

    The base q_2 in 'K_STAR = q_2^(-3/14)' is the octave doubling
    of the log scale -- the natural unit for equal-temperament-like
    divisions in a q_2-generated framework.

    Both uses of q_2 = 2 are the same framework prime, but they
    enter in different structural roles:
      - Base: the q_2-fold scaling that defines the 'octave'
      - Multiplier: the harmonic-subharmonic mirror Z_2

  STATUS:

    The refined q_2 factor is grounded in the Axis 5 reciprocity
    (lep-dn exact mirror), which is a rigorously established
    framework property.  This is cleaner than 'Klein parity
    extended to Farey rationals', which was a structural guess.

    It is STILL a structural identification that the harmonic-
    subharmonic mirror doubles the 'EDO basis count' -- we have
    not proved that the EDO basis must count both harmonic and
    subharmonic positions separately.  But the identification is
    grounded in a verified framework-level reciprocity rather
    than in an uncanonical Klein parity extension.
""")

# ============================================================================
# (D) Refined chain statement
# ============================================================================

def section_refined_chain() -> None:
    header("(D) Refined chain with cleaned vocabulary")
    print("""\
  Step 1: The framework's primary prime q_2 = 2 is the order of
          the Z_2 factor in the canonical Z_6 = Z_2 x Z_3 Klein
          parity (L1, from FRAMEWORK_TOPOLOGY.md).
                                     [canonical]

  Step 2: The lepton sector's phase-state count is
          N_lep = q_2^2 = |Z_2 x Z_2| = |Klein four-group from
          signature (3,1)| = 4.  This is NOT the 'lepton depth'
          from integer conservation (which is 3); it is the
          phase-state count from signature.
                                     [canonical L1/L3]

  Step 3': The integer 4 from Step 2 is identified with the
           Farey sequence index used to count framework-visible
           rationals.  Three convergent arguments (lepton atomic
           rational 1/4 in F_4, max b_1 Stern-Brocot depth = 4,
           tongue-resolution threshold q* ~ 4 at K_STAR) support
           this identification.
                     [structural, 3-way convergent, not theorem]

  Step 4: At Farey index 4, the Farey count is
          |F_4| = 1 + sum_{k=1}^4 phi(k)
                = 1 + 1 + 1 + 2 + 2 = 7
                                     [Farey formula]

  Step 5': The framework's 'EDO basis' at depth 4 is
            q_2 * |F_4| = 2 * 7 = 14
           where the factor 2 is the harmonic-subharmonic mirror
           (x -> 1/x) doubling on the Stern-Brocot tree, grounded
           in the Axis 5 reciprocity (lep.r * dn.r = 1, from
           reciprocity_sweep.py).  Each Farey rational at depth
           4 has a mirror image under x -> 1/x; the total count
           of 'rational phase positions' is doubled.
                                     [structural, grounded in
                                      Axis 5 reciprocity]

  Step 6: The framework's coupling K_STAR satisfies the closed
          form K_STAR^14 = q_2^(-q_3) = 1/8.  Equivalently,
          K_STAR = 2^(-q_3 / (q_2 * |F_4|)) = 2^(-3/14).
                    [conjectured closed form, 0.594 sigma from
                     PDG, requires tighter m_tau to resolve]

  FOLLOW-ON PREDICTION (tau_mass_prediction.py):

    Given Step 6 as an assumption, the framework predicts
      m_tau = m_mu * (3/2)^(3 * 2^(17/14))
            = 1776.78875 +/- 3.87e-5 MeV
    at ~22 ppb precision (inherited from m_mu).  Falsifiable by
    future tau mass measurements at sigma < 0.03 MeV.
""")

# ============================================================================
# (E) What's improved, what remains
# ============================================================================

def section_assessment() -> None:
    header("(E) What's improved, what remains")
    print("""\
  IMPROVED BY THIS VOCABULARY CLEANUP:

    1. Step 3 now explicitly states that the integer 4 enters as
       |Klein four-group from signature (3,1)| = N_lep, not as an
       ambiguous 'framework depth'.  The canonical L1/L3 source
       is identified.

    2. Step 5 is grounded in the Axis 5 reciprocity (a verified
       framework property) rather than in an uncanonical extension
       of Klein parity to Farey rationals.  The harmonic-
       subharmonic mirror is an established framework structure.

    3. The distinction between 'canonical lepton depth = 3' (from
       integer conservation) and 'lepton phase-state count = 4'
       (from signature) is now explicit.  The chain uses the
       latter; the former is a different integer with a different
       role.

    4. The dual roles of q_2 in the formula 2^(-3/14) are made
       explicit: q_2 as the base of the exponential (octave
       doubling) and q_2 as the multiplier in the denominator
       (harmonic-subharmonic mirror).  Same prime, different
       structural roles.

  STILL STRUCTURAL (not theorem) AFTER CLEANUP:

    (a) 'Framework Farey index = |Klein four-group|':  the
        identification of the integer 4 from signature-(3,1)
        phase count with the Farey sequence index is the
        load-bearing assumption of Step 3.  Three convergent
        arguments support it; none is a theorem from Klein
        topology.

    (b) 'EDO basis counts both harmonic and subharmonic positions':
        the claim that the natural count at depth d is 2|F_d|
        rather than |F_d| or |F_d|+1 is grounded in the
        Stern-Brocot self-duality but has not been derived from
        a first-principles Klein topology theorem.

    (c) 'K_STAR^14 = 1/8 exactly':  the closed form holds at
        0.594 sigma of PDG m_tau.  Consistent but not confirmed.

  NEXT STEPS FOR EACH SOFT IDENTIFICATION:

    (a) Prove from Klein topology that the 'framework Farey
        index' is exactly the phase-state count of signature
        (3,1).  Likely route: show that the matter sector's
        atomic rational resolution is bounded below by the
        phase-state count, and parsimony fixes the minimum.

    (b) Prove that the EDO basis at depth d is 2|F_d| rather
        than other counts.  Likely route: show that Stern-Brocot
        self-duality implies the count must be multiplicative
        under x -> 1/x, and the smallest non-trivial count
        satisfying this is 2|F_d|.

    (c) Improve tau mass precision (experimental) or find an
        independent framework quantity that satisfies the same
        K^14 = 1/8-style closed form (theoretical corroboration).

  WHAT DOES NOT REQUIRE FURTHER JUSTIFICATION:

    - Step 1 (q_2 = 2): canonical L1 primitive.
    - Step 2 (N_lep = 4): canonical L1/L3 derivation from
      signature (3,1).
    - Step 4 (|F_4| = 7): Farey formula, exact.

  The chain's structural weight is concentrated in Steps 3, 5, 6.
  This vocabulary cleanup shows that Step 3 and Step 5 can be
  restated using canonical framework objects with documented
  meanings, which strengthens their defensibility without
  promoting them to theorems.  Step 6 remains the falsifiable
  closed-form conjecture, testable via tau mass precision.
""")

def main() -> None:
    print("=" * 78)
    print("  KLEIN VOCABULARY: decompose overloaded terms, refine chain identifications")
    print("=" * 78)
    section_glossary()
    section_step3_refined()
    section_step5_refined()
    section_refined_chain()
    section_assessment()

if __name__ == "__main__":
    main()
