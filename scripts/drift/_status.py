"""Shared status-surface predicates — the single spelling.

The review (2026-07-30) found the class-tag pattern in three divergent
spellings and the "surface asserts strength" predicate implemented
twice with different semantics. Every check that reads a doc's
self-declared status imports from here; a spelling change lands
everywhere at once instead of in whichever copy someone remembered.

NB scripts/experiments/retrodict.py keeps its OWN copy of DERIVED_RE
deliberately: its behavior is pinned by fixtures_263.json and gated
FATALly (check_retrodiction), so its predicate must move only with a
fixture re-proof. The cross-reference comment there points here.
"""

import re

# Case-sensitive standalone "Derived" — the strength-asserting verb.
DERIVED_RE = re.compile(r"\bDerived\b")

# Acknowledgment vocabulary: a status that carries any of these has
# noticed its own weakening/rescope.
ACK_RE = re.compile(r"rescoped|superseded|historical", re.IGNORECASE)

# Class tags, in the corpus's accepted spellings ("Class 1", "Class-1"):
CLASS1_RE = re.compile(r"\bClass[ -]?1\b")
CLASS5_RE = re.compile(r"\bClass[ -]?5\b")


def self_status(meta: dict) -> str:
    """A doc's SELF-DECLARED status surface: inline status line plus
    Status-section bold. Never the corpus-index `classes` scrape — that
    field records every prose MENTION (the Card 8 false positive)."""
    return " ".join(filter(None, [meta.get("status_line"),
                                  meta.get("status_bold")]))
