#!/usr/bin/env python3
"""
Module 4 — Combining two locks.

Module 3 showed a driven oscillator locks at every whole-number ratio, each
lock a wedge, wider over simpler ratios. This module asks: given two
neighboring locks the oscillator already has — say 1/3 and 1/2 — which lock
appears BETWEEN them? The answer, found first from the dynamics and then
confirmed as pure arithmetic, is a combining rule on the two fractions:
add the tops, add the bottoms.

    between  a/b  and  c/d   →   (a + c) / (b + d)

Three demonstrations:
  - "between"  — use the driven-oscillator locks from Module 3: in the gap
                 between two locks, the widest new lock sits exactly at the
                 combined fraction. Discovered, not decreed.
  - "rule"     — the combined fraction always lies between its parents, and
                 (for as-close-as-possible parents) is the unique fraction
                 with the SMALLEST bottom number in the gap.
  - "tree"     — iterate the rule from 0/1 and 1/1: every whole-number ratio
                 appears, each exactly once. (Named in Module 5.)

Pure standard library.
"""
import argparse
import math
from fractions import Fraction

TWO_PI = 2.0 * math.pi


# --------------------------------------------------------------------------- #
# circle map (from Module 3) — to find the widest lock in a gap
# --------------------------------------------------------------------------- #

def rotation_number(Omega, K, n_iter=1500, transient=500):
    theta = 0.0
    for _ in range(transient):
        theta = theta + Omega - (K / TWO_PI) * math.sin(TWO_PI * theta)
    start = theta
    for _ in range(n_iter):
        theta = theta + Omega - (K / TWO_PI) * math.sin(TWO_PI * theta)
    return (theta - start) / n_iter


def tongue_width(p, q, K, grid=2500, tol=1.5e-3):
    """Fraction of the Ω-axis where the driven oscillator locks to p/q."""
    target = p / q
    count = sum(
        1 for i in range(grid + 1)
        if abs(rotation_number(i / grid, K) - target) < tol
    )
    return count / (grid + 1)


def mediant(fr1, fr2):
    return Fraction(fr1.numerator + fr2.numerator,
                    fr1.denominator + fr2.denominator)


# --------------------------------------------------------------------------- #
# Demo A — the between-lock is the combined fraction (from the dynamics)
# --------------------------------------------------------------------------- #

def demo_between():
    print("=" * 70)
    print("A — the lock between two locks (found from the driven oscillator)")
    print("=" * 70)
    print()
    K = 1.0
    pairs = [
        (Fraction(1, 3), Fraction(1, 2)),
        (Fraction(1, 2), Fraction(2, 3)),
        (Fraction(1, 4), Fraction(1, 3)),
    ]
    print(f"Coupling K = {K:.2f}. For each pair of neighboring locks, compare")
    print("the width of the combined-fraction lock against two other candidate")
    print("fractions in the same gap (both with larger bottom numbers):")
    print()
    for left, right in pairs:
        med = mediant(left, right)
        # two competitors in the gap with larger denominators
        comp1 = mediant(left, med)   # deeper on the left
        comp2 = mediant(med, right)  # deeper on the right
        candidates = [med, comp1, comp2]
        widths = [
            (c, tongue_width(c.numerator, c.denominator, K)) for c in candidates
        ]
        widths.sort(key=lambda t: -t[1])
        winner = widths[0][0]
        print(f"  between {left} and {right}:  combined = {med}")
        for c, w in [(med, dict(widths)[med])] + \
                    [(c, wv) for c, wv in widths if c != med]:
            tag = "  <- combined" if c == med else ""
            print(f"      {str(c):>6}  (bottom {c.denominator:>2})  "
                  f"width {w:.4f}{tag}")
        ok = "YES" if winner == med else "no"
        print(f"      widest lock in the gap is the combined fraction? {ok}")
        print()
    print("The widest new lock between two neighbors sits exactly at the")
    print("combined fraction — tops added, bottoms added. The oscillator finds")
    print("it; we did not put it there.")
    print()


