"""
FM-beat / CRT composite chain — Tier-0 simulation.

Tests the modal claim of fm_beat_crt_correspondence_audit.md (PR #252):

  Under the natural cyclic-mode convention ω_n = 2π/n, two phase
  oscillators with carriers at orders (a, b) should produce a coherent
  composite-mode line at ω_{ab} = 2π/(ab) iff |a − b| = 1 (consecutive
  integers).

Pre-test for the Tier-1 benchtop build proposed in f2_scoping.md.

Three runs on identical apparatus:

  Run 1 — POSITIVE CONTROL    (a, b) = (2, 3)
                              Predict coherent line at ω_6  = 2π/6
                              Confirms the harness can resolve the line.

  Run 2 — HEADLINE / CATALAN  (a, b) = (8, 9)
                              Predict coherent line at ω_72 = 2π/72
                              Z_72 is the Catalan composite — NOT YET
                              FRAMEWORK-ENGAGED (audit §3).

  Run 3 — NEGATIVE CONTROL    (a, b) = (3, 5)
                              CRT gives Z_15 algebraically (gcd=1) but
                              |3−5|=2 so the beat identity predicts NO
                              clean line at ω_15. The actual beat lands
                              at |ω_3 − ω_5| = 4π/15. Required to show
                              the consecutive-integer selection is
                              physical, not just arithmetic.

Two parts:

  Part A — K = 0 verification of the audit's bare modal claim.
           Two independent oscillators, composite-mode observable
           cos(φ_a − φ_b), targeted-DFT line search.

  Part B — K-sweep diagnostic.  Substrate_mode_evolution.py couples
           the modes Kuramoto-style with K > 0.  For two oscillators
           with detuning Δω = |ω_a − ω_b|, the locking threshold is
           K_c = Δω/2, and below it the OBSERVED beat shifts from
           Δω to √(Δω² − (2K)²) — a Kuramoto frequency-pulling
           correction the audit's identity does NOT address.  Part B
           sweeps K ∈ [0, K_c) and reports how far the line moves;
           this sets the experimental constraint K << K_c for the
           benchtop FFT to land on the predicted frequency.

Convention and dynamics match substrate_mode_evolution.py: ω_n = 2π/n,
RK4 integration, Kuramoto sin-coupling, pure Python (no numpy/scipy).

Falsifier mapping (audit §6):
  Run 2 null at K=0  →  F-FM-2 falsified in model (Z_72 not realized)
  Run 3 line at ω_15 →  F-FM-1 falsified in model (convention wrong)
  Run 1 null at K=0  →  harness or convention broken at the root
"""

import math


# =========================================================================
# SUBSTRATE CONVENTION  (audit §0 G4)
# =========================================================================

def omega(n):
    return 2.0 * math.pi / n


# =========================================================================
# TWO-MODE KURAMOTO DYNAMICS
# =========================================================================
# Locking threshold for two oscillators is K_c = Δω/2.  At K = 0 the
# oscillators are independent and the composite-mode observable
# cos(φ_a − φ_b) is a pure tone at the audit's predicted line (for
# consecutive pairs) or at the unrelated frequency |ω_a − ω_b| (for
# non-consecutive pairs).  K > 0 introduces frequency pulling.

DT = 0.005


def two_mode_rhs(phases, omega_a, omega_b, K):
    return [
        omega_a + K * math.sin(phases[1] - phases[0]),
        omega_b + K * math.sin(phases[0] - phases[1]),
    ]


def rk4_step(phases, omega_a, omega_b, K, dt):
    def f(y):
        return two_mode_rhs(y, omega_a, omega_b, K)
    k1 = f(phases)
    k2 = f([phases[i] + dt / 2 * k1[i] for i in range(2)])
    k3 = f([phases[i] + dt / 2 * k2[i] for i in range(2)])
    k4 = f([phases[i] + dt       * k3[i] for i in range(2)])
    return [phases[i] + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i])
            for i in range(2)]


def integrate_pair(a, b, K, n_predicted_periods=40, dt=DT):
    omega_a    = omega(a)
    omega_b    = omega(b)
    omega_pred = 2.0 * math.pi / (a * b)
    T          = n_predicted_periods * (2.0 * math.pi / omega_pred)
    n_steps    = int(T / dt)
    phases     = [0.0, 0.0]
    signal     = [0.0] * n_steps
    for k in range(n_steps):
        phases     = rk4_step(phases, omega_a, omega_b, K, dt)
        signal[k]  = math.cos(phases[0] - phases[1])
    return signal


# =========================================================================
# TARGETED DFT — pure-tone amplitude estimator at a chosen ω
# =========================================================================
# For a real signal x(t) = A cos(ω t + φ), this returns A as N → ∞.

