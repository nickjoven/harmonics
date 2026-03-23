#!/usr/bin/env python3
"""
fetch_catalogs.py — Pull high-z kinematic survey data from VizieR via astroquery

Searches for and downloads machine-readable catalogs for:
  - KLASS (Mason+2017, Girard+2020): lensed galaxies z=0.6-2.3
  - GEKO (Danhaive+2025): JWST grism z=4-6
  - ALMA-CRISTAL (Lee+2025): ALMA [CII] z=4-6
  - RC100 (Nestor Shachar+2023): already local, included for completeness

Also searches for other high-z kinematic surveys with published V_rot, sigma.

Requires: astroquery, astropy
    pip install astroquery astropy

Usage:
    python fetch_catalogs.py               # search and download all
    python fetch_catalogs.py --search-only  # just list what's available
    python fetch_catalogs.py --catalog J/ApJ/838/14  # fetch specific catalog
"""

import argparse
import os
import sys
import warnings
from pathlib import Path

import numpy as np

warnings.filterwarnings("ignore")

DATA_DIR = Path(__file__).parent / "data" / "vizier"

# ---------------------------------------------------------------------------
# Known catalog IDs to check (bibcodes → VizieR catalog IDs)
# ---------------------------------------------------------------------------
KNOWN_CATALOGS = {
    "Mason+2017 (KLASS)": {
        "vizier_id": "J/ApJ/838/14",
        "bibcode": "2017ApJ...838...14M",
        "columns": ["z", "logM*", "Vrot", "sigma", "Re"],
    },
    "Girard+2020 (KLASS)": {
        "vizier_id": "J/MNRAS/497/173",
        "bibcode": "2020MNRAS.497..173G",
        "columns": ["z", "logM*", "Vrot", "sigma0", "Vrot/sigma0"],
    },
    "Danhaive+2025 (GEKO dawn)": {
        "vizier_id": "J/MNRAS/543/3249",
        "bibcode": "2025MNRAS.543.3249D",
        "columns": ["z", "logM*", "Vrot", "sigma0"],
    },
    "Danhaive+2025 (GEKO dark)": {
        "vizier_id": "J/MNRAS/546/0",  # placeholder
        "bibcode": "2025arXiv251014779D",
        "columns": ["z", "logM*", "Vrot", "sigma", "logMdyn", "fDM"],
    },
    "Lee+2025 (CRISTAL)": {
        "vizier_id": "J/A+A/701/A260",
        "bibcode": "2025A&A...701A.260L",
        "columns": ["z", "logMbar", "Re", "Vrot", "sigma0", "fgas"],
    },
    "Nestor Shachar+2023 (RC100)": {
        "vizier_id": "J/ApJ/944/78",
        "bibcode": "2023ApJ...944...78N",
        "columns": ["z", "logMstar", "Re", "Vc", "sigma0", "fDM"],
    },
}

# Additional high-z kinematic surveys to search for
SEARCH_KEYWORDS = [
    # Survey name searches
    "SINS galaxy kinematics rotation",
    "KMOS3D galaxy rotation velocity dispersion",
    "MOSDEF kinematics",
    "MASSIV kinematics rotation",
    # Generic high-z kinematic searches
    "high redshift galaxy rotation curve",
    "galaxy kinematics IFU z>2",
    "Tully-Fisher high redshift",
    "velocity dispersion rotation z>1 galaxy",
]


def ensure_data_dir():
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def try_import_astroquery():
    try:
        from astroquery.vizier import Vizier
        return Vizier
    except ImportError:
        print("ERROR: astroquery not installed. Run: pip install astroquery")
        sys.exit(1)


# ---------------------------------------------------------------------------
# Check if a specific catalog exists on VizieR
# ---------------------------------------------------------------------------
def check_catalog(vizier_id, label=""):
    """Check if a VizieR catalog exists and return its table list."""
    Vizier = try_import_astroquery()
    v = Vizier(catalog=vizier_id, row_limit=5)
    try:
        tables = v.get_catalogs(vizier_id)
        if tables:
            print(f"  FOUND: {label} [{vizier_id}]")
            for t in tables:
                print(f"    Table: {t.meta.get('name', '?')} — "
                      f"{len(t)} rows, {len(t.colnames)} columns")
                print(f"    Columns: {', '.join(t.colnames[:15])}")
                if len(t.colnames) > 15:
                    print(f"             ... and {len(t.colnames)-15} more")
            return tables
        else:
            print(f"  NOT FOUND: {label} [{vizier_id}]")
            return None
    except Exception as e:
        print(f"  ERROR checking {label} [{vizier_id}]: {e}")
        return None


# ---------------------------------------------------------------------------
# Search for catalogs by keyword
# ---------------------------------------------------------------------------
def search_catalogs(keywords):
    """Search VizieR for catalogs matching keywords."""
    Vizier = try_import_astroquery()
    all_found = {}
    for kw in keywords:
        print(f"\n  Searching: '{kw}'...")
        try:
            cats = Vizier.find_catalogs(kw)
            for cat_id, cat_info in cats.items():
                if cat_id not in all_found:
                    all_found[cat_id] = cat_info.description
                    print(f"    {cat_id}: {cat_info.description}")
        except Exception as e:
            print(f"    Error: {e}")
    return all_found


