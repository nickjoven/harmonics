"""
Stribeck lattice experiments.

Drive element 0 at ω_d = 2ω₀. Measure the spectrum at the far end.
Sweep chain length N to find the critical number of elements where
subharmonic transfer emerges.

Also sweep driving amplitude at fixed N to map the bifurcation
boundary in the spatially extended system.

Usage:
    python lattice_sweep.py
"""

import math
from stribeck_lattice import StribeckLattice
from bifurcation_sweep import fft, power_spectrum, peak_power, rms_amplitude, rms_energy


def lattice_length_sweep():
    """Vary chain length N at fixed drive amplitude."""
    omega_0 = 1.0
    omega_d = 2.0 * omega_0  # drive at 2ω₀ so subharmonic = ω₀
    f_d = omega_d / (2.0 * math.pi)
    f_0 = omega_0 / (2.0 * math.pi)

    dt = 0.0005
    downsample = 4
    dt_eff = dt * downsample
    n_steps = 600_000

    # Frequency resolution for bandwidth
    n_steady = (n_steps // downsample) // 2
    n_fft = 1
    while n_fft * 2 <= n_steady:
        n_fft *= 2
    df = 1.0 / (n_fft * dt_eff)
    bw = max(df * 3, f_0 * 0.05)

    drive_amp = 1.0  # above single-element bifurcation threshold

    print("=" * 110)
    print("  LATTICE LENGTH SWEEP — drive at ω_d = 2ω₀, A = 1.0")
    print("=" * 110)
    print(f"  ω_d = {omega_d:.3f} rad/s, ω₀ = {omega_0:.3f} rad/s")
    print(f"  Subharmonic ω_d/2 = ω₀ should appear at far end if lattice converts")
    print(f"  FFT: df={df:.5f} Hz, band={bw:.5f} Hz")
    print()
    print(f"{'N':>4s}  {'TX_rms':>7s}  {'RX_rms':>7s}  {'η':>7s}  {'RX@ω₀':>10s}  {'RX@ω_d':>10s}  {'ω₀/ω_d':>8s}  dominant")
    print("-" * 100)

    for N in [2, 3, 4, 5, 6, 8, 10, 12, 16]:
        lattice = StribeckLattice(
            n_elements=N,
            drive_amp=drive_amp,
            drive_freq=omega_d,
        )
        sim = lattice.simulate(dt=dt, n_steps=n_steps, downsample=downsample)

        tx_key = "x_0"
        rx_key = f"x_{N - 1}"

        tx_rms = rms_amplitude(sim[tx_key])
        rx_rms = rms_amplitude(sim[rx_key])
        eta = rx_rms / tx_rms if tx_rms > 1e-30 else 0.0

        n_total = len(sim[rx_key])
        steady_rx = sim[rx_key][n_total // 2:]

        freqs, pwr = power_spectrum(steady_rx, dt_eff)

        p_at_f0 = peak_power(freqs, pwr, f_0, bw)
        p_at_fd = peak_power(freqs, pwr, f_d, bw)

        ratio = p_at_f0 / p_at_fd if p_at_fd > 1e-30 else float('inf')

        if p_at_f0 > p_at_fd * 10:
            dominant = "ω₀ SUBHARMONIC"
        elif p_at_fd > p_at_f0 * 10:
            dominant = "ω_d fundamental"
        elif p_at_f0 > p_at_fd:
            dominant = "ω₀ > ω_d"
        else:
            dominant = "ω_d ≥ ω₀"

        print(f"{N:4d}  {tx_rms:7.4f}  {rx_rms:7.4f}  {eta:7.4f}  {p_at_f0:10.2e}  {p_at_fd:10.2e}  {ratio:8.2f}  {dominant}")

    print()


def lattice_amplitude_sweep(N: int = 8):
    """Sweep driving amplitude at fixed chain length."""
    omega_0 = 1.0
    omega_d = 2.0 * omega_0
    f_d = omega_d / (2.0 * math.pi)
    f_0 = omega_0 / (2.0 * math.pi)

    dt = 0.0005
    downsample = 4
    dt_eff = dt * downsample
    n_steps = 600_000

    n_steady = (n_steps // downsample) // 2
    n_fft = 1
    while n_fft * 2 <= n_steady:
        n_fft *= 2
    df = 1.0 / (n_fft * dt_eff)
    bw = max(df * 3, f_0 * 0.05)

    amplitudes = [0.05, 0.10, 0.20, 0.30, 0.50, 0.80, 1.00, 1.50, 2.00, 3.00, 5.00]

    print("=" * 115)
    print(f"  LATTICE AMPLITUDE SWEEP — N={N} elements, ω_d = 2ω₀")
    print("=" * 115)
    print()
    print(f"{'A':>6s}  {'TX_rms':>7s}  {'RX_rms':>7s}  {'η':>7s}  {'RX@ω₀':>10s}  {'RX@ω_d':>10s}  {'RX@ω/3':>10s}  {'ω₀/ω_d':>8s}  spectrum")
    print("-" * 115)

    for A in amplitudes:
        lattice = StribeckLattice(
            n_elements=N,
            drive_amp=A,
            drive_freq=omega_d,
        )
        sim = lattice.simulate(dt=dt, n_steps=n_steps, downsample=downsample)

        tx_rms = rms_amplitude(sim["x_0"])
        rx_rms = rms_amplitude(sim[f"x_{N - 1}"])
        eta = rx_rms / tx_rms if tx_rms > 1e-30 else 0.0

        n_total = len(sim[f"x_{N - 1}"])
        steady_rx = sim[f"x_{N - 1}"][n_total // 2:]

        freqs, pwr = power_spectrum(steady_rx, dt_eff)

        p_f0 = peak_power(freqs, pwr, f_0, bw)
        p_fd = peak_power(freqs, pwr, f_d, bw)
        p_f3 = peak_power(freqs, pwr, f_d / 3, bw)

        ratio = p_f0 / p_fd if p_fd > 1e-30 else float('inf')

        # Log-scale bar
        all_p = [p_fd, p_f0, p_f3]
        max_p = max(max(all_p), 1e-30)

        def bar_db(p, char, width=15):
            if p < 1e-30 or max_p < 1e-30:
                return ""
            db = 10 * math.log10(p / max_p + 1e-30)
            n = max(0, int((db + 60) / 60 * width))
            return char * n

        bar = f"[{bar_db(p_fd, '█'):<15s}|{bar_db(p_f0, '░'):<15s}|{bar_db(p_f3, '▒'):<8s}]"
        print(f"{A:6.2f}  {tx_rms:7.4f}  {rx_rms:7.4f}  {eta:7.4f}  {p_f0:10.2e}  {p_fd:10.2e}  {p_f3:10.2e}  {ratio:8.2f}  {bar}")

    print()
    print("█ = ω_d (drive)    ░ = ω₀ = ω_d/2 (subharmonic)    ▒ = ω_d/3")
    print()


def spatial_spectrum(N: int = 8, A: float = 1.0):
    """Show spectrum at each element along the chain."""
    omega_0 = 1.0
    omega_d = 2.0 * omega_0
    f_d = omega_d / (2.0 * math.pi)
    f_0 = omega_0 / (2.0 * math.pi)

    dt = 0.0005
    downsample = 4
    dt_eff = dt * downsample
    n_steps = 600_000

    n_steady = (n_steps // downsample) // 2
    n_fft = 1
    while n_fft * 2 <= n_steady:
        n_fft *= 2
    df = 1.0 / (n_fft * dt_eff)
    bw = max(df * 3, f_0 * 0.05)

    lattice = StribeckLattice(
        n_elements=N,
        drive_amp=A,
        drive_freq=omega_d,
    )
    sim = lattice.simulate(dt=dt, n_steps=n_steps, downsample=downsample)

    print("=" * 100)
    print(f"  SPATIAL SPECTRUM — N={N}, A={A}, ω_d = 2ω₀")
    print("=" * 100)
    print(f"  How the spectrum evolves along the chain (element 0 = TX, element {N-1} = RX)")
    print()
    print(f"{'elem':>5s}  {'rms':>7s}  {'P@ω_d':>10s}  {'P@ω₀':>10s}  {'P@ω/3':>10s}  {'ω₀/ω_d':>8s}  spectrum along chain")
    print("-" * 100)

    for i in range(N):
        key = f"x_{i}"
        rms = rms_amplitude(sim[key])
        n_total = len(sim[key])
        steady = sim[key][n_total // 2:]

        freqs, pwr = power_spectrum(steady, dt_eff)

        p_fd = peak_power(freqs, pwr, f_d, bw)
        p_f0 = peak_power(freqs, pwr, f_0, bw)
        p_f3 = peak_power(freqs, pwr, f_d / 3, bw)

        ratio = p_f0 / p_fd if p_fd > 1e-30 else float('inf')

        all_p = [p_fd, p_f0, p_f3]
        max_p = max(max(all_p), 1e-30)

        def bar_db(p, char, width=15):
            if p < 1e-30 or max_p < 1e-30:
                return ""
            db = 10 * math.log10(p / max_p + 1e-30)
            n_out = max(0, int((db + 60) / 60 * width))
            return char * n_out

        bar = f"[{bar_db(p_fd, '█'):<15s}|{bar_db(p_f0, '░'):<15s}|{bar_db(p_f3, '▒'):<8s}]"

        label = " (TX)" if i == 0 else (" (RX)" if i == N - 1 else "")
        print(f"{i:5d}{label:>5s}  {rms:7.4f}  {p_fd:10.2e}  {p_f0:10.2e}  {p_f3:10.2e}  {ratio:8.2f}  {bar}")

    print()
    print("█ = ω_d    ░ = ω₀ = ω_d/2    ▒ = ω_d/3")
    print("If ω₀/ω_d ratio increases along the chain, the lattice is converting.")
    print()


if __name__ == "__main__":
    lattice_length_sweep()
    lattice_amplitude_sweep(N=8)
    spatial_spectrum(N=8, A=1.0)
    spatial_spectrum(N=16, A=2.0)

    print("=" * 100)
    print("  INTERPRETATION")
    print("=" * 100)
    print("""
  The lattice experiments test whether a spatially extended Stribeck medium
  converts drive energy into subharmonic channels.

  What to look for:
  1. LENGTH SWEEP: Does ω₀/ω_d ratio increase with N? If so, longer chains
     produce more subharmonic content — the cascade is spatial.

  2. AMPLITUDE SWEEP: Does the subharmonic channel activate above a threshold?
     The single-element model showed bifurcation at A ≈ 0.5. The lattice may
     have a different (possibly lower) threshold.

  3. SPATIAL SPECTRUM: Does the ω_d component attenuate along the chain while
     ω₀ grows or persists? This is direct evidence of frequency conversion:
     high-frequency modes dissipate in the slip regime while subharmonic modes
     propagate in the stick regime.

  The prediction from the synchronization cost framework: the subharmonic
  channel has lower synchronization cost (it sits in the stick regime where
  coupling is strong and coherent). The lattice should preferentially conduct
  energy through this channel once it has enough elements to develop the
  bifurcation cascade spatially.
""")
