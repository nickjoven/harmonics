"""
Denomination boundary: numerical tests for D30.

Three observables:
1. Intermittency at the transition coupling
2. Mediant peak emergence when parent modes are degenerate
3. Fine coupling sweep for fractal structure of mode-lock onsets

Uses the Stribeck lattice.
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

# ============================================================
# Test 1: Intermittency at the transition coupling
# ============================================================
# Run at F_n = 3.0 (in the transition window) and look for
# alternating sinusoidal / staircase epochs in the time series.

print("Test 1: Intermittency at F_n = 3.0 ...")
lattice = StribeckLattice(
    n_elements=n_elements, drive_amp=drive_amp, drive_freq=drive_freq,
    normal_force=3.0, mu_static=1.2, mu_kinetic=0.25,
    v_threshold=0.15, damping=0.02, stiffness=1.0,
)
result = lattice.simulate(dt=dt, n_steps=1_000_000, downsample=4)
t = np.array(result["t"])
v3 = np.array(result["v_3"])

# Compute local "staircase-ness": ratio of time spent near zero velocity
# (locked / plateau) vs time in transition. Use sliding window.
period = 2 * np.pi / drive_freq
samples_per_period = int(period / (dt * 4))
n_windows = len(v3) // samples_per_period

plateau_fraction = []
for i in range(n_windows):
    chunk = v3[i * samples_per_period:(i + 1) * samples_per_period]
    if len(chunk) == 0:
        continue
    v_range = np.max(np.abs(chunk))
    if v_range == 0:
        plateau_fraction.append(1.0)
        continue
    # Fraction of samples within 10% of a local extremum (plateau)
    near_max = np.sum(np.abs(chunk) > 0.8 * v_range) / len(chunk)
    plateau_fraction.append(near_max)

plateau_fraction = np.array(plateau_fraction)

# ============================================================
# Test 2: Mediant peak emergence
# ============================================================
# Sweep coupling finely and track spectral peaks at 1/2, 1/3, and 2/5
# of the drive frequency. When 1/2 and 1/3 are comparable, 2/5 should appear.

print("Test 2: Mediant peak emergence ...")
fn_sweep = np.linspace(0.5, 6.0, 40)
peak_1_2 = []
peak_1_3 = []
peak_2_5 = []
peak_2_3 = []

f_drive_hz = drive_freq / (2 * np.pi)

for fn in fn_sweep:
    lattice = StribeckLattice(
        n_elements=n_elements, drive_amp=drive_amp, drive_freq=drive_freq,
        normal_force=fn, mu_static=1.2, mu_kinetic=0.25,
        v_threshold=0.15, damping=0.02, stiffness=1.0,
    )
    res = lattice.simulate(dt=dt, n_steps=600_000, downsample=4)
    t_r = np.array(res["t"])
    v_r = np.array(res["v_3"])
    # Steady state: last 20%
    n_ss = len(v_r) // 5
    v_ss = v_r[-n_ss:]
    t_ss = t_r[-n_ss:]

    freqs = np.fft.rfftfreq(len(v_ss), d=(t_ss[1] - t_ss[0]))
    spectrum = np.abs(np.fft.rfft(v_ss * np.hanning(len(v_ss)))) / len(v_ss)
    f_norm = freqs / f_drive_hz

    # Extract power at specific rationals (within ±0.02 bin)
    def power_at(ratio):
        mask = np.abs(f_norm - ratio) < 0.03
        return np.max(spectrum[mask]) if np.any(mask) else 0.0

    peak_1_2.append(power_at(0.5))
    peak_1_3.append(power_at(1/3))
    peak_2_5.append(power_at(0.4))
    peak_2_3.append(power_at(2/3))

    sys.stdout.write(f"\r  F_n = {fn:.2f}")
    sys.stdout.flush()

print()
peak_1_2 = np.array(peak_1_2)
peak_1_3 = np.array(peak_1_3)
peak_2_5 = np.array(peak_2_5)
peak_2_3 = np.array(peak_2_3)

# ============================================================
# Test 3: Fine coupling sweep — mode-lock onset structure
# ============================================================
# Count distinct spectral peaks above noise floor as function of K.
# The onset of new peaks should show staircase structure.

print("Test 3: Mode-lock onset staircase ...")
fn_fine = np.linspace(0.1, 5.0, 80)
n_peaks_list = []

for fn in fn_fine:
    lattice = StribeckLattice(
        n_elements=n_elements, drive_amp=drive_amp, drive_freq=drive_freq,
        normal_force=fn, mu_static=1.2, mu_kinetic=0.25,
        v_threshold=0.15, damping=0.02, stiffness=1.0,
    )
    res = lattice.simulate(dt=dt, n_steps=400_000, downsample=4)
    t_r = np.array(res["t"])
    v_r = np.array(res["v_3"])
    n_ss = len(v_r) // 5
    v_ss = v_r[-n_ss:]
    t_ss = t_r[-n_ss:]

    freqs = np.fft.rfftfreq(len(v_ss), d=(t_ss[1] - t_ss[0]))
    spectrum = np.abs(np.fft.rfft(v_ss * np.hanning(len(v_ss)))) / len(v_ss)
    f_norm = freqs / f_drive_hz

    # Count peaks above 5% of maximum, in range 0.1 < f/f_d < 4
    mask = (f_norm > 0.1) & (f_norm < 4.0)
    spec_m = spectrum[mask]
    threshold = 0.05 * np.max(spec_m) if np.max(spec_m) > 0 else 0
    # Simple peak counting: local maxima above threshold
    peaks = 0
    for i in range(1, len(spec_m) - 1):
        if spec_m[i] > spec_m[i-1] and spec_m[i] > spec_m[i+1] and spec_m[i] > threshold:
            peaks += 1
    n_peaks_list.append(peaks)

    sys.stdout.write(f"\r  F_n = {fn:.2f}")
    sys.stdout.flush()

print()

# ============================================================
# Plot
# ============================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot 1: Intermittency time series
ax1 = axes[0, 0]
window_t = np.arange(len(plateau_fraction)) * period
ax1.plot(window_t, plateau_fraction, "k-", linewidth=0.5)
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Plateau fraction per period")
ax1.set_title("Test 1: Intermittency at F_n = 3.0 (element 3)")
ax1.axhline(0.5, color="red", linestyle="--", alpha=0.5, label="50% threshold")
ax1.legend(fontsize=8)

# Plot 2: Mediant peak emergence
ax2 = axes[0, 1]
ax2.semilogy(fn_sweep, peak_1_2, "C0-o", markersize=3, label="f = 1/2 f_d")
ax2.semilogy(fn_sweep, peak_1_3, "C1-s", markersize=3, label="f = 1/3 f_d")
ax2.semilogy(fn_sweep, peak_2_5, "C3-^", markersize=4, label="f = 2/5 f_d (mediant)")
ax2.semilogy(fn_sweep, peak_2_3, "C2-d", markersize=3, label="f = 2/3 f_d")
ax2.set_xlabel("Normal force F_n")
ax2.set_ylabel("Spectral amplitude (log)")
ax2.set_title("Test 2: Mediant peak at 2/5 when 1/2 ≈ 1/3")
ax2.legend(fontsize=8)
ax2.grid(True, alpha=0.3)

# Find crossing point of 1/2 and 1/3
ratio_12_13 = peak_1_2 / (peak_1_3 + 1e-12)
cross_idx = np.argmin(np.abs(np.log(ratio_12_13 + 1e-12)))
if cross_idx > 0 and cross_idx < len(fn_sweep) - 1:
    ax2.axvline(fn_sweep[cross_idx], color="gray", linestyle=":", alpha=0.5,
                label=f"1/2 ≈ 1/3 at F_n ≈ {fn_sweep[cross_idx]:.1f}")
    ax2.legend(fontsize=8)

# Plot 3: Mode-lock onset staircase
ax3 = axes[1, 0]
ax3.plot(fn_fine, n_peaks_list, "k-o", markersize=2)
ax3.set_xlabel("Normal force F_n")
ax3.set_ylabel("Number of spectral peaks")
ax3.set_title("Test 3: Mode-lock onset count vs coupling")
ax3.grid(True, alpha=0.3)

# Plot 4: Intermittency histogram
ax4 = axes[1, 1]
ax4.hist(plateau_fraction, bins=30, color="k", alpha=0.7, edgecolor="white")
ax4.set_xlabel("Plateau fraction")
ax4.set_ylabel("Count (periods)")
ax4.set_title("Intermittency distribution at F_n = 3.0")
# Bimodal = denomination switching; unimodal = one regime
ax4.axvline(np.median(plateau_fraction), color="red", linestyle="--",
            label=f"median = {np.median(plateau_fraction):.2f}")
ax4.legend(fontsize=8)

plt.tight_layout()
out = __import__("pathlib").Path(__file__).parent / "denomination_boundary.png"
plt.savefig(out, dpi=150)
print(f"\nSaved: {out}")

# Print summary
print("\n=== Summary ===")
print(f"Test 1: Plateau fraction range [{plateau_fraction.min():.3f}, {plateau_fraction.max():.3f}]")
print(f"        Std dev: {plateau_fraction.std():.3f} (high = intermittent)")
bimodal = np.percentile(plateau_fraction, 25) < 0.4 and np.percentile(plateau_fraction, 75) > 0.6
print(f"        Bimodal: {'YES' if bimodal else 'no'}")

print(f"\nTest 2: Peak amplitudes at crossing:")
if cross_idx > 0:
    print(f"        F_n ≈ {fn_sweep[cross_idx]:.1f}")
    print(f"        1/2: {peak_1_2[cross_idx]:.2e}")
    print(f"        1/3: {peak_1_3[cross_idx]:.2e}")
    print(f"        2/5: {peak_2_5[cross_idx]:.2e}")
    print(f"        2/3: {peak_2_3[cross_idx]:.2e}")
    mediant_present = peak_2_5[cross_idx] > 0.1 * min(peak_1_2[cross_idx], peak_1_3[cross_idx])
    print(f"        Mediant present: {'YES' if mediant_present else 'no'}")

print(f"\nTest 3: Peak count range [{min(n_peaks_list)}, {max(n_peaks_list)}]")
# Check for staircase: count number of distinct levels
levels = sorted(set(n_peaks_list))
print(f"        Distinct levels: {len(levels)} ({levels})")
staircase = len(levels) > 3
print(f"        Staircase structure: {'YES' if staircase else 'no'}")

plt.close()
