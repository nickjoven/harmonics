# harmonics — project instructions

This repository is a derivation framework backed by a **content-addressed
knowledge substrate**. Named concepts (derivation docs, lemmas, scorecard
claims) live under `sync_cost/derivations/` and are sealed into the `.ket/`
CAS, where each blob is addressed and integrity-checked by its BLAKE3 CID.
The substrate — not your context window, and not your training prior — is the
source of truth. Orientation lives in `README.md`; the anti-drift tooling is
documented in `scripts/drift/README.md`.

## Knowledge is a cache of the CAS

Treat everything you "know" about a named concept in this repo — a value, a
lemma's statement, what a derivation forces, which class a claim sits in — as a
**cache entry over the CAS**, not as ground truth. Like any cache, an entry has
a *key*, a *resolution*, and a *freshness*:

- **Key** — the named concept: `born_rule`, `klein_bottle`, the 13/19
  Ω_Λ chain, `e_cross_discrete_resolution`, a MANIFEST scorecard row.
- **Resolution** — the granularity you're relying on. "Ω_Λ ≈ 0.68" is a coarse
  cache entry; "13/19 = 0.6842, forced at Stern-Brocot depth 6, 0.07σ from
  Planck" is a fine one. A coarse entry can be right while the fine entry you're
  about to assert is stale or invented.
- **Freshness** — whether *this* entry was read from the CAS recently, or is
  being recalled from earlier in the session, a prior session, or your prior.

A cache entry is **stale** when the underlying CAS content has moved since you
read it (substrate drift), and **fabricated** when you never read it at all —
you're filling in a plausible detail by assumption. Both are silent failures:
the numbers look clean, the prose reads confidently, and nothing surfaces the
gap until someone checks. The repo's history (the SHA-256/BLAKE3 corruption and
the `weinberg_angle` misclassification noted in `scripts/drift/README.md`) is a
record of exactly this class of silent drift.

## Verify-before-assert protocol

Before asserting a named concept at a particular resolution, check the cache
entry against the CAS. **Verify when** any of these hold:

1. **Not read this session** — you haven't retrieved this concept from the CAS
   in the current conversation, or you read it only at a coarser resolution than
   you're about to assert.
2. **Taken on assumption** — the detail is one you're supplying from inference,
   memory, or a "this is probably how it works," rather than from a blob you
   read. If you can't name where it came from, it's an assumption.
3. **Load-bearing** — the assertion will feed a derivation step, a commit, a
   scorecard/MANIFEST edit, or an answer the user will rely on downstream.
4. **The session snapshot is non-clean** — the SessionStart line reports corrupt
   CAS entries, non-zero drift, or git-dirty enforced-spine files. A non-zero
   drift count means working-tree content may disagree with its sealed CID;
   re-read from the substrate, don't trust the cache.

How to verify, in order of preference:

- **Retrieve and read** the concept from the CAS via the `ket_*` MCP tools —
  `ket_search`/`ket_get` to pull the current blob, `ket_lineage` to see how it
  was superseded, `ket_recent` to see what changed lately. Read at the
  resolution you intend to assert, not coarser.
- **Check integrity** with `ket_verify`, or run the drift checks
  (`python3 scripts/drift/verify_cas.py`, or `scripts/drift/run_all.py` for the
  full sweep) when you suspect the working tree has drifted from the substrate.
- **Cross-check the registry** — for quantitative claims, reconcile against
  `MANIFEST.yml` and `numerology_inventory.md` (Class 1–5) and the doc's status
  tag (Survives / Floor / Eliminated). A **bare K=1** arithmetic identity (the
  continuum regime) is *not* a scale-consistent corroborated result the way a
  **K<1** substrate derivation is; don't cache the former at the latter's
  resolution. Read a concept's lineage (`ket_lineage`) to confirm you're holding
  the **canonical** entry and not one that has been **superseded**, **retracted**,
  or **declined**.

If you cannot verify a load-bearing detail against the CAS, **say so** — assert
it as unverified and name the gap, rather than presenting a cache guess as
substrate fact. Re-reading a sealed blob is cheap; a confident stale assertion
that propagates into a derivation is the expensive failure this protocol exists
to prevent.

## Caching what you verify

Once you've read a concept fresh from the CAS this session, you may rely on that
cache entry at that resolution for the rest of the session without re-reading —
unless you (or a hook) mutate the underlying file, in which case the entry is
dirtied and must be re-sealed (`ket put` / `ket_store`) and re-read before reuse.
Mutating an **enforced-spine** path (`scripts/drift/enforced_paths.txt`) without
re-sealing is exactly the drift the precommit gate blocks; a **retrieval-tier**
path may move without gating but is still integrity-checked by `verify_cas`.
Reference the CID or path rather than reproducing the content from memory.

## Vocabulary — caching terms ↔ substrate terms

This protocol borrows cache vocabulary to talk about a substrate that already
has its own canonical words (see `sync_cost/derivations/canonical_glossary.md`).
The table keeps the two registers aligned, in the spirit of that glossary:

| Caching term | Substrate term | Meaning in this repo |
|---|---|---|
| **cache / context** | working memory over the **substrate** | What you hold in-context; never the source of truth — the `.ket` CAS is. |
| **cache entry** | a sealed **blob** at a **CID** | One `ket put`/`ket_store` of a concept; addressed and integrity-checked by its BLAKE3 hash (the filename under `.ket/cas/`). |
| **key** | named concept / **path** | The derivation doc, lemma, or scorecard row — e.g. `baryon_fraction.md`, a `MANIFEST.yml` claim. |
| **resolution** | granularity / **regime** | How fine a claim you assert. Distinct from a `*_resolution.md` doc (which *resolves* an open item). A coarse value vs a forced fraction at a named Farey depth; **bare K=1** vs **K<1** is itself a resolution distinction. |
| **freshness** | read-recency vs **drift** | Whether the entry was retrieved from the CAS this session, or recalled. **Drift** = working-tree content disagrees with the last sealed CID. |
| **stale** | **drifted** entry | CAS content moved since you read it (or the tree drifted from its seal). Caught by `verify_cas` / `check_working_tree`. |
| **fabricated** | **vocabulary artifact** | A detail supplied by assumption, never read — an *imported-vocabulary* framing with no canonical CAS object behind it (`vocabulary_is_the_work_pattern.md`). |
| **cache invalidation** | **supersede** / re-seal | A concept's canonical home changing via `ket_lineage`; or re-`put` after an edit. |
| **eviction** | **retracted** / **declined** / **Eliminated** | A claim removed from canonical status; do not re-assert it from a stale entry. |
| **authoritative read** | **canonical** blob | The current head of a concept's lineage, confirmed via `ket_lineage` / `ket_canonicalize`. |
| **write-through** | **seal** (`ket put` / `ket_store`) | Persisting an edit back into the CAS so the entry is retrievable and integrity-checked. |
| **pinned vs evictable** | **enforced spine** vs **retrieval tier** | Spine paths (`enforced_paths.txt`) gate commits on drift; retrieval-tier paths are integrity-checked but un-gated. |

**Why this framing earns its keep.** A fabricated cache entry is, in the repo's
own terms, a **vocabulary artifact**: a plausible word standing in for a canonical
substrate object that was never named. The recurring unblocking move recorded in
`vocabulary_is_the_work_pattern.md` is the cure — *name the correct CAS object*,
and the confident-but-wrong assertion either dissolves or sharpens into a real,
framework-native question. Verifying against the CAS before asserting is that
move applied pre-emptively, every time.
