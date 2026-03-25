#!/usr/bin/env python3
"""
Coherence length on the Möbius ring: arm formation and topological snap.

At small N, the twist dominates immediately. At large N, coherent arms
form freely, propagate, and snap to quantized gradients when the
reflected wavefront arrives.

Measures:
  - Time-resolved r(t) to detect the reflection event
  - Local phase gradient to count coherent arms
  - Arm length distribution at steady state
  - Comparison: periodic BC (no reflection, no snap)
"""

import numpy as np


def kuramoto_ring(theta, omega, K, antiperiodic=True):
    """Kuramoto nearest-neighbor on a ring."""
    N = len(theta)
    dtheta = omega.copy()
    for i in range(N):
        if i > 0:
            left = theta[i - 1]
        else:
            left = theta[N - 1] - (np.pi if antiperiodic else 0)

        if i < N - 1:
            right = theta[i + 1]
        else:
            right = theta[0] + (np.pi if antiperiodic else 0)

        dtheta[i] += (K / 2) * (np.sin(right - theta[i])
                                 + np.sin(left - theta[i]))
    return dtheta


def rk4(theta, omega, K, dt, antiperiodic=True):
    f = lambda th: kuramoto_ring(th, omega, K, antiperiodic)
    k1 = f(theta)
    k2 = f(theta + 0.5 * dt * k1)
    k3 = f(theta + 0.5 * dt * k2)
    k4 = f(theta + dt * k3)
    return theta + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)


def count_arms(theta):
    """Count coherent arms by detecting sign changes in the phase gradient."""
    N = len(theta)
    diffs = np.array([((theta[(i + 1) % N] - theta[i] + np.pi)
                       % (2 * np.pi)) - np.pi for i in range(N)])

    # An arm boundary is where the gradient changes sign or jumps
    # Use threshold: gradient magnitude > π/2 indicates a break
    breaks = 0
    for i in range(N):
        if abs(diffs[i]) > np.pi / 2:
            breaks += 1

    # Arms = breaks (each break separates two arms), minimum 1
    return max(breaks, 1)


def measure_arm_lengths(theta):
    """Measure lengths of coherent arms (segments with smooth gradient)."""
    N = len(theta)
    diffs = np.array([((theta[(i + 1) % N] - theta[i] + np.pi)
                       % (2 * np.pi)) - np.pi for i in range(N)])

    # Find break points (large jumps)
    breaks = []
    for i in range(N):
        if abs(diffs[i]) > np.pi / 2:
            breaks.append(i)

    if not breaks:
        return [N]  # one arm spanning everything

    # Arm lengths between consecutive breaks
    lengths = []
    for k in range(len(breaks)):
        start = breaks[k]
        end = breaks[(k + 1) % len(breaks)]
        length = (end - start) % N
        if length > 0:
            lengths.append(length)

    return lengths if lengths else [N]


