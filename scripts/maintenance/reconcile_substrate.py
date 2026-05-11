#!/usr/bin/env python3
"""
reconcile_substrate.py — bot-side substrate drift reconciliation.

When a tracked derivation file is edited (via a normal PR merge) but
no fresh `ket put` is appended to `.ket/log`, drift accumulates. The
session-start hook reports it as `drift N`; the `scripts/drift/
session_status.py` script enumerates which files.

This script closes the gap. For each drifted file:

  1. `ket put <file>`            (re-hash; appends to .ket/log)
  2. `ket dag create "..."        (reconciliation reasoning node,
       --kind reasoning           parented on the most recent
       --agent harmonics-bot      dag:create in the log)
       --parent <prior>`

Run from repo root:
    python3 scripts/maintenance/reconcile_substrate.py

Env: `KET_BIN` points at the ket binary; defaults to `ket` on PATH.

Why this is not a Python reimplementation of `ket put` / `ket dag
create`: per `scripts/ket.py`, a previous SHA-256 reimplementation
silently drifted from the canonical BLAKE3 and produced CORRUPTED
entries under `ket verify`. The single source of hashing truth must
be the binary. This script shells out.

Idempotent: if there's no drift, it does nothing.
"""

import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
KET_DIR = ROOT / ".ket"
LOG = KET_DIR / "log"
KET = os.environ.get("KET_BIN", "ket")

sys.path.insert(0, str(ROOT / "scripts" / "drift"))
from _hash import hash_file, HashingUnavailable  # noqa: E402


PUT = re.compile(
    r"^\S+\s+\|\s+put\s+\|\s+(?P<path>\S[^\n]*?)\s+->\s+(?P<cid>[0-9a-f]{64})\s*$"
)
DAG = re.compile(r"^\S+\s+\|\s+dag:create\s+\|\s+(?P<cid>[0-9a-f]{64})\s*$")


def find_drifted() -> list[tuple[str, str, str]]:
    last_put: dict[str, str] = {}
    for line in LOG.read_text().splitlines():
        m = PUT.match(line)
        if m and m.group("path") != "-":
            last_put[m.group("path")] = m.group("cid")

    drifted = []
    for path, declared in last_put.items():
        p = ROOT / path
        if not p.exists():
            continue
        try:
            actual = hash_file(p)
        except HashingUnavailable:
            print(f"ERROR: blake3 module unavailable", file=sys.stderr)
            sys.exit(2)
        if actual != declared:
            drifted.append((path, declared, actual))
    return drifted


def latest_dag_node() -> str | None:
    for line in reversed(LOG.read_text().splitlines()):
        m = DAG.match(line)
        if m:
            return m.group("cid")
    return None


def _run_ket(*args: str) -> str:
    r = subprocess.run(
        [KET, "--home", str(KET_DIR), *args],
        capture_output=True,
        text=True,
        check=True,
        cwd=ROOT,
    )
    return r.stdout


def reconcile_file(path: str, parent_cid: str) -> str:
    _run_ket("put", path)
    desc = (
        f"bot drift reconciliation: {path} re-hashed after derivation edit"
    )
    out = _run_ket(
        "dag",
        "create",
        desc,
        "--kind",
        "reasoning",
        "--agent",
        "harmonics-bot",
        "--parent",
        parent_cid[:12],
    )
    for line in out.splitlines():
        if line.strip().startswith("Node CID:"):
            return line.split(":", 1)[1].strip()
    raise RuntimeError(f"could not parse Node CID from ket output:\n{out}")


def main() -> int:
    if not LOG.exists():
        print(f"ERROR: {LOG} not found", file=sys.stderr)
        return 2

    drifted = find_drifted()
    if not drifted:
        print("substrate-maintenance: no drift to reconcile")
        return 0

    parent = latest_dag_node()
    if parent is None:
        print(
            "ERROR: no dag:create nodes in .ket/log; cannot parent reconciliation",
            file=sys.stderr,
        )
        return 1

    print(f"substrate-maintenance: reconciling {len(drifted)} drifted file(s)")
    print(f"  initial parent: {parent[:12]}")
    for path, declared, actual in drifted:
        print(f"  {path}")
        print(f"    declared: {declared[:12]}")
        print(f"    actual:   {actual[:12]}")
        parent = reconcile_file(path, parent)
        print(f"    new node: {parent[:12]}")

    print(f"\nsubstrate-maintenance: reconciled {len(drifted)} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
