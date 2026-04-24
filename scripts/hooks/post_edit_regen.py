#!/usr/bin/env python3
"""
PostToolUse hook: keep Pages views in sync with their source files.

Reads the Claude Code tool-invocation JSON on stdin.  If the edited
file is one that feeds a generated view, re-runs the relevant
generator.  Intentionally silent on the no-op case so the hook
doesn't spam the session.

Triggers:

  - MANIFEST.yml          → scripts/build_claim_chain.py
  - *numerology_inventory.md | *FRAMEWORK_TOPOLOGY.md
                          → scripts/build_claim_chain.py (their contents
                            flow into the "Bare identities" / proof-chain
                            sections of the page)
  - sync_cost/derivations/*.md
                          → scripts/build_derivation_graph.py (the
                            DAG is built by scanning derivation
                            markdown)

Exit code is always 0 unless a generator itself fails.  We never
want this hook to block an edit — its job is to keep Pages honest,
not to gate changes.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path


def _load_input() -> dict:
    try:
        return json.load(sys.stdin)
    except Exception:
        return {}


def _edited_file(payload: dict) -> str:
    tool_input = payload.get("tool_input") or {}
    # Edit / Write / MultiEdit all expose `file_path`.
    return tool_input.get("file_path") or ""


def _project_root() -> Path:
    return Path(os.environ.get("CLAUDE_PROJECT_DIR", ".")).resolve()


def _run(generator: str, root: Path) -> tuple[str, int, str]:
    proc = subprocess.run(
        ["python3", generator],
        cwd=root,
        capture_output=True,
        text=True,
    )
    return generator, proc.returncode, (proc.stdout or proc.stderr).strip()


def main() -> int:
    payload = _load_input()
    edited = _edited_file(payload)
    if not edited:
        return 0

    root = _project_root()
    try:
        rel = Path(edited).resolve().relative_to(root)
    except ValueError:
        # Edited file is outside the project — nothing to do.
        return 0

    rel_str = str(rel)
    to_run: list[str] = []

    if rel_str == "MANIFEST.yml":
        to_run.append("scripts/build_claim_chain.py")

    if rel_str in (
        "sync_cost/derivations/numerology_inventory.md",
        "sync_cost/derivations/FRAMEWORK_TOPOLOGY.md",
    ):
        # Only claim-chain reads these — the graph JSON is topology
        # based on cross-references, these don't change it.
        if "scripts/build_claim_chain.py" not in to_run:
            to_run.append("scripts/build_claim_chain.py")

    if rel_str.startswith("sync_cost/derivations/") and rel_str.endswith(".md"):
        to_run.append("scripts/build_derivation_graph.py")

    if not to_run:
        return 0

    messages: list[str] = []
    any_fail = False
    for generator in to_run:
        name, rc, out = _run(generator, root)
        short = Path(name).stem
        if rc != 0:
            any_fail = True
            messages.append(f"{short}: FAIL (rc={rc}) — {out[:200]}")
        else:
            # Keep output terse; most generators print a single-line summary.
            first_line = out.splitlines()[0] if out else "ok"
            messages.append(f"{short}: {first_line}")

    # Emit a single status line on stderr so the user sees what was
    # regenerated without cluttering stdout/transcripts.
    sys.stderr.write("post_edit_regen → " + " | ".join(messages) + "\n")
    return 1 if any_fail else 0


if __name__ == "__main__":
    sys.exit(main())
