#!/usr/bin/env python3
"""Owner action: tombstone deliberately deleted sealed paths.

Canonical interface: `make owner-tombstone PATHS="<p> [p…]" REASON="…"`.
Appends `<ts> | rm | <path> (<reason>)` to .ket/log for each path —
the tombstone grammar in scripts/drift/_ketlog.py — so a DELIBERATE
deletion stops counting as drift while accidental deletions (no
tombstone) still do.

Guards, per path:
  - must currently resolve in the log's last_cid (else nothing sealed
    to tombstone);
  - must NOT exist on disk (tombstoning a live file is a lie);
  - must NOT be in scripts/drift/enforced_paths.txt (enforced paths
    leave the roster first — check_enforced_coverage would go red on a
    tombstoned enforced path, by design);
  - reason must be non-empty and contain no parentheses (the grammar's
    terminator).
"""

import argparse
import datetime
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "drift"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("paths", nargs="+", help="repo-relative sealed paths")
    ap.add_argument("--reason", required=True, help="why (no parentheses)")
    ap.add_argument("--home", default=".ket")
    args = ap.parse_args()

    from _ketlog import read_log, RM_LINE

    reason = args.reason.strip()
    if not reason or "(" in reason or ")" in reason:
        print("ERROR: reason must be non-empty and parenthesis-free")
        return 2

    log_path = ROOT / args.home / "log"
    view = read_log(log_path)
    enforced = set()
    roster = ROOT / "scripts" / "drift" / "enforced_paths.txt"
    if roster.exists():
        enforced = {l.strip() for l in roster.read_text().splitlines()
                    if l.strip()}

    lines = []
    for rel in args.paths:
        if rel not in view.last_cid:
            print(f"ERROR: {rel} has no live seal in the log — nothing to "
                  f"tombstone (already tombstoned, or never put)")
            return 2
        if (ROOT / rel).exists():
            print(f"ERROR: {rel} still exists on disk — delete it first "
                  f"(tombstoning a live file is a lie)")
            return 2
        if rel in enforced:
            print(f"ERROR: {rel} is in enforced_paths.txt — remove it from "
                  f"the roster first")
            return 2
        ts = datetime.datetime.now(datetime.timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%SZ")
        line = f"{ts} | rm | {rel} ({reason})"
        if not RM_LINE.match(line):
            print(f"ERROR: constructed line fails the tombstone grammar: "
                  f"{line!r}")
            return 2
        lines.append(line)

    with open(log_path, "a", encoding="utf-8") as fh:
        for line in lines:
            fh.write(line + "\n")
            print(f"tombstoned: {line}")

    after = read_log(log_path)
    for rel in args.paths:
        if rel in after.last_cid:
            print(f"ERROR: {rel} still resolves after tombstone — "
                  f"grammar mismatch, inspect the log tail")
            return 2
    print(f"\nverified: {len(args.paths)} path(s) cleared from last_cid; "
          f"remember to commit .ket/log")
    return 0


if __name__ == "__main__":
    sys.exit(main())
