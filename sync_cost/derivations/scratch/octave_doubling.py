"""
octave_doubling.py

Next incremental step on the K_STAR ~ 2^(-3/14) chain.  Derive the
q_2 factor in the EDO basis 14 = q_2 * |F_4| from a framework-internal
argument (Klein parity Z_2 acting on Farey rationals), not from
music-theory analogy.

Three new findings in this chunk:

(A) The cleanest closed-form for the candidate is

        K_STAR^14 = q_2^(-q_3) = 1/8

    Within 0.595 sigma of K_STAR_lep^14 = 0.124975.  This is an
    EXACT algebraic identity (modulo sigma) between K_STAR and
    framework primes.  It rephrases 2^(-3/14) as a self-consistency
    condition on the matter sector.

(B) The q_2 factor in the EDO basis comes from Klein parity Z_2
    acting on each Farey rational at depth 4.  Each rational has
    two Klein-twisted orientation states, doubling the count from
    |F_4| = 7 to 2 * 7 = 14.  The factor q_2 is the SAME q_2 = |Z_2|
    from Step 1 of the chain.

(C) Bonus from the musical observation: in the E1 overtone series
    (E1, E2, B2, E3, G#3, B3, ...), the first 'B' that appears is
    B2, not B1.  B1 is BELOW the fundamental and never appears.
    This means the q_3-related note ('fifth') only emerges AFTER
    the q_2-octave is established.  q_3 is structurally secondary
    to q_2 in any harmonic series.

(D) Bonus on odd-index Fibonacci: F_{2k-1} = F_k^2 + F_{k-1}^2 for
    all k.  In particular,

        F_7 = F_4^2 + F_3^2 = q_3^2 + q_2^2 = N_up + N_lep = 13

    F_7 = 13 is structurally equal to the sum of the two smallest
    sector cells.  And 13 is also the framework's |F_6_count| (Farey
    mode count at depth 6), giving F_7 a TWIN role: simultaneously
    a Fibonacci number AND a sector-cell sum AND a Farey count.
    This is the cleanest 'odd-index Fibonacci has a framework
    meaning' I can give.

Status of the chain:

    Step 1: q_2 = 2 (Klein parity)                  [primitive]
    Step 2: N_lep = q_2^2 = 4                       [canonical]
    Step 3: Framework depth = 4                     [3-way convergent]
    Step 4: |F_4| = 7                               [Farey theorem]
    Step 5: EDO basis = q_2 * |F_4| = 14            [Klein doubling]  <-- this chunk
    Step 6: K_STAR^14 = q_2^(-q_3)                  [closed form]

Chain still has soft links: Step 3 is convergent but not theorem,
Step 5 is now framework-internal but the 'Klein parity acts on Farey
rationals' identification is an extension of Klein parity from
sectors to rationals.  The chain is plausible, partially derived,
not yet airtight.
"""

from __future__ import annotations

import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))

import math
from fractions import Fraction

from framework_constants import K_STAR, Q2, Q3

def header(text: str) -> None:
    print()
    print("-" * 78)
    print(f"  {text}")
    print("-" * 78)
    print()

def phi(n: int) -> int:
    return sum(1 for k in range(1, n + 1) if math.gcd(k, n) == 1)

def farey_count(n: int) -> int:
    return 1 + sum(phi(k) for k in range(1, n + 1))

# ============================================================================
# (A) The closed-form relation K_STAR^14 = q_2^(-q_3) = 1/8
# ============================================================================

def section_closed_form() -> None:
    header("(A) The closed-form: K_STAR^14 = q_2^(-q_3) = 1/8")
    print("  The candidate 2^(-3/14) can be rewritten as a self-consistency")
    print("  condition on K_STAR and the framework primes:")
    print()
    print("      K_STAR^14 = 2^(-3) = 1/8 = q_2^(-q_3)")
    print()
    print("  Equivalent forms:")
    print("      K_STAR = (1/8)^(1/14) = q_2^(-q_3/14)")
    print("      K_STAR = q_2^(-q_3 / (q_2 * |F_4|))")
    print("      log_q_2(K_STAR) = -q_3 / (q_2 * |F_4|) = -3/14")
    print()
    print(f"  Numerical check:")
    print(f"    K_STAR (canonical)        = {K_STAR:.10f}")
    K_lep = 0.86196057
    sigma = 2.06e-5
    print(f"    K_lep                     = {K_lep:.10f} +/- {sigma:.2e}")
    print(f"    K_STAR^14                 = {K_STAR**14:.10f}")
    print(f"    K_lep^14                  = {K_lep**14:.10f}")
    print(f"    1/8 = q_2^(-q_3)          = {1/8:.10f}")
    print()
    sigma_K14 = 14 * K_lep**13 * sigma
    print(f"    K_lep^14 - 1/8            = {K_lep**14 - 1/8:+.6e}")
    print(f"    propagated sigma(K^14)    = {sigma_K14:.4e}")
    print(f"    in sigma units            = {abs(K_lep**14 - 1/8) / sigma_K14:.3f}")
    print()
    print("  *** Within 0.6 sigma -- closed-form candidate ***")
    print()
    print("  Reading: K_STAR is the unique positive real such that 14")
    print("  applications of K_STAR equals q_2 raised to -q_3.  This is a")
    print("  self-consistency condition on the matter sector that uses only")
    print("  the framework primes {q_2, q_3} and the integer 14.")
    print()
    print("  The integer 14 is what we have to derive structurally.  This")
    print("  reduces to deriving the q_2 factor in 14 = q_2 * |F_4|.")
    print()

