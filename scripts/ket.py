"""
ket.py — minimal k-stack reader using filesystem CAS directly.

K-stack stores reasoning artifacts in .ket/cas/ as BLAKE3-addressed
files.  Each entry is either:

  - A text blob (observation, claim, derivation excerpt, etc.)
  - A reasoning record: JSON with {kind, parents, output_cid, agent,
    timestamp, meta}

This script reads the CAS without needing the k-stack binary, rebuilds
the manifest, and can emit the graph.  It is designed to degrade
gracefully when the k-stack MCP server is unavailable (cloud Claude
Code environments, CI, etc.), while remaining compatible with k-stack
when it is available.

**Writes go through the `ket` binary.** A previous version of this
script computed CIDs with SHA-256, which silently drifted from the
canonical BLAKE3 used by the substrate: appended entries verified
as CORRUPTED under `ket verify`. Writes (append, dag create) now
shell out to the binary so the single source of hashing truth is the
substrate itself. If the binary is unavailable, `append` raises a
clear error instead of falling back to a wrong hash.

Commands:

  list                      Enumerate all CAS entries with type + preview
  show HASH                 Print a specific CAS entry
  graph                     Build the reasoning DAG, emit as JSON
  manifest                  Rebuild .ket/manifest from CAS contents
  append TYPE < input       Store new text blob; print its CID
                            (TYPE = text | reasoning)
  stats                     Summary: count, size, agents, date range

Integration with the derivation graph:

  The emit-graph mode produces JSON in the same format as
  docs/derivation-graph.json, so docs/dag.html can load both
  layers and show derivations + reasoning artifacts together.
"""

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
KET_DIR = ROOT / ".ket"
CAS_DIR = KET_DIR / "cas"
MANIFEST_PATH = KET_DIR / "manifest"

# The canonical substrate uses BLAKE3. We delegate hashing to the
# `ket` binary so this script cannot silently produce wrong CIDs.
# Resolution order: KET_BIN env var, then `ket` on PATH. No hardcoded
# paths — this script lives inside a repo that gets cloned to different
# machines and checkouts.


def _ket_binary() -> str:
    candidates = [os.environ.get("KET_BIN"), shutil.which("ket")]
    for candidate in candidates:
        if candidate and Path(candidate).is_file() and os.access(candidate, os.X_OK):
            return candidate
    raise RuntimeError(
        "ket binary not found. Set KET_BIN to its absolute path or add "
        "`ket` to PATH. This script refuses to compute CIDs locally to "
        "avoid the SHA-256-vs-BLAKE3 drift that previously corrupted "
        "CAS entries."
    )


def list_cas():
    if not CAS_DIR.exists():
        print("No .ket/cas directory", file=sys.stderr)
        return
    entries = sorted(CAS_DIR.iterdir())
    print(f"{len(entries)} CAS entries in {CAS_DIR}")
    for f in entries:
        data = f.read_bytes()
        kind, preview = classify(data)
        print(f"  {f.name[:12]}  [{kind:10s}]  {preview[:80]}")


def classify(data: bytes):
    """Return (kind, preview) tuple. Kind: 'reasoning' | 'text'."""
    try:
        obj = json.loads(data)
        if isinstance(obj, dict) and "kind" in obj and "parents" in obj:
            preview = f"parents={len(obj.get('parents',[]))} → {obj.get('output_cid','')[:8]} ({obj.get('agent','?')})"
            return obj["kind"], preview
    except (json.JSONDecodeError, UnicodeDecodeError):
        pass
    try:
        text = data.decode("utf-8").strip()
        return "text", text.split("\n")[0]
    except UnicodeDecodeError:
        return "binary", f"<{len(data)} bytes>"


def show(cid: str):
    matches = [f for f in CAS_DIR.iterdir() if f.name.startswith(cid)]
    if not matches:
        print(f"No CAS entry matching {cid}", file=sys.stderr)
        return 1
    if len(matches) > 1:
        print(f"Ambiguous prefix {cid} ({len(matches)} matches)", file=sys.stderr)
        return 1
    data = matches[0].read_bytes()
    print(data.decode("utf-8", errors="replace"))


def build_graph():
    """Walk CAS, resolve reasoning records, emit JSON graph."""
    nodes = {}
    for f in CAS_DIR.iterdir():
        cid = f.name
        data = f.read_bytes()
        try:
            obj = json.loads(data)
            if isinstance(obj, dict) and "kind" in obj and "parents" in obj:
                nodes[cid] = {
                    "id": cid[:12],
                    "full_cid": cid,
                    "kind": obj["kind"],
                    "agent": obj.get("agent", "?"),
                    "timestamp": obj.get("timestamp", ""),
                    "parents": [p[:12] for p in obj.get("parents", [])],
                    "output_cid": obj.get("output_cid", "")[:12],
                    "meta": obj.get("meta", []),
                }
                continue
        except (json.JSONDecodeError, UnicodeDecodeError):
            pass
        # Text blob
        try:
            text = data.decode("utf-8").strip()
            preview = text.split("\n", 1)[0][:140]
        except UnicodeDecodeError:
            preview = f"<{len(data)} bytes>"
        nodes[cid] = {
            "id": cid[:12],
            "full_cid": cid,
            "kind": "text",
            "preview": preview,
            "size": len(data),
            "parents": [],
            "output_cid": None,
        }

    # Resolve output_cid references into "depended_on_by"
    by_full = {n["full_cid"]: n for n in nodes.values()}
    for n in nodes.values():
        n["depends_on"] = []
        n["depended_on_by"] = []
    for n in nodes.values():
        if n["kind"] == "reasoning":
            for p in n["parents"]:
                target = next((x for x in nodes.values() if x["id"] == p), None)
                if target:
                    n["depends_on"].append(target["id"])
                    target["depended_on_by"].append(n["id"])

    return {"nodes": sorted(nodes.values(), key=lambda x: x["id"])}


