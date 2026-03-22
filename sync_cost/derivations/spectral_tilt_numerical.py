"""
Numerical companion to Derivation 2: Spectral tilt from synchronization
cost gradient.

Computes the predicted CMB power spectrum, spectral index, and running
from the Michaelis-Menten cost function. Compares to Planck 2018 values.

Usage:
    python sync_cost/derivations/spectral_tilt_numerical.py
"""

import math


def michaelis_menten_cost(tau: float, k_half: float, c_max: float = 1.0) -> float:
    """Synchronization cost after time tau. Saturating decay."""
    return c_max * k_half / (k_half + tau)


def power_spectrum(k: float, tau_0: float, k_half: float) -> float:
    """P(k) ∝ 1/C(τ_sync(k)) where τ_sync = τ_0/k."""
    tau_sync = tau_0 / k
    cost = michaelis_menten_cost(tau_sync, k_half)
    return 1.0 / cost


def spectral_index(k: float, tau_0: float, k_half: float) -> float:
    """n_s = 1 + d ln P / d ln k, computed analytically."""
    x = k_half * k / tau_0  # dimensionless wavenumber
    return 1.0 - 1.0 / (x * x + x)


def running(k: float, tau_0: float, k_half: float) -> float:
    """dn_s/d ln k, computed analytically."""
    x = k_half * k / tau_0
    return (2 * x + 1) / (x * x + x) ** 2


def hill_spectral_index(k: float, tau_0: float, k_half: float, n_hill: float) -> float:
    """
    Generalized Hill-type cost function:
        C(τ) = C_max × K_half^n / (K_half^n + τ^n)

    Gives spectral index:
        n_s - 1 = -n / (x^n + x^(n-1) + ... ) [approximate]

    For n=1: standard Michaelis-Menten.
    For n>1: cooperative synchronization, reduced running.
    """
    x = k_half * k / tau_0
    # Numerically: d ln P / d ln k
    dk = k * 1e-6
    p1 = 1.0 / michaelis_menten_cost_hill(tau_0 / k, k_half, n_hill)
    p2 = 1.0 / michaelis_menten_cost_hill(tau_0 / (k + dk), k_half, n_hill)
    return 1.0 + (math.log(p2) - math.log(p1)) / (math.log(k + dk) - math.log(k))


def michaelis_menten_cost_hill(tau: float, k_half: float, n_hill: float) -> float:
    """Hill-type generalization."""
    return k_half ** n_hill / (k_half ** n_hill + tau ** n_hill)


def running_hill(k: float, tau_0: float, k_half: float, n_hill: float) -> float:
    """Numerical running for Hill-type cost."""
    dk = k * 1e-4
    ns1 = hill_spectral_index(k, tau_0, k_half, n_hill)
    ns2 = hill_spectral_index(k + dk, tau_0, k_half, n_hill)
    return (ns2 - ns1) / (math.log(k + dk) - math.log(k))


