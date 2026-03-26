#!/usr/bin/env python3
"""
Exploration: what can the N=3 Möbius resonator actually do?

Beyond the basic 1/3 frequency division (D18), this explores:
  1. Multi-frequency locking landscape (which p/q are accessible?)
  2. Noise resilience (how much disorder before it breaks?)
  3. Driven response (what happens with external drive at various ω_d?)
  4. Spectral weight distribution (does exp(π/2) or φ appear?)
  5. Basin structure (how do the four Klein bottle states appear in N=3?)
  6. Transient dynamics (is the settling time related to ln(φ²)?)

Usage:
    python3 sync_cost/derivations/mobius_exploration.py
"""

import numpy as np
import math


# ── Dynamics ─────────────────────────────────────────────────────────────────

def kuramoto_mobius(theta, omega, K, F_drive=None):
    N = len(theta)
    dtheta = np.copy(omega)
    for i in range(N):
        left = theta[(i - 1) % N] if i > 0 else theta[N - 1] - np.pi
        right = theta[(i + 1) % N] if i < N - 1 else theta[0] + np.pi
        dtheta[i] += (K / 2) * (np.sin(right - theta[i]) +
                                 np.sin(left - theta[i]))
    if F_drive is not None:
        dtheta += F_drive
    return dtheta


def kuramoto_periodic(theta, omega, K, F_drive=None):
    N = len(theta)
    dtheta = np.copy(omega)
    for i in range(N):
        left = theta[(i - 1) % N]
        right = theta[(i + 1) % N]
        dtheta[i] += (K / 2) * (np.sin(right - theta[i]) +
                                 np.sin(left - theta[i]))
    if F_drive is not None:
        dtheta += F_drive
    return dtheta


def rk4_step(f, theta, omega, K, dt, F_drive=None):
    k1 = f(theta, omega, K, F_drive)
    k2 = f(theta + 0.5 * dt * k1, omega, K, F_drive)
    k3 = f(theta + 0.5 * dt * k2, omega, K, F_drive)
    k4 = f(theta + dt * k3, omega, K, F_drive)
    return theta + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)


def order_parameter(theta):
    return abs(np.mean(np.exp(1j * theta)))


def phase_diffs_mobius(theta):
    N = len(theta)
    diffs = []
    for i in range(N):
        if i < N - 1:
            d = theta[i + 1] - theta[i]
        else:
            d = (theta[0] + np.pi) - theta[i]
        diffs.append(((d + np.pi) % (2 * np.pi)) - np.pi)
    return np.array(diffs)


# ── Experiment 1: Locking landscape ──────────────────────────────────────────

def experiment_1_locking_landscape():
    """Sweep K and initial conditions to find all accessible locked states."""
    print(f"\n{'=' * 70}")
    print("  EXPERIMENT 1: LOCKING LANDSCAPE")
    print("  What rational phase divisions are accessible?")
    print(f"{'=' * 70}")

    N = 3
    gamma = 1.0
    dt = 0.01
    T = 300.0
    n_steps = int(T / dt)

    K_c_mob = 2 * gamma / np.sin(np.pi / (2 * N))  # = 4.0

    # Scan K and random initial conditions
    K_ratios = [0.8, 1.0, 1.2, 1.5, 2.0, 3.0, 5.0]
    n_trials = 20

    locked_states = {}

    for K_ratio in K_ratios:
        K = K_ratio * K_c_mob
        states_at_K = []

        for trial in range(n_trials):
            rng = np.random.default_rng(trial * 137 + 42)
            omega = gamma * np.clip(rng.standard_cauchy(N), -10, 10)
            theta = rng.uniform(0, 2 * np.pi, N)

            for step in range(n_steps):
                theta = rk4_step(kuramoto_mobius, theta, omega, K, dt)

            diffs = phase_diffs_mobius(theta)
            # Characterize by the phase pattern
            d_frac = tuple(round(d / (2 * np.pi) * 12) / 12 for d in diffs)
            states_at_K.append(d_frac)

        unique = set(states_at_K)
        locked_states[K_ratio] = unique

        print(f"\n  K/K_c = {K_ratio:.1f}: {len(unique)} distinct states")
        for state in sorted(unique):
            count = states_at_K.count(state)
            # Try to identify the rational
            labels = []
            for d in state:
                for p, q in [(0, 1), (1, 6), (1, 4), (1, 3), (5, 12),
                              (1, 2), (7, 12), (2, 3), (3, 4), (5, 6), (1, 1)]:
                    if abs(d - p / q) < 0.05 or abs(d + p / q) < 0.05:
                        labels.append(f"{p}/{q}")
                        break
                else:
                    labels.append(f"{d:.3f}")
            print(f"    {count:2d}× ({', '.join(labels)})")

    return locked_states