def emit_graph():
    g = build_graph()
    out_path = ROOT / "docs" / "ket-graph.json"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(g, indent=2))
    print(f"Wrote {len(g['nodes'])} nodes to {out_path}")


def rebuild_manifest():
    """Rebuild .ket/manifest as a directory of type-indexed listings."""
    # k-stack uses 'manifest' as a directory; we lost that.  Rebuild as
    # a JSON file instead (simpler; k-stack can regenerate if installed).
    g = build_graph()
    by_kind = defaultdict(list)
    for n in g["nodes"]:
        by_kind[n["kind"]].append(n["full_cid"])
    manifest = {
        "cas_count": len(g["nodes"]),
        "by_kind": {k: sorted(v) for k, v in by_kind.items()},
    }
    # Replace empty file with JSON manifest
    MANIFEST_PATH.unlink(missing_ok=True)
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2))
    print(f"Wrote {manifest['cas_count']} entries to {MANIFEST_PATH}")
    for k, v in manifest["by_kind"].items():
        print(f"  {k}: {len(v)}")


def append(kind: str):
    """Read stdin and hand it to `ket put` so the CID is BLAKE3.

    `kind` is retained for backward compatibility but is ignored for
    text blobs; reasoning records should be created with
    `ket dag create ... --parent ... --kind reasoning` instead of
    being hand-rolled JSON to stdin, because `dag create` handles the
    parent/output wiring and the log entry atomically.
    """
    data = sys.stdin.buffer.read()
    if kind == "reasoning":
        print(
            "scripts/ket.py no longer accepts hand-rolled reasoning "
            "records. Use: ket dag create <content> --kind reasoning "
            "--parent <cid> [--parent <cid> ...] --agent <name>",
            file=sys.stderr,
        )
        return 1
    try:
        binary = _ket_binary()
    except RuntimeError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    result = subprocess.run(
        [binary, "--home", str(KET_DIR), "put", "-"],
        input=data,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        # Older ket versions may not accept "-" for stdin; fall back
        # to a temp file so behavior is robust across versions.
        import tempfile
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(data)
            tmp_path = tmp.name
        try:
            result = subprocess.run(
                [binary, "--home", str(KET_DIR), "put", tmp_path],
                capture_output=True,
                check=True,
            )
        finally:
            os.unlink(tmp_path)
    # `ket put` prints the CID on stdout
    sys.stdout.write(result.stdout.decode())


def stats():
    g = build_graph()
    nodes = g["nodes"]
    kinds = defaultdict(int)
    agents = defaultdict(int)
    dates = []
    total_size = 0
    for n in nodes:
        kinds[n["kind"]] += 1
        if "agent" in n and n["kind"] == "reasoning":
            agents[n["agent"]] += 1
        if "timestamp" in n and n.get("timestamp"):
            dates.append(n["timestamp"][:10])
        if "size" in n:
            total_size += n.get("size", 0)

    print(f"CAS entries: {len(nodes)}")
    print(f"Total text-blob size: {total_size:,} bytes")
    print(f"By kind:")
    for k, v in sorted(kinds.items()):
        print(f"  {k}: {v}")
    if agents:
        print(f"By agent:")
        for a, v in sorted(agents.items(), key=lambda x: -x[1]):
            print(f"  {a}: {v}")
    if dates:
        print(f"Date range: {min(dates)} to {max(dates)}")

    # Edge stats
    edges = sum(len(n.get("depends_on", [])) for n in nodes)
    roots = [n for n in nodes if not n.get("depends_on")]
    leaves = [n for n in nodes if not n.get("depended_on_by")]
    print(f"Edges: {edges}, roots: {len(roots)}, leaves: {len(leaves)}")


def main():
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    cmd = sys.argv[1]
    if cmd == "list":
        list_cas()
    elif cmd == "show" and len(sys.argv) >= 3:
        return show(sys.argv[2])
    elif cmd == "graph":
        emit_graph()
    elif cmd == "manifest":
        rebuild_manifest()
    elif cmd == "append" and len(sys.argv) >= 3:
        return append(sys.argv[2])
    elif cmd == "stats":
        stats()
    else:
        print(__doc__, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main() or 0)
