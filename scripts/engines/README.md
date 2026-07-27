# scripts/engines/ — deterministic engine runner

The framework's derivation scripts are **engines**: pure, deterministic
computations whose stdout is a *result*. An LLM/HITL session should quote
those results **from a real run**, not estimate them — an LLM eyeballing
`7^(5/2) = 129.6` vs `206.8` and calling it "close" is the failure mode
this directory removes.

## What it does

`run_engine.py run` executes a **whitelisted** engine and **verifies**
its result: it computes the stdout's BLAKE3 CID and compares it to a
**pinned canonical CID**. A match proves the result is bit-identical to
the sealed canonical run — *run the code AND verify it didn't drift from
canonical.* That is what removes the ambiguity.

`run` is **read-only by default** (#328 Card 10: checking never
mutates): it writes nothing — no CAS write, no ledger line. Sealing is
explicit: `run --seal` seals the stdout in the ket CAS, and `pin` always
seals internally (a pin without a sealed canonical is meaningless).

`pin` also records the BLAKE3 of the engine's **script file** in the
lock; the FATAL drift check `scripts/drift/check_engine_pins.py`
(#328 Card 5) re-hashes those scripts on every commit — without running
any engine — and fails if a pinned engine's script changed since pin
time. Remedy: review the change, then `run_engine.py pin <name>`.

## Files

| File | Role |
|---|---|
| `engines.yaml` | human-authored registry: `cmd`, `computes`, `timeout` |
| `engines.lock.json` | generated lock, written only by `pin`: `pins` (`name -> canonical expect_cid`) + `scripts` (`name -> BLAKE3 of engine script at pin time`) |
| `run_engine.py` | CLI: `list` / `run [--seal]` / `info` / `pin` |
| `engine_mcp.py` | minimal MCP server exposing `list_engines` / `run_engine` |

## Usage

```sh
python3 scripts/engines/run_engine.py list
python3 scripts/engines/run_engine.py run koide_closure_check           # verify-only
python3 scripts/engines/run_engine.py run koide_closure_check --json
python3 scripts/engines/run_engine.py run koide_closure_check --seal    # also seal in CAS
python3 scripts/engines/run_engine.py pin --all      # set/refresh canonical CIDs (seals)
```

`run` exits `0` on match (or unpinned), `1` on **DRIFT** (CID ≠ pin —
the engine's output changed from canonical), `2` on engine/env error.

## As an MCP tool

`.mcp.json` registers the `engines` server; on session reload an agent
gets `list_engines` and `run_engine`. `run_engine(name)` returns
`{cid, expect_cid, matches, output, ...}`; `matches=true` means
recomputed-and-identical to the pinned canonical. The MCP tool is
verify-only: it never writes (no CAS entry, no ledger line).

## Adding an engine

1. Confirm the script's stdout is **deterministic** (run twice, compare —
   no timestamps, no absolute paths, no figure-path prints).
2. Add an entry to `engines.yaml` with an honest `computes` (several
   engines are NULL/decline results — that is the point, not a defect).
3. `python3 scripts/engines/run_engine.py pin <name>` to record its CID.

## Why this is drift-gate-safe

Verification (`run` without `--seal`) touches nothing, so there is
nothing to enroll. When sealing IS requested (`run --seal`, `pin`), the
runner seals via `ket put -` (stdin), which logs with path `-`;
`scripts/drift/check_working_tree.py` explicitly ignores stdin puts, so
sealing engine results never enrolls anything in the working-tree drift
gate. The canonical pin lives in `engines.lock.json` (git-tracked), not
the substrate log. Hashing uses the canonical BLAKE3 path
(`scripts/drift/_hash.py`) — never SHA-*.
