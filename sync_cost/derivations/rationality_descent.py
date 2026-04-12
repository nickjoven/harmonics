"""
Rationality descent: is the hidden algorithm real?

Hypothesis (from the conversation that generated this file): the
framework's 'consistency-stipulated resolutions' are Stern-Brocot
descent from 1/1 toward observables, under a finite vocabulary of
primitive transformations.  Every closed item has a finite depth
in the tree.  Open items either have a candidate at reasonable depth
(close to closure) or fail (structurally hard, possibly requiring
vocabulary extension).

This script tests the hypothesis by applying Stern-Brocot descent
to the framework's current content and reporting the depth of every
closure.  If the algorithm is real, the depth histogram should
concentrate at small numbers.

Primitive transformations tested (the framework's native vocabulary):

    T(x) = x            identity
    T(x) = K* * x       multiply by coupling
    T(x) = x / K*       divide by coupling
    T(x) = x * K*^2     square-coupling
    T(x) = x / K*^2     inverse-square-coupling
    T(x) = 1 - x        complement
    T(x) = 1/x          inversion
    T(x) = sqrt(x)      parabola primitive (inverse)
    T(x) = x^2          parabola primitive (forward)

Each transformation is reversible (we can recover x from T(x)), so
finding a small-denominator rational in transformed space is equivalent
to recognizing x as "a rational under T".
"""

from __future__ import annotations

import math
from fractions import Fraction

from framework_constants import (
    K_STAR,
    M_B,
    M_C,
    M_MU,
    M_S,
    M_T,
    M_TAU,
    V_GEV,
)

D_DIM = 3
M_H_GEV = 125.25


def stern_brocot_descent(target: float, tolerance: float,
                         max_depth: int = 200
                         ) -> tuple[Fraction, int] | None:
    """
    Walk the Stern-Brocot tree from the root 1/1 toward target.
    Returns (rational, depth) of the first mediant within tolerance,
    or None if not converged within max_depth.
    """
    if target <= 0 or not math.isfinite(target):
        return None

    l_num, l_den = 0, 1
    r_num, r_den = 1, 0   # represents infinity
    depth = 0
    m_num, m_den = 1, 1

    while depth <= max_depth:
        val = m_num / m_den
        if abs(val - target) <= tolerance:
            return Fraction(m_num, m_den), depth
        if val < target:
            l_num, l_den = m_num, m_den
        else:
            r_num, r_den = m_num, m_den
        m_num = l_num + r_num
        m_den = l_den + r_den
        depth += 1

    return None


def try_all_transformations(observable: float, uncertainty: float
                            ) -> list[tuple[str, float, Fraction, int]]:
    """
    Apply each primitive transformation and Stern-Brocot descend.
    Returns list of (transformation_name, transformed_target,
    best_rational, depth) sorted by depth (smallest = best).
    """
    K = K_STAR
    candidates = []

    def add(name, val, err):
        if val is None or val <= 0 or not math.isfinite(val):
            return
        if err <= 0:
            return
        result = stern_brocot_descent(val, err)
        if result is not None:
            rat, depth = result
            candidates.append((name, val, rat, depth))

    add("id",       observable,          uncertainty)
    add("* K*",     observable * K,      uncertainty * K)
    add("/ K*",     observable / K,      uncertainty / K)
    add("* K*^2",   observable * K**2,   uncertainty * K**2)
    add("/ K*^2",   observable / K**2,   uncertainty / K**2)
    if 0 < observable < 1:
        add("1 - x", 1 - observable,     uncertainty)
    if observable > 0:
        add("1/x",   1 / observable,     uncertainty / observable**2)
        add("sqrt",  math.sqrt(observable),
             uncertainty / (2 * math.sqrt(observable)))
        add("x^2",   observable**2,      2 * observable * uncertainty)

    candidates.sort(key=lambda c: c[3])
    return candidates


# ============================================================================
# Framework observables to test
# ============================================================================

def compute_a1(heavy: float, light: float, b1: float) -> float:
    return math.log(heavy / light) / (D_DIM * math.log(b1))