# --------------------------------------------------------------------------- #
# Demo B — the rule: betweenness + smallest-denominator
# --------------------------------------------------------------------------- #

def smallest_denominator_in_gap(left, right):
    """Return the fraction with the smallest denominator strictly between."""
    d = 1
    while True:
        best = None
        for n in range(math.floor(left * d) , math.ceil(right * d) + 1):
            f = Fraction(n, d)
            if left < f < right:
                if best is None or f.denominator < best.denominator:
                    best = f
        if best is not None:
            return best
        d += 1


def demo_rule():
    print("=" * 70)
    print("B — the rule as pure arithmetic (betweenness + smallest bottom)")
    print("=" * 70)
    print()
    pairs = [
        (Fraction(0, 1), Fraction(1, 1)),
        (Fraction(1, 3), Fraction(1, 2)),
        (Fraction(1, 2), Fraction(2, 3)),
        (Fraction(2, 5), Fraction(1, 2)),
        (Fraction(3, 5), Fraction(2, 3)),
    ]
    print(f"{'left':>6}  {'right':>6}  {'combined':>9}  {'between?':>9}  "
          f"{'= smallest-bottom in gap?':>26}")
    print(f"{'-'*6}  {'-'*6}  {'-'*9}  {'-'*9}  {'-'*26}")
    for left, right in pairs:
        med = mediant(left, right)
        between = left < med < right
        smallest = smallest_denominator_in_gap(left, right)
        matches = (med == smallest)
        print(f"{str(left):>6}  {str(right):>6}  {str(med):>9}  "
              f"{'yes' if between else 'NO':>9}  "
              f"{('yes  (' + str(smallest) + ')') if matches else ('NO (' + str(smallest) + ')'):>26}")
    print()
    print("For neighbors that are as close as a pair of fractions can be, the")
    print("combined fraction is the unique fraction with the smallest bottom")
    print("number anywhere between them — the simplest ratio in the gap, hence")
    print("(Module 3) the widest lock. Rule and dynamics agree.")
    print()


# --------------------------------------------------------------------------- #
# Demo C — iterate the rule into a tree
# --------------------------------------------------------------------------- #

def demo_tree():
    print("=" * 70)
    print("C — iterate the rule: every ratio appears, once (named in Module 5)")
    print("=" * 70)
    print()
    print("Start with the two coarsest locks, 0/1 and 1/1. Between each")
    print("neighboring pair, insert the combined fraction. Repeat.")
    print()
    row = [Fraction(0, 1), Fraction(1, 1)]
    print(f"  row 0:  " + "   ".join(str(f) for f in row))
    all_seen = set()
    for level in range(1, 5):
        new_row = []
        for i in range(len(row) - 1):
            new_row.append(row[i])
            new_row.append(mediant(row[i], row[i + 1]))
        new_row.append(row[-1])
        # the freshly inserted ones are at odd indices
        inserted = [new_row[i] for i in range(1, len(new_row), 2)]
        for f in inserted:
            all_seen.add(f)
        print(f"  row {level}:  " + "   ".join(
            (str(f) if f in inserted else "·" * len(str(f))) for f in new_row))
        row = new_row
    print()
    print("Each new row inserts, between every adjacent pair, exactly one new")
    print("fraction — its combined value. No fraction is ever produced twice,")
    print("and every whole-number ratio eventually appears. Iterating one")
    print("combining rule enumerates all the ratios, in the exact order their")
    print("locks emerge as coupling weakens. Module 5 gives this tree its name")
    print("and proves the 'every ratio, exactly once' claim.")
    print()


# --------------------------------------------------------------------------- #

def main():
    parser = argparse.ArgumentParser(description="Module 4 demonstrations.")
    parser.add_argument(
        "--demo", choices=["between", "rule", "tree", "all"], default="all")
    args = parser.parse_args()
    if args.demo in ("between", "all"):
        demo_between()
    if args.demo in ("rule", "all"):
        demo_rule()
    if args.demo in ("tree", "all"):
        demo_tree()


if __name__ == "__main__":
    main()
