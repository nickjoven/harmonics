#!/usr/bin/env python3
"""
a0_observable.py — Observable-only a₀ extraction from RC100

Extracts the MOND acceleration scale a₀ directly from observables,
bypassing the NFW dark-matter decomposition in Nestor Shachar et al. (2023).

Inputs (all from Table B1, all pre-kinematic-model):
  V_circ(R_e)   — circular velocity at effective radius
  R_e           — effective radius (from photometry)
  M_star        — stellar mass (from SED fitting)
  z             — spectroscopic redshift
  δ(log SFR)    — offset from star-forming main sequence

Derived:
  g_obs = V² / R_e                       (observed centripetal acceleration)
  g_bar = G·M_star / R_e²                (baryonic, stars only — floor)
  M_gas via Tacconi+2018 scaling          (independent empirical calibration)
  g_bar_full = G·(M_star + M_gas) / R_e² (baryonic, stars + gas)

Extraction (deep-MOND limit, g_bar << a₀):
  a₀ = g_obs² / g_bar

No NFW halo profile, no f_DM, no model-fit M_baryon.
"""

import numpy as np
from load_rc100 import has_data, load_galaxies, _read_csv

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
G = 6.674e-11       # m³ kg⁻¹ s⁻²
M_sun = 1.989e30    # kg
kpc_m = 3.086e19    # m
c_m_s = 2.998e8     # m/s

# Planck 2018
H0_km_s_Mpc = 67.4
Mpc_in_m = 3.0857e22
H0_si = H0_km_s_Mpc * 1e3 / Mpc_in_m
Omega_m, Omega_L = 0.315, 0.685

a0_local = 1.2e-10  # m/s², observed RAR scale


def H_of_z(z):
    """Hubble parameter H(z) in SI (s⁻¹), flat ΛCDM."""
    return H0_si * np.sqrt(Omega_m * (1 + z)**3 + Omega_L)


def a0_sync(z):
    """Sync-cost prediction: a₀(z) = c·H(z) / (2π)."""
    return c_m_s * H_of_z(z) / (2 * np.pi)


# ---------------------------------------------------------------------------
# Tacconi et al. (2018) molecular gas scaling relation
# ---------------------------------------------------------------------------
def log_mu_gas_tacconi(z, logMs, delta_ms):
    """
    log₁₀(μ_gas) where μ_gas = M_mol_gas / M_star.

    Power-law form from Tacconi et al. (2018, ApJ 853, 179) abstract:
      μ_gas ∝ (1+z)^2.5 × (δMS)^0.52 × (M*/10^10.7)^(−0.36)

    Normalization: μ_gas = 0.05 at z=0, logM*=10.7, on main sequence,
    calibrated to xCOLD GASS (Saintonge et al. 2017).

    Parameters
    ----------
    z : float — redshift
    logMs : float — log₁₀(M_star / M_sun)
    delta_ms : float — δlog(SFR/SFR_MS), offset from main sequence
    """
    return (-1.30
            + 2.5 * np.log10(1 + z)
            + 0.52 * delta_ms
            - 0.36 * (logMs - 10.7))


def M_gas_tacconi(z, logMs, delta_ms):
    """Molecular gas mass in solar masses from Tacconi+2018."""
    log_mu = log_mu_gas_tacconi(z, logMs, delta_ms)
    return 10**logMs * 10**log_mu


# ---------------------------------------------------------------------------
# Core extraction
# ---------------------------------------------------------------------------
def extract_a0(V_kms, Re_kpc, logMs, z, delta_ms, include_gas=True):
    """
    Extract implied a₀ from observables.

    In the deep-MOND regime:  g_obs ≈ √(a₀ · g_bar)
    so:  a₀ = g_obs² / g_bar

    Returns dict with g_obs, g_bar, a0_implied, and diagnostics.
    """
    V = V_kms * 1e3            # m/s
    R = Re_kpc * kpc_m         # m
    M_star = 10**logMs * M_sun  # kg

    g_obs = V**2 / R

    # Baryonic acceleration: stars only
    g_bar_stars = G * M_star / R**2

    # Baryonic acceleration: stars + gas (Tacconi)
    if include_gas:
        M_gas = M_gas_tacconi(z, logMs, delta_ms) * M_sun
        g_bar_full = G * (M_star + M_gas) / R**2
    else:
        M_gas = 0.0
        g_bar_full = g_bar_stars

    # Deep MOND extraction
    a0_stars = g_obs**2 / g_bar_stars
    a0_full = g_obs**2 / g_bar_full

    # Gas fraction implied by Tacconi
    # M_gas_tacconi() returns solar masses; M_star is in kg
    log_mu = log_mu_gas_tacconi(z, logMs, delta_ms) if include_gas else -99
    mu = 10**log_mu  # M_gas / M_star
    f_gas = mu / (1 + mu) if include_gas else 0.0

    return {
        "g_obs": g_obs,
        "g_bar_stars": g_bar_stars,
        "g_bar_full": g_bar_full,
        "a0_stars": a0_stars,
        "a0_full": a0_full,
        "f_gas_tacconi": f_gas,
        "a0_sync": a0_sync(z),
    }


