"""
build_derivation_graph.py

Extract the dependency graph from sync_cost/derivations/*.md and emit
JSON suitable for the interactive graph viewer at docs/dag.html.

The graph has one node per .md file.  Edges represent cross-references
(file A mentions file B via an inline link or bare filename reference).
Per-node metadata includes:

  - id             : the filename stem
  - path           : relative path to the file
  - title          : first heading, if present
  - summary        : first meaningful paragraph (or status note) if present
  - depends_on     : list of ids this file references
  - depended_on_by : reverse edges (filled in after scan)
  - git            : list of commits touching this file (hash, date, subject)

Output: docs/derivation-graph.json
"""

import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DERIV_DIR = ROOT / "sync_cost" / "derivations"
OUT_PATH = ROOT / "docs" / "derivation-graph.json"

# Scan all .md files (not the scratch directory)
md_files = [
    f for f in DERIV_DIR.glob("*.md")
    if f.name not in {"README.md"}
]


def extract_title(text: str) -> str:
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    return m.group(1).strip() if m else ""


def extract_summary(text: str) -> str:
    """Find first paragraph after a heading that isn't itself a heading."""
    # Skip past the first H1
    parts = re.split(r"^#\s+.*$", text, maxsplit=1, flags=re.MULTILINE)
    body = parts[1] if len(parts) > 1 else text
    # Look for a summary-like section first
    for heading in ["Summary", "Claim", "Theorem", "Status"]:
        m = re.search(
            rf"^##\s+{heading}\s*\n+(.+?)(?=\n##|\Z)",
            body,
            re.MULTILINE | re.DOTALL,
        )
        if m:
            text_block = m.group(1).strip()
            # Take first paragraph
            first_para = text_block.split("\n\n")[0].strip()
            if first_para:
                return first_para[:500]  # cap length
    # Fallback: first non-empty paragraph
    for para in body.split("\n\n"):
        p = para.strip()
        if p and not p.startswith("#") and not p.startswith("*") and len(p) > 40:
            return p[:500]
    return ""


def extract_references(text: str, all_ids: set) -> list:
    """Find other derivation files referenced by this one."""
    refs = set()
    for mid in all_ids:
        # Match the filename in code spans, inline references, or as bare word
        patterns = [
            rf"`{mid}\.md`",
            rf"`{mid}\.py`",
            rf"\[[^\]]*\]\({mid}\.md\)",
            rf"\(`{mid}\.md`\)",
            rf"\b{mid}\.md\b",
        ]
        for pat in patterns:
            if re.search(pat, text):
                refs.add(mid)
                break
    return sorted(refs)


def git_log(path: Path) -> list:
    """Return list of commits touching this file."""
    rel = path.relative_to(ROOT)
    try:
        result = subprocess.run(
            [
                "git",
                "log",
                "--follow",
                "--format=%h|%ai|%s",
                "--",
                str(rel),
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=10,
        )
        commits = []
        for line in result.stdout.strip().splitlines():
            parts = line.split("|", 2)
            if len(parts) == 3:
                commits.append({
                    "hash": parts[0],
                    "date": parts[1][:10],  # YYYY-MM-DD only
                    "subject": parts[2][:100],
                })
        return commits
    except Exception:
        return []


def main():
    all_ids = {f.stem for f in md_files}
    nodes = {}

    for f in md_files:
        text = f.read_text(errors="replace")
        node_id = f.stem
        nodes[node_id] = {
            "id": node_id,
            "path": str(f.relative_to(ROOT)),
            "title": extract_title(text),
            "summary": extract_summary(text),
            "depends_on": extract_references(text, all_ids - {node_id}),
            "depended_on_by": [],
            "git": git_log(f),
        }

    # Reverse edges
    for node_id, node in nodes.items():
        for dep in node["depends_on"]:
            if dep in nodes:
                nodes[dep]["depended_on_by"].append(node_id)

    # Sort reverse edges for stability
    for node in nodes.values():
        node["depended_on_by"].sort()

    # Emit
    OUT_PATH.parent.mkdir(exist_ok=True)
    out = {
        "generated": subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=ROOT, capture_output=True, text=True
        ).stdout.strip(),
        "nodes": sorted(nodes.values(), key=lambda n: n["id"]),
    }
    OUT_PATH.write_text(json.dumps(out, indent=2))
    print(f"Wrote {len(nodes)} nodes to {OUT_PATH}")
    # Report stats
    edge_count = sum(len(n["depends_on"]) for n in nodes.values())
    roots = [n["id"] for n in nodes.values() if not n["depends_on"]]
    leaves = [n["id"] for n in nodes.values() if not n["depended_on_by"]]
    print(f"  {edge_count} edges")
    print(f"  {len(roots)} roots: {', '.join(roots[:10])}{'...' if len(roots) > 10 else ''}")
    print(f"  {len(leaves)} leaves")


if __name__ == "__main__":
    main()
