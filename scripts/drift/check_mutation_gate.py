#!/usr/bin/env python3
"""Mutation gate: a verifier that does not flip under premise mutation
verifies nothing.

For each registered verifier script, this gate stages a temp copy of
sync_cost/derivations/*.py, applies a named premise mutation (textual,
never touching the working tree), runs baseline and mutant, and
extracts verdict lines via per-probe regexes. Outcomes:

  DISCRIMINATES  verdict lines change under the mutation
  VACUOUS        verdict lines identical under the mutation
  BROKEN         baseline failed or produced no verdict lines
  SKIPPED        a declared dependency (e.g. numpy) is unavailable

Each probe declares its EXPECTED outcome. Known-vacuous probes are
standing debt, documented here rather than hidden. Exit 2 if any
probe's actual outcome differs from expected (regression either way —
a vacuous probe becoming discriminating means the verifier changed
and the registry must be re-verified). Exit 0 otherwise.

Runtime: ~3-4 minutes (field_equation_klein runs a pure-python solver;
pass --quick to skip targets marked slow).
"""

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DERIV = ROOT / "sync_cost" / "derivations"

# ---------------------------------------------------------------------------
# Registry. mutations: list of (filename, exact_old, exact_new) applied to the
# staged copy. probes: (name, line_regex, expected_outcome). requires: module
# import-checked before running. slow: skipped under --quick.
# ---------------------------------------------------------------------------

TARGETS = [
    {
        "script": "field_equation_klein.py",
        "slow": True,
        "mutations": {
            "xnor": [
                ("field_equation_klein.py",
                 "if (f1.denominator % 2) == (f2.denominator % 2):",
                 "if (f1.denominator % 2) != (f2.denominator % 2):"),
                ("field_equation_klein.py",
                 "if (f1.denominator % 2) != (f2.denominator % 2))",
                 "if (f1.denominator % 2) == (f2.denominator % 2))"),
            ],
            "numerator-parity": [
                ("field_equation_klein.py",
                 "if (f1.denominator % 2) == (f2.denominator % 2):",
                 "if (f1.numerator % 2) == (f2.numerator % 2):"),
                ("field_equation_klein.py",
                 "if (f1.denominator % 2) != (f2.denominator % 2))",
                 "if (f1.numerator % 2) != (f2.numerator % 2))"),
            ],
        },
        "probes": [
            # Aggregate allowed-pair count: the E1 coincidence — numerator-
            # and denominator-parity XOR allow the same COUNT at this pool.
            ("pair-count", r"Klein filter\s+[-0-9.]+\s+(\d+)",
             {"xnor": "DISCRIMINATES", "numerator-parity": "VACUOUS"}),
            # Full dynamics verdict: |r|, top modes, backbone occupation.
            ("dynamics", r"^\s+(?:Torus|Klein filter|Klein twist|Klein combined)\s+[-0-9.]+\s+\d+\s+\(.*\)\s*$",
             {"xnor": "DISCRIMINATES", "numerator-parity": "DISCRIMINATES"}),
        ],
    },
    {
        "script": "gate_duty_cycle.py",
        "slow": False,
        "mutations": {
            "critical-width-law": [
                ("circle_map_utils.py",
                 "        return 1.0 / (q * q)",
                 "        return 1.0 / (q ** 2.164)"),
            ],
        },
        "probes": [
            # Headline coupling-ratio test: 27/8 and its Delta are hardcoded
            # arithmetic — invariant under any width-law mutation (pass-2
            # tautology finding, now pinned).
            ("coupling-ratio-test", r"duty\(q=2\)/duty\(q=3\) = 27/8|α_s/α₂ at M_Z",
             {"critical-width-law": "VACUOUS"}),
            # Weinberg tree-scale test actually consumes tongue_width at K=1.
            ("weinberg-tree", r"duty\(q=1\)/\[duty\(q=1\)\+duty\(q=2\)\]",
             {"critical-width-law": "DISCRIMINATES"}),
        ],
    },
    {
        "script": "gate_duty_predictions.py",
        "slow": False,
        "mutations": {
            "perturbative-width-law": [
                ("circle_map_utils.py",
                 "    return 2 * (K / 2) ** q / q",
                 "    return 2 * (K / 2) ** q / (q * q)"),
            ],
        },
        "probes": [
            # K* is SOLVED from the observed ratio, then the ratio is checked
            # at K*: the fit re-absorbs any width-law mutation, so this check
            # cannot fail — observation-inverted verifier (cf. w_+ pattern).
            # Baseline currently crashes: find_K_star returns exactly 1.0
            # (E8 — target ratio unreachable below K=1), then K*-1 divides
            # by zero. Standing debt: the verifier cannot run at all.
            ("kstar-selfcheck", r"^\s+Δ\s+=\s+\d",
             {"perturbative-width-law": "BROKEN(baseline)"}),
            # sin²θ_W at the re-solved K* is a genuine derived quantity.
            ("sin2thetaw", r"sin²θ_W = duty|predicted = 0\.",
             {"perturbative-width-law": "BROKEN(baseline)"}),
        ],
    },
    {
        "script": "klein_bottle_kuramoto.py",
        "slow": True,
        "requires": "numpy",
        "mutations": {
            "numerator-parity": [
                ("klein_bottle_kuramoto.py",
                 "        return f.denominator % 2",
                 "        return f.numerator % 2"),
            ],
        },
        "probes": [
            ("xor-analysis", r"[Aa]llowed|[Ff]orbidden|surviv",
             {"numerator-parity": "DISCRIMINATES"}),
        ],
    },
]


