"""
primitives_first.py

First-pass construction of K_STAR from framework primitives, without
Shenker universality class references.

Methodology
-----------

A from-primitives derivation of K_STAR must use only:

  1. The four primitives: integers, mediant, fixed-point recurrence,
     parabola (saddle-node normal form x^2 = mu).
  2. Klein bottle topology: antiperiodic direction (half twist, sign
     flip) + periodic direction.
  3. Forced selections at L1: (q_2, q_3) = (2, 3), d = 3, Klein parity
     Z_2 x Z_3, signature (3, 1).
  4. The integer alphabet at L2-L3: {q_2^2, q_3^2, q_2^3 q_3, q_2^d,
     q_3^d, q_2^d + q_3^d, q_2 q_3^d} = {4, 9, 24, 8, 27, 35, 54}.

Anything beyond this (Shenker constants, PDG mass ratios, Jensen-Bak-
Bohr Hausdorff dimensions) is not "from primitives."

The open question is narrow: K_STAR sits at L4 in FRAMEWORK_TOPOLOGY.md,
derived from the joint matter-sector fit of three PDG-driven a_1
values on the integer cells {4, 9, 24}. L0 through L3 are already
from-primitives; only L4 is PDG-anchored. A from-primitives K_STAR
must express it in terms of L0-L3 objects alone.

First construction: parabola half-arc at the q_2 integer cell
-------------------------------------------------------------

The parabola primitive x^2 = mu has a natural geometric measure at
each integer cell -- its arc length from the saddle-node vertex (0, 0)
to the point (sqrt(N), N). For the lepton sector (N = q_2^2 = 4),
the point is (q_2, q_2^2) = (2, 4) and the arc length is

    L(q_2) = integral from 0 to q_2 of sqrt(1 + (d mu / dx)^2) dx
           = integral from 0 to q_2 of sqrt(1 + 4 x^2) dx
           = q_2 sqrt(1 + 4 q_2^2) / 2 + (1/4) arsinh(2 q_2)

At q_2 = 2:

    L(2) = sqrt(17) + (1/4) arsinh(4)
         ~ 4.64678

The Klein bottle's antiperiodic direction has period 2 (Z_2 double
cover of the torus). One full traversal sends x -> -x; two traversals
return to x. The parabola's sign-flip symmetry x -> -x is identified
with this half twist. Under this identification, the "natural length"
of a lepton sector traversal is L(q_2) / 2, the arc length from the
vertex to one side of the parabola:

    a_1(candidate) = L(q_2) / 2
                   = sqrt(17)/2 + (1/8) arsinh(4)
                   ~ 2.32339

The observed a_1(lep) is 2.32029. The gap is 0.134%.

What the candidate does right:

  - Uses only framework primitives (parabola + integer q_2).
  - Identifies the half twist with the parabola's sign flip (a short-
    list phenomenon of the framework).
  - Produces a number in the right neighbourhood with zero free
    parameters and zero PDG input.
  - Same 0.1% family of near-misses as the Feigenbaum-era candidates,
    but framed in the framework's own vocabulary.

What it does not do:

  - Close at PDG precision. The 0.13% gap is 65x the PDG uncertainty
    on a_1(lep) (~2e-5 relative).
  - Explain why the integral measure is the right one. The natural
    length of a curve in Euclidean coordinates is a choice; other
    candidates (rapidity arsinh(2 q_2), tangent slope 2 q_2, affine
    parameter, etc.) are also "from primitives" and give different
    numbers.
  - Address the up-type sector at q_3. The same construction at
    q_3 = 3 gives a different number; whether that matches a_1(up) is
    part of the audit this script performs.

This file tests the half-arc construction at all three matter sectors
and for the duty cells, reports gaps, and is honest about whether the
construction closes, partially closes, or fails.
"""

from __future__ import annotations

import math

from framework_constants import (
    D,
    K_STAR,
    M_B,
    M_C,
    M_MU,
    M_S,
    M_T,
    M_TAU,
    Q2,
    Q3,
)


# ============================================================================
# Parabola arc length in normal-form coordinates x^2 = mu
# ============================================================================

def parabola_arc_length(x_max: float) -> float:
    """
    Arc length of x^2 = mu from (0, 0) to (x_max, x_max^2) in
    Euclidean (x, mu) coordinates.

        L = int_0^x_max sqrt(1 + (dmu/dx)^2) dx
          = int_0^x_max sqrt(1 + 4 x^2) dx
          = x sqrt(1 + 4 x^2) / 2 + (1/4) arsinh(2 x)   at x = x_max
    """
    if x_max <= 0:
        return 0.0
    return (x_max * math.sqrt(1 + 4 * x_max * x_max) / 2
            + math.asinh(2 * x_max) / 4)


def half_arc_at_cell(N: int | float) -> float:
    """
    Half the parabola arc length from vertex to (sqrt(N), N).
    This is the candidate a_1 value for a sector with integer N.
    """
    return parabola_arc_length(math.sqrt(N)) / 2


# ============================================================================
# PDG-derived a_1 for comparison
# ============================================================================