# ---------------------------------------------------------------------------
# Full-sample extraction using McGaugh interpolating function
# ---------------------------------------------------------------------------
def rar_gobs(g_bar, a0):
    """McGaugh+2016 interpolating function (exact, not deep-MOND)."""
    x = np.sqrt(g_bar / a0)
    return g_bar / (1.0 - np.exp(-x))


def extract_a0_rar(V_kms, Re_kpc, logMs, z, delta_ms,
                   include_gas=True, a0_range=(0.5e-10, 20e-10)):
    """
    Extract a₀ by inverting the full RAR (not the deep-MOND approximation).

    Finds a₀ such that rar_gobs(g_bar, a₀) = g_obs.
    """
    from scipy.optimize import brentq

    V = V_kms * 1e3
    R = Re_kpc * kpc_m
    M_star = 10**logMs * M_sun

    g_obs = V**2 / R

    if include_gas:
        M_gas_kg = M_gas_tacconi(z, logMs, delta_ms) * M_sun
        g_bar = G * (M_star + M_gas_kg) / R**2
    else:
        g_bar = G * M_star / R**2

    # If g_obs <= g_bar, no MOND enhancement needed — skip
    if g_obs <= g_bar * 1.01:
        return None

    def residual(log_a0):
        a0 = 10**log_a0
        return rar_gobs(g_bar, a0) - g_obs

    try:
        log_a0 = brentq(residual, np.log10(a0_range[0]), np.log10(a0_range[1]))
        return 10**log_a0
    except ValueError:
        return None


