#!/usr/bin/env python3
"""
Module 0 — Shapes have jobs.

Three demonstrations:
  - "angle"    — 90° as the angle at which a push contributes nothing to motion
  - "parabola" — the parabola as the boundary trajectory between bound and unbound
  - "square"   — the square as the simplest tile-the-plane shape with binary
                 rotational structure

Run with no arguments to run all three, or pass --shape {angle, parabola, square}.

Pure standard library. No matplotlib required; output is tables of values that
make each role visible numerically.
"""
import argparse
import math


def demo_angle():
    """Sweep the angle between push and velocity; report dKE/dt per unit force."""
    print("=" * 64)
    print("90° — the angle at which a push contributes nothing to motion")
    print("=" * 64)
    print()
    print("A unit force pushing at angle θ relative to the direction of motion.")
    print("The rate at which kinetic energy changes per unit force is cos(θ).")
    print("At θ = 90°, this rate is exactly zero — the push and the motion share")
    print("no direction.")
    print()
    print(f"{'θ (deg)':>10}  {'rate (cos θ)':>14}")
    print(f"{'-' * 10}  {'-' * 14}")
    for theta_deg in range(0, 181, 15):
        theta = math.radians(theta_deg)
        rate = math.cos(theta)
        marker = "  <-- zero" if abs(rate) < 1e-10 else ""
        print(f"{theta_deg:>10}  {rate:>14.6f}{marker}")
    print()
    print("The crossing at 90° is exact. 90° is the answer to: 'at what angle")
    print("does a push contribute nothing to forward motion?'")
    print()


def demo_parabola():
    """Vary launch speed; report whether the trajectory is bound, parabolic, or hyperbolic."""
    print("=" * 64)
    print("Parabola — the boundary between bound and unbound")
    print("=" * 64)
    print()
    print("A body in an inverse-square gravitational field. The trajectory type")
    print("is set by the sign of the total energy E = (1/2)v² − GM/r:")
    print("  E < 0  →  ellipse   (bound; closed orbit)")
    print("  E = 0  →  parabola  (boundary; escapes with zero leftover speed)")
    print("  E > 0  →  hyperbola (unbound; escapes with leftover speed)")
    print()
    GM = 1.0
    r = 1.0
    v_escape = math.sqrt(2 * GM / r)
    print(f"At r = {r}, GM = {GM}: escape speed v_esc = √(2GM/r) = {v_escape:.6f}")
    print()
    print(f"{'v / v_esc':>10}  {'E':>14}  {'eccentricity':>14}  {'trajectory':>12}")
    print(f"{'-' * 10}  {'-' * 14}  {'-' * 14}  {'-' * 12}")
    for ratio in [0.5, 0.7, 0.9, 0.99, 1.0, 1.01, 1.1, 1.3, 1.5]:
        v = ratio * v_escape
        E = 0.5 * v * v - GM / r
        # eccentricity from energy and angular momentum for tangential launch:
        # e² = 1 + 2EL²/(GM)²  (taking unit mass; L = r·v)
        L = r * v
        e_sq = 1 + 2 * E * L * L / (GM * GM)
        e = math.sqrt(abs(e_sq))
        if E < -1e-10:
            kind = "ellipse"
        elif abs(E) <= 1e-10:
            kind = "parabola"
        else:
            kind = "hyperbola"
        marker = "  <-- boundary" if kind == "parabola" else ""
        print(f"{ratio:>10.4f}  {E:>14.6f}  {e:>14.6f}  {kind:>12}{marker}")
    print()
    print("The parabola appears at exactly one launch speed — the boundary case")
    print("between captured (ellipse, e < 1) and free (hyperbola, e > 1). At")
    print("that boundary, e = 1 exactly. The parabola is the shape of 'just")
    print("barely escapes.'")
    print()


def demo_square():
    """Enumerate regular polygons; report rotational order, tiling, and binary divisibility."""
    print("=" * 64)
    print("Square — the simplest tile with binary rotational structure")
    print("=" * 64)
    print()
    print("For a regular N-gon:")
    print("  - rotational symmetry group has order N (rotations by 360°/N)")
    print("  - tiles the plane iff interior angle (N−2)·180/N divides 360°")
    print("  - admits a quarter-turn symmetry iff N is divisible by 4")
    print()
    print(f"{'N':>4}  {'rot. order':>12}  {'interior angle':>16}  {'tiles?':>8}  "
          f"{'÷4?':>6}")
    print(f"{'-' * 4}  {'-' * 12}  {'-' * 16}  {'-' * 8}  {'-' * 6}")
    for N in range(3, 13):
        order = N
        interior = (N - 2) * 180.0 / N
        copies = 360.0 / interior
        tiles = abs(copies - round(copies)) < 1e-9
        binary = (N % 4 == 0)
        marker = ""
        if tiles and binary:
            marker = "  <-- tiles AND ÷4"
        print(f"{N:>4}  {order:>12}  {interior:>14.4f}°  "
              f"{'yes' if tiles else 'no':>8}  {'yes' if binary else 'no':>6}{marker}")
    print()
    print("Only N = 3, 4, 6 tile the plane. Of these, only N = 4 has rotational")
    print("order divisible by 4 — only the square admits the binary chain of")
    print("half-turn, quarter-turn, eighth-turn (via subdivision), and so on.")
    print()
    print("The square is the unique regular polygon that both tiles the plane")
    print("and supports binary rotational refinement.")
    print()


def main():
    parser = argparse.ArgumentParser(description="Module 0 demonstrations.")
    parser.add_argument("--shape", choices=["angle", "parabola", "square", "all"],
                        default="all", help="Which demonstration to run.")
    args = parser.parse_args()

    if args.shape in ("angle", "all"):
        demo_angle()
    if args.shape in ("parabola", "all"):
        demo_parabola()
    if args.shape in ("square", "all"):
        demo_square()


if __name__ == "__main__":
    main()
