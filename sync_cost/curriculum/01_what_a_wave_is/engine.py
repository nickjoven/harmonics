#!/usr/bin/env python3
"""
Module 1 — What a wave is.

Four demonstrations:
  - "restore"  — a particle in a parabolic well with no inertia: snaps to rest, no oscillation
  - "inertia"  — same well with inertia: oscillation; period scales as √(m/k)
  - "wave"     — a chain of coupled points with all three ingredients: outward propagation
  - "doppler"  — observer moving relative to a wave's medium: measured frequency shifts

Run with no arguments to run all four, or pass --demo {restore, inertia, wave, doppler}.

Pure standard library. No matplotlib required; output is tables and ASCII
profiles that make each construction visible numerically.
"""
import argparse
import math


# --------------------------------------------------------------------------- #
# Ingredient 1: restoration (no inertia)
# --------------------------------------------------------------------------- #

def demo_restore():
    """A particle in a parabolic well with no inertia. Snaps to rest; does not oscillate."""
    print("=" * 64)
    print("Ingredient 1 — restoration alone (no inertia)")
    print("=" * 64)
    print()
    print("A particle in a parabolic potential well: U(x) = (1/2)·k·x².")
    print("Restoring force F(x) = -k·x is linear in displacement.")
    print()
    print(f"{'x':>10}  {'F = -k·x  (k=1)':>18}")
    print(f"{'-' * 10}  {'-' * 18}")
    for x in [-2, -1, -0.5, 0, 0.5, 1, 2]:
        F = -1.0 * x
        print(f"{x:>10.2f}  {F:>18.4f}")
    print()
    print("With no inertia (massless particle), velocity is set instantaneously")
    print("by the force. The particle accelerates, but with zero mass it cannot")
    print("'store' kinetic energy: it tracks the restoring force exactly and")
    print("settles at x = 0 with no overshoot. No oscillation.")
    print()
    print("Restoration alone is not enough for a wave.")
    print()


# --------------------------------------------------------------------------- #
# Ingredient 2: restoration + inertia (oscillation at a single point)
# --------------------------------------------------------------------------- #

def simulate_oscillator(mass, stiffness, x0=1.0, v0=0.0, dt=0.01, n_steps=2000):
    """Symplectic (leapfrog) integration of m·ẍ = -k·x."""
    x = x0
    v = v0
    times, xs = [], []
    for i in range(n_steps):
        # leapfrog half-step
        F = -stiffness * x
        v += 0.5 * dt * F / mass
        x += dt * v
        F = -stiffness * x
        v += 0.5 * dt * F / mass
        times.append((i + 1) * dt)
        xs.append(x)
    return times, xs


def measured_period(times, xs):
    """Estimate period from first two upward zero-crossings."""
    crossings = []
    for i in range(1, len(xs)):
        if xs[i - 1] <= 0 < xs[i]:
            t_cross = times[i - 1] + (times[i] - times[i - 1]) * (
                -xs[i - 1] / (xs[i] - xs[i - 1])
            )
            crossings.append(t_cross)
            if len(crossings) == 2:
                return crossings[1] - crossings[0]
    return None


def demo_inertia():
    """Restoration + inertia: oscillation. Period scales as √(m/k)."""
    print("=" * 64)
    print("Ingredient 2 — restoration + inertia (oscillation)")
    print("=" * 64)
    print()
    print("Same parabolic well, now with mass. The particle overshoots rest;")
    print("oscillates sinusoidally. Predicted period: T = 2π·√(m/k).")
    print()
    print(f"{'mass m':>10}  {'stiffness k':>12}  {'measured T':>12}  "
          f"{'predicted 2π√(m/k)':>22}")
    print(f"{'-' * 10}  {'-' * 12}  {'-' * 12}  {'-' * 22}")
    k = 1.0
    for m in [0.25, 0.5, 1.0, 2.0, 4.0]:
        # Use a timestep small enough for the fastest case
        dt = 0.005 * math.sqrt(m / k)
        times, xs = simulate_oscillator(m, k, dt=dt, n_steps=4000)
        T_meas = measured_period(times, xs)
        T_pred = 2 * math.pi * math.sqrt(m / k)
        meas_str = f"{T_meas:.4f}" if T_meas else "n/a"
        print(f"{m:>10.4f}  {k:>12.4f}  {meas_str:>12}  {T_pred:>22.4f}")
    print()
    print("Measured periods match 2π·√(m/k) to integration accuracy.")
    print("This is oscillation at a single point — still not a wave.")
    print()


# --------------------------------------------------------------------------- #
# Ingredient 3: coupling (chain → outward propagation)
# --------------------------------------------------------------------------- #

