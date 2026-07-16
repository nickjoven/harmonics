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

Exit code = number of UNEXPECTED full orphans — pages with zero inbound
links that are not allowlisted in DELIBERATE_ORPHANS. Deliberate
orphans (a WIP viewer, a standalone visualization) are recorded there
with reasons and never count against the verdict.

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

# Pages with no inbound link anywhere, unlinked ON PURPOSE (owner
# decision, 2026-07-16). They don't count against the tree verdict;
# a NEW page landing with zero inbound links still does.
DELIBERATE_ORPHANS = {
    "docs/dag2.html": "WIP alternate graph viewer (#255) — unfinished by intent",
    "docs/framework_predictions.html":
        "standalone Tier-1 visualization (#233) — no nav slot by decision",
}


def nav_json_links() -> set:
    """All hrefs nav.js renders, resolved repo-relative, from nav.json."""
    import json
    data = json.loads((ROOT / "docs" / "nav.json").read_text())
    hrefs = [data["home"]["href"]]
    hrefs += [i["href"] for g in data["groups"] for i in g["items"]]
    out = set()
    for href in hrefs:
        out.add(str((ROOT / "docs" / href).resolve().relative_to(ROOT)))
    return out


def inventory() -> dict:
    shared_nav = nav_json_links()
    pages = {}
    for p in [ROOT / "index.html"] + sorted((ROOT / "docs").glob("*.html")):
        text = p.read_text(errors="replace")

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

        if "data-site-nav" in text:
            # nav.js renders this page's nav from nav.json at load time;
            # the static placeholder holds only the no-JS fallback link.
            nav_links = set(shared_nav)
        else:
            nav_links = resolve(A_RE.findall(" ".join(NAV_RE.findall(text))))
        pages[str(p.relative_to(ROOT))] = {
            "nav": nav_links,
            "all": resolve(A_RE.findall(text)) | nav_links,
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

    broken = sorted(t for t in nav_json_links() if not (ROOT / t).exists())
    if broken:
        print("nav.json points at missing files:")
        for t in broken:
            print(f"  {t}")
        return len(broken)

    nav_seen = reachable(pages, "docs/index.html", "nav")
    body_seen = reachable(pages, "index.html", "all")
    nav_orphans = sorted(set(pages) - nav_seen - {"index.html"})
    full_orphans = sorted(set(pages) - body_seen)
    unexpected = [p for p in full_orphans if p not in DELIBERATE_ORPHANS]

    print(f"pages: {len(pages)} "
          f"(nav-reachable from docs/index.html: {len(nav_seen)}, "
          f"link-reachable from root: {len(body_seen)})")
    if nav_orphans:
        print("\nnot reachable through <nav> alone:")
        for p in nav_orphans:
            if p in DELIBERATE_ORPHANS:
                tag = f"deliberate orphan — {DELIBERATE_ORPHANS[p]}"
            elif p in full_orphans:
                tag = "UNEXPECTED ORPHAN — no inbound link anywhere"
            else:
                tag = "prose/body links only"
            print(f"  {p:42s} {tag}")
    if unexpected:
        print(f"\n{len(unexpected)} unexpected orphan(s) — link them or add "
              f"to DELIBERATE_ORPHANS with a reason")
    else:
        print(f"\nsite is a navigable tree "
              f"({len(DELIBERATE_ORPHANS)} deliberate orphans excluded)")
    return len(unexpected)


if __name__ == "__main__":
    sys.exit(main())