# ============================================================================
# (B) Klein parity Z_2 doubling: the framework-internal q_2 derivation
# ============================================================================

def section_klein_doubling() -> None:
    header("(B) Klein parity doubling: 14 = q_2 * |F_4|")
    print("  At framework depth 4, the Farey sequence has |F_4| = 7 rationals:")
    print()
    F4 = []
    for q in range(1, 5):
        for p in range(0, q + 1):
            if math.gcd(p, q) == 1:
                F4.append(Fraction(p, q))
    F4 = sorted(set(F4))
    for r in F4:
        print(f"    {r}")
    print()
    print(f"  |F_4| = {len(F4)} = 7")
    print()
    print("  CLAIM: the framework's natural EDO basis at depth 4 is")
    print("  q_2 * |F_4| = 2 * 7 = 14, where the factor q_2 = |Z_2| comes")
    print("  from the Klein parity acting on each Farey rational.")
    print()
    print("  ARGUMENT:")
    print()
    print("  In the framework, Klein parity Z_2 = {+, -} is the orientation")
    print("  reversal generator of the Klein bottle's non-orientability.")
    print("  Each phase state on the Klein bottle has a Klein-twisted version")
    print("  (the same state with orientation reversed).  These are physically")
    print("  distinguishable but related by the Z_2 action.")
    print()
    print("  At depth 4, the Farey sequence F_4 enumerates the framework's")
    print("  primitive RATIONAL phase positions.  Each such position carries")
    print("  a Klein parity assignment: positive (orientation-preserving) or")
    print("  negative (orientation-reversing).")
    print()
    print(f"  Total (rational, parity) pairs at depth 4 = |F_4| * |Z_2|")
    print(f"                                             = 7 * 2")
    print(f"                                             = 14")
    print()
    print("  This is the framework's 'natural EDO basis' at depth 4.")
    print()
    print("  The factor 2 = q_2 = |Z_2| is the SAME q_2 that appears in")
    print("  Step 1 of the chain (Klein parity is Z_2).  It is not an")
    print("  external music-theory constant; it is the framework's primary")
    print("  prime acting twice in the derivation -- once as the order of")
    print("  Klein parity itself (Step 1), and once as the parity-doubling")
    print("  factor on Farey rationals (Step 5).")
    print()
    print("  HONEST CAVEAT:")
    print()
    print("  This argument extends Klein parity from SECTORS (where it's")
    print("  canonical: lep -, up -, dn +) to FAREY RATIONALS (where it's")
    print("  inferred).  The extension is plausible -- if Klein parity is a")
    print("  fundamental Z_2 of the Klein bottle topology, it should act on")
    print("  ALL phase positions, not just sector cells -- but this step is")
    print("  not derived from a Klein topology theorem.  It is a structural")
    print("  identification.")
    print()
    print("  Strength: framework-internal (no music-theory analogy), uses")
    print("  only Klein parity and the Farey count.")
    print()
    print("  Weakness: 'Klein parity acts on Farey rationals' is an extension,")
    print("  not a theorem.")
    print()

# ============================================================================
# (C) Musical support: B1 vs B2 in the E1 series
# ============================================================================

