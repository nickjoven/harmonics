"""
deriving_14.py

Derive the 14 in the K_STAR ~ 2^(-3/14) candidate from a structural
chain that connects framework primitives to the EDO denominator.

The candidate from string_nodes_and_pitches.py:

    K_STAR ~= 2^(-3/14) = 0.8619728212
    K_STAR_lep            = 0.8619605700 +/- 2.06e-5
    gap                   = +1.225e-5  (0.59 sigma -- sub-sigma closure)

The numerator 3 is clean: 3 = q_3 (framework prime).  The denominator
14 is the load-bearing question: where does it come from structurally?

This script proposes a chain from framework primitives:

  Step 1: Klein parity is Z_2; |Z_2| = q_2 = 2.
  Step 2: Lepton sector has |Z_2 x Z_2| = q_2^2 = 4 phase states (= N_lep).
  Step 3: Framework's natural Farey depth equals N_lep = 4
          (the lepton sector sets the framework's atomic resolution).
  Step 4: At Farey depth 4, the Farey count is |F_4| = 7.
  Step 5: The natural EDO basis is octave-doubled Farey count:
          q_2 * |F_4| = 2 * 7 = 14.
  Step 6: K_STAR = 2^(-q_3 / (q_2 * |F_4|)) = 2^(-3/14).

Each step has framework justification, but step 3 is the load-bearing
identification: 'framework depth = lepton phase count'.  The reason
is structural:

  - N_lep = 4 is the SMALLEST sector cell.
  - Smallest cell = highest resolution = sets the framework's atomic
    Farey depth.
  - Up and down sectors live at coarser scales (N = 9, 24) but are
    constrained to be CONSISTENT with the lepton scale.
  - Therefore the framework's primary Farey resolution is at depth
    N_lep = 4.

Tongue-width consistency check: at K_STAR ~ 0.862, the leading-order
tongue widths are

    q=1: width ~ 0.86  (visible)
    q=2: width ~ 0.19  (visible)
    q=3: width ~ 0.018 (visible, ~Pythagorean comma scale)
    q=4: width ~ 0.001 (borderline)
    q=5: width ~ 3e-5  (invisible)

The threshold q* between visible and invisible at K_STAR is 3-4.
Consistent with depth 4 as the framework's natural depth, but not
uniquely determined by it.

Status: PARTIAL DERIVATION.  The chain is plausible and uses only
framework primitives, but step 3 is an identification rather than
a derivation.  The numerical result 2^(-3/14) at 0.59 sigma stands
either way as the tightest K_STAR candidate of the session.
"""

from __future__ import annotations

import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))

import math

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
# Step-by-step derivation
# ============================================================================

def step_1() -> None:
    print("  STEP 1: Klein parity is Z_2; |Z_2| = q_2 = 2")
    print()
    print("    Framework primitive: q_2 = 2 is the Klein bottle's")
    print("    orientation reversal generator.  |Z_2| = 2 = q_2.")
    print()

def step_2() -> None:
    print("  STEP 2: Lepton phase count = q_2^2 = 4")
    print()
    print("    The lepton sector has |Z_2 x Z_2| = q_2^2 = 4 distinct")
    print("    phase states.  This is canonical from L3 of the framework")
    print("    topology: N_lep = q_2^2 = 4.")
    print()
    N_lep = Q2 ** 2
    print(f"    N_lep = q_2^2 = {Q2}^2 = {N_lep}")
    print()

def step_3() -> None:
    print("  STEP 3: Framework's natural Farey depth = N_lep = 4")
    print()
    print("    *** This is the load-bearing structural identification. ***")
    print()
    print("    The lepton sector has the smallest integer cell (N_lep = 4),")
    print("    so its phase count sets the highest atomic resolution the")
    print("    framework can resolve.  The up and down sectors (N = 9, 24)")
    print("    live at coarser scales but are constrained to be consistent")
    print("    with the lepton scale.")
    print()
    print("    Therefore the framework's primary Farey depth -- the depth at")
    print("    which all matter-sector content must be hosted -- is N_lep.")
    print()
    print("    Justification: any matter-sector quantity must be expressible")
    print("    at the lepton's resolution.  Below depth 4, the lepton sector")
    print("    cannot be distinguished (its natural rational 1/N_lep = 1/4")
    print("    first appears in F_4 but not in F_1, F_2, F_3).")
    print()
    print("    Framework depth = 4")
    print()

