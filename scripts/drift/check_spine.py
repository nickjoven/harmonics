#!/usr/bin/env python3
"""
Tool #21: SPINE.yml structural gate + regen-no-diff check.

SPINE.yml is the declarative backbone — each entry is a typed edge
(based-on premises → subject, or subject inherits-from source) carrying
one or more equivalent phrasings.  This gate enforces:

BLOCKING:
  - schema: every entry has id, kind, source, subject, forms (non-empty);
    `based-on` carries non-empty premises[]; `inherits-from` carries
    a non-empty `from`.
  - kind ∈ {based-on, inherits-from}; no unknown kinds.
  - ids are unique and match an identifier shape (`^[A-Za-z][A-Za-z0-9_-]*$`).
    Domain notation — `Lambda`, `K1`, `n_s` — is allowed inside an id.
  - the source document file exists on disk (the part of `source:`
    before any " (section)" parenthetical resolves to a real path).
  - optional `status:` values come from STATUS_VOCAB (the premise-
    ledger vocabulary + open/reference).
  - status propagation across the ledger join: an edge with
    status proven/derived may not rest on a premises[]/from ref that
    resolves to an unsettled premise-ledger anchor (conjectured/
    fitted/conditional) or to an unsettled spine edge (conditional/
    conjectured/fitted/open/reference). Mirrors the PREMISES.md
    propagation rule; strongest allowed is `conditional`.
  - docs/spine-data.json is in sync with SPINE.yml — i.e.
    `python3 scripts/build_spine_data.py --check` returns 0.
  - every form is a non-empty string.

ADVISORY (printed as NOTE, not blocking):
  - entries with only one form — the shake-btn surface hides itself
    for these but the entry is still a valid edge.
  - premises[]/from ids that resolve to neither another SPINE entry
    id nor a premise-ledger `provides:` anchor (check_premises scan)
    — an unregistered external concept, or a typo.
  - a proven/derived edge resting on an UNCLASSIFIED spine edge
    (no status field) — unclassified is not settled; classify the
    upstream edge or weaken the downstream one.

Run:
  python3 scripts/drift/check_spine.py
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("error: pyyaml required. pip install --user pyyaml", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent.parent
SPINE_PATH = ROOT / "SPINE.yml"
BUILD_SCRIPT = ROOT / "scripts" / "build_spine_data.py"

SPINE_ID = re.compile(r"^[A-Za-z][A-Za-z0-9_-]*$")
SOURCE_FILE = re.compile(r"^([^\s(]+)")  # strip everything from first " (" or whitespace

# Optional per-entry `status:` — the premise-ledger vocabulary
# (PREMISES.md) plus `open` and `reference`. Absence means the edge
# is unclassified, not settled; coverage is reported in the OK line.
STATUS_VOCAB = {
    "axiom", "definition", "proven", "derived", "imported",
    "conditional", "conjectured", "fitted", "open", "reference",
}

# Propagation across the join (mirrors PREMISES.md): an edge claiming
# proven/derived may not rest on an unsettled upstream.
STRONG = {"proven", "derived"}
LEDGER_UNSETTLED = {"conjectured", "fitted", "conditional"}
SPINE_UNSETTLED = {"conditional", "conjectured", "fitted", "open", "reference"}


def _resolve_source_path(source: str) -> Path:
    m = SOURCE_FILE.match(source)
    return ROOT / m.group(1) if m else ROOT / source


def main() -> int:
    blocking: list[str] = []
    advisory: list[str] = []

    raw = yaml.safe_load(SPINE_PATH.read_text(encoding="utf-8"))
    if not isinstance(raw, dict) or not isinstance(raw.get("spine"), list):
        print("BLOCK: SPINE.yml: top-level `spine:` list missing")
        return 1

    entries = raw["spine"]
    seen_ids: dict[str, int] = {}
    for i, entry in enumerate(entries):
        loc = f"entry #{i}"
        if not isinstance(entry, dict):
            blocking.append(f"{loc}: not a mapping")
            continue
        eid = entry.get("id")
        if not isinstance(eid, str) or not eid:
            blocking.append(f"{loc}: missing or empty `id`")
            continue
        loc = f"id={eid}"
        if not SPINE_ID.match(eid):
            blocking.append(f"{loc}: id is not kebab-case")
        if eid in seen_ids:
            blocking.append(f"{loc}: duplicate id (also at entry #{seen_ids[eid]})")
        seen_ids[eid] = i

        kind = entry.get("kind")
        if kind not in ("based-on", "inherits-from"):
            blocking.append(f"{loc}: unknown kind `{kind}`")
            continue

        for field in ("source", "subject"):
            if not isinstance(entry.get(field), str) or not entry[field]:
                blocking.append(f"{loc}: missing or empty `{field}`")

        source = entry.get("source", "")
        src_path = _resolve_source_path(source)
        if not src_path.exists():
            blocking.append(
                f"{loc}: source document `{src_path.relative_to(ROOT)}` "
                f"(from `source: {source}`) does not exist"
            )

        status = entry.get("status")
        if status is not None and status not in STATUS_VOCAB:
            blocking.append(
                f"{loc}: status `{status}` not in {sorted(STATUS_VOCAB)}")

        forms = entry.get("forms")
        if not isinstance(forms, list) or not forms:
            blocking.append(f"{loc}: `forms` must be a non-empty list")
        else:
            for j, form in enumerate(forms):
                if not isinstance(form, str) or not form.strip():
                    blocking.append(f"{loc}: forms[{j}] is empty or not a string")
            if len(forms) == 1:
                advisory.append(f"{loc}: only one form (shake-btn surface will hide)")

        if kind == "based-on":
            premises = entry.get("premises")
            if not isinstance(premises, list) or not premises:
                blocking.append(f"{loc}: based-on entry must carry non-empty `premises`")
            else:
                for j, p in enumerate(premises):
                    if not isinstance(p, str) or not p:
                        blocking.append(f"{loc}: premises[{j}] is empty or not a string")
        elif kind == "inherits-from":
            frm = entry.get("from")
            if not isinstance(frm, str) or not frm:
                blocking.append(f"{loc}: inherits-from entry must carry non-empty `from`")

    # Cross-reference: premises/from values resolve against spine ids
    # AND the premise-ledger `provides:` anchors (check_premises scan).
    # Unresolved refs are advisory (unregistered concept or typo);
    # a proven/derived edge resting on an unsettled resolution is
    # BLOCKING (propagation rule across the join).
    import check_premises
    ledger_provides, _, _ = check_premises.scan()
    edge_status = {e["id"]: e.get("status") for e in entries
                   if isinstance(e, dict) and isinstance(e.get("id"), str)}

    for entry in entries:
        if not isinstance(entry, dict):
            continue
        eid = entry.get("id", "?")
        refs: list[tuple[str, str]] = []
        if entry.get("kind") == "based-on":
            for j, p in enumerate(entry.get("premises") or []):
                if isinstance(p, str):
                    refs.append((f"premises[{j}]", p))
        elif entry.get("kind") == "inherits-from":
            frm = entry.get("from")
            if isinstance(frm, str):
                refs.append(("from", frm))
        strong = entry.get("status") in STRONG
        for field, val in refs:
            if not SPINE_ID.match(val):
                continue
            if val in seen_ids:
                upstream = edge_status.get(val)
                if strong and upstream in SPINE_UNSETTLED:
                    blocking.append(
                        f"id={eid}: status={entry['status']} rests on spine "
                        f"edge `{val}` with status={upstream} — strongest "
                        f"allowed is `conditional`")
                elif strong and upstream is None:
                    advisory.append(
                        f"id={eid}: status={entry['status']} rests on "
                        f"UNCLASSIFIED spine edge `{val}` (no status field)")
            elif val in ledger_provides:
                anchor_status = ledger_provides[val][1]
                if strong and anchor_status in LEDGER_UNSETTLED:
                    blocking.append(
                        f"id={eid}: status={entry['status']} rests on ledger "
                        f"anchor `{val}` with status={anchor_status} "
                        f"(provided by {ledger_provides[val][0]}) — strongest "
                        f"allowed is `conditional`")
            else:
                advisory.append(
                    f"id={eid}: {field}=`{val}` resolves to neither a spine "
                    f"id nor a premise-ledger anchor (unregistered concept "
                    f"or typo)"
                )

    # Regen-no-diff: SPINE.yml ↔ docs/spine-data.json must agree.
    r = subprocess.run(
        [sys.executable, str(BUILD_SCRIPT), "--check"],
        capture_output=True, text=True, check=False,
    )
    if r.returncode != 0:
        msg = (r.stdout + r.stderr).strip() or "scripts/build_spine_data.py --check failed"
        blocking.append(f"spine-data.json stale: {msg}")

    if advisory:
        print(f"NOTE: {len(advisory)} advisory finding(s):")
        for a in advisory[:8]:
            print(f"  {a}")
        if len(advisory) > 8:
            print(f"  ... and {len(advisory) - 8} more")
        print()

    if blocking:
        print(f"SPINE.yml inconsistencies (blocking): {len(blocking)}")
        for f in blocking:
            print(f"  - {f}")
        return 1

    statused = sum(1 for e in entries
                   if isinstance(e, dict) and "status" in e)
    print(f"OK: {len(entries)} spine entries; docs/spine-data.json in sync; "
          f"status coverage {statused}/{len(entries)} "
          f"(unstatused = unclassified, not settled)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
