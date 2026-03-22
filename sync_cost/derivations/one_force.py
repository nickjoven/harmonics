"""
One force, one mechanism: K is both synchronization and decoherence.

The Kuramoto self-consistency equation contains both sides of the
transition in a single coupling parameter K:

    r = K × ∫_{-π/2}^{π/2} cos²(θ) g(Ω + Kr sinθ) dθ

- Locked oscillators (|ω - Ω| < Kr): contribute to r (coherence)
- Drifting oscillators (|ω - Ω| > Kr): average to zero (decoherence)
- K_c = 2/(π g(0)): the internal boundary, not a balance of externals

The "decoherence" is the frequency spread g(ω). It's not a second
force — it's the same force failing to lock oscillators whose
natural frequencies are too far from the mean field.

The power spectrum P(k) comes from the fluctuations of r, which
depend on K/K_c and the shape of g(ω). One parameter (K/K_c)
determines the phase; g(ω) determines the spectral structure.

Usage:
    python sync_cost/derivations/one_force.py
"""

import math

PHI = (1 + math.sqrt(5)) / 2
INV_PHI = 1 / PHI


# ---------------------------------------------------------------------------
# Kuramoto self-consistency for different g(ω)
# ---------------------------------------------------------------------------

def kuramoto_r_lorentzian(K, gamma):
    """
    Exact order parameter for Lorentzian g(ω) = (γ/π)/(ω² + γ²).

    K_c = 2γ.
    r = sqrt(1 - K_c/K) for K > K_c.
    r = 0 for K ≤ K_c.

    Here γ IS the decoherence — the frequency spread.
    K_c = 2γ: coupling must be twice the spread to synchronize.
    """
    K_c = 2 * gamma
    if K <= K_c:
        return 0.0, K_c
    return math.sqrt(1 - K_c / K), K_c


def kuramoto_r_gaussian(K, sigma, n_points=200):
    """
    Numerical order parameter for Gaussian g(ω) = exp(-ω²/2σ²)/(σ√2π).

    K_c = 2/(π g(0)) = 2σ√(2π)/π ≈ 1.596σ.

    Solved by numerical self-consistency iteration.
    """
    g0 = 1.0 / (sigma * math.sqrt(2 * math.pi))
    K_c = 2.0 / (math.pi * g0)

    if K <= K_c:
        return 0.0, K_c

    # Iterate self-consistency: r = F(r)
    r = 0.5  # initial guess
    for _ in range(200):
        # Locked fraction: oscillators with |ω| < K*r
        # r_new = K × ∫_{-Kr}^{Kr} cos(arcsin(ω/(Kr))) × g(ω) × (1/(Kr)) × ...
        # Simplified: r = K × ∫_{-π/2}^{π/2} cos²(θ) g(Kr sinθ) dθ
        integral = 0.0
        d_theta = math.pi / n_points
        for i in range(n_points):
            theta = -math.pi / 2 + (i + 0.5) * d_theta
            omega = K * r * math.sin(theta)
            g_val = math.exp(-omega ** 2 / (2 * sigma ** 2)) / (sigma * math.sqrt(2 * math.pi))
            integral += math.cos(theta) ** 2 * g_val * d_theta

        r_new = K * integral
        r = 0.5 * r + 0.5 * r_new  # damped update

        if abs(r - r_new) < 1e-12:
            break

    return max(r, 0.0), K_c


def locked_fraction(K, r, gamma_or_sigma, dist='lorentzian'):
    """Fraction of oscillators that are phase-locked."""
    if r <= 0 or K <= 0:
        return 0.0
    lock_width = K * r  # oscillators with |ω| < Kr are locked
    if dist == 'lorentzian':
        # CDF of Lorentzian from -Kr to Kr
        return (2 / math.pi) * math.atan(lock_width / gamma_or_sigma)
    else:
        # CDF of Gaussian
        from math import erf
        return erf(lock_width / (gamma_or_sigma * math.sqrt(2)))


# ---------------------------------------------------------------------------
# Fluctuation power from Kuramoto
# ---------------------------------------------------------------------------

def fluctuation_power_kuramoto(K, gamma, epsilon=0.01):
    """
    Fluctuation power of the order parameter.

    Near criticality: χ ~ 1/|K - K_c|  (mean-field susceptibility)
    In locked phase:  P ~ 1/(K*r)²  (phase fluctuations of locked ensemble)

    Unified: P ∝ 1/(K² × (r² + ε²))
    """
    r, K_c = kuramoto_r_lorentzian(K, gamma)
    return 1.0 / (K ** 2 * (r ** 2 + epsilon ** 2))


# ---------------------------------------------------------------------------
# Scale-dependent K_eff from mode-locking (one parameter!)
# ---------------------------------------------------------------------------

