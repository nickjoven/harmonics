# Koide form substrate derivation — iteration 14 (closing note)

## Status

**Closing note.** Iterations 1–13 are documented as a productive
null result. Koide `K_lepton = 2/3` is moved to the empirical
shelf alongside `sin²θ_W`, `θ_13 PMNS`, the CKM angles, and other
SM-empirical relations the framework notes but does not derive
from current substrate apparatus.

The iteration arc itself is the diagnostic. Thirteen iterations
narrowed the structural gap from "derive Koide algebraic form"
(iter 1) to "one residual structural assumption: uniform
eigenvalue magnitude of the substrate's three-generation
quadratic form `M = q_3 I − q_2 J`" (iter 13). That residual was
not closed by any iteration; the closing chain that would
substrate-derive uniform eigenvalue magnitude has not been
produced.

Under the framework's basepoint principle: Koide is **operationally
open** (no obstruction proven; no derivation produced) rather than
**structurally declined** (no torsorial-decline argument has been
exhibited). It joins the empirical co-shelf as an open item with
documented structural-consistency analysis.

Class: closing note for a productive null iteration arc (Class 3,
arc-closing step).

---

## What iterations 1–13 established

### The structural-consistency theorem (iter 13)

Iteration 13's uniqueness theorem stands as the iteration arc's
strongest analytical content:

`M = q_3 I − q_2 J` is the **unique** 3×3 symmetric matrix
satisfying three constraints:

1. **`S_3`-equivariance** — substrate-derived from three
   indistinguishable generations (`generation_mechanism.md` §1).
2. **Lorentzian `(2, 1)` signature** — substrate-derived via
   iteration 11's chain: cube identity → `(q_2, q_3) = (2, 3)`
   → `Q = q_2/q_3 = 2/3 > 1/3` → Lorentzian
   (`mass_sector_closure.md`, `klein_bottle.md` D19).
3. **Uniform eigenvalue magnitude `q_3`** — residual structural
   assumption, not independently substrate-derived.

Under (1) + (2) + (3), the Koide constraint `K = q_2/q_3 = 2/3`
follows immediately from `M v · v = 0` evaluated on `v = √m`.

The theorem is genuine analytical content: it documents that
the substrate's apparatus is *consistent with* `K = 2/3` modulo
exactly one structural assumption. It is *not* a derivation that
forces `K = 2/3` from substrate primitives alone.

### The ingredient-by-ingredient negative result (iter 12)

Iteration 12 documented that the alternative derivation path —
deriving M's diagonal and off-diagonal weights from independent
substrate quantities — does not work cleanly. Combining
substrate-derived diagonal `q_3` (from `k_lepton / n_gens =
q_3²/q_3`) with substrate-derived off-diagonal `−q_2` (from
Klein-antipodal Z_2 of order `q_2`) requires half-integer weights
or non-substrate-natural corrections.

This is a useful negative result: it rules out the
ingredient-by-ingredient path and forces the unified-object
derivation that iteration 13 then completed.

### The Lorentzian signature substrate-forced chain (iter 11)

Iteration 11 established that the signature of M as Lorentzian
`(2, 1)` is substrate-forced through a chain of
substrate-internal steps:

    cube identity q_2³ = q_2 + 2 q_3
       →  (q_2, q_3) = (2, 3) unique positive-integer solution
       →  Klein-bottle ratio Q = q_2/q_3 = 2/3 > 1/3
       →  M's signature is Lorentzian (2, 1)

Each step is substrate-internal. This is a real structural result
inherited by iteration 13's uniqueness theorem as constraint (2).

### What earlier iterations contributed

- Iter 1–5 reframed Koide geometrically (cos²θ = 1/3), explored
  `S_3` vs `V_4` representations, and arrived at the
  `q_3 : MEDIANT` structure.
- Iter 6 established that the cube identity is necessary but not
  sufficient — a (b)/(c) degeneracy between raising/lowering
  pieces remained.
- Iter 7–8 explored candidate mechanisms (chirality, cascade
  depth) for breaking the degeneracy; results inconclusive.