def stage(tmp: Path, mutation=None) -> Path:
    d = tmp / (mutation or "baseline")
    d.mkdir(parents=True)
    for py in DERIV.glob("*.py"):
        shutil.copy(py, d / py.name)
    return d


def apply_mutation(d: Path, edits):
    for fname, old, new in edits:
        p = d / fname
        text = p.read_text(encoding="utf-8")
        if old not in text:
            raise RuntimeError(f"mutation anchor not found in {fname}: {old[:60]!r}")
        p.write_text(text.replace(old, new, 1), encoding="utf-8")


def run(d: Path, script: str, timeout: int) -> str:
    proc = subprocess.run(
        [sys.executable, script], cwd=d, capture_output=True,
        text=True, timeout=timeout)
    if proc.returncode != 0:
        return None
    return proc.stdout


def extract(regex: str, out: str):
    """Full lines whose content matches the probe regex — the whole
    line is the verdict, so changed values register as changes."""
    pat = re.compile(regex)
    kept = []
    for line in out.splitlines():
        m = pat.search(line)
        if m:
            kept.append(m.group(1) if pat.groups else line)
    return "\n".join(kept)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--quick", action="store_true", help="skip slow targets")
    args = ap.parse_args()

    failures, rows = [], []
    with tempfile.TemporaryDirectory(prefix="mutation-gate-") as tmpdir:
        tmp = Path(tmpdir)
        for target in TARGETS:
            script = target["script"]
            if args.quick and target.get("slow"):
                rows.append((script, "-", "-", "SKIPPED(quick)", ""))
                continue
            req = target.get("requires")
            if req:
                probe_import = subprocess.run(
                    [sys.executable, "-c", f"import {req}"], capture_output=True)
                if probe_import.returncode != 0:
                    for pname, _, exp in target["probes"]:
                        for mname in exp:
                            rows.append((script, mname, pname, "SKIPPED(no-" + req + ")", ""))
                    continue

            base_dir = stage(tmp / script.replace(".py", ""), None)
            timeout = 300 if target.get("slow") else 120
            try:
                base_out = run(base_dir, script, timeout)
            except subprocess.TimeoutExpired:
                base_out = None
            if base_out is None:
                for pname, _, exp in target["probes"]:
                    for mname, expected in exp.items():
                        rows.append((script, mname, pname, "BROKEN(baseline)", ""))
                        if expected != "BROKEN(baseline)":
                            failures.append(
                                f"{script} [{mname}/{pname}]: expected {expected}, "
                                "got BROKEN(baseline)")
                continue

            for mname, edits in target["mutations"].items():
                mut_dir = stage(tmp / script.replace(".py", ""), mname)
                apply_mutation(mut_dir, edits)
                try:
                    mut_out = run(mut_dir, script, timeout)
                except subprocess.TimeoutExpired:
                    mut_out = None
                for pname, regex, expected_by_mut in target["probes"]:
                    if mname not in expected_by_mut:
                        continue
                    expected = expected_by_mut[mname]
                    if mut_out is None:
                        # A mutant crash is a form of discrimination: the
                        # verifier is at least sensitive to the premise.
                        actual = "DISCRIMINATES"
                        note = "mutant crashed"
                    else:
                        base_v = extract(regex, base_out)
                        mut_v = extract(regex, mut_out)
                        if not base_v:
                            actual, note = "BROKEN", "probe matched nothing in baseline"
                        else:
                            actual = "VACUOUS" if base_v == mut_v else "DISCRIMINATES"
                            note = ""
                    rows.append((script, mname, pname, actual, note))
                    if actual != expected and not actual.startswith("SKIPPED"):
                        failures.append(
                            f"{script} [{mname}/{pname}]: expected {expected}, got {actual}"
                            + (f" ({note})" if note else ""))

    w = max(len(r[0]) for r in rows) if rows else 10
    print(f"{'script':<{w}}  {'mutation':<24}  {'probe':<20}  outcome")
    for script, mname, pname, actual, note in rows:
        print(f"{script:<{w}}  {mname:<24}  {pname:<20}  {actual}"
              + (f"  [{note}]" if note else ""))

    vacuous = [r for r in rows if r[3] == "VACUOUS"]
    if vacuous:
        print(f"\nstanding debt: {len(vacuous)} known-vacuous probe(s) — these "
              "verifier outputs cannot fail under their premise mutations "
              "(tautological or observation-inverted).")
    if failures:
        print(f"\nmutation-gate: {len(failures)} unexpected outcome(s)")
        for f in failures:
            print("  " + f)
        return 2
    print("\nmutation-gate: all probes match expected outcomes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