if __name__ == "__main__":
    print("=" * 80)
    print("  SPECTRAL TILT FROM SYNCHRONIZATION COST")
    print("=" * 80)

    # --- Fit x_* to observed n_s ---
    # n_s - 1 = -1/(x² + x), solve for x given n_s = 0.9649
    target = 0.0351  # 1 - n_s
    # x² + x = 1/target = 28.49
    # x = (-1 + sqrt(1 + 4/target)) / 2
    x_star = (-1 + math.sqrt(1 + 4 / target)) / 2
    print(f"\n  Observed: n_s = 0.9649 ± 0.0042 (Planck 2018)")
    print(f"  Required: x_* = {x_star:.4f}")
    print(f"  Meaning: pivot scale has synchronized for {x_star:.1f} half-lives")

    # Set parameters: k_half = 1, tau_0 = x_star (so pivot k=1 → x=x_star ... no)
    # Actually: x = k_half * k / tau_0. At pivot k_* we want x = x_star.
    # Set k_half = 1, k_* = 1, so tau_0 = 1/x_star
    k_half = 1.0
    tau_0 = 1.0 / x_star

    print(f"\n  Parameters: K_half = {k_half}, τ_0 = {tau_0:.4f}")

    # --- Power spectrum ---
    print(f"\n{'k/k_*':>8s}  {'P(k)/P_*':>10s}  {'n_s':>8s}  {'dn_s/dlnk':>10s}")
    print("-" * 45)

    k_star = 1.0
    p_star = power_spectrum(k_star, tau_0, k_half)

    for log_k in [-2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0]:
        k = k_star * 10 ** log_k
        p = power_spectrum(k, tau_0, k_half) / p_star
        ns = spectral_index(k, tau_0, k_half)
        run = running(k, tau_0, k_half)
        print(f"{10**log_k:8.3f}  {p:10.4f}  {ns:8.4f}  {run:10.6f}")

    ns_pivot = spectral_index(k_star, tau_0, k_half)
    run_pivot = running(k_star, tau_0, k_half)
    print(f"\n  At pivot: n_s = {ns_pivot:.4f}, dn_s/d ln k = {run_pivot:.6f}")
    print(f"  Planck:   n_s = 0.9649,  dn_s/d ln k = -0.0045 ± 0.0067")

    # --- Hill generalization ---
    print(f"\n{'='*80}")
    print("  HILL GENERALIZATION — cooperative synchronization")
    print(f"{'='*80}")
    print(f"\n  Standard MM (Hill n=1) overestimates running.")
    print(f"  Hill n>1 models cooperative synchronization: modes assist each other.")
    print()
    print(f"{'n_Hill':>7s}  {'n_s':>8s}  {'dn_s/dlnk':>10s}  {'status':>20s}")
    print("-" * 55)

    for n_hill in [1.0, 1.2, 1.5, 2.0, 2.5, 3.0]:
        # Re-fit x_* for each Hill coefficient (numerically)
        # Search for x_* that gives n_s = 0.9649
        best_k = 1.0
        for trial in range(200):
            k_try = 0.1 + trial * 0.05
            ns_try = hill_spectral_index(k_try, tau_0, k_half, n_hill)
            if abs(ns_try - 0.9649) < abs(hill_spectral_index(best_k, tau_0, k_half, n_hill) - 0.9649):
                best_k = k_try

        ns_h = hill_spectral_index(best_k, tau_0, k_half, n_hill)
        run_h = running_hill(best_k, tau_0, k_half, n_hill)

        status = ""
        if abs(run_h - (-0.0045)) < 0.005:
            status = "*** consistent ***"
        elif abs(run_h) > 0.015:
            status = "running too large"
        else:
            status = ""

        print(f"{n_hill:7.1f}  {ns_h:8.4f}  {run_h:10.6f}  {status:>20s}")

    # --- Lattice analogy ---
    print(f"\n{'='*80}")
    print("  LATTICE ANALOGY")
    print(f"{'='*80}")
    print("""
  The Stribeck lattice differential attenuation is the spectral tilt
  mechanism at small scale:

    CMB                          Lattice
    ───                          ───────
    Large scale (small k)   ↔    Subharmonic ω₀ (stick regime)
    Small scale (large k)   ↔    Drive frequency ω_d (slip regime)
    More power at large k   ↔    P(ω₀) > P(ω_d) at RX
    n_s < 1 (red tilt)      ↔    ω₀/ω_d ratio increases with N
    Cost gradient            ↔    Stribeck friction curve

  The lattice ratio P(ω₀)/P(ω_d) ≈ 2.13 at N=8, A=1.0.
  The CMB ratio at k/k_* = 0.01 vs k/k_* = 100:
""")

    p_low = power_spectrum(0.01, tau_0, k_half) / p_star
    p_high = power_spectrum(100.0, tau_0, k_half) / p_star
    print(f"    P(k=0.01 k_*) / P(k=100 k_*) = {p_low/p_high:.2f}")
    print(f"\n  Both show preferential transport of low-frequency modes.")
    print(f"  The cost gradient is the mechanism in both cases.")