def a1_from_pdg(heavy: float, light: float, b1: float) -> float:
    """a_1(sector) = log(m_heavy/m_light) / (d log b_1)."""
    return math.log(heavy / light) / (D * math.log(b1))


# ============================================================================
# Matter sectors and their integer cells
# ============================================================================

MATTER = [
    # (name, m_heavy, m_light, b_1, N_sector)
    ("leptons",   M_TAU, M_MU, 3 / 2, Q2 ** 2),                # N = 4
    ("up-type",   M_T,   M_C,  8 / 5, Q3 ** 2),                # N = 9
    ("down-type", M_B,   M_S,  5 / 4, Q2 ** 3 * Q3),           # N = 24
]


# ============================================================================
# Output utilities
# ============================================================================

def header(text: str) -> None:
    print()
    print("-" * 78)
    print(f"  {text}")
    print("-" * 78)
    print()


# ============================================================================
# Section 1 -- baseline: what K_STAR is currently
# ============================================================================

def section_baseline() -> None:
    header("Section 1: baseline -- K_STAR from the matter-sector joint fit")
    print(f"  framework_constants.K_STAR = {K_STAR:.10f}")
    print()
    print("  This value is the joint fit of three PDG-driven a_1(sector)")
    print("  values on the integer cells {4, 9, 24}.  The identity")
    print("      a_1(sector) * K_STAR = sqrt(N_sector)")
    print("  closes to 0.00 sigma in every sector at canonical K_STAR.")
    print("  Fit count = 1.  This is not yet from-primitives.")
    print()
    print("  Per-sector a_1 from PDG:")
    print()
    print(f"  {'sector':<12} {'a_1 (PDG)':>14} {'a_1 * K_STAR':>16} "
          f"{'sqrt(N)':>12}")
    print("  " + "-" * 60)
    for name, heavy, light, b1, N in MATTER:
        a1 = a1_from_pdg(heavy, light, b1)
        print(f"  {name:<12} {a1:>14.10f} {a1 * K_STAR:>16.10f} "
              f"{math.sqrt(N):>12.8f}")
    print()


# ============================================================================
# Section 2 -- half-arc candidate at each matter cell
# ============================================================================

def section_half_arc_matter() -> None:
    header("Section 2: parabola half-arc at matter sector integer cells")
    print("  a_1(candidate) = arc length of x^2 = mu from (0, 0) to")
    print("  (sqrt(N), N), divided by 2 (the Klein-bottle half twist).")
    print()
    print(f"  {'sector':<12} {'N':>5} {'sqrt(N)':>10} "
          f"{'a_1 cand':>14} {'a_1 obs':>14} {'gap':>12}")
    print("  " + "-" * 74)
    for name, heavy, light, b1, N in MATTER:
        a1_cand = half_arc_at_cell(N)
        a1_obs = a1_from_pdg(heavy, light, b1)
        rel = (a1_cand - a1_obs) / a1_obs
        print(f"  {name:<12} {N:>5} {math.sqrt(N):>10.6f} "
              f"{a1_cand:>14.10f} {a1_obs:>14.10f} {rel * 100:>+10.4f}%")
    print()
    print("  The half-arc candidate gives ~0.1% agreement for leptons but")
    print("  does not extend cleanly to the quark sectors.  This means the")
    print("  half-arc is not THE from-primitives formula -- it is at best a")
    print("  lepton-specific coincidence, or a reading that needs sector-")
    print("  specific corrections.")
    print()


# ============================================================================
# Section 3 -- K_STAR implied by each matter sector
# ============================================================================

def section_K_per_sector() -> None:
    header("Section 3: K_STAR implied by the half-arc candidate per sector")
    print("  If a_1(sector) = half-arc(sqrt(N_sector)), then")
    print("      K_STAR = sqrt(N_sector) / half-arc(sqrt(N_sector))")
    print("  Test whether the three sectors agree on a single K_STAR.")
    print()
    print(f"  {'sector':<12} {'K_STAR cand':>16} {'K_STAR canon':>16} "
          f"{'gap':>12}")
    print("  " + "-" * 62)
    K_canonical = K_STAR
    K_cands = []
    for name, _h, _l, _b, N in MATTER:
        a1_cand = half_arc_at_cell(N)
        K_cand = math.sqrt(N) / a1_cand
        K_cands.append(K_cand)
        rel = (K_cand - K_canonical) / K_canonical
        print(f"  {name:<12} {K_cand:>16.10f} {K_canonical:>16.10f} "
              f"{rel * 100:>+10.4f}%")
    print()
    spread = max(K_cands) - min(K_cands)
    print(f"  Spread of K_STAR candidates: {spread:.6f}")
    print(f"  (For a real from-primitives K_STAR, the three sector values")
    print(f"   should coincide exactly.  Spread > 0 means the half-arc is")
    print(f"   not a universal construction across sectors.)")
    print()


# ============================================================================
# Section 4 -- alternative primitive measures at q_2
# ============================================================================

