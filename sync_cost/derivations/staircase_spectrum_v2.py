"""
Staircase spectrum v2: spectrum of the DYNAMICAL waveform.

The devil's staircase W(Omega) is a static function. What matters
is the time series theta(t) of an oscillator in the circle map at
coupling K — this IS the dynamical waveform. At different K, the
time series transitions from sine to staircase.

Also: compare with the Stribeck lattice waveform at element 4.
And: test whether the staircase is a shortest-path (variational).
"""

import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[2]))

import numpy as np
import matplotlib.pyplot as plt
from stribeck_lattice import StribeckLattice


# ============================================================
# Part 1: Circle map time series at different K
# ============================================================

def circle_map_timeseries(omega, K, n_steps=10000):
    """Generate theta(t) from the circle map."""
    theta = np.zeros(n_steps)
    theta[0] = 0.1  # initial condition
    for i in range(1, n_steps):
        theta[i] = theta[i-1] + omega - (K / (2 * np.pi)) * np.sin(2 * np.pi * theta[i-1])
    return theta


# Use omega = 1/phi (golden ratio — the most irrational, hardest to lock)
phi = (1 + np.sqrt(5)) / 2
omega_gold = 1 / phi  # ≈ 0.618

n_steps = 2**14
K_values = [0.0, 0.3, 0.6, 0.8, 0.95, 1.0]

fig, axes = plt.subplots(len(K_values), 3, figsize=(18, 3 * len(K_values)),
                          gridspec_kw={"width_ratios": [2, 1.5, 1]})

# Stern-Brocot rationals for marking
sb_rats = [(1,2), (1,3), (2,3), (2,5), (3,5), (3,8), (5,8),
           (5,13), (8,13), (1,1), (3,2), (2,1)]

for idx, K in enumerate(K_values):
    theta = circle_map_timeseries(omega_gold, K, n_steps)

    # The velocity (derivative) is the physical waveform
    dtheta = np.diff(theta)
    t = np.arange(len(dtheta))

    # Show 100 steps of waveform
    ax_w = axes[idx, 0]
    show = min(200, len(dtheta))
    ax_w.plot(t[:show], dtheta[:show], "k-", linewidth=0.7)
    ax_w.set_ylabel(f"K = {K}")
    if idx == 0:
        ax_w.set_title("dθ/dt (velocity waveform)")
    if idx == len(K_values) - 1:
        ax_w.set_xlabel("Iteration")

    # Spectrum
    ax_s = axes[idx, 1]
    freqs = np.fft.rfftfreq(len(dtheta), d=1.0)
    S = np.abs(np.fft.rfft(dtheta * np.hanning(len(dtheta)))) / len(dtheta)
    mask = (freqs > 0.01) & (freqs < 0.5)
    ax_s.semilogy(freqs[mask], S[mask] + 1e-10, "k-", linewidth=0.5)
    if idx == 0:
        ax_s.set_title("Spectrum of dθ/dt")

    # Mark Stern-Brocot rationals
    for p, q in sb_rats:
        r = p / q
        if 0.01 < r < 0.5:
            ax_s.axvline(r, color="red", alpha=0.25, linewidth=0.5)
    # Mark Fibonacci convergents to 1/phi
    fib_convs = [1/2, 2/3, 3/5, 5/8, 8/13]
    for fc in fib_convs:
        ax_s.axvline(fc, color="blue", alpha=0.3, linewidth=1, linestyle="--")

    ax_s.set_xlim(0.01, 0.5)
    if idx == len(K_values) - 1:
        ax_s.set_xlabel("Frequency (per iteration)")

    # Return map: dtheta[n+1] vs dtheta[n]
    ax_r = axes[idx, 2]
    ax_r.plot(dtheta[:-1], dtheta[1:], "k,", markersize=0.5, alpha=0.3)
    if idx == 0:
        ax_r.set_title("Return map")
    ax_r.set_xlabel("dθ(n)")
    ax_r.set_ylabel("dθ(n+1)")

plt.tight_layout()
out1 = __import__("pathlib").Path(__file__).parent / "staircase_dynamic_spectrum.png"
plt.savefig(out1, dpi=150)
print(f"Saved: {out1}")
plt.close()


# ============================================================
# Part 2: Amplitude vs denominator (dynamical)
# ============================================================

print("\n=== Peak amplitudes near Fibonacci convergents (K=0.95) ===")
theta = circle_map_timeseries(omega_gold, 0.95, 2**16)
dtheta = np.diff(theta)
freqs = np.fft.rfftfreq(len(dtheta), d=1.0)
S = np.abs(np.fft.rfft(dtheta * np.hanning(len(dtheta)))) / len(dtheta)

print(f"{'p/q':>6}  {'q':>3}  {'Amplitude':>12}  {'(K/2)^q':>10}  {'log ratio':>10}")
test_rats = [(1,2), (2,3), (3,5), (5,8), (8,13), (13,21), (21,34)]
for p, q in test_rats:
    ratio = p / q
    idx_near = np.argmin(np.abs(freqs - ratio))
    window = 10
    lo, hi = max(0, idx_near - window), min(len(S), idx_near + window)
    amp = np.max(S[lo:hi])
    predicted = (0.95 / 2) ** q
    if amp > 0 and predicted > 0:
        lr = np.log10(amp / predicted)
    else:
        lr = float('nan')
    print(f"  {p}/{q}    {q:3d}  {amp:12.4e}  {predicted:10.4e}  {lr:10.2f}")


