# Premise Ledger

Machine-readable dependency anchors for the derivation corpus,
checked by `scripts/drift/check_premises.py`.

**Trust boundary:** a clean check is consistency accounting, not a
soundness certificate — statuses are recorded human attestations,
undeclared premises are invisible, and green means only "no detected
inconsistency." The portable pattern, its threat model (deterministic
theater), and the mandatory countermeasures are documented in
`docs/premise-ledger-pattern.md`. Reds are theorems; greens are not.

## Schema

Anchors are HTML comments (parser-safe, invisible to renderers and
retrieval chunkers), one per line, anywhere in a doc:

```
<!-- provides: <name> status=<status> -->
<!-- premises: <name>@<providing-doc-basename>, <name2>@<doc2> -->
```

- `<name>`: kebab-case, globally unique per corpus — **one name, one
  providing doc**. Two docs providing the same name is a hard error
  (rival conventions must collide, not fork).
- `status` vocabulary:
  - `axiom` — assumed, stated as such
  - `definition` — true by construction; makes no empirical claim
  - `proven` — proof in this doc, checked
  - `derived` — follows from premises in this doc
  - `imported` — external mathematics/data, cited
  - `conditional` — derivation valid, but ≥1 premise is not settled
  - `conjectured` — asserted; no derivation exists
  - `fitted` — value obtained from observation; not a prediction

## Propagation rule

A doc may declare `provides: X status=proven|derived` **only if** no
premise it cites resolves to `conjectured`, `fitted`, or
`conditional`. Otherwise the strongest allowed status is
`conditional` (or weaker). The checker enforces this transitively —
demoting one anchor flags every downstream `proven`/`derived` that
rests on it.

## Checks (all graph algorithms, O(V+E))

1. **Resolution** — every `premises:` entry names an anchor that
   exists in the named doc.
2. **Uniqueness** — no name has two providers.
3. **Propagation** — the rule above, transitively.
4. **Cycles** — the premise graph is acyclic.

## MANIFEST rows

Scorecard rows in `MANIFEST.yml` may declare a `premises:` list of
the same `name@doc` entries. A row whose premises resolve to an
unsettled anchor may not claim `Class 5` / `exact` in its
`closure_status` unless the status text itself carries the hedge
(conditional / retracted / reference / imported / fitted). This is
the repercussive-feedback guard: a demotion at a providing doc
reaches the scorecard mechanically.

## Ratchet policy

Enforcement is incremental: docs that declare anchors are checked;
docs without anchors are not (yet) required to have them. Backfill
order: spine docs first. A doc touched by any correction batch gets
anchors as part of the edit.

## Imported premises registry

External mathematics and physics the framework consumes without
deriving. Each anchor makes the import explicit so SPINE edges and
doc `premises:` lines can resolve to it. `imported` is a settled
status — the fact is established in the cited literature, not here;
what the framework *does* with the import is what carries a status
of its own.

<!-- provides: energy-conservation status=imported -->
- `energy-conservation` — energy conservation in closed systems
  (Noether's theorem for time-translation invariance). Standard
  classical mechanics.
<!-- provides: stability-under-coupling status=imported -->
- `stability-under-coupling` — weakly coupled self-sustained
  oscillators phase-lock across finite parameter windows (Arnold
  tongues). Synchronization theory; Pikovsky–Rosenblum–Kurths,
  *Synchronization* (2001).
<!-- provides: s1-compactness status=imported -->
- `s1-compactness` — S¹ is compact and π₁(S¹) ≅ ℤ: every continuous
  self-map of the circle carries an integer winding number. Standard
  topology.
<!-- provides: sl2z-action-on-upper-half-plane status=imported -->
- `sl2z-action-on-upper-half-plane` — SL(2, ℤ) acts on the upper
  half-plane by Möbius transformations with the standard fundamental
  domain and its tessellation. Standard modular-group theory.
<!-- provides: dim-sl2r-equals-3 status=imported -->
- `dim-sl2r-equals-3` — SL(2, ℝ) is a 3-dimensional Lie group.
  Standard Lie theory. (Whether any completion of SL(2, ℤ) into
  SL(2, ℝ) is forced is a separate, open framework claim — see the
  spine edge `forces-three-dimensions`.)
<!-- provides: lissajous-figure-at-rational-frequency-ratio status=imported -->
- `lissajous-figure-at-rational-frequency-ratio` — a two-dimensional
  harmonic orbit with rational frequency ratio closes into a
  Lissajous figure. Classical kinematics (Lissajous 1857).
<!-- provides: wightman-axiom-convention status=imported -->
- `wightman-axiom-convention` — the Wightman axioms as the convention
  fixing what counts as a quantum field theory. Streater & Wightman,
  *PCT, Spin and Statistics, and All That*.
<!-- provides: standard-model-silences status=imported -->
- `standard-model-silences` — the Standard Model treats its ~19
  Lagrangian parameters as measured inputs and does not derive them.
  PDG reviews.
<!-- provides: k1-tongue-coverage-discontinuity status=imported -->
- `k1-tongue-coverage-discontinuity` — for the standard circle map
  the mode-locked intervals fill the critical line K = 1 up to
  measure 1 (the complete devil's staircase), while for K < 1 the
  locked measure is strictly below 1. Jensen, Bak & Bohr (1983–84).
<!-- provides: stern-brocot-self-similarity-at-golden-ratio-winding status=imported -->
- `stern-brocot-self-similarity-at-golden-ratio-winding` — the
  winding-number structure is locally self-similar at the golden-mean
  winding (continued fraction [1, 1, 1, …]), with Shenker's scaling
  δ ≈ 2.834 at criticality (not φ² = 2.618; see ERRATA on the
  earlier φ² claim). Shenker (1982).
