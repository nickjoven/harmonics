# Mediant vs. flow: the calculation run — flow fingerprint absent at K=1

The decisive test posed in `mediant_vs_flow_problem.md`, run
(`mediant_vs_flow_calc.py`).

**Result: the universal flow fingerprint `D ≈ 0.8700` is
structurally absent at the framework's K=1. The continuous
*critical* flow is eliminable; discrete-fundamental is favored
(by absence-of-fingerprint + parsimony — not a positive proof).**

## What was computed

The single decidable difference (`mediant_vs_flow_problem.md`) is
the K=1 complement, and it is decided by a *regime* number — the
total mode-locked tongue measure:

- **Critical circle map** (the only place the Jensen–Bak–Bohr
  universal dimension `D ≈ 0.8700` exists) is the **knife-edge**:
  tongues exactly fill, total measure `Σ → 1⁻`, complement is a
  measure-zero Cantor set of dimension `D ≈ 0.8700`.
- **Sub-critical**: `Σ < 1`, complement has positive measure,
  dimension `1`.
- **Past filling** (`Σ > 1`): tongues over-cover, complement is
  **empty** (complete tree) — *no measure-zero fractal, so
  `D ≈ 0.8700` cannot exist*.

Using the framework's **own** perturbative tongue width
`w(p/q, K) = 2 (K/2)^q / q` (`born_rule.md`,
`a1_from_saddle_node.md`), summed over all reduced `p/q ∈ [0,1)`
(`φ(q)` per denominator) at K=1:

    Σ_{p/q} w(p/q, K=1)  =  1.561666   (converged; stable to 6 dp by q≤30)

`Σ = 1.000` already at `q=1`; converges to `≈ 1.5617`. **`Σ > 1`
by a wide, robust margin** — not a knife-edge artifact.

## Verdict

The framework's K=1 is **past exact-filling: the complete-tree
regime** (`Σ ≈ 1.56`, far from the critical knife-edge `Σ = 1`).
Therefore:

- The measure-zero Cantor complement does not exist at K=1 (the
  tree is complete). The universal critical fingerprint
  `D ≈ 0.8700` is **structurally unrealizable** there — it lives
  *only* at `Σ = 1`.
- This is exactly the **(Mediant)** prediction: at K=1 the tree
  is complete, no continuous fractal complement, no universal
  `D`.
- It is incompatible with **both** flow sub-readings: the
  *critical* flow (needs `Σ = 1`, `D ≈ 0.87`) and the
  *sub-critical* flow (needs `Σ < 1`, positive-measure `D = 1`
  complement).
- The one regime that *could* give `Σ > 1` for a continuous map —
  *supercritical / overlapping (chaotic)* — is independently
  excluded by `framework_status.md` "Eliminated": the dynamics
  are **Adler-only / gradient descent on a static potential,
  monotone, not a twist map, not chaotic**. A monotone Adler
  flow cannot be supercritical-chaotic.

So every continuous-flow reading is excluded; only "complete
discrete tree" (Mediant) is consistent. The continuous flow is
**eliminable by parsimony** — the same move as the NAND/4→2
tightening — and the universal number `D ≈ 0.8700` is **not a
framework prediction**.

## Honest scope (do not overclaim)

1. **This is elimination-by-absence + parsimony, not a positive
   proof of discrete-fundamental.** It shows the last foundational
   competitor's *one decisive parameter-free fingerprint* is
   structurally absent at K=1, and that no flow regime is
   consistent with the framework's own structure + recorded
   eliminations. It does not *construct* a theorem that the
   substrate is discrete; it removes the rival.
2. **The width formula is a regime indicator, not an exact K=1
   dimension.** But the verdict only needs `Σ` to robustly exceed
   `1` (it does, ≈1.56, converged) — and the framework's *own*
   Finding-3 disposition independently states K=1 is the
   complete-tree regime where tongue-width truncation degenerates.
   Two independent lines agree; the conclusion is robust to the
   formula's precision (one would need the true aggregate width
   ~36% smaller *and* then only reach the knife-edge, not
   sub-critical).
3. The residual is *philosophical*: absence of the flow-only
   fingerprint + parsimony, corroborated by independent
   structural position — strong, but distinct from a positive
   discreteness proof.

## What this closes

- **`#FLOW` (competitor #1) decisively weakened.** Its sole
  parameter-free discriminator (`D ≈ 0.8700`) is shown
  structurally absent at K=1; no flow regime is consistent.
  Combined with **#2 eliminated** (`#TICK`,
  `tick_continuum_construction.md`), both foundational
  competitors are now down: #2 by construction, #1 by
  absent-fingerprint + parsimony.
- Discrete-fundamental is **favored** (now strongly), not proven.
  The honest standing: no surviving competitor; no positive
  no-go either.

## Status

Class 3 (decisive measurement + honest scope). No new primitive.
Runs the `mediant_vs_flow_problem.md` test; verdict is regime
(complete-tree), corroborated by the framework's independent
Finding-3 position and the recorded Adler-only/monotone
eliminations. `D ≈ 0.8700` is not a framework prediction.

## Cross-links

- `mediant_vs_flow_problem.md` — the posed question; this is its
  run.
- `mediant_vs_flow_calc.py` — the reproducible computation.
- `framework_status.md` — "Eliminated": Adler-only / not-a-twist-
  map / not-chaotic — excludes the only continuous regime that
  could give `Σ > 1`.
- `thread_chronology.md` — `#FLOW` updated: calculation run,
  fingerprint absent, flow eliminable by parsimony.
- `tick_continuum_construction.md` — `#TICK`/#2 eliminated;
  with this, both foundational competitors are down.

## One-line summary

The framework's own K=1 tongue-width sum is `Σ ≈ 1.5617 > 1`
(converged) — the complete-tree regime, far from the critical
knife-edge `Σ = 1` where the universal `D ≈ 0.8700` lives — so
the continuous flow's sole parameter-free fingerprint is
structurally absent, every flow regime is excluded (critical and
sub-critical by `Σ`, supercritical by the recorded
Adler-only/monotone eliminations), and competitor #1 falls by
absence-of-fingerprint + parsimony (not a positive proof);
combined with #2 already eliminated, no foundational competitor
survives.