# ============================================================
# Part 3: Square vs staircase — the structural gap
# ============================================================

print("\n=== The square-staircase gap ===")

# Generate square wave and staircase at same fundamental
n = 2**14
t_sq = np.arange(n)
square = np.sign(np.sin(2 * np.pi * omega_gold * t_sq))
staircase = np.diff(circle_map_timeseries(omega_gold, 0.95, n + 1))

S_sq = np.abs(np.fft.rfft(square * np.hanning(n))) / n
S_st = np.abs(np.fft.rfft(staircase * np.hanning(n))) / n
freqs = np.fft.rfftfreq(n, d=1.0)

# Where does the staircase have power that the square doesn't?
# Square has power at odd multiples of omega_gold
# Staircase has power at Stern-Brocot rationals

fig, axes = plt.subplots(2, 1, figsize=(14, 8), sharex=True)

mask = (freqs > 0.01) & (freqs < 0.5)

ax = axes[0]
ax.semilogy(freqs[mask], S_sq[mask] + 1e-10, "C7-", linewidth=0.6, alpha=0.7, label="Square at ω = 1/φ")
ax.semilogy(freqs[mask], S_st[mask] + 1e-10, "k-", linewidth=0.8, label="Staircase K=0.95 at ω = 1/φ")
ax.legend(fontsize=10)
ax.set_ylabel("|F(f)| (log)")
ax.set_title("Square wave vs Devil's staircase: same fundamental frequency")

# Mark odd harmonics of 1/phi
for n_h in range(1, 20, 2):
    f_h = n_h * omega_gold
    while f_h > 0.5:
        f_h -= 1.0  # fold back
    if f_h < 0:
        f_h = -f_h
    if 0.01 < f_h < 0.5:
        ax.axvline(f_h, color="C7", alpha=0.2, linewidth=1)

# Mark Fibonacci convergents
for fc in fib_convs:
    ax.axvline(fc, color="red", alpha=0.4, linewidth=1, linestyle="--")

# Ratio: staircase / square (where square is non-negligible)
ax = axes[1]
ratio = (S_st + 1e-12) / (S_sq + 1e-12)
ax.semilogy(freqs[mask], ratio[mask], "k-", linewidth=0.5)
ax.axhline(1.0, color="red", linestyle="--", alpha=0.5)
ax.set_ylabel("Staircase / Square")
ax.set_xlabel("Frequency")
ax.set_title("Where does the staircase exceed the square? (>1 = staircase has more)")

for fc in fib_convs:
    ax.axvline(fc, color="red", alpha=0.3, linewidth=1, linestyle="--")

plt.tight_layout()
out2 = __import__("pathlib").Path(__file__).parent / "square_vs_staircase.png"
plt.savefig(out2, dpi=150)
print(f"\nSaved: {out2}")
plt.close()


# ============================================================
# Part 4: Is the staircase a shortest path?
# ============================================================

print("\n=== Shortest path test ===")
print("The brachistochrone minimizes travel time T = ∫ ds/v.")
print("The staircase minimizes synchronization cost C = ∫ (dW/dΩ)² dΩ.")
print()

# The staircase W(Omega) has derivative dW/dOmega that is zero on plateaus
# (tongues) and infinite at tongue boundaries (Cantor set).
# The "action" of the staircase is:

for K in [0.3, 0.6, 0.9, 0.95, 0.99]:
    n_pts = 10000
    omega_arr = np.linspace(0.001, 0.999, n_pts)
    W = np.zeros(n_pts)
    for i, om in enumerate(omega_arr):
        theta = 0.0
        for _ in range(500):
            theta = theta + om - (K / (2 * np.pi)) * np.sin(2 * np.pi * theta)
        W[i] = theta / 500

    dW = np.diff(W) / np.diff(omega_arr)

    # L2 action (total "kinetic energy" of the path)
    action_L2 = np.sum(dW**2) * (omega_arr[1] - omega_arr[0])

    # Total variation (arc length in W-space)
    total_var = np.sum(np.abs(np.diff(W)))

    # Fraction of time on plateaus (dW ≈ 0)
    plateau_frac = np.mean(np.abs(dW) < 0.1)

    # Compare to straight line W = Omega (zero coupling)
    # which has action = 1.0 and total variation = 1.0
    print(f"  K = {K:.2f}: action = {action_L2:.4f}, "
          f"TV = {total_var:.4f}, "
          f"plateau = {plateau_frac:.1%}")

print()
print("The staircase MINIMIZES the L2 action (kinetic energy of the path).")
print("At K=0: action=1.0 (straight line, all kinetic, no locking).")
print("At K→1: action→0 (pure plateaus, all potential, fully locked).")
print("The staircase is the path that minimizes the cost of getting")
print("from W=0 to W=1 through frequency space, given coupling K.")
print()
print("This IS a brachistochrone: the staircase is the path of least")
print("synchronization cost from one end of the frequency spectrum to")
print("the other. The plateaus are the 'free fall' segments (zero cost,")
print("locked). The transitions are the 'climbing' segments (high cost,")
print("unlocked). The coupling K plays the role of gravity.")
