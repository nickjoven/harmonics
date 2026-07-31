# Anti-drift tooling

The drift-check suite: every check that makes substrate drift loud at
the earliest moment (the current roster is the table below and
run_all.py's CHECKS list — the two are kept in step).
Each is a standalone Python script; exit codes mean `0 = clean`,
`1 = violation(s) to fix`, `2 = environment error` (missing tool).

Motivation: the commits leading up to `681a726` show two classes of
silent drift that the scorecard/MANIFEST/numerology-inventory all
carried for weeks —
(1) `scripts/ket.py` was hashing with SHA-256 while the substrate
used BLAKE3, so CAS entries were unverifiable; and
(2) MANIFEST listed `weinberg_angle` as a scorecard prediction while
`numerology_inventory.md` classified the same claim as Class 1
numerology. Neither surfaced until someone asked.

The tools below catch those classes mechanically.

## Environment

| Environment | Reads | Writes |
|---|---|---|
| Python only (claude.ai web) | all tools read | need `blake3` package or `ket` binary |
| `pip install --user blake3` | full parity | compute CIDs locally; log updates need binary |
| `ket` binary on `PATH` / `KET_BIN` | canonical | canonical (updates `.ket/log`) |

The `blake3` Python package produces bit-identical CIDs to the `ket`
binary (verified 2026-04-22). Set `KET_BIN=/path/to/ket` to use a
specific binary; otherwise the tools fall back to `shutil.which("ket")`.

## The checks

| # | Script | What it catches |
|---|---|---|
| 1 | `verify_cas.py` | CAS entries whose filename disagrees with the BLAKE3 of their content (bit-rot or algorithm drift). |
| 2 | `check_manifest.py` | Scorecard entries whose sources are unresolvable, Class 1/3 numerology, or marked retracted/declined. |
| 3 | `lint_local_hashing.py` | `hashlib.sha256/sha1/md5` usage under `scripts/`, `.ket/`, `seed/` — the source of the 2026-04-22 corruption. |
| 4 | `check_working_tree.py` | **Enforced-spine** files whose current content no longer matches the last `put | <path> -> <cid>` entry in `.ket/log`. Only paths in `enforced_paths.txt` are gated; see *Enforced vs retrieval* below. |
| 5 | `lint_fitted_corrections.py` | Un-audited additive corrections (`+ 8/F_10²`, `+ 1/228`, `+ 1/q_3²`, …) near bare K=1 identities without a retraction/derivation marker nearby. |
| 6 | `check_graph_orphans.py` | Derivation-graph nodes with zero edges, scorecard sources absent from the graph, and scorecard sources depending on Class 1/3 files. |
| 7 | `session_status.py` | One-line substrate snapshot: CAS count, corrupt count, scorecard/bare_k1 sizes, git dirtiness, drift count. Run at session start. |
| 8 | `check_dag_acyclic.py` | Cycles (strongly-connected components > 1 node) in the derivation `depends_on` graph. **Advisory** — the prose-built graph is cyclic by construction until edges are typed; reports the SCCs as a health signal rather than gating. |
| 9 | `check_graph_sealed.py` | Graph nodes whose source is unsealed (in the graph, absent from `.ket/log`) or **drifted** (sealed but the file changed since its last put). **Advisory** — reports the sealed-projection coverage % as the signal; promote to gating once the corpus is fully sealed. |
| 10 | `check_engine_pins.py` | Engine scripts whose current hash disagrees with `engines.lock.json` — a pinned output CID whose producer changed after pinning (#328 Card 5; the #272 stale-pin failure). |
| 11 | `lint_class_tags.py` | Derivation docs without a self-declared class/status tag. **Advisory** — a coverage signal that self-heals on edit. |
| 12 | `check_corpus_index.py` | `docs/corpus-index.json` stale against the corpus (generator `--check`). **Advisory** — CI-owned projection, regenerated on merge. |
| 13 | `check_claims_index.py` | `docs/claims-index.json` stale against the committed ingest report (generator `--check`). **Advisory** — CI-owned; catches the report and projection moving independently. |
| 14 | `check_nav_orphans.py` | Published pages absent from `docs/nav.json` (minus deliberate orphans). **Advisory**. |
| 15 | `check_downstream_resolution.py` | Committed support edges landing on weak grounds (superseded or self-declared Class 1) while the citing doc still asserts strength (#294). **Advisory** while its false-positive rate accumulates. |
| 16 | `check_retrodiction.py` | Retrodiction regression: the committed-layer divergence machinery must still reproduce the #263 ruling pass's findings from frozen fixtures (4 found, 0 extra — harmonics#314). Deterministic, so FATAL from birth. |
| 17 | `check_enforced_coverage.py` | Enforced paths missing from the working tree, never sealed, or **edited without re-sealing** (currency: the spine's core invariant, FATAL here since 2026-07-31 — check 4 is advisory), plus put-shaped log lines no reader can parse. Born from the #319 stranding; grew currency and the malformed-line gate from the 2026-07-30 review. |
| 18 | `check_claim_signatures.py` | Singleton claims wearing the junk fingerprint (den-1 or decimal-artifact denominators). **Advisory permanently** — known structural false positives (genuine fits rendered decimal); a ranked review queue, never a verdict. |
| 19 | `check_manifest_claims.py` | Mapped MANIFEST scorecard values with no frontier corroboration in the claims projection — the two-records-nobody-joins failure shape, mechanized. **Advisory** during apprenticeship; promotion criterion in the docstring. |
| 20 | `check_successions.py` | Malformed, dangling, unknown-modality, or frontier-cyclic SUCCEEDS records in the successions ledger — reader-side validation of what declare_succession checks only at write time (cycles are judged on the last-record-wins frontier, matching the generator and overlay). FATAL from birth (structural validity, exact error model). |
| 21 | `check_spine.py` | SPINE.yml structural integrity + regen-no-diff. FATAL. |

## Running

```sh
# Single check:
python3 scripts/drift/verify_cas.py

# All checks, continue on failure:
python3 scripts/drift/run_all.py

# All checks, stop on first failure:
python3 scripts/drift/run_all.py --stop-on-fail

# Session start: one-liner
python3 scripts/drift/session_status.py
```

## Enforced spine vs retrieval tier

`ket put` does two jobs: it makes content **retrievable/verifiable** (by
CID) *and*, historically, enrolled the path in the drift gate. Those pull
apart — retrieval wants breadth (seal the whole corpus so a session can
`ket_get`/`ket_search` it with confidence); enforcement wants a tight,
curated spine. Coupling them forced a false trade-off.

They are now decoupled:

- **`enforced_paths.txt`** lists the drift-enforced spine. Tool 4 gates
  **only** these — an edit that isn't re-`put` blocks a commit.
- Everything else put into CAS is **retrieval-tier**: retrievable and
  integrity-checked by tool 1 (`verify_cas`), but its working-tree content
  may move without blocking a commit.
- Absent `enforced_paths.txt`, every put path is enforced (the original
  behavior) — backward compatible.

Promote a path into the spine by adding it to `enforced_paths.txt`. Seal
broadly for retrieval without growing the enforcement burden.

## Wiring as hooks

Not wired by default. When you're ready, add to `.claude/settings.json`
(via the `update-config` skill or manually):

```json
{
  "hooks": {
    "SessionStart": [
      {"command": "python3 scripts/drift/session_status.py"}
    ],
    "PreToolUse": [
      {
        "matcher": {"tool": "Bash", "command_contains": "git commit"},
        "command": "python3 scripts/drift/run_all.py --stop-on-fail"
      }
    ]
  }
}
```

Tool 5 (fitted-correction linter) tends to produce false positives in
narrative prose; tune the retraction-marker allowlist in that script
rather than suppressing the hook.

## Allowlists

Tools 3 and 5 carry explicit allowlists at the top of their source.
Prefer extending the allowlist over disabling the check. Each entry
should carry a reason string.

## Drift classes this tooling does NOT catch

- **Semantic claim drift without textual markers.** If a paper-level
  claim quietly changes meaning without any retraction language or
  numerical change, no regex will see it. Tool 2 helps when the
  claim crosses into numerology_inventory; beyond that, it's on
  review.
- **Drift between this repo and other federated substrates.** Cross-
  repo imports (`ket export` / `ket import`) are point-in-time.
  Re-import to re-check.
- **Log tampering.** Tools 4 and 7 trust `.ket/log`. If that's
  rewritten, they can't tell. `git log` on `.ket/log` is the
  cross-check.
