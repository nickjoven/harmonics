#!/usr/bin/env python3
"""
3×3 Klein bottle device: the four-state topological memory.

Connects the D22 engineering target to today's results:
  - Does the 4-state structure emerge from random ICs?
  - Do the basins have the exp(π/2) asymmetry?
  - Is r ≈ 0.5 robust (partial coherence as ground state)?
  - How much noise before a state flips?
  - What's the basin boundary geometry?

Usage:
    python3 sync_cost/derivations/klein_device_exploration.py
"""

import numpy as np
import math


# ── Neighbor maps ────────────────────────────────────────────────────────────

def neighbors_torus(i, j, Nx, Ny):
    return [
        ((i - 1) % Nx, j, 0),
        ((i + 1) % Nx, j, 0),
        (i, (j - 1) % Ny, 0),
        (i, (j + 1) % Ny, 0),
    ]


def neighbors_klein(i, j, Nx, Ny):
    nbrs = []
    if i > 0:
        nbrs.append((i - 1, j, 0))
    else:
        nbrs.append((Nx - 1, Ny - 1 - j, -np.pi))
    if i < Nx - 1:
        nbrs.append((i + 1, j, 0))
    else:
        nbrs.append((0, Ny - 1 - j, np.pi))
    nbrs.append((i, (j - 1) % Ny, 0))
    nbrs.append((i, (j + 1) % Ny, 0))
    return nbrs


# ── Dynamics ─────────────────────────────────────────────────────────────────

def build_neighbor_arrays(Nx, Ny, neighbor_func):
    """Pre-compute neighbor indices and shifts for vectorized dynamics."""
    nbr_i = np.zeros((Nx, Ny, 4), dtype=int)
    nbr_j = np.zeros((Nx, Ny, 4), dtype=int)
    nbr_s = np.zeros((Nx, Ny, 4))
    for i in range(Nx):
        for j in range(Ny):
            for k, (ni, nj, shift) in enumerate(neighbor_func(i, j, Nx, Ny)):
                nbr_i[i, j, k] = ni
                nbr_j[i, j, k] = nj
                nbr_s[i, j, k] = shift
    return nbr_i, nbr_j, nbr_s


def kuramoto_2d_fast(theta, omega, K, nbr_i, nbr_j, nbr_s):
    dtheta = omega.copy()
    for k in range(4):
        neighbor_theta = theta[nbr_i[:, :, k], nbr_j[:, :, k]] + nbr_s[:, :, k]
        dtheta += (K / 4) * np.sin(neighbor_theta - theta)
    return dtheta


def kuramoto_2d(theta, omega, K, Nx, Ny, neighbor_func):
    dtheta = omega.copy()
    for i in range(Nx):
        for j in range(Ny):
            for ni, nj, shift in neighbor_func(i, j, Nx, Ny):
                dtheta[i, j] += (K / 4) * np.sin(
                    theta[ni, nj] + shift - theta[i, j])
    return dtheta


def rk4_step(theta, omega, K, Nx, Ny, neighbor_func, dt):
    f = lambda th: kuramoto_2d(th, omega, K, Nx, Ny, neighbor_func)
    k1 = f(theta)
    k2 = f(theta + 0.5 * dt * k1)
    k3 = f(theta + 0.5 * dt * k2)
    k4 = f(theta + dt * k3)
    return theta + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)


def rk4_fast(theta, omega, K, nbr_i, nbr_j, nbr_s, dt):
    """Euler step (fast enough for basin survey)."""
    return theta + dt * kuramoto_2d_fast(theta, omega, K, nbr_i, nbr_j, nbr_s)


def order_parameter(theta):
    return abs(np.mean(np.exp(1j * theta)))


def classify_state(theta, Nx, Ny):
    """Classify the phase pattern by discretizing to nearest π/6."""
    pattern = np.round(theta / (np.pi / 6)) * (np.pi / 6)
    # Reduce to a canonical form (shift so [0,0] = 0)
    pattern = (pattern - pattern[0, 0]) % (2 * np.pi)
    # Hash the pattern
    return tuple(np.round(pattern.flatten(), 2))