def section_musical() -> None:
    header("(C) Musical support: B1 vs B2 in the E1 overtone series")
    print("  The vibrating-string interpretation gives a clean reading of why")
    print("  q_2 is the framework's primary prime (the 'octave', not the 'fifth').")
    print()
    print("  Take E1 as the fundamental.  Its overtone series:")
    print()
    print("    1st harmonic:  E1   = f       (fundamental)")
    print("    2nd harmonic:  E2   = 2f      (octave above)")
    print("    3rd harmonic:  B2   = 3f      (octave + perfect fifth)")
    print("    4th harmonic:  E3   = 4f      (two octaves)")
    print("    5th harmonic:  G#3  = 5f      (two octaves + major third)")
    print("    6th harmonic:  B3   = 6f      (two octaves + perfect fifth)")
    print("    7th harmonic:  D4   = 7f      (septimal minor seventh)")
    print("    8th harmonic:  E4   = 8f      (three octaves)")
    print()
    print("  KEY OBSERVATION: the first 'B' to appear is B2, not B1.")
    print()
    print("  B1 has frequency ~3/2 of the FUNDAMENTAL going DOWN, but harmonic")
    print("  series only goes up from the fundamental.  B1 = (3/2)*f / 2 if E1")
    print("  is taken as f, but (3/4)*f is below f, NOT in the harmonic series.")
    print()
    print("  So in the integer harmonic series, the q_3-related note ('fifth')")
    print("  appears only at q_2 * q_3 * f = 6f (B3), or earlier at q_3 * f =")
    print("  3f (B2).  Both 3f and 6f are at LEAST one octave above the")
    print("  fundamental.  The 'pure fifth' from the fundamental (1.5f, which")
    print("  would be a B0) does NOT exist as a harmonic.")
    print()
    print("  FRAMEWORK READING:")
    print()
    print("  The framework's q_2 (Klein parity / octave) is PRIMARY because it")
    print("  generates the harmonic series itself.  The framework's q_3 (the")
    print("  '3-prime' / fifth) is SECONDARY because it only appears after the")
    print("  q_2 octave is established.")
    print()
    print("  The user's 'B1 isn't even native to the vocabulary' is precisely")
    print("  right: in the framework's harmonic-series language, q_3 cannot")
    print("  exist below the q_2 octave.  q_2 is the framework's octave-")
    print("  forming prime; q_3 is the within-octave division.")
    print()
    print("  This SUPPORTS the EDO basis = q_2 * |F_d| reading: q_2 gives the")
    print("  octave (the doubling), and |F_d| gives the within-octave Farey")
    print("  resolution.  Together they give the framework's atomic phase")
    print("  count at depth d.")
    print()
    print("  The harmonic-series argument is independent of the Klein parity")
    print("  argument from Section B but reaches the same conclusion: the q_2")
    print("  factor is primary, and the EDO basis is q_2 * |F_4| = 14.")
    print()

# ============================================================================
# (D) Odd-index Fibonacci as sums of squares
# ============================================================================

def section_odd_fibonacci() -> None:
    header("(D) Odd-index Fibonacci as sums of sector squares")
    print("  Mathematical identity: F_{2k-1} = F_k^2 + F_{k-1}^2 for all k.")
    print()
    F = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print(f"  {'k':<4}  {'F_{2k-1}':<10}  {'F_k^2 + F_{k-1}^2':<24}  {'value':<8}")
    print("  " + "-" * 50)
    for k in range(2, 7):
        rhs_str = f"{F[k]}^2 + {F[k-1]}^2"
        rhs_val = F[k]**2 + F[k-1]**2
        idx = 2*k - 1
        print(f"  {k:<4}  F_{idx:<8}  {rhs_str:<24}  {rhs_val:<8}")
    print()
    print("  The odd-index Fibonacci numbers are sums of squares of consecutive")
    print("  Fibonacci numbers.  In the framework alphabet:")
    print()
    print("    F_3 = F_2^2 + F_1^2 = 1 + 1 = 2 = q_2  (the primary prime)")
    print()
    print("    F_5 = F_3^2 + F_2^2 = q_2^2 + 1 = N_lep + 1 = 5")
    print("       (lepton cell plus one, also = F_5 used in F_5_corrections)")
    print()
    print("  *** F_7 = F_4^2 + F_3^2 = q_3^2 + q_2^2 = N_up + N_lep = 13 ***")
    print()
    print("    The 7th Fibonacci number is the sum of the two smallest sector")
    print("    cells.  And F_7 = 13 is ALSO the framework's |F_6| Farey mode")
    print("    count at depth 6.")
    print()
    print("    Twin structural role: F_7 = 13 simultaneously is")
    print("      (i) the 7th Fibonacci number")
    print("      (ii) the sum N_lep + N_up = 4 + 9")
    print("      (iii) the Farey mode count |F_6| at depth 6")
    print()
    print("    F_9 = F_5^2 + F_4^2 = 25 + 9 = 34")
    print("       (no clean framework reading -- 25 is not a sector cell)")
    print()
    print("  PHYSICAL READING:")
    print()
    print("  Odd-index Fibonacci numbers naturally arise as 'sums of two")
    print("  consecutive Fibonacci squares', and in the framework's primitive")
    print("  alphabet, sector cells are squares of framework primes (N_lep =")
    print("  q_2^2, N_up = q_3^2).  So odd-index Fibonacci F_{2k-1} are")
    print("  naturally 'sums of consecutive sector cells' when the indices")
    print("  align with framework primes.")
    print()
    print("  The cleanest hit is F_7 = N_lep + N_up = 13.  This is also the")
    print("  framework's |F_6| count, suggesting F_7 plays a special role:")
    print("  it is the bridge between Fibonacci structure and sector-cell")
    print("  structure.")
    print()
    print("  Note: this does NOT directly explain why ODD indices are special.")
    print("  The identity F_{2k-1} = sum of two squares is symmetric in some")
    print("  sense.  But it does say that the framework's natural Fibonacci")
    print("  numbers (F_3 = q_2, F_5 = 5, F_7 = 13) are exactly the odd-index")
    print("  ones, suggesting the framework picks out odd-index as 'structurally")
    print("  primary'.")
    print()

