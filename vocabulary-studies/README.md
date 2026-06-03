# vocabulary-studies

**Readings of external mathematics through the harmonics minimum alphabet.**

A federated sibling of [`harmonics`](https://github.com/nickjoven/harmonics).
Where harmonics is the *derivation chain* (the equation and its physical
consequences), this repo holds **Class 2 structural readings** of famous
external objects — Ramanujan's 1/π series, the Collatz map, the Riemann
Hypothesis — through the framework's four primitives (integers, mediant,
fixed-point, parabola; see `minimum_alphabet.md` upstream).

These are **not** derivation-chain content. They produce no scorecard
claim and no new constants. They *consume* the harmonics substrate
(referencing canonical concepts by name/CID) and live here precisely so
the derivation spine stays clean — the federation's separation-of-roles
discipline (`MANIFEST.yml repos:`).

## Why a separate repo

Per the placement decision (harmonics PR #210 thread): vocabulary readings
are a different register from physics derivations. Accumulating "this
famous object also speaks the vocabulary" notes inside
`harmonics/sync_cost/derivations/` is exactly the dilution the anti-drift
discipline guards against, even when each note is individually honest. This
repo is the quarantine and the publishing surface.

## Contents

- **`farey_tree_synthesis.md`** — capstone: one object (the Farey tree =
  mediant primitive = PSL(2,Z) on ℚ) under three problems; structure
  forced, arithmetic open. Anchored on Franel–Landau (RH ⟺ Farey
  equidistribution). Companion `farey_tree_synthesis.py`.
- **Ramanujan thread** — `ramanujan_pi_minimum_alphabet.md`,
  `ramanujan_pi_modular_discriminator.md`,
  `ramanujan_pi_structure_not_numbers.md` (+ `.py` checks).
- **Collatz** — `collatz_minimal_chaos.md` (+ `.py`).

Each note is classified, limits-first, with runnable checks (pure-Python,
no numpy).

## Upstream

Unqualified references to substrate concepts (`minimum_alphabet.md`,
`mediant_derivation.md`, `psl2z_subgroup_phase_a_results.md`,
`second_law_topological.md`, `docs/archive/collatz.html`) resolve against
the **harmonics** upstream (`MANIFEST.yml → repos.harmonics`).

## Status

Class 2 throughout. Expository / `math.HO`-targeted, not research claims.
The recurring finding is the boundary itself: the mediant primitive fixes
*structure*, never the *arithmetic* at the tree's boundary.
