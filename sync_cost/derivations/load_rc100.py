#!/usr/bin/env python3
"""
load_rc100.py — Data loader for RC100 Table 3

Reads data/rc100_table3.csv and provides it in the formats expected by:
  - rar_high_z.py   (individual galaxy dicts for RAR construction)
  - fdm_redshift.py (redshift-binned medians for f_DM analysis)
  - a0_sensitivity.py (binned parameters for sensitivity sweeps)

Source: Nestor Shachar et al. (2023), ApJ 944, 78, Table 3
  100 galaxies at z = 0.6–2.5 with best-fit rotation curve parameters.
"""

import csv
import os
import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_CSV = os.path.join(_HERE, "data", "rc100_table3.csv")

M_sun = 1.989e30  # kg


def _read_csv():
    """Read rc100_table3.csv, skipping comment lines."""
    rows = []
    if not os.path.exists(_CSV):
        return rows
    with open(_CSV, newline="") as f:
        # Skip comment lines starting with #
        lines = [line for line in f if not line.startswith("#")]
    reader = csv.DictReader(lines)
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
    """True if rc100_table3.csv exists and contains data rows."""
    return len(_read_csv()) > 0


def load_galaxies():
    """Load individual galaxies for RAR construction.

    Returns list of dicts with keys:
        id, z, logMs, Re_kpc, f_gas, f_DM, f_DM_err,
        V_circ, sigma_0, log_Mbulge, M_baryon
    """
    raw = _read_csv()
    galaxies = []
    for r in raw:
        logMs = r["log_Mstar"]
        logMb = r["log_Mbaryon"]
        # f_gas = (M_baryon - M_star) / M_baryon = 1 - 10^(logMs - logMb)
        f_gas = max(0.0, 1.0 - 10**(logMs - logMb))

        gal = {
            "id": r.get("Galaxy", ""),
            "z": r["z"],
            "logMs": logMs,
            "Re_kpc": r["Re_kpc"],
            "f_gas": f_gas,
            "f_DM": r["fDM"],
            "f_DM_err": r.get("e_fDM", 0.0),
            "V_circ": r.get("Vc_kms", 0.0),
            "sigma_0": r.get("sigma0_kms", 0.0),
            "log_Mbulge": r.get("log_Mbulge", 0.0),
            "M_baryon": 10**logMb * M_sun,
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
        print("data/rc100_table3.csv not found or empty.")
