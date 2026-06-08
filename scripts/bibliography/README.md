# Bibliography substrate

The derivation docs cite the external literature inline, in the two
notations the repo already uses:

```
arXiv:2504.19874              arXiv:hep-th/9711200 (old style)
doi:10.1126/science.aea3321   https://doi.org/10.1126/science.aea3321
```

`build_bibliography.py` turns those inline strings into a checked,
resolved bibliography. It is the bibliography analogue of
`scripts/build_derivation_graph.py`: a pure function of the markdown
sources, owned by CI, never hand-edited.

## What it does

1. **Extract** every arXiv id / DOI from `sync_cost/**.md`. Each
   normalizes to a canonical id — `arxiv:<id>` (version-stripped) or
   `doi:<doi>` (lowercased) — so the same work cited two ways collapses
   to one entry.
2. **Resolve** each id to canonical metadata:
   - arXiv → the arXiv Atom API (`export.arxiv.org/api/query`)
   - DOI → the CrossRef REST API (`api.crossref.org/works/<doi>`,
     polite pool via `mailto`)
   Every lookup is cached in `cache.json`, so resolution is incremental
   and PR-time validation needs the network only for *new* citations.
3. **Render** three artifacts that travel with the repo:
   - `sync_cost/derivations/references.bib` — BibTeX
   - `sync_cost/derivations/REFERENCES.md` — human index with per-entry
     back-links to the citing docs
   - `docs/bibliography.json` — machine index for the site

## Commands

```
python3 scripts/bibliography/build_bibliography.py build       # resolve + write artifacts (hits APIs)
python3 scripts/bibliography/build_bibliography.py build --refresh   # re-resolve even cached ids
python3 scripts/bibliography/build_bibliography.py check       # validate citations + artifact freshness
python3 scripts/bibliography/build_bibliography.py check --no-artifacts   # citations only (PR gate)
python3 scripts/bibliography/build_bibliography.py check --offline        # validate from cache, no network
python3 scripts/bibliography/build_bibliography.py list        # list citations found (no resolution)
```

Or via make: `make bibliography` (build) and `make bibliography-check`
(`OFFLINE=1` to skip the network).

## Failure semantics

`check` distinguishes three outcomes per citation, which is what makes
the CI gate trustworthy rather than flaky:

| outcome | example | effect |
|---|---|---|
| **malformed / not found** | `arXiv:2599.99999`, a 404 DOI | **error** — fails the check |
| **network unreachable** | API timeout / DNS failure | **warning** — falls back to cache, does not fail |
| **resolved** | found via API or cache | recorded |

A flaky API therefore never reddens an unrelated PR, but a citation
that points at no real paper always does.

## CI ownership

`.github/workflows/bibliography.yml`:

- **validate** (PRs + pushes) — runs `check --no-artifacts`: every
  citation must resolve to a real paper. Artifact freshness is *not*
  enforced on PRs.
- **regen** (push to main) — runs `build`, then bot-commits the cache
  and artifacts with a race-safe push loop, exactly like
  `regen-derivation-graph.yml`.

So contributors add a citation inline and open a PR; the gate confirms
the paper exists; the main-branch bot regenerates `references.bib`,
`REFERENCES.md`, and `docs/bibliography.json`. You only run `make
bibliography` locally if you want the artifacts updated in your own
branch.

## Why the cache is committed

Committing `cache.json` makes PR validation deterministic and mostly
offline: a PR that touches prose but no citations validates with zero
network calls. Only a genuinely new arXiv id / DOI reaches the API.
The cache is metadata only (title, authors, year, venue) — it is a
convenience layer over the APIs, which remain the authority.
