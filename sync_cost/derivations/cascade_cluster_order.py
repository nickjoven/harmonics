#!/usr/bin/env python3
"""Multi-cluster order parameter: why the clarinet r_1 = 0 is a symmetry
zero, not a sync-onset failure.

cascade_rn_compute.py used the single-cluster Kuramoto order parameter
r_1 = <e^{i theta}> = sqrt(1 - K_c/K). That is the correct coherence
measure only for a SINGLE synchronized cluster (the K=1 boundary, full
lock). The K<1 cascade sectors are MODE-LOCKED: the ensemble splits into
b symmetric phase clusters, where b is the sector's cascade base
(= the acoustic overblow ratio: bowed/sax overblow at the octave b=q_2=2,
clarinet at the twelfth b=q_3=3; instrument_family_taxonomy.md).

For a symmetric b-cluster state theta_k = theta_0 + 2*pi*k/b (k=0..b-1):

    r_m = <e^{i m theta}> = e^{i m theta_0}        if b | m
                          = 0                       otherwise

So r_1 = 0 for EVERY b >= 2 sector -- identically, by symmetry, at any
coupling. The coherence lives in r_b (the base-th harmonic). The clarinet
(b=3) has r_1 = r_2 = 0 and coherence purely in r_3 -- exactly its
odd-harmonic / square-wave / three-fold signature. Measuring r_1 and
concluding "below onset, no kink" was the wrong order parameter.

The kink mass uses the *sector's own* order parameter r_b. For a
well-locked sector r_b -> 1, so the kink mass returns to the bare bound
M_k/M_k(1) = b^(-n/(2d)) -- and the clarinet kink EXISTS, at ~0.760, not 0.

Run: python3 cascade_cluster_order.py
"""
from __future__ import annotations

import cmath
import math


def cluster_order(b: int, theta0: float = 0.3, m_max: int = 6) -> list[float]:
    """|r_m| for a symmetric b-cluster state, m = 1..m_max."""
    phases = [theta0 + 2 * math.pi * k / b for k in range(b)]
    out = []
    for m in range(1, m_max + 1):
        z = sum(cmath.exp(1j * m * th) for th in phases) / b
        out.append(abs(z))
    return out


def main() -> int:
    print("=" * 70)
    print("SYMMETRY ZERO OF r_1 FOR b-CLUSTER (MODE-LOCKED) SECTORS")
    print("=" * 70)
    print(f"{'b (clusters)':<14}" + "".join(f"|r_{m}|".rjust(8) for m in range(1, 7)))
    print("-" * 70)
    for b in (1, 2, 3, 6):
        rs = cluster_order(b)
        print(f"{b:<14}" + "".join(f"{r:8.3f}" for r in rs))
    print("-" * 70)
    print("Reading: r_1 = 0 for every b>=2 sector (symmetry). The single-")
    print("cluster r_1 = sqrt(1-K_c/K) used earlier is the WRONG measure for")
    print("mode-locked sectors. Coherence lives in r_b: bowed/Z6/K* in r_2,")
    print("clarinet in r_3. The clarinet's odd-harmonic/square-wave/three-")
    print("fold structure IS the r_1=0, r_3-coherent pattern.")
    print()

    # The sector's own r_b is NOT ~1 -- it must be solved by
    # self-consistency. cascade_kink_onset.py simulates the b-harmonic
    # Kuramoto and finds the b-cluster onset is b-INDEPENDENT (= K_c = 2/pi),
    # so the discriminator is just whether K_n exceeds 2/pi.
    print("KINK-MASS FLOW (r_b from self-consistency; see cascade_kink_onset.py):")
    sectors = [
        ("Z_6  (d,n,b)=(6,1,2)", 6, 1, 2, 0.525),
        ("K*   (d,n,b)=(14,3,2)", 14, 3, 2, 0.502),
        ("Bowed(d,n,b)=(3,1,2)", 3, 1, 2, 0.433),
        ("Clarinet (d,n,b)=(2,1,3)", 2, 1, 3, 0.013),
    ]
    print(f"{'sector':<26}{'b^(-n/2d)':>11}{'r_b (sim)':>10}{'kink?':>20}")
    print("-" * 70)
    for label, d, n, b, rb in sectors:
        bound = b ** (-n / (2 * d))
        kink = "soft kink (square)" if rb > 0.05 else "NO kink (triangle)"
        print(f"{label:<26}{bound:>11.4f}{rb:>10.3f}{kink:>20}")
    print("-" * 70)
    print("CORRECTION to an earlier reading: the clarinet kink does NOT exist")
    print("at ~0.760. Clarinet K = 3^(-1/2) = 0.577 < K_c = 2/pi = 0.637, so")
    print("r_3 ~ 0 (below the b-independent cluster onset) -> no coherent")
    print("background -> no stable kink. The above-onset sectors host SOFT")
    print("kinks (r_b ~ 0.43-0.53, not ~1); their kink-mass ratios are")
    print("sqrt(K_n r_b)/sqrt(K_1 r_1) ~ 0.76-0.88, close to the original")
    print("cascade_rn_compute numbers (which were right as r_b values).")
    print()
    print("Bridge to spin-statistics: under the field half-twist theta->theta+pi,")
    print("r_m -> (-1)^m r_m, so odd harmonics are the antisymmetric (fermionic)")
    print("modes (sine_gordon_substrate.md: half-twist => spin-statistics, CPT).")
    print("The clarinet (odd-harmonic) sector is the antiperiodic/fermionic one;")
    print("its kink is the carrier of the Z_2-graded (Q mod 2) topological charge.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
