#!/usr/bin/env python3
"""
Kuramoto lattice K-sweep on Klein bottle vs torus.

Sweeps K from 2 to 20 on a 5×5 lattice, measuring:
  - Order parameter |r|
  - Phase gradient ratio (∂x/∂y → winding number ratio)
  - Dominant rational mode
  - Velocity histogram (dwell time on plateaus)
  - (2,3) vs (3,2) asymmetry from actual dynamics

This is the DYNAMIC counterpart to klein_phase_diagram.py (field equation).

Usage:
    python3 sync_cost/derivations/klein_kuramoto_sweep.py
"""

import numpy as np


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


# ── Observables ──────────────────────────────────────────────────────────────

def order_parameter(theta):
    z = np.exp(1j * theta)
    return np.abs(z.mean())


def phase_gradients(theta, Nx, Ny):
    dx = np.zeros((Nx, Ny))
    dy = np.zeros((Nx, Ny))
    for i in range(Nx):
        for j in range(Ny):
            i_next = (i + 1) % Nx
            dx[i, j] = theta[i_next, j] - theta[i, j]
            j_next = (j + 1) % Ny
            dy[i, j] = theta[i, j_next] - theta[i, j]
    dx = (dx + np.pi) % (2 * np.pi) - np.pi
    dy = (dy + np.pi) % (2 * np.pi) - np.pi
    return dx, dy