def phase_gradient_signature(theta, Nx, Ny):
    """Compact signature: mean x-gradient and y-gradient."""
    dx = 0.0
    dy = 0.0
    for i in range(Nx):
        for j in range(Ny):
            i_next = (i + 1) % Nx
            j_next = (j + 1) % Ny
            dx += ((theta[i_next, j] - theta[i, j] + np.pi) % (2 * np.pi) - np.pi)
            dy += ((theta[i, j_next] - theta[i, j] + np.pi) % (2 * np.pi) - np.pi)
    dx /= (Nx * Ny)
    dy /= (Nx * Ny)
    return round(dx, 2), round(dy, 2)


# ── Experiment 1: Basin survey ───────────────────────────────────────────────

def experiment_1_basins(Nx, Ny, K, n_trials=200):
    """Random ICs → how many distinct attractors?"""
    print(f"\n{'=' * 70}")
    print(f"  EXPERIMENT 1: BASIN SURVEY ({Nx}×{Ny}, K={K})")
    print(f"  {n_trials} random initial conditions")
    print(f"{'=' * 70}")

    gamma = 1.0
    dt = 0.02
    T = 100.0
    n_steps = int(T / dt)

    # Pre-compute neighbors
    nbr_ki, nbr_kj, nbr_ks = build_neighbor_arrays(Nx, Ny, neighbors_klein)
    nbr_ti, nbr_tj, nbr_ts = build_neighbor_arrays(Nx, Ny, neighbors_torus)

    states_klein = {}
    states_torus = {}
    r_klein = []
    r_torus = []

    for trial in range(n_trials):
        rng = np.random.default_rng(trial * 31 + 17)
        omega = gamma * np.clip(rng.standard_cauchy((Nx, Ny)), -10, 10)
        theta_k = rng.uniform(0, 2 * np.pi, (Nx, Ny))
        theta_t = theta_k.copy()

        for _ in range(n_steps):
            theta_k = rk4_fast(theta_k, omega, K, nbr_ki, nbr_kj, nbr_ks, dt)
            theta_t = rk4_fast(theta_t, omega, K, nbr_ti, nbr_tj, nbr_ts, dt)

        sig_k = phase_gradient_signature(theta_k, Nx, Ny)
        sig_t = phase_gradient_signature(theta_t, Nx, Ny)

        states_klein[sig_k] = states_klein.get(sig_k, 0) + 1
        states_torus[sig_t] = states_torus.get(sig_t, 0) + 1

        r_klein.append(order_parameter(theta_k))
        r_torus.append(order_parameter(theta_t))

    print(f"\n  Klein bottle: {len(states_klein)} distinct gradient signatures")
    sorted_k = sorted(states_klein.items(), key=lambda x: -x[1])
    for sig, count in sorted_k[:10]:
        frac = count / n_trials
        print(f"    ({sig[0]:+.2f}, {sig[1]:+.2f}): {count:3d} "
              f"({frac:.1%})")

    print(f"\n  Torus: {len(states_torus)} distinct gradient signatures")
    sorted_t = sorted(states_torus.items(), key=lambda x: -x[1])
    for sig, count in sorted_t[:10]:
        frac = count / n_trials
        print(f"    ({sig[0]:+.2f}, {sig[1]:+.2f}): {count:3d} "
              f"({frac:.1%})")

    print(f"\n  Order parameter statistics:")
    print(f"    Klein: <r> = {np.mean(r_klein):.4f} ± {np.std(r_klein):.4f}")
    print(f"    Torus: <r> = {np.mean(r_torus):.4f} ± {np.std(r_torus):.4f}")
    print(f"    Klein r ≈ 0.5 prediction: "
          f"{'PASS' if abs(np.mean(r_klein) - 0.5) < 0.15 else 'FAIL'}")

    return states_klein, states_torus, r_klein, r_torus


