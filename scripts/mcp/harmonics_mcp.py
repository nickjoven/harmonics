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
import re
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


SUCCESSIONS_LEDGER = ROOT / "sync_cost" / "successions.jsonl"


def _corpus_index() -> dict:
    """Docs projection with the quantum-declaration ledger overlaid.

    The overlay gives read-your-write: a succession declared this
    session is visible to resolve/doc_get/search immediately, without
    waiting for the CI index regen (canon.d#11 commitment 8)."""
    if "docs_overlaid" not in _cache:
        docs = {k: dict(v)
                for k, v in _load_json("docs/corpus-index.json")["docs"].items()}
        if SUCCESSIONS_LEDGER.exists():
            for line in SUCCESSIONS_LEDGER.read_text().splitlines():
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if rec.get("kind") != "SUCCEEDS":
                    continue
                new = rec.get("new")
                new = new if isinstance(new, list) else [new]
                targets = list(dict.fromkeys(
                    t for t in new if t in docs and t != rec.get("old")))
                if rec.get("old") in docs and targets:
                    docs[rec["old"]]["superseded_by"] = targets
                    docs[rec["old"]]["superseded_basis"] = "quantum"
        _cache["docs_overlaid"] = docs
    return _cache["docs_overlaid"]


def _frontier_head(doc_id: str) -> tuple:
    """Follow the succession chain. Returns (heads, chain).

    `superseded_by` is a LIST (a doc may be displaced by several
    successors jointly, e.g. f2_scoping). Single-successor links are
    followed transitively; a multi-successor link ends the chain with
    all successors as heads. Cycle-safe. Succession is harvested from
    self-declarations only (RULES 0-8, adjudicated 2026-07-21; the
    interim for sealed SUCCEEDS quanta, canon.d#6/#11)."""
    index = _corpus_index()

    def walk(doc, seen):
        if doc in seen:
            return [], [doc]  # cycle: no resolvable head (review finding 6)
        meta = index.get(doc, {})
        if "superseded_by" not in meta:
            return [doc], []
        seen = seen | {doc}
        heads, chain = [], [doc]
        for s in meta["superseded_by"]:
            if s not in index:
                if s not in heads:
                    heads.append(s)
                continue
            h, c = walk(s, seen)  # successors resolve recursively
            heads += [x for x in h if x not in heads]
            chain += [x for x in c if x not in chain]
        return heads, chain

    return walk(doc_id, frozenset())


def _is_frontier(doc_id: str) -> bool:
    return "superseded_by" not in _corpus_index().get(doc_id, {})


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
            # Section-style statuses ('## Status' + bold verdict) have
            # status_line: null and live in status_bold — the entire
            # quantum-superseded koide family reads blank without it
            # (review 2026-07-30).
            "status_bold": meta.get("status_bold"),
            "d_numbers": meta["d_numbers"],
        })
        if "superseded_by" in meta:
            heads, chain = _frontier_head(doc_id)
            out["superseded_by"] = meta["superseded_by"]
            out["superseded_basis"] = meta.get("superseded_basis")
            out["frontier_heads"] = heads
            out["frontier_note"] = (
                "this doc is NOT on the frontier; the current head(s) of "
                f"this line of work: {heads}. "
                "Do not assert this doc's status claims as current."
            )
    return out


def _tool_doc_search(args: dict) -> dict:
    query = ((args or {}).get("query") or "").lower()
    klass = (args or {}).get("class")
    historical = bool((args or {}).get("historical"))
    if not query and klass is None:
        return {"error": "provide query and/or class"}
    index = _corpus_index()
    hits, hidden = [], 0
    for doc_id, node in _graph_nodes().items():
        meta = index.get(doc_id, {})
        if klass is not None and int(klass) not in meta.get("classes", []):
            continue
        hay = f"{doc_id} {node['title']} {node['summary']}".lower()
        if query and query not in hay:
            continue
        if "superseded_by" in meta and not historical:
            hidden += 1
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
            "truncated": len(hits) > 25,
            "superseded_hidden": hidden,
            "note": ("frontier view; pass historical=true to include "
                     "superseded docs") if hidden else None}


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
    historical = bool((args or {}).get("historical"))
    hits, hidden = [], 0
    for doc_id, meta in sorted(_corpus_index().items()):
        if klass is not None and int(klass) not in meta["classes"]:
            continue
        if coverage is not None and meta["coverage"] != coverage:
            continue
        if "superseded_by" in meta and not historical:
            hidden += 1
            continue
        hits.append({"id": doc_id, "title": meta["title"],
                     "classes": meta["classes"],
                     "status_line": meta["status_line"]})
    return {"count": len(hits), "hits": hits, "superseded_hidden": hidden}


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


