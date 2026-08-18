#!/usr/bin/env python3
"""
Generator: machine-readable corpus index (issue #263 ⓾ / #295 groundwork).

The corpus self-classifies claims Class 1–5 as honor-system inline prose
(see `numerology_inventory.md`), and doc status lives in free-text
`**Status**:` lines. `scripts/drift/lint_class_tags.py` reports the
*coverage gap*; this script goes one step further and projects the tags
themselves — per top-level derivation doc — into a single committed JSON
artifact, so "list all Class-5 claims" is a lookup instead of a 322-file
regex sweep.

Per doc it records:
  title        first `# ` heading
  classes      all Class 1–5 tags found (doc may cite several)
  coverage     classified | unclassified-quantitative | prose-only
               (same taxonomy as lint_class_tags.py)
  status_line  first `**Status**:` line, verbatim (free prose, advisory)
  has_lineage  whether a typed `## Lineage` section exists (issue #300)
  d_numbers    D-numbers mapped to this file by INDEX.md

Like `docs/derivation-graph.json`, the output is a committed projection:
regenerate after corpus edits. Deterministic (sorted) so diffs are stable.

Run:
  python3 scripts/build_corpus_index.py            # writes docs/corpus-index.json
  python3 scripts/build_corpus_index.py --check    # exit 1 if committed file is stale
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

CLASS_RE = re.compile(r"\bClass[ -]?([1-5])\b")
QUANT_RE = re.compile(r"≈|=\s*0\.\d|σ|%")
STATUS_RE = re.compile(r"^\*\*Status\*\*:\s*(.+)$", re.MULTILINE)
LINEAGE_RE = re.compile(r"^## Lineage\s*$", re.MULTILINE)
TITLE_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
# Succession harvest, RULES 0-8 (adjudicated by the canon.d#11 workflow,
# 2026-07-21; nine agents, per-rule corpus evidence on the workflow
# record). SELF-DECLARATION ONLY: an edge doc->target exists only when
# the doc itself declares its supersession, in one of two regions —
# R1, a top-note blockquote before the first '## ' heading whose FIRST
# bold span opens with "Supersed…"; R2, a Status section sentence whose
# segment opens with passive "superseded by". Table rows never trigger
# (registry docs record OTHERS' supersessions). Scope qualifiers veto
# ("superseded in/for …", "value only"): a scoped supersession keeps
# the doc on the frontier. Targets come from doc references in the
# trigger sentence (several coordinated targets each yield an edge);
# fallback, only for a trigger sentence with no reference: a region
# reference tagged '(canonical)' or 'Current value:'. D-number-only
# successors never create edges. Registry-titled docs never self-demote
# silently. Numbered-family adjacency, successor-side statements, and
# REVISED-BY/CORRECTION banners create no edges — the adjudication
# found every such candidate to be parts-of-one-arc or corrections,
# not displacement. The source of record will be sealed SUCCEEDS
# quanta (canon.d#6/#11); this is the projection-level interim.
DOCREF_RE = re.compile(
    r"`([A-Za-z0-9_./-]+)\.md`|\]\(([A-Za-z0-9_./-]+)\.md\)|\[\[([A-Za-z0-9_-]+)\]\]")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*", re.DOTALL)
R1_TRIGGER_RE = re.compile(r"(?i)^\s*supersed")
VETO_RE = re.compile(r"(?i)\bsupersed\w*\s+(?:in|for)\b|\bvalue\s+only\b")
R2_TRIGGER_RE = re.compile(r"(?i)(?:^|[;:])\s*(?:\*\*)?\s*superseded by\b")
STATUS_HEAD_RE = re.compile(r"^(#{2,})\s+Status\b")
REGISTRY_H1_RE = re.compile(
    r"(?i)\b(index|ledger|chronology|glossary|scorecard|status map|atlas|"
    r"cross-reference)\b")
# INDEX.md mapping rows: | D1 | [`born_rule.md`](born_rule.md) | ... |
INDEX_ROW_RE = re.compile(r"^\|\s*(D\d+)\s*\|\s*\[`([^`]+)`\]")

OUT_REL = "docs/corpus-index.json"


def load_dnumbers(deriv: Path) -> dict:
    """filename stem -> [D-numbers], from INDEX.md's mapping table."""
    index = deriv / "INDEX.md"
    stems = {}
    if not index.exists():
        return stems
    for line in index.read_text(errors="replace").splitlines():
        m = INDEX_ROW_RE.match(line)
        if m:
            stems.setdefault(Path(m.group(2)).stem, []).append(m.group(1))
    return stems


def _docrefs(text: str) -> list:
    return [next(g for g in m.groups() if g).split("/")[-1]
            for m in DOCREF_RE.finditer(text)]


