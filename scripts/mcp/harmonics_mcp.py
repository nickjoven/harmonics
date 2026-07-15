#!/usr/bin/env python3
"""
harmonics_mcp.py — MCP server over the derivation corpus.

Speaks JSON-RPC 2.0 over line-delimited stdin/stdout, same transport and
idiom as `scripts/engines/engine_mcp.py`. Where that server *runs* the
deterministic engines, this one *queries* the corpus projections, so a
session can answer "what depends on born_rule", "list Class-5 claims",
or "is the corpus healthy" from the committed artifacts instead of a
322-file sweep or a cache guess.

Read surfaces (all committed projections; see each generator):
  docs/derivation-graph.json   scripts/build_derivation_graph.py (CI-regen)
  docs/corpus-index.json       scripts/build_corpus_index.py
  docs/spine-data.json         scripts/build_spine_data.py
  MANIFEST.yml                 hand-curated source of truth for numbers
  scripts/drift/*.py           health gates (subprocess, read-only)

Register in .mcp.json:
  "harmonics": { "command": "python3",
                 "args": ["scripts/mcp/harmonics_mcp.py"],
                 "env": {"KET_HOME": ".ket"} }

Stdlib + PyYAML only (PyYAML is already a repo dependency via
build_spine_data.py). Artifacts are loaded lazily and cached per-process;
the server is per-session, so staleness tracks the working tree.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

PROTOCOL_VERSION = "2024-11-05"
SERVER_INFO = {"name": "harmonics-corpus", "version": "0.1.0"}

_cache: dict = {}


def _load_json(rel: str):
    if rel not in _cache:
        _cache[rel] = json.loads((ROOT / rel).read_text())
    return _cache[rel]


def _graph_nodes() -> dict:
    if "graph_by_id" not in _cache:
        g = _load_json("docs/derivation-graph.json")
        _cache["graph_by_id"] = {n["id"]: n for n in g["nodes"]}
    return _cache["graph_by_id"]


def _corpus_index() -> dict:
    return _load_json("docs/corpus-index.json")["docs"]


def _manifest() -> dict:
    if "manifest" not in _cache:
        import yaml
        _cache["manifest"] = yaml.safe_load((ROOT / "MANIFEST.yml").read_text())
    return _cache["manifest"]


# ---------------------------------------------------------------- tools

def _tool_doc_get(args: dict) -> dict:
    doc_id = (args or {}).get("id", "")
    node = _graph_nodes().get(doc_id)
    meta = _corpus_index().get(doc_id)
    if node is None and meta is None:
        return {"error": f"unknown doc id: {doc_id!r} (try doc_search)"}
    out = {"id": doc_id}
    if node:
        out.update({
            "path": node["path"],
            "title": node["title"],
            "summary": node["summary"],
            "cid": node["cid"],
            "sealed": node["sealed"],
            "depends_on": node["depends_on"],
            "depended_on_by": node["depended_on_by"],
            "typed_edges": [e for e in node["edges"] if e["kind"] != "references"],
            "last_commit": node["git"][0] if node.get("git") else None,
        })
    if meta:
        out.update({
            "classes": meta["classes"],
            "coverage": meta["coverage"],
            "status_line": meta["status_line"],
            "d_numbers": meta["d_numbers"],
        })
    return out


def _tool_doc_search(args: dict) -> dict:
    query = ((args or {}).get("query") or "").lower()
    klass = (args or {}).get("class")
    if not query and klass is None:
        return {"error": "provide query and/or class"}
    index = _corpus_index()
    hits = []
    for doc_id, node in _graph_nodes().items():
        meta = index.get(doc_id, {})
        if klass is not None and int(klass) not in meta.get("classes", []):
            continue
        hay = f"{doc_id} {node['title']} {node['summary']}".lower()
        if query and query not in hay:
            continue
        hits.append({
            "id": doc_id,
            "title": node["title"],
            "classes": meta.get("classes", []),
            "sealed": node["sealed"],
        })
    hits.sort(key=lambda h: (query not in h["id"].lower(), h["id"]) if query
              else (0, h["id"]))
    return {"count": len(hits), "hits": hits[:25],
            "truncated": len(hits) > 25}


def _tool_graph_walk(args: dict) -> dict:
    doc_id = (args or {}).get("id", "")
    direction = (args or {}).get("direction", "dependents")
    depth = min(int((args or {}).get("depth", 2)), 6)
    nodes = _graph_nodes()
    if doc_id not in nodes:
        return {"error": f"unknown doc id: {doc_id!r}"}
    key = {"deps": "depends_on", "dependents": "depended_on_by"}.get(direction)
    if key is None:
        return {"error": "direction must be 'deps' or 'dependents'"}
    seen, frontier, levels = {doc_id}, [doc_id], []
    for _ in range(depth):
        nxt = sorted({t for f in frontier for t in nodes[f][key]
                      if t in nodes and t not in seen})
        if not nxt:
            break
        levels.append(nxt)
        seen.update(nxt)
        frontier = nxt
    return {"id": doc_id, "direction": direction, "depth": len(levels),
            "levels": levels, "total": sum(len(l) for l in levels)}


def _tool_class_query(args: dict) -> dict:
    klass = (args or {}).get("class")
    coverage = (args or {}).get("coverage")
    if klass is None and coverage is None:
        idx = _load_json("docs/corpus-index.json")
        return {"coverage_totals": idx["coverage_totals"],
                "count": idx["count"], "generated": idx["generated"]}
    hits = []
    for doc_id, meta in sorted(_corpus_index().items()):
        if klass is not None and int(klass) not in meta["classes"]:
            continue
        if coverage is not None and meta["coverage"] != coverage:
            continue
        hits.append({"id": doc_id, "title": meta["title"],
                     "classes": meta["classes"],
                     "status_line": meta["status_line"]})
    return {"count": len(hits), "hits": hits}


def _tool_spine_get(args: dict) -> dict:
    data = _load_json("docs/spine-data.json")
    entry_id = (args or {}).get("id")
    if not entry_id:
        return {"count": len(data["entries"]),
                "ids": sorted(data["entries"])}
    entry = data["entries"].get(entry_id)
    if entry is None:
        return {"error": f"unknown spine id: {entry_id!r}"}
    return {"id": entry_id, **entry}


def _tool_manifest_claim(args: dict) -> dict:
    scorecard = _manifest().get("scorecard", {})
    name = (args or {}).get("name")
    if not name:
        return {"count": len(scorecard), "names": sorted(scorecard)}
    claim = scorecard.get(name)
    if claim is None:
        return {"error": f"unknown scorecard claim: {name!r}"}
    return {"name": name, **claim}


def _tool_corpus_health(args: dict) -> dict:
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts/drift/session_status.py")],
        capture_output=True, text=True, cwd=str(ROOT), timeout=120,
    )
    return {"status_line": proc.stdout.strip(),
            "exit_code": proc.returncode,
            "stderr": proc.stderr.strip() or None}


TOOLS = [
    {
        "name": "doc_get",
        "description": (
            "Fetch one derivation doc's full record: title, summary, path, "
            "seal state (cid/sealed), dependencies and dependents, typed "
            "lineage edges, Class 1-5 tags, status line, and D-numbers. "
            "The substrate-backed answer to 'what does the corpus say "
            "about X' — use before asserting a doc's content or status."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {"id": {"type": "string",
                                  "description": "doc id (filename stem), e.g. 'born_rule'"}},
            "required": ["id"],
        },
    },
    {
        "name": "doc_search",
        "description": (
            "Search derivation docs by substring over id/title/summary, "
            "optionally filtered to a numerology class. Returns up to 25 "
            "compact hits."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "case-insensitive substring"},
                "class": {"type": "integer", "minimum": 1, "maximum": 5,
                          "description": "only docs carrying this Class tag"},
            },
        },
    },
    {
        "name": "graph_walk",
        "description": (
            "Walk the derivation graph from a doc: direction 'deps' (what "
            "it builds on) or 'dependents' (what builds on it), breadth-"
            "first to a depth (default 2, max 6). Returns one list per level."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "direction": {"type": "string", "enum": ["deps", "dependents"]},
                "depth": {"type": "integer", "minimum": 1, "maximum": 6},
            },
            "required": ["id"],
        },
    },
    {
        "name": "class_query",
        "description": (
            "List docs by numerology class (1-5) and/or coverage category "
            "('classified', 'unclassified-quantitative', 'prose-only'). "
            "With no arguments, returns corpus-wide coverage totals."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "class": {"type": "integer", "minimum": 1, "maximum": 5},
                "coverage": {"type": "string",
                             "enum": ["classified", "unclassified-quantitative",
                                      "prose-only"]},
            },
        },
    },
    {
        "name": "spine_get",
        "description": (
            "Fetch one entry from the epistemic spine (SPINE.yml projection): "
            "kind, source, subject, forms, premises. Without an id, lists "
            "all spine entry ids."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {"id": {"type": "string"}},
        },
    },
    {
        "name": "manifest_claim",
        "description": (
            "Fetch a quantitative scorecard claim from MANIFEST.yml (the "
            "source of truth for numbers): computed vs observed values, "
            "sources, closure status. Without a name, lists claim names. "
            "Use this instead of quoting a number from memory."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {"name": {"type": "string"}},
        },
    },
    {
        "name": "corpus_health",
        "description": (
            "One-line substrate health snapshot (scripts/drift/"
            "session_status.py): CAS size, corrupt entries, drift count, "
            "scorecard counts. Non-clean output means verify before assert."
        ),
        "inputSchema": {"type": "object", "properties": {}},
    },
]

_DISPATCH = {
    "doc_get": _tool_doc_get,
    "doc_search": _tool_doc_search,
    "graph_walk": _tool_graph_walk,
    "class_query": _tool_class_query,
    "spine_get": _tool_spine_get,
    "manifest_claim": _tool_manifest_claim,
    "corpus_health": _tool_corpus_health,
}


def _dispatch_tool(name: str, args: dict) -> tuple[dict, bool]:
    fn = _DISPATCH.get(name)
    if fn is None:
        return {"error": f"unknown tool: {name}"}, True
    res = fn(args)
    return res, bool(res.get("error"))


def _result(id_, payload):
    return {"jsonrpc": "2.0", "id": id_, "result": payload}


def _error(id_, code, message):
    return {"jsonrpc": "2.0", "id": id_, "error": {"code": code, "message": message}}


def handle(msg: dict):
    """Return a response dict, or None for notifications (no id)."""
    method = msg.get("method")
    id_ = msg.get("id")
    is_notification = id_ is None

    if method == "initialize":
        return _result(id_, {
            "protocolVersion": PROTOCOL_VERSION,
            "capabilities": {"tools": {}},
            "serverInfo": SERVER_INFO,
        })
    if method in ("notifications/initialized", "initialized"):
        return None
    if method == "ping":
        return _result(id_, {})
    if method == "tools/list":
        return _result(id_, {"tools": TOOLS})
    if method == "tools/call":
        params = msg.get("params") or {}
        obj, is_err = _dispatch_tool(params.get("name"), params.get("arguments") or {})
        return _result(id_, {
            "content": [{"type": "text", "text": json.dumps(obj, indent=2,
                                                            ensure_ascii=False)}],
            "isError": is_err,
        })
    if is_notification:
        return None
    return _error(id_, -32601, f"method not found: {method}")


def main() -> int:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue
        try:
            resp = handle(msg)
        except Exception as ex:  # never crash the server on one bad call
            resp = _error(msg.get("id"), -32603, f"internal error: {ex}")
        if resp is not None:
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
