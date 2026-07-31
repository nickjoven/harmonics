"""Shared .ket/log parsing — the single copy.

The 2026-07-30 review found FIVE divergent copies of the put-line
regex (check_working_tree, session_status, check_graph_sealed,
check_enforced_coverage, reconcile_substrate), four of which skipped
unparseable lines silently — and the concatenated-append corruption
survived all five because the non-greedy path group BACKTRACKED and
matched the joined line with a garbage path, so even the malformed
detector never fired. This module is the one grammar every reader
uses, strict enough that a concatenated line cannot parse:

  * the path may not contain " -> " (a joined line carries a second
    arrow, so it fails to parse as one entry instead of capturing a
    garbage path), and
  * the CID must terminate the line.

Anything put-shaped that fails the grammar is returned as `malformed`,
never dropped.
"""

import re
from typing import NamedTuple

# Strict entry grammar. The tempered path group (?:(?!\s->\s).)+? is
# the anti-backtracking guard: it cannot expand across an arrow.
PUT_LINE = re.compile(
    r"^(?P<ts>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)"
    r"\s+\|\s+put\s+\|\s+"
    r"(?P<path>(?:(?!\s->\s).)+?)"
    r"\s+->\s+(?P<cid>[0-9a-f]{64})\s*$"
)


class LogView(NamedTuple):
    """last_cid: path -> most recent CID; malformed: (lineno, fragment)
    for every put-shaped line the grammar rejects."""
    last_cid: dict
    malformed: list


def read_log(log_path) -> LogView:
    last_cid, malformed = {}, []
    for n, line in enumerate(log_path.read_text().splitlines(), 1):
        m = PUT_LINE.match(line)
        if m:
            path = m.group("path")
            # `ket put -` (stdin) logs "-" as the path; not a file.
            if path != "-":
                last_cid[path] = m.group("cid")
        elif "| put |" in line:
            malformed.append((n, line[:80]))
    return LogView(last_cid, malformed)