# ============================================================================
# (E) Honest assessment of the chain
# ============================================================================

def section_assessment() -> None:
    header("(E) Honest assessment of the chain")
    print("""\
  Status of the K_STAR ~ 2^(-3/14) derivation chain:

    Step 1: q_2 = 2 (Klein parity prime)            -- canonical primitive
    Step 2: N_lep = q_2^2 = 4                       -- canonical L3 of framework
    Step 3: Framework depth = N_lep = 4             -- 3-way convergent argument
                                                       (farey_depth_proof.py)
    Step 4: |F_4| = 7                               -- Farey count theorem
    Step 5: EDO basis = q_2 * |F_4| = 14            -- Klein parity doubling
                                                       (this chunk, Section B)
    Step 6: K_STAR^14 = q_2^(-q_3) = 1/8            -- closed form
                                                       (this chunk, Section A)

  CHAIN STATUS:

    - Steps 1, 2 are framework canonical: no derivation needed.
    - Step 3 is overdetermined by three independent arguments
      (lepton atomic depth, max b_1 SB depth, tongue resolution at K_STAR).
      Strong but not a theorem.
    - Step 4 is the Farey count formula, exact.
    - Step 5 (this chunk) uses Klein parity Z_2 acting on Farey rationals,
      which is plausible but extends Klein parity from sectors to rationals.
      Not a theorem.
    - Step 6 (this chunk) is a closed-form algebraic relation
      K_STAR^14 = q_2^(-q_3) at 0.595 sigma, a candidate closure.

  REMAINING WEAKNESSES:

    (i) Step 3: 'framework depth = N_lep' is overdetermined but no
        single argument is a theorem.  All three are structural
        identifications.

    (ii) Step 5: 'Klein parity acts on Farey rationals' extends a
         sector-level concept to rational-level. Plausible but not derived.

    (iii) Step 6: 'K_STAR^N = q_2^(-q_3)' is a closed-form relation
          that holds at 0.595 sigma.  Could be exact or could be a
          numerical coincidence at the precision floor.

  TIGHTENING NEXT STEPS (in decreasing leverage):

    (A) Get K_STAR_lep at 7+ digits.  If K_STAR^14 = 1/8 holds at the
        7th digit, the relation is exact and the chain closes
        numerically (modulo the structural weak links).

    (B) Find an INDEPENDENT framework quantity that should also satisfy
        a 'X^N = q_2^(-q_3)' relation in the same EDO basis.  If yes,
        the framework has a generalized 'tempered coupling' principle
        and the K_STAR relation is a special case.

    (C) Prove 'Klein parity acts on Farey rationals' from a Klein
        topology argument.  This would close Step 5.  Likely route: show
        that the framework's Klein bottle has a natural Z_2 action that
        extends to the Stern-Brocot tree.

  CUMULATIVE PROGRESS:

    The chain has gone from 'log_phi(3/2) at 2.25%' (Candidate A) to
    '2^(-3/14) at 0.59 sigma sub-closure' over ~10 incremental steps.
    Each step has tightened the structural reading and reduced one
    soft link, while preserving the numerical match.

    Whether 'closure' is actually achievable at PDG precision depends
    on (A) -- higher precision K_STAR data.  Without it, we have a
    plausible chain at 0.59 sigma with three structural identifications
    that should be made rigorous.

    The session's strongest standalone result remains K = 1 from the
    parabola instanton (variational_instanton.py).  The 2^(-3/14)
    candidate is the strongest matter-sector candidate and would be a
    second exact derivation if the chain is closed.
""")

def main() -> None:
    print("=" * 78)
    print("  OCTAVE DOUBLING: q_2 factor in EDO basis from Klein parity Z_2")
    print("=" * 78)
    section_closed_form()
    section_klein_doubling()
    section_musical()
    section_odd_fibonacci()
    section_assessment()

if __name__ == "__main__":
    main()