def simulate_chain(N, mass, stiffness_rest, stiffness_coup, dt, n_steps,
                   impulse_index, impulse_velocity):
    """
    Integrate N coupled points with restoring + coupling forces.
    Returns list of (time, displacement profile) snapshots.
    """
    x = [0.0] * N
    v = [0.0] * N
    v[impulse_index] = impulse_velocity

    snapshots = [(0.0, list(x))]
    snap_every = max(1, n_steps // 6)

    for step in range(1, n_steps + 1):
        # leapfrog
        # accelerations
        a = [0.0] * N
        for i in range(N):
            F = -stiffness_rest * x[i]
            if i > 0:
                F += stiffness_coup * (x[i - 1] - x[i])
            if i < N - 1:
                F += stiffness_coup * (x[i + 1] - x[i])
            a[i] = F / mass
        # first half-kick
        for i in range(N):
            v[i] += 0.5 * dt * a[i]
        # drift
        for i in range(N):
            x[i] += dt * v[i]
        # recompute a after drift
        for i in range(N):
            F = -stiffness_rest * x[i]
            if i > 0:
                F += stiffness_coup * (x[i - 1] - x[i])
            if i < N - 1:
                F += stiffness_coup * (x[i + 1] - x[i])
            a[i] = F / mass
        # second half-kick
        for i in range(N):
            v[i] += 0.5 * dt * a[i]

        if step % snap_every == 0:
            snapshots.append((step * dt, list(x)))

    return snapshots


def ascii_profile(xs, width=60, scale=1.5):
    """Render a displacement profile as an ASCII strip."""
    out = []
    for x in xs:
        if x > 0:
            n = max(0, min(width // 2, int(round((x / scale) * (width // 2)))))
            out.append(" " * (width // 2) + "█" * n)
        elif x < 0:
            n = max(0, min(width // 2, int(round((-x / scale) * (width // 2)))))
            out.append(" " * (width // 2 - n) + "█" * n + " " * n)
        else:
            out.append(" " * (width // 2) + "·")
    return out


def demo_wave():
    """A chain of fifty coupled points; impulse at the middle; outward propagation."""
    print("=" * 64)
    print("Ingredient 3 — coupling (the wave appears)")
    print("=" * 64)
    print()
    print("Fifty points in a line. Each has restoring force (k_rest = 0.05),")
    print("inertia (m = 1.0), and is coupled to its neighbors with stiffness")
    print("k_coup = 1.0 — a force proportional to the difference in their")
    print("displacements. An impulse is delivered to point #25 at t = 0.")
    print()
    N = 50
    snaps = simulate_chain(
        N=N, mass=1.0, stiffness_rest=0.05, stiffness_coup=1.0,
        dt=0.05, n_steps=600,
        impulse_index=N // 2, impulse_velocity=1.0,
    )
    # show 5 snapshots (skip the t=0 trivial one)
    chosen = snaps[1:6]
    print(f"Displacement profile at successive times. Point index 0..{N - 1}")
    print(f"runs left to right. '█' marks displacement magnitude (column = point).")
    print()
    for t, xs in chosen:
        print(f"  t = {t:5.2f}")
        # show as a single-line strip: + signs above axis, - signs below
        bar = []
        for x in xs:
            mag = abs(x)
            if mag < 0.01:
                ch = " "
            elif mag < 0.1:
                ch = "·"
            elif mag < 0.3:
                ch = "▂"
            elif mag < 0.6:
                ch = "▄"
            elif mag < 1.0:
                ch = "▆"
            else:
                ch = "█"
            bar.append(ch)
        print("    " + "".join(bar))
        print()
    print("The impulse, initially localised at point #25, spreads outward in")
    print("both directions. The two fronts move at the same speed — set by")
    print("√(k_coup / m) = " + f"{math.sqrt(1.0 / 1.0):.4f} (cells per unit time).")
    print()
    print("Restoration + inertia + coupling = a wave.")
    print()


# --------------------------------------------------------------------------- #
# Observation: Doppler (frequency shift from observer motion)
# --------------------------------------------------------------------------- #

def demo_doppler():
    """Observer moving relative to the medium. Measured frequency shifts."""
    print("=" * 64)
    print("Observation — observer motion shifts the measured frequency")
    print("=" * 64)
    print()
    print("A source emits a wave at fixed frequency f_s. The wave travels through")
    print("a medium at speed c. An observer at position x_obs moves through the")
    print("medium at velocity v_obs. The frequency the observer measures is:")
    print()
    print("    f_obs = f_s · (1 − v_obs / c)")
    print()
    print("(positive v_obs = observer moves away from the source).")
    print()
    f_s = 1.0
    c = 1.0
    print(f"f_s = {f_s:.2f} Hz, wave speed c = {c:.2f}")
    print()
    print(f"{'v_obs / c':>10}  {'observer state':>22}  {'f_obs':>10}  "
          f"{'shift':>10}")
    print(f"{'-' * 10}  {'-' * 22}  {'-' * 10}  {'-' * 10}")
    for ratio in [-0.5, -0.2, -0.1, 0.0, 0.1, 0.2, 0.5]:
        f_obs = f_s * (1.0 - ratio)
        if ratio < 0:
            state = "approaching source"
        elif ratio > 0:
            state = "receding from source"
        else:
            state = "stationary"
        shift = f_obs - f_s
        print(f"{ratio:>10.2f}  {state:>22}  {f_obs:>10.4f}  {shift:>+10.4f}")
    print()
    print("The wave itself did not change. The relative motion through the")
    print("medium changed what the observer measures. This is the first of")
    print("the six observations promised at the end of the module.")
    print()


# --------------------------------------------------------------------------- #

def main():
    parser = argparse.ArgumentParser(description="Module 1 demonstrations.")
    parser.add_argument(
        "--demo",
        choices=["restore", "inertia", "wave", "doppler", "all"],
        default="all",
        help="Which demonstration to run.",
    )
    args = parser.parse_args()

    if args.demo in ("restore", "all"):
        demo_restore()
    if args.demo in ("inertia", "all"):
        demo_inertia()
    if args.demo in ("wave", "all"):
        demo_wave()
    if args.demo in ("doppler", "all"):
        demo_doppler()


if __name__ == "__main__":
    main()
