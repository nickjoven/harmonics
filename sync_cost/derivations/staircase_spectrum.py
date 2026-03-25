"""
Fourier analysis of canonical waveforms vs the devil's staircase.

Computes and compares:
1. Sine, sawtooth, triangle, square (textbook)
2. Devil's staircase from the circle map at several K values
3. The lattice waveform at element 4

Also: spectral ordering test — are the staircase peaks ordered
by Stern-Brocot denominator q, and does amplitude scale as (K/2)^q?
"""

import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[2]))

import numpy as np
import matplotlib.pyplot as plt
from stribeck_lattice import StribeckLattice


# ============================================================
# Part 1: Generate canonical waveforms + devil's staircase
# ============================================================

N = 2**16  # samples
t = np.linspace(0, 1, N, endpoint=False)
f0 = 1.0  # fundamental

# Canonical waveforms (one period)
sine = np.sin(2 * np.pi * f0 * t)
sawtooth = 2 * (t * f0 - np.floor(t * f0 + 0.5))
triangle = 2 * np.abs(sawtooth) - 1
square = np.sign(sine)


def circle_map_staircase(omega_array, K, n_iter=200):
    """Compute devil's staircase: winding number W(Omega) at coupling K."""
    W = np.zeros_like(omega_array)
    for i, omega in enumerate(omega_array):
        theta = 0.0
        for _ in range(n_iter):
            theta = theta + omega - (K / (2 * np.pi)) * np.sin(2 * np.pi * theta)
        W[i] = theta / n_iter
    return W


# Devil's staircase as a waveform: use W(t) where t sweeps [0,1]
# This is the staircase evaluated as a function of time
K_values = [0.3, 0.6, 0.9]
staircases = {}
for K in K_values:
    W = circle_map_staircase(t, K, n_iter=300)
    # Normalize to [-1, 1] for comparison
    W_norm = 2 * (W - W.min()) / (W.max() - W.min() + 1e-15) - 1
    staircases[K] = W_norm


# ============================================================
# Part 2: Fourier transforms
# ============================================================

def spectrum(signal):
    """Return (frequencies, amplitudes) normalized."""
    S = np.abs(np.fft.rfft(signal * np.hanning(len(signal)))) / len(signal)
    freqs = np.fft.rfftfreq(len(signal), d=1.0/N)
    return freqs, S


fig, axes = plt.subplots(4, 2, figsize=(16, 16))

waveforms = [
    ("Sine", sine),
    ("Square", square),
    ("Sawtooth", sawtooth),
    ("Triangle", triangle),
]

