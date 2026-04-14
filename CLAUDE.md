# CLAUDE.md — orientation for future sessions

*This file is the persistent starting point. Read it before doing
anything.  It is meant to survive across sessions and branches.
Updated 2026-04-13 after the cross-branch reconciliation.*

## Canonical branch

**`main`** is canonical as of 2026-04-13 (PR #58 landed). The full
mass-sector closure, K_STAR_PRECISE, neutrino solar closure, tongue
audit, gauge residuals, and Higgs λ all live on `main`.

Pre-merge canonical work was on `claude/empirical-predictions-P25ZK`;
that branch is now equivalent to `main` and can be considered
archived.

Do **not** start new branches from older merge-bases (e.g. `07ba6ed`
or `fa83443`) without first checking what's on `main`. The 2026-04-13
reconciliation was necessitated by exactly that mistake: a new branch
started from a merge-base while the canonical work had already
closed under different definitions.

## Topology, not chronology

**Read `sync_cost/derivations/FRAMEWORK_TOPOLOGY.md` for the
dependency-driven map of the canonical state.**  It is the one-stop
"what depends on what" reference. Use it before deriving anything.

The topology is organized in five levels:
- **L0** — Foundations (four primitives, Klein bottle topology)
- **L1** — Forced selections from L0 (`(q_2, q_3) = (2, 3)`, `d = 3`,
  Klein parity, signature)
- **L2** — Derived integers from L1 (framework alphabet)
- **L3** — Derived structural laws from L2 (integer conservation,
  per-sector base pairs, sector integers `N`, tongue audit)
- **L4** — Tree-scale coupling `K_STAR_PRECISE = 0.86196052` from
  joint matter-sector fit
- **L5** — Predicted observables (mass, neutrino, gauge, Higgs,
  cosmology, generation count)

Chronology of how the framework was discovered is in
`RECONCILIATION_LOG.md` and `SESSION_RETROSPECTIVE_2026_04_13.md`.
**Use chronology for context, topology for work.**

## Session-start checklist

**Before deriving anything**, walk the topology:

1. Read `sync_cost/derivations/FRAMEWORK_TOPOLOGY.md` — the dependency
   map. Five levels (L0 foundations → L5 observables). Find where
   your candidate sits in the graph; if it's already at L2/L3/L4 you
   are about to re-derive canonical work.
2. Read `sync_cost/derivations/mass_sector_closure.md` — the
   cross-link uniqueness theorem (L1). The framework's integers
   `(q_2, q_3) = (2, 3)` are not chosen; they are the unique integer
   solution to `q_2² − 1 = q_3`, `q_3² − 1 = q_2³`. Any new
   "why (2, 3)" derivation is at best a pedagogical restatement.
3. Read `sync_cost/derivations/framework_constants.py` — the canonical
   numerical values (L2 → L4). **Always import from this, never
   hardcode**. Key values:
     - `K_STAR_PRECISE = 0.86196052` (5-digit, joint matter-sector
       closure; use this, not `K_STAR = 0.862`)
     - `K_LEPTON = 9 = q_3²`, `K_QUARK = 8 = q_2³`
     - `F_6_COUNT = 13 = |F_6| = q_2² + q_3²`, `F_7_COUNT = 19`
     - PDG masses (`PDG_MASS` dict, `M_E`, `M_MU`, `M_TAU`, ...)
4. Check `git log --oneline main -- sync_cost/derivations/` for the
   last few commits. Recent commits often retract or refine earlier
   work — trust HEAD, not history.
5. **Do NOT trust `open_items.md`** as a source. It is the
   fastest-staling document. Derive item status from the topology
   and the code, not from `open_items.md`.

## Canonical closures (as of 2026-04-13)

These are **closed with first-principles derivation**, numerically
at observational precision:

| closure | file | status |
|---|---|---|
| Cross-link uniqueness `(2, 3)` | `mass_sector_closure.md` | theorem |
| `K_STAR_PRECISE = 0.86196052` (5 digits) | `item12_K_star_closure.py` | χ²/dof = 0.06 |
| Lepton identity `a_1 · K* = 2` | `item12_C_from_K_star.py` | 0.00σ under K_STAR_PRECISE |
| Cross-sector `a_1² · K*² = N_sector` | `item12_cross_sector_derivation.py` | sub-1σ, three sectors |
| Sector integers `N = {4, 9, 24} = {q_2², q_3², q_2³·q_3}` | `item12_cross_sector_derivation.py` | from parabola rotation reading (D) + Fibonacci shift + Klein parity |
| Neutrino solar closure | `item12_neutrino_solar_closure.py` | atm 0.31σ, solar 0.12σ of NuFIT |
| Neutrino depth `35 = q_2³ + q_3³` | `item12_neutrino_solar_closure.py` | exact |
| Neutrino `m_1/m_3 = 1/q_2³ = 1/8` | `item12_neutrino_solar_closure.py` | exact |
| `sin²θ_W = 8/35 + 8/F_10²` | `item12_sin_W_and_signs.py` | ~2×10⁻⁵ of PDG |
| `α_s/α_2 = 27/8 + 1/q_3²` | `item12_other_residuals.py` | 0.17% of PDG |
| Higgs `λ = 1/8 + 1/228`, `228 = q_2² q_3 \|F_7\|` | `fc677bc` commit | at PDG |
| Tongue audit reading (D): `w = π × Ω-width` | `tongue_formula_accuracy.py` | resolves perturbative / critical ambiguity |

## Canonical `a_1` definition (important — most common mistake)

`a_1(sector)` on the canonical branch is the **single-step** quantity:

```python
a_1 = log(m_heavy / m_light) / (d * log(b_1))
```

with `d = 3` and per-sector base pairs:

| sector | base pair `(b_1, b_2)` | heavy/light ratio |
|---|---|---|
| lepton | `(3/2, 5/3)` | `m_τ / m_μ` |
| up-type | `(8/5, 3/2)` | `m_t / m_c` |
| down-type | `(5/4, 9/8)` | `m_b / m_s` |

Under this definition, `a_1(lep) · K_STAR_PRECISE = q_2 = 2` closes
at **0.00σ** of PDG.  See `item12_C_from_K_star.py`.

**Common mistake** (I made it this session on the summarize branch):
defining `a_1` as the combined-τ/e form
```python
a_1_bad = log(m_τ / m_e) / (3·log(3/2) + (9/2)·log(5/3))
```
gives `2.31970`, which is **0.026% off** the canonical `2.32029` and
leads to closed-form fits that look tight (I found
`ln(13) − 2/(3e) = 2.319696` at 0.02σ of this wrong number) but are
**not the canonical identity**.  If you find yourself writing the
combined form, stop and check `item12_C_from_K_star.py`.

## Retractions on the canonical branch

Canonical history contains intermediate attempts that were later
retracted or refined.  **The HEAD is the final state, not the full
history.**  Some retractions to know about:

| retracted | commit | replaced by | note |
|---|---|---|---|
| Lepton `+2/F_12²` correction | `2673614` introduced, `c36d636` retracted | `K_STAR_PRECISE` | was a rounding artifact of `0.862` vs `0.86196052` |
| Neutrino depth = 36 | `5ad40f8` | depth = 35 (`a3f7388`, `386fcaf`) | superseded |
| `N = 54` neutrino conjecture | `2673614` | `c6a06f8` killed | 54 is cosmological, not neutrino |
| `K_STAR = 0.8668` (A-2 neutrino refit) | `15c2aca` | `K_STAR_PRECISE = 0.86196052` | A-2 was pre-joint-closure |
| Multiple sin²θ_W attempts | several | `2bf8aca` + `7f8f4a6` | final form: `8/35 + 8/F_10²` |
| Multiple Higgs λ forms | several | `fc677bc` | final form: `1/8 + 1/228` |
| Various "nearly-integer" walk-sum anchors | `committed_walk_masses.py` | — | mass formula A superseded by formulation B |

If you see a numerical claim on an old commit that disagrees with
the HEAD, trust the HEAD.

## Things to trust vs things to distrust

**Trust:**
1. `framework_constants.py` (canonical source of all numerical values)
2. `item12_*` files (final closure work)
3. `mass_sector_closure.md` (the uniqueness theorem)
4. `RECONCILIATION_LOG.md` (the most recent cross-branch state)
5. Commit messages on recent commits (they're usually honest about what's being tried vs what's closed)

**Distrust:**
1. `open_items.md` — fastest-staling
2. Any script that hardcodes `K_STAR = 0.862` (3-digit; use `K_STAR_PRECISE` instead)
3. Any closed-form claim for `a_1` that uses the combined-τ/e definition
4. Retracted commits (see table above) — they remain in history but are not canonical
5. Your memory across sessions — assume everything is stale

## If you're about to derive something new

Run this mental checklist first:

1. Does `mass_sector_closure.md` already state it?
2. Does any `item12_*` script already compute it?
3. Does `framework_constants.py` already store the value?
4. Does `RECONCILIATION_LOG.md` list it as closed or retracted?
5. Does the commit history contain a `retract` or `kill` or `walk back` for this idea?
6. If you're about to claim a closed form matches "at quoted precision," **pull the precise value from `framework_constants.py` first** — `K_STAR` is 3-digit, `K_STAR_PRECISE` is 5-digit, they differ at digit 4 and it matters.

If all six checks pass, proceed.  Otherwise, you may be about to
re-derive something that's already closed under a different
(correct) framing.

## How branches have been going wrong

From the 2026-04-13 reconciliation, the failure mode was:

1. A new branch (`claude/summarize-commits-questions-P25ZK`) was
   started from the old merge-base `07ba6ed`.
2. It did not pull in 88 commits of intervening work on
   `claude/empirical-predictions-P25ZK`.
3. It independently re-derived slightly-wrong versions of things
   already closed on canonical.
4. It convinced itself these were new results.
5. Reconciliation cost several hours of timeline archaeology.

**Defense:**

- Never start a new branch from a merge-base you haven't surveyed.
- Always check `git log main -- sync_cost/derivations/` first.
- When in doubt, work directly on `main`.
- If a new branch is needed for isolation, first rebase it on top of
  `main`.

**Branch hygiene principles (added 2026-04-13 in response to a
second-order failure):**

- **PR on branch creation.** Every new branch gets a PR opened at
  the moment it is pushed, with a defined merge path. A branch
  without a PR is an orphan that compounds into a reconciliation
  problem.
- **Modifications stay close to additions.** A new branch with N
  pure additions and 0 modifications cannot diverge. A new branch
  with even 1 modification of an existing file can diverge if
  anything else lands on that file. Modifications need fast merge
  windows.
- **Branches measured in minutes, not days.** The orphan-branch
  failure mode was a 13-commit branch that lived for 16 hours
  before reconciliation. The window between push and PR should be
  measured in minutes — tighter than the time it takes to write the
  PR description. If you find yourself debating whether to open a
  PR, you have already waited too long.
- **No strategy that forces inconsistency or fails to account for
  it.** Every branch that adds divergence must have a defined plan
  for how the divergence is resolved. Otherwise it is a future
  reconciliation problem deferred.

## The framework in one paragraph (for quick grounding)

Four primitives (integers, mediant, fixed point, parabola) on a
Stern-Brocot tree with a Klein bottle topology.  The integers
`(q_2, q_3) = (2, 3)` are the unique minimum solution to the
gauge-adjoint cross-link.  The spatial dimension `d = 3 = q_3` is
the dimension of `SL(2, R)`.  The self-consistent tree-scale coupling
`K_STAR_PRECISE = 0.86196052` is the fixed point of the joint
matter-sector closure.  The mass sector closes through
`a_1² · K*² = N_sector` with `N = {4, 9, 24}`.  The neutrino sector
closes at depth `35 = q_2³ + q_3³` with `m_1/m_3 = 1/8` exact and a
solar correction `−1/36`.  Gauge residuals are Fibonacci-square and
gauge-integer-square finite-K corrections to tree-scale rationals.
Everything is closed within observational precision; only the
dimensionful scale `v = 246 GeV` is input.

---

*This CLAUDE.md is persistent.  If you update it with new canonical
information, keep it focused: it should be the first thing a new
session reads, so it must stay short and unambiguous.*
