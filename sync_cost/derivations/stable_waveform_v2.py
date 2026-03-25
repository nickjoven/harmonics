"""
Stable waveform v2: zoom into the mode-locking window.

The sweet spot is F_n ≈ 2–6 where the system is past the sine
but before broadband chaos. Focus on element 4 (past N=3 critical
chain length). Longer runs, finer coupling sweep.
"""

import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[2]))

import numpy as np
import matplotlib.pyplot as plt
from stribeck_lattice import StribeckLattice

drive_freq = 6.0
drive_amp = 0.5
dt = 0.0005
downsample = 2  # finer sampling for waveform shape
n_elements = 6
n_steps = 1_500_000  # 750s, very long settling

couplings = [1.5, 2.5, 3.5, 5.0]
period = 2 * np.pi / drive_freq

fig, axes = plt.subplots(len(couplings), 3,
                          figsize=(16, 3.5 * len(couplings)),
                          gridspec_kw={"width_ratios": [2.5, 1, 1]})

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
    n_ss = len(t) // 10  # last 10%
    t_ss = t[-n_ss:] - t[-n_ss]

    # Element 4 (past N=3 threshold)
    v4 = np.array(result["v_4"])[-n_ss:]
    x4 = np.array(result["x_4"])[-n_ss:]

    # Also element 1 for comparison
    v1 = np.array(result["v_1"])[-n_ss:]

    mask = t_ss < 8 * period

    # Waveform overlay: element 1 vs 4
    ax_w = axes[idx, 0]
    # Normalize both for shape comparison
    v1m, v4m = v1[mask], v4[mask]
    v1_norm = v1m / (np.max(np.abs(v1m)) or 1)
    v4_norm = v4m / (np.max(np.abs(v4m)) or 1)
    ax_w.plot(t_ss[mask] / period, v1_norm, "C7-", linewidth=0.6, alpha=0.5, label="elem 1 (normalized)")
    ax_w.plot(t_ss[mask] / period, v4_norm, "k-", linewidth=0.9, label="elem 4 (normalized)")
    ax_w.set_ylabel("v(t) / max|v|")
    ax_w.set_title(f"F_n = {fn:.1f}", fontsize=11)
    ax_w.set_xlim(0, 8)
    ax_w.legend(fontsize=7)
    if idx == len(couplings) - 1:
        ax_w.set_xlabel("Drive periods")

    # Log spectrum of element 4
    ax_fft = axes[idx, 1]
    freqs = np.fft.rfftfreq(len(v4), d=(t_ss[1] - t_ss[0]))
    spectrum = np.abs(np.fft.rfft(v4 * np.hanning(len(v4)))) / len(v4)
    f_norm = freqs / (drive_freq / (2 * np.pi))
    mask_f = (f_norm > 0.05) & (f_norm < 4)
    ax_fft.semilogy(f_norm[mask_f], spectrum[mask_f] + 1e-12, "k-", linewidth=0.6)
    ax_fft.set_ylabel("|V(f)| (log)")
    ax_fft.set_title("Elem 4 spectrum", fontsize=9)
    ax_fft.set_xlim(0, 4)
    # Mark Stern-Brocot rationals up to depth 3
    rationals = [(1,3), (1,2), (2,3), (1,1), (3,2), (2,1), (3,1)]
    for p, q in rationals:
        ax_fft.axvline(p/q, color="red", alpha=0.3, linewidth=0.5, linestyle="--")
        ax_fft.text(p/q, ax_fft.get_ylim()[1] if idx == 0 else 0,
                    f"{p}/{q}", fontsize=6, ha="center", va="bottom",
                    color="red", alpha=0.5)
    if idx == len(couplings) - 1:
        ax_fft.set_xlabel("f / f_drive")

    # Phase portrait element 4
    ax_pp = axes[idx, 2]
    ax_pp.plot(x4[mask], v4[mask], "k-", linewidth=0.25, alpha=0.5)
    ax_pp.set_xlabel("x")
    ax_pp.set_ylabel("v")
    ax_pp.set_title("Phase portrait (elem 4)", fontsize=9)

    # Print peak frequencies
    top5 = np.argsort(spectrum)[::-1][:5]
    peaks = f_norm[top5]
    amps = spectrum[top5]
    print(f"  Top peaks (f/f_d): {', '.join(f'{p:.3f}' for p in sorted(peaks))}")
    print(f"  Amplitudes:        {', '.join(f'{a:.2e}' for a in amps)}")

plt.tight_layout()
out = __import__("pathlib").Path(__file__).parent / "stable_waveform_v2.png"
plt.savefig(out, dpi=150)
print(f"\nSaved: {out}")
plt.close()
