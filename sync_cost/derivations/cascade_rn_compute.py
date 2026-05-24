#!/usr/bin/env python3
"""Compute the sector order parameter r(K_n) and the kink-mass flow.

SUPERSEDED FOR THE K<1 SECTORS — see cascade_cluster_order.py. This
script uses the SINGLE-CLUSTER order parameter r_1 = sqrt(1 - K_c/K),
which is correct only at the K=1 boundary (full lock). The mode-locked
cascade sectors split into b symmetric phase clusters, where r_1 = 0
identically by symmetry and the coherence lives in r_b. The clarinet
"below onset, r=0" finding below is an ARTIFACT of measuring r_1 for a
three-cluster state; with the correct r_b measure the clarinet kink
exists (~0.760). Kept for the record and the boundary case.

The sine-Gordon reduction falls out at every cascade-locked sector
(structurally forced; sine_gordon_substrate.md "net-state update"),
giving kink mass M_k = 8 sigma sqrt(K r). The only sector-dependent
unknown is r_n. sqrt_r_n_correction.md names "direct rfe-style
Kuramoto measurement" as a closure route: r_n is the self-consistent
Kuramoto order parameter at coupling K_n.

This script runs that route in its closed mean-field form. For the
standard (Lorentzian g(omega)) Kuramoto self-consistency,

    r(K) = sqrt(1 - K_c / K)   for K > K_c,   else 0,

with the framework's critical coupling K_c = 2/pi (README "second
clarifying note"; prototype metronome wall). It then forms the
kink-mass ratio M_k(K_n)/M_k(K=1) = sqrt(K_n r_n) / sqrt(K_1 r_1)
and compares to the bare bound b^(-n/(2d)) (the r_n = 1 limit).

CAVEAT (Class-2, stated honestly): r(K) = sqrt(1 - K_c/K) is the
GLOBAL mean-field order parameter for a spread (Lorentzian) ensemble.
A cascade sector is LOCALLY mode-locked to a rational p/q, so its
coherence may be the local tongue order parameter rather than the
global one. The two routes (global Kuramoto here vs. tongue-width
r ~ 2(K/2)^q) can disagree; that route-dependence IS the residual
Class-2 freedom. Results below are the global-Kuramoto route.

Run: python3 cascade_rn_compute.py
"""
from __future__ import annotations

import math
from dataclasses import dataclass

K_C = 2.0 / math.pi  # framework critical coupling ~ 0.63662


@dataclass
class Sector:
    label: str
    K: float
    d: int | None   # cascade depth (None for the n=0 boundary)
    n: int
    b: int | None   # cascade base


SECTORS = [
    Sector("K=1 boundary (string)", 1.0, None, 0, None),
    Sector("Z_6 (conjectured)", 2.0 ** (-1 / 6), 6, 1, 2),
    Sector("Matter equilibrium K*", 0.86196052, 14, 3, 2),
    Sector("Bowed (IMF / Salpeter)", 2.0 ** (-1 / 3), 3, 1, 2),
    Sector("Clarinet (q_3 cascade)", 3.0 ** (-1 / 2), 2, 1, 3),
]


def r_kuramoto(K: float) -> float:
    """Self-consistent Kuramoto order parameter (Lorentzian g)."""
    if K <= K_C:
        return 0.0
    return math.sqrt(1.0 - K_C / K)


def bare_bound(s: Sector) -> float:
    """b^(-n/(2d)): the r_n = 1 kink-mass-ratio bound."""
    if s.n == 0 or s.d is None or s.b is None:
        return 1.0
    return s.b ** (-s.n / (2.0 * s.d))


def main() -> int:
    print("=" * 76)
    print(f"SECTOR ORDER PARAMETER r(K_n)   (K_c = 2/pi = {K_C:.5f})")
    print("=" * 76)

    r1 = r_kuramoto(1.0)  # boundary order parameter, same self-consistency
    Mk1 = math.sqrt(1.0 * r1)

    hdr = (f"{'sector':<26}{'K_n':>9}{'r_n':>9}"
           f"{'M_k/M_k(1)':>12}{'bare bnd':>10}{'sqrt(r_n) f':>12}")
    print(hdr)
    print("-" * 76)
    for s in SECTORS:
        r = r_kuramoto(s.K)
        if r == 0.0:
            Mk_ratio = 0.0
            sqrt_factor = 0.0
        else:
            Mk = math.sqrt(s.K * r)
            Mk_ratio = Mk / Mk1
            sqrt_factor = math.sqrt(r / r1)
        bnd = bare_bound(s)
        flag = "  <-- BELOW ONSET" if r == 0.0 else ""
        print(f"{s.label:<26}{s.K:>9.4f}{r:>9.4f}"
              f"{Mk_ratio:>12.4f}{bnd:>10.4f}{sqrt_factor:>12.4f}{flag}")

    print("-" * 76)
    print("Columns: r_n self-consistent Kuramoto order parameter; "
          "M_k/M_k(1) = sqrt(K_n r_n)/sqrt(K_1 r_1);")
    print("bare bnd = b^(-n/2d) (r_n=1 limit); sqrt(r_n) f = "
          "sqrt(r_n/r_1) = the residual correction.")
    print()
    print("Findings:")
    print(f"  - r_1 (boundary, K=1) = {r1:.4f} under the spread ensemble.")
    print("  - sqrt(r_n) correction is 0.86-0.94 for Z_6 / K* / bowed:")
    print("    a modest few-to-15% pull below the bare bound, now COMPUTED,")
    print("    not a free parameter.")
    print(f"  - Clarinet K = 3^(-1/2) = {3.0**-0.5:.4f} < K_c = {K_C:.4f}:")
    print("    BELOW the Kuramoto sync onset -> r=0 -> no coherent kink in")
    print("    the global-mean-field route. Either the steepest cascade")
    print("    hosts no stable soliton, or its coherence is purely local")
    print("    (tongue) and the global order parameter is the wrong measure.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
