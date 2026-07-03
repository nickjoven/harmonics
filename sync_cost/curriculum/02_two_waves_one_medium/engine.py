#!/usr/bin/env python3
"""
Module 2 — Two waves on one medium.

Three demonstrations:
  - "normalmodes" — two identical coupled pendula: linear coupling reorganizes
                    them into two orthogonal normal modes; energy sloshes fully
                    from one pendulum to the other (beating). No locking.
  - "locking"     — two phase oscillators of DIFFERENT natural frequency with
                    nonlinear (phase) coupling: below a threshold they drift;
                    above it they lock to a common rhythm (ratio 1:1). The
                    integer ratio emerges with no integer put in by hand.
  - "band"        — at fixed coupling, sweep the frequency mismatch: the locked
                    band has width |Δω| ≤ 2K. This is the first slice of an
                    Arnold tongue (Module 3).

Run with no arguments to run all three, or pass
--demo {normalmodes, locking, band}.

Pure standard library. RK4 integration; output is tables and an ASCII
energy-exchange strip. Every model is stated explicitly in-code so each
number is traceable.
"""
import argparse
import math


# --------------------------------------------------------------------------- #
# Part A — linear coupling: normal modes and beating (no locking)
# --------------------------------------------------------------------------- #
#
# Two identical pendula (natural frequency ω0) joined by a coupling spring κ:
#     x1'' = -ω0² x1 - κ (x1 - x2)
#     x2'' = -ω0² x2 - κ (x2 - x1)
#
# Normal coordinates  s = (x1 + x2)/√2,  d = (x1 - x2)/√2  decouple the system:
#     s'' = -ω0² s                 → symmetric  mode, frequency ω_s = ω0
#     d'' = -(ω0² + 2κ) d          → antisym.   mode, frequency ω_d = √(ω0² + 2κ)
#
# The (s, d) axes are a 45° rotation of the (x1, x2) axes — they are at 90° to
# each other. That right angle is the "force does no work" orthogonality role
# from Module 0: along a normal-mode axis, the coupling does no work that would
# transfer energy OUT of that mode. The modes evolve independently.

def _pendula_accel(x1, x2, w0sq, kappa):
    a1 = -w0sq * x1 - kappa * (x1 - x2)
    a2 = -w0sq * x2 - kappa * (x2 - x1)
    return a1, a2


def _rk4_pendula(state, dt, w0sq, kappa):
    x1, v1, x2, v2 = state

    def deriv(s):
        x1, v1, x2, v2 = s
        a1, a2 = _pendula_accel(x1, x2, w0sq, kappa)
        return (v1, a1, v2, a2)

    k1 = deriv(state)
    s2 = tuple(state[i] + 0.5 * dt * k1[i] for i in range(4))
    k2 = deriv(s2)
    s3 = tuple(state[i] + 0.5 * dt * k2[i] for i in range(4))
    k3 = deriv(s3)
    s4 = tuple(state[i] + dt * k3[i] for i in range(4))
    k4 = deriv(s4)
    return tuple(
        state[i] + (dt / 6.0) * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i])
        for i in range(4)
    )


