#!/usr/bin/env python3
"""
load_rc100.py — Data loader for RC100 Table B1

Reads data/rc100.csv and provides it in the formats expected by:
  - rar_high_z.py   (individual galaxy dicts for RAR construction)
  - fdm_redshift.py (redshift-binned medians for f_DM analysis)
  - a0_sensitivity.py (binned parameters for sensitivity sweeps)

CSV columns (from Nestor Shachar et al. 2023, ApJ 944, 78, Table B1):
  id        — galaxy identifier
  z         — spectroscopic redshift
  log_Mstar — log10(stellar mass / M_sun)
  Re_kpc    — effective radius [kpc]
  f_gas     — gas fraction M_gas / M_baryon
  f_DM      — dark matter fraction within R_e
  f_DM_err  — uncertainty on f_DM
  V_circ    — circular velocity at R_e [km/s]
  sigma_0   — central velocity dispersion [km/s]
  B_T       — bulge-to-total ratio
  inc_deg   — inclination [degrees]

When the CSV has data rows, every downstream script uses real measurements.
When it has only the header, scripts fall back to synthetic/fiducial parameters.
"""

import csv
import os
import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_CSV = os.path.join(_HERE, "data", "rc100.csv")

M_sun = 1.989e30  # kg


def _read_csv():
    """Read rc100.csv, return list of row dicts with floats where possible."""
    rows = []
    with open(_CSV, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            parsed = {}
            for k, v in row.items():
                k = k.strip()
                v = v.strip()
                try:
                    parsed[k] = float(v)
                except ValueError:
                    parsed[k] = v
            rows.append(parsed)
    return rows


def has_data():
    """True if rc100.csv contains at least one data row."""
    if not os.path.exists(_CSV):
        return False
    rows = _read_csv()
    return len(rows) > 0


def load_galaxies():
    """Load individual galaxies for RAR construction.

    Returns list of dicts with keys:
        id, z, logMs, Re_kpc, f_gas, f_DM, f_DM_err,
        V_circ, M_baryon, sigma_0, B_T, inc_deg
    """
    raw = _read_csv()
    galaxies = []
    for r in raw:
        logMs = r["log_Mstar"]
        f_gas = r["f_gas"]
        gal = {
            "id": r.get("id", ""),
            "z": r["z"],
            "logMs": logMs,
            "Re_kpc": r["Re_kpc"],
            "f_gas": f_gas,
            "f_DM": r["f_DM"],
            "f_DM_err": r.get("f_DM_err", 0.0),
            "V_circ": r.get("V_circ", 0.0),
            "sigma_0": r.get("sigma_0", 0.0),
            "B_T": r.get("B_T", 0.0),
            "inc_deg": r.get("inc_deg", 0.0),
            "M_baryon": 10**logMs * M_sun * (1 + f_gas),
        }
        galaxies.append(gal)
    return galaxies


def load_bins(z_edges=None):
    """Bin galaxies by redshift and compute medians.

    Returns list of bin dicts matching the format used by fdm_redshift.py
    and a0_sensitivity.py:
        label, z, logMs, Re, fg, fDM_obs, fDM_err, V_obs, n_gal
    """
    if z_edges is None:
        z_edges = [0.6, 1.22, 2.14, 2.53]

    galaxies = load_galaxies()
    bins = []
    for i in range(len(z_edges) - 1):
        z_lo, z_hi = z_edges[i], z_edges[i + 1]
        in_bin = [g for g in galaxies if z_lo <= g["z"] < z_hi]
        if not in_bin:
            continue

        z_med = np.median([g["z"] for g in in_bin])
        logMs_med = np.median([g["logMs"] for g in in_bin])
        Re_med = np.median([g["Re_kpc"] for g in in_bin])
        fg_med = np.median([g["f_gas"] for g in in_bin])
        fDM_med = np.median([g["f_DM"] for g in in_bin])
        V_med = np.median([g["V_circ"] for g in in_bin])

        # Error on the median: MAD / sqrt(N) scaled to sigma
        n = len(in_bin)
        fDM_vals = np.array([g["f_DM"] for g in in_bin])
        fDM_mad = np.median(np.abs(fDM_vals - fDM_med))
        fDM_err = 1.4826 * fDM_mad / np.sqrt(n)  # MAD -> sigma -> sigma_median

        bins.append({
            "label": f"z~{z_med:.1f}",
            "z": float(z_med),
            "logMs": float(logMs_med),
            "Re": float(Re_med),
            "fg": float(fg_med),
            "fDM_obs": float(fDM_med),
            "fDM_err": float(fDM_err),
            "V_obs": float(V_med),
            "n_gal": n,
        })

    return bins


if __name__ == "__main__":
    if has_data():
        galaxies = load_galaxies()
        bins = load_bins()
        print(f"Loaded {len(galaxies)} galaxies in {len(bins)} bins:")
        for b in bins:
            print(f"  {b['label']}: N={b['n_gal']}, "
                  f"logMs={b['logMs']:.2f}, Re={b['Re']:.1f} kpc, "
                  f"f_gas={b['fg']:.2f}, f_DM={b['fDM_obs']:.2f} "
                  f"± {b['fDM_err']:.2f}")
    else:
        print("data/rc100.csv has no data rows yet.")
        print("Expected columns:")
        print("  id, z, log_Mstar, Re_kpc, f_gas, f_DM, f_DM_err,")
        print("  V_circ, sigma_0, B_T, inc_deg")
