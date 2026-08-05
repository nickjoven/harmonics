#!/usr/bin/env python3
"""
Tool #2: MANIFEST ↔ sources consistency check.

For every scorecard entry in MANIFEST.yml with a `source: [...]` list:
  (a) each source file exists under sync_cost/derivations/ (with
      .md or .py extension, or a D-number like D25 mapped via INDEX);
  (b) the source file is not classified Class 1 or Class 3 in
      numerology_inventory.md;
  (c) the source markdown's Status / top section does not contain
      tokens like "declined", "retracted", "withdrawn", "ruled out".

Exits 1 if any violation. This would have surfaced the pre-honest-null
contradiction between MANIFEST.scorecard.weinberg_angle (listed as a
prediction) and numerology_inventory.md §Class 1 (classified as
numerology) on commit #0.

Run:
  python3 scripts/drift/check_manifest.py
"""

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("error: pyyaml required. pip install --user pyyaml", file=sys.stderr)
    sys.exit(2)


# Tokens in a markdown's leading lines that signal it's no longer
# authoritative as a scorecard source. Class tags are matched as
# regexes because the corpus's accepted spellings include "Class-1"
# (lint_class_tags's grammar); a plain substring missed the hyphenated
# form (review 2026-07-30).
RETRACTION_TOKENS = (
    "declined",
    "retracted",
    "withdrawn",
    "ruled out",
    "honest-null",
)
RETRACTION_RES = (
    re.compile(r"\bClass[ -]?1\b"),  # numerology confirmed
    re.compile(r"\bClass[ -]?3\b"),  # numerology by association
)


def _looks_retracted(md_path: Path, max_scan_lines: int = 80) -> list[str]:
    """Return the list of retraction tokens found near the top of the file."""
    if not md_path.exists():
        return []
    text = md_path.read_text()
    head_raw = "\n".join(text.splitlines()[:max_scan_lines])
    head = head_raw.lower()
    hits = [t for t in RETRACTION_TOKENS if t.lower() in head]
    hits += [r.pattern for r in RETRACTION_RES if r.search(head_raw)]
    return hits


def _load_index(deriv_dir: Path) -> dict[str, str]:
    """Parse sync_cost/derivations/INDEX.md for D-number → filename
    mappings.  Matches table rows whose first column is a `Dn` token
    and whose second column contains a `[file.md](file.md)` link.
    Tolerant: any row that doesn't match is silently ignored.

    Returns a dict like {"D25": "farey_partition.md", ...}."""
    index_path = deriv_dir / "INDEX.md"
    if not index_path.exists():
        return {}
    text = index_path.read_text()
    mapping: dict[str, str] = {}
    row_re = re.compile(
        r"^\|\s*(D\d+)\s*\|\s*\[`?([A-Za-z_0-9]+\.(?:md|py))`?\]",
        re.MULTILINE,
    )
    for dnum, fname in row_re.findall(text):
        # Last occurrence wins, in the rare case of duplicates.
        mapping[dnum] = fname
    return mapping


