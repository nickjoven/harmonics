"""
sqrt_r_n_correction.py
======================

K-zoo kink-mass ratio table — bare (upper bound) vs corrected
(with the honest √r_n residual factor, Class-2 absent structural input).

Companion script for `sqrt_r_n_correction.md`. Reproduces the
upper-bound column of the table from `master_cascade_identity.md`
soliton-sector implication, and prints the Route-B tongue-width
candidate r_n values explicitly (flagged Class-2, not promoted to
prediction).

No new physics; arithmetic verification of the doc's table.
"""

from fractions import Fraction


# Cascade master-identity instances per master_cascade_identity.md.
# Each row: (label, K_n, (d, n, b), q_n_for_route_B).  q_n is the
# cascade-locking denominator at depth n — q_2=2 for matter/clarinet
# (q_2-tongue), q_3=3 for bowed (q_3-tongue), 6 for the Z_6 cascade
# (conjectural).  Used only in Route B's r_n candidate; the closure
# remains Class-2.
CASCADE_INSTANCES = [
    ("String boundary K = 1", 1.0,            (None, 0, None), None),
    ("Z_6 cascade (conj.)",    2 ** (-1 / 6),  (6, 1, 2),       6),
    ("Matter equilib. K*",     2 ** (-3 / 14), (14, 3, 2),      2),
    ("Bowed cascade (IMF)",    2 ** (-1 / 3),  (3, 1, 2),       3),
    ("Clarinet cascade",       3 ** (-1 / 2),  (2, 1, 3),       2),
]


def bare_ratio(d, n, b):
    """Upper bound `b^(−n/(2d))` from `M_k(d,n,b)/M_k(K=1) = √K_n`.

    Saturated only at the bare-conjecture limit r_n = 1.
    """
    if d is None:
        return 1.0
    return b ** (-Fraction(n, 2 * d))


def route_b_r_candidate(K_n, q_n):
    """Route B (tongue-width) candidate r_n = 2(K_n/2)^q_n.

    Flagged Class-2 in the companion doc; the identification of
    locked-tongue-width with Kuramoto |⟨e^{iθ}⟩| in the identical-
    oscillator substrate requires a structural argument the corpus
    does not yet have.  Reported only as the cleanest numerical
    candidate available with current tools.
    """
    if K_n == 1.0 or q_n is None:
        return 1.0
    return 2 * (K_n / 2) ** q_n


def print_table():
    print("K-zoo kink-mass ratios (bare = upper bound, with √r_n correction)")
    print("=" * 90)
    print(f"{'Sector':<24} {'K_n':>10} {'(d,n,b)':>14} "
          f"{'bare (≤)':>10} {'r_B cand.':>12} {'corrected':>14}")
    print("-" * 90)
    for label, K_n, (d, n, b), q_n in CASCADE_INSTANCES:
        bare = bare_ratio(d, n, b)
        bare_f = float(bare)
        r_b = route_b_r_candidate(K_n, q_n)
        corrected = bare_f * (r_b ** 0.5)
        if d is None:
            tag = "(—,0,—)"
        else:
            tag = f"({d},{n},{b})"
        print(f"{label:<24} {K_n:>10.5f} {tag:>14} "
              f"{bare_f:>10.5f} {r_b:>12.5f} {corrected:>14.5f}")
    print("=" * 90)
    print()
    print("Reading:")
    print("  bare (≤)   — structural upper bound b^(−n/(2d)) (Class-3).")
    print("  r_B cand.  — Route B (tongue-width) r_n candidate (Class-2).")
    print("  corrected  — bare · √r_B (illustrative, NOT a prediction).")
    print()
    print("The corpus's K-zoo kink-mass claim is the bare column read as ≤.")
    print("The Route-B r_B values are catalogued for transparency only —")
    print("Class-2 by Region C pigeonhole (numerology_count_phase_b.md),")
    print("correctly not chased as predictions.")


if __name__ == "__main__":
    print_table()
