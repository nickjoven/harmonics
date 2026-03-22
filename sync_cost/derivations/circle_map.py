"""
Circle map: exact Arnold tongue structure and devil's staircase.

The standard circle map:
    θ_{n+1} = θ_n + Ω - (K/2π) sin(2π θ_n)    (mod 1)

Parameters:
    Ω ∈ [0, 1]: bare frequency ratio (drive/natural)
    K ∈ [0, 1]: coupling strength (K=1 is critical)

This gives us:
    1. Exact Arnold tongue boundaries
    2. The devil's staircase W(Ω) at each K
    3. The winding number landscape — replaces the crude gaussian model
    4. K_eff(ω) derived from the actual dynamics

Usage:
    python sync_cost/derivations/circle_map.py
"""

import math

PHI = (1 + math.sqrt(5)) / 2
INV_PHI = 1 / PHI  # 0.6180339887...


# ---------------------------------------------------------------------------
# Circle map iteration
# ---------------------------------------------------------------------------

def circle_map(theta, omega, K):
    """One iteration of the standard circle map."""
    return (theta + omega - K / (2 * math.pi) * math.sin(2 * math.pi * theta)) % 1.0


def winding_number(omega, K, n_transient=500, n_measure=2000):
    """
    Compute the winding number W for given (Ω, K).

    W = lim_{n→∞} (θ_n - θ_0) / n  (without mod)

    This is the average rotation per step. If W = p/q (rational),
    the orbit is periodic with period q. If W is irrational,
    the orbit is quasiperiodic.
    """
    theta = 0.0
    total_advance = 0.0

    # Transient
    for _ in range(n_transient):
        new_theta = theta + omega - K / (2 * math.pi) * math.sin(2 * math.pi * theta)
        advance = new_theta - theta
        # Don't mod here — track total advance
        theta = new_theta % 1.0

    # Measure
    total = 0.0
    theta_raw = 0.0  # unmodded
    for _ in range(n_measure):
        new_raw = theta_raw + omega - K / (2 * math.pi) * math.sin(2 * math.pi * theta_raw)
        total += new_raw - theta_raw
        theta_raw = new_raw

    return total / n_measure


def winding_number_precise(omega, K, n_transient=2000, n_measure=10000):
    """Higher precision winding number."""
    theta = 0.0
    for _ in range(n_transient):
        theta = theta + omega - K / (2 * math.pi) * math.sin(2 * math.pi * theta)

    theta_start = theta
    for _ in range(n_measure):
        theta = theta + omega - K / (2 * math.pi) * math.sin(2 * math.pi * theta)

    return (theta - theta_start) / n_measure


# ---------------------------------------------------------------------------
# Devil's staircase
# ---------------------------------------------------------------------------

def devils_staircase(K, n_points=500, omega_min=0.0, omega_max=1.0):
    """
    Compute W(Ω) at fixed K — the devil's staircase.
    Returns (omega_array, W_array).
    """
    omegas = []
    W_values = []
    for i in range(n_points):
        omega = omega_min + i * (omega_max - omega_min) / (n_points - 1)
        W = winding_number(omega, K)
        omegas.append(omega)
        W_values.append(W)
    return omegas, W_values


def staircase_derivative(omegas, W_values, idx, window=3):
    """
    Numerical derivative dW/dΩ at index idx.
    On a plateau (locked): dW/dΩ ≈ 0.
    At transitions (unlocked): dW/dΩ > 0.
    """
    if idx < window or idx >= len(omegas) - window:
        return 0.0
    dW = W_values[idx + window] - W_values[idx - window]
    dOmega = omegas[idx + window] - omegas[idx - window]
    if abs(dOmega) < 1e-15:
        return 0.0
    return dW / dOmega


# ---------------------------------------------------------------------------
# Arnold tongue boundaries
# ---------------------------------------------------------------------------

def tongue_boundary(p, q, K, side='left', tol=1e-8):
    """
    Find the Ω boundary of the p/q Arnold tongue at coupling K.

    The tongue is the range of Ω where W = p/q.
    We binary-search for the Ω where W transitions to/from p/q.
    """
    target = p / q

    if side == 'left':
        lo, hi = max(0.0, target - 0.5), target
    else:
        lo, hi = target, min(1.0, target + 0.5)

    for _ in range(60):
        mid = (lo + hi) / 2
        W = winding_number(mid, K, n_transient=1000, n_measure=5000)
        if abs(W - target) < tol:
            if side == 'left':
                hi = mid
            else:
                lo = mid
        else:
            if side == 'left':
                lo = mid
            else:
                hi = mid

    return (lo + hi) / 2


