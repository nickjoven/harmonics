"""
Amplitude sweep across the stick-slip bifurcation boundary.

Drives a single Stribeck oscillator at frequency ω_d while sweeping
the driving amplitude A. At each amplitude, computes the power spectrum
of the steady-state response and measures energy at:

    ω_d      (fundamental)
    ω_d / 2  (first subharmonic)
    ω_d / 3  (second subharmonic)
    ω_d / 4  (third subharmonic)

The bifurcation threshold is where subharmonic peaks emerge from the
noise floor — the point at which the Stribeck nonlinearity begins
converting high-frequency drive into low-frequency coherent response.

Three experiments:
  1. Single oscillator sweep — subharmonic emergence in driven response
  2. Coupled pair at ω_d = ω₀ — baseline: what happens when drive = resonance
  3. Coupled pair at ω_d = 2ω₀ — key test: subharmonic at ω₀ hits RX resonance

Usage:
    python bifurcation_sweep.py
"""

import math
from driven_stribeck import DrivenStribeckOscillator, CoupledStribeckPair


# ---------------------------------------------------------------------------
# FFT using only the standard library (no numpy dependency)
# ---------------------------------------------------------------------------

def _bit_reverse(x: list) -> list:
    """Bit-reversal permutation for power-of-2 length."""
    n = len(x)
    bits = n.bit_length() - 1
    result = [0.0] * n
    for i in range(n):
        rev = 0
        tmp = i
        for _ in range(bits):
            rev = (rev << 1) | (tmp & 1)
            tmp >>= 1
        result[rev] = x[i]
    return result


def fft(x: list) -> list:
    """
    Radix-2 Cooley-Tukey FFT. Input length must be a power of 2.
    Returns list of complex numbers.
    """
    n = len(x)
    assert n > 0 and (n & (n - 1)) == 0, f"length {n} is not a power of 2"

    xr = _bit_reverse(x)
    out = [complex(v) for v in xr]

    stage = 2
    while stage <= n:
        half = stage // 2
        w_base = -2.0 * math.pi / stage
        for start in range(0, n, stage):
            for k in range(half):
                angle = w_base * k
                w = complex(math.cos(angle), math.sin(angle))
                even = out[start + k]
                odd = out[start + k + half] * w
                out[start + k] = even + odd
                out[start + k + half] = even - odd
        stage *= 2

    return out


