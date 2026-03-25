"""
Waveform evolution: sine → triangle → square → staircase

Runs the Stribeck lattice at increasing coupling strengths (normal_force)
and plots the velocity waveform at each element, showing how the
sinusoidal drive progressively locks into rational plateaus.

Also: for a fixed high coupling, plots the waveform at elements 1–5
showing the spatial progression from distorted sine to staircase.

Output: waveform_evolution.png
"""

import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[2]))

import numpy as np
import matplotlib.pyplot as plt
from stribeck_lattice import StribeckLattice

# --- Experiment 1: Coupling sweep at element 2 (first "output" element) ---

coupling_strengths = [0.05, 0.2, 0.4, 0.8, 1.5]
labels = ["K ≈ 0.05 (sine)", "K ≈ 0.2 (clipped)", "K ≈ 0.4 (triangle)",
          "K ≈ 0.8 (square-ish)", "K ≈ 1.5 (staircase)"]

fig, axes = plt.subplots(len(coupling_strengths) + 1, 2,
                          figsize=(14, 3 * (len(coupling_strengths) + 1)),
                          gridspec_kw={"width_ratios": [2, 1]})

drive_freq = 6.0  # rad/s
drive_amp = 0.5
n_elements = 5
dt = 0.0005
n_steps = 400_000
downsample = 4

for idx, fn in enumerate(coupling_strengths):
    print(f"Running coupling {fn:.2f} ({idx+1}/{len(coupling_strengths)})...")
    lattice = StribeckLattice(
        n_elements=n_elements,
        drive_amp=drive_amp,
        drive_freq=drive_freq,
        normal_force=fn,
        mu_static=1.2,
        mu_kinetic=0.25,
        v_threshold=0.15,
        damping=0.02,
        stiffness=1.0,
    )
    result = lattice.simulate(dt=dt, n_steps=n_steps, downsample=downsample)

    t = np.array(result["t"])
    # Use element 2 (first element past the contact pair)
    v2 = np.array(result["v_2"])

    # Steady state: last 20% of simulation
    n_ss = len(t) // 5
    t_ss = t[-n_ss:] - t[-n_ss]
    v_ss = v2[-n_ss:]

    # Waveform: show ~4 drive periods
    period = 2 * np.pi / drive_freq
    mask = t_ss < 4 * period
    ax_wave = axes[idx, 0]
    ax_wave.plot(t_ss[mask] / period, v_ss[mask], "k-", linewidth=0.8)
    ax_wave.set_ylabel("v(t)")
    ax_wave.set_title(labels[idx], fontsize=10)
    ax_wave.set_xlim(0, 4)
    if idx == len(coupling_strengths) - 1:
        ax_wave.set_xlabel("Drive periods")

    # Power spectrum
    ax_fft = axes[idx, 1]
    freqs = np.fft.rfftfreq(len(v_ss), d=(t_ss[1] - t_ss[0]))
    spectrum = np.abs(np.fft.rfft(v_ss * np.hanning(len(v_ss)))) / len(v_ss)
    # Normalize frequencies to drive frequency
    f_norm = freqs / (drive_freq / (2 * np.pi))
    mask_f = f_norm < 5
    ax_fft.plot(f_norm[mask_f], spectrum[mask_f], "k-", linewidth=0.8)
    ax_fft.set_ylabel("|V(f)|")
    ax_fft.set_title("Spectrum", fontsize=10)
    ax_fft.set_xlim(0, 5)
    # Mark rational frequencies
    for p, q, lbl in [(1, 1, "1"), (1, 2, "1/2"), (1, 3, "1/3"),
                       (2, 3, "2/3"), (3, 2, "3/2"), (2, 1, "2")]:
        ax_fft.axvline(p / q, color="red", alpha=0.3, linewidth=0.5)

    if idx == len(coupling_strengths) - 1:
        ax_fft.set_xlabel("f / f_drive")

# --- Experiment 2: Spatial progression at high coupling ---

print("Running spatial progression (high coupling)...")
lattice_hi = StribeckLattice(
    n_elements=6,
    drive_amp=drive_amp,
    drive_freq=drive_freq,
    normal_force=1.2,
    mu_static=1.2,
    mu_kinetic=0.25,
    v_threshold=0.15,
    damping=0.02,
    stiffness=1.0,
)
result_hi = lattice_hi.simulate(dt=dt, n_steps=n_steps, downsample=downsample)
t_hi = np.array(result_hi["t"])
n_ss = len(t_hi) // 5
t_ss = t_hi[-n_ss:] - t_hi[-n_ss]
period = 2 * np.pi / drive_freq
mask = t_ss < 4 * period

ax_spatial = axes[-1, 0]
colors = plt.cm.viridis(np.linspace(0.2, 0.9, 5))
for elem in range(1, 6):
    v_elem = np.array(result_hi[f"v_{elem}"])[-n_ss:]
    # Normalize amplitude for comparison
    vmax = np.max(np.abs(v_elem[mask])) or 1.0
    ax_spatial.plot(t_ss[mask] / period, v_elem[mask] / vmax + elem * 2.5,
                    color=colors[elem - 1], linewidth=0.8,
                    label=f"element {elem}")
ax_spatial.set_xlabel("Drive periods")
ax_spatial.set_ylabel("v(t) (offset)")
ax_spatial.set_title("Spatial progression: elements 1–5 at high coupling", fontsize=10)
ax_spatial.legend(fontsize=8, loc="upper right")

# Spectrum of element 5 at high coupling
ax_sp5 = axes[-1, 1]
v5 = np.array(result_hi["v_5"])[-n_ss:]
freqs = np.fft.rfftfreq(len(v5), d=(t_ss[1] - t_ss[0]))
spectrum5 = np.abs(np.fft.rfft(v5 * np.hanning(len(v5)))) / len(v5)
f_norm = freqs / (drive_freq / (2 * np.pi))
mask_f = f_norm < 5
ax_sp5.plot(f_norm[mask_f], spectrum5[mask_f], "k-", linewidth=0.8)
ax_sp5.set_xlabel("f / f_drive")
ax_sp5.set_ylabel("|V(f)|")
ax_sp5.set_title("Element 5 spectrum", fontsize=10)
for p, q, lbl in [(1, 1, "1"), (1, 2, "1/2"), (1, 3, "1/3"),
                   (2, 3, "2/3"), (3, 2, "3/2"), (2, 1, "2")]:
    ax_sp5.axvline(p / q, color="red", alpha=0.3, linewidth=0.5)

plt.tight_layout()
out = __import__("pathlib").Path(__file__).parent / "waveform_evolution.png"
plt.savefig(out, dpi=150)
print(f"\nSaved: {out}")
plt.close()