def _is_stop(text: str, k: int) -> bool:
    """Sentence terminator: ./!/? NOT followed by an alphanumeric.

    Covers '. ', '.\\n', '.**', '.)', EOF; excludes filename dots
    ('…_reframed.md' continues). Symmetric — used by both scan
    directions (review findings 1 and 2, 2026-07-21)."""
    if text[k] not in ".!?":
        return False
    return k + 1 == len(text) or not (text[k + 1].isalnum() or text[k + 1] == "_")


def _trigger_sentence(text: str, pos: int) -> str:
    """Sentence containing pos, bounded by _is_stop in both directions."""
    end, in_tick = pos, False
    while end < len(text):
        if text[end] == "`":
            in_tick = not in_tick
        elif not in_tick and _is_stop(text, end):
            break
        end += 1
    start = 0
    k = pos - 1
    while k > 0:
        if text[k] == "\n" and text[k - 1] == "\n":
            start = k + 1
            break
        if _is_stop(text, k):
            start = k + 1
            break
        k -= 1
    return text[start:end + 1]


def _drop_table_rows(lines: list) -> list:
    return [l for l in lines if not l.lstrip().startswith("|")]  # RULE 2


# Quantum declarations ledger (canon.d#11 commitment 8): succession
# declared as sealed envelope-attributed records, one JSON object per
# line, never as content edits. Read FIRST; the prose harvest below is
# the legacy importer for pre-quantum declarations. On conflict the
# quantum wins (it is the later, cheaper, attributable act).
SUCCESSIONS_LEDGER = "sync_cost/successions.jsonl"


def load_quantum_successions(root: Path, known: set) -> dict:
    ledger = root / SUCCESSIONS_LEDGER
    if not ledger.exists():
        return {}
    out = {}
    for line in ledger.read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            print(f"  WARNING: unparseable ledger line skipped: {line[:60]}")
            continue
        if rec.get("kind") != "SUCCEEDS":
            continue
        if rec.get("modality") != "committed":
            # `proposed` records are visible in the ledger but do not
            # move the frontier (modality was write-only before this:
            # a proposed record projected as a committed supersession).
            continue
        old = rec.get("old")
        new = rec.get("new")
        new = new if isinstance(new, list) else [new]
        targets = list(dict.fromkeys(
            t for t in new if t in known and t != old))
        if old in known and targets:
            out[old] = {"by": targets, "basis": "quantum"}
    return out


def compute_succession(texts: dict, rule8_flags: list = None) -> dict:
    """{stem: {"by": [targets], "basis": "declared"}} per RULES 0-8."""
    succession = {}
    rule8_flags = rule8_flags if rule8_flags is not None else []
    for stem, text in texts.items():
        lines = text.splitlines()
        first_h2 = next((i for i, l in enumerate(lines)
                         if l.startswith("## ")), len(lines))
        targets = []

        # R1: top-note blockquotes, banner-initial bold, veto-checked
        i = 0
        while i < first_h2:
            if lines[i].startswith(">"):
                j = i
                while j < first_h2 and lines[j].startswith(">"):
                    j += 1
                block = "\n".join(_drop_table_rows(
                    [l[1:].lstrip() for l in lines[i:j]]))
                bold = BOLD_RE.search(block)
                if (bold and R1_TRIGGER_RE.match(bold.group(1))
                        and not VETO_RE.search(bold.group(1))):
                    sent = _trigger_sentence(block, bold.start())
                    found = [t for t in _docrefs(sent) if t != stem]
                    if not found:  # RULE 6 fallback
                        for m in DOCREF_RE.finditer(block):
                            ref = next(g for g in m.groups() if g).split("/")[-1]
                            tail = block[m.end():m.end() + 20]
                            head_ctx = block[max(0, m.start() - 20):m.start()]
                            if "(canonical)" in tail or "Current value:" in head_ctx:
                                found.append(ref)
                    targets += found
                i = j
            else:
                i += 1

        # R2: Status region, passive segment-initial "superseded by"
        for i, l in enumerate(lines):
            m = STATUS_HEAD_RE.match(l)
            if not m:
                continue
            level = len(m.group(1))
            j = i + 1
            while j < len(lines):
                hm = re.match(r"^(#{1,6})\s", lines[j])
                if hm and len(hm.group(1)) <= level:
                    break
                j += 1
            region = "\n".join(_drop_table_rows(lines[i + 1:j]))
            for tm in R2_TRIGGER_RE.finditer(region):
                if VETO_RE.search(_trigger_sentence(region, tm.start())):
                    continue
                sent = _trigger_sentence(region, tm.start())
                targets += [t for t in _docrefs(sent) if t != stem]

        # RULE 7 validity + dedup; RULE 8 registry guard
        seen, valid = set(), []
        for t in targets:
            if t in texts and t != stem and t not in seen:
                seen.add(t)
                valid.append(t)
        if not valid:
            continue
        # RULE 8: only a registry KEYWORD in the H1's leading words marks a
        # registry doc — "Derivation Index" is one, "…from Gaussian Lattice
        # Index" is a math title (review finding 3, 2026-07-21). Suppressed
        # edges are persisted into the JSON as rule8_flags, not just stdout.
        h1 = next((l[2:] for l in lines if l.startswith("# ")), "")
        leading = " ".join(h1.split()[:3])
        if REGISTRY_H1_RE.search(leading):
            rule8_flags.append({"doc": stem, "suppressed_targets": valid,
                                "h1": h1})
            print(f"  WARNING (RULE 8): registry doc {stem!r} self-declares "
                  f"supersession by {valid}; suppressed, review manually")
            continue
        succession[stem] = {"by": valid, "basis": "declared"}
    return succession