def _dnumber_to_doc() -> dict:
    """Reverse map D-number -> doc stem, from the corpus index."""
    if "dnum_map" not in _cache:
        _cache["dnum_map"] = {
            d: doc_id
            for doc_id, meta in _corpus_index().items()
            for d in meta.get("d_numbers", [])
        }
    return _cache["dnum_map"]


def _resolve_source(src: str) -> dict:
    """Resolve a MANIFEST source token (D-number or stem) to its frontier."""
    doc = _dnumber_to_doc().get(src, src)
    if doc not in _corpus_index():
        return {"source": src, "doc": None, "frontier": None}
    heads, chain = _frontier_head(doc)
    on_frontier = heads == [doc]
    return {"source": src, "doc": doc,
            "frontier": on_frontier,
            "frontier_heads": None if on_frontier else heads}


def _tool_manifest_claim(args: dict) -> dict:
    scorecard = _manifest().get("scorecard", {})
    name = (args or {}).get("name")
    if not name:
        return {"count": len(scorecard), "names": sorted(scorecard)}
    claim = scorecard.get(name)
    if claim is None:
        return {"error": f"unknown scorecard claim: {name!r}"}
    out = {"name": name, **claim}
    sources = claim.get("source")
    if isinstance(sources, list):
        resolved = [_resolve_source(s) for s in sources]
        out["sources_resolved"] = resolved
        stale = [r for r in resolved if r["frontier"] is False]
        if stale:
            out["source_frontier_warning"] = (
                "some sources are superseded docs: "
                + ", ".join(f"{r['doc']} -> {r['frontier_heads']}" for r in stale))
    return out


def _tool_resolve(args: dict) -> dict:
    """Claim-first resolution: the unit of query is the claim, the doc
    is its container (canon.d#11 commitment 1). Docs resolve through
    the succession chain to the frontier head."""
    name = (args or {}).get("name", "")
    if not name:
        return {"error": "provide name (scorecard claim, D-number, or doc stem)"}
    scorecard = _manifest().get("scorecard", {})
    if name in scorecard:
        out = {"kind": "claim", **_tool_manifest_claim({"name": name})}
        # A claim key can shadow a doc stem (spectral_tilt is both). The
        # doc-level supersession must stay reachable through the advertised
        # entry point (review finding 4, 2026-07-21).
        meta = _corpus_index().get(name)
        if meta and "superseded_by" in meta:
            heads, chain = _frontier_head(name)
            out["doc_view"] = {
                "doc": name, "frontier": False,
                "superseded_by": meta["superseded_by"],
                "frontier_heads": heads,
                "warning": (f"the DOC named {name!r} is superseded "
                            f"(heads: {heads}); the claim row above is the "
                            "current claim state — do not read the doc's "
                            "content as current"),
            }
        return out
    doc = _dnumber_to_doc().get(name, name)
    index = _corpus_index()
    if doc not in index:
        return {"error": f"unresolvable: {name!r} is neither a scorecard "
                         f"claim, a D-number, nor a doc stem"}
    heads, chain = _frontier_head(doc)
    on_frontier = heads == [doc]
    out = {"kind": "doc", "input": name, "doc": doc,
           "frontier_heads": heads, "frontier": on_frontier}
    if chain:
        out["chain"] = chain + heads
        out["basis"] = index[chain[0]].get("superseded_basis")
    if len(heads) == 1:
        head_meta = index.get(heads[0], {})
        # status_line falls back to status_bold: section-style statuses
        # have no inline line, and a null here on exactly the frontier
        # head the caller asked about is information loss (review
        # 2026-07-30).
        out["head_status_line"] = (head_meta.get("status_line")
                                   or head_meta.get("status_bold"))
        out["head_classes"] = head_meta.get("classes")
    return out


