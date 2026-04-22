#!/usr/bin/env python3
"""
Tool #1: Bulk CAS verification.

Walks .ket/cas/, recomputes the BLAKE3 hash of each blob, compares it
to the filename (which is the declared CID). Exits 1 if any file is
CORRUPTED (hash mismatch).

This would have caught the SHA-256 retraction entries
(`8e23247fd488`, `ba196964d683`) at commit time on 2026-04-22.

Run:
  python3 scripts/drift/verify_cas.py
  python3 scripts/drift/verify_cas.py --home path/to/.ket
"""

import argparse
import sys
from pathlib import Path

from _hash import hash_file, HashingUnavailable, environment_summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--home", default=".ket", help="path to .ket dir")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    cas = Path(args.home) / "cas"
    if not cas.is_dir():
        print(f"error: {cas} is not a directory", file=sys.stderr)
        return 2

    try:
        entries = sorted(cas.iterdir())
        corrupt = []
        for entry in entries:
            declared = entry.name
            actual = hash_file(entry)
            if declared != actual:
                corrupt.append((declared, actual))
    except HashingUnavailable as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    if corrupt:
        print(f"CORRUPTED: {len(corrupt)} of {len(entries)} CAS entries")
        for declared, actual in corrupt:
            print(f"  declared {declared[:12]}  actual {actual[:12]}")
        return 1

    if not args.quiet:
        print(f"OK: {len(entries)} CAS entries verified ({environment_summary()})")
    return 0


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).parent))
    sys.exit(main())
