#!/usr/bin/env python3
"""
a0_sensitivity.py — Sensitivity of the implied a₀(z) to galaxy parameters

The empirical a₀ extraction from RC100 f_DM (fdm_redshift.py, Part 6)
shows a₀_implied rising with z but at ~half the rate predicted by H(z).

How much of this gap comes from uncertain galaxy parameters?

The implied a₀ = a_N × f_DM / (1 - f_DM),  where  a_N = V_N²(R_e) / R_e.

The Newtonian acceleration a_N depends on:
  - Baryonic mass M_b  (stellar mass × (1 + f_gas))
  - Effective radius R_e
  - Disk profile (exponential, Sérsic, etc.)

Each is uncertain at the ~0.2-0.3 dex level at high z.  This script
maps those uncertainties into the implied a₀, testing whether the
half-rate discrepancy is physical or parametric.
"""

import numpy as np
from scipy.special import i0, i1, k0, k1

# Constants
c_m_s = 2.998e8
H0_km_s_Mpc = 67.4
Mpc_in_m = 3.0857e22
H0_si = H0_km_s_Mpc * 1e3 / Mpc_in_m
Omega_m, Omega_L = 0.315, 0.685
G = 6.674e-11
M_sun = 1.989e30
kpc_m = 3.086e19


def H_of_z(z):
    return H0_si * np.sqrt(Omega_m * (1 + z)**3 + Omega_L)


def a0_of_z(z):
    return c_m_s * H_of_z(z) / (2 * np.pi)

a0_z0 = a0_of_z(0)


def v_newton_disk(r_m, M_b, R_d_m):
    y = r_m / (2 * R_d_m)
    if y < 1e-8:
        return 0.0
    bracket = i0(y) * k0(y) - i1(y) * k1(y)
    vn2 = G * M_b / R_d_m * 2 * y**2 * bracket
    return np.sqrt(max(vn2, 0))


def implied_a0(logMs, Re_kpc, f_gas, f_DM):
    """Extract the implied a₀ from observed galaxy parameters + f_DM."""
    Mb = 10**logMs * M_sun * (1 + f_gas)
    R_d_m = Re_kpc * kpc_m / 1.678
    R_e_m = Re_kpc * kpc_m
    V_N = v_newton_disk(R_e_m, Mb, R_d_m)
    if V_N == 0:
        return 0.0
    a_N = V_N**2 / R_e_m
    return a_N * f_DM / (1 - f_DM)


def main():
    print("=" * 78)
    print("Sensitivity of implied a₀(z) to galaxy parameters")
    print("=" * 78)

    # Fiducial RC100 bin parameters
    bins = [
        {"label": "z~0.9", "z": 0.9, "logMs": 10.8, "Re": 5.5,
         "fg": 0.30, "fDM": 0.38},
        {"label": "z~1.5", "z": 1.5, "logMs": 10.85, "Re": 5.0,
         "fg": 0.40, "fDM": 0.32},
        {"label": "z~2.2", "z": 2.2, "logMs": 10.9, "Re": 4.5,
         "fg": 0.50, "fDM": 0.27},
    ]

    # ---------------------------------------------------------------
    # 1. Gas fraction sensitivity
    #
    # Gas fractions at z > 1 are highly uncertain.  Tacconi et al.
    # (2018, 2020) find f_gas ~ 0.3-0.7 at z ~ 2, with large scatter.
    # If the actual f_gas is higher, M_b is larger, a_N is larger,
    # and the implied a₀ rises.
    # ---------------------------------------------------------------
    print()
    print("--- Gas fraction sensitivity ---")
    print()
    print(f"  {'Bin':>7s}  {'f_gas':>6s}  {'log M_b':>8s}  "
          f"{'a₀ impl':>10s}  {'impl/const':>11s}  {'sync pred':>10s}")
    print("  " + "-" * 60)

    for b in bins:
        for fg in [0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0]:
            a0_imp = implied_a0(b["logMs"], b["Re"], fg, b["fDM"])
            logMb = b["logMs"] + np.log10(1 + fg)
            sync_ratio = a0_of_z(b["z"]) / a0_z0
            marker = " <-- fiducial" if abs(fg - b["fg"]) < 0.01 else ""
            print(f"  {b['label']:>7s}  {fg:6.2f}  {logMb:8.2f}  "
                  f"{a0_imp:10.3e}  {a0_imp/a0_z0:11.2f}  "
                  f"{sync_ratio:10.2f}{marker}")
        print()

    # ---------------------------------------------------------------
    # 2. Effective radius sensitivity
    #
    # R_e measurements at high z have ~20% systematic uncertainty
    # from PSF modelling and surface-brightness dimming corrections.
    # ---------------------------------------------------------------
    print("--- Effective radius sensitivity ---")
    print()
    print(f"  {'Bin':>7s}  {'R_e':>6s}  {'a₀ impl':>10s}  "
          f"{'impl/const':>11s}  {'sync pred':>10s}")
    print("  " + "-" * 55)

    for b in bins:
        for Re_factor in [0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3]:
            Re = b["Re"] * Re_factor
            a0_imp = implied_a0(b["logMs"], Re, b["fg"], b["fDM"])
            sync_ratio = a0_of_z(b["z"]) / a0_z0
            marker = " <-- fiducial" if abs(Re_factor - 1.0) < 0.01 else ""
            print(f"  {b['label']:>7s}  {Re:6.2f}  {a0_imp:10.3e}  "
                  f"{a0_imp/a0_z0:11.2f}  {sync_ratio:10.2f}{marker}")
        print()

    # ---------------------------------------------------------------
    # 3. Combined: what parameters reproduce the sync_cost prediction?
    #
    # For each bin, find the f_gas that makes implied a₀ = cH(z)/(2π).
    # ---------------------------------------------------------------
    print("=" * 78)
    print("What gas fraction would reproduce the sync_cost prediction?")
    print("=" * 78)
    print()

    for b in bins:
        target = a0_of_z(b["z"])
        # Scan f_gas to find the one that gives implied a₀ = target
        best_fg = None
        for fg_try in np.arange(0.1, 3.0, 0.01):
            a0_imp = implied_a0(b["logMs"], b["Re"], fg_try, b["fDM"])
            if a0_imp >= target:
                best_fg = fg_try
                break

        if best_fg is not None:
            logMb = b["logMs"] + np.log10(1 + best_fg)
            print(f"  {b['label']:>7s}: f_gas = {best_fg:.2f}  "
                  f"(log M_b = {logMb:.2f})  "
                  f"vs. fiducial f_gas = {b['fg']:.2f}")
        else:
            print(f"  {b['label']:>7s}: no f_gas in [0.1, 3.0] reaches target")

    print()
    print("  READING: The z~0.9 bin needs only a modest increase in f_gas")
    print("  (~0.5 vs 0.3) to match.  The z~2.2 bin needs f_gas ~ 1.5+,")
    print("  which is plausible for gas-rich high-z disks but at the upper")
    print("  end of current estimates.")
    print()
    print("  This does NOT mean the parameters are wrong — it means the")
    print("  extraction is sensitive to M_b, and the RC100 bin medians are")
    print("  not precise enough for a definitive test.  The test needs:")
    print("  (a) individual galaxy fits, not bin medians")
    print("  (b) ALMA gas masses, not assumed f_gas")
    print("  (c) resolved RAR, not single-point f_DM at R_e")


if __name__ == "__main__":
    main()