def _tool_claim_search(args: dict) -> dict:
    """Search the sealed-claims projection (clean ingest, 2026-07-22):
    quantitative propositions keyed by content address, with
    frontier-split corroboration. Cite the proposition_cid in
    discussion — it is stable across sessions and reformattings."""
    query = ((args or {}).get("subject") or "").lower()
    min_corr = int((args or {}).get("min_corroboration") or 0)
    claims = _load_json("docs/claims-index.json")["claims"]
    hits = []
    for cid, c in claims.items():
        if query and query not in (c.get("subject") or "").lower():
            continue
        if c["corroboration"] < min_corr:
            continue
        hits.append({
            "proposition_cid": cid,
            "subject": c["subject"],
            "witness": c["witness"],
            # succession-chain-deduped (#328 Card 2): drafts are not
            # independent witnesses; corroboration_docs is the raw count.
            "corroboration": c["corroboration"],
            "corroboration_docs": c.get("corroboration_docs",
                                        c["corroboration"]),
            "corroboration_frontier": c["corroboration_frontier"],
        })
    hits.sort(key=lambda h: -h["corroboration_frontier"])
    out = {"count": len(hits), "hits": hits[:25],
           "truncated": len(hits) > 25}
    stale = _claims_staleness_note()
    if stale:
        out["staleness_note"] = stale
    return out


def _claims_staleness_note():
    """The claims layer has no read-your-write overlay (its frontier
    fields bake in at generation), so a succession declared this
    session is visible in doc_get/resolve but not here until CI
    regenerates — say so instead of silently disagreeing with the
    doc-side tools (review 2026-07-30)."""
    try:
        ci = ROOT / "docs" / "claims-index.json"
        if (SUCCESSIONS_LEDGER.exists() and ci.exists()
                and SUCCESSIONS_LEDGER.stat().st_mtime > ci.stat().st_mtime):
            return ("successions have been declared since this projection "
                    "was generated; frontier/corroboration fields may lag "
                    "until CI regenerates (doc_get/resolve are live)")
    except OSError:
        pass
    return None


def _tool_claim_get(args: dict) -> dict:
    """Fetch one sealed claim by proposition CID (prefix ok): the full
    support record, frontier docs first."""
    cid = (args or {}).get("cid", "")
    claims = _load_json("docs/claims-index.json")["claims"]
    matches = [k for k in claims if k.startswith(cid)] if cid else []
    if len(matches) != 1:
        return {"error": f"{len(matches)} claims match prefix {cid!r}"}
    full = matches[0]
    out = {"proposition_cid": full, **claims[full]}
    out["superseded_supporters"] = [
        d["doc"] for d in out["docs"] if not d["frontier"]]
    stale = _claims_staleness_note()
    if stale:
        out["staleness_note"] = stale
    return out