# ── Experiment 2: Basin asymmetry ────────────────────────────────────────────

def experiment_2_asymmetry(Nx, Ny, K_vals, n_trials=100):
    """Do basin sizes show the exp(π/2) ratio?"""
    print(f"\n{'=' * 70}")
    print("  EXPERIMENT 2: BASIN ASYMMETRY vs K")
    print("  Do basin occupation ratios match exp(π/2)?")
    print(f"{'=' * 70}")

    gamma = 1.0
    dt = 0.02
    T = 100.0
    n_steps = int(T / dt)

    phi = (1 + np.sqrt(5)) / 2
    exp_pi2 = np.exp(np.pi / 2)

    nbr_i, nbr_j, nbr_s = build_neighbor_arrays(Nx, Ny, neighbors_klein)

    print(f"\n  {'K':>6s}  {'n_states':>8s}  {'<r>':>8s}  "
          f"{'top/2nd':>8s}  {'exp(π/2)':>8s}  {'top_sig':>15s}")
    print("  " + "-" * 60)

    results = []

    for K in K_vals:
        states = {}
        r_vals = []

        for trial in range(n_trials):
            rng = np.random.default_rng(trial * 53 + 3)
            omega = gamma * np.clip(rng.standard_cauchy((Nx, Ny)), -10, 10)
            theta = rng.uniform(0, 2 * np.pi, (Nx, Ny))

            for _ in range(n_steps):
                theta = rk4_fast(theta, omega, K, nbr_i, nbr_j, nbr_s, dt)

            sig = phase_gradient_signature(theta, Nx, Ny)
            states[sig] = states.get(sig, 0) + 1
            r_vals.append(order_parameter(theta))

        sorted_s = sorted(states.items(), key=lambda x: -x[1])
        n_states = len(states)
        r_mean = np.mean(r_vals)
        top = sorted_s[0][1] if len(sorted_s) > 0 else 0
        second = sorted_s[1][1] if len(sorted_s) > 1 else 1
        ratio = top / second if second > 0 else float('inf')
        top_sig = sorted_s[0][0] if sorted_s else (0, 0)

        results.append({
            "K": K, "n_states": n_states, "r_mean": r_mean,
            "ratio": ratio, "states": states,
        })

        print(f"  {K:6.1f}  {n_states:8d}  {r_mean:8.4f}  "
              f"{ratio:8.2f}  {exp_pi2:8.4f}  "
              f"({top_sig[0]:+.2f},{top_sig[1]:+.2f})")

    return results


# ── Experiment 3: Noise-induced flipping ─────────────────────────────────────

def experiment_3_flipping(Nx, Ny, K):
    """Start in a locked state, add noise, measure flip rate."""
    print(f"\n{'=' * 70}")
    print(f"  EXPERIMENT 3: STATE FLIPPING UNDER NOISE (K={K})")
    print(f"{'=' * 70}")

    gamma = 0.5
    dt = 0.02
    T_settle = 100.0
    T_noise = 200.0
    n_settle = int(T_settle / dt)
    n_noise = int(T_noise / dt)

    nbr_i, nbr_j, nbr_s = build_neighbor_arrays(Nx, Ny, neighbors_klein)

    noise_levels = [0.0, 0.1, 0.5, 1.0, 2.0, 5.0]

    print(f"\n  {'σ_noise':>8s}  {'n_flips':>8s}  {'<r>':>8s}  "
          f"{'r_std':>8s}  {'frac_in_start':>14s}")
    print("  " + "-" * 55)

    for sigma in noise_levels:
        rng = np.random.default_rng(42)
        omega = gamma * np.clip(rng.standard_cauchy((Nx, Ny)), -10, 10)
        theta = np.zeros((Nx, Ny))
        theta[0, 0] = 0.1

        for _ in range(n_settle):
            theta = rk4_fast(theta, omega, K, nbr_i, nbr_j, nbr_s, dt)

        start_sig = phase_gradient_signature(theta, Nx, Ny)

        # Apply noise and track
        n_flips = 0
        current_sig = start_sig
        in_start = 0
        r_vals = []

        for step in range(n_noise):
            # Add Gaussian noise
            if sigma > 0:
                theta += sigma * np.sqrt(dt) * rng.standard_normal((Nx, Ny))
            theta = rk4_fast(theta, omega, K, nbr_i, nbr_j, nbr_s, dt)

            if step % 100 == 0:
                sig = phase_gradient_signature(theta, Nx, Ny)
                if sig != current_sig:
                    n_flips += 1
                    current_sig = sig
                if sig == start_sig:
                    in_start += 1
                r_vals.append(order_parameter(theta))

        total_checks = n_noise // 100
        frac_start = in_start / total_checks if total_checks > 0 else 0
        r_mean = np.mean(r_vals) if r_vals else 0
        r_std = np.std(r_vals) if r_vals else 0

        print(f"  {sigma:8.2f}  {n_flips:8d}  {r_mean:8.4f}  "
              f"{r_std:8.4f}  {frac_start:14.3f}")


