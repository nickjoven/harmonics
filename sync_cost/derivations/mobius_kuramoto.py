#!/usr/bin/env python3
"""
Kuramoto oscillators on a Möbius ring (antiperiodic boundary condition).

Derivation 18: Does a single perturbation of rest on a compact
non-orientable surface produce stable rational phase divisions?

Compare with periodic BC (cylinder) to verify odd-mode selection.
"""

import numpy as np
import sys


# --- Dynamics ---

def kuramoto_mobius(theta, omega, K):
    """Kuramoto nearest-neighbor on a ring with antiperiodic BC.

    theta_{N+1} = theta_1 + pi  (the Möbius twist)
    theta_0     = theta_N - pi  (wrap the other direction)
    """
    N = len(theta)
    dtheta = np.copy(omega)
    for i in range(N):
        left = theta[(i - 1) % N] if i > 0 else theta[N - 1] - np.pi
        right = theta[(i + 1) % N] if i < N - 1 else theta[0] + np.pi
        dtheta[i] += (K / 2) * (np.sin(right - theta[i]) + np.sin(left - theta[i]))
    return dtheta


def kuramoto_periodic(theta, omega, K):
    """Standard Kuramoto ring with periodic BC (cylinder)."""
    N = len(theta)
    dtheta = np.copy(omega)
    for i in range(N):
        left = theta[(i - 1) % N]
        right = theta[(i + 1) % N]
        dtheta[i] += (K / 2) * (np.sin(right - theta[i]) + np.sin(left - theta[i]))
    return dtheta


def rk4_step(f, theta, omega, K, dt):
    k1 = f(theta, omega, K)
    k2 = f(theta + 0.5 * dt * k1, omega, K)
    k3 = f(theta + 0.5 * dt * k2, omega, K)
    k4 = f(theta + dt * k3, omega, K)
    return theta + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)


# --- Observables ---

def order_parameter(theta):
    """Kuramoto order parameter r = |mean(exp(i*theta))|."""
    return abs(np.mean(np.exp(1j * theta)))


def phase_differences(theta):
    """Adjacent phase differences mod 2pi, mapped to [-pi, pi]."""
    N = len(theta)
    diffs = []
    for i in range(N):
        if i < N - 1:
            d = theta[i + 1] - theta[i]
        else:
            d = (theta[0] + np.pi) - theta[i]  # Möbius wrap
        diffs.append(((d + np.pi) % (2 * np.pi)) - np.pi)
    return np.array(diffs)


def detect_rational(diff, tol=0.05):
    """Check if a phase difference is near 2*pi*p/q for small p/q."""
    candidates = [(0, 1), (1, 2), (1, 3), (2, 3), (1, 4), (3, 4),
                  (1, 5), (2, 5), (3, 5), (4, 5), (1, 6), (5, 6)]
    d = (diff % (2 * np.pi)) / (2 * np.pi)
    for p, q in candidates:
        if abs(d - p / q) < tol or abs(d - (1 - p / q)) < tol:
            return f"{p}/{q}"
    return None


# --- Simulation ---

def run_simulation(N, K_ratio, epsilon, bc="mobius", gamma=1.0,
                   omega0=0.0, dt=0.01, T=100.0, seed=42):
    """Run one simulation.

    Args:
        N: number of oscillators
        K_ratio: K / K_c where K_c = 4*gamma for Möbius (N=3)
        epsilon: initial perturbation of oscillator 0
        bc: "mobius" or "periodic"
        gamma: Lorentzian half-width
        omega0: center frequency
        dt: timestep
        T: total time
        seed: random seed for frequencies

    Returns: dict with trajectory and diagnostics
    """
    rng = np.random.default_rng(seed)

    # Lorentzian frequencies via Cauchy
    omega = omega0 + gamma * rng.standard_cauchy(N)
    # Clip extremes for numerical stability
    omega = np.clip(omega, omega0 - 10 * gamma, omega0 + 10 * gamma)

    # Critical coupling
    if bc == "mobius":
        K_c = 2 * gamma / np.sin(np.pi / (2 * N))
    else:
        K_c = 2 * gamma / np.sin(np.pi / N)
    K = K_ratio * K_c

    # Initial condition: rest + perturbation
    theta = np.zeros(N)
    theta[0] = epsilon

    dynamics = kuramoto_mobius if bc == "mobius" else kuramoto_periodic

    n_steps = int(T / dt)
    r_history = np.zeros(n_steps)
    theta_history = np.zeros((n_steps, N))

    for step in range(n_steps):
        r_history[step] = order_parameter(theta)
        theta_history[step] = theta.copy()
        theta = rk4_step(dynamics, theta, omega, K, dt)

    # Final phase differences
    final_diffs = phase_differences(theta)

    # Detect locking
    locked_rationals = [detect_rational(d) for d in final_diffs]

    return {
        "N": N,
        "K": K,
        "K_c": K_c,
        "K_ratio": K_ratio,
        "bc": bc,
        "gamma": gamma,
        "epsilon": epsilon,
        "omega": omega,
        "r_final": r_history[-1],
        "r_history": r_history,
        "theta_history": theta_history,
        "final_diffs": final_diffs,
        "locked_rationals": locked_rationals,
    }


def print_result(res):
    tag = "MÖBIUS" if res["bc"] == "mobius" else "CYLINDER"
    print(f"\n{'='*60}")
    print(f"[{tag}] N={res['N']}, K/K_c={res['K_ratio']:.2f}, "
          f"ε={res['epsilon']:.3f}")
    print(f"  K_c = {res['K_c']:.4f}, K = {res['K']:.4f}")
    print(f"  r(final) = {res['r_final']:.4f}")
    print(f"  Phase differences (mod 2π):")
    for i, d in enumerate(res["final_diffs"]):
        rat = res["locked_rationals"][i]
        lock_str = f"  ← locked to {rat}" if rat else ""
        print(f"    Δθ_{i},{(i+1) % res['N']} = {d:.4f} "
              f"({d/(2*np.pi):.4f} × 2π){lock_str}")


def main():
    print("Derivation 18: Kuramoto on Möbius ring")
    print("=" * 60)

    # --- Experiment 1: N=3, scan K/K_c ---
    print("\n### Experiment 1: N=3, coupling scan")
    for K_ratio in [0.5, 1.0, 1.2, 1.5, 2.0]:
        for bc in ["mobius", "periodic"]:
            res = run_simulation(N=3, K_ratio=K_ratio, epsilon=0.1, bc=bc)
            print_result(res)

    # --- Experiment 2: N scan at K/K_c = 1.5 ---
    print("\n\n### Experiment 2: N scan at K/K_c = 1.5")
    for N in [3, 5, 8, 13]:
        for bc in ["mobius", "periodic"]:
            res = run_simulation(N=N, K_ratio=1.5, epsilon=0.1, bc=bc)
            print_result(res)

    # --- Experiment 3: Perturbation scan ---
    print("\n\n### Experiment 3: ε scan, N=3, K/K_c=1.5")
    for eps in [0.001, 0.01, 0.1, 1.0, np.pi]:
        res = run_simulation(N=3, K_ratio=1.5, epsilon=eps, bc="mobius")
        print_result(res)

    print("\n" + "=" * 60)
    print("Done. Compare Möbius vs Cylinder for odd-mode selection.")


if __name__ == "__main__":
    main()
