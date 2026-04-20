#!/usr/bin/env python3
"""
predict_highz.py — Zero-free-parameter predictions for high-z kinematic surveys

Predictions from a₀(z) = c·H(z)/(2π) for galaxy samples matching
KLASS, GEKO, and ALMA-CRISTAL survey parameters.

Every number here follows from:
  1. Planck 2018 cosmology (H₀, Ω_m, Ω_Λ)
  2. The McGaugh+2016 RAR interpolating function
  3. The single relation a₀(z) = c·H(z)/(2π)

No fitted parameters. No dark matter halo model. No gas prescription
(gas enters only through M_baryon = M_star + M_gas, which is an
observable the surveys provide).

FALSIFIABILITY
--------------
For a galaxy with measured (V_obs, M_bar, R_e) at redshift z:

  g_obs = V_obs² / R_e
  g_bar = G·M_bar / R_e²

The prediction is:

  g_obs = g_bar / [1 - exp(-√(g_bar / a₀(z)))]

with a₀(z) = c·H(z)/(2π) — no free parameters.

Three models make distinct predictions:
  (A) Standard MOND:  a₀ = 1.2×10⁻¹⁰ m/s²  (constant)
  (B) sync_cost:      a₀ = c·H(z)/(2π)       (rises with z)
  (C) ΛCDM effective: a₀ ~ 1.2×10⁻¹⁰·(1+z)^¾ (Xu 2022 power law)

Each predicts a different V_obs for the same (M_bar, R_e, z).
The survey measures V_obs. One model wins.
"""

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from framework_constants import C_LIGHT, G_NEWTON, H_0_KM_S_MPC, H_0_SI

# ---------------------------------------------------------------------------
# Constants (Planck 2018)
# ---------------------------------------------------------------------------
G = G_NEWTON         # m³ kg⁻¹ s⁻²
M_sun = 1.989e30     # kg
kpc_m = 3.086e19     # m
c_m_s = C_LIGHT      # m/s

H0_km_s_Mpc = H_0_KM_S_MPC
H0_si = H_0_SI
# Observed Planck 2018 (not framework's 6/19, 13/19).
Omega_m, Omega_L = 0.315, 0.685


def H_of_z(z):
    """Hubble parameter H(z) in SI (s⁻¹), flat ΛCDM."""
    return H0_si * np.sqrt(Omega_m * (1 + z)**3 + Omega_L)


# ---------------------------------------------------------------------------
# Three models for a₀(z)
# ---------------------------------------------------------------------------
def a0_const(z):
    """Standard MOND: a₀ = constant."""
    return 1.2e-10


def a0_sync(z):
    """sync_cost: a₀(z) = c·H(z)/(2π)."""
    return c_m_s * H_of_z(z) / (2 * np.pi)


def a0_xu(z):
    """Xu (2022) ΛCDM effective: a₀ ∝ (1+z)^(3/4)."""
    return 1.2e-10 * (1 + z)**0.75


MODEL_FUNCS = {
    "const_MOND": a0_const,
    "sync_cost":  a0_sync,
    "LCDM_Xu":   a0_xu,
}


# ---------------------------------------------------------------------------
# RAR: McGaugh+2016 interpolating function
# ---------------------------------------------------------------------------
def rar_gobs(g_bar, a0):
    """Predicted g_obs from the RAR given g_bar and a₀."""
    x = np.sqrt(g_bar / a0)
    return g_bar / (1.0 - np.exp(-x))


def predicted_Vcirc(logMbar, Re_kpc, a0):
    """Predicted circular velocity at R_e [km/s] from RAR."""
    M_bar = 10**logMbar * M_sun
    R = Re_kpc * kpc_m
    g_bar = G * M_bar / R**2
    g_obs = rar_gobs(g_bar, a0)
    V = np.sqrt(g_obs * R)
    return V / 1e3  # km/s


def predicted_fDM(logMbar, Re_kpc, a0):
    """Predicted dark matter fraction f_DM(R_e) from RAR.

    f_DM = 1 - g_bar/g_obs = 1 - (1 - exp(-√(g_bar/a₀)))
    """
    M_bar = 10**logMbar * M_sun
    R = Re_kpc * kpc_m
    g_bar = G * M_bar / R**2
    g_obs = rar_gobs(g_bar, a0)
    return 1.0 - g_bar / g_obs