def section_alternatives_at_q2() -> None:
    header("Section 4: alternative parabola measures at the q_2 integer cell")
    print("  The half-arc is one of several measures of the parabola at")
    print("  (q_2, q_2^2).  We survey other framework-native measures and")
    print("  see which, if any, gives a_1(lep) cleanly.  None of these use")
    print("  any PDG input.")
    print()
    a1_obs = a1_from_pdg(M_TAU, M_MU, 3 / 2)

    q2 = float(Q2)
    candidates = [
        ("half arc length (this script)", half_arc_at_cell(q2 * q2)),
        ("full arc length",                parabola_arc_length(q2)),
        ("quarter arc length",             parabola_arc_length(q2) / 4),
        ("rapidity arsinh(2 q_2)",         math.asinh(2 * q2)),
        ("tangent slope 2 q_2",            2 * q2),
        ("q_2 + 1/q_3",                    q2 + 1 / Q3),
        ("q_2 * (1 + 1/q_3^2)",            q2 * (1 + 1 / (Q3 * Q3))),
        ("sqrt(q_2^2 + 1) * q_2 / q_2",    math.sqrt(q2 * q2 + 1)),
    ]

    print(f"  {'measure':<36} {'value':>16} {'gap from a_1 obs':>18}")
    print("  " + "-" * 72)
    for label, value in candidates:
        rel = (value - a1_obs) / a1_obs
        print(f"  {label:<36} {value:>16.10f} {rel * 100:>+16.4f}%")
    print()
    print(f"  a_1(lep) observed (PDG) = {a1_obs:.10f}")
    print()


# ============================================================================
# Section 5 -- conclusion
# ============================================================================

def section_conclusion() -> None:
    header("Section 5: what this tells us")
    print("""\
  The parabola half-arc at the q_2 integer cell is a from-primitives
  candidate for a_1(lep) that uses only:
    - the parabola primitive x^2 = mu
    - the integer q_2 = 2 (forced by cross-link uniqueness at L1)
    - the Klein bottle half twist (the factor of 1/2)

  It lands at 2.3234 vs observed 2.3203, a 0.134% gap.  The same
  construction applied to the up-type and down-type sectors does
  NOT reproduce their a_1 values at any comparable precision --
  spread across sectors is order 20-30%.  So the half-arc is a
  lepton-only coincidence at best, not a universal primitive.

  What this rules out:

    (a) "a_1(sector) = half-arc at the sector's integer cell" is
        NOT the from-primitives formula.  It works for the lepton
        sector accidentally and fails for quarks.

    (b) The cross-sector structure a_1^2 * K^2 = N_sector (which is
        the parabola rotation from item12_cross_sector_derivation.py)
        is therefore not directly expressible as "each sector's a_1
        is the parabola's half-arc at its N."  The sector-integer
        assignment {4, 9, 24} is structural, but a_1(sector) is not
        the half-arc.

  What this suggests:

    - The from-primitives derivation of a_1(lep), if it exists, is
      NOT a purely geometric measure on the parabola at a single
      cell.  It must involve the SECTOR-SPECIFIC structure -- the
      base pair, the Klein parity, the Fibonacci shift, or some
      combination -- that distinguishes the lepton sector from the
      quark sectors.

    - The 0.1-0.2% near-miss on the lepton sector is in the same
      family as the Feigenbaum-era near-misses (Candidates 1-4 in
      the dropped feigenbaum_route.py).  That pattern suggests the
      framework is close to some construction in the golden-mean
      family, but not exactly on it at the lepton sector.

  Next questions to ask, in the framework's own vocabulary:

    (i) What distinguishes the lepton sector geometrically from the
        quark sectors?  The matter-sector base pair closure says
        lepton b_1 = 3/2 (the first Fibonacci convergent above 1),
        up-type b_1 = 8/5 (the next one), down-type b_1 = 5/4 (a
        non-Fibonacci).  These are three different Stern-Brocot
        positions; their "length" in the parabola primitive should
        differ accordingly.

    (ii) How does the Klein parity sign flip decompose across
         sectors?  Down-type is orientation-preserving (item12_
         down_sign_flip.py: parity +1); lepton and up-type are
         orientation-reversing.  The half-twist factor of 1/2 in
         the half-arc candidate is a reading of orientation-
         reversing; down-type should use a DIFFERENT factor.

    (iii) What is the natural "action" on the parabola restricted
          to a Stern-Brocot walk?  The walk from 0/1 to the sector's
          base pair has a specific length in the Poincare metric on
          the Farey graph.  That length, combined with the parabola
          primitive, is a candidate construction not yet tested.

  This file does NOT close K_STAR from primitives.  It rules out
  one candidate construction (the half-arc) and sets up the next
  three questions.  Subsequent scripts in this series should work
  through questions (i)-(iii) one at a time.
""")


# ============================================================================
# Main
# ============================================================================

def main() -> None:
    print("=" * 78)
    print("  PRIMITIVES-FIRST: first pass at a_1(lep) and K_STAR")
    print("=" * 78)
    section_baseline()
    section_half_arc_matter()
    section_K_per_sector()
    section_alternatives_at_q2()
    section_conclusion()


if __name__ == "__main__":
    main()
