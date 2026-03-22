"""
Two-force model: synchronization vs decoherence.

The missing mechanism: something actively resists coherence. The
steady state is a BALANCE between coupling (K, toward order) and
decoherence (D, toward disorder). The spectral tilt encodes the
equilibrium point.

Three candidate decoherence mechanisms, explored in turn:
  1. Noise (thermal/quantum fluctuations)
  2. Frequency spread (natural drift apart)
  3. Self-consistency barrier (mean field bootstrapping)

The key new ingredient: r(ω) is scale-dependent. Frequencies near
rational ratios lock easily (large r). Frequencies near 1/φ barely
lock (small r → near criticality → large fluctuations).

Usage:
    python sync_cost/derivations/coherence_decoherence.py
"""

import math

PHI = (1 + math.sqrt(5)) / 2
INV_PHI = 1 / PHI


# ---------------------------------------------------------------------------
# 1. Rational approximability as effective coupling
# ---------------------------------------------------------------------------

def rational_approximability(omega, depth=50):
    """
    How well can omega be approximated by rationals?
    Uses continued fraction expansion. Returns a measure where
    SMALL = hard to approximate (like 1/φ), LARGE = easy (like 1/2).

    Specifically: the geometric mean of the continued fraction
    coefficients. For 1/φ = [0; 1, 1, 1, ...] this is 1.
    For most rationals and "easy" irrationals, this is larger.
    """
    # Continued fraction expansion
    coefficients = []
    x = omega
    for _ in range(depth):
        a = int(x)
        coefficients.append(max(a, 1))
        frac = x - a
        if frac < 1e-12:
            break
        x = 1.0 / frac

    if not coefficients:
        return 1.0

    # Geometric mean of coefficients (excluding the integer part)
    cf = coefficients[1:] if len(coefficients) > 1 else coefficients
    if not cf:
        return 10.0  # rational number, very approximable
    log_mean = sum(math.log(c) for c in cf) / len(cf)
    return math.exp(log_mean)


def irrationality_measure(omega, depth=30):
    """
    Approximate irrationality measure via continued fraction.
    1/φ has the smallest possible partial quotients (all 1s).
    Returns a value where SMALLER = more irrational (harder to lock).
    """
    # Use the sum of reciprocals of CF coefficients as a proxy
    # For 1/φ: all 1s → sum = depth (maximum for bounded CFs)
    # For well-approximable numbers: some large coefficients → smaller sum
    coefficients = []
    x = omega
    for _ in range(depth):
        a = int(x)
        coefficients.append(max(a, 1))
        frac = x - a
        if frac < 1e-12:
            break
        x = 1.0 / frac

    cf = coefficients[1:] if len(coefficients) > 1 else [1]
    if not cf:
        return 0.1

    # Mean of 1/a_n — large for 1/φ (all 1s), small for well-approximable
    return sum(1.0 / c for c in cf) / len(cf)


# ---------------------------------------------------------------------------
# 2. Effective coupling K_eff(ω) from Arnold tongue overlap
# ---------------------------------------------------------------------------

def arnold_tongue_coupling(omega, K_base=1.0, n_max=12):
    """
    Effective coupling at frequency omega. Near rational p/q with
    small q, the Arnold tongue is wide → strong effective coupling.
    Near 1/φ, all tongues are narrow → weak effective coupling.
    """
    K_eff = 0.0
    for q in range(1, n_max + 1):
        for p in range(0, q + 1):
            if math.gcd(p, q) != 1:
                continue
            center = p / q
            width = K_base ** q / q  # tongue width
            sigma = width * 0.5
            if sigma < 1e-10:
                continue
            # Contribution: gaussian envelope of the tongue
            dist = abs(omega - center)
            K_eff += (K_base / q) * math.exp(-0.5 * (dist / sigma) ** 2)
    return K_eff


# ---------------------------------------------------------------------------
# 3. Order parameter r(ω) from balance of coupling and decoherence
# ---------------------------------------------------------------------------

def order_parameter(K_eff, D):
    """
    Kuramoto order parameter with noise/decoherence D.
    For Lorentzian g(ω): r = sqrt(1 - 2D/K_eff) when K_eff > K_c = 2D.
    Below critical: r = 0.
    """
    K_c = 2 * D
    if K_eff <= K_c:
        return 0.0
    return math.sqrt(1 - K_c / K_eff)


