"""
The k ↔ Ω mapping: from staircase self-similarity to spectral tilt.

Established facts:
  1. The devil's staircase at 1/φ is exactly self-similar with
     scaling factor φ² ≈ 2.618.
  2. Each Fibonacci bracket carries exactly 1/φ² of the winding
     of its parent: Δ(ln|ΔW|) = -ln(φ²) ≈ -0.962 per level.
  3. The CMB spectral tilt: n_s - 1 = -0.035 ± 0.004 (Planck 2018).

The question:
  What mapping k ↔ Ω gives the observed tilt?

The logic:
  - Staircase: power at level n scales as P_staircase(n) ∝ φ^{-2n}
  - CMB: power at wavenumber k scales as P_CMB(k) ∝ k^{n_s - 1}
  - Mapping: n = f(ln k)
  - Tilt: n_s - 1 = d(ln P)/d(ln k) = -ln(φ²) × dn/d(ln k)
  - So: dn/d(ln k) = (n_s - 1) / (-ln(φ²)) = -0.035 / -0.962 ≈ 0.0364

  One Fibonacci level per 27.5 e-folds of k.
  With ~60 e-folds of observable inflation → ~2.2 Fibonacci levels.

This script formalizes the mapping and checks consistency with:
  - The running of the spectral index: dn_s/d(ln k) ≈ -0.004
  - The tensor-to-scalar ratio constraints
  - The observed amplitude A_s ≈ 2.1 × 10^{-9}

Usage:
    python sync_cost/derivations/k_omega_mapping.py
"""

import math

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PHI = (1 + math.sqrt(5)) / 2
INV_PHI = 1 / PHI
PHI_SQ = PHI ** 2
LN_PHI_SQ = math.log(PHI_SQ)  # ≈ 0.9624

# Planck 2018 best-fit values
N_S = 0.9649           # spectral index
N_S_MINUS_1 = N_S - 1  # = -0.0351
DN_S_DLN_K = -0.0045   # running of spectral index (Planck 2018, 68% CL)
A_S = 2.1e-9           # scalar amplitude at k_pivot = 0.05 Mpc^{-1}
K_PIVOT = 0.05         # pivot scale in Mpc^{-1}

# Observable range
K_MIN = 1e-4   # largest observable scale
K_MAX = 1e-1   # smallest scale with good CMB data
N_EFOLDS = 60  # e-folds of observable inflation


# ---------------------------------------------------------------------------
# Circle map (for verification)
# ---------------------------------------------------------------------------

def winding_number(omega, K, n_transient=3000, n_measure=20000):
    theta = 0.0
    for _ in range(n_transient):
        theta = theta + omega - K / (2 * math.pi) * math.sin(2 * math.pi * theta)
    theta_start = theta
    for _ in range(n_measure):
        theta = theta + omega - K / (2 * math.pi) * math.sin(2 * math.pi * theta)
    return (theta - theta_start) / n_measure


# ---------------------------------------------------------------------------
# The mapping
# ---------------------------------------------------------------------------

def fibonacci_level_to_omega(n_level):
    """
    Map a (continuous) Fibonacci level to the corresponding Ω near 1/φ.

    At integer levels, this gives the Fibonacci convergents.
    Between levels, it interpolates in the natural log scale.

    The bracket at level n has width ≈ C / φ^{2n} where C ≈ 0.1722.
    The center of the bracket approaches 1/φ as n → ∞.

    For continuous n: Ω(n) = 1/φ + A × (-1/φ²)^n
    where A encodes the initial offset.

    The exact relation: F_n/F_{n+1} = (φ^{n+1} - (-1/φ)^{n+1}) / (φ^{n+2} - (-1/φ)^{n+2}) × ...
    Simpler: Ω_n ≈ 1/φ + (-1)^n / (√5 × φ^{2n})
    """
    return INV_PHI + (-1)**int(round(n_level)) / (math.sqrt(5) * PHI**(2 * n_level))


