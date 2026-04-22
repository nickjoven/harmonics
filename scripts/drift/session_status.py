#!/usr/bin/env python3
"""
Tool #7: Session-start substrate snapshot.

One-line status report: CAS size, corrupt count, scorecard counts,
git dirtiness, drift. Fast — designed to be run at the start of
every session so you don't build on a drifted foundation.

Example output:
  harmonics: CAS 80 (0 corrupt) | scorecard 16 + bare_k1 5 |
             git 0 dirty | drift 0 | env: blake3 module

Exits 0 on clean state, 1 on any non-zero counter (except git dirty,
which is informational only).

Run:
  python3 scripts/drift/session_status.py
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _hash import hash_file, HashingUnavailable, environment_summary

try:
    import yaml
except ImportError:
    yaml = None


def _git_dirty_count(root: Path) -> int:
    try:
        r = subprocess.run(
            ["git", "-C", str(root), "status", "--porcelain"],
            capture_output=True, check=False,
        )
        return len([ln for ln in r.stdout.decode().splitlines() if ln.strip()])
    except Exception:
        return -1


def _cas_counts(cas: Path) -> tuple[int, int]:
    if not cas.is_dir():
        return (0, 0)
    entries = list(cas.iterdir())
    try:
        corrupt = sum(1 for e in entries if hash_file(e) != e.name)
    except HashingUnavailable:
        return (len(entries), -1)  # -1 = unknown
    return (len(entries), corrupt)


def _drift_count(root: Path, log_path: Path) -> int:
    if not log_path.exists():
        return 0
    import re
    PUT = re.compile(
        r"^\S+\s+\|\s+put\s+\|\s+(?P<path>\S[^\n]*?)\s+->\s+(?P<cid>[0-9a-f]{64})\s*$"
    )
    last = {}
    for line in log_path.read_text().splitlines():
        m = PUT.match(line)
        if m:
            path = m.group("path")
            if path == "-":  # stdin put; not a tracked file
                continue
            last[path] = m.group("cid")
    drift = 0
    try:
        for rel, declared in last.items():
            p = root / rel
            if p.exists() and hash_file(p) != declared:
                drift += 1
    except HashingUnavailable:
        return -1
    return drift


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="repo root")
    parser.add_argument("--home", default=".ket", help="path to .ket dir")
    parser.add_argument("--name", default=None, help="display name (default: dir name)")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    name = args.name or root.name

    manifest_path = root / "MANIFEST.yml"
    scorecard_n = bare_n = "?"
    if manifest_path.exists() and yaml:
        m = yaml.safe_load(manifest_path.read_text())
        scorecard_n = len(m.get("scorecard") or {})
        bare_n = len(m.get("bare_k1_identities") or {})

    cas_dir = Path(args.home) / "cas"
    log_path = Path(args.home) / "log"
    cas_n, corrupt_n = _cas_counts(cas_dir)
    dirty_n = _git_dirty_count(root)
    drift_n = _drift_count(root, log_path)
    env = environment_summary()

    def fmt(v):
        return "?" if v == -1 else str(v)

    print(
        f"{name}: CAS {cas_n} ({fmt(corrupt_n)} corrupt) | "
        f"scorecard {scorecard_n} + bare_k1 {bare_n} | "
        f"git {dirty_n} dirty | drift {fmt(drift_n)} | env: {env}"
    )

    # Non-zero exit if anything is definitively broken (not unknown).
    if (isinstance(corrupt_n, int) and corrupt_n > 0) or (
        isinstance(drift_n, int) and drift_n > 0
    ):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