# ---------------------------------------------------------------------------
# Download a full catalog
# ---------------------------------------------------------------------------
def download_catalog(vizier_id, label="", row_limit=-1):
    """Download all tables from a VizieR catalog and save as CSV."""
    Vizier = try_import_astroquery()
    ensure_data_dir()

    v = Vizier(catalog=vizier_id, row_limit=row_limit)
    try:
        tables = v.get_catalogs(vizier_id)
    except Exception as e:
        print(f"  Failed to download {vizier_id}: {e}")
        return None

    if not tables:
        print(f"  No tables found in {vizier_id}")
        return None

    saved_files = []
    for i, table in enumerate(tables):
        tname = table.meta.get("name", f"table{i}")
        safe_id = vizier_id.replace("/", "_")
        fname = DATA_DIR / f"{safe_id}_{tname}.csv"

        # Convert astropy Table to CSV
        table.write(str(fname), format="csv", overwrite=True)
        saved_files.append(fname)
        print(f"  Saved: {fname} ({len(table)} rows, {len(table.colnames)} cols)")
        print(f"    Columns: {', '.join(table.colnames)}")

    return saved_files


# ---------------------------------------------------------------------------
# Load a downloaded catalog into a standard format
# ---------------------------------------------------------------------------
def load_kinematic_catalog(csv_path, column_map=None):
    """Load a VizieR CSV into a list of galaxy dicts.

    column_map: dict mapping standard keys to CSV column names.
    Standard keys: z, logMs, Re_kpc, V_rot, sigma, logMbar
    """
    import csv as csv_mod

    if column_map is None:
        column_map = {}

    rows = []
    with open(csv_path, newline="") as f:
        reader = csv_mod.DictReader(f)
        for row in reader:
            gal = {}
            for std_key, csv_col in column_map.items():
                if csv_col in row:
                    try:
                        gal[std_key] = float(row[csv_col])
                    except (ValueError, TypeError):
                        gal[std_key] = row[csv_col]
            rows.append(gal)
    return rows


# ---------------------------------------------------------------------------
# Az9 hardcoded (single object, Pope+2023)
# ---------------------------------------------------------------------------
def load_az9():
    """Return Az9 data from Pope+2023 (single galaxy, values from paper)."""
    return [{
        "id": "Az9",
        "survey": "Pope+2023",
        "z": 4.274,
        "logMs": np.log10(2e9),       # 9.30
        "logMbar": None,               # unknown gas mass; SFR=26 Msun/yr
        "Re_kpc": 1.8,                 # [CII] half-light radius, source plane
        "V_rot": 139.0,                # km/s, max from 3D-Barolo
        "sigma": 26.0,                 # km/s
        "V_over_sigma": 5.3,
        "SFR": 26.0,                   # Msun/yr, total
        "mu_lens": 7.0,                # magnification factor
        "tracer": "[CII]",
        "notes": "Lensed disk behind Abell 2744. CO(4-3) confirms V/sigma=4.6±1.7.",
    }]


# ---------------------------------------------------------------------------
# Summary of what's available
# ---------------------------------------------------------------------------
def list_local_data():
    """List all locally cached VizieR data."""
    ensure_data_dir()
    csvs = sorted(DATA_DIR.glob("*.csv"))
    if csvs:
        print(f"\nLocal VizieR data in {DATA_DIR}/:")
        for f in csvs:
            # Count lines
            with open(f) as fh:
                n = sum(1 for _ in fh) - 1
            print(f"  {f.name}: {n} rows")
    else:
        print(f"\nNo local VizieR data yet. Run with --fetch to download.")

    # Always have Az9
    az9 = load_az9()
    print(f"\nHardcoded data:")
    print(f"  Az9 (Pope+2023): z={az9[0]['z']}, V_rot={az9[0]['V_rot']} km/s, "
          f"sigma={az9[0]['sigma']} km/s")

    # Check for RC100
    rc100_path = Path(__file__).parent / "data" / "rc100_table3.csv"
    if rc100_path.exists():
        with open(rc100_path) as f:
            n = sum(1 for line in f if not line.startswith("#")) - 1
        print(f"  RC100 (Nestor Shachar+2023): {n} galaxies, z=0.6-2.5")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description="Fetch high-z kinematic catalogs from VizieR")
    parser.add_argument("--search-only", action="store_true",
                        help="Only search, don't download")
    parser.add_argument("--check-known", action="store_true",
                        help="Check if known catalogs exist on VizieR")
    parser.add_argument("--fetch", action="store_true",
                        help="Download all available catalogs")
    parser.add_argument("--catalog", type=str,
                        help="Fetch a specific VizieR catalog ID")
    parser.add_argument("--search", type=str, nargs="+",
                        help="Search VizieR for catalogs matching keywords")
    parser.add_argument("--local", action="store_true",
                        help="List locally cached data")
    args = parser.parse_args()

    if args.local or not any(vars(args).values()):
        list_local_data()
        if not any(vars(args).values()):
            print("\nRun with --check-known, --search-only, --fetch, or --catalog <ID>")
        return

    if args.check_known:
        print("Checking known catalogs on VizieR...")
        print()
        for label, info in KNOWN_CATALOGS.items():
            check_catalog(info["vizier_id"], label)
            print()

    if args.search_only or args.search:
        kws = args.search if args.search else SEARCH_KEYWORDS
        print("Searching VizieR for high-z kinematic surveys...")
        found = search_catalogs(kws)
        print(f"\nTotal unique catalogs found: {len(found)}")

    if args.catalog:
        print(f"Fetching catalog {args.catalog}...")
        download_catalog(args.catalog, args.catalog)

    if args.fetch:
        print("Attempting to download all known catalogs...")
        print()
        for label, info in KNOWN_CATALOGS.items():
            print(f"Trying {label}...")
            download_catalog(info["vizier_id"], label)
            print()

        print("Done. Use --local to see what was saved.")


if __name__ == "__main__":
    main()
