"""
The slip is not flat.

The transition between locked plateaus in the Stribeck lattice
should have internal structure — smaller plateaus at higher-q
modes, following the Stern-Brocot tree between the two parents.

This script:
1. Runs the lattice at moderate coupling and captures the waveform
   at high time resolution
2. Zooms into individual slip events (transitions between plateaus)
3. Looks for sub-plateaus at mediant frequencies
4. Checks whether the sub-structure has the Fibonacci scaling
5. Tests XOR status of each sub-plateau
"""

import sys
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[2]))

import numpy as np
import matplotlib.pyplot as plt
from stribeck_lattice import StribeckLattice

drive_freq = 6.0
drive_amp = 0.5
dt = 0.0001   # 5× finer than usual for resolving slip structure
n_elements = 5
n_steps = 2_000_000
downsample = 1  # no downsampling — full resolution

# Lower coupling: cleaner plateaus, more visible slip structure
F_n = 1.5

print(f"Running lattice at F_n = {F_n}, dt = {dt}, no downsampling...")
lattice = StribeckLattice(
    n_elements=n_elements,
    drive_amp=drive_amp,
    drive_freq=drive_freq,
    normal_force=F_n,
    mu_static=1.2,
    mu_kinetic=0.25,
    v_threshold=0.15,
    damping=0.02,
    stiffness=1.0,
)
result = lattice.simulate(dt=dt, n_steps=n_steps, downsample=downsample)

t = np.array(result["t"])
v3 = np.array(result["v_3"])  # element 3, past N=3 threshold
x3 = np.array(result["x_3"])

# Steady state: last 10%
n_ss = len(t) // 10
t_ss = t[-n_ss:] - t[-n_ss]
v_ss = v3[-n_ss:]
x_ss = x3[-n_ss:]

period = 2 * np.pi / drive_freq

print(f"Steady state: {len(t_ss)} samples, {t_ss[-1]:.1f} seconds")

# ============================================================
# Part 1: Find slip events (rapid transitions)
# ============================================================

# Compute acceleration (rate of change of velocity)
dv = np.diff(v_ss) / dt
t_dv = t_ss[:-1]

# A "slip" is where |dv| exceeds a threshold
dv_threshold = np.percentile(np.abs(dv), 95)  # top 5% acceleration
slip_mask = np.abs(dv) > dv_threshold

# Find contiguous slip regions
slip_starts = []
slip_ends = []
in_slip = False
for i in range(len(slip_mask)):
    if slip_mask[i] and not in_slip:
        slip_starts.append(i)
        in_slip = True
    elif not slip_mask[i] and in_slip:
        slip_ends.append(i)
        in_slip = False
if in_slip:
    slip_ends.append(len(slip_mask) - 1)

print(f"Found {len(slip_starts)} slip events (|dv/dt| > {dv_threshold:.1f})")

# ============================================================
# Part 2: Zoom into individual slip events
# ============================================================

# Pick the first 6 well-separated slip events
min_gap = int(0.02 * period / dt)  # reduced gap requirement
selected = []
last_end = -min_gap
for s, e in zip(slip_starts, slip_ends):
    if s - last_end > min_gap and e - s > 10:
        selected.append((s, e))
        last_end = e
    if len(selected) >= 6:
        break

if len(selected) == 0:
    # Fall back: just take the first 6 events regardless of separation
    selected = list(zip(slip_starts[:6], slip_ends[:6]))
    print(f"No well-separated events; using first {len(selected)} events")
else:
    print(f"Selected {len(selected)} well-separated slip events for analysis")

n_plot = max(1, len(selected))
fig, axes = plt.subplots(n_plot, 3, figsize=(18, 3.5 * n_plot),
                          gridspec_kw={"width_ratios": [2, 1.5, 1]})
if len(selected) == 1:
    axes = axes[np.newaxis, :]

