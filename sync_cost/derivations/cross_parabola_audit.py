"""
cross_parabola_audit.py

Audit of the proposed K*↔d cross-parabola self-consistency closure.

Proposal (from the four-rotations / d-audit conversation): find (K*, d)
such that the matter cells

    N_matter = {q_2^2, q_3^2, q_2^3 q_3} = {4, 9, 24}

(d-independent, from reading D + Klein parity) and the duty cells

    N_duty = {q_2^d, q_3^d, q_2^d + q_3^d, q_2 q_3^d} = {8, 27, 35, 54}
                (at d = 3)

(d-dependent, from duty_cycle_dictionary.md / duty_dimension_proof.md)
jointly populate the parabola x^2 = N.  Hope: the unique (K*, d) is
(0.86196052, 3), giving K* without consuming PDG.

This script numerically tests the proposal and confirms that it does not
constrain K*:

  Section 1.  Matter cells at K = K_STAR.  Reproduces the PDG-driven
              joint matter-sector closure (item12_K_star_closure.py).
              x^2 = N within PDG; K_STAR was set by this fit.

  Section 2.  Duty cells under the K = 1 critical reading, where
              x = sqrt(N) is built in.  Residuals are identically zero
              by construction; K does not appear.  Zero gradient on K.

  Section 3.  Duty cells off-critical at K = K_STAR under three
              candidate K-dependent readings.  None of the readings
              gives x^2 = N for the duty cells at the canonical K*.

  Section 4.  K-scan: for the simplest off-critical reading, find the K
              that zeros each duty cell's residual independently.  The
              four K's differ from each other and none equals K_STAR.

  Section 5.  Conclusion: the cross-parabola rotation is a coordinate
              alignment, not a constraint.  The matter cells are
              evaluated at K = K_STAR; the duty cells are evaluated at
              K = 1; the two regimes are joined by SM running, not by
              a single self-consistent K.  K* is unaffected.

The structural reason this fails: matter cells use the parabola primitive
in x^2 form (q^2 exponents from the saddle-node x^2 = mu), while duty
cells use the q^d duty cycle (q^3 exponents from duty_dimension_proof.md
at the K = 1 critical limit).  These are different powers of q, so the
two cell sets live on parabolas of different "openings" and cannot be
co-evaluated at a single coupling.

For the parallel result on the rational field equation iteration, see
K_star_iteration.py: r -> |sum g w e^{2 pi i p/q}| contracts to r = 0
in every ensemble below K_0 ~ 3.  The local map near r = 0 is exactly
r_{n+1} = (K_0/2)^2 r_n^2 + O(r_n^3), with exponent q_min = q_2 = 2.
That r* = 0 is the disordered phase of a quadratic Kuramoto-like map,
not a vacuum failure; the framework's K* lives in that disordered
phase, meaning K* is not a synchronization order parameter -- it is
the parabola primitive's coordinate scale.
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
# Cell tables
# ============================================================================

# Matter sectors: (name, m_heavy, m_light, b_1 step base, N integer)
# N from item12 / parabola rotation: a_1(sector) * K* = sqrt(N).
MATTER = [
    ("leptons",    M_TAU, M_MU, 3 / 2, Q2 ** 2),                # N = 4
    ("up-type",    M_T,   M_C,  8 / 5, Q3 ** 2),                # N = 9
    ("down-type",  M_B,   M_S,  5 / 4, Q2 ** 3 * Q3),           # N = 24
]

# Duty cells: integers from the K = 1 critical limit duty(q) = 1/q^d.
# These appear in the gauge sector via the duty cycle dictionary.
DUTY = [
    ("alpha_2 tree (q_2^d)",          Q2,        Q2 ** D),       # 8
    ("alpha_s tree (q_3^d)",          Q3,        Q3 ** D),       # 27
    ("sin^2_W denom (q_2^d + q_3^d)", Q2 + Q3,   Q2 ** D + Q3 ** D),  # 35
    ("R hierarchy (q_2 q_3^d)",       Q3,        Q2 * Q3 ** D),  # 54
]


def a1_from_pdg(heavy: float, light: float, b1: float) -> float:
    return math.log(heavy / light) / (D * math.log(b1))


def header(text: str) -> None:
    print()
    print("-" * 78)
    print(f"  {text}")
    print("-" * 78)
    print()


# ============================================================================
# Section 1 -- matter cells (PDG-driven baseline)
# ============================================================================

def section_matter() -> None:
    header("Section 1: Matter cells at K = K_STAR (PDG-driven baseline)")
    print(f"  K_STAR = {K_STAR:.10f}")
    print(f"  d      = {D}")
    print()
    print(f"  {'sector':<12} {'a_1 (PDG)':>14} {'x = a_1*K':>14} "
          f"{'sqrt(N)':>12} {'x^2 - N':>14}")
    print("  " + "-" * 70)
    for name, heavy, light, b1, N in MATTER:
        a1 = a1_from_pdg(heavy, light, b1)
        x = a1 * K_STAR
        sN = math.sqrt(N)
        resid = x * x - N
        print(f"  {name:<12} {a1:>14.10f} {x:>14.10f} "
              f"{sN:>12.10f} {resid:>+14.4e}")
    print()
    print("  Each matter sector has x^2 = N within PDG: this is the joint")
    print("  matter-sector closure (item12_K_star_closure.py) that fixes")
    print("  K_STAR from three PDG mass ratios.  Fit count = 1 (K_STAR).")
    print()


# ============================================================================
# Section 2 -- duty cells in the K=1 critical reading
# ============================================================================

def section_duty_critical() -> None:
    header("Section 2: Duty cells under the K = 1 critical reading")
    print("  At K = 1, duty(q) = 1/q^d (duty_dimension_proof.md).")
    print("  Reading: place each duty cell at x = sqrt(N).")
    print()
    print(f"  {'cell':<32} {'N':>6} {'x = sqrt(N)':>14} {'x^2 - N':>14}")
    print("  " + "-" * 68)
    for name, _q, N in DUTY:
        x = math.sqrt(N)
        resid = x * x - N
        print(f"  {name:<32} {N:>6} {x:>14.8f} {resid:>+14.4e}")
    print()
    print("  Residual is identically zero by construction.  K does not")
    print("  appear in the x-coordinate, so dr/dK = 0: these cells exert")
    print("  ZERO pressure on any K* fit.  Including them in a 'joint")
    print("  closure' adds zero information.")
    print()


# ============================================================================
# Section 3 -- duty cells under K-dependent readings
# ============================================================================

def section_duty_offcritical() -> None:
    header("Section 3: Duty cells off-critical at K = K_STAR")
    print("  The off-critical perturbative duty cycle is")
    print("      duty(q, K) = (K/2)^q / q")
    print("  which equals 1/q^d only at K = 1.  We try three K-dependent")
    print("  readings of x and ask: at K = K_STAR, does x^2 = N hold for")
    print("  the duty cells?")
    print()
    K = K_STAR

    def reading_A(q: int) -> float:
        """x = q / K  (matter-sector form a_1 * K = q at q = q_2)."""
        return q / K

    def reading_B(q: int) -> float:
        """x = 1 / sqrt(duty(q, K)) = sqrt(q) / (K/2)^(q/2)."""
        d = (K / 2) ** q / q
        return 1.0 / math.sqrt(d)

    def reading_C(q: int) -> float:
        """x = q * (K/2)^(q/2)  (symmetric, K^q-scaled)."""
        return q * (K / 2) ** (q / 2)

    readings = [
        ("A: x = q / K",                reading_A),
        ("B: x = 1 / sqrt(duty(q, K))", reading_B),
        ("C: x = q * (K/2)^(q/2)",      reading_C),
    ]

    for label, fn in readings:
        print(f"  {label}")
        print(f"    {'cell':<32} {'q':>3} {'x':>12} {'x^2':>14} "
              f"{'N':>6} {'x^2 - N':>14}")
        print("    " + "-" * 72)
        for name, q, N in DUTY:
            x = fn(q)
            resid = x * x - N
            print(f"    {name:<32} {q:>3} {x:>12.6f} {x*x:>14.6f} "
                  f"{N:>6} {resid:>+14.4e}")
        print()

    print("  None of the three readings gives x^2 = N for all four duty")
    print("  cells at K = K_STAR.  The matter-sector reading x = q/K only")
    print("  works at q = q_2 because the matter cell at q=2 has N = q_2^2")
    print("  = 4 (parabola primitive's q^2), while the duty cell at q=2 has")
    print("  N = q_2^d = 8.  Different powers of q, different parabolas.")
    print()


# ============================================================================
# Section 4 -- K-scan: per-cell zero-crossings
# ============================================================================

def section_kscan() -> None:
    header("Section 4: K-scan -- where does each cell's residual vanish?")
    print("  For reading A (x = q/K), the residual x^2 - N = q^2/K^2 - N")
    print("  vanishes at K_zero = q / sqrt(N).  If the four cells share")
    print("  one K_zero, that's the cross-parabola closure for K*.")
    print()
    print(f"  {'cell':<32} {'q':>3} {'N':>6} "
          f"{'K_zero = q/sqrt(N)':>22}")
    print("  " + "-" * 68)
    K_zeros: list[float] = []
    for name, q, N in DUTY:
        Kz = q / math.sqrt(N)
        K_zeros.append(Kz)
        print(f"  {name:<32} {q:>3} {N:>6} {Kz:>22.10f}")
    print()
    print(f"  K_STAR = {K_STAR:.10f}")
    print()
    spread = max(K_zeros) - min(K_zeros)
    print(f"  Spread of K_zeros: {min(K_zeros):.6f} to {max(K_zeros):.6f}")
    print(f"  Range:             {spread:.6f}")
    print(f"  Distance from K_STAR to nearest K_zero: "
          f"{min(abs(K_STAR - Kz) for Kz in K_zeros):.6f}")
    print()
    print("  The four cells have four different K_zero values.  They do")
    print("  not share a joint zero, and the closest one is several")
    print("  percent off K_STAR.  Reading A has no joint cross-parabola")
    print("  closure under any K.")
    print()
    print("  (Aside: K_zero(sin^2_W denom) = (q_2+q_3)/sqrt(q_2^d+q_3^d)")
    print("   = 5/sqrt(35) = sqrt(5/7) ~ 0.8452, the closest of the four")
    print("   to K_STAR.  Suggestive but not exact -- 2% miss.  No reading")
    print("   tested makes all four cells coincide.)")
    print()


# ============================================================================
# Section 5 -- conclusion + tangent on K_star_iteration.py
# ============================================================================

def section_conclusion() -> None:
    header("Section 5: Conclusion")
    print("""\
  The cross-parabola K*↔d proposal does not constrain K*.

  1. Under the canonical K = 1 critical reading, the duty cells satisfy
     x^2 = N by construction.  K does not appear.  Zero gradient on K.

  2. Under K-dependent readings (Section 3), the duty cells use q^d
     exponents while the matter cells use q^2 (parabola primitive).
     Different powers of q -> different parabolas -> no single K
     places both cell sets on one curve.

  3. Under a K-scan of the simplest reading (Section 4), the four duty
     cells have four distinct K_zeros, none equal to K_STAR.

  Structural reason: the cross-parabola rotation is a COORDINATE
  ALIGNMENT.  The framework's integer alphabet
      {4, 9, 24} (matter, q^2)
      {8, 27, 35, 54} (duty, q^d)
  is small enough that matter and duty integers occupy a small range
  on the parabola, but they are not co-evaluated at a single coupling.
  Matter cells use K = K_STAR (the operating point); duty cells use
  K = 1 (the critical limit).  The two regimes are joined by SM
  running (the gauge couplings run from tree to M_Z), not by joint
  self-consistency on a single parabola.

  The K* gap is unaffected.  K_STAR remains the joint matter-sector
  fit, fit count = 1.  The only structurally well-formed candidate
  route to K* without PDG is the Feigenbaum-style iteration of
  a_1(lep) along the Fibonacci backbone -- proposed in
  item12_cross_sector_derivation.py and not yet executed.  That
  calculation would exploit the parabola primitive's intrinsic
  scaling at the golden-mean rotation, not the synchronization
  order parameter of K_star_iteration.py.

  Tangent on K_star_iteration.py's "r* = 0" outcome:

    K_star_iteration.py iterates r -> |sum g(p/q) w(p/q, K_0 r)
    exp(2 pi i p/q)| under three ensembles (Fibonacci backbone,
    Stern-Brocot to depth 14, Farey to q=200).  All three contract
    to r* = 0 below K_0 ~ 3 and find an upper branch above.

    This is NOT XOR-vacuum cancellation (that was the deleted
    field_equation_iteration.py story, which used only the four
    Klein minimum modes -- those were antipodal).  K_star_iteration.py
    uses ensembles that break antipodal symmetry, so r = 0 is not
    forced by parity.

    What r = 0 actually is here: the disordered phase of a quadratic
    Kuramoto-like map.  K_star_iteration.py Part 5 verifies that the
    local linearization of the iteration near r = 0 is exactly

        r_{n+1} = (K_0/2)^2 r_n^2 + O(r_n^3)

    with prefactor (K_0/2)^2 matching to machine precision in every
    ensemble.  The exponent 2 = q_min = q_2 (smallest tongue
    denominator after excluding q=1), and the prefactor is the q=2
    perturbative tongue width.  The framework's primitive integer
    q_2 = 2 IS the iteration's local exponent.

    Implication for K*: the framework's K_STAR = 0.86196052 sits
    BELOW the upper-branch nucleation (K_0 ~ 3) of this iteration.
    K_STAR is in the iteration's disordered phase, so K_STAR cannot
    be a synchronization order parameter of this map.  K_STAR is
    the parabola primitive's coordinate scale (matter cells), NOT a
    Kuramoto fixed point.  The iteration's "failure" to give K_STAR
    is informative: it tells us K_STAR is the wrong kind of object
    for this iteration to produce.
""")


# ============================================================================
# Main
# ============================================================================

def main() -> None:
    print("=" * 78)
    print("  CROSS-PARABOLA AUDIT: does the K*↔d proposal constrain K*?")
    print("=" * 78)
    section_matter()
    section_duty_critical()
    section_duty_offcritical()
    section_kscan()
    section_conclusion()


if __name__ == "__main__":
    main()
