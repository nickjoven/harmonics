#!/usr/bin/env python3
"""
Check: enforced-spine coverage (FATAL).

Every path in enforced_paths.txt must (a) exist in the working tree and
(b) have at least one `put` entry in .ket/log. check_working_tree.py
audits drift only for paths that HAVE a log entry, so an enforced path
with no entry at all is invisible to it — and the whole check is
advisory besides.

Born from a real loss (2026-07-29): sync_cost/successions.jsonl — the
koide arc's 13 committed SUCCEEDS declarations, an owner ruling — was
enrolled in enforced_paths.txt, but the commit carrying the file and
its seal (#319) merged into a side branch (provenance-envelope) that
never reached main. For a week, main declared the ledger enforced
while not containing it, and every gate ran green over the absence.
The predicate here is crisp (path exists, log names it) and the error
model is exact, so per the gate ladder this is FATAL from birth.

Exit code: number of enforced paths missing from tree or log.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ENFORCED = Path(__file__).resolve().parent / "enforced_paths.txt"
PUT_LINE = re.compile(
    r"^\S+\s+\|\s+put\s+\|\s+(?P<path>\S[^\n]*?)\s+->\s+[0-9a-f]{64}\s*$"
)


def main() -> int:
    if not ENFORCED.exists():
        print("(no enforced_paths.txt — every put path is enforced; "
              "nothing to cross-check)")
        return 0
    enforced = {
        ln.strip()
        for ln in ENFORCED.read_text().splitlines()
        if ln.strip() and not ln.lstrip().startswith("#")
    }
    log_path = ROOT / ".ket" / "log"
    logged = set()
    malformed = []
    if log_path.exists():
        for n, line in enumerate(log_path.read_text().splitlines(), 1):
            m = PUT_LINE.match(line)
            if m:
                logged.add(m.group("path"))
            elif "| put |" in line:
                # Put-shaped but unparseable — every log READER silently
                # skips such a line, so without this branch a corrupted
                # entry simply vanishes from enforcement. Real case
                # (2026-07-30): `ket put` appends without a trailing-
                # newline guard, so an append onto a no-LF EOF
                # concatenated two entries into one unparseable line,
                # and the sealed path silently left the audited set.
                malformed.append((n, line[:80]))

    absent = sorted(p for p in enforced if not (ROOT / p).exists())
    unsealed = sorted(p for p in enforced - logged if p not in absent)

    if malformed:
        print(f"MALFORMED: {len(malformed)} put-shaped log line(s) no "
              f"reader can parse")
        for n, frag in malformed:
            print(f"  .ket/log:{n}: {frag}")
        print("  (likely a concatenated append onto a no-newline EOF — "
              "split the entries; see ket newline-guard issue)")
    if not absent and not unsealed and not malformed:
        print(f"OK: all {len(enforced)} enforced paths exist and are sealed")
        return 0
    if absent:
        print(f"MISSING from working tree: {len(absent)} enforced path(s)")
        for p in absent:
            print(f"  {p}")
        print("  (an enforced path that is gone is a loss, not drift — "
              "recover it or deliberately retire it from the spine)")
    if unsealed:
        print(f"NEVER SEALED: {len(unsealed)} enforced path(s) with no "
              f"`put` entry in .ket/log")
        for p in unsealed:
            print(f"  {p}")
        print("  (seal via `KET_HOME=.ket ket put <path>`)")
    return len(absent) + len(unsealed) + len(malformed)


if __name__ == "__main__":
    sys.exit(main())