def btfr_Mbar(Vflat_kms, a0):
    """BTFR: M_bar = V⁴ / (G·a₀) in solar masses.

    In MOND, the asymptotic BTFR is exact: V⁴ = G·M·a₀
    """
    V = Vflat_kms * 1e3
    return V**4 / (G * a0 * M_sun)


# ---------------------------------------------------------------------------
# Survey parameter grids
# ---------------------------------------------------------------------------
# KLASS: 44 lensed galaxies, z=0.6-2.3, median logM*=9.5
KLASS_GRID = {
    "name": "KLASS (Girard+2020)",
    "desc": "44 lensed galaxies, KMOS IFU, z=0.6-2.3, logM*=8-11",
    "z_bins": [0.8, 1.2, 1.8],
    "logMbar_range": [9.0, 9.5, 10.0, 10.5],
    "Re_kpc": [2.0, 3.0, 5.0],
}

# GEKO: 163 galaxies, z~4-6, logM*=7-10
GEKO_GRID = {
    "name": "GEKO (Danhaive+2026)",
    "desc": "163 galaxies, JWST grism, z=4-6, logM*=7-10",
    "z_bins": [4.0, 5.0, 6.0],
    "logMbar_range": [8.0, 8.5, 9.0, 9.5],
    "Re_kpc": [1.0, 2.0, 3.0],
}

# CRISTAL: 32 galaxies, z~4-6, logM*=9.5-10.9
CRISTAL_GRID = {
    "name": "ALMA-CRISTAL (Lee+2025)",
    "desc": "32 galaxies, ALMA [CII], z=4-6, logM*=9.5-10.9",
    "z_bins": [4.5, 5.0, 5.5],
    "logMbar_range": [9.5, 10.0, 10.5, 10.8],
    "Re_kpc": [1.5, 3.0, 5.0],
}

SURVEYS = [KLASS_GRID, GEKO_GRID, CRISTAL_GRID]