# ---------------------------------------------------------------------------
# Main analysis
# ---------------------------------------------------------------------------
def main():
    raw = _read_csv()
    if not raw:
        print("No data found in rc100_table3.csv")
        return

    # -----------------------------------------------------------------------
    # Part 1: Per-galaxy extraction
    # -----------------------------------------------------------------------
    print("=" * 72)
    print("OBSERVABLE-ONLY a₀ EXTRACTION FROM RC100")
    print("=" * 72)
    print()
    print("Inputs: V_circ(R_e), R_e, M_star, z, δ(SFR) — all pre-model")
    print("Gas:    Tacconi et al. (2018) scaling relation (independent)")
    print("Method: deep-MOND a₀ = g_obs² / g_bar")
    print()

    results = []
    for r in raw:
        z = r["z"]
        logMs = r["log_Mstar"]
        Re = r["Re_kpc"]
        Vc = r["Vc_kms"]
        delta_ms = r["delta_log_SFR"]
        galaxy = r.get("Galaxy", "")

        ext = extract_a0(Vc, Re, logMs, z, delta_ms, include_gas=True)
        ext_stars = extract_a0(Vc, Re, logMs, z, delta_ms, include_gas=False)

        # Full RAR inversion
        a0_rar_full = extract_a0_rar(Vc, Re, logMs, z, delta_ms, include_gas=True)
        a0_rar_stars = extract_a0_rar(Vc, Re, logMs, z, delta_ms, include_gas=False)

        results.append({
            "galaxy": galaxy, "z": z, "logMs": logMs,
            "Re": Re, "Vc": Vc, "delta_ms": delta_ms,
            "g_obs": ext["g_obs"],
            "g_bar_stars": ext["g_bar_stars"],
            "g_bar_full": ext["g_bar_full"],
            "a0_deep_stars": ext["a0_stars"],
            "a0_deep_full": ext["a0_full"],
            "a0_rar_stars": a0_rar_stars,
            "a0_rar_full": a0_rar_full,
            "f_gas_tacconi": ext["f_gas_tacconi"],
            "a0_sync": ext["a0_sync"],
        })

    # -----------------------------------------------------------------------
    # Part 2: Redshift-binned results
    # -----------------------------------------------------------------------
    z_edges = [0.6, 1.22, 2.14, 2.53]
    bin_labels = ["z ~ 0.9", "z ~ 1.5", "z ~ 2.2"]

    print("-" * 72)
    print("PART 1: Binned medians (deep-MOND extraction)")
    print("-" * 72)
    print()
    print(f"{'Bin':>8s}  {'N':>3s}  {'a₀(stars)':>12s}  {'a₀(+gas)':>12s}  "
          f"{'a₀(sync)':>12s}  {'ratio_s':>8s}  {'ratio_g':>8s}  {'f_gas':>6s}")

    for i in range(len(z_edges) - 1):
        z_lo, z_hi = z_edges[i], z_edges[i + 1]
        in_bin = [r for r in results if z_lo <= r["z"] < z_hi]
        if not in_bin:
            continue

        a0_s = np.array([r["a0_deep_stars"] for r in in_bin])
        a0_g = np.array([r["a0_deep_full"] for r in in_bin])
        a0_sync_arr = np.array([r["a0_sync"] for r in in_bin])
        fg = np.array([r["f_gas_tacconi"] for r in in_bin])

        med_s = np.median(a0_s)
        med_g = np.median(a0_g)
        med_sync = np.median(a0_sync_arr)
        med_fg = np.median(fg)

        # Ratio to sync prediction
        ratio_s = med_s / med_sync
        ratio_g = med_g / med_sync

        print(f"{bin_labels[i]:>8s}  {len(in_bin):3d}  "
              f"{med_s:.3e}  {med_g:.3e}  {med_sync:.3e}  "
              f"{ratio_s:8.2f}  {ratio_g:8.2f}  {med_fg:6.2f}")

    # -----------------------------------------------------------------------
    # Part 3: Full RAR inversion (exact, not deep-MOND)
    # -----------------------------------------------------------------------
    print()
    print("-" * 72)
    print("PART 2: Binned medians (full RAR inversion)")
    print("-" * 72)
    print()
    print(f"{'Bin':>8s}  {'N':>3s}  {'N_fit':>5s}  {'a₀(stars)':>12s}  "
          f"{'a₀(+gas)':>12s}  {'a₀(sync)':>12s}  {'ratio_s':>8s}  {'ratio_g':>8s}")

    for i in range(len(z_edges) - 1):
        z_lo, z_hi = z_edges[i], z_edges[i + 1]
        in_bin = [r for r in results if z_lo <= r["z"] < z_hi]
        if not in_bin:
            continue

        # Filter to galaxies where RAR inversion succeeded
        a0_s = [r["a0_rar_stars"] for r in in_bin if r["a0_rar_stars"] is not None]
        a0_g = [r["a0_rar_full"] for r in in_bin if r["a0_rar_full"] is not None]
        a0_sync_arr = np.array([r["a0_sync"] for r in in_bin])
        med_sync = np.median(a0_sync_arr)

        n_s = len(a0_s)
        n_g = len(a0_g)
        med_s = np.median(a0_s) if a0_s else float("nan")
        med_g = np.median(a0_g) if a0_g else float("nan")

        ratio_s = med_s / med_sync if a0_s else float("nan")
        ratio_g = med_g / med_sync if a0_g else float("nan")

        print(f"{bin_labels[i]:>8s}  {len(in_bin):3d}  {n_g:5d}  "
              f"{med_s:.3e}  {med_g:.3e}  {med_sync:.3e}  "
              f"{ratio_s:8.2f}  {ratio_g:8.2f}")

    # -----------------------------------------------------------------------
    # Part 4: Ratio to a₀_local vs ratio to a₀_sync
    # -----------------------------------------------------------------------
    print()
    print("-" * 72)
    print("PART 3: Does a₀ evolve with redshift?")
    print("-" * 72)
    print()
    print("If a₀ = const (standard MOND): ratio to a₀_local ≈ 1 at all z")
    print("If a₀ ∝ H(z) (sync_cost):      ratio to a₀_sync ≈ 1 at all z")
    print()
    print(f"{'Bin':>8s}  {'a₀(+gas)':>12s}  "
          f"{'/ a₀_local':>10s}  {'/ a₀(sync)':>10s}  "
          f"{'H(z)/H₀':>8s}")

    for i in range(len(z_edges) - 1):
        z_lo, z_hi = z_edges[i], z_edges[i + 1]
        in_bin = [r for r in results if z_lo <= r["z"] < z_hi]
        if not in_bin:
            continue

        a0_g = [r["a0_rar_full"] for r in in_bin if r["a0_rar_full"] is not None]
        if not a0_g:
            continue

        z_med = np.median([r["z"] for r in in_bin])
        med_g = np.median(a0_g)
        med_sync = a0_sync(z_med)

        print(f"{bin_labels[i]:>8s}  {med_g:.3e}  "
              f"{med_g / a0_local:10.2f}  {med_g / med_sync:10.2f}  "
              f"{H_of_z(z_med) / H0_si:8.2f}")

    # -----------------------------------------------------------------------
    # Part 5: Gas fraction sensitivity
    # -----------------------------------------------------------------------
    print()
    print("-" * 72)
    print("PART 4: Sensitivity to gas prescription")
    print("-" * 72)
    print()
    print("What a₀ do you get if you scale Tacconi gas mass by a factor?")
    print()

    gas_factors = [0.0, 0.5, 1.0, 1.5, 2.0]
    print(f"{'Bin':>8s}", end="")
    for gf in gas_factors:
        label = "stars only" if gf == 0 else f"×{gf:.1f}"
        print(f"  {label:>12s}", end="")
    print(f"  {'a₀(sync)':>12s}")

    for i in range(len(z_edges) - 1):
        z_lo, z_hi = z_edges[i], z_edges[i + 1]
        in_bin_raw = [r for r in raw if z_lo <= r["z"] < z_hi]
        if not in_bin_raw:
            continue

        print(f"{bin_labels[i]:>8s}", end="")

        for gf in gas_factors:
            a0_vals = []
            for r in in_bin_raw:
                V = r["Vc_kms"] * 1e3
                R = r["Re_kpc"] * kpc_m
                M_star = 10**r["log_Mstar"] * M_sun

                g_obs = V**2 / R

                if gf == 0:
                    g_bar = G * M_star / R**2
                else:
                    M_gas_kg = M_gas_tacconi(r["z"], r["log_Mstar"],
                                             r["delta_log_SFR"]) * M_sun * gf
                    g_bar = G * (M_star + M_gas_kg) / R**2

                if g_obs > g_bar * 1.01:
                    # Full RAR inversion
                    from scipy.optimize import brentq
                    def residual(log_a0, gb=g_bar, go=g_obs):
                        a0 = 10**log_a0
                        return rar_gobs(gb, a0) - go
                    try:
                        log_a0 = brentq(residual, -11, -8)
                        a0_vals.append(10**log_a0)
                    except ValueError:
                        pass

            med = np.median(a0_vals) if a0_vals else float("nan")
            print(f"  {med:.3e}", end="")

        med_sync = np.median([a0_sync(r["z"]) for r in in_bin_raw])
        print(f"  {med_sync:.3e}")

    # -----------------------------------------------------------------------
    # Part 6: Individual galaxy scatter
    # -----------------------------------------------------------------------
    print()
    print("-" * 72)
    print("PART 5: Per-galaxy a₀ (full RAR, stars+gas)")
    print("-" * 72)
    print()
    print(f"{'Galaxy':>15s}  {'z':>5s}  {'logM*':>6s}  {'Re':>5s}  "
          f"{'Vc':>4s}  {'f_gas':>5s}  {'a₀':>10s}  {'a₀/a₀_loc':>9s}  "
          f"{'a₀/sync':>7s}")

    for r in sorted(results, key=lambda x: x["z"]):
        a0 = r["a0_rar_full"]
        if a0 is None:
            flag = " [g_obs ≤ g_bar]"
            print(f"{r['galaxy']:>15s}  {r['z']:5.2f}  {r['logMs']:6.2f}  "
                  f"{r['Re']:5.2f}  {r['Vc']:4.0f}  {r['f_gas_tacconi']:5.2f}  "
                  f"{'---':>10s}  {'---':>9s}  {'---':>7s}{flag}")
        else:
            print(f"{r['galaxy']:>15s}  {r['z']:5.2f}  {r['logMs']:6.2f}  "
                  f"{r['Re']:5.2f}  {r['Vc']:4.0f}  {r['f_gas_tacconi']:5.2f}  "
                  f"{a0:.3e}  {a0 / a0_local:9.2f}  "
                  f"{a0 / r['a0_sync']:7.2f}")

    # Summary stats
    valid = [r for r in results if r["a0_rar_full"] is not None]
    skipped = [r for r in results if r["a0_rar_full"] is None]
    print()
    print(f"Galaxies with a₀ extraction: {len(valid)}/100")
    print(f"Skipped (g_obs ≤ g_bar, no DM enhancement): {len(skipped)}")
    if skipped:
        print(f"  (these are baryon-dominated at R_e — MOND indistinguishable from Newton)")


if __name__ == "__main__":
    main()
