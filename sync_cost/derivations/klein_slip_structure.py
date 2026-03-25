"""
Slip structure on the Klein bottle vs torus.

Run Kuramoto on both topologies, capture full velocity time series,
and compare dwell time distributions. If the XOR filter shapes the
slip dynamics, the Klein bottle should show:
1. Suppressed dwell at XOR-forbidden velocity ratios
2. Enhanced dwell at XOR-allowed velocity ratios
3. Different acceleration statistics during slips
"""

import numpy as np
import matplotlib.pyplot as plt
from klein_bottle_kuramoto import (
    neighbors_torus, neighbors_klein,
    kuramoto_2d, rk4_step_2d, order_parameter_2d
)


def run_and_record(Nx, Ny, K, neighbor_func, dt=0.005, T=500.0,
                   gamma=0.5, seed=42):
    """Run simulation and record full velocity time series."""
    rng = np.random.default_rng(seed)
    omega = gamma * np.clip(rng.standard_cauchy((Nx, Ny)), -5, 5)
    theta = rng.uniform(0, 0.1, (Nx, Ny))

    n_steps = int(T / dt)
    # Record velocity (dtheta/dt) of center oscillator
    ci, cj = Nx // 2, Ny // 2

    t_arr = np.zeros(n_steps)
    v_arr = np.zeros(n_steps)
    r_arr = np.zeros(n_steps)

    theta_prev = theta.copy()

    for step in range(n_steps):
        t_arr[step] = step * dt
        r_arr[step] = order_parameter_2d(theta)

        # Velocity = dtheta/dt from the Kuramoto equation directly
        dtheta = kuramoto_2d(theta, omega, K, Nx, Ny, neighbor_func)
        v_arr[step] = dtheta[ci, cj]

        theta = rk4_step_2d(theta, omega, K, Nx, Ny, neighbor_func, dt)

    return t_arr, v_arr, r_arr, omega[ci, cj]


# ============================================================
# Run both topologies
# ============================================================

Nx, Ny = 5, 5
dt = 0.005
T = 800.0  # long run for statistics

