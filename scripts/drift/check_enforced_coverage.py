#!/usr/bin/env python3
"""
Check: enforced-spine coverage AND currency (FATAL).

Every path in enforced_paths.txt must (a) exist in the working tree,
(b) have at least one parseable `put` entry in .ket/log, and (c) hash
to its last-sealed CID. Plus (d): no put-shaped log line may be
unparseable — a malformed line hides entries from EVERY reader, which
is how the 2026-07-30 concatenation corruption survived five of them.

History: born 2026-07-29 from the #319 stranding (an enforced path
lost off main for a week under green gates) covering only (a)+(b).
The 2026-07-30 review then found the spine's core documented
invariant — "an edit that isn't re-`put` blocks a commit" — was
enforced by NO FATAL check anywhere (check_working_tree is advisory),
so (c) moved here: enforced-spine drift now gates. Retrieval-tier
drift stays advisory in check_working_tree, by design.

Exit code: 0 clean, 1 violation(s) — never a count (POSIX truncates
exit status mod 256; 256 violations would read as success).
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _hash import hash_file, HashingUnavailable
from _ketlog import read_log

ROOT = Path(__file__).resolve().parents[2]
ENFORCED = Path(__file__).resolve().parent / "enforced_paths.txt"


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
    view = read_log(log_path) if log_path.exists() else None
    last_cid = view.last_cid if view else {}
    malformed = view.malformed if view else []

    absent = sorted(p for p in enforced if not (ROOT / p).exists())
    unsealed = sorted(p for p in enforced - set(last_cid)
                      if p not in absent)
    drifted = []
    try:
        for p in sorted(enforced - set(absent) - set(unsealed)):
            actual = hash_file(ROOT / p)
            if actual != last_cid[p]:
                drifted.append((p, last_cid[p][:12], actual[:12]))
    except HashingUnavailable as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    if not (absent or unsealed or drifted or malformed):
        print(f"OK: all {len(enforced)} enforced paths exist, are "
              f"sealed, and are current")
        return 0
    if malformed:
        print(f"MALFORMED: {len(malformed)} put-shaped log line(s) no "
              f"reader can parse")
        for n, frag in malformed:
            print(f"  .ket/log:{n}: {frag}")
        print("  (likely a concatenated append onto a no-newline EOF — "
              "split the entries; see ket#18)")
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
    if drifted:
        print(f"DRIFTED: {len(drifted)} enforced path(s) edited without "
              f"re-sealing")
        for p, declared, actual in drifted:
            print(f"  {p}  declared {declared}  actual {actual}")
        print("  (re-seal via `KET_HOME=.ket ket put <path>` — the "
              "spine's core invariant: an un-resealed edit blocks)")
    return 1


if __name__ == "__main__":
    sys.exit(main())
