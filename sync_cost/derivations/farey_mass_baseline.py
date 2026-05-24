#!/usr/bin/env python3
"""K=1 baseline mass-function slope from the Farey mode-counting measure.

Attempt to nativize the -2 baseline of the bowed-cascade slope
alpha = -q_2 - n/d (imf_bowed_cascade.md). The -2 was previously imported
as the standard fragmentation result -1 - log_2(2) and relabeled -q_2.
Here it is derived from framework-native objects only:

  (1) Mode count. The locked modes are the Farey/Stern-Brocot fractions
      p/q; the count with denominator <= n is |F_n| ~ (3/pi^2) n^2, so the
      mode density grows as dN/dq ~ q.

  (2) Mass = entrained measure. A locked mode p/q commands an Arnold
      tongue of width w(p/q) ~ 1/q^2 at K=1 (the Farey measure, which ->
      Lebesgue at criticality). The framework's core primitive is
      "energy = synchronization cost = the phase-space volume a mode
      entrains", so a structure's mass is M ~ w(p/q) ~ 1/q^2. The
      simplest ratios (small q, widest tongues) are the heaviest.

  Then N(>=M) = #modes with q <= M^(-1/2) = |F_{M^(-1/2)}| ~ M^(-1), and
  the differential mass function is dN/dM = |d N(>=M)/dM| ~ M^(-2).

  Slope alpha = -2 = -q_2. The "-1" Jacobian that used to be imported is
  now the dq/dM Jacobian of the tongue-width mass map -- derived, not
  assumed. NOTE this is a THIRD mass concept, distinct from the soliton
  kink mass (~ sqrt(Kr)) and the ADM gravitational mass (~ sqrt(rho));
  it is the only one with the measure-theoretic shape the slope needs.

This script verifies the cumulative slope numerically; the differential
slope is the cumulative slope minus 1 (the integration relation).

Run: python3 farey_mass_baseline.py
"""
from __future__ import annotations

from math import log, pi


def euler_phi(n: int) -> int:
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


def main() -> int:
    N = 6000
    phi = [0] + [euler_phi(q) for q in range(1, N + 1)]
    cumF = [0] * (N + 1)          # |F_q| up to denominator q (interior count)
    run = 0
    for q in range(1, N + 1):
        run += phi[q]
        cumF[q] = run

    print("=" * 60)
    print("K=1 BASELINE SLOPE FROM THE FAREY MODE-COUNTING MEASURE")
    print("=" * 60)
    print(f"(1) Farey count |F_n| ~ (3/pi^2) n^2:")
    for q in (1000, 3000, 6000):
        print(f"    |F_{q}| = {cumF[q]:>9}   (3/pi^2)q^2 = {3/pi**2*q*q:>11.0f}"
              f"   ratio {cumF[q]/(3/pi**2*q*q):.4f}")
    print()

    # (2) mass M_q = 1/q^2; cumulative N(>=M_q) = |F_q|.
    # fit log|F_q| vs log M_q over a clean mid-range of q.
    xs, ys = [], []
    for q in range(50, N + 1):
        M = 1.0 / (q * q)
        xs.append(log(M))
        ys.append(log(cumF[q]))
    n = len(xs)
    sx, sy = sum(xs), sum(ys)
    sxx = sum(x * x for x in xs)
    sxy = sum(x * y for x, y in zip(xs, ys))
    cum_slope = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    diff_slope = cum_slope - 1.0   # dN/dM exponent = cumulative exponent - 1

    print(f"(2) mass = tongue-width measure M ~ 1/q^2")
    print(f"    cumulative  N(>=M) ~ M^({cum_slope:.4f})     (expected -1)")
    print(f"    differential dN/dM ~ M^({diff_slope:.4f})    (expected -2 = -q_2)")
    print()
    print("RESULT: alpha_baseline = -2 = -q_2, derived from the Farey mode")
    print("count (|F_n| ~ n^2) + the tongue-width mass map (M ~ 1/q^2 =")
    print("entrained synchronization cost). The imported '-1' and 'mass-")
    print("halving' are replaced by one native identification (mass =")
    print("entrained measure); the '-1' is now the dq/dM Jacobian.")
    print()
    print("Scope: this is the K=1 baseline only. The K<1 cascade correction")
    print("-n/d = -1/q_3 (-> -7/3) is the separate, Step-2-grounded piece")
    print("(imf_step2_klein_orbit.py). The mass=tongue-width identification")
    print("is derived from the synchronization-cost functional in")
    print("mass_entrained_measure.md (modulo a q-independent binding energy).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
