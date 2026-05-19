#!/usr/bin/env python3
"""
PreToolUse(Bash) gate: run the anti-drift suite ONLY before a real
`git commit`.

Why this exists: the hook was scoped with the settings.json `if`
filter (`"if": "Bash(git commit:*)"`). That filter is documented but
was NOT honored in the running Claude Code build — the hook fired on
*every* Bash call and (because drift used to be fatal) wedged
unrelated work all session. This wrapper makes the scoping
**build-independent**: the hook fires unconditionally, but this
script self-filters by inspecting the actual command on stdin and
exits 0 immediately unless it is a `git commit`. The `if` key is
kept in settings as a no-cost optimization for builds that DO honor
it; correctness no longer depends on it.

Contract:
  - stdin: PreToolUse hook JSON, `{"tool_input":{"command":"..."}}`.
  - If the command invokes `git commit` (incl. `git -C p commit`,
    `git -c k=v commit`, chained `... && git commit ...`):
      exec `python3 scripts/drift/run_all.py --stop-on-fail`
      and propagate its exit code (THIS is the gate — a fatal
      check, e.g. CAS corruption, blocks the commit; drift itself
      is advisory per run_all.py's severity model).
  - Otherwise, or on any parse failure: exit 0 (fail OPEN — never
    re-introduce the misfire that this fixes; the gate is
    best-effort and CI is the backstop).

Run dir: the hook `cd`s to $CLAUDE_PROJECT_DIR first, so run_all is
invoked from the repo root.
"""

from __future__ import annotations

import json
import os
import re
import sys

# `git`, then zero or more *global* options (-C <path>, -c <kv>,
# -p, --no-pager, --git-dir=..., etc.), then the `commit`
# subcommand. If a non-option token appears before `commit`, then
# `commit` is not the subcommand (e.g. `git log --grep=commit`,
# `git status`) and this will not match.
GIT_COMMIT = re.compile(
    r"\bgit\b"
    r"(?:\s+(?:-C\s+\S+|-c\s+\S+|--?[\w.-]+(?:=\S+)?))*"
    r"\s+commit\b"
)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
        command = (payload.get("tool_input") or {}).get("command") or ""
    except Exception:
        return 0  # fail open — unknown input must not gate

    if not command or not GIT_COMMIT.search(command):
        return 0  # not a commit — no-op, hook passes through

    # It's a git commit: hand off to the suite and propagate its rc.
    os.execv(
        sys.executable,
        [sys.executable, "scripts/drift/run_all.py", "--stop-on-fail"],
    )
    # os.execv only returns on failure to exec.
    return 0


if __name__ == "__main__":
    sys.exit(main())