def detect_rational(val, tol=0.08):
    x = abs(val) / (2 * np.pi)
    if x > 0.5:
        x = 1 - x
    for p, q in [(0, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
                  (2, 5), (2, 3), (3, 4), (3, 5), (3, 8), (5, 8)]:
        if q > 0 and abs(x - p / q) < tol:
            return (p, q)
    return None


def velocity_histogram(theta_history, dt, n_bins=50):
    """Compute angular velocity histogram from late-time trajectory."""
    # Use last 40% of trajectory
    n = len(theta_history)
    start = int(0.6 * n)
    velocities = []
    for t in range(start, n - 1):
        dth = theta_history[t + 1] - theta_history[t]
        dth = (dth + np.pi) % (2 * np.pi) - np.pi
        velocities.append(dth / dt)
    return np.array(velocities)


# ── Run simulation ───────────────────────────────────────────────────────────

def run_sweep_point(Nx, Ny, K, neighbor_func, gamma=1.0, dt=0.01,
                    T_transient=100.0, T_measure=200.0, seed=42):
    """Run simulation, return observables dict."""
    rng = np.random.default_rng(seed)
    omega = gamma * np.clip(rng.standard_cauchy((Nx, Ny)), -10, 10)
    theta = rng.uniform(0, 0.1, (Nx, Ny))

    n_transient = int(T_transient / dt)
    n_measure = int(T_measure / dt)

    # Transient
    for _ in range(n_transient):
        theta = rk4_step(theta, omega, K, Nx, Ny, neighbor_func, dt)

    # Measurement
    r_vals = []
    grad_x_vals = []
    grad_y_vals = []
    # Track center oscillator trajectory for velocity histogram
    center_i, center_j = Nx // 2, Ny // 2
    center_theta = []

    for step in range(n_measure):
        r_vals.append(order_parameter(theta))
        dx, dy = phase_gradients(theta, Nx, Ny)
        grad_x_vals.append(dx.mean())
        grad_y_vals.append(dy.mean())
        center_theta.append(theta[center_i, center_j])
        theta = rk4_step(theta, omega, K, Nx, Ny, neighbor_func, dt)

    r_arr = np.array(r_vals)
    gx_arr = np.array(grad_x_vals)
    gy_arr = np.array(grad_y_vals)

    # Time-averaged observables
    r_mean = r_arr.mean()
    r_std = r_arr.std()
    gx_mean = gx_arr.mean()
    gy_mean = gy_arr.mean()

    # Gradient ratio
    if abs(gy_mean) > 0.01:
        grad_ratio = gx_mean / gy_mean
    else:
        grad_ratio = np.nan

    # Dominant rational from gradient
    rat_x = detect_rational(gx_mean)
    rat_y = detect_rational(gy_mean)

    # Velocity statistics
    vel = velocity_histogram(np.array(center_theta), dt)
    vel_std = vel.std() if len(vel) > 0 else 0
    # Fraction of time near zero velocity (unlocked)
    zero_frac = np.mean(np.abs(vel) < 0.5) if len(vel) > 0 else 0

    # Plateau detection: fraction of time velocity is within 10% of
    # a rational multiple of 2π
    plateau_frac = 0.0
    if len(vel) > 0:
        for p, q in [(1, 3), (1, 2), (2, 3), (1, 1), (3, 2), (2, 1)]:
            target = 2 * np.pi * p / q
            frac = np.mean(np.abs(vel - target) < 0.3 * target) if target > 0 else 0
            plateau_frac += frac

    # Winding number from total phase advance
    total_phase = center_theta[-1] - center_theta[0]
    winding = total_phase / (2 * np.pi * T_measure)

    return {
        "r_mean": r_mean,
        "r_std": r_std,
        "gx": gx_mean,
        "gy": gy_mean,
        "grad_ratio": grad_ratio,
        "rat_x": rat_x,
        "rat_y": rat_y,
        "vel_std": vel_std,
        "zero_frac": zero_frac,
        "plateau_frac": plateau_frac,
        "winding": winding,
    }


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    Nx, Ny = 5, 5
    K_vals = np.concatenate([
        np.linspace(2.0, 6.0, 12),
        np.linspace(6.0, 12.0, 8),
        np.linspace(12.0, 20.0, 5),
    ])

    print("=" * 70)
    print("  KURAMOTO LATTICE K-SWEEP: KLEIN BOTTLE vs TORUS")
    print(f"  Lattice: {Nx}×{Ny}, {len(K_vals)} K values")
    print("=" * 70)

    results = {"torus": [], "klein": []}

    for idx, K in enumerate(K_vals):
        print(f"  K = {K:.1f} ({idx+1}/{len(K_vals)})", end="", flush=True)

        res_t = run_sweep_point(Nx, Ny, K, neighbors_torus, seed=42)
        res_k = run_sweep_point(Nx, Ny, K, neighbors_klein, seed=42)
        results["torus"].append(res_t)
        results["klein"].append(res_k)

        print(f"  T: r={res_t['r_mean']:.3f} gx/gy={res_t['grad_ratio']:.3f}"
              f"  K: r={res_k['r_mean']:.3f} gx/gy={res_k['grad_ratio']:.3f}")

    # ── Summary table ────────────────────────────────────────────────────
    print(f"\n{'=' * 70}")
    print("  SUMMARY TABLE")
    print("=" * 70)
    print(f"  {'K':>5s}  {'':>3s}  {'<r>':>6s}  {'σ_r':>6s}  "
          f"{'<∂x>':>7s}  {'<∂y>':>7s}  {'∂x/∂y':>7s}  "
          f"{'rat_x':>6s}  {'rat_y':>6s}  {'v_std':>6s}  {'f₀':>5s}")
    print("  " + "-" * 80)

    for idx, K in enumerate(K_vals):
        for label, key in [("T", "torus"), ("K", "klein")]:
            r = results[key][idx]
            rx = f"{r['rat_x'][0]}/{r['rat_x'][1]}" if r['rat_x'] else "·"
            ry = f"{r['rat_y'][0]}/{r['rat_y'][1]}" if r['rat_y'] else "·"
            print(f"  {K:5.1f}  {label:>3s}  {r['r_mean']:6.3f}  "
                  f"{r['r_std']:6.3f}  {r['gx']:7.4f}  {r['gy']:7.4f}  "
                  f"{r['grad_ratio']:7.3f}  {rx:>6s}  {ry:>6s}  "
                  f"{r['vel_std']:6.2f}  {r['zero_frac']:5.3f}")

    # ── Plot ─────────────────────────────────────────────────────────────
    fig, axes = plt.subplots(3, 2, figsize=(14, 14))
    fig.suptitle(f"Kuramoto Lattice K-Sweep: Klein vs Torus ({Nx}×{Ny})",
                 fontsize=14, fontweight="bold", y=0.98)

    K = K_vals

    # A: Order parameter
    ax = axes[0, 0]
    r_t = [r["r_mean"] for r in results["torus"]]
    r_k = [r["r_mean"] for r in results["klein"]]
    r_t_std = [r["r_std"] for r in results["torus"]]
    r_k_std = [r["r_std"] for r in results["klein"]]
    ax.errorbar(K, r_t, yerr=r_t_std, fmt="b-o", ms=4, lw=1.5,
                label="Torus", capsize=3)
    ax.errorbar(K, r_k, yerr=r_k_std, fmt="r-s", ms=4, lw=1.5,
                label="Klein", capsize=3)
    ax.set_ylabel("<|r|>")
    ax.set_title("A. Time-averaged order parameter")
    ax.legend()
    ax.grid(True, alpha=0.3)

    # B: Gradient ratio ∂x/∂y
    ax = axes[0, 1]
    gr_t = [r["grad_ratio"] for r in results["torus"]]
    gr_k = [r["grad_ratio"] for r in results["klein"]]
    ax.plot(K, gr_t, "b-o", ms=4, lw=1.5, label="Torus")
    ax.plot(K, gr_k, "r-s", ms=4, lw=1.5, label="Klein")
    # Mark key rationals
    for p, q, c in [(1, 3, "green"), (1, 2, "orange"), (2, 3, "purple"),
                     (1, 1, "gray")]:
        ax.axhline(p / q, color=c, ls=":", alpha=0.5, label=f"{p}/{q}")
        ax.axhline(-p / q, color=c, ls=":", alpha=0.3)
    ax.set_ylabel("<∂x>/<∂y>")
    ax.set_title("B. Gradient ratio (winding asymmetry)")
    ax.legend(fontsize=7, ncol=2)
    ax.grid(True, alpha=0.3)

    # C: Velocity spread
    ax = axes[1, 0]
    vs_t = [r["vel_std"] for r in results["torus"]]
    vs_k = [r["vel_std"] for r in results["klein"]]
    ax.plot(K, vs_t, "b-o", ms=4, lw=1.5, label="Torus")
    ax.plot(K, vs_k, "r-s", ms=4, lw=1.5, label="Klein")
    ax.set_ylabel("σ(dθ/dt)")
    ax.set_title("C. Velocity spread (dynamics breadth)")
    ax.legend()
    ax.grid(True, alpha=0.3)

    # D: Zero-velocity fraction (unlocked time)
    ax = axes[1, 1]
    zf_t = [r["zero_frac"] for r in results["torus"]]
    zf_k = [r["zero_frac"] for r in results["klein"]]
    ax.plot(K, zf_t, "b-o", ms=4, lw=1.5, label="Torus")
    ax.plot(K, zf_k, "r-s", ms=4, lw=1.5, label="Klein")
    ax.set_xlabel("K")
    ax.set_ylabel("f(|v| < 0.5)")
    ax.set_title("D. Unlocked fraction")
    ax.legend()
    ax.grid(True, alpha=0.3)

    # E: x-gradient (winding in twist direction)
    ax = axes[2, 0]
    gx_t = [r["gx"] for r in results["torus"]]
    gx_k = [r["gx"] for r in results["klein"]]
    gy_t = [r["gy"] for r in results["torus"]]
    gy_k = [r["gy"] for r in results["klein"]]
    ax.plot(K, gx_t, "b-o", ms=4, lw=1.5, label="Torus <∂x>")
    ax.plot(K, gx_k, "r-s", ms=4, lw=1.5, label="Klein <∂x>")
    ax.plot(K, gy_t, "b--^", ms=4, lw=1, label="Torus <∂y>")
    ax.plot(K, gy_k, "r--v", ms=4, lw=1, label="Klein <∂y>")
    ax.set_xlabel("K")
    ax.set_ylabel("Phase gradient")
    ax.set_title("E. Directional gradients")
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # F: Winding number
    ax = axes[2, 1]
    wn_t = [r["winding"] for r in results["torus"]]
    wn_k = [r["winding"] for r in results["klein"]]
    ax.plot(K, wn_t, "b-o", ms=4, lw=1.5, label="Torus")
    ax.plot(K, wn_k, "r-s", ms=4, lw=1.5, label="Klein")
    ax.set_xlabel("K")
    ax.set_ylabel("Winding number")
    ax.set_title("F. Center oscillator winding")
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    out_path = "sync_cost/derivations/klein_kuramoto_sweep.png"
    fig.savefig(out_path, dpi=150)
    print(f"\nSaved: {out_path}")

    print(f"\n{'=' * 70}")
    print("  DONE")
    print("=" * 70)


if __name__ == "__main__":
    main()