def step_4() -> None:
    print("  STEP 4: Farey count at depth 4 = |F_4| = 7")
    print()
    print("    The Farey sequence F_n contains all reduced rationals p/q")
    print("    with q <= n in [0, 1].  |F_n| = 1 + sum_{k=1}^n phi(k).")
    print()
    print(f"    {'n':<4}  {'|F_n|':<8}  contents")
    for n in range(1, 8):
        count = farey_count(n)
        contents_examples = []
        for q in range(1, n + 1):
            for p in range(0, q + 1):
                if math.gcd(p, q) == 1:
                    contents_examples.append(f"{p}/{q}")
        contents_str = ", ".join(sorted(set(contents_examples), key=lambda x: float(eval(x))))
        if len(contents_str) > 50:
            contents_str = contents_str[:47] + "..."
        marker = "  <<" if n == 4 else ""
        print(f"    {n:<4}  {count:<8}  {{{contents_str}}}{marker}")
    print()
    print("    |F_4| = 7  (the Farey count at depth N_lep)")
    print()

def step_5() -> None:
    print("  STEP 5: Natural EDO basis = q_2 * |F_4| = 14")
    print()
    print("    In music theory, equal temperament divides an OCTAVE")
    print("    (factor q_2 = 2) into n equal parts.  The natural EDO basis")
    print("    for a system at Farey depth d is:")
    print()
    print("        EDO_basis = q_2 * |F_d|")
    print()
    print("    The factor q_2 reflects that we're dividing the OCTAVE,")
    print("    which is a factor-of-q_2 interval.  The |F_d| reflects the")
    print("    framework's resolution at depth d.")
    print()
    print("    For framework depth d = 4:")
    print()
    print(f"        EDO_basis = q_2 * |F_4| = {Q2} * {farey_count(4)} = {Q2 * farey_count(4)}")
    print()

def step_6() -> None:
    print("  STEP 6: K_STAR = 2^(-q_3 / (q_2 * |F_4|)) = 2^(-3/14)")
    print()
    print("    The framework's K_STAR is the EDO step at index -q_3.")
    print("    Why -q_3?  Because q_3 is the OTHER framework prime, and")
    print("    K_STAR represents the matter-sector compromise between q_2")
    print("    and q_3 iteration (the Pythagorean comma is at the framework's")
    print("    natural depth, see low_index_structure.py).")
    print()
    print("    K_STAR = 2^(-q_3 / (q_2 * |F_4|))")
    print(f"           = 2^(-{Q3} / ({Q2} * {farey_count(4)}))")
    print(f"           = 2^(-{Q3}/{Q2 * farey_count(4)})")
    print(f"           = 2^(-3/14)")
    print()
    val = 2 ** (-Q3 / (Q2 * farey_count(4)))
    print(f"    Numerical value: 2^(-3/14) = {val:.10f}")
    print()

# ============================================================================
# Verification
# ============================================================================

def verification() -> None:
    header("Verification: comparison to K_STAR_lep")
    val = 2 ** (-Q3 / (Q2 * farey_count(4)))
    K_lep = 0.86196057
    sigma = 2.06e-5
    gap = val - K_lep
    nsigma = abs(gap) / sigma
    print(f"  predicted K = 2^(-3/14)        = {val:.10f}")
    print(f"  K_STAR (joint canonical)       = {K_STAR:.10f}")
    print(f"  K_STAR_lep (lepton-only fit)   = {K_lep:.10f} +/- {sigma:.2e}")
    print()
    print(f"  predicted - K_STAR_lep         = {gap:+.6e}")
    print(f"  in sigma units                 = {nsigma:.3f}")
    print()
    if nsigma < 1.0:
        print("  *** Within 1 sigma of K_STAR_lep -- candidate closure ***")
    print()

