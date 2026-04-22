# Anti-drift tooling

Seven checks that make substrate drift loud at the earliest moment.
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

## The seven checks

| # | Script | What it catches |
|---|---|---|
| 1 | `verify_cas.py` | CAS entries whose filename disagrees with the BLAKE3 of their content (bit-rot or algorithm drift). |
| 2 | `check_manifest.py` | Scorecard entries whose sources are unresolvable, Class 1/3 numerology, or marked retracted/declined. |
| 3 | `lint_local_hashing.py` | `hashlib.sha256/sha1/md5` usage under `scripts/`, `.ket/`, `seed/` — the source of the 2026-04-22 corruption. |
| 4 | `check_working_tree.py` | Tracked files whose current content no longer matches the last `put | <path> -> <cid>` entry in `.ket/log`. |
| 5 | `lint_fitted_corrections.py` | Un-audited additive corrections (`+ 8/F_10²`, `+ 1/228`, `+ 1/q_3²`, …) near bare K=1 identities without a retraction/derivation marker nearby. |
| 6 | `check_graph_orphans.py` | Derivation-graph nodes with zero edges, scorecard sources absent from the graph, and scorecard sources depending on Class 1/3 files. |
| 7 | `session_status.py` | One-line substrate snapshot: CAS count, corrupt count, scorecard/bare_k1 sizes, git dirtiness, drift count. Run at session start. |

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