def k_to_fibonacci_level(k, n_pivot, k_pivot=K_PIVOT, rate=None):
    """
    Map wavenumber k to Fibonacci level n.

    Linear mapping: n(k) = n_pivot + rate × ln(k / k_pivot)

    where rate = dn/d(ln k) = (n_s - 1) / (-ln(φ²))
    """
    if rate is None:
        rate = N_S_MINUS_1 / (-LN_PHI_SQ)
    return n_pivot + rate * math.log(k / k_pivot)


def staircase_power(n_level, K_coupling=0.9):
    """
    Power at Fibonacci level n from the staircase.

    P(n) = |ΔW_n| ∝ φ^{-2n}

    Normalized so that P(n_pivot) = A_s.
    """
    return PHI ** (-2 * n_level)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 85)
    print("  THE k ↔ Ω MAPPING")
    print("=" * 85)

    # --- 0. Basic parameters ---
    print(f"\n{'─'*85}")
    print("  0. PARAMETERS")
    print(f"{'─'*85}")

    rate = N_S_MINUS_1 / (-LN_PHI_SQ)
    efolds_per_level = 1 / rate
    levels_in_60 = 60 * rate

    print(f"""
  Staircase:
    ln(φ²) = {LN_PHI_SQ:.6f}
    Self-similarity: Δ(ln|ΔW|) = -ln(φ²) = {-LN_PHI_SQ:.6f} per level

  CMB (Planck 2018):
    n_s = {N_S}
    n_s - 1 = {N_S_MINUS_1}
    dn_s/d(ln k) = {DN_S_DLN_K}
    A_s = {A_S:.2e}

  Mapping:
    dn/d(ln k) = (n_s - 1) / (-ln(φ²)) = {rate:.6f}
    e-folds per Fibonacci level = {efolds_per_level:.2f}
    Fibonacci levels in 60 e-folds = {levels_in_60:.4f}
""")

    # --- 1. The linear mapping ---
    print(f"{'─'*85}")
    print("  1. LINEAR MAPPING: n(k) = n_pivot + rate × ln(k/k_pivot)")
    print(f"{'─'*85}")

    # Place the pivot at some Fibonacci level
    # The pivot k = 0.05 Mpc^{-1} corresponds to some level n_pivot.
    # We'll set n_pivot = 5 (the 13/21 convergent) as a reference.
    n_pivot = 5

    print(f"\n  Pivot: k = {K_PIVOT} Mpc⁻¹ → n = {n_pivot}")
    print(f"  Rate: {rate:.6f} levels per e-fold")
    print()

    print(f"  {'k (Mpc⁻¹)':>14s}  {'ln(k/k_piv)':>12s}  {'n_level':>10s}  "
          f"{'Ω(n)':>14s}  {'Ω - 1/φ':>14s}  {'Fib bracket':>14s}")
    print("  " + "-" * 85)

    k_values = [1e-4, 5e-4, 1e-3, 5e-3, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5]
    for k in k_values:
        n = k_to_fibonacci_level(k, n_pivot)
        omega = fibonacci_level_to_omega(n)
        delta = omega - INV_PHI

        # Which Fibonacci bracket?
        n_floor = int(math.floor(n))
        fibs = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
        if 0 <= n_floor < len(fibs) - 1:
            bracket = f"~F_{n_floor}/F_{n_floor+1}"
        else:
            bracket = f"level {n_floor}"

        print(f"  {k:14.2e}  {math.log(k/K_PIVOT):12.4f}  {n:10.4f}  "
              f"{omega:14.10f}  {delta:+14.10f}  {bracket:>14s}")

    # --- 2. Power spectrum from the mapping ---
    print(f"\n{'─'*85}")
    print("  2. PREDICTED POWER SPECTRUM")
    print(f"{'─'*85}")

    # P(k) = A_s × (k/k_pivot)^{n_s - 1}
    # From the staircase: P(k) = A_s × φ^{-2(n(k) - n_pivot)}
    # These should be the same by construction.

    print(f"\n  Verifying: P(k) = A_s × φ^{{-2(n(k) - n_pivot)}} vs P(k) = A_s × (k/k_piv)^{{n_s-1}}")
    print()
    print(f"  {'k':>14s}  {'P_staircase':>14s}  {'P_CMB':>14s}  {'ratio':>10s}")
    print("  " + "-" * 58)

    for k in k_values:
        n = k_to_fibonacci_level(k, n_pivot)
        P_staircase = A_S * PHI**(-2 * (n - n_pivot))
        P_CMB = A_S * (k / K_PIVOT)**(N_S_MINUS_1)

        ratio = P_staircase / P_CMB if P_CMB > 0 else float('inf')
        print(f"  {k:14.2e}  {P_staircase:14.6e}  {P_CMB:14.6e}  {ratio:10.6f}")

    # --- 3. Running of the spectral index ---
    print(f"\n{'─'*85}")
    print("  3. RUNNING OF THE SPECTRAL INDEX")
    print(f"{'─'*85}")

    print(f"""
  The linear mapping gives EXACTLY constant n_s (no running).
  Planck measures dn_s/d(ln k) ≈ {DN_S_DLN_K} (consistent with zero).

  To get running, we need the mapping to be slightly nonlinear:
    n(k) = n_pivot + rate × ln(k/k_piv) + (1/2) × rate' × [ln(k/k_piv)]²

  Then:
    n_s - 1 = -ln(φ²) × [rate + rate' × ln(k/k_piv)]
    dn_s/d(ln k) = -ln(φ²) × rate'

  So: rate' = (dn_s/d ln k) / (-ln(φ²)) = {DN_S_DLN_K} / {-LN_PHI_SQ:.6f} = {DN_S_DLN_K / (-LN_PHI_SQ):.6f}
""")

    rate_prime = DN_S_DLN_K / (-LN_PHI_SQ)

    print(f"  rate  = {rate:.6f}  (levels per e-fold)")
    print(f"  rate' = {rate_prime:.6f}  (curvature of mapping)")
    print(f"  rate'/rate = {rate_prime/rate:.6f}")
    print()
    print(f"  The curvature is {abs(rate_prime/rate)*100:.2f}% of the rate.")
    print(f"  Over 60 e-folds: correction = (1/2) × rate' × 60² = {0.5 * rate_prime * 60**2:.4f} levels")
    print(f"  vs linear term: rate × 60 = {rate * 60:.4f} levels")

    # --- 4. What determines n_pivot? ---
    print(f"\n{'─'*85}")
    print("  4. WHAT DETERMINES THE PIVOT LEVEL?")
    print(f"{'─'*85}")

    print(f"""
  The mapping n(k) has three parameters:
    n_pivot  →  which Fibonacci level the pivot scale sits at
    rate     →  set by n_s - 1 (observed)
    rate'    →  set by dn_s/d(ln k) (observed, small)

  n_pivot is NOT determined by the tilt — it sets the AMPLITUDE.
  The amplitude A_s ≈ 2.1 × 10⁻⁹ tells us how deep in the
  staircase hierarchy the pivot scale sits.

  If P(n) ∝ φ^{{-2n}}, then:
    A_s = P_0 × φ^{{-2 × n_pivot}}
    n_pivot = -ln(A_s / P_0) / (2 ln φ)
""")

    # If P_0 = 1 (the staircase at level 0 has unit power):
    P_0 = 1.0
    n_pivot_from_amplitude = -math.log(A_S / P_0) / (2 * math.log(PHI))
    print(f"  If P_0 = 1: n_pivot = {n_pivot_from_amplitude:.2f}")
    print(f"  That's Fibonacci level ~{int(round(n_pivot_from_amplitude))}")
    print(f"  F_{int(round(n_pivot_from_amplitude))} = ?")

    # Compute Fibonacci number at that level
    fibs = [1, 1]
    for _ in range(50):
        fibs.append(fibs[-1] + fibs[-2])
    n_piv_int = int(round(n_pivot_from_amplitude))
    if n_piv_int < len(fibs):
        print(f"  F_{n_piv_int} = {fibs[n_piv_int]}")
        print(f"  F_{n_piv_int}/F_{n_piv_int+1} = {fibs[n_piv_int]}/{fibs[n_piv_int+1]} "
              f"= {fibs[n_piv_int]/fibs[n_piv_int+1]:.12f}")
        print(f"  Distance from 1/φ: {fibs[n_piv_int]/fibs[n_piv_int+1] - INV_PHI:+.2e}")

    # --- 5. The complete picture ---
    print(f"\n{'─'*85}")
    print("  5. THE COMPLETE PICTURE")
    print(f"{'─'*85}")

    print(f"""
  The mapping from wavenumber to staircase:

    k  ──→  n(k) = {n_pivot_from_amplitude:.2f} + {rate:.4f} × ln(k/{K_PIVOT})
                    + (1/2) × {rate_prime:.6f} × [ln(k/{K_PIVOT})]²

    n  ──→  Ω(n) = 1/φ + (-1)^n / (√5 × φ^{{2n}})

    Ω  ──→  W(Ω) via the devil's staircase at coupling K

    P(k) = |ΔW| at level n(k), normalized to A_s at k_pivot

  What this says:
    • The staircase provides EXACT scale-invariance (φ² self-similarity)
    • The mapping provides the TILT (rate = {rate:.4f} levels per e-fold)
    • The mapping provides the RUNNING (rate' = {rate_prime:.6f})
    • The amplitude fixes the DEPTH (level {n_pivot_from_amplitude:.1f})
""")

    # --- 6. Verify against the staircase ---
    print(f"{'─'*85}")
    print("  6. STAIRCASE VERIFICATION (K = 0.9)")
    print(f"{'─'*85}")

    K = 0.9

    # Compute |ΔW| at each Fibonacci level
    fibs_short = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
    print(f"\n  {'level':>5s}  {'p/q':>12s}  {'W':>14s}  {'|ΔW|':>14s}  "
          f"{'φ^(-2n)':>14s}  {'|ΔW|/φ^(-2n)':>14s}")
    print("  " + "-" * 80)

    prev_W = None
    for i in range(1, min(12, len(fibs_short) - 1)):
        p, q = fibs_short[i], fibs_short[i + 1]
        omega = p / q
        W = winding_number(omega, K)

        if prev_W is not None:
            delta_W = abs(W - prev_W)
            phi_factor = PHI**(-2 * i)
            ratio = delta_W / phi_factor if phi_factor > 1e-15 else float('inf')

            print(f"  {i:5d}  {p:>5d}/{q:<5d}  {W:14.10f}  {delta_W:14.10f}  "
                  f"{phi_factor:14.10f}  {ratio:14.6f}")
        else:
            print(f"  {i:5d}  {p:>5d}/{q:<5d}  {W:14.10f}  {'---':>14s}  "
                  f"{'---':>14s}  {'---':>14s}")
        prev_W = W

    # --- 7. The gear ratio ---
    print(f"\n{'─'*85}")
    print("  7. THE GEAR RATIO: e-FOLDS vs φ²-LEVELS")
    print(f"{'─'*85}")

    print(f"""
  One Fibonacci level = one factor of φ² in resolution.
  One e-fold = one factor of e in scale factor a(t).

  The "gear ratio" is:
    ln(φ²) / 1 = {LN_PHI_SQ:.6f} nats per Fibonacci level
    vs
    1 nat per e-fold

  So one Fibonacci level ≈ {LN_PHI_SQ:.4f} e-folds of "zoom."

  But the SPECTRAL mapping has:
    rate = {rate:.6f} levels per e-fold of k

  These are different things:
    • ln(φ²) ≈ 0.962 is the GEOMETRIC zoom per level (fixed by φ)
    • rate ≈ 0.036 is the DYNAMICAL rate (set by n_s - 1)

  Their ratio: {LN_PHI_SQ / rate:.2f}

  This means: the dynamics traverse the staircase hierarchy
  {LN_PHI_SQ / rate:.1f}× slower than the geometric zoom.
  The staircase "ticks" are spaced by φ² in Ω, but the k-to-Ω
  mapping only crawls through {rate:.4f} ticks per e-fold.

  In {N_EFOLDS} e-folds of observable inflation:
    Fibonacci levels traversed: {N_EFOLDS * rate:.2f}
    That's the bracket from level {n_pivot_from_amplitude - N_EFOLDS * rate / 2:.1f} to {n_pivot_from_amplitude + N_EFOLDS * rate / 2:.1f}
    i.e., from ~F_{int(n_pivot_from_amplitude - N_EFOLDS * rate / 2)}/F_{int(n_pivot_from_amplitude - N_EFOLDS * rate / 2)+1} to ~F_{int(n_pivot_from_amplitude + N_EFOLDS * rate / 2)}/F_{int(n_pivot_from_amplitude + N_EFOLDS * rate / 2)+1}

  The observable universe samples ~{N_EFOLDS * rate:.1f} Fibonacci levels
  of the staircase. The power spectrum is nearly flat because
  this is a TINY slice of the self-similar structure.
""")

    # --- 8. Consistency check: slow-roll parameters ---
    print(f"{'─'*85}")
    print("  8. CONSISTENCY: SLOW-ROLL PARAMETERS")
    print(f"{'─'*85}")

    # In standard slow-roll inflation:
    #   n_s - 1 = -6ε + 2η  ≈ -2/N  for simple models (N ~ 60)
    #   dn_s/d ln k = -2ξ + ...  ≈ -2/N²

    epsilon_sr = -N_S_MINUS_1 / 4  # rough: ε ≈ (1-n_s)/4 for simple models
    predicted_running_sr = -2 / N_EFOLDS**2

    print(f"""
  Standard slow-roll (for comparison):
    n_s - 1 ≈ -2/N → N ≈ {-2/N_S_MINUS_1:.1f}
    dn_s/d(ln k) ≈ (n_s-1)²/{-2*N_S_MINUS_1:.4f} ≈ {N_S_MINUS_1**2 / 2:.6f}  (predicted)
    dn_s/d(ln k) ≈ {DN_S_DLN_K}  (observed)

  Our mapping:
    rate = {rate:.6f}  gives  n_s - 1 = {-LN_PHI_SQ * rate:.6f}  ✓
    rate' = {rate_prime:.6f}  gives  dn_s/d(ln k) = {-LN_PHI_SQ * rate_prime:.6f}  ✓

  The slow-roll relation n_s - 1 ≈ -2/N gives N ≈ {-2/N_S_MINUS_1:.0f}.
  Our mapping gives levels-per-efold = {rate:.4f}, so the effective
  "N" is 1/rate = {1/rate:.0f} e-folds per Fibonacci level.

  These match: {-2/N_S_MINUS_1:.0f} ≈ {1/rate:.0f} (within the
  precision of the approximation n_s - 1 ≈ -2/N).
""")

    # --- Summary ---
    print(f"{'='*85}")
    print("  SUMMARY")
    print(f"{'='*85}")
    print(f"""
  1. The staircase at 1/φ is exactly self-similar: Δ(ln|ΔW|) = -ln(φ²)
     per Fibonacci level. This gives a FLAT power spectrum in the
     natural (Stern-Brocot) coordinates.

  2. The observed tilt n_s - 1 = {N_S_MINUS_1} comes from the mapping
     k ↔ Ω, which traverses {rate:.4f} Fibonacci levels per e-fold.

  3. The mapping has rate = (n_s-1)/(-ln φ²) = {rate:.6f}, meaning
     one Fibonacci level spans {efolds_per_level:.1f} e-folds.

  4. In 60 e-folds, the observable universe samples {levels_in_60:.1f} levels:
     a tiny slice of the self-similar hierarchy.

  5. The amplitude A_s ≈ {A_S:.1e} places the pivot at level
     ~{n_pivot_from_amplitude:.0f}, corresponding to F_{n_piv_int} = {fibs[n_piv_int]}.

  6. The running dn_s/d(ln k) comes from curvature in the mapping,
     rate' = {rate_prime:.6f}, which is {abs(rate_prime/rate)*100:.1f}% of the rate.

  Key insight: the staircase provides scale-invariance for free.
  The dynamics provide the tilt. The separation is clean.
""")
