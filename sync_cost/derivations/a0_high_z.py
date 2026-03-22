#!/usr/bin/env python3
"""
a0_high_z.py — Redshift dependence of the MOND acceleration scale

Computes the sync_cost prediction:  a0(z) = c H(z) / (2 pi)

Uses standard LCDM cosmology for H(z):
    H(z) = H0 * sqrt(Omega_m (1+z)^3 + Omega_Lambda)

Planck 2018 parameters:
    H0      = 67.4 km/s/Mpc
    Omega_m = 0.315
    Omega_L = 0.685
"""

import numpy as np

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
c_m_s = 2.998e8          # speed of light [m/s]
H0_km_s_Mpc = 67.4       # Hubble constant [km/s/Mpc]
Mpc_in_m = 3.0857e22     # 1 Mpc in metres
H0_si = H0_km_s_Mpc * 1e3 / Mpc_in_m   # H0 in s^-1

Omega_m = 0.315
Omega_L = 0.685

a0_observed = 1.2e-10    # observed MOND acceleration scale [m/s^2]


# ---------------------------------------------------------------------------
# H(z) and a0(z)
# ---------------------------------------------------------------------------
def H_of_z(z):
    """Hubble parameter H(z) in s^-1 (flat LCDM, matter + Lambda only)."""
    return H0_si * np.sqrt(Omega_m * (1 + z)**3 + Omega_L)


def a0_of_z(z):
    """Predicted MOND acceleration scale at redshift z [m/s^2]."""
    return c_m_s * H_of_z(z) / (2 * np.pi)