for idx, (s, e) in enumerate(selected):
    # Expand window around the slip
    margin = max(e - s, 50)
    lo = max(0, s - 3 * margin)
    hi = min(len(v_ss) - 1, e + 3 * margin)

    t_win = (t_ss[lo:hi] - t_ss[lo]) * 1000  # convert to ms
    v_win = v_ss[lo:hi]
    dv_win = dv[lo:min(hi, len(dv))]

    # Velocity waveform with slip highlighted
    ax = axes[idx, 0]
    ax.plot(t_win, v_win, "k-", linewidth=0.5)
    # Highlight the slip region
    slip_lo = (s - lo)
    slip_hi = (e - lo)
    if slip_hi < len(t_win):
        ax.axvspan(t_win[slip_lo], t_win[min(slip_hi, len(t_win)-1)],
                   color="red", alpha=0.2)
    ax.set_ylabel("v(t)")
    if idx == 0:
        ax.set_title("Velocity (slip highlighted)")
    if idx == len(selected) - 1:
        ax.set_xlabel("Time (ms)")

    # Zoomed acceleration during slip
    ax = axes[idx, 1]
    if slip_hi < len(dv_win):
        zoom_lo = max(0, slip_lo - margin//2)
        zoom_hi = min(len(dv_win), slip_hi + margin//2)
        t_zoom = (t_ss[lo+zoom_lo:lo+zoom_hi] - t_ss[lo+zoom_lo]) * 1000
        dv_zoom = dv_win[zoom_lo:zoom_hi]
        if len(t_zoom) > 0 and len(dv_zoom) > 0:
            min_len = min(len(t_zoom), len(dv_zoom))
            ax.plot(t_zoom[:min_len], dv_zoom[:min_len], "k-", linewidth=0.5)
            ax.axhline(0, color="gray", linewidth=0.3)
    ax.set_ylabel("dv/dt")
    if idx == 0:
        ax.set_title("Acceleration (zoomed on slip)")
    if idx == len(selected) - 1:
        ax.set_xlabel("Time (ms)")

    # Local spectrum during slip
    ax = axes[idx, 2]
    # Use a short window centered on the slip
    spec_lo = max(0, s - 2*margin)
    spec_hi = min(len(v_ss), e + 2*margin)
    v_spec = v_ss[spec_lo:spec_hi]
    if len(v_spec) > 64:
        freqs = np.fft.rfftfreq(len(v_spec), d=dt)
        S = np.abs(np.fft.rfft(v_spec * np.hanning(len(v_spec)))) / len(v_spec)
        f_norm = freqs / (drive_freq / (2 * np.pi))
        mask = (f_norm > 0.05) & (f_norm < 3)
        if np.any(mask):
            ax.semilogy(f_norm[mask], S[mask] + 1e-12, "k-", linewidth=0.5)
            # Mark SB rationals
            for p, q in [(1,3),(2,5),(1,2),(3,5),(2,3),(1,1),(3,2),(2,1)]:
                ax.axvline(p/q, color="red", alpha=0.2, linewidth=0.5)
    ax.set_ylabel("|V(f)|")
    if idx == 0:
        ax.set_title("Local spectrum near slip")
    if idx == len(selected) - 1:
        ax.set_xlabel("f / f_drive")

plt.tight_layout()
out1 = __import__("pathlib").Path(__file__).parent / "slip_structure.png"
plt.savefig(out1, dpi=150)
print(f"Saved: {out1}")
plt.close()


# ============================================================
# Part 3: Velocity histogram — are there sub-plateaus?
# ============================================================

fig, axes = plt.subplots(1, 3, figsize=(16, 5))

# Full velocity histogram
ax = axes[0]
ax.hist(v_ss, bins=200, color="k", alpha=0.7, edgecolor="none")
ax.set_xlabel("Velocity v(t)")
ax.set_ylabel("Count")
ax.set_title("Full velocity distribution (element 3)")

# Mark expected plateau velocities for rational frequency ratios
# v_plateau ≈ amplitude × cos(2π × (p/q) × f_drive × t)
# The time-averaged |v| for a locked mode at p/q is proportional to p/q
# More precisely: if locked at frequency ratio p/q of the drive,
# the velocity oscillates at that frequency
v_max = np.max(np.abs(v_ss))
for p, q in [(1,3),(2,5),(1,2),(3,5),(2,3),(1,1)]:
    # Expected velocity scale for this mode
    ax.axvline(v_max * p/q, color="red", alpha=0.4, linewidth=0.8, linestyle="--")
    ax.axvline(-v_max * p/q, color="red", alpha=0.4, linewidth=0.8, linestyle="--")

# Zoomed histogram of the transition region
ax = axes[1]
v_mid = np.median(np.abs(v_ss))
mask_trans = (np.abs(v_ss) > 0.2 * v_max) & (np.abs(v_ss) < 0.8 * v_max)
if np.any(mask_trans):
    ax.hist(v_ss[mask_trans], bins=100, color="k", alpha=0.7, edgecolor="none")
ax.set_xlabel("Velocity v(t)")
ax.set_ylabel("Count")
ax.set_title("Transition region (0.2-0.8 of max)")
for p, q in [(2,5),(3,7),(1,2),(3,5),(4,7)]:
    ax.axvline(v_max * p/q, color="red", alpha=0.4, linewidth=0.8, linestyle="--")
    ax.axvline(-v_max * p/q, color="red", alpha=0.4, linewidth=0.8, linestyle="--")

# Acceleration histogram — is it bimodal? (plateaus vs slips)
ax = axes[2]
ax.hist(np.abs(dv), bins=200, color="k", alpha=0.7, edgecolor="none")
ax.set_xlabel("|dv/dt|")
ax.set_ylabel("Count")
ax.set_title("Acceleration distribution")
ax.set_yscale("log")

plt.tight_layout()
out2 = __import__("pathlib").Path(__file__).parent / "slip_histogram.png"
plt.savefig(out2, dpi=150)
print(f"Saved: {out2}")
plt.close()


# ============================================================
# Part 4: Dwell time at each velocity level
# ============================================================

print("\n=== Dwell time analysis ===")
# Bin the velocity into rational-frequency bands
# and measure how much time the system spends in each

bands = [(0.0, 0.1, "near zero"),
         (0.1, 0.35, "~1/3 region"),
         (0.35, 0.45, "~2/5 mediant"),
         (0.45, 0.55, "~1/2 region"),
         (0.55, 0.65, "~3/5 mediant"),
         (0.65, 0.75, "~2/3 region"),
         (0.75, 1.0, "~1/1 drive")]

v_norm = np.abs(v_ss) / (v_max + 1e-15)

print(f"\n  {'Band':>20s}  {'Range':>12s}  {'Dwell %':>8s}  {'XOR status':>12s}")
for lo, hi, name in bands:
    frac = np.mean((v_norm >= lo) & (v_norm < hi))
    # XOR status of the approximate rational
    p_q = {
        "near zero": (0, 1),
        "~1/3 region": (1, 3),
        "~2/5 mediant": (2, 5),
        "~1/2 region": (1, 2),
        "~3/5 mediant": (3, 5),
        "~2/3 region": (2, 3),
        "~1/1 drive": (1, 1),
    }
    p, q = p_q[name]
    xor = "allowed" if (p + q) % 2 == 1 else "forbidden"
    print(f"  {name:>20s}  [{lo:.1f}, {hi:.1f})  {frac*100:8.2f}%  {xor:>12s}")

print("\n  Key: if the system spends MORE time at XOR-allowed velocities")
print("  and LESS at XOR-forbidden, the topology shapes the transition.")