def consistency_check() -> None:
    header("Consistency check: tongue widths at K_STAR")
    print("  Leading-order Arnold tongue width: W(q, K) ~ K^q / (q!)^2")
    print()
    K = K_STAR
    print(f"  At K = K_STAR = {K_STAR}:")
    print()
    print(f"    {'q':<4}  {'K^q':<14}  {'width':<14}  {'visible?':<12}")
    print("    " + "-" * 50)
    for q in range(1, 8):
        Kq = K ** q
        width = Kq / math.factorial(q) ** 2
        visible = "visible" if width > 1e-3 else "negligible"
        marker = "  <-- depth 4" if q == 4 else ""
        print(f"    {q:<4}  {Kq:<14.4e}  {width:<14.4e}  {visible:<12}{marker}")
    print()
    print("  The threshold between 'visible' (width > 0.001) and 'negligible'")
    print("  is at q = 4 (borderline) or q = 5 (clearly invisible).  This is")
    print("  consistent with the framework operating at depth 4, but does not")
    print("  uniquely determine K_STAR (any K in roughly [0.85, 0.87] gives")
    print("  the same q*).")
    print()
    print("  Reading: the depth-4 identification is consistent with the")
    print("  tongue-width threshold but is not derived from it.  The")
    print("  derivation chain depends on step 3 (framework depth = N_lep),")
    print("  which is structural identification, not first-principles.")
    print()

# ============================================================================
# Honest assessment
# ============================================================================

def assessment() -> None:
    header("Honest assessment: what this derivation does and doesn't do")
    print("""\
  WHAT IT DOES:

    1. Provides a structural chain from framework primitives
       {q_2, q_3, Klein parity, N_lep} to the candidate K_STAR
       expression 2^(-3/14).

    2. Each step uses only framework alphabet:
       - q_2 = 2 (Klein parity generator)
       - q_3 = 3 (other framework prime)
       - N_lep = q_2^2 = 4 (lepton phase count)
       - |F_4| = 7 (Farey count at depth N_lep)

    3. Yields the closest K_STAR candidate of the session (0.59 sigma),
       structurally derived rather than fit.

    4. Provides a physical reading of K_STAR: it is the q_3 step in
       the framework's natural EDO temperament, where the EDO basis
       is q_2 * |F_(N_lep)| = 14.

  WHAT IT DOESN'T DO:

    1. STEP 3 is the load-bearing identification ('framework depth =
       N_lep') and is justified by 'lepton has smallest cell' -- this
       is plausible structural reasoning but not a theorem.

    2. The derivation does not explain WHY the natural EDO basis is
       q_2 * |F_d| (with the specific octave-doubling factor q_2)
       rather than just |F_d|, or some other multiplier.  In music,
       the q_2 factor reflects the octave structure, but in the
       framework it is an analogy.

    3. The 0.59 sigma residual is real.  If the chain is exactly
       correct, K_STAR_lep should match 2^(-3/14) at higher precision.
       Whether it does requires K_STAR at 7+ digits of precision.

    4. The Pythagorean comma derivation from low_index_structure.py
       (3^12 / 2^19, exponents both framework alphabet) is independent
       of this chain and may be a stronger structural fact.

  STATUS:

    PARTIAL DERIVATION at 0.59 sigma sub-closure.  Stronger than
    'observation', weaker than 'theorem'.  The chain is consistent
    with all framework constraints but contains one identification
    (step 3) that should be made rigorous before claiming closure.

  TIGHTENING NEXT STEPS:

    (i) Prove that 'framework Farey depth = N_lep' from a Klein-
        topology argument or a tongue-resolution argument.

    (ii) Get K_STAR_lep at 7+ digits of precision and check whether
         2^(-3/14) holds at that level.

    (iii) Find an INDEPENDENT framework quantity that should be
          q_2 * |F_d|-EDO-tempered, and check whether it lands at
          the predicted value.  If yes, the chain is corroborated.
""")

def main() -> None:
    print("=" * 78)
    print("  DERIVING 14: structural chain for K_STAR ~ 2^(-3/14)")
    print("=" * 78)
    header("Derivation chain (framework primitives -> 14)")
    step_1()
    step_2()
    step_3()
    step_4()
    step_5()
    step_6()
    verification()
    consistency_check()
    assessment()

if __name__ == "__main__":
    main()
