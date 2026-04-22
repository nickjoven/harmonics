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


def _resolve_source(name: str, deriv_dir: Path) -> Path | None:
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
    # D-numbers: D25, D33, etc. We'd need INDEX.md to resolve these.
    # For now, flag as unresolved.
    if re.match(r"^D\d+$", name):
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

    # Load numerology classifications so we can cross-check.
    numerology_text = numerology_path.read_text() if numerology_path.exists() else ""
    class_1_3_files: set[str] = set()
    current_class = None
    for line in numerology_text.splitlines():
        m = re.match(r"^## Class (\d)", line)
        if m:
            current_class = int(m.group(1))
            continue
        if current_class in (1, 3):
            for fn in re.findall(r"`([a-z_0-9]+\.md)`", line):
                class_1_3_files.add(fn)

    violations: list[str] = []
    d_number_refs: list[str] = []
    for entry_key, entry in scorecard.items():
        sources = entry.get("source") or []
        if not isinstance(sources, list):
            violations.append(f"{entry_key}: source is not a list")
            continue
        for s in sources:
            if re.match(r"^D\d+$", s):
                d_number_refs.append(f"{entry_key}: '{s}'")
                continue  # separate bucket; known-limitation
            resolved = _resolve_source(s, deriv_dir)
            if resolved is None:
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

    if d_number_refs:
        # Known limitation: no INDEX.md exists to map D-numbers to
        # files. Report separately, do not fail the check on these.
        print(
            f"NOTE: {len(d_number_refs)} scorecard source(s) use D-numbers "
            f"but no INDEX.md exists to resolve them:"
        )
        for ref in d_number_refs:
            print(f"  {ref}")
        print("Consider creating sync_cost/derivations/INDEX.md with a")
        print("D-number → filename mapping, or replace D-numbers with filenames.")
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
