#!/usr/bin/env python3
"""
Convenience: run all drift checks, exit with the max of their codes.

Order is cheapest-first; later checks are skipped if an earlier one
fails fatally (rc >= 2 = environment error).

Run:
  python3 scripts/drift/run_all.py
  python3 scripts/drift/run_all.py --stop-on-fail
"""

import argparse
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent

CHECKS = [
    ("session status", "session_status.py"),
    ("hashlib linter", "lint_local_hashing.py"),
    ("fitted-correction linter", "lint_fitted_corrections.py"),
    ("manifest consistency", "check_manifest.py"),
    ("graph orphans", "check_graph_orphans.py"),
    ("working-tree drift", "check_working_tree.py"),
    ("CAS verification", "verify_cas.py"),
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stop-on-fail", action="store_true")
    args = parser.parse_args()

    worst = 0
    for label, script in CHECKS:
        path = SCRIPT_DIR / script
        print(f"\n=== {label} ===")
        r = subprocess.run([sys.executable, str(path)], check=False)
        worst = max(worst, r.returncode)
        if args.stop_on_fail and r.returncode != 0:
            print(f"\nstop-on-fail: aborting after {label} (rc {r.returncode})")
            return r.returncode
    print(f"\n=== all checks done; worst rc: {worst} ===")
    return worst


if __name__ == "__main__":
    sys.exit(main())
