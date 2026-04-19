"""
down_type_dof_monodromy.py

Extract the primitive-walk count on K² and T² using the Klein
connection's Z₂ monodromy (klein_connection.md Step 2).

Target: justify DoF(K²) = 1 required by Phase C (halt C1).

Approach:
  - On T²: walks at tongue (p_x/q_x, p_y/q_y) visit q_x·q_y discrete
    orbit-start points.
  - On K²: the Klein Z₂ monodromy (−1 per x-loop) couples closure to
    x-winding parity. Walks with odd p_x do NOT close on K² in one
    period; they require the T² lift.
  - Compute the walk count on each surface for each sector base pair.
"""

from fractions import Fraction
from math import gcd, lcm


SECTORS = {
    'lepton':   (Fraction(3, 2), Fraction(5, 3)),
    'up-type':  (Fraction(8, 5), Fraction(3, 2)),
    'down-type': (Fraction(5, 4), Fraction(9, 8)),
}

# Klein bottle cycle lengths (the framework integers, not base-pair denoms)
Q2, Q3 = 2, 3


def klein_parity(pair):
    q1 = pair[0].denominator
    q2 = pair[1].denominator
    odd = sum(1 for q in (q1, q2) if q % 2 == 1)
    return (-1) ** odd


def x_winding_parity(pair):
    """Numerator parity of the first base-pair element = x-winding mod 2."""
    return pair[0].numerator % 2


def t2_walk_count(pair):
    """
    On T² the walk at (p_x/q_x, p_y/q_y) fills a q_x × q_y lattice of
    orbit-start points.  With the orientable lift's doubled x-cycle
    (length 2q_2 projecting to K²'s q_2), the effective count per
    K²-fiber is q_x · q_y / gcd with the surface lattice:
    """
    qx = pair[0].denominator
    qy = pair[1].denominator
    # Discrete orbit-starts on T² before surface normalization
    return qx * qy


def k2_walk_count_via_monodromy(pair):
    """
    On K² the Z_2 monodromy identifies points (x, y) ~ (x + L_x, L_y − y).
    For a walk at (p_x/q_x, p_y/q_y), the monodromy action on orbit-start
    points is free if and only if there are no fixed lattice points
    under y → q_y − y.  Fixed: y = q_y/2 (lattice point iff q_y even).

    If the action is free, K² count = T² count / 2.
    If fixed points exist, they don't get identified, so
    K² count = (paired lattice points)/2 + (fixed points)
            = (q_x·q_y − f)/2 + f  where f = q_x (one per x-position if q_y even)
            = q_x · (q_y + [q_y even]) / 2
    """
    qx = pair[0].denominator
    qy = pair[1].denominator
    t2 = t2_walk_count(pair)
    if qy % 2 == 0:
        # y-lattice has a fixed point at q_y/2; count q_x fixed starts
        f = qx
    else:
        f = 0
    return (t2 - f) // 2 + f


def primitive_closure_on_k2(pair):
    """
    Does the walk close on K² in one period?  Requires monodromy = 1,
    i.e., (-1)^(p_x · number_of_x_loops) = 1 after one walk period.
    A walk at (p_x/q_x, p_y/q_y) has x-winding = p_x per period.
    Closure: p_x must be EVEN for the walk to close on K² alone.
    """
    return x_winding_parity(pair) == 0


