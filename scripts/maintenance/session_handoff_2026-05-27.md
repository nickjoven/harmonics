# Session handoff — 2026-05-27 — substrate / ket tooling + physics framework

**Purpose:** a cold-start "where we left off" record so the next LLM/HITL
session resumes without re-deriving context. Human-readable here; also
sealed as a catbus packet (see *Sealing* below). Spans four repos
(`harmonics`, `ket`, `k-stack`, `canon.d`) — all authored by us.

---

## TL;DR

The week's physics content landed and the substrate tooling was audited.
Found and fixed the "lost progress": `.mcp.json` pointed at a `k-stack`
binary that was never installed, so sessions started with **zero** ket
tools. ket was minor-bumped to **0.2.0** (additive; downstreams unaffected).
The bigger thread — making novel content usable in sessions with
*provenance-backed facts* and *runnable deterministic engines* — has a
decided direction (below) but is **not yet built**.

## What was done this session

1. **Clone provenance.** Confirmed `/home/nick/harmonics` is the freshest
   clone (== `origin/main` `3ee5c08`); the other three on disk
   (`code/harmonics`, `handoff/harmonics`, `code/research/harmonics`) are
   stale or already-merged feature branches. `/mnt/wslg/...` is a bind-mount
   of this same checkout, not a copy.
2. **MCP fix.** `.mcp.json` `command: k-stack` → `command: ket, args:[mcp]`
   (KET_HOME=.ket). `k-stack` is a real product (the MCP server) but was
   never built/installed here. The repoint is a **stopgap** — `ket mcp`
   serves 19 tools; the intended server is the `k-stack` binary. *Takes
   effect on next session reload, not mid-session.*
3. **ket 0.2.0.** Branch `bump/ket-0.2.0`, tag `v0.2.0` (`b83a4fb`),
   `CHANGELOG.md` added. `cargo check --workspace --exclude ket-py` clean.
   **Local only — not pushed.**
4. **Downstream all-clear.** #9 (epistemic edge kinds) changed
   `ket-sql/-mcp/-cli/-agent/-opt`, **not** `ket-cas`/`ket-dag`. k-stack &
   canon.d use only `ket-cas`/`ket-dag`; catbus uses `ket-sql::DoltDb::init`
   (unchanged). Verified empirically: **catbus and k-stack both build
   against local ket 0.2.0**. The one breaking signature in #9 (a `ket-sql`
   link fn gained an `edge_kind` param) is called by none of them.

## Key design decisions (the "substrate for LLM sessions" thread)

- **Goal (user's framing):** novel content usable in LLM/HITL sessions with
  *complete confidence of facts* and *use of code/engines where
  deterministic results remove ambiguity*. We own the whole toolchain, so
  building tools is on the table.
- **Engine runner — DECIDED: repo-side runner + registry.** `engines.yaml`
  maps each engine → command + what it computes + canonical output; a thin
  Python runner executes a whitelisted engine, `ket put`s its stdout (result
  becomes content-addressed), pins the expected CID, and is exposed as an MCP
  tool. Turns "run code" into "run code *and verify the result didn't drift
  from canonical*." Not yet built.
- **Facts confidence — the trap:** a CAS gives *integrity* confidence, not
  *truth* confidence. Retrieval MUST surface a claim's **disposition**
  (Class 1–5 / forced / null / declined) or it becomes a confident-wrongness
  amplifier. `negative_results_ledger.md` + `numerology_inventory.md` are the
  disposition source of truth. This is *why* "note anything downgraded" was
  part of the brief — it's the system's safety property, not a side errand.
- **Substrate format — agnostic store, aware interface.** Keep BLAKE3-over-
  bytes universal. The fix for content-type variety is NOT more node fields
  (they'd drift from the bytes); it's: (a) `kind` as a *behavior dispatcher*
  (code→symbol, claim→fetch-disposition, prose→chunk), (b) pluggable
  **projectors** (`blob → units + facets`; CDOM is the prototype for code),
  (c) content-addressed **facets** (esp. claim→disposition) as annotations
  pointing at a CID. ket #9 epistemic edge kinds (`grounds/derives/proposes`)
  is a step toward edge semantics.
- **Repo-now vs ket-general:** for harmonics *now*, two projectors carry the
  value — a claim→disposition facet and a working CDOM. Semantic chunking and
  mixed-doc decomposition are ket-the-general-tool concerns; deferred.
- **CDOM/SQL — deferred (Tier-1).** `.ket/ket.db` not initialized, so
  `ket_query_cdom` fails until code is scanned. Lower priority than
  disposition-aware retrieval + the engine runner.

## This week's downgrades / audits (the original reporting ask)

| Item | Disposition | PR |
|---|---|---|
| N17 D-preservation (station↔epoch map) | **VACUOUS** — not geometrically forced (`geometric_forcing_null.py`) | #169 |
| Mass-function family framing | "tension" → **"domain"** (category/ontology correction) | #170 |
| Tongue-width universal slope | −1.86 was wrong; β multifractal, **δ_FKS ≈ −1.924** | #171 |
| Mass-function baseline width step | **NULL** | #165 |
| Cascade structural gate / K↔energy residual | gate **CLOSED**; residual **stays Class-2** | #163, #164 |
| 26:7:1 charged-fermion hierarchy | conflict reconciled → **Class-1 / Floor** (μ/e `7^(5/2)=129.6` misses 206.8 by 37%; "K→μ running" is an undefined patch) | #173 |
| sin²θ_W via d_eff=80/27 | **NULL** — reclassified *down* from Class 4 | (ledger) |
| Articulation audit + graviton/gluon reframings | overstatements eliminated; reframed | #151 |
| Archive failed/superseded; create negative-results ledger | consolidation | #158 |

## Open questions / next steps

1. **CAS scope (still open).** Which of the 35 new files (20 `.md` + 15 `.py`)
   to `ket put`. Deeper fix flagged: **decouple retrieval-put from
   drift-gated tracked-put** in ket (we own it) so breadth ≠ enforcement
   burden. Until then, every `ket put` enrolls a file in the drift gate.
2. **Build the engine runner** (repo-side registry + output-CID pinning + MCP
   tool).
3. **Build + install the real `k-stack` binary** (0.2.0-compatible) and
   repoint `.mcp.json` back at it.
4. **Disposition-aware retrieval** projector (claim → Class/status facet).
5. Optionally move k-stack's ket rev pin `168c54a → v0.2.0` (cosmetic; needs
   ket pushed first).
6. **Nothing is pushed.** ket `bump/ket-0.2.0` + tag `v0.2.0` are local.

## Repo state at handoff

| Repo | Branch | State |
|---|---|---|
| harmonics | `main` @ `3ee5c08` (== origin) | authoritative `.ket`: CAS 259, drift 0 |
| ket | `bump/ket-0.2.0` @ `b83a4fb`, tag `v0.2.0` | local only, builds clean |
| k-stack | `main` @ `b902cef` | clean; builds vs ket 0.2.0; pins ket rev `168c54a` |
| canon.d | `main` @ `b75a87d` | clean; ket is an optional feature |
| catbus | `main` | clean; builds vs ket 0.2.0 |

## Sealing

This file is sealed as a catbus handoff packet in the isolated handoff
store (`KET_HOME=/home/nick/handoff/.ket`), per the authoritative-store
runbook (don't use the repo's authoritative `.ket` for handoff/scratch).
Retrieve with `catbus --ket-home /home/nick/handoff/.ket list` /
`catbus unpack <cid>`. The git-tracked copy here is the durable anchor.