def demo_normalmodes():
    print("=" * 68)
    print("Part A — linear coupling: normal modes and beating (no locking)")
    print("=" * 68)
    print()
    w0 = 1.0
    w0sq = w0 * w0
    kappa = 0.2
    w_s = math.sqrt(w0sq)             # symmetric-mode frequency
    w_d = math.sqrt(w0sq + 2 * kappa)  # antisymmetric-mode frequency
    print(f"Two identical pendula, ω0 = {w0:.3f}, coupling κ = {kappa:.3f}.")
    print(f"Normal-mode frequencies: ω_s = ω0 = {w_s:.5f}  (symmetric, in phase)")
    print(f"                         ω_d = √(ω0²+2κ) = {w_d:.5f}  (antisym., "
          f"out of phase)")
    print()
    print("Start pendulum 1 displaced, pendulum 2 at rest. Energy fraction in")
    print("pendulum 1 over time (■ = fraction of total energy in pendulum 1):")
    print()

    state = (1.0, 0.0, 0.0, 0.0)  # x1, v1, x2, v2
    dt = 0.01
    T = 70.0
    steps = int(T / dt)
    sample_every = int(2.5 / dt)  # sample every 2.5 time units

    for step in range(steps + 1):
        if step % sample_every == 0:
            x1, v1, x2, v2 = state
            e1 = 0.5 * v1 * v1 + 0.5 * w0sq * x1 * x1
            e2 = 0.5 * v2 * v2 + 0.5 * w0sq * x2 * x2
            frac = e1 / (e1 + e2) if (e1 + e2) > 1e-12 else 0.0
            t = step * dt
            bar = "■" * int(round(frac * 40))
            print(f"  t={t:5.1f}  E1={frac:4.2f}  {bar}")
        state = _rk4_pendula(state, dt, w0sq, kappa)

    beat_period = 2 * math.pi / (w_d - w_s)
    print()
    print(f"Energy transfers fully from pendulum 1 to pendulum 2 and back with")
    print(f"beat period 2π/(ω_d − ω_s) = {beat_period:.2f}. The two pendula")
    print("EXCHANGE energy — they never settle into a shared locked rhythm.")
    print("Linear coupling reorganizes; it does not lock.")
    print()


# --------------------------------------------------------------------------- #
# Part B — nonlinear (phase) coupling: locking (integers emerge)
# --------------------------------------------------------------------------- #
#
# Two phase oscillators with different natural frequencies, symmetric coupling:
#     θ1' = ω1 + K sin(θ2 − θ1)
#     θ2' = ω2 + K sin(θ1 − θ2)
#
# The phase difference φ = θ2 − θ1 obeys the Adler equation
#     φ' = Δω − 2K sin φ,   Δω = ω2 − ω1
# which has a fixed point (lock) sin φ* = Δω/(2K) iff |Δω| ≤ 2K, i.e.
#     K ≥ K_c = |Δω| / 2.
# Below threshold, φ drifts and the observed beat frequency is
#     Ω_beat = √(Δω² − (2K)²),
# which → 0 as K → K_c from below (critical slowing).

def _rk4_phase(theta1, theta2, dt, w1, w2, K):
    def deriv(t1, t2):
        return (w1 + K * math.sin(t2 - t1),
                w2 + K * math.sin(t1 - t2))

    d1a, d2a = deriv(theta1, theta2)
    d1b, d2b = deriv(theta1 + 0.5 * dt * d1a, theta2 + 0.5 * dt * d2a)
    d1c, d2c = deriv(theta1 + 0.5 * dt * d1b, theta2 + 0.5 * dt * d2b)
    d1d, d2d = deriv(theta1 + dt * d1c, theta2 + dt * d2c)
    theta1 += (dt / 6.0) * (d1a + 2 * d1b + 2 * d1c + d1d)
    theta2 += (dt / 6.0) * (d2a + 2 * d2b + 2 * d2c + d2d)
    return theta1, theta2


def _measure_beat(w1, w2, K, dt=0.01, T=1500.0):
    """Integrate the pair; return |Ω2 − Ω1| measured over the second half."""
    theta1, theta2 = 0.0, 0.0
    half = int((T / 2) / dt)
    steps = int(T / dt)
    for _ in range(half):
        theta1, theta2 = _rk4_phase(theta1, theta2, dt, w1, w2, K)
    t1_mid, t2_mid = theta1, theta2
    for _ in range(steps - half):
        theta1, theta2 = _rk4_phase(theta1, theta2, dt, w1, w2, K)
    span = (steps - half) * dt
    omega1 = (theta1 - t1_mid) / span
    omega2 = (theta2 - t2_mid) / span
    return abs(omega2 - omega1)