def build_observables() -> list[tuple[str, float, float, str]]:
    """
    Returns list of (name, value, 1-sigma, category) tuples.
    Categories: "closed" (framework has a rational closure),
                "open"   (framework has open item).
    """
    a1_lep = compute_a1(M_TAU, M_MU, 3 / 2)
    a1_up = compute_a1(M_T, M_C, 8 / 5)
    a1_dn = compute_a1(M_B, M_S, 5 / 4)

    # PDG 2024 values with 1-sigma
    return [
        # -- closed items (framework has a rational closure)
        ("a_1(leptons)",           a1_lep,                   5.6e-5, "closed"),
        ("a_1(up-type)",           a1_up,                    1.1e-2, "closed"),
        ("a_1(down-type)",         a1_dn,                    1.3e-1, "closed"),
        ("a_1(lep)^2 K*^2 = N_l",  (a1_lep * K_STAR) ** 2,   2.6e-4, "closed"),
        ("a_1(up)^2 K*^2 = N_u",   (a1_up * K_STAR) ** 2,    5.8e-2, "closed"),
        ("a_1(dn)^2 K*^2 = N_d",   (a1_dn * K_STAR) ** 2,    9.8e-1, "closed"),
        ("sin^2(theta_W)",         0.23122,                  0.00017, "closed"),
        ("Omega_Lambda",           0.6847,                   0.0073, "closed"),
        ("alpha_s / alpha_2",      3.4863,                   0.005,  "closed"),
        ("Higgs lambda_obs",       (M_H_GEV/V_GEV)**2 / 2,   0.0003, "closed"),

        # -- open or partially-closed items
        ("a_2(lep)/a_1(lep)",      1.4994,                   3.6e-5, "open"),
        ("K* itself (framework)",  K_STAR,                   1e-5,   "open"),
        ("K* itself (loose)",      K_STAR,                   1e-3,   "open"),

        # -- mass ratios (checking if they are directly rational)
        ("m_tau / m_mu",           M_TAU/M_MU,               1e-4,   "info"),
        ("m_mu / m_e",             M_MU / 0.51099895,        1e-7,   "info"),
        ("m_t / m_c",              M_T / M_C,                0.03,   "info"),
    ]


# ============================================================================
# Main
# ============================================================================