# ── Experiment 2: Noise resilience ───────────────────────────────────────────

def experiment_2_noise():
    """How much frequency disorder before locking breaks?"""
    print(f"\n{'=' * 70}")
    print("  EXPERIMENT 2: NOISE RESILIENCE")
    print("  Max disorder γ before 1/3 lock breaks")
    print(f"{'=' * 70}")

    N = 3
    dt = 0.01
    T = 500.0
    n_steps = int(T / dt)
    K = 8.0  # 2× K_c for γ=1

    gamma_vals = np.concatenate([
        np.linspace(0.1, 2.0, 20),
        np.linspace(2.0, 5.0, 10),
        np.linspace(5.0, 15.0, 10),
    ])

    n_trials = 10

    print(f"\n  {'γ':>6s}  {'lock_frac':>10s}  {'<r>':>8s}  {'σ_r':>8s}")
    print("  " + "-" * 40)

    results = []

    for gamma in gamma_vals:
        locked = 0
        r_vals = []

        for trial in range(n_trials):
            rng = np.random.default_rng(trial * 97 + 7)
            omega = gamma * np.clip(rng.standard_cauchy(N), -10, 10)
            theta = rng.uniform(0, 0.1, N)

            for step in range(n_steps):
                theta = rk4_step(kuramoto_mobius, theta, omega, K, dt)

            r = order_parameter(theta)
            r_vals.append(r)

            diffs = phase_diffs_mobius(theta)
            # Check if near 1/3
            d_frac = [abs(d) / (2 * np.pi) for d in diffs]
            if any(abs(df - 1 / 3) < 0.08 for df in d_frac):
                locked += 1

        lock_frac = locked / n_trials
        r_mean = np.mean(r_vals)
        r_std = np.std(r_vals)
        results.append((gamma, lock_frac, r_mean, r_std))

        if abs(gamma - round(gamma)) < 0.1 or lock_frac < 0.5:
            print(f"  {gamma:6.2f}  {lock_frac:10.2f}  {r_mean:8.4f}  {r_std:8.4f}")

    # Find critical gamma
    for i, (g, lf, _, _) in enumerate(results):
        if lf < 0.5:
            print(f"\n  Lock breaks at γ ≈ {g:.2f} (K = {K:.1f})")
            print(f"  γ_crit/γ_0 ≈ {g:.2f} (where γ_0 = 1)")
            print(f"  K/γ_crit = {K/g:.2f}")
            break

    return results


# ── Experiment 3: Driven response ────────────────────────────────────────────

