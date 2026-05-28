#!/usr/bin/env python3
"""
engine_mcp.py — minimal MCP server exposing the deterministic engine runner.

Speaks JSON-RPC 2.0 over line-delimited stdin/stdout (the same transport
`ket mcp` uses). Exposes two tools so an LLM/HITL session can run a
framework engine and quote a CID-verified result instead of estimating:

  - list_engines()        -> the registry (name, what it computes, pinned?)
  - run_engine(name)      -> runs a whitelisted engine, seals stdout in the
                             ket CAS, and reports {cid, expect_cid, matches,
                             output}. matches=true means the result is
                             bit-identical to the sealed canonical run.

Register in .mcp.json:
  "engines": { "command": "python3",
               "args": ["scripts/engines/engine_mcp.py"],
               "env": {"KET_HOME": ".ket"} }

This is intentionally tiny and dependency-free (stdlib only); the real
work lives in run_engine.py, which this imports.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run_engine as R  # noqa: E402

PROTOCOL_VERSION = "2024-11-05"
SERVER_INFO = {"name": "harmonics-engines", "version": "0.1.0"}

TOOLS = [
    {
        "name": "list_engines",
        "description": (
            "List the deterministic derivation engines available to run, "
            "with what each computes and whether its canonical output CID "
            "is pinned."
        ),
        "inputSchema": {"type": "object", "properties": {}},
    },
    {
        "name": "run_engine",
        "description": (
            "Run a whitelisted derivation engine and return its result. The "
            "stdout is sealed in the ket CAS and its BLAKE3 CID compared to "
            "the pinned canonical CID: matches=true means the result is "
            "bit-identical to the sealed canonical run (verified, not "
            "estimated). Quote the 'output' field, not a guess."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Engine name (see list_engines).",
                }
            },
            "required": ["name"],
        },
    },
]


def _tool_list_engines() -> dict:
    engines, pins = R.load_registry(), R.load_pins()
    items = [
        {
            "name": n,
            "computes": engines[n].get("computes", ""),
            "pinned": n in pins,
            "expect_cid": pins.get(n),
        }
        for n in sorted(engines)
    ]
    return {"engines": items, "count": len(items)}


def _tool_run_engine(args: dict) -> dict:
    name = (args or {}).get("name")
    if not name:
        return {"error": "missing required argument: name"}
    return R.run_engine(name)


def _dispatch_tool(name: str, args: dict) -> tuple[dict, bool]:
    """Return (result_obj, is_error)."""
    if name == "list_engines":
        return _tool_list_engines(), False
    if name == "run_engine":
        res = _tool_run_engine(args)
        is_err = bool(res.get("error")) or res.get("matches") is False
        return res, is_err
    return {"error": f"unknown tool: {name}"}, True


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
            "content": [{"type": "text", "text": json.dumps(obj, indent=2)}],
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
