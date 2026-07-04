#!/usr/bin/env python3
"""N17 -- does D-preservation force the cascade->FRW embedding exponent? No.

The K(t) frontier (k_of_t_problem_statement.md) localizes the cosmological
mass-function slope to ONE open object: the station<->epoch map, the relabel
of the cascade scale axis into FRW redshift/epoch. A free map predicts any
slope; only a FORCED map predicts. So the question is what forces it.

One candidate (tested here): require the scale-relativistic invariant
D ~ 0.87 -- the devil's-staircase complement dimension, lab-confirmed as the
Josephson/CDW universality class (josephson_staircase_comparison.py) and
shown redshift-robust (frw_staircase_transform.py) -- to be PRESERVED across
the embedding. If only one exponent preserves D, geometry forces the map.

This tests it directly. An embedding with exponent p relabels the scale axis
Omega -> Omega^p (different p = different concavity of the perspective). The
result: D ~ 0.87 for EVERY p. D-preservation is VACUOUS -- box-counting
dimension is bi-Lipschitz-invariant, so any smooth embedding preserves it.
D is too robust to discriminate; it does NOT force the exponent. This closes
the "geometrically forced via the invariant D" route for the map.

What this does NOT show: it does not establish a positive replacement. A
stronger condition -- metric/curvature matching (isometric embedding of the
cascade self-similarity into the FRW geometry), not a topological invariant
-- WOULD constrain the map, but it carries one free rate parameter (cascade
steps per unit FRW expansion). Whether that rate coincides with the
inflation-segment cadence (2/57 ~ 0.0351 levels/e-fold, substrate-forced
per PRs #178/#179; supersedes the earlier n_s-anchored ~0.0365 rate cited
in continuity_in_K_nulls.md N12/S2) is an OPEN CONJECTURE, not a result:
the inflationary k<->level mapping (which sets n_s) and the matter-era
tongue<->epoch mapping (which sets the slope) are distinct, and the
N12/S2 catalog of rate-conflation as an ambiguity null still applies
under either cadence value. So the rate is NOT shown to be the
inflation-segment cadence here; that identification would itself need a
derivation. The map stays Class-2.

Run: python3 geometric_forcing_null.py   (pure stdlib; ~5 s)
"""
from __future__ import annotations

import math

TWO_PI = 2.0 * math.pi


def W(Omega: float, K: float = 1.0, n: int = 4000) -> float:
    th = 0.1
    half = n // 2
    for _ in range(half):
        th += Omega - (K / TWO_PI) * math.sin(TWO_PI * th)
    th0, m = th, n - half
    for _ in range(m):
        th += Omega - (K / TWO_PI) * math.sin(TWO_PI * th)
    return (th - th0) / m


def boxcount_D(Ws: list[float], thresh: float = 1e-3) -> float:
    M = len(Ws)
    xs, ys = [], []
    for k in range(5, 10):
        nb = 2 ** k
        cells = M // nb
        active = sum(1 for b in range(nb)
                     if max(Ws[b*cells:(b+1)*cells]) - min(Ws[b*cells:(b+1)*cells]) > thresh)
        xs.append(k * math.log(2)); ys.append(math.log(active))
    n = len(xs); sx, sy = sum(xs), sum(ys)
    return (n*sum(x*y for x, y in zip(xs, ys)) - sx*sy) / (n*sum(x*x for x in xs) - sx*sx)


def main() -> int:
    M = 2 ** 12
    print("D under a family of embedding exponents Omega -> Omega^p")
    print("(different p = different perspective concavity / station<->epoch map)")
    print(f"{'p':>6}{'D':>10}")
    print("-" * 18)
    Ds = []
    for p in (0.6, 0.8, 1.0, 1.3, 1.7):
        # embedded staircase: sample W at Omega = u^(1/p) on a uniform u-grid
        Ws = [W(((i + 0.5) / M) ** (1.0 / p), 1.0) for i in range(M)]
        D = boxcount_D(Ws)
        Ds.append(D)
        print(f"{p:>6.1f}{D:>10.3f}")
    print("-" * 18)
    spread = max(Ds) - min(Ds)
    print(f"D spread across exponents: {spread:.3f}")
    print()
    print("VERDICT (N17)")
    print("-" * 60)
    if spread < 0.06:
        print(f"* D ~ 0.87 for EVERY exponent (spread {spread:.3f}). D-preservation")
        print("  is VACUOUS: box-counting dimension is bi-Lipschitz-invariant, so")
        print("  any smooth embedding preserves it. It does NOT force the exponent.")
        print("  The 'geometrically forced via the invariant D' route is CLOSED.")
    else:
        print(f"* D varies by {spread:.3f} across exponents -- it discriminates.")
    print()
    print("What this does NOT establish")
    print("-" * 60)
    print("A positive replacement. Metric/curvature matching (not a topological")
    print("invariant) WOULD constrain the map, but carries one free rate: cascade")
    print("steps per unit FRW expansion. Whether that rate IS the substrate-forced")
    print("inflation cadence (2/57 ~ 0.0351 levels/e-fold; PRs #178/#179)")
    print("is an OPEN CONJECTURE, not a result -- the inflationary k<->level")
    print("map (sets n_s) and the matter-era tongue<->epoch map (sets the slope)")
    print("are distinct, and continuity_in_K_nulls.md N12/S2 flags rate-conflation")
    print("(off by a comparable factor) as an ambiguity null.")
    print("The station<->epoch map stays Class-2: D does not force it, and the")
    print("n_s identification is unproven. The frontier is unmoved -- one route")
    print("closed, no scale smuggled, no slope manufactured.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
