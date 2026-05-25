#!/usr/bin/env python3
"""The epsilon residual: per-captured binding energy is q-independent at K=1.

The K=1 mass baseline (mass_entrained_measure.md) writes a locked mode's
mass as M(p/q) = epsilon * N_cap, with N_cap = g0 * w(p/q) the captured-
oscillator count and epsilon the binding energy per captured oscillator.
The baseline left epsilon q-independent as an assumption. This closes it,
and shows where the two natural objections (mode survival; perturbation-
theory breakdown) actually enter.

THE ARGUMENT. Every Arnold tongue, whatever its order q, captures
oscillators at the SAME density. The tongue width is w(p/q) ~ 1/q^2 and the
K=1 bare-frequency density is uniform (Farey -> Lebesgue), g0, so the
captured density inside the tongue is

    rho_cap = N_cap / w = (g0 * w) / w = g0       (independent of q).

The internal synchronization that binds the captured band into one
coherent structure is a Kuramoto problem whose onset depends only on the
density, K_c = 2/(pi g0) -- also q-independent. Hence the internal order
parameter r = sqrt(1 - K_c/K) and the per-oscillator binding epsilon = K r
are q-INDEPENDENT. The mass is

    M(p/q) = epsilon * N_cap = (K r)(g0 / q^2)  ~  1/q^2,

with a q-independent prefactor. M ~ 1/q^2 is derived, not posited.

WHY THE PERTURBATIVE OBJECTION FAILS (the breakdown you have to invoke).
At small K the p/q lock is a q-th order resonance with well depth
V_q ~ K^q -- strongly q-dependent -- and one might expect the binding to
inherit that K^q. But the mass function lives at K=1 (criticality), where
perturbation theory breaks down: the tongues are O(1) with measure 1/q^2
(the non-perturbative Farey/Lebesgue structure), NOT K^q. At criticality
the entire q-dependence sits in the CAPTURE (the tongue width / N_cap);
the per-captured binding is the cluster coherence K r, fixed by the
universal capture density, not by the resonance depth. The q^q that
perturbation theory would put in epsilon is relocated to N_cap.

MODES THAT DO NOT SURVIVE. N_cap = g0/q^2 drops below one captured
oscillator for q > q_max ~ sqrt(g0). Those modes capture < 1 oscillator
and form no structure -- a physical high-q / low-mass cutoff that sets the
small end of the mass function (and does not touch the slope).

Run: python3 epsilon_residual.py
"""
from __future__ import annotations

import math

K = 1.0
K_C = 2.0 / math.pi


def main() -> int:
    g0 = 1.0
    r_int = math.sqrt(1 - K_C / K)
    eps = K * r_int
    print(f"K_c = 2/pi = {K_C:.4f};  internal order parameter "
          f"r = sqrt(1 - K_c/K) = {r_int:.4f}")
    print(f"per-captured binding  epsilon = K r = {eps:.4f}   (q-INDEPENDENT)")
    print()
    print(f"{'q':>4}{'w~1/q^2':>11}{'N_cap=g0*w':>12}{'rho_cap':>10}"
          f"{'epsilon':>9}{'M=eps*N':>11}")
    print("-" * 57)
    for q in (1, 2, 3, 4, 5, 10, 20):
        w = 1.0 / q**2
        ncap = g0 * w
        rho = ncap / w
        M = eps * ncap
        print(f"{q:>4}{w:>11.4f}{ncap:>12.4f}{rho:>10.4f}{eps:>9.4f}{M:>11.5f}")
    print("-" * 57)
    print("rho_cap is constant (= g0): every tongue captures at the uniform")
    print("K=1 density, so epsilon is the same for all q.")
    print()
    for Ntot in (1e4, 1e6, 1e9):
        print(f"  N_total = {Ntot:.0e}:  q_max ~ sqrt(N) = {Ntot**0.5:.0f}"
              f"   (q>q_max captures <1 oscillator -> no structure)")
    print()
    print("=> epsilon is q-independent: this result STANDS, and it is")
    print("   width-independent (it needs only uniform capture density, which")
    print("   holds whatever the tongue-width law). So M(p/q) ~ epsilon * w(p/q)")
    print("   with a constant prefactor.")
    print()
    print("   NOTE: the further step M ~ 1/q^2 -> slope -2 is NULL -- the")
    print("   physical width is w ~ q^(-beta), beta ~ 2.3 (> 2 forced by the")
    print("   complete K=1 staircase), not 1/q^2. See farey_tongue_width_null.py.")
    print("   So this closes the prefactor, not the -2 slope.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
