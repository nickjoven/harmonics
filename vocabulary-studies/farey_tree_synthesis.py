"""
farey_tree_synthesis.py

Capstone check for farey_tree_synthesis.md. One object — the
Stern-Brocot / Farey tree (the PSL(2,Z) action on Q, i.e. the mediant
primitive) — under three celebrated problems. In each, the STRUCTURE
(tree / group / level / boundary) is forced and tractable; the
ARITHMETIC (discriminant / orbit / leaf-distribution) at the boundary
is the hard/open part.

This script demonstrates the third (Riemann) leg concretely, because it
is the most surprising: the Riemann Hypothesis IS a statement about how
evenly the Farey tree's leaves are spaced (Franel-Landau, 1924).

Pure-Python, no numpy.
"""

from math import gcd


def farey(n):
    """All Farey fractions of order n in [0,1], ascending, via the
    standard neighbour recurrence (mediant-adjacency in disguise)."""
    a, b, c, d = 0, 1, 1, n
    seq = [(a, b)]
    while c <= n:
        k = (n + b) // d
        a, b, c, d = c, d, k * c - a, k * d - b
        seq.append((a, b))
    return seq  # includes 0/1 ... 1/1


def franel_landau(n):
    """Franel's discrepancy D(n) = sum_v |r_v - v/M|, where r_v is the
    v-th Farey fraction and v/M its uniform-spacing position.
    RH  <=>  D(n) = O(n^{1/2+eps}).  (Franel 1924; Landau 1924.)"""
    F = farey(n)
    M = len(F) - 1                      # intervals; F has M+1 points 0..1
    d_abs = 0.0
    d_sq = 0.0
    for v, (p, q) in enumerate(F):
        delta = p / q - v / M
        d_abs += abs(delta)
        d_sq += delta * delta
    return M + 1, d_abs, d_sq


if __name__ == "__main__":
    print("=" * 68)
    print("The Farey tree under three problems  (mediant primitive = PSL(2,Z))")
    print("=" * 68)

    print("\nLEG 3 (Riemann) -- RH = even spacing of the tree's leaves")
    print("Franel-Landau: RH <=> D(N)=sum|r_v - v/M| = O(N^{1/2+eps})\n")
    print(f"{'N':>4} {'|F_N|':>7} {'D(N)':>10} {'D(N)/sqrt(N)':>14}")
    for N in (8, 16, 32, 64, 128, 256):
        cnt, d_abs, d_sq = franel_landau(N)
        print(f"{N:>4} {cnt:>7} {d_abs:>10.4f} {d_abs/(N**0.5):>14.4f}")
    print("\n  D(N)/sqrt(N) staying bounded is the RH-equivalent signal;")
    print("  proving the bound for ALL N is the open problem. The framework")
    print("  forces the tree (the leaves' existence/order); their fine")
    print("  EQUIDISTRIBUTION -- the arithmetic at the boundary -- is RH.")

    print("\n--- the three legs, structure (forced) vs arithmetic (hard) ---")
    rows = [
        ("problem", "structure on the tree (forced)", "arithmetic at boundary (hard/open)"),
        ("Ramanujan 1/pi", "level Gamma_0(6); convergent path", "CM discriminant d=58 (selector 29)"),
        ("Collatz", "integers = q=1 boundary; one cycle", "which orbit converges (per-n, open)"),
        ("Riemann (RH)", "Farey leaves: order + count |F_N|", "their equidistribution D(N) bound"),
    ]
    w = (16, 34, 36)
    for r in rows:
        print("  " + "".join(c[:wi].ljust(wi + 1) for c, wi in zip(r, w)))
    print("\n  Through-line: the mediant primitive is a STRUCTURE-fixer.")
    print("  Every leg's open part lives in the arithmetic at the boundary.")
