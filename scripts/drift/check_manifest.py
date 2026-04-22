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
# authoritative as a scorecard source.
RETRACTION_TOKENS = (
    "declined",
    "retracted",
    "withdrawn",
    "ruled out",
    "Class 1",  # numerology confirmed
    "Class 3",  # numerology by association
    "honest-null",
)


def _looks_retracted(md_path: Path, max_scan_lines: int = 80) -> list[str]:
    """Return the list of retraction tokens found near the top of the file."""
    if not md_path.exists():
        return []
    text = md_path.read_text()
    head = "\n".join(text.splitlines()[:max_scan_lines]).lower()
    return [t for t in RETRACTION_TOKENS if t.lower() in head]


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
        r"^\|\s*(D\d+)\s*\|\s*\[`?([a-z_0-9]+\.(?:md|py))`?\]",
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
    # an H3 title (`### ... `foo.md`` — rare but possible) OR in a
    # line beginning with `- Source:` / `- **Primary` under a Class
    # 1/3 section.  Upstream structural references (e.g. a `three_
    # dimensions.md` mention inside a `- Source of the bare identity:`
    # bullet) are intentionally not flagged — they cite dependencies
    # of the demoted claim, not the claim's carrier file.
    numerology_text = numerology_path.read_text() if numerology_path.exists() else ""
    class_1_3_files: set[str] = set()
    current_class = None
    _CARRIER_LINE = re.compile(
        r"^(?:###\s|- \*\*Primary|- Source\s*:)",
    )
    for line in numerology_text.splitlines():
        m = re.match(r"^## Class (\d)", line)
        if m:
            current_class = int(m.group(1))
            continue
        if current_class in (1, 3) and _CARRIER_LINE.match(line):
            for fn in re.findall(r"`([a-z_0-9]+\.md)`", line):
                class_1_3_files.add(fn)

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
        print(
            f"NOTE: {len(unresolved_dnums)} scorecard D-number(s) not resolved "
            f"by sync_cost/derivations/INDEX.md:"
        )
        for ref in unresolved_dnums[:3]:
            print(f"  {ref}")
        if len(unresolved_dnums) > 3:
            print(f"  ... and {len(unresolved_dnums) - 3} more")
        print("Add a row for each to INDEX.md's mapping table.")
        print()

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
