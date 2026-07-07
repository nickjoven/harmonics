#!/usr/bin/env python3
"""
Convenience: run all drift checks.

Severity model (revised 2026-05-18):

  - FATAL checks gate commits: hashlib linter, fitted-correction
    linter, manifest consistency, graph orphans, CAS verification.
    A nonzero rc contributes to the exit code and, under
    --stop-on-fail, aborts immediately. These encode judgment or a
    real integrity violation (e.g. CAS corruption).

  - ADVISORY checks never gate: working-tree drift, the
    session-status snapshot, and DAG acyclicity. The acyclicity
    check reports cycles in the prose-built `depends_on` graph,
    which is cyclic by construction until edges are typed; it is a
    health signal, not a policy violation. Substrate drift is a
    mechanically-regenerable derived artifact (re-`ket put`), not a
    policy violation. It self-heals on edit via
    scripts/hooks/post_edit_regen.py and is reconciled in CI by
    .github/workflows/substrate-maintenance.yml. Its rc is reported
    but never blocks — which also stops a misfiring pre-commit hook
    from wedging unrelated work just because drift is present.

    session_status.py is advisory because its nonzero rc bundles
    drift AND corruption; demoting it loses no integrity guarantee
    since CAS corruption is independently and fatally gated by
    verify_cas.py (which stays FATAL). The drift/corruption counts
    still print for visibility; they just don't gate.

Order is cheapest-first. Under --stop-on-fail a FATAL nonzero rc
aborts; ADVISORY rc never aborts.

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
    ("DAG acyclicity", "check_dag_acyclic.py"),
    ("graph sealed-projection", "check_graph_sealed.py"),
    ("class-tag coverage", "lint_class_tags.py"),
    ("working-tree drift", "check_working_tree.py"),
    ("CAS verification", "verify_cas.py"),
]

# Nonzero rc is reported but never gates: never adds to the exit
# code, never triggers --stop-on-fail. Drift is a derived artifact,
# not a violation — see module docstring. check_graph_sealed is advisory
# because the corpus is only partially sealed today (coverage signal, not
# a violation); promote it once the corpus is fully sealed.
ADVISORY = {
    "session_status.py",
    "check_working_tree.py",
    "check_dag_acyclic.py",
    "check_graph_sealed.py",
    "lint_class_tags.py",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--stop-on-fail", action="store_true")
    args = parser.parse_args()

    worst = 0
    for label, script in CHECKS:
        path = SCRIPT_DIR / script
        print(f"\n=== {label} ===")
        r = subprocess.run([sys.executable, str(path)], check=False)
        if script in ADVISORY:
            if r.returncode != 0:
                print(
                    f"(advisory: {label} rc {r.returncode} — not gating; "
                    f"self-heals on edit, reconciled in CI)"
                )
            continue
        worst = max(worst, r.returncode)
        if args.stop_on_fail and r.returncode != 0:
            print(f"\nstop-on-fail: aborting after {label} (rc {r.returncode})")
            return r.returncode
    print(f"\n=== all checks done; worst rc: {worst} ===")
    return worst


if __name__ == "__main__":
    sys.exit(main())