def main():
    print("=" * 72)
    print("  PHASE C HALT C1: monodromy extraction")
    print("=" * 72)
    print()
    print(f"Klein cycle lengths: q_2 = {Q2}, q_3 = {Q3}")
    print()

    header = f"  {'sector':<10} {'base pair':<14} {'denoms':<8} {'p_x':>4} {'p_x parity':>11} {'K² closes?':>12}"
    print(header)
    print("  " + "-" * (len(header) - 2))
    for name, pair in SECTORS.items():
        q = (pair[0].denominator, pair[1].denominator)
        p_x = pair[0].numerator
        closes = "yes" if primitive_closure_on_k2(pair) else "no (needs T²)"
        print(f"  {name:<10} ({pair[0]},{pair[1]})  {str(q):<8} {p_x:>4} {p_x % 2:>11} {closes:>12}")
    print()

    print("-" * 72)
    print("  Observation on p_x parity")
    print("-" * 72)
    print("""
  All three sectors have ODD p_x:
    lepton    b_1 = 3/2  -> p_x = 3
    up-type   b_1 = 8/5  -> p_x = 8 (EVEN)  -- wait, check
    down-type b_1 = 5/4  -> p_x = 5

  So the "closes on K² iff p_x even" reading is wrong --
  up-type has p_x = 8 (even), lepton p_x = 3 (odd),
  down-type p_x = 5 (odd).  This does NOT align with Klein
  parity (lepton & up-type = -1, down-type = +1).

  The correct monodromy-based split uses DENOMINATOR parity
  (item12_down_sign_flip.py), not numerator:
""")

    header2 = f"  {'sector':<10} {'(q_x, q_y)':<12} {'# odd q':>8} {'parity':>8} {'Klein class':>14}"
    print(header2)
    print("  " + "-" * (len(header2) - 2))
    for name, pair in SECTORS.items():
        qx, qy = pair[0].denominator, pair[1].denominator
        n_odd = (qx % 2) + (qy % 2)
        par = (-1) ** n_odd
        cls = "K²" if par == -1 else "T² (lifted)"
        print(f"  {name:<10} ({qx}, {qy}){'':<{max(0, 12-len(f'({qx}, {qy})'))}} "
              f"{n_odd:>8} {par:>+8d} {cls:>14}")
    print()

    print("-" * 72)
    print("  Discrete walk counts per surface")
    print("-" * 72)
    print()
    print(f"  {'sector':<10} {'T² count':>10} {'K² count':>10} {'K² fix-pts':>12} {'ratio T²/K²':>14}")
    print("  " + "-" * 60)
    for name, pair in SECTORS.items():
        t2 = t2_walk_count(pair)
        k2 = k2_walk_count_via_monodromy(pair)
        qy = pair[1].denominator
        fp = pair[0].denominator if qy % 2 == 0 else 0
        ratio = t2 / k2 if k2 else float('inf')
        print(f"  {name:<10} {t2:>10} {k2:>10} {fp:>12} {ratio:>14.4f}")
    print()

    print("-" * 72)
    print("  Comparison to target ratio q_2·q_3 = 6")
    print("-" * 72)
    print()
    print("  For down-type: T² count / K² count =",
          f"{t2_walk_count(SECTORS['down-type'])}/"
          f"{k2_walk_count_via_monodromy(SECTORS['down-type'])} =",
          t2_walk_count(SECTORS['down-type']) /
          k2_walk_count_via_monodromy(SECTORS['down-type']))
    print()
    print("  The discrete walk count is a PER-BASE-PAIR quantity.  The")
    print("  Phase C target is a SURFACE-LEVEL ratio at fixed cycle")
    print("  lengths (q_2, q_3) = (2, 3), independent of the specific")
    print("  base pair.  Using the surface's own cycle lengths:")
    print()
    print(f"    T² surface count: q_2 · q_3 = {Q2 * Q3}")
    print(f"    K² surface count via free-monodromy quotient: {Q2 * Q3 // 2} "
          f"(Z_2 acts freely since q_3 = 3 is odd)")
    print(f"    ratio = {Q2 * Q3 / (Q2 * Q3 / 2)}")
    print()
    print("  **This is ratio 2, not 6.**")
    print()
    print("  For ratio 6 we need K²-count = 1, not q_2·q_3/2 = 3.")
    print()

    print("=" * 72)
    print("  WHERE THIS LEAVES PHASE C")
    print("=" * 72)
    print("""
  The monodromy extraction from klein_connection.md gives:
    - T² walk count at cycle lengths (q_2, q_3) = q_2 · q_3 = 6
    - K² walk count via the Z_2 free quotient = q_2 · q_3 / 2 = 3
    - Ratio = 2

  Phase C's claimed DoF(K²) = 1 requires an ADDITIONAL factor-3
  reduction from 3 down to 1.  This factor of 3 = q_3 is not
  supplied by pure topology (the Z_2 monodromy is fully accounted
  for by the /2 quotient above).  A second reduction mechanism is
  missing.

  Candidate mechanisms for the missing factor-3:

  1. Commensurability condition.  The y-direction walk closes on
     K² only at lattice points compatible with the Klein flip
     y -> q_3 - y.  For q_3 = 3 (odd), the flip has NO fixed
     lattice points -- all three y-positions pair up with
     non-existent mirror positions, forcing the walk to traverse
     a SINGLE y-orbit representative rather than three.  This
     collapse from q_3 = 3 y-positions to 1 effective y-orbit is
     the missing factor.  But the collapse is dynamical (depends
     on what "walk closes" means operationally), not purely
     topological.

  2. Klein-flip self-consistency.  Perhaps the walk must be
     COMPATIBLE with the Klein flip at both endpoints, giving a
     constraint that kills all but one of the q_3 y-representatives.
     This would be a "self-consistent boundary" reading per the
     user's suggestion and boundary_weight.md's precedent (topology
     gives the interval, dynamics give the point).

  3. Partial locking / interpolation.  The true K² count may not
     be an integer but a self-consistent weight w* in (1, 3), with
     the PDG-compatible value w* = 1 corresponding to the observed
     down-type factor 6.  At other K* values the factor would
     depart from 6.  This is the exact boundary_weight.md shape.

  Status of halt C1:
    - Pure topology: insufficient (gives ratio 2).
    - Topology + Z_2-free-quotient: insufficient (gives ratio 2).
    - Topology + Klein-flip commensurability (q_3 odd): plausibly
      sufficient but requires operational definition of closure.
    - Partial-locking self-consistency: the boundary_weight.md
      analog that would close the derivation.

  The walk-dynamics route (Phase B follow-up, Route 3) remains
  the right framing.  The specific next step is to operationalize
  "Klein-flip commensurability for odd q_3" as either a closure
  theorem or a self-consistency fixed point.
""")


if __name__ == "__main__":
    main()