def detect_reflection_time(r_history, dt, window=50):
    """Detect when the order parameter first changes slope (reflection event).

    Look for the first local minimum in dr/dt after the initial growth.
    """
    if len(r_history) < 2 * window:
        return None

    # Smooth r
    kernel = np.ones(window) / window
    r_smooth = np.convolve(r_history, kernel, mode='valid')

    # Find first local minimum after initial rise
    dr = np.diff(r_smooth)
    rising = False
    for i in range(len(dr)):
        if dr[i] > 0:
            rising = True
        elif rising and dr[i] < 0:
            # First downturn after rise
            return (i + window // 2) * dt
    return None


def run_sweep(N, K_ratio, gamma=1.0, epsilon=0.1, dt=0.01, T=300.0,
              seed=42, antiperiodic=True):
    """Run one simulation and extract coherence diagnostics."""
    rng = np.random.default_rng(seed)

    K_c = 2 * gamma / np.sin(np.pi / (2 * N))
    K = K_ratio * K_c

    omega = gamma * np.clip(rng.standard_cauchy(N), -10, 10)
    theta = np.zeros(N)
    theta[0] = epsilon

    n_steps = int(T / dt)
    r_hist = np.zeros(n_steps)
    arms_hist = np.zeros(n_steps, dtype=int)

    # Sample phase snapshots
    snapshots = {}
    snapshot_times = [0.1, 1.0, 5.0, 10.0, 20.0, 50.0, 100.0, T - dt]

    for step in range(n_steps):
        t = step * dt
        r_hist[step] = np.abs(np.mean(np.exp(1j * theta)))
        arms_hist[step] = count_arms(theta)

        for st in snapshot_times:
            if abs(t - st) < dt / 2 and st not in snapshots:
                snapshots[st] = theta.copy()

        theta = rk4(theta, omega, K, dt, antiperiodic)

    # Final measurements
    final_arms = count_arms(theta)
    arm_lengths = measure_arm_lengths(theta)
    t_reflect = detect_reflection_time(r_hist, dt)

    # Phase gradient at steady state
    diffs = np.array([((theta[(i + 1) % N] - theta[i] + np.pi)
                       % (2 * np.pi)) - np.pi for i in range(N)])
    mean_grad = np.mean(np.abs(diffs))

    return {
        "N": N,
        "K": K,
        "K_c": K_c,
        "K_ratio": K_ratio,
        "gamma": gamma,
        "antiperiodic": antiperiodic,
        "r_final": r_hist[-1],
        "r_hist": r_hist,
        "arms_final": final_arms,
        "arm_lengths": arm_lengths,
        "mean_grad": mean_grad,
        "t_reflect": t_reflect,
        "snapshots": snapshots,
        "n_max_predicted": np.pi * K / (4 * gamma),
        "arms_predicted": max(1, round(4 * N * gamma / (np.pi * K))),
    }


def print_result(res):
    bc = "MÖBIUS" if res["antiperiodic"] else "PERIODIC"
    print(f"\n  [{bc}] N={res['N']}, K/K_c={res['K_ratio']:.1f}, "
          f"K={res['K']:.2f}")
    print(f"    r(final)     = {res['r_final']:.4f}")
    print(f"    Arms (final) = {res['arms_final']}")
    print(f"    Arm lengths  = {res['arm_lengths']}")
    print(f"    Mean |∂θ|    = {res['mean_grad']:.4f} "
          f"({res['mean_grad']/(2*np.pi):.4f} × 2π)")
    if res['t_reflect'] is not None:
        print(f"    t_reflect    = {res['t_reflect']:.1f}")
    else:
        print(f"    t_reflect    = not detected (immediate or gradual)")
    print(f"    n_max (pred) = {res['n_max_predicted']:.1f}")
    print(f"    Arms (pred)  = {res['arms_predicted']}")


def print_snapshots(res):
    """Show phase evolution at snapshot times."""
    N = res["N"]
    if N > 21:
        return  # too wide to print
    print(f"    Phase snapshots (N={N}):")
    for t in sorted(res["snapshots"].keys()):
        theta = res["snapshots"][t]
        phases = theta % (2 * np.pi)
        row = f"      t={t:6.1f}: "
        for i in range(N):
            row += f"{phases[i]:5.2f} "
        # Count arms at this snapshot
        arms = count_arms(theta)
        row += f"  [{arms} arm{'s' if arms > 1 else ''}]"
        print(row)


def main():
    print("=" * 75)
    print("  COHERENCE LENGTH ON THE MÖBIUS RING")
    print("  Derivation 18: arm formation and topological snap")
    print("=" * 75)

    # ── Experiment 1: N sweep at fixed K/K_c ─────────────────────────────
    print(f"\n{'─' * 75}")
    print("  EXPERIMENT 1: N sweep at K/K_c = 1.5")
    print(f"{'─' * 75}")

    for N in [3, 5, 8, 13, 21, 34, 55]:
        for ap in [True, False]:
            res = run_sweep(N, K_ratio=1.5, antiperiodic=ap)
            print_result(res)
            if N <= 21:
                print_snapshots(res)

    # ── Experiment 2: K sweep at N = 21 ──────────────────────────────────
    print(f"\n{'─' * 75}")
    print("  EXPERIMENT 2: K/K_c sweep at N = 21")
    print(f"{'─' * 75}")

    for K_ratio in [1.2, 1.5, 2.0, 3.0, 5.0]:
        res = run_sweep(21, K_ratio=K_ratio, antiperiodic=True)
        print_result(res)
        print_snapshots(res)

    # ── Experiment 3: arm count at N = 55 ────────────────────────────────
    print(f"\n{'─' * 75}")
    print("  EXPERIMENT 3: N = 55, K sweep — arm count")
    print(f"{'─' * 75}")

    for K_ratio in [1.2, 1.5, 2.0, 3.0, 5.0, 8.0]:
        res = run_sweep(55, K_ratio=K_ratio, antiperiodic=True)
        print_result(res)

    # ── Summary ──────────────────────────────────────────────────────────
    print(f"\n{'=' * 75}")
    print("  SUMMARY: COHERENCE LENGTH SCALING")
    print(f"{'=' * 75}")

    print(f"\n  {'N':>4s}  {'K/K_c':>6s}  {'r':>6s}  {'arms':>5s}  "
          f"{'lengths':>20s}  {'n_max':>6s}  {'pred':>5s}  {'BC':>8s}")
    print("  " + "-" * 72)

    for N in [3, 5, 8, 13, 21, 34, 55]:
        for K_ratio in [1.5]:
            for ap in [True, False]:
                res = run_sweep(N, K_ratio=K_ratio, antiperiodic=ap)
                bc = "Möbius" if ap else "Periodic"
                lens = str(res["arm_lengths"])
                if len(lens) > 20:
                    lens = lens[:17] + "..."
                print(f"  {N:4d}  {K_ratio:6.1f}  {res['r_final']:6.3f}  "
                      f"{res['arms_final']:5d}  {lens:>20s}  "
                      f"{res['n_max_predicted']:6.1f}  "
                      f"{res['arms_predicted']:5d}  {bc:>8s}")

    print(f"\n  Key prediction: arms form freely up to length n_max = πK/(4γ),")
    print(f"  then quantize when they hit the twist. Arm count = N/n_max")
    print(f"  (rounded, minimum 1). Periodic BC: no snap, arms merge to 0/1.")


if __name__ == "__main__":
    main()