def build(root: Path) -> dict:
    deriv = root / "sync_cost" / "derivations"
    dnums = load_dnumbers(deriv)
    texts = {p.stem: p.read_text(errors="replace")
             for p in sorted(deriv.glob("*.md"))}
    rule8_flags = []
    succession = compute_succession(texts, rule8_flags)
    succession.update(load_quantum_successions(root, set(texts)))
    docs = {}
    totals = {"classified": 0, "unclassified-quantitative": 0, "prose-only": 0}
    for p in sorted(deriv.glob("*.md")):
        text = texts[p.stem]
        classes = sorted({int(c) for c in CLASS_RE.findall(text)})
        if classes:
            coverage = "classified"
        elif QUANT_RE.search(text):
            coverage = "unclassified-quantitative"
        else:
            coverage = "prose-only"
        totals[coverage] += 1
        status = STATUS_RE.search(text)
        title = TITLE_RE.search(text)
        # status_bold: the first bold span inside a '## Status' section —
        # docs like coupling_scales carry their status there rather than
        # in an inline '**Status**:' line (review finding 5, 2026-07-21).
        status_bold = None
        s_lines = text.splitlines()
        for i, l in enumerate(s_lines):
            hm = STATUS_HEAD_RE.match(l)
            if hm:
                level = len(hm.group(1))
                j = i + 1
                while j < len(s_lines):
                    nm = re.match(r"^(#{1,6})\s", s_lines[j])
                    if nm and len(nm.group(1)) <= level:
                        break
                    j += 1
                region = "\n".join(_drop_table_rows(s_lines[i + 1:j]))
                bm = BOLD_RE.search(region)
                if bm:
                    status_bold = " ".join(bm.group(1).split())[:200]
                break
        entry = {
            "title": title.group(1).strip() if title else p.stem,
            "classes": classes,
            "coverage": coverage,
            "status_line": status.group(1).strip() if status else None,
            "status_bold": status_bold,
            "has_lineage": bool(LINEAGE_RE.search(text)),
            "d_numbers": dnums.get(p.stem, []),
        }
        if p.stem in succession:
            entry["superseded_by"] = succession[p.stem]["by"]  # list
            entry["superseded_basis"] = succession[p.stem]["basis"]
        docs[p.stem] = entry
    head = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "--short", "HEAD"],
        capture_output=True, text=True,
    ).stdout.strip()
    return {
        "generated": head,
        "generator": "scripts/build_corpus_index.py",
        "count": len(docs),
        "coverage_totals": totals,
        "rule8_flags": rule8_flags,
        "docs": docs,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="repo root")
    parser.add_argument("--check", action="store_true",
                        help="exit 1 if the committed index is stale")
    args = parser.parse_args()
    root = Path(args.root).resolve()

    index = build(root)
    out = root / OUT_REL
    rendered = json.dumps(index, indent=1, ensure_ascii=False, sort_keys=True) + "\n"

    if args.check:
        if not out.exists():
            print(f"STALE: {OUT_REL} missing")
            return 1
        committed = json.loads(out.read_text())
        fresh = json.loads(rendered)
        # compare content, not the generated-at sha
        committed.pop("generated", None), fresh.pop("generated", None)
        if committed != fresh:
            print(f"STALE: {OUT_REL} does not match the corpus — regenerate")
            return 1
        print(f"OK: {OUT_REL} is fresh ({index['count']} docs)")
        return 0

    out.write_text(rendered)
    t = index["coverage_totals"]
    print(f"wrote {OUT_REL}: {index['count']} docs "
          f"(classified {t['classified']}, unclassified-quant "
          f"{t['unclassified-quantitative']}, prose-only {t['prose-only']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