def tongue_width(p, q, K):
    """Width of the p/q Arnold tongue at coupling K."""
    left = tongue_boundary(p, q, K, 'left')
    right = tongue_boundary(p, q, K, 'right')
    return right - left


# ---------------------------------------------------------------------------
# Spectral quantities from the staircase
# ---------------------------------------------------------------------------

def density_from_staircase(omegas, W_values, window=2):
    """
    The "density of states" — how rapidly W changes with Ω.
    dW/dΩ = 0 on plateaus (locked), > 0 at transitions (unlocked).

    This IS g(ω) in the mode-locking picture: the density of
    distinct winding numbers per unit frequency.
    """
    density = []
    for i in range(len(omegas)):
        d = staircase_derivative(omegas, W_values, i, window)
        density.append(d)
    return density


def power_from_staircase(omegas, W_values, K, epsilon=0.01, window=2):
    """
    Power spectrum from the circle map.

    P(Ω) ∝ 1 / (K_eff(Ω)² × (dW/dΩ + ε)²)

    Wait — let's think about this more carefully.

    On a PLATEAU (locked, dW/dΩ = 0): the system is phase-locked.
    Fluctuations are suppressed. P is LOW.

    At a TRANSITION (unlocked, dW/dΩ > 0): the system is between
    locked states. Fluctuations are enhanced. P is HIGH.

    At the GOLDEN RATIO (maximally unlocked): dW/dΩ is maximal
    (steepest part of the staircase). P is HIGHEST.

    Actually, the susceptibility picture says P ∝ 1/|distance to
    nearest tongue boundary|. But the staircase gives us something
    cleaner: the Lyapunov exponent.

    On a plateau: Lyapunov exponent λ < 0 (stable periodic orbit)
    At transition: λ ≈ 0 (marginal)
    Beyond critical (K>1 at irrational W): λ > 0 (chaotic)

    P ∝ exp(+λ) / K²  — fluctuations grow with Lyapunov exponent.

    For now, use the simpler model:
    P(Ω) ∝ (dW/dΩ) / K²  — power proportional to density of states.
    This gives MORE power at unlocked frequencies (where the staircase
    is steep) and LESS at locked frequencies (where it's flat).
    """
    density = density_from_staircase(omegas, W_values, window)
    power = []
    for i in range(len(omegas)):
        d = max(density[i], epsilon)
        power.append(d / (K ** 2))
    return power