def _resolve_source(
    name: str,
    deriv_dir: Path,
    d_index: dict[str, str] | None = None,
) -> Path | None:
    """Resolve a source string like 'D25' or 'farey_partition' or
    'farey_partition.md' to a concrete file under deriv_dir. Returns
    None if unresolvable (a violation)."""
    if name.endswith(".md") or name.endswith(".py"):
        candidate = deriv_dir / name
        return candidate if candidate.exists() else None
    # Try bare name with .md or .py
    for ext in (".md", ".py"):
        candidate = deriv_dir / f"{name}{ext}"
        if candidate.exists():
            return candidate
    # D-numbers: resolve via INDEX.md if available.
    if re.match(r"^D\d+$", name):
        if d_index and name in d_index:
            candidate = deriv_dir / d_index[name]
            return candidate if candidate.exists() else None
        return None
    return None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="repo root")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    manifest_path = root / "MANIFEST.yml"
    deriv_dir = root / "sync_cost" / "derivations"
    numerology_path = deriv_dir / "numerology_inventory.md"

    if not manifest_path.exists():
        print(f"error: {manifest_path} not found", file=sys.stderr)
        return 2

    manifest = yaml.safe_load(manifest_path.read_text())
    scorecard = manifest.get("scorecard", {})
    # Cross-repo references are valid per the federation model
    # (`CLAUDE.md` §Federation). Names listed under `repos:` resolve
    # to sibling repositories, not files under this repo's
    # sync_cost/derivations/.
    known_repos = set((manifest.get("repos") or {}).keys())

    # Load numerology classifications so we can cross-check.  Narrow
    # sweep: we only flag a file as Class 1/3 if its name appears in
    # an H3 title OR in a *carrier bullet* under a Class 1/3 section.
    # Carrier bullets are `- Source:` / `- **Primary` / the live
    # convention `- Bare K=1 identity: ... from `foo.md``.  Upstream
    # structural references (e.g. a mention inside a `- Source of the
    # bare identity:` bullet) are intentionally not flagged — they
    # cite dependencies of the demoted claim, not the claim's carrier
    # file.
    #
    # Corrected 2026-08-04: the original matcher required the `.md`
    # name on the SAME line as the bullet head, but the inventory
    # wraps bullets — filenames sit on indented continuation lines —
    # so extraction returned the empty set on every revision of the
    # file that has ever existed, and this branch had never fired.
    # Bullets are now joined into logical lines before matching, and
    # an empty extraction in the presence of Class 1/3 sections is an
    # error rather than a silent pass.
    numerology_text = numerology_path.read_text() if numerology_path.exists() else ""
    class_1_3_files: set[str] = set()
    current_class = None
    saw_class_1_3 = False
    _CARRIER_HEAD = re.compile(
        r"^(?:- \*\*Primary|- Source\s*:|- Bare K=1 identity)",
    )
    # Join wrapped bullets: a line starting with whitespace continues
    # the previous logical line.
    logical: list[tuple[int, str]] = []  # (class, joined text)
    for line in numerology_text.splitlines():
        m = re.match(r"^## Class (\d)", line)
        if m:
            current_class = int(m.group(1))
            if current_class in (1, 3):
                saw_class_1_3 = True
            continue
        if current_class not in (1, 3):
            continue
        if line.startswith("###"):
            logical.append((current_class, line))
        elif line.startswith("- "):
            logical.append((current_class, line))
        elif line[:1].isspace() and line.strip() and logical:
            cls, prev = logical[-1]
            logical[-1] = (cls, prev + " " + line.strip())
    for _cls, text_line in logical:
        if text_line.startswith("###") or _CARRIER_HEAD.match(text_line):
            for fn in re.findall(r"`([A-Za-z_0-9]+\.md)`", text_line):
                class_1_3_files.add(fn)
    if saw_class_1_3 and not class_1_3_files:
        print(
            "error: numerology_inventory.md has Class 1/3 sections but "
            "the carrier extractor matched no files — the extractor is "
            "stale against the inventory's format and every Class-1/3 "
            "check below would silently pass",
            file=sys.stderr,
        )
        return 2

    d_index = _load_index(deriv_dir)

    violations: list[str] = []
    unresolved_dnums: list[str] = []
    cross_repo_refs: list[str] = []
    for entry_key, entry in scorecard.items():
        sources = entry.get("source") or []
        if not isinstance(sources, list):
            violations.append(f"{entry_key}: source is not a list")
            continue
        for s in sources:
            if s in known_repos:
                cross_repo_refs.append(f"{entry_key}: '{s}' (federated repo)")
                continue
            resolved = _resolve_source(s, deriv_dir, d_index=d_index)
            if resolved is None:
                if re.match(r"^D\d+$", s):
                    unresolved_dnums.append(f"{entry_key}: '{s}' (not in INDEX.md)")
                else:
                    violations.append(f"{entry_key}: source '{s}' unresolved under {deriv_dir}")
                continue
            if resolved.name in class_1_3_files:
                violations.append(
                    f"{entry_key}: source '{resolved.name}' is classified "
                    f"Class 1 or Class 3 in numerology_inventory.md"
                )
            tokens = _looks_retracted(resolved)
            if tokens:
                violations.append(
                    f"{entry_key}: source '{resolved.name}' has retraction "
                    f"tokens near top: {tokens}"
                )

    if unresolved_dnums:
        # A violation, not a NOTE (review 2026-07-30): most scorecard
        # rows are D-only, so an unresolved D-number silently exempts
        # the row from every Class-1/3 and retraction check — an
        # INDEX.md table reformat could recreate the founding
        # weinberg-class failure with all gates green.
        for ref in unresolved_dnums:
            violations.append(
                f"{ref}: scorecard D-number unresolved by "
                f"sync_cost/derivations/INDEX.md — the row is invisible "
                f"to the Class-1/3 and retraction checks until mapped"
            )

    if cross_repo_refs:
        print(f"NOTE: {len(cross_repo_refs)} cross-repo source(s) (federation):")
        for ref in cross_repo_refs:
            print(f"  {ref}")
        print()

    if violations:
        print(f"MANIFEST inconsistencies: {len(violations)}")
        for v in violations:
            print(f"  - {v}")
        return 1

    print(f"OK: {len(scorecard)} scorecard entries consistent with their sources")
    return 0


if __name__ == "__main__":
    sys.exit(main())