def susceptibility(K_eff, D):
    """
    Fluctuation susceptibility χ = dR/dK near the transition.
    Diverges at K_c (critical fluctuations).

    χ ∝ 1/|K - K_c| near criticality (mean-field exponent γ = 1).
    In the locked phase: χ ∝ 1/(K - K_c).
    In the unlocked phase: χ ∝ 1/(K_c - K) (finite but large).
    """
    K_c = 2 * D
    delta = abs(K_eff - K_c)
    if delta < 1e-10:
        delta = 1e-10
    return 1.0 / delta


# ---------------------------------------------------------------------------
# 4. Power spectrum from fluctuations
# ---------------------------------------------------------------------------

def fluctuation_power(omega, K_base=1.0, D=0.3, n_max=12):
    """
    P(ω) = fluctuation power at frequency ω.

    In the locked phase (r > 0):
        P ∝ D / (K_eff × r)²  — suppressed by coherence

    Near criticality (r → 0):
        P ∝ χ(K_eff, D)  — critical fluctuations, divergent

    In the unlocked phase (r = 0):
        P ∝ D / K_eff²  — noise-driven, moderate

    We use a unified formula:
        P = D / (K_eff² × (r² + ε²))
    where ε is a small regularizer (quantum/thermal floor).
    """
    K_eff = arnold_tongue_coupling(omega, K_base, n_max)
    if K_eff < 1e-10:
        K_eff = 1e-10

    r = order_parameter(K_eff, D)

    # Regularizer: prevents divergence, represents minimum fluctuation scale
    epsilon = 0.01

    return D / (K_eff ** 2 * (r ** 2 + epsilon ** 2))


def ln_P(omega, K_base=1.0, D=0.3, n_max=12):
    p = fluctuation_power(omega, K_base, D, n_max)
    if p <= 0:
        return -100.0
    return math.log(p)


def tilt_and_running(omega, K_base=1.0, D=0.3, n_max=12):
    """Numerical n_s - 1 and running."""
    h = 1e-5

    ln_om = math.log(omega)
    f0 = ln_P(omega, K_base, D, n_max)
    fp = ln_P(math.exp(ln_om + h), K_base, D, n_max)
    fm = ln_P(math.exp(ln_om - h), K_base, D, n_max)

    tilt = (fp - fm) / (2 * h)
    running = (fp - 2 * f0 + fm) / h ** 2

    return tilt, running