- Iter 9 ran the empirical Path A test using `three_basins.py`;
  null result on identifying basin widths as mass ratios.
- Iter 10 surfaced the reversibility-class observation (Koide is
  Class A algebraic, not Class B probabilistic), retroactively
  validating the earlier choice to pursue algebraic derivation
  rather than dynamical basin-selection.

These contribute progressively to the narrowing-but-not-closing
pattern that characterizes the arc.

---

## What the arc did not establish

Under the new disposition (post-discipline shift documented in
the conversation `2026-05-31`):

- **Koide `K_lepton = 2/3` is not substrate-derived.** The
  iteration arc produced a structural-consistency result (iter
  13) modulo one assumption that the substrate does not
  independently force. This is operationally open, not closed.

- **`m_μ/m_e` at 0.96% is not a framework prediction.** The
  apparent 0.96% match in `generation_mechanism.md` §4 imports
  the Koide constraint `Q = 2/3` empirically — solving for `m_μ`
  given the bare-tree `τ/e` and the imposed Koide relation. The
  framework's actual substrate prediction for `m_μ/m_e` is the
  bare-tree value `7^(5/2) = 129.6`, which differs from observed
  `206.77` by 37%. The 37% gap is open.

- **The `√(5/2)` m_μ dressing reading is not framework-supported.**
  The observation that `m_μ_observed / m_μ_bare ≈ 1.595 ≈ √(5/2)`
  is a one-parameter fit on one observable with no
  cross-check. Under the framework's numerology discipline, this
  is selection-bias risk, not a derivation.

- **The self-field NLO proposal does not survive the cross-check.**
  Symmetric self-field coupling `α ≈ W_A = 1/18` closes PMNS θ_12
  (33.36° vs observed 33.41°) but worsens θ_13 (31.93° vs
  observed 8.6°, larger gap than the LO 28.13°). The mapping of
  self-field cloud onto the V_4 dark D state was also
  mechanically incoherent — dark D is a peer V_4 state, not a
  cloud surrounding observables.

---

## Position on the empirical shelf

Koide `K_lepton = 2/3` joins:

- `sin²θ_W ≈ 0.231` — gauge mixing parameter, framework notes,
  does not derive
- PMNS `θ_13 ≈ 8.6°` — structural failure of bare Fritzsch-form
  prediction (28.13°); no NLO mechanism
- All CKM angles — require SM RG running, orthogonal to
  framework
- `m_μ/m_e` 37% bare-tree gap — open without Koide import
- Muon g−2 anomaly — no framework apparatus

These items share administrative status (open in the
basepoint-principle sense — operational gap, no obstruction
proven) but differ structurally:

- Koide has an *exact* rational match to an independently derived
  framework primitive (`Q = q_2/q_3 = 2/3` from
  `klein_bottle.md` D19). Whether this is a coincidence or a
  structural correspondence waiting to be derived is the open
  question.
- `sin²θ_W` has no analogous framework correspondence.
- The other empirical-shelf items each have their own structural
  positions.

Koide's shelf-position is closer to the framework's apparatus
than `sin²θ_W`'s, but it has not crossed the line into the moat.
Same shelf, different positions on it.

---

## What this arc contributes to the framework

### Documented structural reach for Koide

The arc's net analytical content (iter 11–13) is a complete
characterization of how close the framework's current substrate
apparatus gets to Koide:

- The matrix `M = q_3 I − q_2 J` that would yield Koide is *unique*
  given three named constraints.
- Two of three constraints are substrate-derived; the third is
  not.
- Multiple structural-consistency arguments (S_3 representation
  theory, V_4 partition counting, cube identity decomposition,
  pair-wise Q-conservation, dark-state coupling) each touch part
  of the substrate's apparatus relative to Koide but none forces
  closure.

This documentation prevents future iterations from rediscovering
the same partial results.

### The methodological pattern (productive null arc)

