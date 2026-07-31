#!/usr/bin/env python3
"""
Engine pin gate (#328 Card 5, FATAL): a changed engine script
invalidates its pinned output CID.

engines.lock.json records, for every pinned engine, both the canonical
output CID (`pins`) and the BLAKE3 hash of the engine's script file at
pin time (`scripts`). If the script changes, the pin no longer
describes what the script now computes — a session quoting
`matches=true` would be verifying against the wrong canonical. This
check hashes each pinned engine's script file and compares it to the
lock. It executes NO engine (fast: a handful of file hashes), so it is
safe to run on every commit.

Failure = any pinned engine whose script hash is missing from the lock,
disagrees with the current file, or whose script/registry entry cannot
be located. Remedy, after reviewing the script change:

    python3 scripts/engines/run_engine.py pin <name>

Registered as FATAL in scripts/drift/run_all.py (NOT advisory): a stale
pin is a policy violation, not a regenerable artifact.

Exit codes: 0 = all pinned engine scripts match the lock; 1 = stale or
missing entries; 2 = environment error (hashing/registry unavailable).
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(ROOT / "scripts" / "engines"))

from _hash import hash_file, HashingUnavailable  # noqa: E402
import run_engine as R  # noqa: E402


def main() -> int:
    try:
        engines = R.load_registry()
    except SystemExit as ex:
        print(f"engine pin gate: cannot load registry: {ex}", file=sys.stderr)
        return 2
    lock = R.load_lock()
    pins, scripts = lock["pins"], lock["scripts"]
    if not pins:
        # An empty pin set while engines exist is a DISARMED gate, not a
        # clean one: a deleted or key-renamed engines.lock.json used to
        # print "nothing to check" and pass (review 2026-07-30). A repo
        # genuinely without engines still passes.
        if engines:
            print(f"engine pin gate: {len(engines)} engine(s) registered "
                  f"but ZERO pins loaded — engines.lock.json missing, "
                  f"unreadable, or key-renamed. A vanished lock must not "
                  f"read as a pass.")
            return 1
        print("engine pin gate: no engines registered; nothing to check.")
        return 0

    stale: list[tuple[str, str]] = []
    ok = 0
    for name in sorted(pins):
        e = engines.get(name)
        if e is None:
            stale.append((name, "pinned but missing from engines.yaml"))
            continue
        script = R.engine_script(e)
        if script is None:
            stale.append((name, "engine script not found in registry cmd"))
            continue
        try:
            actual = hash_file(script)
        except HashingUnavailable as ex:
            print(f"engine pin gate: {ex}", file=sys.stderr)
            return 2
        expect = scripts.get(name)
        if expect is None:
            stale.append(
                (name, f"no script hash recorded in {R.LOCKFILE.name}"))
        elif actual != expect:
            stale.append(
                (name, f"script drifted since pin: {script.relative_to(ROOT)}"))
        else:
            ok += 1

    if stale:
        print(f"ENGINE PIN GATE: {len(stale)} stale pin(s):")
        for name, why in stale:
            print(f"  - {name}: {why}")
        print(
            "\nA changed engine script invalidates its pinned output CID."
            "\nReview the change, then re-pin:"
            "\n  python3 scripts/engines/run_engine.py pin <name>"
        )
        return 1

    print(f"engine pin gate OK: {ok} pinned engine script(s) match the lock.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
