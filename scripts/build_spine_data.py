"""
build_spine_data.py

Project SPINE.yml into a browser-consumable JSON artifact at
docs/spine-data.json so docs/genesis.html (and any future Pages
surface) can read alternate phrasings without reproducing them
inline.

SPINE.yml is the canonical document — the declarative backbone of
the framework. This script is a write-through projection: it never
edits SPINE.yml, only derives a cache keyed by entry id.

A companion check in scripts/drift/check_spine.py asserts that the
working tree's spine-data.json matches what this script would emit,
so a SPINE.yml edit without a regen is caught by the precommit /
CI drift gate the same way an un-sealed derivation is.

Output shape:
  {
    "version": 1,
    "entries": {
      "<id>": {
        "kind":     "based-on" | "inherits-from",
        "source":   "<document (section)>",
        "subject":  "<consequent-or-inheritor>",
        "forms":    ["<form 1>", "<form 2>", ...],
        "premises": ["<premise-id>", ...]   // present iff kind == based-on
        "from":     "<source-id>"           // present iff kind == inherits-from
      },
      ...
    }
  }
"""

import json
import sys
from collections import OrderedDict
from pathlib import Path

try:
    import yaml
except ImportError:
    print(
        "build_spine_data.py: PyYAML is required (pip install pyyaml).",
        file=sys.stderr,
    )
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
SPINE_PATH = ROOT / "SPINE.yml"
OUT_PATH = ROOT / "docs" / "spine-data.json"


def build() -> OrderedDict:
    raw = yaml.safe_load(SPINE_PATH.read_text(encoding="utf-8"))
    if not isinstance(raw, dict) or "spine" not in raw:
        raise SystemExit("SPINE.yml: top-level `spine:` list missing")

    entries = OrderedDict()
    for entry in raw["spine"]:
        eid = entry["id"]
        if eid in entries:
            raise SystemExit(f"SPINE.yml: duplicate id `{eid}`")
        kind = entry["kind"]
        record = OrderedDict()
        record["kind"] = kind
        record["source"] = entry["source"]
        record["subject"] = entry["subject"]
        if "status" in entry:
            record["status"] = entry["status"]
        if "status_note" in entry:
            record["status_note"] = entry["status_note"]
        record["forms"] = list(entry["forms"])
        if kind == "based-on":
            record["premises"] = list(entry["premises"])
        elif kind == "inherits-from":
            record["from"] = entry["from"]
        else:
            raise SystemExit(f"SPINE.yml: entry `{eid}` has unknown kind `{kind}`")
        entries[eid] = record

    return OrderedDict([("version", raw.get("version", 1)), ("entries", entries)])


def main() -> int:
    data = build()
    text = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    if "--check" in sys.argv:
        if not OUT_PATH.exists():
            print(f"::error::{OUT_PATH} missing; run scripts/build_spine_data.py")
            return 1
        if OUT_PATH.read_text(encoding="utf-8") != text:
            print(
                f"::error::{OUT_PATH} is stale; "
                f"run scripts/build_spine_data.py and commit the result"
            )
            return 1
        return 0
    OUT_PATH.write_text(text, encoding="utf-8")
    print(f"wrote {OUT_PATH.relative_to(ROOT)} ({len(data['entries'])} entries)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
