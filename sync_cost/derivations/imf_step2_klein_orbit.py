#!/usr/bin/env python3
"""Step-2 lemma for the bowed (Salpeter) cascade: depth = Klein-orbit count.

The IMF bowed-cascade slope alpha = -q_2 - n/d = -7/3 (imf_bowed_cascade.md)
uses (d, n) = (q_3, 1). This derives both from the canonical Klein-bottle
antiperiodic involution r -> 1 - r -- the same y -> 1-y action that
step3_step5_klein_proof.py uses to fix the signature (3,1) / Farey index 4 --
applied here at Farey level F_{q_3} = F_3.

Lemma:
  (a) The orbit count of F_3 under r -> 1-r is 3 = q_3  =>  cascade depth d = q_3.
  (b) Decomposition is (2 pairs, 1 fixed). The boundary pair {0/1, 1/1} is
      redundant with the y-periodic identification (0 ~ 1); the fixed point
      {1/2} carries no flip; leaving 1 non-redundant antiperiodic flip
      {1/3, 2/3}  =>  n = 1.
  (c) alpha = -q_2 - n/d = -2 - 1/3 = -7/3, the Salpeter slope.
  (d) The identity orbit_count(F_m) = m holds precisely for m in {2,3,4}
      (it fails at m = 5, where phi(5) = 4), so the orbit grounding is
      available exactly for the small-denominator cascades and does NOT
      ground the deeper Z_6 (d=6) or K* (d=14) sectors.

Run: python3 imf_step2_klein_orbit.py
"""
from __future__ import annotations

from fractions import Fraction


def farey(n: int) -> list[Fraction]:
    s = {Fraction(p, q) for q in range(1, n + 1) for p in range(0, q + 1)}
    return sorted(s)


def klein_orbits(F: list[Fraction]) -> tuple[list[tuple[Fraction, Fraction]], list[Fraction]]:
    """Decompose F under the Klein involution r -> 1-r into (pairs, fixed)."""
    pairs: list[tuple[Fraction, Fraction]] = []
    fixed: list[Fraction] = []
    seen: set[Fraction] = set()
    for r in F:
        if r in seen:
            continue
        img = Fraction(1) - r
        (fixed if img == r else pairs).append(r if img == r else (r, img))
        seen.add(r)
        seen.add(img)
    return pairs, fixed


def main() -> int:
    q2, q3 = 2, 3
    F3 = farey(q3)
    pairs, fixed = klein_orbits(F3)
    n_orbits = len(pairs) + len(fixed)

    print("=" * 66)
    print("STEP-2 LEMMA  (bowed / Salpeter cascade)")
    print("Klein antiperiodic involution r -> 1-r on F_{q_3} = F_3")
    print("=" * 66)
    print(f"F_3 = {{{', '.join(str(r) for r in F3)}}}")
    print()
    for a, b in pairs:
        tag = ("boundary {0/1,1/1}: redundant with y-periodicity (0~1)"
               if a == 0 else "interior: non-redundant antiperiodic flip")
        print(f"  pair  {a} <-> {b}    [{tag}]")
    for r in fixed:
        print(f"  fixed {r}              [invariant: no flip]")
    print()

    interior = [(a, b) for a, b in pairs if a != 0]
    n = len(interior)
    d = n_orbits
    assert d == q3, "orbit count must equal q_3"
    assert n == 1, "non-redundant flip count must be 1"
    alpha = Fraction(-q2) - Fraction(n, d)
    print(f"(a) orbit count = {d} = q_3            -> cascade depth d = q_3")
    print(f"(b) non-redundant flips n = {n}")
    print(f"(c) alpha = -q_2 - n/d = -{q2} - {n}/{d} = {alpha} = {float(alpha):.4f}")
    print(f"    (observed Salpeter high-mass IMF: -2.35 +/- 0.05; 0.33 sigma)")
    print()

    print("(d) Selection: orbit_count(F_m) = m only for small m")
    print(f"    {'m':>3}{'orbit_count':>13}{'= m ?':>8}")
    for m in range(2, 8):
        oc = sum(map(len, klein_orbits(farey(m))))
        print(f"    {m:>3}{oc:>13}{'  match' if oc == m else '  no':>8}")
    print()
    print("    Holds for m in {2,3,4}; fails at m=5 (phi(5)=4). So depth =")
    print("    orbit-count grounds the bowed (d=q_3=3) and clarinet (d=q_2=2)")
    print("    cascades, and does NOT ground the deeper Z_6 (d=6, orbit_count")
    print("    = 7) or K* (d=14) sectors -- consistent with those being the")
    print("    unsupported rungs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