def K_eff_from_mode_locking(omega, K_0, n_max=12):
    """
    Effective coupling at frequency ω.

    The key insight: K is ONE parameter, but its EFFECTIVE value
    varies with frequency because mode-locking enhances coupling
    at rational ratios.

    K_eff(ω) = K_0 × (1 + enhancement from nearby rationals)
    """
    enhancement = 0.0
    for q in range(1, n_max + 1):
        for p in range(0, q + 1):
            if math.gcd(p, q) != 1:
                continue
            center = p / q
            # Tongue width ~ K_0^q / q  (Arnold)
            width = K_0 ** q / q
            dist = abs(omega - center)
            if width > 1e-10:
                enhancement += math.exp(-0.5 * (dist / (width * 0.3)) ** 2) / q
    return K_0 * (1 + enhancement)


# ---------------------------------------------------------------------------
# The unified picture: P(ω) from one K and one g
# ---------------------------------------------------------------------------

def unified_spectrum(omega, K_0, gamma, n_max=12, epsilon=0.01):
    """
    P(ω) from the unified Kuramoto picture.

    K_eff(ω) varies with frequency (mode-locking enhancement).
    γ is the frequency spread (same everywhere — it's a property of
    the oscillator ensemble, not the individual frequencies).

    r(ω) is determined by K_eff(ω)/K_c where K_c = 2γ.

    P(ω) ∝ 1/(K_eff² × (r² + ε²))
    """
    K_eff = K_eff_from_mode_locking(omega, K_0, n_max)
    r, K_c = kuramoto_r_lorentzian(K_eff, gamma)
    return 1.0 / (K_eff ** 2 * (r ** 2 + epsilon ** 2))