# Sweep K to find the transition regime
print("Finding transition regime...")
for K_test in [1.0, 2.0, 3.0, 4.0, 6.0]:
    _, v_test, _, _ = run_and_record(Nx, Ny, K_test, neighbors_klein, dt=dt, T=100.0)
    v_range = np.max(np.abs(v_test[len(v_test)//2:]))
    v_spread = np.std(v_test[len(v_test)//2:])
    print(f"  K={K_test}: v_range={v_range:.4f}, v_std={v_spread:.4f}")

K = 3.0  # transition regime: partially locked

print(f"Running {Nx}×{Ny} lattice, K={K}, T={T}...")

print("  Torus...")
t_tor, v_tor, r_tor, omega_tor = run_and_record(
    Nx, Ny, K, neighbors_torus, dt=dt, T=T)

print("  Klein bottle...")
t_kln, v_kln, r_kln, omega_kln = run_and_record(
    Nx, Ny, K, neighbors_klein, dt=dt, T=T)

# Steady state: last 50%
n_half = len(t_tor) // 2
v_tor_ss = v_tor[n_half:]
v_kln_ss = v_kln[n_half:]
t_ss = t_tor[n_half:] - t_tor[n_half]

print(f"  Torus:  omega_center = {omega_tor:.4f}, <|v|> = {np.mean(np.abs(v_tor_ss)):.4f}")
print(f"  Klein:  omega_center = {omega_kln:.4f}, <|v|> = {np.mean(np.abs(v_kln_ss)):.4f}")


# ============================================================
# Part 1: Velocity histograms comparison
# ============================================================

fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# Normalize velocities to drive frequency for comparison
v_scale_tor = np.max(np.abs(v_tor_ss)) or 1
v_scale_kln = np.max(np.abs(v_kln_ss)) or 1

# Torus histogram
ax = axes[0, 0]
ax.hist(v_tor_ss / v_scale_tor, bins=200, color="C0", alpha=0.7,
        edgecolor="none", density=True)
ax.set_xlabel("v / v_max")
ax.set_ylabel("Density")
ax.set_title(f"Torus {Nx}×{Ny} velocity distribution")

# Klein bottle histogram
ax = axes[0, 1]
ax.hist(v_kln_ss / v_scale_kln, bins=200, color="C1", alpha=0.7,
        edgecolor="none", density=True)
ax.set_xlabel("v / v_max")
ax.set_ylabel("Density")
ax.set_title(f"Klein bottle {Nx}×{Ny} velocity distribution")

# Overlay
ax = axes[0, 2]
ax.hist(v_tor_ss / v_scale_tor, bins=200, color="C0", alpha=0.5,
        edgecolor="none", density=True, label="Torus")
ax.hist(v_kln_ss / v_scale_kln, bins=200, color="C1", alpha=0.5,
        edgecolor="none", density=True, label="Klein")
ax.legend()
ax.set_xlabel("v / v_max")
ax.set_title("Overlay")

# Mark rational velocity levels
for ax_row in axes[0, :]:
    for p, q in [(1,3),(2,5),(1,2),(3,5),(2,3)]:
        for sign in [1, -1]:
            ax_row.axvline(sign * p/q, color="red", alpha=0.2,
                          linewidth=0.5, linestyle="--")


# ============================================================
# Part 2: Acceleration distributions
# ============================================================

dv_tor = np.diff(v_tor_ss) / dt
dv_kln = np.diff(v_kln_ss) / dt

ax = axes[1, 0]
ax.hist(np.abs(dv_tor), bins=200, color="C0", alpha=0.7,
        edgecolor="none", density=True)
ax.set_xlabel("|dv/dt|")
ax.set_ylabel("Density (log)")
ax.set_title("Torus acceleration")
ax.set_yscale("log")

ax = axes[1, 1]
ax.hist(np.abs(dv_kln), bins=200, color="C1", alpha=0.7,
        edgecolor="none", density=True)
ax.set_xlabel("|dv/dt|")
ax.set_ylabel("Density (log)")
ax.set_title("Klein bottle acceleration")
ax.set_yscale("log")

# Ratio of Klein to Torus dwell time at each velocity level
ax = axes[1, 2]
bins = np.linspace(-1, 1, 101)
hist_tor, _ = np.histogram(v_tor_ss / v_scale_tor, bins=bins, density=True)
hist_kln, _ = np.histogram(v_kln_ss / v_scale_kln, bins=bins, density=True)
bin_centers = 0.5 * (bins[:-1] + bins[1:])

# Ratio with floor to avoid div by zero
ratio = (hist_kln + 1e-3) / (hist_tor + 1e-3)
ax.plot(bin_centers, ratio, "k-", linewidth=0.8)
ax.axhline(1.0, color="red", linestyle="--", alpha=0.5)
ax.set_xlabel("v / v_max")
ax.set_ylabel("Klein / Torus density ratio")
ax.set_title("Topology effect on dwell (>1 = Klein favored)")

# Mark rationals
for p, q in [(1,3),(2,5),(1,2),(3,5),(2,3)]:
    for sign in [1, -1]:
        ax.axvline(sign * p/q, color="red", alpha=0.2,
                  linewidth=0.5, linestyle="--")

plt.tight_layout()
out = __import__("pathlib").Path(__file__).parent / "klein_slip_structure.png"
plt.savefig(out, dpi=150)
print(f"\nSaved: {out}")
plt.close()


# ============================================================
# Part 3: Dwell time at rational bands — Klein vs Torus
# ============================================================

print("\n" + "=" * 70)
print("  DWELL TIME COMPARISON: Klein bottle vs Torus")
print("=" * 70)

bands = [
    (0.0, 0.15, "near zero", 0, 1),
    (0.15, 0.4, "~1/3", 1, 3),
    (0.35, 0.45, "~2/5 med", 2, 5),
    (0.45, 0.55, "~1/2", 1, 2),
    (0.55, 0.65, "~3/5 med", 3, 5),
    (0.6, 0.75, "~2/3", 2, 3),
    (0.75, 1.0, "~1/1", 1, 1),
]

v_tor_norm = np.abs(v_tor_ss) / v_scale_tor
v_kln_norm = np.abs(v_kln_ss) / v_scale_kln

print(f"\n  {'Band':>12s}  {'Torus %':>9s}  {'Klein %':>9s}  {'Ratio K/T':>10s}  "
      f"{'XOR(p+q)':>10s}")
print("  " + "-" * 60)

for lo, hi, name, p, q in bands:
    t_frac = np.mean((v_tor_norm >= lo) & (v_tor_norm < hi))
    k_frac = np.mean((v_kln_norm >= lo) & (v_kln_norm < hi))
    ratio = k_frac / t_frac if t_frac > 0 else float('inf')
    xor = "odd" if (p + q) % 2 == 1 else "even"
    marker = "  ← ENHANCED" if ratio > 1.3 else ("  ← SUPPRESSED" if ratio < 0.7 else "")
    print(f"  {name:>12s}  {t_frac*100:8.2f}%  {k_frac*100:8.2f}%  "
          f"{ratio:10.3f}  {xor:>10s}{marker}")

print(f"""
  If XOR shapes dwell: modes with p+q ODD (allowed) should be
  ENHANCED on Klein relative to torus, and p+q EVEN (forbidden)
  should be SUPPRESSED.
""")

# ============================================================
# Part 4: Spectral comparison
# ============================================================

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

for ax, v_ss, label, color in [(axes[0], v_tor_ss, "Torus", "C0"),
                                  (axes[1], v_kln_ss, "Klein", "C1")]:
    freqs = np.fft.rfftfreq(len(v_ss), d=dt)
    S = np.abs(np.fft.rfft(v_ss * np.hanning(len(v_ss)))) / len(v_ss)

    # Normalize to natural frequency of center oscillator
    f_nat = abs(omega_tor) / (2 * np.pi) if label == "Torus" else abs(omega_kln) / (2 * np.pi)
    if f_nat > 0:
        f_norm = freqs / f_nat
    else:
        f_norm = freqs

    mask = (f_norm > 0.05) & (f_norm < 5)
    ax.semilogy(f_norm[mask], S[mask] + 1e-12, f"{color}-", linewidth=0.5)
    ax.set_xlabel("f / f_natural")
    ax.set_ylabel("|V(f)|")
    ax.set_title(f"{label} spectrum")

    for p, q in [(1,3),(2,5),(1,2),(3,5),(2,3),(1,1),(3,2),(2,1)]:
        ax.axvline(p/q, color="red", alpha=0.25, linewidth=0.5)

plt.tight_layout()
out2 = __import__("pathlib").Path(__file__).parent / "klein_slip_spectrum.png"
plt.savefig(out2, dpi=150)
print(f"Saved: {out2}")
plt.close()