# ── Experiment 4: Phase pattern catalog ──────────────────────────────────────

def experiment_4_patterns(Nx, Ny, K):
    """Show actual phase patterns for the dominant states."""
    print(f"\n{'=' * 70}")
    print(f"  EXPERIMENT 4: PHASE PATTERN CATALOG (K={K})")
    print(f"{'=' * 70}")

    gamma = 1.0
    dt = 0.02
    T = 100.0
    n_steps = int(T / dt)
    n_trials = 20

    nbr_i, nbr_j, nbr_s = build_neighbor_arrays(Nx, Ny, neighbors_klein)

    patterns = {}

    for trial in range(n_trials):
        rng = np.random.default_rng(trial * 71 + 11)
        omega = gamma * np.clip(rng.standard_cauchy((Nx, Ny)), -10, 10)
        theta = rng.uniform(0, 2 * np.pi, (Nx, Ny))

        for _ in range(n_steps):
            theta = rk4_fast(theta, omega, K, nbr_i, nbr_j, nbr_s, dt)

        sig = phase_gradient_signature(theta, Nx, Ny)
        r = order_parameter(theta)

        if sig not in patterns:
            patterns[sig] = {
                "theta": theta.copy(),
                "r": r,
                "count": 0,
                "sig": sig,
            }
        patterns[sig]["count"] += 1

    sorted_p = sorted(patterns.values(), key=lambda x: -x["count"])

    for idx, pat in enumerate(sorted_p[:6]):
        print(f"\n  State {idx+1}: ({pat['sig'][0]:+.2f}, {pat['sig'][1]:+.2f}) "
              f"— {pat['count']}/{n_trials} trials, r = {pat['r']:.4f}")

        theta = pat["theta"]
        # Show phase lattice (mod 2π, in units of π/6 for readability)
        print(f"    Phase lattice (×π/6):")
        for j in range(Ny - 1, -1, -1):
            row = "      "
            for i in range(Nx):
                val = (theta[i, j] % (2 * np.pi)) / (np.pi / 6)
                row += f"{val:5.1f} "
            print(row)

        # Phase differences in x and y
        print(f"    x-diffs (rad):")
        for j in range(Ny):
            diffs = []
            for i in range(Nx):
                i_next = (i + 1) % Nx
                d = ((theta[i_next, j] - theta[i, j] + np.pi)
                     % (2 * np.pi) - np.pi)
                diffs.append(d)
            row = f"      y={j}: " + " ".join(f"{d:+.3f}" for d in diffs)
            print(row)


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    Nx, Ny = 3, 3

    print("=" * 70)
    print("  3×3 KLEIN BOTTLE DEVICE: FOUR-STATE TOPOLOGICAL MEMORY")
    print("=" * 70)

    # Experiment 1: Basin survey at K=8
    states_k, states_t, r_k, r_t = experiment_1_basins(Nx, Ny, K=8.0,
                                                         n_trials=50)

    # Experiment 2: Basin asymmetry vs K
    K_vals = [4.0, 8.0, 12.0, 20.0]
    asym_results = experiment_2_asymmetry(Nx, Ny, K_vals, n_trials=30)

    # Experiment 3: Noise flipping at K=8
    experiment_3_flipping(Nx, Ny, K=8.0)

    # Experiment 4: Phase patterns at K=8
    experiment_4_patterns(Nx, Ny, K=8.0)

    # ── Plot ─────────────────────────────────────────────────────────────
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("3×3 Klein Bottle Device: Topological States",
                 fontsize=14, fontweight="bold")

    # A: r distribution
    ax = axes[0, 0]
    ax.hist(r_k, bins=20, alpha=0.7, color="red", label="Klein", density=True)
    ax.hist(r_t, bins=20, alpha=0.5, color="blue", label="Torus", density=True)
    ax.axvline(0.5, color="green", ls="--", lw=2, label="r = 0.5")
    ax.axvline(np.mean(r_k), color="red", ls=":", lw=2,
               label=f"Klein <r>={np.mean(r_k):.3f}")
    ax.axvline(np.mean(r_t), color="blue", ls=":", lw=2,
               label=f"Torus <r>={np.mean(r_t):.3f}")
    ax.set_xlabel("|r|")
    ax.set_ylabel("Density")
    ax.set_title("A. Order parameter distribution (K=8)")
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # B: Number of states vs K
    ax = axes[0, 1]
    Ks = [r["K"] for r in asym_results]
    ns = [r["n_states"] for r in asym_results]
    rs = [r["r_mean"] for r in asym_results]
    ax.bar(range(len(Ks)), ns, color="steelblue")
    ax.set_xticks(range(len(Ks)))
    ax.set_xticklabels([f"{k:.0f}" for k in Ks])
    ax.set_xlabel("K")
    ax.set_ylabel("Distinct states")
    ax.set_title("B. State count vs coupling")
    ax2 = ax.twinx()
    ax2.plot(range(len(Ks)), rs, "r-o", ms=6, lw=2, label="<r>")
    ax2.set_ylabel("<r>", color="red")
    ax2.axhline(0.5, color="green", ls="--", alpha=0.5)
    ax.grid(True, alpha=0.3)

    # C: Basin sizes at K=8
    ax = axes[1, 0]
    sorted_k = sorted(states_k.items(), key=lambda x: -x[1])
    labels = [f"({s[0]:+.1f},{s[1]:+.1f})" for s, _ in sorted_k[:8]]
    counts = [c for _, c in sorted_k[:8]]
    ax.barh(range(len(counts)), counts, color="steelblue")
    ax.set_yticks(range(len(counts)))
    ax.set_yticklabels(labels, fontsize=8)
    ax.set_xlabel("Count (out of 200)")
    ax.set_title("C. Basin sizes (Klein, K=8)")
    ax.grid(True, alpha=0.3)
    # Mark exp(π/2) ratio
    if len(counts) > 1:
        ratio = counts[0] / counts[1]
        ax.text(0.7, 0.9, f"top/2nd = {ratio:.2f}\nexp(π/2) = {np.exp(np.pi/2):.2f}",
                transform=ax.transAxes, fontsize=10,
                bbox=dict(boxstyle="round", facecolor="lightyellow"))

    # D: r vs K comparison
    ax = axes[1, 1]
    ax.plot(Ks, rs, "r-o", ms=6, lw=2, label="Klein <r>")
    ax.axhline(0.5, color="green", ls="--", lw=2, label="r = 0.5 (predicted)")
    ax.set_xlabel("K")
    ax.set_ylabel("<r>")
    ax.set_title("D. Partial coherence vs K")
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 1)

    plt.tight_layout()
    out = "sync_cost/derivations/klein_device_exploration.png"
    fig.savefig(out, dpi=150)
    print(f"\nSaved: {out}")

    print(f"\n{'=' * 70}")
    print("  DONE")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()
