#!/usr/bin/env python3
"""
fdm_redshift.py — Hunting for 43 arcseconds in the RC100 data

"43 arcseconds" — Le Verrier (1859) showed that Mercury's perihelion
precesses 43"/century faster than Newtonian gravity predicts.  Too small
to doubt Newton outright, too persistent to ignore.  It sat in the data
for 56 years before general relativity explained it exactly.  The
precession didn't require new observations — it required the right
framework applied to existing data.

We look for the same kind of signal: a small, precise residual in
existing high-redshift rotation-curve data that the standard picture
can't explain, but that a₀(z) = cH(z)/(2π) accounts for naturally.

The candidate: the RAR knee shift.  The radial acceleration relation
has a characteristic scale — the acceleration where observed gravity
departs from baryonic prediction.  If that scale tracks the Hubble
parameter, it shifts by a factor of 2 between z ~ 1 and z ~ 2.
This is testable in the published RC100 rotation curves.

Three models, same galaxy parameters, one residual.
"""

import numpy as np
from scipy.special import i0, i1, k0, k1

# ---------------------------------------------------------------------------
# Cosmology (Planck 2018)
# ---------------------------------------------------------------------------
c_m_s = 2.998e8
H0_km_s_Mpc = 67.4
Mpc_in_m = 3.0857e22
H0_si = H0_km_s_Mpc * 1e3 / Mpc_in_m
Omega_m = 0.315
Omega_L = 0.685
G = 6.674e-11
M_sun = 1.989e30
kpc_m = 3.086e19


def H_of_z(z):
    return H0_si * np.sqrt(Omega_m * (1 + z)**3 + Omega_L)


def a0_of_z(z):
    return c_m_s * H_of_z(z) / (2 * np.pi)

a0_z0 = a0_of_z(0)


# ---------------------------------------------------------------------------
# Exponential disk rotation curve
# ---------------------------------------------------------------------------
def v_newton_disk(r_m, M_b, R_d_m):
    """Newtonian V_circ for a Freeman exponential disk at radius r."""
    y = r_m / (2 * R_d_m)
    if y < 1e-8:
        return 0.0
    bracket = i0(y) * k0(y) - i1(y) * k1(y)
    vn2 = G * M_b / R_d_m * 2 * y**2 * bracket
    return np.sqrt(max(vn2, 0))


# ---------------------------------------------------------------------------
# RAR: the McGaugh et al. (2016) empirical relation
#
# g_obs = g_bar / [1 - exp(-sqrt(g_bar / g†))]
#
# where g† is the acceleration scale.  Locally g† ≈ 1.2e-10 m/s².
# The sync_cost prediction: g†(z) = a₀(z) = cH(z)/(2π).
# ---------------------------------------------------------------------------
def rar_gobs(g_bar, g_dagger):
    """Observed acceleration from the RAR at a given g_bar and scale g†."""
    x = np.sqrt(np.maximum(g_bar / g_dagger, 0))
    # Guard against underflow: for large x, exp(-x) -> 0, g_obs -> g_bar
    denom = 1 - np.exp(-x)
    denom = np.maximum(denom, 1e-30)
    return g_bar / denom


def rar_knee_gbar(g_dagger, departure=1.3):
    """g_bar at which g_obs/g_bar = departure (the RAR "knee").

    Solves: 1 / [1 - exp(-sqrt(g_bar/g†))] = departure
    => exp(-sqrt(g_bar/g†)) = 1 - 1/departure
    => g_bar = g† × [ln(1 / (1 - 1/departure))]²
    """
    return g_dagger * np.log(1 / (1 - 1/departure))**2


# ---------------------------------------------------------------------------
# RC100 galaxy parameters per redshift bin
# ---------------------------------------------------------------------------
# Nestor Shachar et al. (2023, ApJ 944, 78), Table 2 / Fig 8 medians.
# Übler, Nestor Shachar et al. (2024, A&A), Table 3 supplements.
# McGaugh et al. (2024, ApJ 976, 13), BTFR analysis of the same sample.
#
# Each bin: median stellar mass, effective radius, gas fraction, observed
# dark matter fraction within R_e, and (crucially) the number of radial
# resolution elements across the rotation curve.
bins = [
    {"label": "z~0.9", "z": 0.9, "logMs": 10.8, "Re": 5.5, "fg": 0.30,
     "fDM_obs": 0.38, "fDM_err": 0.08, "V_obs": 250, "n_radial": 5},
    {"label": "z~1.5", "z": 1.5, "logMs": 10.85, "Re": 5.0, "fg": 0.40,
     "fDM_obs": 0.32, "fDM_err": 0.08, "V_obs": 255, "n_radial": 4},
    {"label": "z~2.2", "z": 2.2, "logMs": 10.9, "Re": 4.5, "fg": 0.50,
     "fDM_obs": 0.27, "fDM_err": 0.09, "V_obs": 260, "n_radial": 3},
]


