#!/usr/bin/env python3
"""b-harmonic Kuramoto simulation: does each cascade sector actually lock?

Measures the b-cluster order parameter r_b = |<e^{i b theta}>| by direct
simulation of

    dtheta_i/dt = omega_i + (K/N) sum_j sin(b (theta_j - theta_i))
                = omega_i + K R_b sin(Psi_b - b theta_i)

with omega_i ~ Lorentzian (HWHM gamma = 1/pi, so the standard-Kuramoto
onset is K_c = 2 gamma = 2/pi, the framework's critical coupling).

Purpose: settle whether the clarinet sector (K = 3^(-1/2) = 0.577)
hosts a coherent b=3 cluster background (=> a kink) or not. The
b-harmonic onset is b-INDEPENDENT (phi = b theta maps to standard
Kuramoto with freqs b*omega and coupling b*K, the b's cancel:
K_c = 2 gamma for all b), so the discriminator is simply whether
K_n exceeds 2/pi.

This is the "square vs triangle" question made quantitative: a coherent
b-cluster background (r_b > 0) is a sharp, plateaued (square-wave-like)
profile that hosts kink steps; r_b -> 0 is the smooth (sinusoid/triangle)
regime with no localized kink.

Run: python3 cascade_kink_onset.py     (pure stdlib; ~1 min)
"""
from __future__ import annotations

import cmath
import math

GAMMA = 1.0 / math.pi          # Lorentzian HWHM -> K_c = 2*gamma = 2/pi
K_C = 2.0 * GAMMA              # 0.63662
N = 800
DT = 0.05
N_STEPS = 2400
N_AVG = 800                   # average r_b over the final N_AVG steps


def lorentz_freqs(n: int, gamma: float) -> list[float]:
    """Deterministic Lorentzian quantiles (low-noise, reproducible)."""
    return [gamma * math.tan(math.pi * ((i + 0.5) / n - 0.5)) for i in range(n)]


def simulate_rb(K: float, b: int, freqs: list[float]) -> float:
    n = len(freqs)
    # seed near a b-cluster splay so the locked branch (if stable) is found
    theta = [2 * math.pi * ((i % b) / b) + 0.01 * (i / n) for i in range(n)]
    acc, cnt = 0.0, 0
    for step in range(N_STEPS):
        z = sum(cmath.exp(1j * b * t) for t in theta) / n
        Rb, Psi = abs(z), cmath.phase(z)
        for i in range(n):
            theta[i] += DT * (freqs[i] + K * Rb * math.sin(Psi - b * theta[i]))
        if step >= N_STEPS - N_AVG:
            acc += Rb
            cnt += 1
    return acc / cnt


def closed_form(K: float) -> float:
    return math.sqrt(1 - K_C / K) if K > K_C else 0.0


def main() -> int:
    freqs = lorentz_freqs(N, GAMMA)
    print(f"K_c = 2/pi = {K_C:.4f}   (Lorentzian gamma = 1/pi, N = {N})")
    print("=" * 60)
    print("ONSET SCAN  (r_b vs K)")
    print(f"{'K':>6}{'r_2 (sim)':>11}{'r_3 (sim)':>11}{'sqrt(1-Kc/K)':>14}")
    print("-" * 60)
    for K in (0.45, 0.55, 0.637, 0.70, 0.80, 0.90, 1.00):
        r2 = simulate_rb(K, 2, freqs)
        r3 = simulate_rb(K, 3, freqs)
        print(f"{K:>6.3f}{r2:>11.3f}{r3:>11.3f}{closed_form(K):>14.3f}")

    print()
    print("AT THE CASCADE COUPLINGS")
    print(f"{'sector':<24}{'K_n':>8}{'b':>3}{'r_b (sim)':>11}{'verdict':>16}")
    print("-" * 60)
    sectors = [
        ("Z_6", 2.0 ** (-1 / 6), 2),
        ("Matter K*", 0.86196052, 2),
        ("Bowed (Salpeter)", 2.0 ** (-1 / 3), 2),
        ("Clarinet", 3.0 ** (-1 / 2), 3),
    ]
    for label, K, b in sectors:
        rb = simulate_rb(K, b, freqs)
        verdict = "kink (square)" if rb > 0.05 else "NO kink (triangle)"
        print(f"{label:<24}{K:>8.4f}{b:>3}{rb:>11.3f}{verdict:>16}")
    print("-" * 60)
    print("Reading: the b-cluster onset is b-independent (= K_c = 2/pi).")
    print("Clarinet K = 0.577 < K_c = 0.637 -> r_3 ~ 0 -> NO coherent")
    print("cluster background -> no stable kink (the smooth/triangle regime).")
    print("Z_6 / K* / bowed sit above onset -> coherent (square) -> kinks,")
    print("with modest r_b (soft kinks). So 'square vs triangle' IS")
    print("'above vs below the cluster-sync onset' = 'kink vs no kink'.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