def bin_amplitude(signal, dt, omega_target):
    re = 0.0
    im = 0.0
    for k, x in enumerate(signal):
        theta = omega_target * k * dt
        re += x * math.cos(theta)
        im -= x * math.sin(theta)
    T = len(signal) * dt
    return 2.0 * math.hypot(re, im) / T


def line_search(signal, dt, omega_center, half_window_frac=0.30, n_probes=61):
    """Find the dominant amplitude peak in a window around ω_center.

    Returns (omega_peak, amplitude_peak).
    """
    half      = half_window_frac * omega_center
    best_w    = omega_center
    best_amp  = -1.0
    for i in range(n_probes):
        w = omega_center - half + 2.0 * half * i / (n_probes - 1)
        amp = bin_amplitude(signal, dt, w)
        if amp > best_amp:
            best_amp = amp
            best_w   = w
    return best_w, best_amp


def selectivity(signal, dt, omega_target,
                half_window_frac=0.30, n_probes=41, exclusion_bins=3):
    """Amplitude at ω_target ÷ median amplitude in surrounding window."""
    a_target  = bin_amplitude(signal, dt, omega_target)
    half      = half_window_frac * omega_target
    bin_width = 2.0 * math.pi / (len(signal) * dt)
    floor     = []
    for i in range(n_probes):
        off = -half + 2.0 * half * i / (n_probes - 1)
        if abs(off) <= exclusion_bins * bin_width:
            continue
        floor.append(bin_amplitude(signal, dt, omega_target + off))
    floor.sort()
    median = floor[len(floor) // 2] if floor else 0.0
    ratio  = (a_target / median) if median > 0 else float("inf")
    return a_target, median, ratio


# =========================================================================
# PART A — bare audit claim at K = 0
# =========================================================================

VERDICT_THRESHOLD = 10.0


def part_a_run(a, b, label):
    omega_a, omega_b = omega(a), omega(b)
    omega_pred       = 2.0 * math.pi / (a * b)
    omega_beat       = abs(omega_a - omega_b)
    consecutive      = (abs(a - b) == 1)

    signal = integrate_pair(a, b, K=0.0)
    amp_pred, floor_pred, ratio_pred = selectivity(signal, DT, omega_pred)

    if consecutive:
        amp_beat, floor_beat, ratio_beat = amp_pred, floor_pred, ratio_pred
    else:
        amp_beat, floor_beat, ratio_beat = selectivity(signal, DT, omega_beat)

    line_present = ratio_pred >= VERDICT_THRESHOLD
    if consecutive:
        verdict = ("PASS — line at ω_{ab} as audit predicts"
                   if line_present
                   else "FAIL — predicted line absent")
    else:
        beat_present = ratio_beat >= VERDICT_THRESHOLD
        if not line_present and beat_present:
            verdict = "PASS — no line at ω_{ab}; beat lives at |ω_a-ω_b| as audit predicts"
        elif line_present:
            verdict = "FAIL — line at ω_{ab} despite |a-b|≠1"
        else:
            verdict = "FAIL — no line at ω_{ab} AND no line at |ω_a-ω_b| (harness broken)"

    return {
        "label":           label,
        "a":               a,
        "b":               b,
        "consecutive":     consecutive,
        "omega_pred":      omega_pred,
        "omega_beat":      omega_beat,
        "amp_pred":        amp_pred,
        "ratio_pred":      ratio_pred,
        "amp_beat":        amp_beat,
        "ratio_beat":      ratio_beat,
        "verdict":         verdict,
    }


def part_a_print(r):
    print(f"\n--- {r['label']} :  (a, b) = ({r['a']}, {r['b']}) ---")
    print(f"  |a-b| = 1 (consecutive):         {r['consecutive']}")
    print(f"  ω_predicted  = 2π/{r['a']*r['b']:<3d} = {r['omega_pred']:.6f}")
    print(f"  ω_beat       = |ω_a-ω_b|  = {r['omega_beat']:.6f}")
    print(f"  amplitude at ω_predicted  : {r['amp_pred']:.4f}  "
          f"(selectivity ratio {r['ratio_pred']:.1f})")
    if not r["consecutive"]:
        print(f"  amplitude at ω_beat (audit-predicted): "
              f"{r['amp_beat']:.4f}  (selectivity ratio {r['ratio_beat']:.1f})")
    print(f"  VERDICT: {r['verdict']}")


# =========================================================================
# PART B — K-sweep, Kuramoto frequency pulling
# =========================================================================

def part_b_sweep(a, b, k_fractions=(0.0, 0.10, 0.25, 0.50, 0.75, 0.90)):
    """Sweep K as a fraction of K_c = Δω/2 for consecutive pairs.

    Reports observed dominant frequency and the analytical prediction
      ω_obs(K) = √(Δω² − (2K)²)   for two-oscillator Kuramoto, K < K_c.
    """
    omega_a, omega_b = omega(a), omega(b)
    omega_pred       = 2.0 * math.pi / (a * b)
    delta_omega      = abs(omega_a - omega_b)
    K_c              = delta_omega / 2.0

    rows = []
    for kf in k_fractions:
        K       = kf * K_c
        signal  = integrate_pair(a, b, K, n_predicted_periods=30)
        w_peak, amp_peak = line_search(signal, DT, omega_pred)
        if (2.0 * K) < delta_omega:
            w_analytic = math.sqrt(delta_omega ** 2 - (2.0 * K) ** 2)
        else:
            w_analytic = 0.0
        rows.append({
            "k_fraction": kf,
            "K":          K,
            "w_peak":     w_peak,
            "amp_peak":   amp_peak,
            "w_analytic": w_analytic,
            "frac_shift": (omega_pred - w_peak) / omega_pred,
        })
    return {"a": a, "b": b, "omega_pred": omega_pred, "K_c": K_c, "rows": rows}


def part_b_print(sweep):
    a, b = sweep["a"], sweep["b"]
    print(f"\n--- K-sweep for (a, b) = ({a}, {b})  "
          f"(ω_predicted = {sweep['omega_pred']:.6f},  K_c = {sweep['K_c']:.6f}) ---")
    print(f"  {'K/K_c':>7} {'K':>10} {'ω_peak':>10} {'amp_peak':>10} "
          f"{'ω_analytic':>11} {'shift':>9}")
    for r in sweep["rows"]:
        print(f"  {r['k_fraction']:>7.2f} {r['K']:>10.4f} "
              f"{r['w_peak']:>10.6f} {r['amp_peak']:>10.4f} "
              f"{r['w_analytic']:>11.6f} {100*r['frac_shift']:>+8.2f}%")


# =========================================================================
# MAIN
# =========================================================================

CONFIGURATIONS = [
    (2, 3, "Run 1 — POSITIVE CONTROL (Z_6, primitive pair)"),
    (8, 9, "Run 2 — HEADLINE / CATALAN COMPOSITE (Z_72, framework-unengaged)"),
    (3, 5, "Run 3 — NEGATIVE CONTROL (non-consecutive; CRT yes, beat no)"),
]


def main():
    print("=" * 76)
    print("FM-beat / CRT composite chain — Tier-0 simulation")
    print("Tests fm_beat_crt_correspondence_audit.md (PR #252) modal claim:")
    print("  coherent line at ω_{ab} = 2π/(ab)  iff  |a − b| = 1")
    print(f"Convention: ω_n = 2π/n   |   dt = {DT}   |   "
          f"verdict threshold: selectivity > {VERDICT_THRESHOLD:.0f}")
    print("=" * 76)

    print("\n### PART A — bare audit claim at K = 0")
    results = []
    for a, b, label in CONFIGURATIONS:
        r = part_a_run(a, b, label)
        results.append(r)
        part_a_print(r)

    print("\n" + "=" * 76)
    print("PART A SUMMARY")
    print("=" * 76)
    for r in results:
        tag = "PASS" if r["verdict"].startswith("PASS") else "FAIL"
        print(f"  [{tag}] ({r['a']}, {r['b']})  "
              f"ratio@ω_pred = {r['ratio_pred']:>7.1f}   {r['label']}")
    all_pass = all(r["verdict"].startswith("PASS") for r in results)

    print("\n### PART B — K-sweep (Kuramoto frequency pulling) on consecutive pairs")
    for a, b, _ in CONFIGURATIONS:
        if abs(a - b) == 1:
            part_b_print(part_b_sweep(a, b))

    print("\n" + "=" * 76)
    print("VERDICT")
    print("=" * 76)
    if all_pass:
        print("Part A — model agrees with the audit's K=0 modal prediction on all runs.")
        print("Part B — Kuramoto coupling shifts the line; the audit's identity is the")
        print("K→0 statement.  Benchtop constraint: keep coupling K << Δω/2 so the")
        print("predicted line at ω_{ab} = 2π/(ab) lands within FFT bin resolution.")
        print("Tier-1 hardware build is well-motivated.")
    else:
        print("Model disagrees with the audit on at least one Part A run.  Diagnose")
        print("before Tier-1: simulation harness (DT, integration length, signal choice)")
        print("vs the audit's claim itself.")


if __name__ == "__main__":
    main()