def _tool_declare_succession(args: dict) -> dict:
    """The first write-path tool (canon.d#11 commitment 8): declare a
    supersession as one sealed ledger record. Envelope (agent, time)
    is auto-stamped; the doc's content is never touched. The banner a
    reader sees is a projection from this record, not stored prose."""
    import datetime
    import os
    old = (args or {}).get("old", "")
    new = (args or {}).get("new")
    reason = (args or {}).get("reason", "")
    if isinstance(new, str):
        new = [new]
    new = list(dict.fromkeys(new or []))  # order-preserving dedup
    # Validate against the LIVE ledger, not this session's cached overlay
    # (TOCTOU: another session may have declared since our first read).
    _cache.pop("docs_overlaid", None)
    index = _corpus_index()
    if old not in index:
        return {"error": f"unknown doc: {old!r}"}
    if not new or any(t not in index for t in new):
        return {"error": f"unknown successor(s): {new!r}"}
    # Disk must agree with the index: the FATAL ledger validator
    # (check_successions) checks sync_cost/derivations/<id>.md existence,
    # and the ledger is append-only, so writing a record the validator
    # rejects would be a permanent red (review 2026-07-30 — the two
    # tools validated against different universes).
    missing = [d for d in [old, *new]
               if not (ROOT / "sync_cost" / "derivations" / f"{d}.md").exists()]
    if missing:
        return {"error": f"doc(s) in the index but not on disk (stale "
                         f"index?): {missing!r} — refusing a record the "
                         f"ledger validator would permanently reject"}
    if old in new:
        return {"error": "a doc cannot succeed itself"}
    warnings = []
    for t in new:
        heads, chain = _frontier_head(t)
        if old in chain or old in heads:
            return {"error": f"cycle: {t!r} already resolves through {old!r}"}
        if heads != [t]:
            warnings.append(f"target {t!r} is itself superseded "
                            f"(heads: {heads}); did you mean the head?")
    previous = index[old].get("superseded_by")
    record = {
        "kind": "SUCCEEDS",
        "old": old,
        "new": new,
        "agent": os.environ.get("HARMONICS_AGENT",
                                os.environ.get("USER", "unknown")) + "@mcp",
        "time": datetime.datetime.now(datetime.timezone.utc)
                .isoformat(timespec="seconds"),
        "modality": "committed",
    }
    if reason:
        record["reason"] = reason
    line = json.dumps(record, ensure_ascii=False) + "\n"
    # Single O_APPEND write + fsync: atomic vs concurrent sessions for
    # normal record sizes; newline-guard heals a crash-truncated tail
    # so a partial line can never merge with this record.
    fd = os.open(SUCCESSIONS_LEDGER, os.O_APPEND | os.O_CREAT | os.O_WRONLY,
                 0o644)
    try:
        if os.fstat(fd).st_size > 0:
            with open(SUCCESSIONS_LEDGER, "rb") as fh:
                fh.seek(-1, 2)
                if fh.read(1) != b"\n":
                    line = "\n" + line
        os.write(fd, line.encode())
        os.fsync(fd)
    finally:
        os.close(fd)
    # Read-your-write must survive any seal failure below.
    _cache.pop("docs_overlaid", None)
    sealed, seal_error = None, None
    if not os.environ.get("HARMONICS_MCP_NO_SEAL"):
        try:
            proc = subprocess.run(
                # KET_BIN honored like every other ket caller in the
                # repo (reconcile_substrate, post_edit_regen); the bare
                # "ket" fallback used to fail on boxes where ket lives
                # only behind KET_BIN (review 2026-07-30).
                [os.environ.get("KET_BIN", "ket"), "put",
                 str(SUCCESSIONS_LEDGER.relative_to(ROOT))],
                capture_output=True, text=True, cwd=str(ROOT),
                env={**os.environ,
                     "KET_HOME": os.environ.get("KET_HOME", ".ket")},
                timeout=60,
            )
            if proc.returncode == 0:
                sealed = proc.stdout.strip()[:64]
            else:
                seal_error = (proc.stderr or proc.stdout).strip()[:200]
        except Exception as ex:
            seal_error = f"{type(ex).__name__}: {ex}"
    out = {"declared": record, "ledger": str(SUCCESSIONS_LEDGER.name),
           "sealed_cid": sealed,
           "note": ("succession is live in this server immediately; the "
                    "committed index projection updates on the next regen")}
    if warnings:
        out["warnings"] = warnings
    if previous:
        out["previous_superseded_by"] = previous
        out["re_declaration"] = True
    if seal_error:
        out["seal_error"] = (seal_error +
                             " — record IS in the ledger; re-seal with "
                             "`ket put sync_cost/successions.jsonl` (the "
                             "enforced-spine gate will block commits until "
                             "sealed)")
    return out