def demo_locking():
    print("=" * 68)
    print("Part B — nonlinear coupling: locking (the integer emerges)")
    print("=" * 68)
    print()
    w1, w2 = 1.0, 1.6
    dwn = w2 - w1
    Kc = abs(dwn) / 2.0
    print(f"Two phase oscillators, natural frequencies ω1 = {w1:.3f}, "
          f"ω2 = {w2:.3f}.")
    print(f"Frequency mismatch Δω = {dwn:.3f}. Predicted lock threshold "
          f"K_c = Δω/2 = {Kc:.3f}.")
    print()
    print("No integer is anywhere in these inputs — only three real numbers")
    print("(ω1, ω2, K). Sweep the coupling K and measure the beat between the")
    print("two observed frequencies:")
    print()
    print(f"{'K':>8}  {'K/K_c':>7}  {'measured beat':>14}  "
          f"{'√(Δω²−(2K)²)':>14}  {'state':>10}")
    print(f"{'-'*8}  {'-'*7}  {'-'*14}  {'-'*14}  {'-'*10}")
    for K in [0.0, 0.10, 0.20, 0.25, 0.29, 0.30, 0.35, 0.45, 0.60]:
        beat = _measure_beat(w1, w2, K)
        arg = dwn * dwn - (2 * K) ** 2
        analytic = math.sqrt(arg) if arg > 0 else 0.0
        locked = beat < 1e-3
        state = "LOCKED 1:1" if locked else "drifting"
        print(f"{K:>8.3f}  {K/Kc:>7.2f}  {beat:>14.5f}  "
              f"{analytic:>14.5f}  {state:>10}")
    print()
    print("Below K_c the two run at different rates and the beat matches")
    print("√(Δω²−(2K)²), shrinking to zero as K → K_c (critical slowing). At and")
    print("above K_c the beat is zero: both oscillators run at ONE shared")
    print("frequency. The ratio is exactly 1:1 — an integer that was never put")
    print("in. It is the attractor of the coupling dynamics.")
    print()


# --------------------------------------------------------------------------- #
# Part C — the locked band: first slice of a tongue
# --------------------------------------------------------------------------- #

def demo_band():
    print("=" * 68)
    print("Part C — the locked band widens with coupling (a tongue begins)")
    print("=" * 68)
    print()
    w1 = 1.0
    K = 0.30
    band_half = 2 * K  # locks when |Δω| ≤ 2K
    print(f"Fix ω1 = {w1:.3f} and coupling K = {K:.3f}. Vary the second")
    print(f"oscillator's frequency ω2, i.e. the mismatch Δω. Prediction: the")
    print(f"pair locks 1:1 whenever |Δω| ≤ 2K = {band_half:.3f}.")
    print()
    print(f"{'Δω':>8}  {'|Δω| ≤ 2K ?':>12}  {'measured beat':>14}  {'state':>10}")
    print(f"{'-'*8}  {'-'*12}  {'-'*14}  {'-'*10}")
    for dwn in [0.0, 0.20, 0.40, 0.55, 0.60, 0.62, 0.65, 0.80, 1.00]:
        w2 = w1 + dwn
        beat = _measure_beat(w1, w2, K)
        predict_lock = abs(dwn) <= band_half + 1e-9
        locked = beat < 1e-3
        state = "LOCKED 1:1" if locked else "drifting"
        flag = "yes" if predict_lock else "no"
        print(f"{dwn:>8.3f}  {flag:>12}  {beat:>14.5f}  {state:>10}")
    print()
    print(f"The lock holds out to Δω = 2K = {band_half:.3f} and breaks beyond it.")
    print("Raise K and the band widens; lower it and the band narrows. Plotted")
    print("in the (Δω, K) plane, the locked region is a wedge rising from the")
    print("point Δω = 0 — the first Arnold tongue (Module 3). There is one such")
    print("wedge above EVERY rational frequency ratio, not just 1:1.")
    print()


# --------------------------------------------------------------------------- #

def main():
    parser = argparse.ArgumentParser(description="Module 2 demonstrations.")
    parser.add_argument(
        "--demo",
        choices=["normalmodes", "locking", "band", "all"],
        default="all",
        help="Which demonstration to run.",
    )
    args = parser.parse_args()

    if args.demo in ("normalmodes", "all"):
        demo_normalmodes()
    if args.demo in ("locking", "all"):
        demo_locking()
    if args.demo in ("band", "all"):
        demo_band()


if __name__ == "__main__":
    main()