def experiment_3_driven():
    """Drive oscillator 0 at various frequencies, measure response."""
    print(f"\n{'=' * 70}")
    print("  EXPERIMENT 3: DRIVEN RESPONSE")
    print("  Drive osc 0 at ω_d, measure spectrum of all oscillators")
    print(f"{'=' * 70}")

    N = 3
    gamma = 1.0
    K = 8.0
    dt = 0.01
    T_trans = 200.0
    T_meas = 400.0
    n_trans = int(T_trans / dt)
    n_meas = int(T_meas / dt)

    omega_d_ratios = [1 / 3, 1 / 2, 2 / 3, 1.0, 3 / 2, 2.0, 3.0]

    rng = np.random.default_rng(42)
    omega = gamma * np.clip(rng.standard_cauchy(N), -10, 10)
    omega_0 = np.mean(omega)

    print(f"\n  Natural frequencies: {omega}")
    print(f"  Mean ω₀ = {omega_0:.4f}")
    print(f"  K = {K:.1f}, γ = {gamma}")

    print(f"\n  {'ω_d/ω₀':>8s}  {'ω_d':>8s}  {'r_avg':>8s}  "
          f"{'dom_freq₀':>10s}  {'dom_freq₁':>10s}  {'dom_freq₂':>10s}")
    print("  " + "-" * 60)

    A_drive = 2.0  # drive amplitude

    for ratio in omega_d_ratios:
        omega_d = ratio * abs(omega_0) if abs(omega_0) > 0.1 else ratio
        theta = rng.uniform(0, 0.1, N)

        # Transient
        for step in range(n_trans):
            F = np.zeros(N)
            t = step * dt
            F[0] = A_drive * np.sin(omega_d * t)
            theta = rk4_step(kuramoto_mobius, theta, omega, K, dt, F)

        # Measurement: record velocities
        velocities = np.zeros((n_meas, N))
        r_vals = []
        for step in range(n_meas):
            t = (n_trans + step) * dt
            F = np.zeros(N)
            F[0] = A_drive * np.sin(omega_d * t)
            dtheta = kuramoto_mobius(theta, omega, K, F)
            velocities[step] = dtheta
            r_vals.append(order_parameter(theta))
            theta = rk4_step(kuramoto_mobius, theta, omega, K, dt, F)

        r_avg = np.mean(r_vals)

        # FFT of each oscillator's velocity
        dom_freqs = []
        for j in range(N):
            fft = np.fft.rfft(velocities[:, j])
            power = np.abs(fft) ** 2
            freqs = np.fft.rfftfreq(n_meas, dt)
            # Find dominant frequency (skip DC)
            idx = np.argmax(power[1:]) + 1
            dom_freqs.append(freqs[idx])

        print(f"  {ratio:8.4f}  {omega_d:8.4f}  {r_avg:8.4f}  "
              f"{dom_freqs[0]:10.4f}  {dom_freqs[1]:10.4f}  "
              f"{dom_freqs[2]:10.4f}")


# ── Experiment 4: Settling time and golden ratio ─────────────────────────────

def experiment_4_settling():
    """Measure settling time vs K. Look for ln(φ²) in the dynamics."""
    print(f"\n{'=' * 70}")
    print("  EXPERIMENT 4: SETTLING DYNAMICS")
    print("  Does the settling time relate to ln(φ²)?")
    print(f"{'=' * 70}")

    N = 3
    gamma = 1.0
    dt = 0.01
    K_c = 2 * gamma / np.sin(np.pi / (2 * N))

    K_ratios = np.linspace(1.01, 5.0, 30)

    phi = (1 + np.sqrt(5)) / 2
    ln_phi_sq = np.log(phi ** 2)

    print(f"\n  K_c = {K_c:.4f}")
    print(f"  ln(φ²) = {ln_phi_sq:.6f}")

    print(f"\n  {'K/K_c':>8s}  {'τ_settle':>10s}  {'τ/ln(φ²)':>10s}  "
          f"{'(K-Kc)/Kc':>10s}  {'τ×(K-Kc)':>10s}")
    print("  " + "-" * 55)

    tau_vals = []
    delta_K_vals = []

    for K_ratio in K_ratios:
        K = K_ratio * K_c
        rng = np.random.default_rng(42)
        omega = gamma * np.clip(rng.standard_cauchy(N), -10, 10)
        theta = np.zeros(N)
        theta[0] = 0.1

        # Run until r stabilizes
        r_prev = 0
        settle_step = 0
        max_steps = 100000
        r_history = []

        for step in range(max_steps):
            r = order_parameter(theta)
            r_history.append(r)
            theta = rk4_step(kuramoto_mobius, theta, omega, K, dt)

            if step > 1000 and abs(r - r_prev) < 1e-5:
                settle_step = step
                break
            r_prev = r

        tau = settle_step * dt
        delta_K = (K - K_c) / K_c
        tau_vals.append(tau)
        delta_K_vals.append(delta_K)

        product = tau * delta_K if delta_K > 0 else float('nan')
        ratio_ln = tau / ln_phi_sq if tau > 0 else float('nan')

        if len(tau_vals) % 3 == 0:
            print(f"  {K_ratio:8.3f}  {tau:10.2f}  {ratio_ln:10.4f}  "
                  f"{delta_K:10.4f}  {product:10.4f}")

    # Check if τ × (K - K_c)/K_c = const
    products = [t * d for t, d in zip(tau_vals, delta_K_vals) if d > 0.01]
    if products:
        mean_prod = np.mean(products)
        std_prod = np.std(products)
        print(f"\n  <τ × ΔK/K_c> = {mean_prod:.4f} ± {std_prod:.4f}")
        print(f"  Ratio to ln(φ²) = {mean_prod / ln_phi_sq:.4f}")
        print(f"  Ratio to π/2   = {mean_prod / (np.pi/2):.4f}")
        print(f"  Ratio to 1     = {mean_prod:.4f}")

    return tau_vals, delta_K_vals