def tilt_and_running(omega, K_0, gamma, n_max=12, epsilon=0.01):
    """Numerical tilt and running."""
    h = 1e-5
    ln_om = math.log(omega)

    def ln_P(ln_o):
        w = math.exp(ln_o)
        p = unified_spectrum(w, K_0, gamma, n_max, epsilon)
        return math.log(max(p, 1e-30))

    f0 = ln_P(ln_om)
    fp = ln_P(ln_om + h)
    fm = ln_P(ln_om - h)

    tilt = (fp - fm) / (2 * h)
    running = (fp - 2 * f0 + fm) / h ** 2
    return tilt, running


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 80)
    print("  ONE FORCE: K IS BOTH SYNCHRONIZATION AND DECOHERENCE")
    print("=" * 80)

    # --- 0. Show the unification ---
    print(f"\n{'─'*80}")
    print("  0. THE KURAMOTO SELF-CONSISTENCY: ONE K, TWO REGIMES")
    print(f"{'─'*80}")

    gamma = 0.5  # frequency spread
    K_c = 2 * gamma
    print(f"\n  γ (frequency spread) = {gamma}")
    print(f"  K_c = 2γ = {K_c}")
    print(f"\n  {'K':>8s}  {'K/K_c':>8s}  {'r':>8s}  {'locked%':>8s}  {'regime':>15s}")
    print("  " + "-" * 55)

    for K_10 in range(1, 30):
        K = K_10 * 0.1
        r, _ = kuramoto_r_lorentzian(K, gamma)
        frac = locked_fraction(K, r, gamma)
        ratio = K / K_c
        regime = "incoherent" if r == 0 else "partial sync" if frac < 0.9 else "full sync"
        marker = " ← critical" if abs(ratio - 1.0) < 0.06 else ""
        print(f"  {K:8.2f}  {ratio:8.2f}  {r:8.4f}  {frac*100:7.1f}%  {regime:>15s}{marker}")

    # --- 1. K_eff landscape (one parameter generates the structure) ---
    print(f"\n{'─'*80}")
    print("  1. K_eff LANDSCAPE FROM MODE-LOCKING")
    print(f"{'─'*80}")
    print(f"\n  One base coupling K₀. Mode-locking enhancement varies with ω.")

    for K_0 in [0.5, 0.8, 1.0]:
        print(f"\n  K₀ = {K_0}:")
        print(f"  {'ω':>8s}  {'K_eff':>8s}  {'K_eff/K₀':>8s}  {'note':>10s}")
        print("  " + "-" * 40)

        for i in range(21):
            omega = 0.05 + i * 0.045
            K_eff = K_eff_from_mode_locking(omega, K_0)
            note = ""
            if abs(omega - INV_PHI) < 0.01: note = "1/φ"
            elif abs(omega - 0.5) < 0.01: note = "1/2"
            elif abs(omega - 1/3) < 0.015: note = "1/3"
            elif abs(omega - 2/3) < 0.015: note = "2/3"
            elif abs(omega - 3/5) < 0.01: note = "3/5"
            print(f"  {omega:8.3f}  {K_eff:8.4f}  {K_eff/K_0:8.4f}  {note:>10s}")

    # --- 2. The critical crossing: where K_eff(ω) = K_c ---
    print(f"\n{'─'*80}")
    print("  2. CRITICAL CROSSING: K_eff(ω) = K_c = 2γ")
    print(f"{'─'*80}")
    print(f"\n  For a given K₀ and γ, some frequencies are locked (K_eff > K_c)")
    print(f"  and others are unlocked (K_eff < K_c). The BOUNDARY is the critical surface.")

    K_0 = 0.8
    print(f"\n  K₀ = {K_0}")
    print(f"\n  {'γ':>8s}  {'K_c':>8s}  {'locked ω range':>30s}  {'critical ω':>15s}")
    print("  " + "-" * 75)

    for gamma_10 in range(3, 15):
        gamma = gamma_10 * 0.05
        K_c = 2 * gamma

        # Find locked and critical frequencies
        locked = []
        critical_omegas = []
        prev_locked = False
        for i in range(500):
            omega = 0.05 + i * 0.0018
            K_eff = K_eff_from_mode_locking(omega, K_0)
            is_locked = K_eff > K_c
            if is_locked:
                locked.append(omega)
            if is_locked != prev_locked:
                critical_omegas.append(omega)
            prev_locked = is_locked

        if locked:
            locked_range = f"{min(locked):.3f} - {max(locked):.3f}"
        else:
            locked_range = "none"

        crit_str = ", ".join(f"{w:.3f}" for w in critical_omegas[:4])
        if len(critical_omegas) > 4:
            crit_str += "..."

        # Is 1/φ locked or unlocked?
        K_eff_phi = K_eff_from_mode_locking(INV_PHI, K_0)
        phi_state = "locked" if K_eff_phi > K_c else "UNLOCKED"

        print(f"  {gamma:8.2f}  {K_c:8.2f}  {locked_range:>30s}  {crit_str:>15s}  1/φ:{phi_state}")

    # --- 3. Power spectrum from unified picture ---
    print(f"\n{'─'*80}")
    print("  3. POWER SPECTRUM P(ω) — ONE FORCE")
    print(f"{'─'*80}")

    # Find γ that puts K_eff(1/φ) at criticality
    K_eff_phi = K_eff_from_mode_locking(INV_PHI, K_0=0.8)
    gamma_crit_phi = K_eff_phi / 2
    print(f"\n  K_eff(1/φ) = {K_eff_phi:.4f}")
    print(f"  γ for 1/φ critical = {gamma_crit_phi:.4f}")

    for gamma_frac, label in [(0.85, "subcritical"), (0.95, "near-critical"),
                               (1.0, "critical"), (1.05, "supercritical")]:
        gamma = gamma_crit_phi * gamma_frac
        K_c = 2 * gamma
        print(f"\n  γ = {gamma:.4f} ({label} for 1/φ), K_c = {K_c:.4f}:")
        print(f"  {'ω':>8s}  {'K_eff':>8s}  {'r':>8s}  {'P':>12s}  {'n_s-1':>10s}  {'running':>10s}  {'note':>8s}")
        print("  " + "-" * 75)

        for i in range(0, 21):
            omega = 0.05 + i * 0.045
            K_eff = K_eff_from_mode_locking(omega, K_0=0.8)
            r, _ = kuramoto_r_lorentzian(K_eff, gamma)
            P = unified_spectrum(omega, K_0=0.8, gamma=gamma)
            tilt, run = tilt_and_running(omega, K_0=0.8, gamma=gamma)

            note = ""
            if abs(omega - INV_PHI) < 0.01: note = "1/φ"
            elif abs(omega - 0.5) < 0.01: note = "1/2"
            elif abs(omega - 1/3) < 0.015: note = "1/3"
            elif abs(omega - 2/3) < 0.015: note = "2/3"
            elif abs(omega - 3/5) < 0.01: note = "3/5"

            marker = ""
            if run < 0 and -0.06 < tilt < -0.02: marker = " ***"

            print(f"  {omega:8.3f}  {K_eff:8.4f}  {r:8.4f}  {P:12.4f}  "
                  f"{tilt:+10.4f}  {run:+10.4f}  {note:>8s}{marker}")

    # --- 4. γ scan for n_s match ---
    print(f"\n{'─'*80}")
    print("  4. FREQUENCY SPREAD SCAN: WHERE IS n_s = 0.965?")
    print(f"{'─'*80}")

    print(f"\n  Scanning γ. For each γ, check tilt and running at key frequencies.")
    print(f"\n  {'γ':>8s}  {'ω':>8s}  {'n_s':>8s}  {'running':>10s}  {'note':>15s}")
    print("  " + "-" * 60)

    for gamma_100 in range(30, 100):
        gamma = gamma_100 / 100.0
        for omega_test in [INV_PHI, 0.5, 1/3, 2/3, 3/5, 5/8]:
            tilt, run = tilt_and_running(omega_test, K_0=0.8, gamma=gamma)
            ns = 1 + tilt
            if abs(ns - 0.9649) < 0.005:
                note = ""
                if abs(omega_test - INV_PHI) < 0.01: note = "1/φ"
                elif abs(omega_test - 0.5) < 0.01: note = "1/2"
                elif abs(omega_test - 1/3) < 0.02: note = "1/3"
                elif abs(omega_test - 2/3) < 0.02: note = "2/3"
                elif abs(omega_test - 3/5) < 0.01: note = "3/5"
                elif abs(omega_test - 5/8) < 0.01: note = "5/8"
                sign = "NEG!" if run < 0 else ""
                print(f"  {gamma:8.2f}  {omega_test:8.4f}  {ns:8.4f}  {run:+10.4f}  {note:>10s} {sign}")

    # --- 5. The self-consistency constraint ---
    print(f"\n{'─'*80}")
    print("  5. SELF-CONSISTENCY: γ IS NOT FREE")
    print(f"{'─'*80}")
    print(f"""
  In the Kuramoto model, γ (the frequency spread) is an INPUT.
  But in the cosmological setting, the frequency distribution g(ω)
  is SHAPED by the dynamics. The spread γ must be self-consistent
  with the coupling K and the resulting synchronization pattern.

  The self-consistency condition:

    γ_eff = γ_0 × (1 - r²)  +  γ_min × r²

  When r ≈ 0 (incoherent): γ_eff = γ_0 (full natural spread)
  When r ≈ 1 (coherent):    γ_eff = γ_min (locked, narrow)

  This is ONE equation with ONE free parameter (K₀) once we specify
  the oscillator physics. The spectral tilt, running, and all
  observables follow from K₀ alone.
  """)

    # Self-consistent γ iteration
    print(f"  Self-consistent γ for K₀ = 0.8, γ₀ = 1.0, γ_min = 0.01:")
    print(f"\n  {'iter':>6s}  {'γ':>8s}  {'K_c':>8s}  {'r(1/φ)':>8s}  {'K/Kc(1/φ)':>10s}")
    print("  " + "-" * 50)

    gamma = 1.0  # initial spread
    gamma_0 = 1.0
    gamma_min = 0.01
    K_0 = 0.8
    K_eff_phi = K_eff_from_mode_locking(INV_PHI, K_0)

    for it in range(30):
        r, K_c = kuramoto_r_lorentzian(K_eff_phi, gamma)
        gamma_new = gamma_0 * (1 - r ** 2) + gamma_min * r ** 2
        ratio = K_eff_phi / (2 * gamma)

        if it < 10 or it % 5 == 0:
            print(f"  {it:6d}  {gamma:8.4f}  {K_c:8.4f}  {r:8.4f}  {ratio:10.4f}")

        gamma = 0.5 * gamma + 0.5 * gamma_new

    print(f"\n  Fixed point: γ* = {gamma:.6f}")
    print(f"  K_c* = {2*gamma:.6f}")
    print(f"  K_eff(1/φ)/K_c* = {K_eff_phi/(2*gamma):.6f}")
    r_final, _ = kuramoto_r_lorentzian(K_eff_phi, gamma)
    print(f"  r*(1/φ) = {r_final:.6f}")

    # Tilt at fixed point
    tilt, run = tilt_and_running(INV_PHI, K_0=0.8, gamma=gamma)
    print(f"  n_s = {1+tilt:.6f}")
    print(f"  running = {run:+.6f}")

    # --- Summary ---
    print(f"\n{'='*80}")
    print("  THE PICTURE")
    print(f"{'='*80}")
    print(f"""
  ONE force (coupling K).
  ONE distribution (natural frequencies g(ω)).

  K sin(Δθ) synchronizes in-phase pairs and desynchronizes
  out-of-phase pairs. Same mechanism, two regimes.

  The frequency spread γ = width of g(ω) is the "decoherence."
  It's not a separate force — it's the diversity of the oscillators.
  K_c = 2γ is the threshold where coupling overcomes diversity.

  Mode-locking makes K_eff(ω) frequency-dependent: enhanced near
  rationals, with the Fibonacci pile-up near 1/φ.

  The spectral tilt is:
    n_s - 1 = d ln P / d ln ω

  where P(ω) = 1/(K_eff(ω)² × (r(ω)² + ε²)).

  The ONLY free parameter is K₀ (base coupling strength).
  γ is self-consistently determined. Everything else follows
  from the Kuramoto dynamics and the mode-locking structure.

  The spectral tilt encodes K₀/K_c — how far the universe is
  from the synchronization threshold. And K_c itself is set by
  the frequency diversity of the primordial oscillators.
""")