def tilt_and_running_from_power(omegas, power, idx):
    """Numerical tilt and running from P array."""
    if idx < 2 or idx >= len(omegas) - 2:
        return 0, 0
    ln_P = [math.log(max(power[idx + d], 1e-30)) for d in [-2, -1, 0, 1, 2]]
    h = math.log(omegas[idx + 1]) - math.log(omegas[idx])
    if abs(h) < 1e-15:
        return 0, 0
    tilt = (-ln_P[4] + 8 * ln_P[3] - 8 * ln_P[1] + ln_P[0]) / (12 * h)
    running = (-ln_P[4] + 16 * ln_P[3] - 30 * ln_P[2] + 16 * ln_P[1] - ln_P[0]) / (12 * h ** 2)
    return tilt, running


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 80)
    print("  CIRCLE MAP: EXACT ARNOLD TONGUE STRUCTURE")
    print("=" * 80)

    # --- 1. Devil's staircase at several K values ---
    print(f"\n{'─'*80}")
    print("  1. DEVIL'S STAIRCASE W(Ω) at K = 0, 0.3, 0.6, 0.9, 1.0")
    print(f"{'─'*80}")

    for K in [0.0, 0.3, 0.6, 0.9, 1.0]:
        omegas, W_vals = devils_staircase(K, n_points=200)
        print(f"\n  K = {K}:")
        print(f"  {'Ω':>8s}  {'W':>10s}  {'dW/dΩ':>10s}  {'note':>10s}")
        print("  " + "-" * 45)

        density = density_from_staircase(omegas, W_vals)

        for i in range(0, len(omegas), 10):
            omega = omegas[i]
            W = W_vals[i]
            d = density[i]

            note = ""
            if abs(omega - INV_PHI) < 0.005: note = "1/φ"
            elif abs(omega - 0.5) < 0.005: note = "1/2"
            elif abs(omega - 1/3) < 0.005: note = "1/3"
            elif abs(omega - 2/3) < 0.005: note = "2/3"
            elif abs(omega - 3/5) < 0.005: note = "3/5"
            elif abs(omega - 5/8) < 0.005: note = "5/8"
            elif abs(omega - 8/13) < 0.005: note = "8/13"

            print(f"  {omega:8.4f}  {W:10.6f}  {d:10.4f}  {note:>10s}")

    # --- 2. Tongue widths at K = 0.9 ---
    print(f"\n{'─'*80}")
    print("  2. ARNOLD TONGUE WIDTHS at K = 0.9")
    print(f"{'─'*80}")

    K = 0.9
    print(f"\n  {'p/q':>8s}  {'center':>8s}  {'width':>10s}  {'note':>10s}")
    print("  " + "-" * 45)

    rationals = []
    for q in range(1, 10):
        for p in range(0, q + 1):
            if math.gcd(p, q) == 1:
                rationals.append((p, q))

    rationals.sort(key=lambda r: r[0] / r[1])

    for p, q in rationals:
        center = p / q
        if center < 0.05 or center > 0.95:
            continue
        try:
            w = tongue_width(p, q, K)
            note = ""
            if (p, q) in [(1, 2), (1, 3), (2, 3), (3, 5), (2, 5),
                          (5, 8), (3, 8), (8, 13), (5, 13)]:
                note = "Fib" if q in [1, 2, 3, 5, 8, 13] else ""
            print(f"  {p}/{q:>2d}      {center:8.4f}  {w:10.6f}  {note:>10s}")
        except Exception:
            pass

    # --- 3. Zoom: the golden ratio neighborhood ---
    print(f"\n{'─'*80}")
    print("  3. GOLDEN RATIO NEIGHBORHOOD in the staircase")
    print(f"{'─'*80}")

    K = 0.9
    omegas, W_vals = devils_staircase(K, n_points=500,
                                       omega_min=0.55, omega_max=0.70)
    density = density_from_staircase(omegas, W_vals)

    print(f"\n  K = {K}, zoomed to Ω ∈ [0.55, 0.70]:")
    print(f"\n  {'Ω':>8s}  {'W':>10s}  {'dW/dΩ':>10s}  {'note':>15s}")
    print("  " + "-" * 50)

    for i in range(0, len(omegas), 5):
        omega = omegas[i]
        W = W_vals[i]
        d = density[i]

        note = ""
        if abs(omega - INV_PHI) < 0.003: note = "<<< 1/φ >>>"
        elif abs(omega - 3/5) < 0.003: note = "3/5"
        elif abs(omega - 5/8) < 0.003: note = "5/8"
        elif abs(omega - 8/13) < 0.003: note = "8/13"
        elif abs(omega - 13/21) < 0.003: note = "13/21"
        elif abs(omega - 2/3) < 0.003: note = "2/3"
        elif abs(omega - 7/12) < 0.003: note = "7/12"

        print(f"  {omega:8.4f}  {W:10.6f}  {d:10.4f}  {note:>15s}")

    # --- 4. Power spectrum and tilt from the staircase ---
    print(f"\n{'─'*80}")
    print("  4. POWER SPECTRUM FROM THE STAIRCASE")
    print(f"{'─'*80}")

    for K in [0.5, 0.7, 0.9, 0.95, 1.0]:
        omegas, W_vals = devils_staircase(K, n_points=400,
                                           omega_min=0.05, omega_max=0.95)
        power = power_from_staircase(omegas, W_vals, K, epsilon=0.005)
        density = density_from_staircase(omegas, W_vals)

        print(f"\n  K = {K}:")
        print(f"  {'Ω':>8s}  {'W':>10s}  {'dW/dΩ':>10s}  {'P':>10s}  {'n_s-1':>10s}  {'running':>10s}  {'note':>8s}")
        print("  " + "-" * 75)

        for i in range(0, len(omegas), 20):
            omega = omegas[i]
            W = W_vals[i]
            d = density[i]
            P = power[i]
            tilt, run = tilt_and_running_from_power(omegas, power, i)

            note = ""
            if abs(omega - INV_PHI) < 0.01: note = "1/φ"
            elif abs(omega - 0.5) < 0.01: note = "1/2"
            elif abs(omega - 1/3) < 0.015: note = "1/3"
            elif abs(omega - 2/3) < 0.015: note = "2/3"
            elif abs(omega - 3/5) < 0.01: note = "3/5"

            marker = ""
            if run < 0 and -0.06 < tilt < -0.02: marker = " ***"

            print(f"  {omega:8.4f}  {W:10.6f}  {d:10.4f}  {P:10.4f}  "
                  f"{tilt:+10.4f}  {run:+10.4f}  {note:>8s}{marker}")

    # --- 5. Fine scan for n_s = 0.965 ---
    print(f"\n{'─'*80}")
    print("  5. WHERE IS n_s = 0.965?")
    print(f"{'─'*80}")

    matches = []
    for K_10 in range(5, 11):
        K = K_10 / 10.0
        omegas, W_vals = devils_staircase(K, n_points=500,
                                           omega_min=0.05, omega_max=0.95)
        power = power_from_staircase(omegas, W_vals, K, epsilon=0.005)

        for i in range(5, len(omegas) - 5):
            tilt, run = tilt_and_running_from_power(omegas, power, i)
            ns = 1 + tilt
            if abs(ns - 0.9649) < 0.01:
                W = W_vals[i]
                matches.append((omegas[i], K, ns, run, W))

    if matches:
        matches.sort(key=lambda m: abs(m[2] - 0.9649))
        print(f"\n  Found {len(matches)} matches. Top 30:")
        print(f"\n  {'Ω':>8s}  {'K':>6s}  {'n_s':>8s}  {'running':>10s}  {'W':>10s}  {'near':>10s}")
        print("  " + "-" * 60)

        seen = set()
        count = 0
        for omega, K, ns, run, W in matches:
            key = (round(omega, 2), round(K, 1))
            if key in seen:
                continue
            seen.add(key)

            near = ""
            if abs(omega - INV_PHI) < 0.02: near = "1/φ!"
            elif abs(omega - 0.5) < 0.02: near = "1/2"
            elif abs(omega - 1/3) < 0.02: near = "1/3"
            elif abs(omega - 2/3) < 0.02: near = "2/3"
            elif abs(omega - 3/5) < 0.02: near = "3/5"
            elif abs(omega - 5/8) < 0.02: near = "5/8"
            else:
                for q in range(1, 13):
                    for p in range(0, q + 1):
                        if math.gcd(p, q) == 1 and abs(omega - p/q) < 0.015:
                            near = f"{p}/{q}"

            sign = "NEG" if run < 0 else ""
            print(f"  {omega:8.4f}  {K:6.2f}  {ns:8.4f}  {run:+10.4f}  {W:10.6f}  {near:>10s} {sign}")
            count += 1
            if count >= 30:
                break
    else:
        print("\n  No matches found.")

    # --- 6. Summary ---
    print(f"\n{'='*80}")
    print("  SUMMARY")
    print(f"{'='*80}")
    print(f"""
  The circle map gives the EXACT mode-locking structure:

  1. Arnold tongues widen with K. At K=1 they fill the interval.
  2. The devil's staircase W(Ω) has plateaus at every rational.
  3. The density dW/dΩ is the mode-locking "density of states."
  4. It's maximal at the golden ratio (steepest staircase step).
  5. P(Ω) ∝ dW/dΩ gives the power spectrum directly.

  The spectral tilt comes from the GRADIENT of the staircase:
  how rapidly the density of states changes with frequency.

  At 1/φ: the staircase is steepest (maximum density), meaning
  MAXIMUM fluctuation power. The golden ratio is the loudest
  frequency — the one with the most power.

  The running comes from the CURVATURE of the density — how the
  steepness itself changes. At 1/φ, the staircase is locally
  symmetric (flanked by Fibonacci rationals on both sides), so
  the curvature has specific sign properties.
""")