# ---------------------------------------------------------------------------
# Known high-z galaxies with published kinematics (for direct testing)
# ---------------------------------------------------------------------------
AZ9 = {
    "name": "Az9",
    "ref": "Pope+2023, ApJL 951, L46",
    "z": 4.274,
    "logMs": 9.30,        # log(M*/Msun), intrinsic (mu=7 lensing corrected)
    "Re_kpc": 1.8,        # [CII] half-light radius, source plane
    "V_rot": 139.0,       # km/s, 3D-Barolo tilted-ring max
    "sigma": 26.0,        # km/s
    "V_over_sigma": 5.3,
    "SFR": 26.0,          # Msun/yr total
    "tracer": "[CII]",
}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 78)
    print("ZERO-FREE-PARAMETER PREDICTIONS FOR HIGH-z KINEMATIC SURVEYS")
    print("=" * 78)
    print()
    print("Framework: a₀(z) = c·H(z)/(2π)  [Planck 2018, no fitted parameters]")
    print("RAR:       g_obs = g_bar / [1 - exp(-√(g_bar/a₀))]  [McGaugh+2016]")
    print()

    # ------------------------------------------------------------------
    # Part 0: a₀(z) predictions
    # ------------------------------------------------------------------
    print("-" * 78)
    print("TABLE 0: a₀(z) under each model")
    print("-" * 78)
    print()
    print(f"{'z':>5s}  {'H(z) km/s/Mpc':>14s}  "
          f"{'const_MOND':>12s}  {'sync_cost':>12s}  {'LCDM_Xu':>12s}  "
          f"{'sync/const':>10s}  {'Xu/const':>10s}")

    for z in [0.0, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0]:
        H_val = H_of_z(z) * Mpc_in_m / 1e3  # back to km/s/Mpc
        a_c = a0_const(z)
        a_s = a0_sync(z)
        a_x = a0_xu(z)
        print(f"{z:5.1f}  {H_val:14.1f}  "
              f"{a_c:.3e}  {a_s:.3e}  {a_x:.3e}  "
              f"{a_s/a_c:10.2f}  {a_x/a_c:10.2f}")

    # ------------------------------------------------------------------
    # Part 1: Predicted V_circ for each survey grid
    # ------------------------------------------------------------------
    for survey in SURVEYS:
        print()
        print("-" * 78)
        print(f"TABLE 1: Predicted V_circ(R_e) [km/s] — {survey['name']}")
        print(f"  {survey['desc']}")
        print("-" * 78)
        print()

        for z in survey["z_bins"]:
            print(f"  z = {z:.1f}  |  H(z)/H₀ = {H_of_z(z)/H0_si:.2f}  |  "
                  f"a₀(sync) = {a0_sync(z):.2e} m/s²")
            print()

            # Header
            print(f"  {'logMbar':>8s}  {'Re[kpc]':>7s}  ", end="")
            for model in MODEL_FUNCS:
                print(f"{'V_'+model:>14s}", end="")
            print(f"  {'ΔV s-c [%]':>10s}  {'ΔV s-x [%]':>10s}")

            for logMbar in survey["logMbar_range"]:
                for Re in survey["Re_kpc"]:
                    vals = {}
                    for model, func in MODEL_FUNCS.items():
                        a0 = func(z)
                        vals[model] = predicted_Vcirc(logMbar, Re, a0)

                    v_c = vals["const_MOND"]
                    v_s = vals["sync_cost"]
                    v_x = vals["LCDM_Xu"]

                    # Percentage difference sync vs const, sync vs Xu
                    dv_sc = (v_s - v_c) / v_c * 100
                    dv_sx = (v_s - v_x) / v_x * 100

                    print(f"  {logMbar:8.1f}  {Re:7.1f}  ", end="")
                    for model in MODEL_FUNCS:
                        print(f"{vals[model]:14.1f}", end="")
                    print(f"  {dv_sc:+10.1f}  {dv_sx:+10.1f}")

            print()

    # ------------------------------------------------------------------
    # Part 2: Predicted f_DM(R_e) for each survey
    # ------------------------------------------------------------------
    for survey in SURVEYS:
        print()
        print("-" * 78)
        print(f"TABLE 2: Predicted f_DM(R_e) — {survey['name']}")
        print("-" * 78)
        print()

        for z in survey["z_bins"]:
            print(f"  z = {z:.1f}")
            print()
            print(f"  {'logMbar':>8s}  {'Re[kpc]':>7s}  ", end="")
            for model in MODEL_FUNCS:
                print(f"{'fDM_'+model:>14s}", end="")
            print(f"  {'Δ(s-c)':>8s}")

            for logMbar in survey["logMbar_range"]:
                for Re in survey["Re_kpc"]:
                    vals = {}
                    for model, func in MODEL_FUNCS.items():
                        a0 = func(z)
                        vals[model] = predicted_fDM(logMbar, Re, a0)

                    delta = vals["sync_cost"] - vals["const_MOND"]

                    print(f"  {logMbar:8.1f}  {Re:7.1f}  ", end="")
                    for model in MODEL_FUNCS:
                        print(f"{vals[model]:14.3f}", end="")
                    print(f"  {delta:+8.3f}")
            print()

    # ------------------------------------------------------------------
    # Part 3: BTFR predictions
    # ------------------------------------------------------------------
    print()
    print("-" * 78)
    print("TABLE 3: Baryonic Tully-Fisher Relation — log(M_bar) at fixed V_flat")
    print("-" * 78)
    print()
    print("BTFR: M_bar = V⁴/(G·a₀)  →  log(M_bar) = 4·log(V) - log(G·a₀)")
    print("At fixed V_flat, higher a₀ → lower inferred M_bar (or equivalently,")
    print("at fixed M_bar, higher a₀ → higher V_flat).")
    print()

    V_flats = [50, 80, 100, 120, 150, 200]
    z_vals = [0.0, 1.0, 2.0, 4.0, 6.0]

    print(f"{'V_flat':>7s}", end="")
    for z in z_vals:
        print(f"  {'z='+str(z):>8s}", end="")
    print(f"  {'Δlog(z=0→2)':>12s}  {'Δlog(z=0→4)':>12s}")

    for V in V_flats:
        print(f"{V:7d}", end="")
        log_M_vals = []
        for z in z_vals:
            a0 = a0_sync(z)
            M = btfr_Mbar(V, a0)
            logM = np.log10(M)
            log_M_vals.append(logM)
            print(f"  {logM:8.2f}", end="")
        delta_2 = log_M_vals[2] - log_M_vals[0]
        delta_4 = log_M_vals[3] - log_M_vals[0]
        print(f"  {delta_2:+12.2f}  {delta_4:+12.2f}")

    print()
    print("Interpretation: at V_flat = 100 km/s, a galaxy at z=2 needs")
    a0_0 = a0_sync(0)
    a0_2 = a0_sync(2)
    M_0 = btfr_Mbar(100, a0_0)
    M_2 = btfr_Mbar(100, a0_2)
    print(f"  log(M_bar) = {np.log10(M_2):.2f} to reach V_flat=100,")
    print(f"  vs. {np.log10(M_0):.2f} at z=0.")
    print(f"  That's a {np.log10(M_0)-np.log10(M_2):.2f} dex shift — "
          f"{M_0/M_2:.1f}× less baryonic mass for the same velocity.")
    print(f"  Standard MOND predicts NO shift.")

    # ------------------------------------------------------------------
    # Part 4: Falsifiability summary
    # ------------------------------------------------------------------
    print()
    print("=" * 78)
    print("FALSIFIABILITY")
    print("=" * 78)
    print()
    print("Each prediction above has ZERO free parameters.")
    print("The framework is falsified if:")
    print()
    print("  1. V_obs at fixed (M_bar, R_e, z) matches const_MOND, not sync_cost")
    print("     → a₀ does not evolve with redshift")
    print()
    print("  2. V_obs matches neither model")
    print("     → RAR itself breaks at high z (challenges MOND entirely)")
    print()
    print("  3. f_DM(R_e) does not decrease with z for fixed galaxy properties")
    print("     → contradicts both sync_cost and const_MOND")
    print()
    print("  4. BTFR zero point does not shift between z=0 and z=2")
    print("     → rules out sync_cost, supports const_MOND")
    print()

    # ------------------------------------------------------------------
    # Part 5: Where each survey has discriminating power
    # ------------------------------------------------------------------
    print("-" * 78)
    print("DISCRIMINATING POWER BY SURVEY")
    print("-" * 78)
    print()

    for survey in SURVEYS:
        print(f"  {survey['name']}")
        print(f"    {survey['desc']}")
        print()

        # Find the regime with maximum model separation
        max_delta_V = 0
        best_params = None
        for z in survey["z_bins"]:
            for logM in survey["logMbar_range"]:
                for Re in survey["Re_kpc"]:
                    v_c = predicted_Vcirc(logM, Re, a0_const(z))
                    v_s = predicted_Vcirc(logM, Re, a0_sync(z))
                    dv = abs(v_s - v_c)
                    dv_pct = dv / v_c * 100
                    if dv_pct > max_delta_V:
                        max_delta_V = dv_pct
                        best_params = (z, logM, Re, v_c, v_s, dv_pct)

        z, logM, Re, v_c, v_s, pct = best_params
        print(f"    Maximum separation: {pct:.0f}% in V_circ")
        print(f"      at z={z}, logMbar={logM}, Re={Re} kpc")
        print(f"      const_MOND: V={v_c:.0f} km/s  |  sync_cost: V={v_s:.0f} km/s")
        print()

        # What measurement precision is needed?
        # To distinguish at 3σ with N galaxies:
        # Need σ_V/V < ΔV/(3·V) per galaxy, or N > (3·σ_V/ΔV)²
        for sigma_frac in [0.10, 0.20, 0.30]:
            N_needed = (3 * sigma_frac * v_c / (v_s - v_c))**2
            print(f"    At {sigma_frac*100:.0f}% V_circ uncertainty: "
                  f"need N > {N_needed:.0f} galaxies for 3σ detection")
        print()

    # ------------------------------------------------------------------
    # Part 6: The sweet spot — where to look
    # ------------------------------------------------------------------
    print("-" * 78)
    print("THE SWEET SPOT: galaxy parameters that maximize discrimination")
    print("-" * 78)
    print()
    print("Low mass + large radius + high z = deep MOND regime = maximum signal")
    print()

    print(f"{'z':>5s}  {'logMbar':>8s}  {'Re':>5s}  "
          f"{'V_const':>8s}  {'V_sync':>8s}  {'V_Xu':>8s}  "
          f"{'Δ(s-c)%':>8s}  {'g_bar/a₀(s)':>11s}  {'regime':>10s}")

    sweet_spots = [
        (1.0, 9.0, 4.0),
        (1.5, 9.0, 4.0),
        (2.0, 9.0, 3.0),
        (2.0, 9.5, 5.0),
        (3.0, 9.0, 3.0),
        (4.0, 8.5, 2.0),
        (4.0, 9.0, 3.0),
        (5.0, 8.5, 2.0),
        (6.0, 8.0, 2.0),
    ]

    for z, logM, Re in sweet_spots:
        v_c = predicted_Vcirc(logM, Re, a0_const(z))
        v_s = predicted_Vcirc(logM, Re, a0_sync(z))
        v_x = predicted_Vcirc(logM, Re, a0_xu(z))
        dv = (v_s - v_c) / v_c * 100

        # What regime? g_bar / a₀
        M_bar = 10**logM * M_sun
        R = Re * kpc_m
        g_bar = G * M_bar / R**2
        ratio = g_bar / a0_sync(z)

        if ratio < 0.1:
            regime = "deep MOND"
        elif ratio < 1.0:
            regime = "transition"
        else:
            regime = "Newtonian"

        print(f"{z:5.1f}  {logM:8.1f}  {Re:5.1f}  "
              f"{v_c:8.1f}  {v_s:8.1f}  {v_x:8.1f}  "
              f"{dv:+8.1f}  {ratio:11.3f}  {regime:>10s}")

    print()
    print("Key: g_bar/a₀ < 0.1 → deep MOND (signal largest, ~30-50% ΔV)")
    print("     g_bar/a₀ ~ 0.1-1 → transition zone (signal ~10-30%)")
    print("     g_bar/a₀ > 1 → Newtonian (models indistinguishable)")

    # ------------------------------------------------------------------
    # Part 7: Az9 — first concrete test point
    # ------------------------------------------------------------------
    print()
    print("=" * 78)
    print("Az9 (Pope+2023) — FIRST CONCRETE TEST POINT")
    print("=" * 78)
    print()
    print(f"z = {AZ9['z']},  logM* = {AZ9['logMs']},  "
          f"R_e = {AZ9['Re_kpc']} kpc,  V_obs = {AZ9['V_rot']} km/s,  "
          f"σ = {AZ9['sigma']} km/s")
    print()
    print("Gas fraction is unknown — predictions bracketed over plausible f_gas:")
    print()
    print(f"{'f_gas':>6s}  {'logMbar':>8s}  ", end="")
    for model in MODEL_FUNCS:
        print(f"{'V_'+model:>14s}", end="")
    print(f"  {'V_obs':>8s}  {'best match':>14s}")

    V_obs = AZ9["V_rot"]
    logMs = AZ9["logMs"]
    Re = AZ9["Re_kpc"]
    z = AZ9["z"]

    for fg in [0.0, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]:
        if fg == 0:
            logMbar = logMs
        else:
            logMbar = np.log10(10**logMs / (1 - fg))

        vals = {}
        for model, func in MODEL_FUNCS.items():
            a0 = func(z)
            vals[model] = predicted_Vcirc(logMbar, Re, a0)

        # Which model is closest?
        best = min(vals, key=lambda m: abs(vals[m] - V_obs))
        print(f"{fg:6.2f}  {logMbar:8.2f}  ", end="")
        for model in MODEL_FUNCS:
            marker = " *" if model == best and abs(vals[model] - V_obs) / V_obs < 0.05 else "  "
            print(f"{vals[model]:12.1f}{marker}", end="")
        print(f"  {V_obs:8.1f}  {best:>14s}")

    print()
    print("  * = within 5% of V_obs")
    print()
    print("sync_cost matches V_obs≈139 km/s at f_gas≈0.3 (plausible for logM*=9.3, z=4.3)")
    print("const_MOND requires f_gas≈0.7 (extreme for this stellar mass)")


if __name__ == "__main__":
    main()
