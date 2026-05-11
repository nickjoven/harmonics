# scripts/maintenance/

Bot-side substrate upkeep. CI-owned, complementing the human-driven
derivation work.

## Files

- `reconcile_substrate.py` — re-hash drifted derivation files and
  append reconciliation reasoning DAG nodes. Idempotent; no-op when
  drift is 0.

## How it runs

`.github/workflows/substrate-maintenance.yml` triggers on push to
main when derivation-relevant paths change. The workflow:

1. Builds the `ket` binary from `github.com/nickjoven/ket` (cached
   across runs).
2. Reports initial drift via `scripts/drift/session_status.py`.
3. If drift > 0, runs `reconcile_substrate.py`.
4. Runs `scripts/drift/run_all.py` for broader consistency checks
   (manifest, graph orphans, CAS verification).
5. Commits `.ket/` changes directly to main with a `bot:` prefix.

The workflow only modifies `.ket/cas/*` and `.ket/log`. It will not
touch derivation `.md`, `.py`, or `MANIFEST.yml` content. Non-drift
issues from `run_all.py` fail the workflow to alert maintainers
without auto-fixing.

## Why direct-to-main and not auto-PR

Substrate reconciliation is mechanical: re-hash a file that was
edited, add a provenance node, append to the log. No judgment.
Same pattern as `regen-derivation-graph.yml`. Auto-PR adds review
friction without review value.

## Why shell out to the ket binary

`scripts/ket.py` is explicit: a previous Python reimplementation
silently drifted from BLAKE3 and produced CORRUPTED CAS entries
under `ket verify`. The single source of hashing truth is the
binary. The workflow builds it from source rather than reimplementing.

## When to extend

The current scope is drift + the existing consistency checks. If
broader maintenance becomes useful (Dolt restoration, scorecard
auto-repair, CAS-vs-git divergence), add a separate script under
this directory and a new step in the workflow. Keep mechanical
operations here; anything requiring judgment should stay manual or
go to a Claude-side scheduled agent.
