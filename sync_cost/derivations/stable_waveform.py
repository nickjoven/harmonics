"""
Find the stable locked waveform at high coupling.

Push coupling well past K=1, run long enough for transients to die,
and plot the final periodic orbit. The question: what does the
stable oscillation look like when mode-locking is complete?
"""

import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[2]))

import numpy as np
import matplotlib.pyplot as plt
from stribeck_lattice import StribeckLattice

drive_freq = 6.0
drive_amp = 0.5
dt = 0.0005
downsample = 4

# Sweep from moderate to very high coupling, long runs for settling
couplings = [0.4, 1.0, 2.0, 4.0, 8.0, 16.0]
n_elements = 5
# Long run: 1.2M steps = 600s at dt=0.0005
n_steps = 1_200_000

fig, axes = plt.subplots(len(couplings), 3,
                          figsize=(16, 3 * len(couplings)),
                          gridspec_kw={"width_ratios": [2, 1, 1]})

period = 2 * np.pi / drive_freq

for idx, fn in enumerate(couplings):
    print(f"Running F_n = {fn:.1f} ({idx+1}/{len(couplings)})...")
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

    # Use last 10% for steady state (very conservative)
    n_ss = len(t) // 10
    t_ss = t[-n_ss:] - t[-n_ss]

    # Element 2 (through one contact) and element 4 (through three contacts)
    v2 = np.array(result["v_2"])[-n_ss:]
    v4 = np.array(result["v_4"])[-n_ss:]

    # Show 6 drive periods of waveform
    mask = t_ss < 6 * period

    # Waveform at element 2
    ax_w = axes[idx, 0]
    ax_w.plot(t_ss[mask] / period, v2[mask], "k-", linewidth=0.7, label="elem 2")
    ax_w.plot(t_ss[mask] / period, v4[mask], "C0-", linewidth=0.7, alpha=0.7, label="elem 4")
    ax_w.set_ylabel("v(t)")
    ax_w.set_title(f"F_n = {fn:.1f}  (K/K_c ≈ {fn/0.15:.0f})", fontsize=10)
    ax_w.set_xlim(0, 6)
    ax_w.legend(fontsize=7, loc="upper right")
    if idx == len(couplings) - 1:
        ax_w.set_xlabel("Drive periods")

    # Spectrum of element 2
    ax_fft = axes[idx, 1]
    freqs = np.fft.rfftfreq(len(v2), d=(t_ss[1] - t_ss[0]))
    spectrum = np.abs(np.fft.rfft(v2 * np.hanning(len(v2)))) / len(v2)
    f_norm = freqs / (drive_freq / (2 * np.pi))
    mask_f = f_norm < 4
    ax_fft.semilogy(f_norm[mask_f], spectrum[mask_f] + 1e-10, "k-", linewidth=0.7)
    ax_fft.set_ylabel("|V(f)| (log)")
    ax_fft.set_title("Elem 2 spectrum", fontsize=9)
    ax_fft.set_xlim(0, 4)
    for p, q in [(1, 1), (1, 2), (1, 3), (2, 3), (3, 2), (2, 1), (3, 1)]:
        ax_fft.axvline(p / q, color="red", alpha=0.25, linewidth=0.5)
    if idx == len(couplings) - 1:
        ax_fft.set_xlabel("f / f_drive")

    # Phase portrait: v vs x for element 2 (last 6 periods)
    x2 = np.array(result["x_2"])[-n_ss:]
    ax_pp = axes[idx, 2]
    ax_pp.plot(x2[mask], v2[mask], "k-", linewidth=0.3, alpha=0.6)
    ax_pp.set_xlabel("x")
    ax_pp.set_ylabel("v")
    ax_pp.set_title("Phase portrait (elem 2)", fontsize=9)
    ax_pp.set_aspect("equal", adjustable="datalim")

plt.tight_layout()
out = __import__("pathlib").Path(__file__).parent / "stable_waveform.png"
plt.savefig(out, dpi=150)
print(f"\nSaved: {out}")
plt.close()

# --- Print dominant frequencies at each coupling ---
print("\nDominant frequencies (element 2, steady state):")
print(f"{'F_n':>6}  {'f1/f_d':>8}  {'f2/f_d':>8}  {'f3/f_d':>8}")
for idx, fn in enumerate(couplings):
    lattice = StribeckLattice(
        n_elements=n_elements, drive_amp=drive_amp, drive_freq=drive_freq,
        normal_force=fn, mu_static=1.2, mu_kinetic=0.25,
        v_threshold=0.15, damping=0.02, stiffness=1.0,
    )
    result = lattice.simulate(dt=dt, n_steps=n_steps, downsample=downsample)
    t = np.array(result["t"])
    n_ss = len(t) // 10
    v2 = np.array(result["v_2"])[-n_ss:]
    t_ss = t[-n_ss:]
    freqs = np.fft.rfftfreq(len(v2), d=(t_ss[1] - t_ss[0]))
    spectrum = np.abs(np.fft.rfft(v2 * np.hanning(len(v2))))
    f_norm = freqs / (drive_freq / (2 * np.pi))
    # Top 3 peaks
    peak_idx = np.argsort(spectrum)[::-1][:3]
    peaks = sorted(f_norm[peak_idx])
    print(f"{fn:6.1f}  {peaks[0]:8.3f}  {peaks[1]:8.3f}  {peaks[2]:8.3f}")