for idx, (name, wf) in enumerate(waveforms):
    # Waveform
    ax_w = axes[idx, 0]
    ax_w.plot(t[:N//4], wf[:N//4], "k-", linewidth=0.8)
    ax_w.set_ylabel(name)
    ax_w.set_xlim(0, t[N//4])
    if idx == 0:
        ax_w.set_title("Waveform (1/4 period)")

    # Spectrum
    ax_s = axes[idx, 1]
    f, S = spectrum(wf)
    mask = (f > 0.5) & (f < 30)
    ax_s.semilogy(f[mask], S[mask], "k-", linewidth=0.6)
    ax_s.set_ylabel("|F(f)| (log)")
    if idx == 0:
        ax_s.set_title("Spectrum")

    # Mark integer harmonics
    for n in range(1, 20):
        ax_s.axvline(n, color="blue", alpha=0.15, linewidth=0.5)

    ax_s.set_xlim(0.5, 30)

axes[-1, 0].set_xlabel("Time")
axes[-1, 1].set_xlabel("Frequency (harmonic number)")

plt.tight_layout()
out1 = __import__("pathlib").Path(__file__).parent / "spectrum_classical.png"
plt.savefig(out1, dpi=150)
print(f"Saved: {out1}")
plt.close()


# ============================================================
# Part 3: Devil's staircase spectra at different K
# ============================================================

fig, axes = plt.subplots(len(K_values) + 1, 2, figsize=(16, 4 * (len(K_values) + 1)))

# Stern-Brocot rationals for marking
sb_rationals = []
for q in range(1, 12):
    for p in range(1, q):
        if np.gcd(p, q) == 1:
            sb_rationals.append((p, q, p/q))
# Also overtones
for q in range(1, 6):
    for p in range(q+1, 4*q):
        if np.gcd(p, q) == 1:
            sb_rationals.append((p, q, p/q))

for idx, K in enumerate(K_values):
    wf = staircases[K]

    ax_w = axes[idx, 0]
    ax_w.plot(t[:N//4], wf[:N//4], "k-", linewidth=0.8)
    ax_w.set_ylabel(f"K = {K}")
    ax_w.set_xlim(0, t[N//4])
    if idx == 0:
        ax_w.set_title("Devil's staircase waveform")

    ax_s = axes[idx, 1]
    f, S = spectrum(wf)
    mask = (f > 0.5) & (f < 30)
    ax_s.semilogy(f[mask], S[mask], "k-", linewidth=0.5)

    # Mark rational frequencies by denominator
    colors_q = {1: "red", 2: "C1", 3: "C2", 4: "C3", 5: "C4",
                6: "C5", 7: "C6", 8: "C7", 9: "C8", 10: "C9"}
    for p, q, ratio in sb_rationals:
        if 0.5 < ratio * N < 30 * N:
            c = colors_q.get(q, "gray")
            ax_s.axvline(ratio * f0, color=c, alpha=0.2, linewidth=0.3)

    # Mark key rationals explicitly
    for p, q in [(1,2), (1,3), (2,3), (1,1), (3,2), (2,1), (3,1)]:
        ax_s.axvline(p/q, color="red", alpha=0.4, linewidth=0.8, linestyle="--")

    ax_s.set_ylabel("|F(f)| (log)")
    ax_s.set_xlim(0.5, 15)
    if idx == 0:
        ax_s.set_title("Spectrum (red dashes: Stern-Brocot depth ≤ 3)")

# Compare square wave vs K=0.9 staircase
ax_w = axes[-1, 0]
ax_w.plot(t[:N//4], square[:N//4], "C7-", linewidth=0.8, label="Square")
ax_w.plot(t[:N//4], staircases[0.9][:N//4], "k-", linewidth=0.8, label=f"Staircase K=0.9")
ax_w.legend(fontsize=9)
ax_w.set_xlabel("Time")
ax_w.set_title("Square vs Staircase")
ax_w.set_xlim(0, t[N//4])

ax_s = axes[-1, 1]
f_sq, S_sq = spectrum(square)
f_st, S_st = spectrum(staircases[0.9])
mask = (f_sq > 0.5) & (f_sq < 15)
ax_s.semilogy(f_sq[mask], S_sq[mask], "C7-", linewidth=0.6, alpha=0.6, label="Square")
ax_s.semilogy(f_st[mask], S_st[mask], "k-", linewidth=0.8, label="Staircase K=0.9")
ax_s.legend(fontsize=9)
ax_s.set_xlabel("Frequency")
ax_s.set_title("Square: odd integers 1/n  vs  Staircase: all rationals (K/2)^q")
ax_s.set_xlim(0.5, 15)
# Mark odd integers (square) and rationals (staircase)
for n in [1, 3, 5, 7, 9, 11, 13]:
    ax_s.axvline(n, color="C7", alpha=0.2, linewidth=1)
for p, q in [(1,2), (1,3), (2,3), (2,5), (3,5), (3,4), (4,3), (5,3)]:
    ax_s.axvline(p/q, color="red", alpha=0.3, linewidth=0.8, linestyle="--")

plt.tight_layout()
out2 = __import__("pathlib").Path(__file__).parent / "spectrum_staircase.png"
plt.savefig(out2, dpi=150)
print(f"Saved: {out2}")
plt.close()


# ============================================================
# Part 4: Amplitude vs denominator test
# ============================================================
# At the staircase peaks, does amplitude scale as (K/2)^q?

print("\n=== Amplitude vs denominator at K = 0.9 ===")
f_st, S_st = spectrum(staircases[0.9])

print(f"{'p/q':>6}  {'q':>3}  {'Amplitude':>12}  {'(K/2)^q':>10}  {'Ratio':>8}")
for p, q in [(1,1), (1,2), (1,3), (2,3), (1,4), (2,5), (3,5), (1,5)]:
    ratio = p / q
    # Find peak near this frequency
    idx_near = np.argmin(np.abs(f_st - ratio))
    # Search in a small window
    window = 5
    lo, hi = max(0, idx_near - window), min(len(S_st), idx_near + window)
    amp = np.max(S_st[lo:hi])
    predicted = (0.9 / 2) ** q
    r = amp / predicted if predicted > 0 else 0
    print(f"  {p}/{q}    {q:3d}  {amp:12.4e}  {predicted:10.4e}  {r:8.2f}")


# ============================================================
# Part 5: The gap — where square and staircase differ
# ============================================================

print("\n=== Square vs Staircase: the gap ===")
print("Square wave has power at ODD INTEGERS only: 1, 3, 5, 7, ...")
print("Staircase has power at ALL RATIONALS: 1/3, 1/2, 2/3, 1, 3/2, 2, 5/2, 3, ...")
print()
print("The gap: the square wave has ZERO power at:")
print("  - Even integers (2, 4, 6, ...)")
print("  - ALL non-integer rationals (1/2, 1/3, 2/3, 3/2, 5/3, ...)")
print()
print("The staircase fills these gaps. The 'extra' content is the")
print("rational subharmonics — modes that don't exist in integer-harmonic")
print("waveforms. This is the difference between a periodic signal")
print("(integer harmonics) and a mode-locked signal (rational harmonics).")
print()

# Measure: how much spectral power is at non-integer frequencies?
f_st, S_st = spectrum(staircases[0.9])
f_sq, S_sq = spectrum(square)

# Power at integer frequencies (within ±0.5 of each integer)
int_power_sq = 0
int_power_st = 0
non_int_power_st = 0
total_power_sq = np.sum(S_sq**2)
total_power_st = np.sum(S_st**2)

for n in range(1, 30):
    mask = np.abs(f_st - n) < 0.5
    int_power_st += np.sum(S_st[mask]**2)
    int_power_sq += np.sum(S_sq[mask]**2)

non_int_power_st = total_power_st - int_power_st

print(f"Square:    {int_power_sq/total_power_sq:.1%} at integers, "
      f"{1-int_power_sq/total_power_sq:.1%} elsewhere")
print(f"Staircase: {int_power_st/total_power_st:.1%} at integers, "
      f"{non_int_power_st/total_power_st:.1%} at non-integer rationals")
print(f"\nThe staircase's non-integer content is the mode-locking signature.")