def main():
    print("=" * 78)
    print("  RATIONALITY DESCENT: is the algorithm real?")
    print("=" * 78)
    print()
    print("  Stern-Brocot descent from 1/1 toward each framework observable,")
    print("  under a finite vocabulary of primitive transformations.")
    print("  For each observable: report the transformation whose descent")
    print("  terminates at smallest depth, within PDG uncertainty.")
    print()

    observables = build_observables()

    print(f"  {'observable':<22} {'category':<8} {'best T':<10} "
          f"{'depth':>5} {'rational':>14} {'T(x)':>14}")
    print("  " + "-" * 76)

    closed_depths = []
    open_depths = []
    not_found = []

    for name, val, err, category in observables:
        results = try_all_transformations(val, err)
        if not results:
            print(f"  {name:<22} {category:<8} {'<no match>':<10}")
            not_found.append(name)
            continue
        # Best (smallest depth)
        t_name, t_val, rat, depth = results[0]
        rat_str = f"{rat.numerator}/{rat.denominator}"
        print(f"  {name:<22} {category:<8} {t_name:<10} "
              f"{depth:>5} {rat_str:>14} {t_val:>14.8f}")

        if category == "closed":
            closed_depths.append(depth)
        elif category == "open":
            open_depths.append((name, depth, t_name, rat))

    # ---------------------------------------------------------------
    print()
    print("-" * 78)
    print("  DEPTH HISTOGRAM FOR CLOSED ITEMS")
    print("-" * 78)
    print()

    if closed_depths:
        depth_counts = {}
        for d in closed_depths:
            depth_counts[d] = depth_counts.get(d, 0) + 1
        print("  depth | count | bar")
        print("  ------|-------|" + "-" * 30)
        for d in sorted(depth_counts):
            bar = "#" * depth_counts[d]
            print(f"  {d:>5} | {depth_counts[d]:>5} | {bar}")
        print()
        avg = sum(closed_depths) / len(closed_depths)
        total = sum(closed_depths)
        print(f"  Closed items: {len(closed_depths)}")
        print(f"  Sum of depths: {total}")
        print(f"  Mean depth:    {avg:.2f}")
        print(f"  Max depth:     {max(closed_depths)}")
        print(f"  Min depth:     {min(closed_depths)}")
    print()

    # ---------------------------------------------------------------
    print("-" * 78)
    print("  OPEN ITEMS AND THEIR BEST-CANDIDATE DEPTHS")
    print("-" * 78)
    print()
    if open_depths:
        for name, depth, t_name, rat in open_depths:
            rat_str = f"{rat.numerator}/{rat.denominator}"
            flag = "CLOSEABLE" if depth < 15 else "deep"
            print(f"  {name:<25} depth {depth:>3} via {t_name:<8} "
                  f"-> {rat_str:<14} [{flag}]")
    print()

    # ---------------------------------------------------------------
    print("-" * 78)
    print("  CANONICAL CLOSURES: how many sigmas off?")
    print("-" * 78)
    print()
    print("  For each closed item, test the framework's CANONICAL rational")
    print("  closure against the observed value.  'Sigma off' is the")
    print("  residual divided by the observable's 1-sigma uncertainty.")
    print()

    a1_lep = compute_a1(M_TAU, M_MU, 3 / 2)
    a1_up = compute_a1(M_T, M_C, 8 / 5)
    a1_dn = compute_a1(M_B, M_S, 5 / 4)

    canonical = [
        # (name, observed_value, canonical_prediction, uncertainty, form)
        ("a_1(lep) * K*",
         a1_lep * K_STAR, 2.0, 5.6e-5 * K_STAR, "q_2 = 2"),
        ("a_1(up) * K*",
         a1_up * K_STAR, 3.0, 1.1e-2 * K_STAR, "q_3 = 3"),
        ("a_1(dn)^2 * K*^2",
         (a1_dn * K_STAR) ** 2, 24.0, 0.98, "q_2^3 q_3 = 24"),
        ("Omega_Lambda (F_6 lim)",
         0.6847, 13 / 19, 0.0073, "|F_6|/|F_7| = 13/19"),
        ("sin^2(theta_W) tree",
         0.23122, 8 / 35, 0.00017, "q_2^3 / (q_2^3 + q_3^3) = 8/35"),
        ("alpha_s / alpha_2 tree",
         3.4863, 27 / 8, 0.005, "q_3^3 / q_2^3 = 27/8"),
    ]

    print(f"  {'closure':<24} {'observed':>12} {'canonical':>12} "
          f"{'sigma off':>11} {'form':<20}")
    print("  " + "-" * 78)
    for name, obs, pred, err, form in canonical:
        diff = obs - pred
        sig = abs(diff) / err if err > 0 else float("inf")
        marker = "OK" if sig < 1 else ("~" if sig < 3 else "X")
        print(f"  {name:<24} {obs:>12.8f} {pred:>12.8f} "
              f"{sig:>10.2f}s {form:<20} [{marker}]")
    print()

    # ---------------------------------------------------------------
    print("-" * 78)
    print("  DIAGNOSTIC: K* reachable by direct descent?")
    print("-" * 78)
    print()
    print("  Run Stern-Brocot descent on K* directly under each")
    print("  transformation, at two tolerance levels:")
    print()
    for tol in [1e-3, 1e-5, 1e-7]:
        print(f"  tolerance = {tol}")
        for t_name, t_val in [
            ("K*",         K_STAR),
            ("2 / K*",     2 / K_STAR),
            ("1 - K*",     1 - K_STAR),
            ("K*^2",       K_STAR ** 2),
            ("(K*/2)^2",   (K_STAR / 2) ** 2),
            ("K* * pi",    K_STAR * math.pi),
            ("K* / pi",    K_STAR / math.pi),
        ]:
            result = stern_brocot_descent(t_val, tol, max_depth=100)
            if result:
                rat, depth = result
                rat_str = f"{rat.numerator}/{rat.denominator}"
                print(f"    {t_name:<14} = {t_val:>12.8f}  "
                      f"-> {rat_str:<14} at depth {depth}")
            else:
                print(f"    {t_name:<14} = {t_val:>12.8f}  "
                      f"-> not found within depth 100")
        print()

    # ---------------------------------------------------------------
    print("=" * 78)
    print("  VERDICT")
    print("=" * 78)
    print()
    print("  Reading the histogram above:")
    print()
    print("  - If closed items cluster at small depth (< ~15), the hidden")
    print("    algorithm is REAL.  Every closed item is Stern-Brocot")
    print("    reachable under a finite vocabulary, and the framework has")
    print("    been running rationality descent implicitly all along.")
    print()
    print("  - If open items have candidates at reasonable depth, they")
    print("    are CLOSEABLE -- the algorithm points at the next step.")
    print()
    print("  - If K* is found by direct descent at small depth under any")
    print("    transformation, the framework's K* has a Stern-Brocot")
    print("    content address and can be derived from the algorithm")
    print("    without lepton masses.")
    print()
    print("  - If K* is NOT found at small depth under any transformation,")
    print("    the lepton identity IS the framework's K* determination,")
    print("    and the Stern-Brocot depth of K* is derived from the")
    print("    depth of its structural role (q=2 tongue), not from direct")
    print("    descent.")
    print()


if __name__ == "__main__":
    main()