The 13-iteration narrowing-but-not-closing pattern is itself
informative. When a productive iteration arc converges on a
single named residual that the framework cannot independently
derive, the residual is the substrate's reach-boundary. Naming
it explicitly distinguishes "this residual is a genuine open
operational gap" from "we haven't tried hard enough" or "the
problem is closed and we're in denial."

This pattern is what the basepoint-principle's discriminator is
built to catch. The arc demonstrates the discriminator working
correctly: 13 iterations of honest effort, single named residual,
no closure, status set to operationally open.

### The next-leg directions

The arc's residual ("uniform eigenvalue magnitude of M") points
to candidate substrate mechanisms that have not been attempted:

- **Horn-branch dissipation profiles** — could derive eigenvalue
  magnitude from substrate→tree regime-crossing dynamics.
  Independently motivated by Class B (`m_μ` at 37%) and Class C
  (PMNS θ_12 at 10%) work.
- **Torus-branch winding-number geometry** — could derive
  `(q_2, q_3)` and the cube identity from torus topology rather
  than as independently posited primes. Indirectly supports
  Koide via cleaner substrate-prime derivation.
- **Axial-trajectory conservation audit** — checks whether the
  framework's existing apparatus carries the three
  ± axes (direction, chirality, scale) at the resolution that
  horn-branch dissipation work requires.

These directions are documented as the next leg's targets. They
are not within this iteration arc; they constitute the
post-arc work.

---

## The disposition update

`framework_status.md` (or equivalent) should be updated to
reflect:

| Item | Previous | Updated |
|---|---|---|
| Koide `K_lepton = 2/3` | "Floor closure (Koide form imported)" | Empirical shelf, sin²θ_W class — open, not declined |
| `m_μ/m_e` | "0.96% match (Floor)" | Bare-tree 37% gap, open |
| Iter arc | (active) | Closed as productive null |

`substrate_prediction_selection.md` should be closed at
**Outcome 2** (per-prediction structural verdict): Koide is the
verdict's first instance — undecided, framework declines to
claim derivation.

---

## Cross-links

- `koide_form_substrate_iteration_1.md` through
  `koide_form_substrate_iteration_13.md` — the iteration arc.
- `mass_sector_closure.md` — substrate-derived sector mode
  budgets `k_lepton = q_3²`, `k_quark = q_2³`, cube identity.
- `klein_bottle.md` (D19) — Klein-bottle population ratio
  `Q = q_2/q_3 = 2/3`; independent of Koide.
- `generation_mechanism.md` (D34) — three-generation `V_4`
  structure; bare-tree mass formula; mixing-angle apparatus.
- `mixing_angle_audit.md` — framework's tree-level PMNS prediction
  match (θ_12, θ_23) and miss (θ_13).
- `basepoint_principle.md` — operational-open vs
  structurally-declined discriminator.
- `substrate_prediction_selection.md` — selection thread,
  closing at Outcome 2.
- `framework_status.md` — disposition table.

---

## One-line summary

Iterations 1–13 are closed as a productive null arc; the 13-step
narrowing from "derive Koide algebraic form" to "one residual
structural assumption (uniform eigenvalue magnitude of `M = q_3
I − q_2 J`)" produces a real structural-consistency theorem
(iter 13) showing M is uniquely determined by three constraints
of which two are substrate-derived, but the third constraint is
not substrate-forced and no closure was produced; Koide
`K_lepton = 2/3` is therefore moved to the empirical shelf
alongside `sin²θ_W` and other framework-noted-but-not-derived
quantities, with the iteration arc's documentation serving as
analytical record of how the framework's apparatus reaches
Koide and where it stops; `m_μ/m_e` is also honestly demoted
from the apparent 0.96% Koide-imported match to the bare-tree
37% gap (which the framework predicts as `7^(5/2) = 129.6` vs
observed `206.77`); next-leg work targets the horn-branch
(regime-change dissipation for Class B + C residuals),
torus-branch (winding-number geometry for `(q_2, q_3)`), and
axial-trajectory conservation audit (chirality resolution
required for horn-branch dissipation derivations), with the
audit serving as precondition for the horn-branch work.
