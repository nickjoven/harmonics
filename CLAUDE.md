# harmonics — project instructions

This repository is a **derivation framework**. Named concepts — derivation docs,
lemmas, scorecard claims — live under `sync_cost/derivations/` and are the
substance of the repo. They are backed by a **source-of-truth substrate** that
addresses and integrity-checks each concept, so that the *substrate* — not your
context window, and not your training prior — is the authority on what a concept
says. Orientation lives in `README.md`.

The substrate is **swappable**. Today it is the content-addressed `.ket` store
(BLAKE3-addressed blobs, Merkle-DAG provenance); the mechanics of that current
implementation are isolated in the [Current substrate](#current-substrate-ket--swappable)
section and in `scripts/drift/README.md`. The **discipline** in this file does
not depend on which substrate backs the repo — only on there being one. If the
backing changes, only the Current-substrate section changes.

## Knowledge is a cache of the substrate

Treat everything you "know" about a named concept — a value, a lemma's
statement, what a derivation forces, which class a claim sits in — as a **cache
entry over the substrate**, not as ground truth. Like any cache, an entry has a
*key*, a *resolution*, and a *freshness*:

- **Key** — the named concept: `born_rule`, `klein_bottle`, the 13/19 Ω_Λ
  chain, a MANIFEST scorecard row.
- **Resolution** — the granularity you're relying on. "Ω_Λ ≈ 0.68" is a coarse
  cache entry; "13/19 = 0.6842, forced at Stern-Brocot depth 6, 0.07σ from
  Planck" is a fine one. A coarse entry can be right while the fine entry you're
  about to assert is stale or invented.
- **Freshness** — whether *this* entry was read from the substrate recently, or
  is being recalled from earlier in the session, a prior session, or your prior.

An entry is **stale** when the underlying content has moved since you read it
(drift), and **fabricated** when you never read it at all — you're filling in a
plausible detail by assumption. Both are silent failures: the numbers look
clean, the prose reads confidently, and nothing surfaces the gap until someone
checks. The repo's history (the SHA-256/BLAKE3 corruption and the
`weinberg_angle` misclassification noted in `scripts/drift/README.md`) is a
record of exactly this class of silent drift.

## Verify-before-assert protocol

Before asserting a named concept at a particular resolution, check the cache
entry against the substrate. **Verify when** any of these hold:

1. **Not read this session** — you haven't retrieved this concept from the
   substrate in the current conversation, or you read it only at a coarser
   resolution than you're about to assert.
2. **Taken on assumption** — the detail is one you're supplying from inference,
   memory, or a "this is probably how it works," rather than from content you
   read. If you can't name where it came from, it's an assumption.
3. **Load-bearing** — the assertion will feed a derivation step, a commit, a
   scorecard/MANIFEST edit, or an answer the user will rely on downstream.
4. **The session snapshot is non-clean** — the SessionStart line reports corrupt
   entries, non-zero drift, or git-dirty enforced-spine files. A non-zero drift
   count means working-tree content may disagree with its sealed address;
   re-read from the substrate, don't trust the cache.

How to verify, in order of preference (the operations are substrate-agnostic;
the current tools for each are in the Current-substrate section):

- **Retrieve and read** the concept from the substrate at the resolution you
  intend to assert, not coarser. Read its **lineage** to confirm you're holding
  the **canonical** entry and not one that has been **superseded**, **retracted**,
  or **declined**.
- **Check integrity** — re-hash/verify the entry, or run the drift checks, when
  you suspect the working tree has drifted from the sealed content.
- **Cross-check the domain registry** — for quantitative claims, reconcile
  against `MANIFEST.yml` and `numerology_inventory.md` (Class 1–5) and the doc's
  status tag (Survives / Floor / Eliminated). A **bare K=1** arithmetic identity
  (the continuum regime) is *not* a scale-consistent corroborated result the way
  a **K<1** substrate derivation is; don't cache the former at the latter's
  resolution. This registry is the repo's own domain check and stands
  independent of which substrate backs the concepts.

If you cannot verify a load-bearing detail against the substrate, **say so** —
assert it as unverified and name the gap, rather than presenting a cache guess as
substrate fact. Re-reading a sealed entry is cheap; a confident stale assertion
that propagates into a derivation is the expensive failure this protocol exists
to prevent.