# ── Experiment 5: Spectral weight at overtones ───────────────────────────────

def experiment_5_spectral_weights():
    """Measure spectral weights at rational overtones of the 1/3 mode."""
    print(f"\n{'=' * 70}")
    print("  EXPERIMENT 5: SPECTRAL WEIGHTS AT OVERTONES")
    print("  Does exp(π/2) or φ appear in the weight ratios?")
    print(f"{'=' * 70}")

    N = 3
    gamma = 1.0
    K = 8.0
    dt = 0.005
    T = 1000.0
    n_steps = int(T / dt)

    rng = np.random.default_rng(42)
    omega = gamma * np.clip(rng.standard_cauchy(N), -10, 10)
    theta = np.zeros(N)
    theta[0] = 0.1

    # Transient
    for _ in range(int(200 / dt)):
        theta = rk4_step(kuramoto_mobius, theta, omega, K, dt)

    # Record velocity of oscillator 1 (middle of the chain)
    vel = np.zeros(n_steps)
    for step in range(n_steps):
        dtheta = kuramoto_mobius(theta, omega, K)
        vel[step] = dtheta[1]
        theta = rk4_step(kuramoto_mobius, theta, omega, K, dt)

    # FFT
    fft = np.fft.rfft(vel)
    power = np.abs(fft) ** 2
    freqs = np.fft.rfftfreq(n_steps, dt)

    # Find dominant frequency
    idx_peak = np.argmax(power[1:]) + 1
    f_dom = freqs[idx_peak]
    p_dom = power[idx_peak]

    print(f"\n  Dominant frequency: {f_dom:.4f}")
    print(f"  Dominant power: {p_dom:.2e}")

    # Check power at rational multiples
    print(f"\n  {'p/q':>6s}  {'freq':>8s}  {'power':>12s}  {'ratio':>10s}  {'note':>15s}")
    print("  " + "-" * 60)

    phi = (1 + np.sqrt(5)) / 2
    exp_pi2 = np.exp(np.pi / 2)

    for p, q in [(1, 3), (1, 2), (2, 3), (1, 1), (4, 3), (3, 2),
                  (2, 1), (5, 3), (3, 1)]:
        target_f = f_dom * p / q
        # Find nearest FFT bin
        idx = np.argmin(np.abs(freqs - target_f))
        if idx > 0:
            pw = power[idx]
            ratio = pw / p_dom if p_dom > 0 else 0
            # Check if ratio is near a recognizable constant
            note = ""
            if abs(ratio - 1 / exp_pi2) < 0.05:
                note = "≈ exp(-π/2)"
            elif abs(ratio - 1 / phi) < 0.05:
                note = "≈ 1/φ"
            elif abs(ratio - 1 / phi ** 2) < 0.05:
                note = "≈ 1/φ²"
            elif abs(ratio - exp_pi2) < 0.3:
                note = "≈ exp(π/2)"
            print(f"  {p}/{q:1d}    {freqs[idx]:8.4f}  {pw:12.2e}  "
                  f"{ratio:10.6f}  {note:>15s}")


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    print("=" * 70)
    print("  MÖBIUS RESONATOR: EXPLORATION OF WHAT'S POSSIBLE")
    print("=" * 70)

    states = experiment_1_locking_landscape()
    noise_results = experiment_2_noise()
    experiment_3_driven()
    tau_vals, delta_K_vals = experiment_4_settling()
    experiment_5_spectral_weights()

    # ── Plot ─────────────────────────────────────────────────────────────
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Möbius Resonator (N=3): Exploration",
                 fontsize=14, fontweight="bold")

    # A: Noise resilience
    ax = axes[0, 0]
    gammas = [r[0] for r in noise_results]
    lock_fracs = [r[1] for r in noise_results]
    r_means = [r[2] for r in noise_results]
    ax.plot(gammas, lock_fracs, "r-o", ms=3, lw=2, label="Lock fraction")
    ax.plot(gammas, r_means, "b-s", ms=3, lw=1.5, label="<r>")
    ax.set_xlabel("γ (frequency disorder)")
    ax.set_ylabel("Fraction / Order parameter")
    ax.set_title("A. Noise resilience (K=8)")
    ax.legend()
    ax.grid(True, alpha=0.3)

    # B: Settling time vs K
    ax = axes[0, 1]
    K_c = 2 * 1.0 / np.sin(np.pi / 6)
    K_plot = [K_c * (1 + dk) for dk in delta_K_vals]
    ax.plot(delta_K_vals, tau_vals, "b-o", ms=4, lw=2)
    ax.set_xlabel("(K - K_c) / K_c")
    ax.set_ylabel("Settling time τ")
    ax.set_title("B. Critical slowing")
    ax.grid(True, alpha=0.3)
    # Fit τ = A / (K - K_c)
    valid = [(dk, t) for dk, t in zip(delta_K_vals, tau_vals)
             if dk > 0.05 and t > 0]
    if valid:
        dks, taus = zip(*valid)
        # log-log fit
        log_dk = np.log(dks)
        log_tau = np.log(taus)
        coeffs = np.polyfit(log_dk, log_tau, 1)
        ax.set_xscale("log")
        ax.set_yscale("log")
        exponent = coeffs[0]
        ax.set_title(f"B. Critical slowing (exponent = {exponent:.2f})")

    # C: Number of distinct states vs K
    ax = axes[1, 0]
    K_ratios = sorted(states.keys())
    n_states = [len(states[kr]) for kr in K_ratios]
    ax.bar(range(len(K_ratios)), n_states, color="steelblue")
    ax.set_xticks(range(len(K_ratios)))
    ax.set_xticklabels([f"{kr:.1f}" for kr in K_ratios])
    ax.set_xlabel("K / K_c")
    ax.set_ylabel("Number of distinct locked states")
    ax.set_title("C. Locking landscape")
    ax.grid(True, alpha=0.3)

    # D: τ × ΔK product
    ax = axes[1, 1]
    products = [t * dk for t, dk in zip(tau_vals, delta_K_vals)
                if dk > 0.01 and t > 0]
    if products:
        ax.hist(products, bins=15, color="steelblue", alpha=0.7)
        ax.axvline(np.mean(products), color="red", ls="--", lw=2,
                   label=f"mean = {np.mean(products):.3f}")
        phi = (1 + np.sqrt(5)) / 2
        ax.axvline(np.log(phi ** 2), color="green", ls="-.", lw=2,
                   label=f"ln(φ²) = {np.log(phi**2):.3f}")
        ax.axvline(np.pi / 2, color="magenta", ls=":", lw=2,
                   label=f"π/2 = {np.pi/2:.3f}")
    ax.set_xlabel("τ × (K-K_c)/K_c")
    ax.set_ylabel("Count")
    ax.set_title("D. Scaling product")
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    out = "sync_cost/derivations/mobius_exploration.png"
    fig.savefig(out, dpi=150)
    print(f"\nSaved: {out}")

    print(f"\n{'=' * 70}")
    print("  DONE")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()
