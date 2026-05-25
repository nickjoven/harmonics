#!/usr/bin/env python3
"""NULL RESULT: the critical (K=1) tongue width does NOT follow Farey 1/q^2.

The mass-function baseline (mass_entrained_measure.md, farey_mass_baseline.py)
identified a locked mode's mass with its entrained tongue width AND assumed
that width equals the Farey weight w(p/q) ~ 1/q^2, giving slope -1 - 2/beta
= -2 for beta = 2. This records why that identification fails.

A-PRIORI (decisive, independent of any measurement):
At K=1 the devil's staircase is COMPLETE -- the mode-locked tongues fill
[0,1] with measure 1, sum_{p/q} w(p/q) = 1. With Farey multiplicity
phi(q) ~ (6/pi^2) q and a width law w ~ q^(-beta),

    sum_q phi(q) q^(-beta)  ~  sum_q q^(1-beta)   converges iff beta > 2.

So beta = 2 (the Farey 1/q^2) gives an INFINITE total width -- it over-fills
[0,1] and is inconsistent with a complete staircase. The physical tongue
width MUST decay faster than 1/q^2; beta = 2 is impossible.

MEASURED (sine-circle map theta -> theta + Omega - (K/2pi)sin(2pi theta),
K=1; widths by plateau bisection on the rotation number, see git history):

    q:        2       3       4       5       6       7
    w(1/q):   0.0740  0.0306  0.0159  0.0093  0.0059  0.0040
    w*q^2:    0.296   0.275   0.254   0.233   0.214   0.197   (falling: beta>2)

Fitted w ~ q^(-2.3) (local exponent rises 2.2 -> 2.5 across the range; not
even a clean power law). Stable from n=12k to n=80k iterations.

IMPLICATION. The dynamical mass-function slope is -1 - 2/beta ~ -1.86 (for
beta ~ 2.3), NOT -2. So:
  - mass = physical entrained tongue width  ->  baseline ~ -1.86, and the
    -7/3 = baseline - 1/q_3 reconstruction misses Salpeter (-2.35).
  - the -2 baseline holds only for the combinatorial Farey TREE weight
    1/q^2 (exact by definition), whose identification with physical mass
    is NOT established.

SCOPE. This nulls only the mass<->width step of the mass-function baseline.
It does NOT touch results that use the Farey COUNT |F_n| ~ (3/pi^2) n^2
(Omega_Lambda = 13/19, the 13:5:1 partition) -- those are pure combinatorics,
independent of any width law. The Step-2 Klein-orbit lemma (d = orbit count)
and the epsilon = const result (uniform capture density, width-independent)
also survive.

Run: python3 farey_tongue_width_null.py
"""
from __future__ import annotations

import math


def main() -> int:
    print("A-PRIORI: complete K=1 staircase => sum_{p/q} w = 1 => beta > 2.")

    def phi(n):
        r, m, p = n, n, 2
        while p * p <= m:
            if m % p == 0:
                while m % p == 0:
                    m //= p
                r -= r // p
            p += 1
        if m > 1:
            r -= r // m
        return r
    for cut in (10, 100, 1000, 10000):
        s = sum(phi(q) / q**2 for q in range(1, cut + 1))
        print(f"  sum_q phi(q)/q^2 up to q={cut:>5}: {s:.3f}   "
              f"(beta=2 total diverges ~ log -> cannot equal 1)")
    print()

    print("MEASURED critical tongue widths (recorded; see git history):")
    data = {2: 0.0740, 3: 0.0306, 4: 0.0159, 5: 0.0093, 6: 0.0059, 7: 0.0040}
    xs = [math.log(q) for q in data]
    ys = [math.log(w) for w in data.values()]
    n = len(xs)
    sx, sy = sum(xs), sum(ys)
    beta = -(n * sum(x*y for x, y in zip(xs, ys)) - sx*sy) / \
           (n * sum(x*x for x in xs) - sx*sx)
    print(f"  fitted w ~ q^(-{beta:.2f})  (Farey assumes 2; staircase forces >2)")
    slope = -1.0 - 2.0 / beta
    print(f"  => dynamical mass-function slope -1 - 2/beta = {slope:.2f}  (not -2)")
    print()
    print("CONCLUSION: the mass<->width identification is NULL. The Farey 1/q^2")
    print("is the combinatorial tree weight, not the physical critical width.")
    print("Unaffected: |F_n| ~ n^2 count (Omega_Lambda), Step-2 orbit count,")
    print("epsilon = const (uniform capture density).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
