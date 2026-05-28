# scripts/engines/ — deterministic engine runner

The framework's derivation scripts are **engines**: pure, deterministic
computations whose stdout is a *result*. An LLM/HITL session should quote
those results **from a real run**, not estimate them — an LLM eyeballing
`7^(5/2) = 129.6` vs `206.8` and calling it "close" is the failure mode
this directory removes.

## What it does

`run_engine.py` runs a **whitelisted** engine, seals its stdout in the
ket CAS (content-addressed, dedup-free), and compares the result's BLAKE3
CID to a **pinned canonical CID**. A match proves the result is
bit-identical to the sealed canonical run — *run the code AND verify it
didn't drift from canonical.* That is what removes the ambiguity.

## Files

| File | Role |
|---|---|
| `engines.yaml` | human-authored registry: `cmd`, `computes`, `timeout` |
| `engines.lock.json` | generated pins: `name -> canonical expect_cid` |
| `run_engine.py` | CLI: `list` / `run` / `info` / `pin` |
| `engine_mcp.py` | minimal MCP server exposing `list_engines` / `run_engine` |

## Usage

```sh
python3 scripts/engines/run_engine.py list
python3 scripts/engines/run_engine.py run koide_closure_check
python3 scripts/engines/run_engine.py run koide_closure_check --json
python3 scripts/engines/run_engine.py pin --all      # set/refresh canonical CIDs
```

`run` exits `0` on match (or unpinned), `1` on **DRIFT** (CID ≠ pin —
the engine's output changed from canonical), `2` on engine/env error.

## As an MCP tool

`.mcp.json` registers the `engines` server; on session reload an agent
gets `list_engines` and `run_engine`. `run_engine(name)` returns
`{cid, expect_cid, matches, output, ...}`; `matches=true` ⇒ verified.

## Adding an engine

1. Confirm the script's stdout is **deterministic** (run twice, compare —
   no timestamps, no absolute paths, no figure-path prints).
2. Add an entry to `engines.yaml` with an honest `computes` (several
   engines are NULL/decline results — that is the point, not a defect).
3. `python3 scripts/engines/run_engine.py pin <name>` to record its CID.

## Why this is drift-gate-safe

The runner seals output via `ket put -` (stdin), which logs with path
`-`. `scripts/drift/check_working_tree.py` explicitly ignores stdin puts,
so sealing engine results never enrolls anything in the drift gate. The
canonical pin lives in `engines.lock.json` (git-tracked), not the
substrate log. Hashing uses the canonical BLAKE3 path
(`scripts/drift/_hash.py`) — never SHA-*.
