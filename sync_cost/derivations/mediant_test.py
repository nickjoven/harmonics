"""
Focused test: mediant peak emergence.

Fine coupling sweep around the 1/2 ≈ 1/3 degeneracy point.
Track all Stern-Brocot depth-3 rationals and their mediants.
"""

import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[2]))

import numpy as np
import matplotlib.pyplot as plt
from stribeck_lattice import StribeckLattice

drive_freq = 6.0
drive_amp = 0.5
dt = 0.0005
n_elements = 5

# Stern-Brocot rationals up to depth 3 (as fractions of drive freq)
# and their mediants
rationals = {
    "1/3": 1/3,
    "2/5": 2/5,   # mediant(1/3, 1/2)
    "1/2": 1/2,
    "3/5": 3/5,   # mediant(1/2, 2/3)
    "2/3": 2/3,
    "3/4": 3/4,   # mediant(2/3, 1/1)
    "1/1": 1.0,
    "4/3": 4/3,   # mediant(1/1, 3/2)
    "3/2": 3/2,
    "5/3": 5/3,   # mediant(3/2, 2/1)
    "2/1": 2.0,
    "5/2": 5/2,   # mediant(2/1, 3/1)
    "3/1": 3.0,
}

fn_sweep = np.linspace(0.3, 4.0, 60)
f_drive_hz = drive_freq / (2 * np.pi)

# Track power at each rational
powers = {name: [] for name in rationals}

for fn in fn_sweep:
    lattice = StribeckLattice(
        n_elements=n_elements, drive_amp=drive_amp, drive_freq=drive_freq,
        normal_force=fn, mu_static=1.2, mu_kinetic=0.25,
        v_threshold=0.15, damping=0.02, stiffness=1.0,
    )
    res = lattice.simulate(dt=dt, n_steps=600_000, downsample=4)
    t_r = np.array(res["t"])
    v_r = np.array(res["v_3"])
    n_ss = len(v_r) // 5
    v_ss = v_r[-n_ss:]
    t_ss = t_r[-n_ss:]

    freqs = np.fft.rfftfreq(len(v_ss), d=(t_ss[1] - t_ss[0]))
    spectrum = np.abs(np.fft.rfft(v_ss * np.hanning(len(v_ss)))) / len(v_ss)
    f_norm = freqs / f_drive_hz

    for name, ratio in rationals.items():
        mask = np.abs(f_norm - ratio) < 0.025
        powers[name].append(np.max(spectrum[mask]) if np.any(mask) else 0.0)

    sys.stdout.write(f"\r  F_n = {fn:.2f}")
    sys.stdout.flush()

print()

# Convert to arrays
for name in powers:
    powers[name] = np.array(powers[name])

# ============================================================
# Plot 1: Parent modes and their mediants
# ============================================================

fig, axes = plt.subplots(3, 1, figsize=(12, 12), sharex=True)

# Panel A: 1/3, 1/2, and mediant 2/5
ax = axes[0]
ax.semilogy(fn_sweep, powers["1/3"], "C0-o", markersize=3, label="1/3 (parent)")
ax.semilogy(fn_sweep, powers["1/2"], "C1-s", markersize=3, label="1/2 (parent)")
ax.semilogy(fn_sweep, powers["2/5"], "C3-^", markersize=4, linewidth=2, label="2/5 (mediant of 1/3, 1/2)")
ax.set_ylabel("Spectral amplitude (log)")
ax.set_title("Mediant test: 2/5 emerges when 1/3 ≈ 1/2")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Mark where 1/3 ≈ 1/2
ratio = powers["1/2"] / (powers["1/3"] + 1e-15)
cross_idx = np.argmin(np.abs(np.log(ratio + 1e-15)))
ax.axvline(fn_sweep[cross_idx], color="gray", linestyle=":", alpha=0.5)

# Panel B: 1/2, 2/3, and mediant 3/5
ax = axes[1]
ax.semilogy(fn_sweep, powers["1/2"], "C1-s", markersize=3, label="1/2 (parent)")
ax.semilogy(fn_sweep, powers["2/3"], "C2-d", markersize=3, label="2/3 (parent)")
ax.semilogy(fn_sweep, powers["3/5"], "C3-^", markersize=4, linewidth=2, label="3/5 (mediant of 1/2, 2/3)")
ax.set_ylabel("Spectral amplitude (log)")
ax.set_title("Mediant test: 3/5 emerges when 1/2 ≈ 2/3")
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel C: All modes — the tree lighting up
ax = axes[2]
parent_modes = ["1/3", "1/2", "2/3", "1/1", "3/2", "2/1", "3/1"]
mediant_modes = ["2/5", "3/5", "3/4", "4/3", "5/3", "5/2"]

for name in parent_modes:
    ax.semilogy(fn_sweep, powers[name], "-", linewidth=1, alpha=0.6, label=f"{name}")
for name in mediant_modes:
    ax.semilogy(fn_sweep, powers[name], "--", linewidth=1.5, alpha=0.8, label=f"{name} (med)")

ax.set_xlabel("Normal force F_n")
ax.set_ylabel("Spectral amplitude (log)")
ax.set_title("Full Stern-Brocot tree: parents (solid) and mediants (dashed)")
ax.legend(fontsize=7, ncol=3, loc="upper left")
ax.grid(True, alpha=0.3)

plt.tight_layout()
out = __import__("pathlib").Path(__file__).parent / "mediant_test.png"
plt.savefig(out, dpi=150)
print(f"\nSaved: {out}")

# ============================================================
# Print the degeneracy table
# ============================================================
print("\n=== Degeneracy resolution table ===")
print(f"{'Parents':>12}  {'F_n cross':>10}  {'Parent power':>13}  {'Mediant':>8}  {'Med power':>10}  {'Med/Parent':>10}")

pairs = [
    ("1/3", "1/2", "2/5"),
    ("1/2", "2/3", "3/5"),
    ("2/3", "1/1", "3/4"),
    ("1/1", "3/2", "4/3"),
    ("3/2", "2/1", "5/3"),
    ("2/1", "3/1", "5/2"),
]

for p1, p2, med in pairs:
    ratio = powers[p1] / (powers[p2] + 1e-15)
    ci = np.argmin(np.abs(np.log(np.abs(ratio) + 1e-15)))
    parent_pwr = min(powers[p1][ci], powers[p2][ci])
    med_pwr = powers[med][ci]
    frac = med_pwr / (parent_pwr + 1e-15)
    print(f"  {p1}+{p2:>3}  {fn_sweep[ci]:10.2f}  {parent_pwr:13.2e}  {med:>8}  {med_pwr:10.2e}  {frac:10.1%}")

plt.close()