def _tool_corpus_health(args: dict) -> dict:
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts/drift/session_status.py")],
        capture_output=True, text=True, cwd=str(ROOT), timeout=120,
    )
    out = {"status_line": proc.stdout.strip(),
           "exit_code": proc.returncode,
           "stderr": proc.stderr.strip() or None}
    # The claims-layer review queue (#328 follow-through): singleton
    # claims wearing the junk fingerprint, surfaced here so a session
    # sees where review attention belongs without running the suite.
    # The count is parsed from stdout, never taken from the exit code:
    # exit status truncates mod 256, and a crashed check would have
    # masqueraded as "1 flagged claim" (review 2026-07-30).
    try:
        sig = subprocess.run(
            [sys.executable,
             str(ROOT / "scripts/drift/check_claim_signatures.py")],
            capture_output=True, text=True, cwd=str(ROOT), timeout=60,
        )
        lines = sig.stdout.strip().splitlines()
        m = re.match(r"NOTE: (\d+) singleton", lines[0]) if lines else None
        if m:
            queue = {"flagged": int(m.group(1)), "detail": lines[1:]}
        elif lines and lines[0].startswith("OK:"):
            queue = {"flagged": 0, "detail": None}
        else:
            queue = {"flagged": None,
                     "error": (sig.stderr.strip() or sig.stdout.strip()
                               or f"rc {sig.returncode}")[:300]}
    except subprocess.TimeoutExpired:
        queue = {"flagged": None, "error": "signature check timed out"}
    out["claim_review_queue"] = queue
    return out


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
                "historical": {"type": "boolean",
                               "description": "include superseded docs "
                                              "(default false: frontier only)"},
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
                "historical": {"type": "boolean",
                               "description": "include superseded docs "
                                              "(default false: frontier only)"},
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
        "name": "resolve",
        "description": (
            "Resolve a name to the frontier: a scorecard claim returns the "
            "claim row with frontier-resolved sources; a D-number or doc "
            "stem follows the succession chain to the current head. The "
            "claim is the unit of query; the doc is its container. Use "
            "this FIRST when checking what the corpus currently holds on "
            "a topic — it is how you avoid reading a superseded doc as "
            "current."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {"name": {"type": "string",
                                    "description": "claim name, D-number, or doc stem"}},
            "required": ["name"],
        },
    },
    {
        "name": "claim_search",
        "description": (
            "Search the sealed-claims projection: quantitative "
            "propositions from the clean ingest, keyed by content "
            "address. Corroboration counts INDEPENDENT witnesses "
            "(succession chains collapse to one — drafts are not "
            "witnesses); corroboration_docs is the raw doc count, "
            "corroboration_frontier the frontier split. The way to "
            "discuss corpus claims without context rot: cite "
            "proposition CIDs, not remembered prose."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "subject": {"type": "string",
                            "description": "substring over claim subjects"},
                "min_corroboration": {"type": "integer"},
            },
        },
    },
    {
        "name": "claim_get",
        "description": (
            "Fetch one sealed claim by proposition CID (prefix ok): "
            "witness value, routes, and every supporting doc with its "
            "frontier state."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {"cid": {"type": "string"}},
            "required": ["cid"],
        },
    },
    {
        "name": "declare_succession",
        "description": (
            "WRITE: declare that a doc is superseded by one or more "
            "successors, as a sealed envelope-attributed ledger record. "
            "The doc's content is never edited; readers see the "
            "supersession as a computed projection. Use for owner-ratified "
            "successions only — this is a commitment, not a proposal."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "old": {"type": "string", "description": "superseded doc stem"},
                "new": {"type": "array", "items": {"type": "string"},
                        "description": "successor stem(s)"},
                "reason": {"type": "string",
                           "description": "claim-level reason (optional)"},
            },
            "required": ["old", "new"],
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
    "resolve": _tool_resolve,
    "claim_search": _tool_claim_search,
    "claim_get": _tool_claim_get,
    "declare_succession": _tool_declare_succession,
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
