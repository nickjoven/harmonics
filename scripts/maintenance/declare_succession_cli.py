#!/usr/bin/env python3
"""Owner action: declare one committed SUCCEEDS record.

Canonical interface: `make owner-succession OLD=<doc> NEW="<doc> [doc…]"
REASON="…"`. Runs the same code path as the MCP declare_succession tool
(validate -> atomic append -> ket put reseal of the enforced ledger).
"""

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "mcp"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("old", help="doc id being superseded (stem, no .md)")
    ap.add_argument("new", nargs="+", help="successor doc id(s)")
    ap.add_argument("--reason", default="", help="one-line why")
    args = ap.parse_args()

    import harmonics_mcp as mcp
    out = mcp._tool_declare_succession(
        {"old": args.old, "new": args.new, "reason": args.reason})
    if "error" in out:
        print(f"ERROR: {out['error']}")
        return 2
    print(f"declared: {args.old} -> {args.new}")
    print(f"sealed_cid: {out.get('sealed_cid')}")
    for w in out.get("warnings", []):
        print(f"warning: {w}")
    print("remember to commit: sync_cost/successions.jsonl and .ket; then "
          "regenerate docs/corpus-index.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
