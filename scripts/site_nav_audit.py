#!/usr/bin/env python3
"""
Tool: docs-site navigation audit (issue #297 follow-up).

Answers "is the site a navigable tree?" mechanically: inventories the
root index.html plus every docs/*.html, extracts <nav> links and body
links, walks reachability, and reports the pages a visitor cannot reach
by clicking — nav-orphans (reachable only through prose links) and full
orphans (reachable only by knowing the URL).

Nav-reachability is walked from docs/index.html, the hub page carrying
the canonical nav (the root index.html is a landing page with no <nav>
by design). Body-reachability is walked from the root.

Exit code = number of FULLY orphaned pages (advisory; a WIP viewer may
be deliberately unlinked).

Run:
  python3 scripts/site_nav_audit.py           # full report
  python3 scripts/site_nav_audit.py --list    # one page per line (for make)
"""

import argparse
import re
import sys
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NAV_RE = re.compile(r"<nav[^>]*>(.*?)</nav>", re.S | re.I)
A_RE = re.compile(r'<a\s+href="([^"#?]+\.html)"', re.I)


def inventory() -> dict:
    pages = {}
    for p in [ROOT / "index.html"] + sorted((ROOT / "docs").glob("*.html")):
        text = p.read_text(errors="replace")
        nav_html = " ".join(NAV_RE.findall(text))

        def resolve(links):
            out = set()
            for link in links:
                if link.startswith(("http:", "https:")):
                    continue
                target = (p.parent / link).resolve()
                try:
                    out.add(str(target.relative_to(ROOT)))
                except ValueError:
                    pass
            return out

        pages[str(p.relative_to(ROOT))] = {
            "nav": resolve(A_RE.findall(nav_html)),
            "all": resolve(A_RE.findall(text)),
        }
    return pages


def reachable(pages: dict, start: str, key: str) -> set:
    seen, queue = {start}, deque([start])
    while queue:
        for nxt in pages.get(queue.popleft(), {}).get(key, ()):
            if nxt in pages and nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return seen


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", action="store_true",
                        help="print one page path per line and exit 0")
    args = parser.parse_args()

    pages = inventory()
    if args.list:
        for p in sorted(pages):
            print(p)
        return 0

    nav_seen = reachable(pages, "docs/index.html", "nav")
    body_seen = reachable(pages, "index.html", "all")
    nav_orphans = sorted(set(pages) - nav_seen - {"index.html"})
    full_orphans = sorted(set(pages) - body_seen)

    print(f"pages: {len(pages)} "
          f"(nav-reachable from docs/index.html: {len(nav_seen)}, "
          f"link-reachable from root: {len(body_seen)})")
    if nav_orphans:
        print("\nnot reachable through <nav> alone:")
        for p in nav_orphans:
            tag = "FULL ORPHAN — no inbound link anywhere" \
                if p in full_orphans else "prose/body links only"
            print(f"  {p:42s} {tag}")
    missing_nav = sorted(p for p, v in pages.items()
                         if not v["nav"] and p != "index.html")
    if missing_nav:
        print("\npages with no <nav> element (root index excluded by design):")
        for p in missing_nav:
            print(f"  {p}")
    if not nav_orphans and not missing_nav:
        print("site is a fully navigable tree")
    return len(full_orphans)


if __name__ == "__main__":
    sys.exit(main())