def power_spectrum(signal: list, dt: float) -> tuple:
    """
    Compute one-sided power spectrum of a real signal.

    Returns (freqs, power) where freqs is in Hz.
    """
    n_raw = len(signal)
    n = 1
    while n < n_raw:
        n *= 2
    if n > n_raw:
        n //= 2
    sig = signal[:n]

    # Hann window
    windowed = [
        sig[i] * (0.5 - 0.5 * math.cos(2.0 * math.pi * i / (n - 1)))
        for i in range(n)
    ]

    spec = fft(windowed)

    freqs = [k / (n * dt) for k in range(n // 2)]
    power = [(abs(spec[k]) ** 2) / n for k in range(n // 2)]

    return freqs, power


def peak_power(freqs: list, power: list, f_center: float, bandwidth: float) -> float:
    """
    Find peak power near f_center within ±bandwidth/2.
    Uses the maximum bin rather than integral to avoid resolution artifacts.
    Falls back to band integral if no bin is within range.
    """
    f_lo = f_center - bandwidth / 2
    f_hi = f_center + bandwidth / 2
    best = 0.0
    for f, p in zip(freqs, power):
        if f_lo <= f <= f_hi and p > best:
            best = p
    return best


def rms_amplitude(signal: list) -> float:
    """RMS of the latter half of a signal (after transient)."""
    tail = signal[len(signal) // 2:]
    if not tail:
        return 0.0
    return math.sqrt(sum(x ** 2 for x in tail) / len(tail))


def rms_energy(signal: list) -> float:
    """Mean squared amplitude of the latter half (proportional to energy)."""
    tail = signal[len(signal) // 2:]
    if not tail:
        return 0.0
    return sum(x ** 2 for x in tail) / len(tail)


# ---------------------------------------------------------------------------
# Single oscillator: amplitude sweep
# ---------------------------------------------------------------------------

def single_oscillator_sweep():
    """Sweep driving amplitude, measure subharmonic emergence."""
    omega_0 = math.sqrt(1.0)  # natural frequency
    # Drive at 2× natural frequency so ω_d/2 = ω₀
    omega_d = 2.0 * omega_0
    f_d = omega_d / (2.0 * math.pi)
    f_0 = omega_0 / (2.0 * math.pi)

    dt = 0.0005
    downsample = 4       # less downsampling → better frequency resolution
    dt_eff = dt * downsample
    n_steps = 400_000    # longer run for cleaner spectra
    # Bandwidth: at least 3× frequency resolution
    n_fft = 1
    n_steady = (n_steps // downsample) // 2
    while n_fft * 2 <= n_steady:
        n_fft *= 2
    df = 1.0 / (n_fft * dt_eff)
    bw = max(df * 3, f_d * 0.05)

    amplitudes = [
        0.01, 0.02, 0.05, 0.08, 0.10,
        0.12, 0.15, 0.18, 0.20, 0.25,
        0.30, 0.40, 0.50, 0.60, 0.80,
        1.00, 1.50, 2.00, 3.00,
    ]

    print("=" * 100)
    print("  SINGLE OSCILLATOR: Amplitude sweep — drive at ω_d = 2ω₀")
    print("=" * 100)
    print(f"  Drive frequency: ω_d = {omega_d:.3f} rad/s  (f_d = {f_d:.4f} Hz)")
    print(f"  Natural frequency: ω₀ = {omega_0:.3f} rad/s  (f₀ = {f_0:.4f} Hz)")
    print(f"  Subharmonic ω_d/2 = ω₀  ←  this is the key channel")
    print(f"  FFT: N={n_fft}, df={df:.5f} Hz, band={bw:.5f} Hz")
    print(f"  Stribeck: v_thr=0.15, μ_s/μ_k=1.2/0.25, F_n=0.4")
    print()
    print(f"{'A':>7s}  {'RMS':>7s}  {'P(ω_d)':>10s}  {'P(ω₀)':>10s}  {'P(ω/3)':>10s}  {'sub/fund':>9s}  spectrum")
    print("-" * 100)

    results = []

    for A in amplitudes:
        osc = DrivenStribeckOscillator(
            drive_amp=A,
            drive_freq=omega_d,
        )
        sim = osc.simulate(dt=dt, n_steps=n_steps, downsample=downsample)

        n_total = len(sim["x"])
        steady = sim["x"][n_total // 2:]

        freqs, pwr = power_spectrum(steady, dt_eff)

        p_fund = peak_power(freqs, pwr, f_d, bw)          # ω_d (drive)
        p_sub2 = peak_power(freqs, pwr, f_d / 2, bw)      # ω_d/2 = ω₀
        p_sub3 = peak_power(freqs, pwr, f_d / 3, bw)      # ω_d/3
        rms = rms_amplitude(sim["x"])

        ratio = (p_sub2 + p_sub3) / p_fund if p_fund > 1e-30 else 0.0

        # Log-scale bars (dB relative to max)
        all_p = [p_fund, p_sub2, p_sub3]
        max_p = max(max(all_p), 1e-30)

        def bar_db(p, char, width=20):
            if p < 1e-30 or max_p < 1e-30:
                return ""
            db = 10 * math.log10(p / max_p + 1e-30)
            n = max(0, int((db + 60) / 60 * width))  # -60 dB floor
            return char * n

        bar = f"[{bar_db(p_fund, '█'):<20s}|{bar_db(p_sub2, '░'):<20s}|{bar_db(p_sub3, '▒'):<10s}]"

        print(f"{A:7.3f}  {rms:7.4f}  {p_fund:10.2e}  {p_sub2:10.2e}  {p_sub3:10.2e}  {ratio:9.4f}  {bar}")

        results.append({
            "A": A, "rms": rms,
            "p_fund": p_fund, "p_sub2": p_sub2, "p_sub3": p_sub3,
            "ratio": ratio,
        })

    print()
    print("█ = drive frequency (ω_d = 2ω₀)")
    print("░ = first subharmonic (ω_d/2 = ω₀ = natural frequency)")
    print("▒ = second subharmonic (ω_d/3)")
    print()

    # Identify bifurcation threshold
    threshold_A = None
    for i in range(1, len(results)):
        if results[i]["ratio"] > 0.01 and results[i - 1]["ratio"] <= 0.01:
            threshold_A = results[i]["A"]
            break

    if threshold_A is not None:
        print(f"  ⟶  Bifurcation threshold: A ≈ {threshold_A:.3f}")
        print(f"      Below this: response stays at drive frequency.")
        print(f"      Above this: energy cascades into ω₀ subharmonic.")
    else:
        # Check if subharmonics are dominant throughout
        always_sub = all(r["ratio"] > 0.01 for r in results if r["p_fund"] > 1e-30)
        if always_sub:
            print("  ⟶  Subharmonics present across entire sweep range.")
            print("      The natural frequency ω₀ captures energy from ω_d = 2ω₀ at all amplitudes.")
        else:
            print("  ⟶  No clear bifurcation threshold detected in sweep range.")

    print()
    return results


# ---------------------------------------------------------------------------
# Coupled pair: TX → medium → RX with frequency mismatch experiments
# ---------------------------------------------------------------------------

def coupled_pair_experiment(omega_d_factor: float, label: str):
    """
    Sweep amplitude for coupled TX-RX at ω_d = omega_d_factor × ω₀.

    The key test: when omega_d_factor = 2, the subharmonic ω_d/2 = ω₀
    lands on the RX natural frequency. Compare to omega_d_factor = 1
    (baseline) to see if the subharmonic channel is more efficient.
    """
    omega_0 = math.sqrt(1.0)
    omega_d = omega_d_factor * omega_0
    f_d = omega_d / (2.0 * math.pi)
    f_0 = omega_0 / (2.0 * math.pi)

    dt = 0.0005
    downsample = 4
    dt_eff = dt * downsample
    n_steps = 400_000

    n_fft = 1
    n_steady = (n_steps // downsample) // 2
    while n_fft * 2 <= n_steady:
        n_fft *= 2
    df = 1.0 / (n_fft * dt_eff)
    bw = max(df * 3, f_0 * 0.05)

    amplitudes = [0.05, 0.10, 0.15, 0.20, 0.30, 0.50, 0.80, 1.00, 1.50, 2.00, 3.00]

    print("=" * 110)
    print(f"  COUPLED PAIR: {label}")
    print("=" * 110)
    print(f"  TX drive: ω_d = {omega_d_factor:.0f}ω₀ = {omega_d:.3f} rad/s  (f_d = {f_d:.4f} Hz)")
    print(f"  RX natural: ω₀ = {omega_0:.3f} rad/s  (f₀ = {f_0:.4f} Hz)")
    if omega_d_factor > 1:
        print(f"  Subharmonic ω_d/{omega_d_factor:.0f} = ω₀ → should excite RX at resonance")
    print(f"  Medium: mass=0.5, damping=0.05")
    print()
    print(f"{'A':>6s}  {'TX_rms':>7s}  {'RX_rms':>7s}  {'η':>7s}  {'RX@ω₀':>10s}  {'RX@ω_d':>10s}  {'RX E':>10s}  channel")
    print("-" * 110)

    for A in amplitudes:
        pair = CoupledStribeckPair(
            drive_amp=A,
            drive_freq=omega_d,
        )
        sim = pair.simulate(dt=dt, n_steps=n_steps, downsample=downsample)

        tx_rms = rms_amplitude(sim["tx_x"])
        rx_rms = rms_amplitude(sim["rx_x"])
        eta = rx_rms / tx_rms if tx_rms > 1e-30 else 0.0

        n_total = len(sim["rx_x"])
        steady_rx = sim["rx_x"][n_total // 2:]

        freqs, pwr = power_spectrum(steady_rx, dt_eff)

        p_at_f0 = peak_power(freqs, pwr, f_0, bw)     # power at RX natural freq
        p_at_fd = peak_power(freqs, pwr, f_d, bw)      # power at drive freq
        rx_e = rms_energy(sim["rx_x"])

        # Which channel dominates at RX?
        if p_at_f0 > p_at_fd * 10:
            channel = "ω₀ (subharmonic)"
        elif p_at_fd > p_at_f0 * 10:
            channel = "ω_d (fundamental)"
        elif p_at_f0 > p_at_fd:
            channel = "ω₀ > ω_d"
        else:
            channel = "ω_d ≥ ω₀"

        print(f"{A:6.2f}  {tx_rms:7.4f}  {rx_rms:7.4f}  {eta:7.4f}  {p_at_f0:10.2e}  {p_at_fd:10.2e}  {rx_e:10.2e}  {channel}")

    print()


def coupled_comparison():
    """Run the key comparison: drive at ω₀ vs drive at 2ω₀."""
    coupled_pair_experiment(1.0, "Baseline — drive at ω_d = ω₀ (no subharmonic channel)")
    coupled_pair_experiment(2.0, "Test — drive at ω_d = 2ω₀ (subharmonic at ω₀)")
    coupled_pair_experiment(3.0, "Test — drive at ω_d = 3ω₀ (subharmonic at ω₀)")

    print("=" * 110)
    print("  COMPARISON")
    print("=" * 110)
    print("""
  If the ω_d = 2ω₀ or 3ω₀ experiments show:
    • η comparable to or exceeding the ω_d = ω₀ baseline, AND
    • RX spectrum dominated by ω₀ (not ω_d),
  then the frictional medium IS acting as a frequency converter.

  The energy path is: TX(ω_d) → Stribeck bifurcation → ω_d/n → RX(ω₀).
  The medium's nonlinearity is the mechanism. The subharmonic channel
  exploits the stick regime where coupling is strongest.

  If η drops sharply when ω_d ≠ ω₀, the Stribeck nonlinearity in this
  single-element model is insufficient — the frequency conversion requires
  a spatially extended medium (multiple coupled elements) where the
  bifurcation cascade can develop spatially, not just temporally.
""")


# ---------------------------------------------------------------------------
# Stribeck curve visualization
# ---------------------------------------------------------------------------

def stribeck_map():
    """Show the Stribeck friction curve and identify regime boundaries."""
    osc = DrivenStribeckOscillator()
    print("=" * 60)
    print("  STRIBECK FRICTION CURVE — Regime Map")
    print("=" * 60)
    print()
    print(f"{'v_rel':>8s}  {'v/v_thr':>8s}  {'μ_eff':>8s}  {'regime':>12s}  curve")
    print("-" * 60)

    for v_pct in [0.01, 0.03, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0]:
        v_rel = v_pct * osc.v_threshold
        f = osc.stribeck_friction(v_rel)
        mu_eff = f / osc.normal_force

        if v_pct < 0.3:
            regime = "STICK"
        elif v_pct < 1.5:
            regime = "transition"
        else:
            regime = "SLIP"

        bar = "█" * int(mu_eff * 25)
        print(f"{v_rel:8.4f}  {v_pct:8.3f}  {mu_eff:8.4f}  {regime:>12s}  {bar}")

    print()
    print("STICK regime: strong coupling, coherent energy transfer")
    print("SLIP regime: weak coupling, dissipative")
    print("Transition: bifurcation boundary — where subharmonics emerge")
    print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    stribeck_map()
    single_oscillator_sweep()
    coupled_comparison()
