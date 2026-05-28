#!/usr/bin/env python3
"""Multi-cluster order parameter for the mode-locked cascade sectors.

A cascade sector locks into b symmetric phase clusters, where b is the
sector's cascade base (the acoustic overblow ratio: octave b = q_2 = 2
for the all-harmonic sectors, twelfth b = q_3 = 3 for the odd-harmonic
one; instrument_family_taxonomy.md). For a symmetric b-cluster state
theta_k = theta_0 + 2*pi*k/b (k = 0..b-1):

    r_m = <e^{i m theta}> = e^{i m theta_0}   if b | m,   else 0.

So r_1 = 0 for every b >= 2 sector -- identically, by symmetry, at any
coupling -- and the coherence lives in r_b (the base-th harmonic). The
b = 3 sector has r_1 = r_2 = 0 with coherence purely in r_3, its
odd-harmonic / three-fold signature. The single-cluster order parameter
r_1 is therefore the wrong coherence measure for a mode-locked sector;
r_b is the right one.

Whether r_b is actually nonzero -- a coherent background, hence a kink --
is a dynamical question: r_b is positive only above the cluster-sync
onset. cascade_kink_onset.py simulates the b-harmonic Kuramoto and finds
the onset is b-independent (= K_c = 2/pi), so the kink exists iff
K_n > K_c.

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
    print("r_1 = 0 for every b>=2 sector (symmetry); coherence is in r_b:")
    print("the all-harmonic sectors in r_2, the odd-harmonic one in r_3.")
    print("The b=3 odd-harmonic/three-fold structure IS the r_1=r_2=0,")
    print("r_3-coherent pattern. r_1 is not the right measure here.")
    print()

    # r_b (whether the cluster background is coherent) is dynamical;
    # values below are the b-harmonic Kuramoto measurement from
    # cascade_kink_onset.py. Onset is b-independent at K_c = 2/pi.
    print("KINK PRESENCE (r_b measured; see cascade_kink_onset.py):")
    sectors = [
        ("Z_6  (d,n,b)=(6,1,2)", 6, 1, 2, 0.525),
        ("K*   (d,n,b)=(14,3,2)", 14, 3, 2, 0.502),
        ("Bowed(d,n,b)=(3,1,2)", 3, 1, 2, 0.433),
        ("Odd  (d,n,b)=(2,1,3)", 2, 1, 3, 0.013),
    ]
    print(f"{'sector':<26}{'b^(-n/2d)':>11}{'r_b':>8}{'kink?':>20}")
    print("-" * 70)
    for label, d, n, b, rb in sectors:
        bound = b ** (-n / (2 * d))
        kink = "soft kink" if rb > 0.05 else "none (below onset)"
        print(f"{label:<26}{bound:>11.4f}{rb:>8.3f}{kink:>20}")
    print("-" * 70)
    print("The all-harmonic sectors (K_n > K_c) host soft kinks, r_b ~ 0.43-0.53,")
    print("mass ratios sqrt(K_n r_b)/sqrt(K_1 r_1) ~ 0.76-0.88. The odd-harmonic")
    print("sector sits at K = 3^(-1/2) = 0.577 < K_c = 0.637: r_3 ~ 0, no coherent")
    print("background, no stable kink.")
    print()
    print("Spin-statistics bridge: under the field half-twist theta->theta+pi,")
    print("r_m -> (-1)^m r_m, so odd harmonics are the antisymmetric (fermionic)")
    print("modes (sine_gordon_substrate.md: half-twist => spin-statistics, CPT).")
    print("The odd-harmonic sector is the antiperiodic/fermionic one; a kink there")
    print("carries the Z_2-graded (Q mod 2) topological charge.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
