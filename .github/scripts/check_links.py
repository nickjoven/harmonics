#!/usr/bin/env python3
"""Validate local <a href="..."> targets in HTML files exist.

Usage:
    check_links.py file1.html file2.html ...

For each file, parses href and src attributes and verifies that any
non-external, non-anchor target points at an existing file under
_site/.  External (http/https/mailto/tel/javascript/data/protocol-
relative) links and anchor (#) links are skipped.

Exits 1 if any local link target is missing.

This catches the most common Pages breaker for a docs-heavy repo:
a doc link to a file that got renamed or deleted.  It does not
attempt to follow links transitively -- pass each entry-point file
explicitly.
"""

from __future__ import annotations

import pathlib
import re
import sys

SITE_ROOT = pathlib.Path("_site").resolve()

# Match href="..." and src="..." attributes (single or double quoted).
HREF_PATTERN = re.compile(
    r'(?:href|src)\s*=\s*["\']([^"\'>\s]+)["\']',
    re.IGNORECASE,
)

EXTERNAL_PREFIXES: tuple[str, ...] = (
    "http://",
    "https://",
    "mailto:",
    "tel:",
    "javascript:",
    "data:",
    "//",          # protocol-relative
)


def check_file(path: pathlib.Path) -> list[str]:
    """Return a list of missing-target strings for one HTML file."""
    if not path.exists():
        return [f"{path}: file does not exist"]

    text = path.read_text(encoding="utf-8", errors="replace")
    missing: list[str] = []

    for match in HREF_PATTERN.finditer(text):
        href = match.group(1).strip()
        if not href or href.startswith("#") or href.startswith(EXTERNAL_PREFIXES):
            continue

        # Strip query and fragment
        target_str = href.split("?", 1)[0].split("#", 1)[0]
        if not target_str:
            continue

        target = (path.parent / target_str).resolve()

        # Ignore targets outside _site/ (defensive: shouldn't normally happen)
        try:
            target.relative_to(SITE_ROOT)
        except ValueError:
            continue

        if not target.exists():
            missing.append(f"{path.name}: -> {href}  (resolved: {target.relative_to(SITE_ROOT)})")

    return missing


def main() -> int:
    files = [pathlib.Path(p) for p in sys.argv[1:]]
    if not files:
        print("usage: check_links.py file1.html [file2.html ...]", file=sys.stderr)
        return 2

    if not SITE_ROOT.exists():
        print(
            f"ERROR: {SITE_ROOT} does not exist "
            "(expected after the Assemble _site step)",
            file=sys.stderr,
        )
        return 2

    all_missing: list[str] = []
    for f in files:
        all_missing.extend(check_file(f))

    if all_missing:
        print(f"::error::{len(all_missing)} broken local link(s) found:")
        for line in all_missing:
            print(f"  {line}")
        return 1

    print(f"OK: checked {len(files)} file(s), no broken local links")
    return 0


if __name__ == "__main__":
    sys.exit(main())