# ---------------------------------------------------------------------------
# Main exploration
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 80)
    print("  COHERENCE vs DECOHERENCE: TWO-FORCE MODEL")
    print("=" * 80)

    # --- 0. The rational approximability landscape ---
    print(f"\n{'─'*80}")
    print("  0. RATIONAL APPROXIMABILITY LANDSCAPE")
    print(f"{'─'*80}")
    print(f"\n  {'ω':>8s}  {'approx':>8s}  {'irr_meas':>8s}  {'K_eff':>8s}  {'note':>15s}")
    print("  " + "-" * 55)

    test_points = [
        (0.5000, "1/2"),
        (0.3333, "1/3"),
        (0.6667, "2/3"),
        (0.6000, "3/5"),
        (0.6250, "5/8"),
        (0.6154, "8/13"),
        (INV_PHI, "1/φ"),
        (0.4142, "√2-1"),
        (0.3183, "1/π"),
        (0.6180, "≈1/φ"),
    ]

    for omega, name in test_points:
        apx = rational_approximability(omega)
        irr = irrationality_measure(omega)
        keff = arnold_tongue_coupling(omega, K_base=0.8, n_max=12)
        print(f"  {omega:8.4f}  {apx:8.3f}  {irr:8.3f}  {keff:8.4f}  {name:>15s}")

    # --- 1. Scan D (decoherence strength) ---
    print(f"\n{'─'*80}")
    print("  1. DECOHERENCE STRENGTH SCAN")
    print(f"{'─'*80}")
    print(f"\n  At ω = 1/φ: how does the balance shift with D?")
    print(f"\n  {'D':>8s}  {'K_eff':>8s}  {'r':>8s}  {'P':>10s}  {'phase':>12s}")
    print("  " + "-" * 55)

    K_eff_phi = arnold_tongue_coupling(INV_PHI, K_base=0.8, n_max=12)
    K_c_phi = K_eff_phi / 2  # critical D

    for D_10 in range(1, 30):
        D = D_10 * 0.02
        r = order_parameter(K_eff_phi, D)
        P = fluctuation_power(INV_PHI, K_base=0.8, D=D, n_max=12)
        phase = "locked" if r > 0.01 else "critical" if abs(K_eff_phi - 2*D) < 0.05 else "unlocked"
        marker = " <<<" if phase == "critical" else ""
        print(f"  {D:8.3f}  {K_eff_phi:8.4f}  {r:8.4f}  {P:10.4f}  {phase:>12s}{marker}")

    print(f"\n  K_eff at 1/φ = {K_eff_phi:.4f}")
    print(f"  Critical D   = {K_c_phi:.4f}")

    # --- 2. Full spectrum: P(ω) across [0.1, 0.9] ---
    print(f"\n{'─'*80}")
    print("  2. FULL SPECTRUM P(ω) — coherence vs decoherence")
    print(f"{'─'*80}")

    # Find D that puts 1/φ near criticality
    D_crit = K_eff_phi / 2
    print(f"\n  Using D = {D_crit:.4f} (critical for 1/φ)")
    print(f"\n  {'ω':>8s}  {'K_eff':>8s}  {'r':>8s}  {'P':>12s}  {'n_s-1':>10s}  {'running':>10s}  {'note':>10s}")
    print("  " + "-" * 80)

    for i in range(81):
        omega = 0.10 + i * 0.01
        K_eff = arnold_tongue_coupling(omega, K_base=0.8, n_max=12)
        r = order_parameter(K_eff, D_crit)
        P = fluctuation_power(omega, K_base=0.8, D=D_crit, n_max=12)
        tilt, run = tilt_and_running(omega, K_base=0.8, D=D_crit, n_max=12)

        note = ""
        if abs(omega - INV_PHI) < 0.005:
            note = "1/φ"
        elif abs(omega - 0.5) < 0.005:
            note = "1/2"
        elif abs(omega - 1/3) < 0.005:
            note = "1/3"
        elif abs(omega - 2/3) < 0.005:
            note = "2/3"
        elif abs(omega - 3/5) < 0.005:
            note = "3/5"
        elif abs(omega - 5/8) < 0.005:
            note = "5/8"

        if i % 5 == 0 or note:
            print(f"  {omega:8.3f}  {K_eff:8.4f}  {r:8.4f}  {P:12.4f}  {tilt:+10.4f}  {run:+10.4f}  {note:>10s}")

    # --- 3. Zoom: golden ratio neighborhood at criticality ---
    print(f"\n{'─'*80}")
    print("  3. GOLDEN RATIO NEIGHBORHOOD AT CRITICALITY")
    print(f"{'─'*80}")
    print(f"\n  D = {D_crit:.4f} (1/φ is exactly critical)")
    print(f"\n  {'ω':>10s}  {'K_eff':>8s}  {'r':>8s}  {'P':>12s}  {'n_s-1':>10s}  {'running':>10s}")
    print("  " + "-" * 70)

    for i in range(61):
        omega = 0.58 + i * 0.002
        K_eff = arnold_tongue_coupling(omega, K_base=0.8, n_max=12)
        r = order_parameter(K_eff, D_crit)
        P = fluctuation_power(omega, K_base=0.8, D=D_crit, n_max=12)
        tilt, run = tilt_and_running(omega, K_base=0.8, D=D_crit, n_max=12)

        note = ""
        if abs(omega - INV_PHI) < 0.002:
            note = " <<< 1/φ"

        marker = ""
        if run < 0 and -0.06 < tilt < -0.02:
            marker = " ***"

        if i % 5 == 0 or note or marker:
            print(f"  {omega:10.4f}  {K_eff:8.4f}  {r:8.4f}  {P:12.4f}  {tilt:+10.4f}  {run:+10.4f}{note}{marker}")

    # --- 4. The phase diagram: K_base vs D ---
    print(f"\n{'─'*80}")
    print("  4. PHASE DIAGRAM AT ω = 1/φ")
    print(f"{'─'*80}")
    print(f"\n  Tilt and running as function of K_base and D")
    print(f"\n  {'K':>6s}  {'D':>6s}  {'K_eff':>8s}  {'r':>6s}  {'n_s-1':>10s}  {'running':>10s}  {'match':>8s}")
    print("  " + "-" * 65)

    for K_base_10 in range(5, 16):
        K_base = K_base_10 / 10.0
        K_eff = arnold_tongue_coupling(INV_PHI, K_base=K_base, n_max=12)
        # Scan D from subcritical to supercritical
        for D_frac in [0.3, 0.45, 0.49, 0.50, 0.51, 0.55, 0.7, 0.9]:
            D = K_eff / 2 * D_frac / 0.5  # D_frac=0.5 → critical
            r = order_parameter(K_eff, D)
            tilt, run = tilt_and_running(INV_PHI, K_base=K_base, D=D, n_max=12)
            ns = 1 + tilt

            match = ""
            if abs(ns - 0.9649) < 0.01 and run < 0:
                match = "<<< !!!"
            elif abs(ns - 0.9649) < 0.02:
                match = "~"

            if match:
                print(f"  {K_base:6.2f}  {D:6.4f}  {K_eff:8.4f}  {r:6.3f}  {tilt:+10.4f}  {run:+10.4f}  {match:>8s}")

    # --- 5. Scan ALL frequencies for n_s match with negative running ---
    print(f"\n{'─'*80}")
    print("  5. GLOBAL SCAN: WHERE IS n_s = 0.965 WITH NEGATIVE RUNNING?")
    print(f"{'─'*80}")

    best_matches = []
    for K_base_10 in range(5, 15):
        K_base = K_base_10 / 10.0
        for D_100 in range(1, 50):
            D = D_100 * 0.01
            for i in range(180):
                omega = 0.05 + i * 0.005
                try:
                    tilt, run = tilt_and_running(omega, K_base=K_base, D=D, n_max=12)
                    ns = 1 + tilt
                    if abs(ns - 0.9649) < 0.005 and run < 0:
                        best_matches.append((omega, K_base, D, ns, run))
                except (ValueError, ZeroDivisionError, OverflowError):
                    pass

    if best_matches:
        # Sort by closeness to n_s = 0.9649
        best_matches.sort(key=lambda m: abs(m[3] - 0.9649))
        print(f"\n  Found {len(best_matches)} matches. Top 20:")
        print(f"\n  {'ω':>8s}  {'K':>6s}  {'D':>6s}  {'n_s':>8s}  {'running':>10s}  {'ω/φ':>8s}  {'near':>10s}")
        print("  " + "-" * 70)

        seen = set()
        count = 0
        for omega, K_base, D, ns, run in best_matches:
            # Deduplicate nearby points
            key = (round(omega, 2), round(K_base, 1), round(D, 2))
            if key in seen:
                continue
            seen.add(key)

            ratio_phi = omega / INV_PHI

            # Nearest simple rational
            near = ""
            for q in range(1, 9):
                for p in range(0, q + 1):
                    if math.gcd(p, q) == 1 and abs(omega - p/q) < 0.01:
                        near = f"{p}/{q}"

            print(f"  {omega:8.4f}  {K_base:6.2f}  {D:6.2f}  {ns:8.4f}  {run:+10.4f}  {ratio_phi:8.4f}  {near:>10s}")
            count += 1
            if count >= 20:
                break
    else:
        print("\n  No matches found in scan range.")

    # --- Summary ---
    print(f"\n{'='*80}")
    print("  INTERPRETATION")
    print(f"{'='*80}")
    print(f"""
  Two competing forces:
    - Synchronization (K): drives toward coherence, mode-locking
    - Decoherence (D): drives toward disorder, phase diffusion

  The effective coupling K_eff(ω) varies with frequency:
    - Near simple rationals (1/2, 1/3): K_eff is large (Arnold tongues)
    - Near 1/φ: K_eff is minimal (maximally irrational, no tongue)

  The order parameter r(ω) = sqrt(1 - 2D/K_eff(ω)):
    - Near rationals: r ≈ 1 (fully locked)
    - Near 1/φ: r ≈ 0 (barely locked or unlocked)

  The fluctuation power P(ω) ∝ D / (K_eff × r)²:
    - Near rationals: P small (coherent, quiet)
    - Near 1/φ: P large (critical fluctuations)

  The spectral tilt comes from the GRADIENT of P(ω) — how
  fluctuation power varies with frequency. The running comes from
  the CURVATURE of this gradient.

  At criticality (D = K_eff/2 at the pivot):
    - The system is exactly at the phase transition
    - Fluctuations are maximal
    - The tilt encodes how the critical surface curves
    - The running sign depends on which side of the transition
      neighboring frequencies sit on
""")