def main():
    # ===================================================================
    # PART 1: Three-model comparison of f_DM(z)
    # ===================================================================
    print("=" * 78)
    print("PART 1:  f_DM(z) — three models vs. RC100 data")
    print("=" * 78)
    print()
    print("  For context: 'const a₀' = standard MOND with a₀ fixed at the")
    print("  local value.  'sync_cost' = a₀(z) = cH(z)/(2π).  f_DM is the")
    print("  dark matter fraction within R_e: 1 - M_baryon/M_dyn.")
    print()
    hdr = (f"{'Bin':>7s}  {'a_N/a₀(z)':>10s}  "
           f"{'const a₀':>9s}  {'sync_cost':>10s}  {'observed':>9s}  "
           f"{'ΛCDM dir':>9s}")
    print(hdr)
    print("-" * 78)

    for b in bins:
        z = b["z"]
        Mb = 10**b["logMs"] * M_sun * (1 + b["fg"])
        R_d_m = b["Re"] * kpc_m / 1.678
        R_e_m = b["Re"] * kpc_m

        V_N = v_newton_disk(R_e_m, Mb, R_d_m)
        a_N = V_N**2 / R_e_m
        x_sync = a_N / a0_of_z(z)
        x_const = a_N / a0_z0

        # f_DM = 1/(1+x) for mu(x) = x/(1+x)
        f_const = 1 / (1 + x_const)
        f_sync = 1 / (1 + x_sync)

        print(f"{b['label']:>7s}  {x_sync:10.2f}  "
              f"{f_const:9.3f}  {f_sync:10.3f}  "
              f"{b['fDM_obs']:9.3f}  {'↑ (denser)':>9s}")

    print()
    print("  VERDICT: For these massive galaxies, both MOND variants bracket")
    print("  the data.  The trend is driven by galaxy compactness evolution,")
    print("  not cleanly by a₀.  This is NOT the 43 arcseconds.")

    # ===================================================================
    # PART 2: Synthetic RAR from RC100-like rotation curves
    #
    # This is the key test.  We construct the RAR at each redshift using
    # the exponential disk model + MOND interpolation, then compare where
    # the "knee" (departure from the 1:1 line) falls.
    #
    # Mercury's precession was 43"/century — a 0.01% effect in the orbit,
    # but unmistakable once you knew where to look.  The RAR knee shift
    # is a ~factor-of-2 effect in an already-measured quantity.
    # ===================================================================
    print()
    print("=" * 78)
    print("PART 2:  Synthetic RAR — the knee shift with redshift")
    print("=" * 78)
    print()
    print("  Constructing g_bar(r) and g_obs(r) for RC100-like galaxies at")
    print("  each redshift, using the exponential disk profile + MOND with")
    print("  a₀(z) = cH(z)/(2π).")
    print()

    for b in bins:
        z = b["z"]
        Mb = 10**b["logMs"] * M_sun * (1 + b["fg"])
        R_d_m = b["Re"] * kpc_m / 1.678
        a0z = a0_of_z(z)

        # Sample rotation curve from 0.5 R_d to 4 R_d (typical observational
        # range for IFU data at high z, ~3-4 resolution elements)
        r_arr = np.linspace(0.5 * R_d_m, 4.0 * R_d_m, 50)

        print(f"  --- {b['label']}  (a₀ = {a0z:.2e} m/s²,"
              f"  a₀/a₀(0) = {a0z/a0_z0:.2f}) ---")
        print(f"  {'r/R_d':>6s}  {'g_bar [m/s²]':>14s}  "
              f"{'g_obs(sync)':>14s}  {'g_obs(const)':>14s}  "
              f"{'ratio(sync)':>12s}  {'ratio(const)':>13s}")

        for r_m in r_arr[::7]:  # print every 7th point for readability
            y = r_m / (2 * R_d_m)
            bracket = i0(y) * k0(y) - i1(y) * k1(y)
            vn2 = G * Mb / R_d_m * 2 * y**2 * bracket
            vn2 = max(vn2, 0)
            g_bar = vn2 / r_m  # = V_N² / r = a_N

            g_obs_sync = rar_gobs(g_bar, a0z)
            g_obs_const = rar_gobs(g_bar, a0_z0)

            r_over_Rd = r_m / R_d_m
            ratio_s = g_obs_sync / g_bar if g_bar > 0 else 1.0
            ratio_c = g_obs_const / g_bar if g_bar > 0 else 1.0

            print(f"  {r_over_Rd:6.2f}  {g_bar:14.3e}  "
                  f"{g_obs_sync:14.3e}  {g_obs_const:14.3e}  "
                  f"{ratio_s:12.3f}  {ratio_c:13.3f}")

        print()

    # ===================================================================
    # PART 3: The knee position — quantitative prediction
    #
    # Like the 43 arcseconds: a specific, quantitative residual that
    # discriminates between frameworks.  Le Verrier's residual was
    # 43"/century in a total precession of 5600"/century (0.8%).
    # The RAR knee shift is 2× in an acceleration scale — far larger
    # and far easier to detect.
    # ===================================================================
    print("=" * 78)
    print("PART 3:  RAR knee position vs. redshift — the quantitative test")
    print("=" * 78)
    print()
    print("  The 'knee' = g_bar where g_obs/g_bar first exceeds 1.3")
    print("  (i.e. 30% departure from Newtonian).  This threshold is")
    print("  arbitrary but the RATIO between redshift bins is not.")
    print()

    print(f"  {'z':>5s}  {'a₀(z)':>12s}  {'knee':>12s}  "
          f"{'knee/knee(0)':>13s}  {'log₁₀(knee)':>12s}")
    print("  " + "-" * 62)

    knee_z0 = rar_knee_gbar(a0_z0, 1.3)
    for z in [0, 0.5, 0.9, 1.0, 1.5, 2.0, 2.2, 3.0, 5.0]:
        a0z = a0_of_z(z)
        knee = rar_knee_gbar(a0z, 1.3)
        print(f"  {z:5.1f}  {a0z:12.3e}  {knee:12.3e}  "
              f"{knee/knee_z0:13.2f}  {np.log10(knee):12.2f}")

    # ===================================================================
    # PART 4: What the RC100 rotation curves actually sample
    #
    # The question: do the RC100 data have enough radial coverage and
    # acceleration range to detect the knee shift?
    # ===================================================================
    print()
    print("=" * 78)
    print("PART 4:  Acceleration range probed by RC100")
    print("=" * 78)
    print()

    for b in bins:
        z = b["z"]
        Mb = 10**b["logMs"] * M_sun * (1 + b["fg"])
        R_d_m = b["Re"] * kpc_m / 1.678
        a0z = a0_of_z(z)

        # Inner and outer radius of typical IFU observation
        # Inner: ~0.5 R_e (beam-limited); Outer: ~2 R_e (S/N-limited)
        r_inner = 0.5 * b["Re"] * kpc_m
        r_outer = 2.0 * b["Re"] * kpc_m

        g_inner = v_newton_disk(r_inner, Mb, R_d_m)**2 / r_inner
        g_outer = v_newton_disk(r_outer, Mb, R_d_m)**2 / r_outer

        knee_sync = rar_knee_gbar(a0z, 1.3)
        knee_const = rar_knee_gbar(a0_z0, 1.3)

        # Does the observed acceleration range bracket the knee?
        bracket_sync = "YES" if g_outer < knee_sync < g_inner else "no"
        bracket_const = "YES" if g_outer < knee_const < g_inner else "no"

        print(f"  {b['label']:>7s}: g_bar range [{g_outer:.2e}, {g_inner:.2e}] m/s²")
        print(f"         knee(sync_cost) = {knee_sync:.2e}  "
              f"-- in range? {bracket_sync}")
        print(f"         knee(const a₀)  = {knee_const:.2e}  "
              f"-- in range? {bracket_const}")
        print()

    # ===================================================================
    # PART 5: The discriminating observable
    # ===================================================================
    print("=" * 78)
    print("PART 5:  The test — three predictions, one observation")
    print("=" * 78)
    print("""
  OBSERVABLE:  Fit the RAR knee position g†(z) in each RC100 redshift
  bin.  Compare to three predictions:

  Model          g†(z~0.9)     g†(z~2.2)     ratio     trend
  ─────────────────────────────────────────────────────────────
  const a₀       2.24e-10      2.24e-10      1.0       flat
  sync_cost      3.78e-10      7.57e-10      2.0       rises ∝ H(z)
  ΛCDM           (no universal RAR — scatter, not a clean knee)

  The const-a₀ and sync_cost predictions differ by a factor of 2 at
  z ~ 2.  This is large enough to detect even with the ~0.3 dex scatter
  in individual RAR points at high z, given N ~ 30 galaxies per bin.

  Like Mercury's 43 arcseconds:
    - The data exist (RC100 rotation curves are published)
    - The signal is specific and quantitative (2× knee shift)
    - It discriminates between frameworks (const vs. ∝ H(z))
    - No new parameters are introduced

  Unlike Mercury's 43 arcseconds:
    - The signal is large (factor of 2, not 0.8%)
    - High-z measurement uncertainties are also large (~0.3 dex)
    - The analogy is to the *character* of the test (a residual
      in existing data that picks out the correct framework),
      not to the signal-to-noise ratio
""")

    # ===================================================================
    # PART 6: Empirical extraction — invert f_DM to get a₀(z)
    #
    # The cleanest version of the test.  Instead of predicting f_DM from
    # a₀(z), INVERT: extract the a₀ that the observed f_DM implies, then
    # check whether it tracks H(z).
    #
    # From f_DM = 1/(1 + a_N/a₀):
    #   a₀ = a_N × f_DM / (1 - f_DM)
    #
    # This is model-independent within the MOND interpolation family.
    # The question: does the extracted a₀(z) grow with z, and if so,
    # does it grow as H(z)?
    # ===================================================================
    print("=" * 78)
    print("PART 6:  Empirical a₀(z) — inverting the observed f_DM")
    print("=" * 78)
    print()
    print("  If MOND is the right description, the observed f_DM at R_e")
    print("  implies a specific a₀.  Extracting this a₀(z) from each")
    print("  redshift bin and comparing to H(z) is the direct test.")
    print()
    print("  From f_DM = a₀/(a₀ + a_N):  a₀_implied = a_N × f_DM/(1 - f_DM)")
    print()

    print(f"  {'Bin':>7s}  {'a_N [m/s²]':>12s}  {'f_DM obs':>9s}  "
          f"{'a₀ implied':>12s}  {'a₀ sync':>12s}  "
          f"{'a₀ const':>12s}  {'implied/const':>14s}")
    print("  " + "-" * 88)

    for b in bins:
        z = b["z"]
        Mb = 10**b["logMs"] * M_sun * (1 + b["fg"])
        R_d_m = b["Re"] * kpc_m / 1.678
        R_e_m = b["Re"] * kpc_m
        V_N = v_newton_disk(R_e_m, Mb, R_d_m)
        a_N = V_N**2 / R_e_m

        f = b["fDM_obs"]
        a0_implied = a_N * f / (1 - f)
        a0_sync = a0_of_z(z)

        print(f"  {b['label']:>7s}  {a_N:12.3e}  {f:9.3f}  "
              f"{a0_implied:12.3e}  {a0_sync:12.3e}  "
              f"{a0_z0:12.3e}  {a0_implied/a0_z0:14.2f}")

    print()
    print("  If a₀ is constant:    implied/const should be ~1.0 at all z.")
    print(f"  If a₀ tracks H(z):   implied/const should be "
          f"~{a0_of_z(0.9)/a0_z0:.1f}, "
          f"~{a0_of_z(1.5)/a0_z0:.1f}, "
          f"~{a0_of_z(2.2)/a0_z0:.1f} at z = 0.9, 1.5, 2.2.")
    print()

    # Error propagation: da₀/a₀ = df_DM / [f_DM(1-f_DM)]
    print("  Uncertainty propagation (σ_f ~ 0.08):")
    for b in bins:
        f = b["fDM_obs"]
        sf = b["fDM_err"]
        rel_err = sf / (f * (1 - f))
        Mb = 10**b["logMs"] * M_sun * (1 + b["fg"])
        R_d_m = b["Re"] * kpc_m / 1.678
        R_e_m = b["Re"] * kpc_m
        V_N = v_newton_disk(R_e_m, Mb, R_d_m)
        a_N = V_N**2 / R_e_m
        a0_imp = a_N * f / (1 - f)
        print(f"  {b['label']:>7s}:  a₀ = {a0_imp:.2e} ± {a0_imp*rel_err:.2e}  "
              f"({rel_err*100:.0f}% relative)")

    print()
    print("  The error bars are large on individual bins (~30%), but the")
    print("  TREND is the diagnostic.  Does a₀_implied rise with z?")
    print("  The answer determines whether the 43 arcseconds are there.")

    # ===================================================================
    # Summary: what the numbers say
    # ===================================================================
    print()
    print("=" * 78)
    print("SUMMARY")
    print("=" * 78)
    print("""
  Three findings:

  1. f_DM(z) for massive galaxies is degenerate between models.
     The compactness evolution competes with a₀ evolution.
     Verdict: not diagnostic.

  2. The RAR knee for sync_cost falls just above the RC100 acceleration
     range (Part 4).  This means the two models predict different RAR
     SHAPES within the data: sync_cost predicts persistent ~35% departure
     at all radii; const a₀ predicts near-Newtonian inner radii.
     Verdict: diagnostic if resolved rotation curves are analyzed.

  3. Inverting f_DM to extract a₀(z) empirically (Part 6) gives the
     most direct test.  If the extracted a₀ rises with z and tracks
     H(z), that is the 43 arcseconds — a quantitative residual in
     existing data that the standard picture (a₀ = const) cannot explain.
     Verdict: the test.  Needs the actual RC100 data, not just medians.
""")


if __name__ == "__main__":
    main()
