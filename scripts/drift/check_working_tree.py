#!/usr/bin/env python3
"""
Tool #4: Working-tree drift detector.

Parses .ket/log for `put | <path> -> <cid>` lines. For each declared
path, compares the current file's BLAKE3 to the last-logged CID.
Files that have been edited since their last `put` have drifted.

This is the Python equivalent of `ket drift`. Runs without the ket
binary if the blake3 Python package is installed.

Run:
  python3 scripts/drift/check_working_tree.py
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _hash import hash_file, HashingUnavailable


from _ketlog import read_log  # the one put-line grammar (review 2026-07-30)

# The curated, drift-enforced spine. A path listed here is gated: edits
# that aren't re-`put` block a commit. Everything else put into CAS is
# retrieval-tier — retrievable/verifiable, but not gated (breadth without
# enforcement burden). Absent this file, every put path is enforced.
DEFAULT_ENFORCED = Path(__file__).resolve().parent / "enforced_paths.txt"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="repo root")
    parser.add_argument("--home", default=".ket", help="path to .ket dir")
    parser.add_argument(
        "--enforced",
        default=str(DEFAULT_ENFORCED),
        help="allowlist of drift-enforced paths (one per line); "
        "if absent, all put paths are enforced",
    )
    args = parser.parse_args()
    root = Path(args.root).resolve()
    log_path = Path(args.home) / "log"
    if not log_path.exists():
        print(f"(no log at {log_path}, nothing to check)")
        return 0

    view = read_log(log_path)
    last_cid = view.last_cid
    for n, frag in view.malformed:
        print(f"note: unparseable put-shaped log line {n} "
              f"(gated FATALly by check_enforced_coverage): {frag}")

    if not last_cid:
        print("(log has no `put` entries)")
        return 0

    # Decouple enforcement from retrieval. A path in CAS is *retrievable*;
    # only the curated spine is *drift-enforced*. With an allowlist present,
    # gate ONLY those paths; everything else put into CAS is retrieval-tier
    # (still integrity-checked by verify_cas, but its working-tree content
    # may move without blocking a commit). Absent the allowlist, every put
    # path is enforced — the original behavior, backward compatible.
    enforced_file = Path(args.enforced)
    if enforced_file.exists():
        enforced = {
            ln.strip()
            for ln in enforced_file.read_text().splitlines()
            if ln.strip() and not ln.lstrip().startswith("#")
        }
        enforced_cid = {p: c for p, c in last_cid.items() if p in enforced}
        retrieval_n = len(last_cid) - len(enforced_cid)
    else:
        enforced_cid = last_cid
        retrieval_n = 0

    drifted: list[tuple[str, str, str]] = []
    missing: list[str] = []
    try:
        for rel_path, declared in sorted(enforced_cid.items()):
            abs_path = root / rel_path
            if not abs_path.exists():
                missing.append(rel_path)
                continue
            actual = hash_file(abs_path)
            if actual != declared:
                drifted.append((rel_path, declared, actual))
    except HashingUnavailable as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    if drifted or missing:
        if drifted:
            print(f"Drifted: {len(drifted)} enforced file(s)")
            for rel, declared, actual in drifted:
                print(f"  {rel}")
                print(f"    declared {declared[:12]}  actual {actual[:12]}")
            print()
            print("Re-put these via `ket put <path>` to record the new CID,")
            print("and create a DAG node linking to the prior CID so the")
            print("lineage stays intact.")
        if missing:
            print(f"Missing: {len(missing)} enforced path(s) no longer in tree")
            for rel in missing:
                print(f"  {rel}")
        return 1

    tail = f" ({retrieval_n} retrieval-tier, not gated)" if retrieval_n else ""
    print(
        f"OK: {len(enforced_cid)} enforced paths match their "
        f"last-logged CID{tail}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
