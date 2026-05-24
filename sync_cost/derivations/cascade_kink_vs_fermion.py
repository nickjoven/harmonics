#!/usr/bin/env python3
"""Cascade kink masses vs. the observed fermion mass spectrum.

The above-onset cascade sectors host soft sine-Gordon kinks with masses
M_k(K_n) = 8 sigma sqrt(K_n r_n), giving ratios to the K=1 boundary kink

    M_k(K_n)/M_k(1) = sqrt(K_n r_n) / sqrt(K_1 r_1),

with r_n the b-harmonic Kuramoto order parameter measured in
cascade_kink_onset.py (r_1 = r(K=1)). By the Coleman sine-Gordon <->
Thirring correspondence these kinks are fermions. This script asks the
direct question: do the cascade kink-mass ratios land on the observed
charged-lepton / quark mass ratios? Pigeonhole discipline applies, but
is only needed if the dynamic ranges are even commensurate.

Run: python3 cascade_kink_vs_fermion.py
"""
from __future__ import annotations

import math

K_C = 2.0 / math.pi


# r_b from the b-harmonic simulation (cascade_kink_onset.py)
SECTORS = [
    ("K=1 boundary", 1.0, 0.6028),
    ("Z_6", 2.0 ** (-1 / 6), 0.525),
    ("Matter K*", 0.86196052, 0.502),
    ("Bowed", 2.0 ** (-1 / 3), 0.433),
]

# Observed masses (MeV); PDG central values.
LEPTONS = {"e": 0.5110, "mu": 105.66, "tau": 1776.86}
QUARKS = {"u": 2.16, "d": 4.67, "s": 93.4, "c": 1270.0, "b": 4180.0, "t": 172690.0}


def span(vals: list[float]) -> float:
    return max(vals) / min(vals)


def main() -> int:
    r1 = SECTORS[0][2]
    Mk1 = math.sqrt(1.0 * r1)
    print("=" * 64)
    print("CASCADE KINK-MASS RATIOS (to K=1 boundary kink)")
    print("=" * 64)
    print(f"{'sector':<16}{'K_n':>9}{'r_b':>8}{'M_k/M_k(1)':>13}")
    print("-" * 64)
    kink_ratios = []
    for label, K, rb in SECTORS:
        ratio = math.sqrt(K * rb) / Mk1
        kink_ratios.append(ratio)
        print(f"{label:<16}{K:>9.4f}{rb:>8.3f}{ratio:>13.4f}")
    print("-" * 64)
    kspan = span(kink_ratios)
    print(f"kink-mass dynamic range (max/min): {kspan:.3f}x")
    print()

    print("OBSERVED FERMION MASSES (MeV) and dynamic range")
    print("-" * 64)
    lep = list(LEPTONS.values())
    qk = list(QUARKS.values())
    print(f"charged leptons {LEPTONS}: span {span(lep):,.0f}x")
    print(f"  ratios to e: " + ", ".join(f"{m/lep[0]:.1f}" for m in lep))
    print(f"quarks span (u..t): {span(qk):,.0f}x")
    print(f"all 9 charged fermions: span {span(lep+qk):,.0f}x")
    print()

    print("VERDICT")
    print("-" * 64)
    full = span(lep + qk)
    print(f"Fermion masses span ~{full:,.0f}x; cascade kinks span ~{kspan:.2f}x.")
    print(f"Mismatch in dynamic range: factor ~{full/kspan:,.0f}.")
    print("The identified cascade kinks are NEARLY DEGENERATE (all within")
    print("~25% of the boundary kink) -- the b^(-n/2d).sqrt(r_n) flow is an")
    print("order-1 modulation, not a hierarchy. They cannot be the fermion")
    print("mass spectrum.")
    print()
    # How deep a cascade would be needed to reach the fermion range?
    # need b^(-n/(2d)) ~ 1/full, b=2, d=3:
    n_needed = 2 * 3 * math.log(full) / math.log(2)
    print(f"To span {full:,.0f}x via b^(-n/2d) (b=2,d=3) would need cascade")
    print(f"depth n ~ {n_needed:.0f} -- far beyond the identified K-zoo")
    print("(n = 1, 3). Such deep cascades are not in the master identity;")
    print("invoking them to manufacture the hierarchy would be unforced.")
    print()
    print("Pigeonhole test is moot: the ranges are incommensurate by ~5")
    print("orders of magnitude, so this fails before any near-match count.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