# ---------------------------------------------------------------------------
# Tabulate predictions
# ---------------------------------------------------------------------------
def main():
    z_values = np.array([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 5.0, 7.0, 10.0])

    a0_z0 = a0_of_z(0.0)

    print("=" * 72)
    print("Prediction:  a0(z) = c H(z) / (2 pi)")
    print(f"H0 = {H0_km_s_Mpc} km/s/Mpc   =>  H0 = {H0_si:.4e} s^-1")
    print(f"a0(z=0) predicted = {a0_z0:.4e} m/s^2")
    print(f"a0 observed       = {a0_observed:.4e} m/s^2")
    print(f"Ratio obs/pred    = {a0_observed / a0_z0:.3f}")
    print("=" * 72)
    print()
    print(f"{'z':>6s}  {'H(z) [km/s/Mpc]':>18s}  {'a0(z) [m/s^2]':>16s}  "
          f"{'a0(z)/a0(0)':>12s}  {'Lookback [Gyr]':>15s}")
    print("-" * 72)

    for z in z_values:
        Hz = H_of_z(z)
        Hz_kms = Hz * Mpc_in_m / 1e3   # back to km/s/Mpc for display
        a0z = a0_of_z(z)
        ratio = a0z / a0_z0
        # Approximate lookback time (flat LCDM numerical integration)
        t_lb = _lookback_time_gyr(z)
        print(f"{z:6.1f}  {Hz_kms:18.1f}  {a0z:16.4e}  {ratio:12.3f}  "
              f"{t_lb:15.2f}")

    print()
    print("KEY RESULT:  At z=2,  a0 is predicted to be ~{:.1f}x larger than "
          "today.".format(a0_of_z(2.0) / a0_z0))
    print("             At z=5,  a0 ~ {:.1f}x larger.".format(
          a0_of_z(5.0) / a0_z0))
    print()

    # -----------------------------------------------------------------------
    # Observational comparison
    # -----------------------------------------------------------------------
    print("=" * 72)
    print("OBSERVATIONAL STATUS (as of early 2026)")
    print("=" * 72)
    print("""
Nestor Shachar et al. (2023, ApJ 944, 78) — "RC100"
  100 massive star-forming galaxies at z = 0.6–2.5, Halpha/CO rotation
  curves from VLT SINFONI/KMOS + ALMA.
  Key finding: dark-matter fraction within R_e decreases with redshift,
  f_DM ~ 0.38 at z~1, ~0.27 at z~2.  Half of z~2 galaxies are maximal
  disks.  This is qualitatively consistent with a larger a0(z).

McGaugh et al. (2024, ApJ 976, 13) — "Accelerated Structure Formation"
  Used the RC100 data binned by redshift on the baryonic Tully-Fisher
  relation (BTFR).  Found NO clear evolution of the BTFR zero point out
  to z ~ 2.5 (lookback ~ 11 Gyr).
  Interpretation:  If a0 were constant (standard MOND), the BTFR would
  not evolve.  If a0 = cH(z)/(2pi), BTFR normalisation should shift by
  ~3x in a0 (or ~0.5 dex in log Mb at fixed V).  The data do not yet
  clearly show this shift, but:
    - The RC100 sample is biased toward massive galaxies (V > 200 km/s)
      where the Newtonian regime dominates and a0 shifts are less visible.
    - The measurement uncertainties on individual rotation curves at z~2
      are 20-40%, swamping the predicted ~0.4 dex signal.

Ubler, Nestor Shachar et al. (2024, A&A) — TFR at 0.6 < z < 2.5
  Stellar TFR slope alpha = 3.03 +/- 0.25, "subtle deviation" from
  local studies.  Modest evidence for evolution, not yet decisive.

Xu (2022, arXiv:2203.05606, updated Feb 2025)
  Proposes a0 ~ (1+z)^(3/4) from CDM simulations (Magneticum, EAGLE).
  Magneticum: a0 increases ~3x from z=0 to z=2.3.
  This cH(z)/(2pi) prediction gives ~3.0x at z=2 — similar order but
  different functional form (testably different at z > 3).

CURRENT VERDICT:
  The data are not yet precise enough to confirm or rule out a0(z).
  The strongest near-term path is:
    1. JWST NIRSpec IFU rotation curves of z=2-4 disk galaxies in the
       LOW-MASS regime (V ~ 50-100 km/s) where MOND effects dominate.
    2. Stacking analyses of the BTFR at z>2 with baryonic masses from
       SED fitting + gas masses from ALMA dust continuum.
    3. Euclid + LSST strong-lensing statistics of disk galaxies as a
       complementary probe (Tian et al. 2025).
""")

    # -----------------------------------------------------------------------
    # What instruments need to measure
    # -----------------------------------------------------------------------
    print("=" * 72)
    print("MEASUREMENT REQUIREMENTS")
    print("=" * 72)
    print("""
To test a0(z) = cH(z)/(2pi) we need:

1. Rotation curves of LOW-MASS disk galaxies at z > 1.5
   - Flat rotation velocity V_flat ~ 50–120 km/s (MOND regime: a < a0)
   - Need V_flat to ~10% accuracy => spectral resolution R > 3000
   - JWST NIRSpec IFU (R~2700) is marginal; R~4000 mode preferred
   - Need spatial resolution < 1 kpc => lensed arcs or AO-assisted

2. Baryonic masses to ~0.2 dex
   - Stellar mass: JWST NIRCam photometry + SED fitting
   - Gas mass: ALMA Band 6/7 dust continuum or CO(3-2) for z ~ 2

3. Sample size
   - The BTFR shift between a0(z=0) and a0(z=2) is ~0.5 dex in log(Mb)
     at fixed V_flat.
   - To detect 0.5 dex offset at 3-sigma with 0.3 dex scatter:
     N ~ (3 * 0.3 / 0.5)^2 ~ 4 per redshift bin (statistical only)
   - Systematic floor (beam smearing, pressure support corrections,
     inclination uncertainty) likely requires N > 20 per bin.

4. Redshift baseline
   - z=0 (local SPARC sample, well-measured)
   - z=1 (H(z)/H0 ~ 1.8 => a0 ratio ~ 1.8)
   - z=2 (H(z)/H0 ~ 3.0 => a0 ratio ~ 3.0)
   - z=3 (H(z)/H0 ~ 4.6 => a0 ratio ~ 4.6)
   Minimum: compare z~0 with z~2 for a factor-of-3 lever arm.
""")


def _lookback_time_gyr(z, n_steps=1000):
    """Numerical lookback time for flat LCDM [Gyr]."""
    sec_per_gyr = 3.1557e16   # seconds in 1 Gyr
    zp = np.linspace(0, z, n_steps + 1)
    integrand = 1.0 / ((1 + zp) * np.sqrt(Omega_m * (1 + zp)**3 + Omega_L))
    integral = np.trapezoid(integrand, zp) if hasattr(np, 'trapezoid') else np.trapz(integrand, zp)
    return integral / (H0_si * sec_per_gyr)  # 1/H0 in Gyr * integral


if __name__ == "__main__":
    main()
