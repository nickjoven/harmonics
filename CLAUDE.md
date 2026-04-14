# CLAUDE.md — orientation for future sessions

*Persistent starting point. Read it before doing anything. Should
stay short and unambiguous; if it grows, the canonical substrate
elsewhere has drifted and that's where the fix belongs.*

## Where canonical state lives

1. **`sync_cost/derivations/FRAMEWORK_TOPOLOGY.md`** — dependency map
   of the canonical state, organized L0 (foundations) → L5 (observables).
   Read this **before deriving anything**. If your candidate sits at
   L2/L3/L4 you are about to re-derive canonical work.
2. **`sync_cost/derivations/framework_constants.py`** — every numerical
   constant and PDG value used in the framework. **Always import from
   this; never hardcode.** In particular, `K_STAR = 0.86196052` (the
   joint matter-sector closure value); do not use 0.862 or 0.8668.
3. **`sync_cost/derivations/mass_sector_closure.md`** — the cross-link
   uniqueness theorem. The integers `(q_2, q_3) = (2, 3)` are the
   unique solution to `q_2² − 1 = q_3`, `q_3² − 1 = q_2³`. Any new
   "why (2, 3)" derivation is at best a pedagogical restatement.
4. **`sync_cost/derivations/item12_*.py`** — the matter-sector closure
   scripts. They run to canonical numerical values; trust the running
   output, not surrounding prose.

The framework's L4 fixed point and all L5 observables are computed by
these scripts. Do not re-summarize their state in markdown elsewhere
— summary documents drift, scripts do not.

## Canonical `a_1` definition

`a_1(sector)` is the **single-step** quantity:

```python
a_1 = log(m_heavy / m_light) / (d * log(b_1))
```

with `d = 3` and per-sector base pairs:

| sector | base pair `(b_1, b_2)` | heavy/light ratio |
|---|---|---|
| lepton | `(3/2, 5/3)` | `m_τ / m_μ` |
| up-type | `(8/5, 3/2)` | `m_t / m_c` |
| down-type | `(5/4, 9/8)` | `m_b / m_s` |

Under this definition, `a_1(lep) · K_STAR = q_2 = 2` closes at **0.00σ**
of PDG. Do **not** use the combined-τ/e form
`log(m_τ / m_e) / (3·log(3/2) + (9/2)·log(5/3))` — it gives a different
number (2.31970 vs 2.32029) and any closed form built on it is for the
wrong projection. See `item12_C_from_K_star.py`.

## The framework in one paragraph

Four primitives (integers, mediant, fixed point, parabola) on a
Stern-Brocot tree with a Klein bottle topology. The integers
`(q_2, q_3) = (2, 3)` are the unique minimum solution to the
gauge-adjoint cross-link. The spatial dimension `d = 3 = q_3` is the
dimension of `SL(2, R)`. The self-consistent tree-scale coupling
`K_STAR = 0.86196052` is the fixed point of the joint matter-sector
closure. The mass sector closes through `a_1² · K*² = N_sector` with
`N = {4, 9, 24}`. The neutrino sector closes at depth
`35 = q_2³ + q_3³` with `m_1/m_3 = 1/8` exact and a solar correction
`−1/36`. Gauge residuals are Fibonacci-square and gauge-integer-square
finite-K corrections to tree-scale rationals. Everything is closed
within observational precision; only the dimensionful scale
`v = 246 GeV` is input.

## Branch hygiene

- **PR on branch creation.** Every new branch gets a PR at the moment
  it is pushed, with a defined merge path. A branch without a PR is
  an orphan.
- **Modifications stay close to additions.** A new branch with N pure
  additions and 0 modifications cannot diverge. Modifications to
  existing files need fast merge windows.
- **Branches measured in minutes, not days.** The window between push
  and PR should be tighter than the time it takes to write the PR
  description.
- **No divergence without a resolution plan.** Every branch that adds
  divergence must have a defined plan for how the divergence resolves.
- **Trust HEAD, not history.** Recent commits often retract or refine
  earlier work. If a numerical claim on an old commit disagrees with
  the HEAD, trust the HEAD.
- **Trust code + topology, not summary prose.** Anything that
  restates state in markdown will drift. The derivation scripts and
  `FRAMEWORK_TOPOLOGY.md` are the canonical surface.