## Caching what you verify

Once you've read a concept fresh from the substrate this session, you may rely on
that cache entry at that resolution for the rest of the session without
re-reading — unless you (or a hook) mutate the underlying file, in which case the
entry is dirtied and must be re-sealed and re-read before reuse. Mutating an
**enforced-spine** path without re-sealing is exactly the drift the precommit
gate blocks; a **retrieval-tier** path may move without gating but is still
integrity-checked. Reference the address/path rather than reproducing the content
from memory.

## Vocabulary — caching terms ↔ substrate concepts

This protocol borrows cache vocabulary to talk about a substrate that already has
its own canonical words (see `sync_cost/derivations/canonical_glossary.md`). The
middle column names the **substrate-general** concept; the current ket
realization of each is in the Current-substrate section.

| Caching term | Substrate concept | Meaning in this repo |
|---|---|---|
| **cache / context** | working memory over the **substrate** | What you hold in-context; never the source of truth. |
| **cache entry** | a **sealed entry** at an **address** | One seal of a concept; addressed and integrity-checked by its content hash. |
| **key** | named concept / **path** | The derivation doc, lemma, or scorecard row — e.g. `baryon_fraction.md`, a `MANIFEST.yml` claim. |
| **resolution** | granularity / **regime** | How fine a claim you assert; **bare K=1** vs **K<1** is itself a resolution distinction. |
| **freshness** | read-recency vs **drift** | Whether the entry was retrieved this session, or recalled. Drift = working-tree content disagrees with the last sealed address. |
| **stale** | **drifted** entry | Content moved since you read it (or the tree drifted from its seal). |
| **fabricated** | **vocabulary artifact** | A detail supplied by assumption, never read — a framing with no canonical object behind it (`vocabulary_is_the_work_pattern.md`). |
| **cache invalidation** | **supersede** / re-seal | A concept's canonical home changing via lineage; or re-sealing after an edit. |
| **eviction** | **retracted** / **declined** / **Eliminated** | A claim removed from canonical status; do not re-assert it from a stale entry. |
| **authoritative read** | **canonical** entry | The current head of a concept's lineage. |
| **write-through** | **seal** | Persisting an edit back into the substrate so the entry is retrievable and integrity-checked. |
| **pinned vs evictable** | **enforced spine** vs **retrieval tier** | Spine paths gate commits on drift; retrieval-tier paths are integrity-checked but un-gated. |

## Current substrate: ket (swappable)

The repo is currently backed by the `.ket` content-addressed store: each named
concept is sealed into a BLAKE3-addressed blob under `.ket/cas/`, with Merkle-DAG
provenance and a queryable Dolt projection. The substrate-agnostic operations
above map to concrete tools:

- **retrieve / read** → `ket_search`, `ket_get`; **lineage** → `ket_lineage`;
  **recent changes** → `ket_recent` (the `ket_*` MCP tools).
- **integrity** → `ket_verify`, or `python3 scripts/drift/verify_cas.py` /
  `scripts/drift/run_all.py` for the full sweep.
- **seal / re-seal** → `ket put` / `ket_store`.
- **enforced spine vs retrieval tier** → `scripts/drift/enforced_paths.txt` lists
  the drift-gated spine; everything else sealed is retrieval-tier (integrity-
  checked by `verify_cas` but un-gated). See `scripts/drift/README.md`.

ket's own design invariants — content-addressing, projection-only SQL, the
self-heal/audit partition — live in that repo's `DESIGN.md`. The ket intersection
with this repo is a backing choice, not part of the derivation work; if the
backing substrate changes, this section changes and the discipline above does
not.

## Why this framing earns its keep

A fabricated cache entry is, in the repo's own terms, a **vocabulary artifact**:
a plausible word standing in for a real concept that was never named or read. The
recurring unblocking move recorded in `vocabulary_is_the_work_pattern.md` is the
cure — *name the correct object*, and the confident-but-wrong assertion either
dissolves or sharpens into a real, framework-native question. Verifying against
the substrate before asserting is that move applied pre-emptively, every time.
