# Q mod 2 conservation theorem

## Status

**Standalone theorem articulated** for substrate inviolable #1
(`substrate_determinism.md` L166-167) — the Z₂ topological-charge
conservation that had been committed as a structural inviolable
but was flagged "not a closed standalone theorem — the explicit
standalone theorem is *not yet articulated*"
(`framework_status.md` L31; `phenomenology_cross_reference.md:439`).

This doc supplies the missing standalone statement. It does not
introduce new content: every ingredient already lived in the
corpus (`klein_bottle.md` for the antiperiodicity rule;
`sine_gordon_substrate.md` §"Z_2-graded topological charge from
Klein topology" for the kink↔antikink identification; the framework's
locality concept for the qualifier "local"). The contribution is
the synthesis — packaged as a theorem with a precise statement,
a proof, an explicit definition of "local," exhibited
consequences, and falsifiers.

No new primitive.

---

## The theorem

**Theorem (Q mod 2 conservation under local processes).** Let
`K² = [0,L_x] × [0,L_y]` be the Klein bottle, identified by

    (x, 0) ∼ (x, L_y)             [periodic in y]
    (0, y) ∼ (L_x, L_y − y)       [antiperiodic + reflection in x]

Let `φ : K² × ℝ → ℝ` be a continuous-in-`t` sine-Gordon field
configuration satisfying the induced antiperiodicity condition

    φ(x + L_x, y, t)  =  − φ(x, L_y − y, t)       (∗)

for all `t`. Let `Q(t) ∈ ℤ/2ℤ` denote the topological (winding)
charge per antiperiodic loop, defined by the kink-number reduction
of §"Q is well-defined mod 2" below. Then for any **local process**
— a continuous-in-`t` deformation `φ_t` whose instantaneous
support `supp(∂_t φ_t) ⊂ K²` is contained in an open set `D ⊂ K²`
of spatial diameter strictly less than `L_x` — the charge is
preserved:

    Q(t)  ≡  Q(0)   mod 2,    for all t.

Equivalently: no process whose support fits inside any single
antiperiodic-loop-free chart of `K²` can change `Q mod 2`. To
change `Q mod 2`, a process must encircle the antiperiodic
direction — by definition, a non-local (global) operation.

### Scale-qualification clause (added 2026-06)

The theorem's diameter condition `< L_x` is **scale-qualified by
construction**. The proof and statement operate within scale
ranges where Klein-bottle topology is well-defined — i.e., where
the antiperiodic-cycle structure on `K²` exists as a substrate
fact. Per `conservation_scale_stratification_audit.md`:

- **Standard scale** (K_STAR ≈ 0.86, our pocket): canonical
  Klein-bottle substrate; theorem applies as stated. Q mod 2 is
  universal.
- **Hubble scale** (cosmological boundary at finite mode count
  12.66, w* ≈ 0.83): Klein-bottle topology persists; theorem
  applies within the 12.66-mode horizon. The cosmological
  boundary is a mode-count cutoff, not a topological transition,
  so Q mod 2 is preserved within the horizon.
- **Planck scale**: the diameter condition automatically
  scale-qualifies the theorem. Any process with support of
  spatial diameter `< L_x` includes Planck-scale processes by
  construction (Planck length is many orders of magnitude
  smaller than `L_x`). So Q mod 2 conservation is **trivially
  preserved** at Planck scales: no Planck-scale process can
  encircle the antiperiodic direction, because its support is
  far smaller than `L_x`. This is "conserved by inability rather
  than by inviolability" — the theorem doesn't claim Planck-scale
  Q mod 2 is *forced* to remain definite, only that no
  Planck-scale process can *change* it. If Planck-scale substrate
  is non-topological (NCG, foam, causal sets, etc.), Q mod 2 as
  defined here may become ill-defined rather than non-conserved
  at those scales — a regime distinction the theorem doesn't
  attempt to derive.

Equivalently: this theorem governs Q mod 2 conservation at
scales where smooth-manifold Klein-bottle topology is the
substrate's operational form. The framework's inviolable #1
status (`substrate_determinism.md`) is correctly read as
*topology-conditional*: universal at standard and Hubble scales;
contingent at Planck where the topological basis may dissolve.
For the algebraic counterpart that survives all scales without
topological dependence, see dissipation (D46,
`rank1_temporal_causation.md`).

See `conservation_scale_stratification_audit.md` for the
three-candidate resolution of the Planck contingency (resolution
(ii), the scale-qualification clause used here, recommended).

---

## Proof

### Step 1 — Q is well-defined mod 2 on K²

On the orientable universal cover `ℝ × [0, L_y]` of `K²` along
the antiperiodic direction, the sine-Gordon vacuum set is the
discrete set `φ ∈ 2πℤ`. For a configuration interpolating between
vacua at `x → ±∞` (or between two boundary cycles on a finite
patch), the integer kink-number

    Q̃  =  (1/2π) · [φ(+∞, y) − φ(−∞, y)]    ∈ ℤ           (1)

is well-defined and integer-valued (vacuum-set discreteness;
standard sine-Gordon).

The Klein antiperiodicity (∗) acts on lifted configurations by

    φ̃(x + L_x, y)  =  − φ̃(x, L_y − y).                     (2)

Under this deck transformation, a kink profile with
`φ̃ → 0, 2π` becomes one with `φ̃ → 0, −2π` — a kink lifts to an
antikink:

    Q̃  ⟶  −Q̃                                              (3)

(`sine_gordon_substrate.md` L170-181, verbatim). Therefore on
`K²` itself, `Q̃` is **not** well-defined as an integer; only
the residue class `Q ≡ Q̃ mod 2` descends, because

    Q̃  ≡  −Q̃   (mod 2),     i.e.   2Q̃ ≡ 0 (mod 2)         (4)

holds for every integer. This defines `Q ∈ ℤ/2ℤ` on `K²` as the
unique invariant of the equivalence class `{Q̃, −Q̃}`. (Single-kink
configurations carry `Q = 1`; kink–antikink pairs and the vacuum
carry `Q = 0`; etc.)

### Step 2 — Definition of "local process"

A continuous-in-`t` deformation `φ_t : K² → ℝ` is a **local
process** at instant `t` iff there exists an open set `D ⊂ K²`
with:

(L1) `supp(φ_t − φ_0) ⊂ D`, and
(L2) `diam(D) < L_x`.

(L2) is the operative locality content: it forces `D` to be
strictly smaller than the antiperiodic loop, which makes `D`
contained in an orientable chart of `K²` (the chart-trivialization
condition for the non-orientable cover). Concretely, any open
ball of diameter `< L_x` on `K²` lifts to a disjoint union of
balls on the universal cover, none of which wrap the antiperiodic
direction.

(L1)+(L2) together are the substrate-level form of locality used
throughout the framework (`framework_lagrangian.py`'s nearest-
neighbor coupling; `tick_continuum_construction.md`'s context
window `L_x`). Note that the locality threshold is *exactly* the
antiperiodic loop length — no smaller scale and no separate
ε-margin. The Klein topology determines its own scale.

### Step 3 — Local processes preserve Q mod 2

Fix a local process `φ_t` with supporting open set `D` satisfying
(L1)–(L2). Choose a representative antiperiodic loop
`γ : [0, L_x] → K²` (an x-cycle at fixed `y = y_0`) with
`γ ∩ D = ∅`. Existence of such a `γ`: since `D` has diameter
`< L_x` and there is a one-parameter family of antiperiodic loops
(one per `y₀ ∈ [0, L_y]`), the obstruction set `{y : γ_y ∩ D ≠ ∅}`
has measure less than `L_x` along the `y`-direction in the worst
case — strictly speaking, at most `diam(D) < L_x`. The complement
is non-empty; pick `γ` from it.

Along `γ`, the field `φ_t |_γ` is *unchanged* by the deformation
(by (L1) and `γ ∩ D = ∅`). Therefore `Q̃_t` evaluated on the
universal-cover lift of `γ` — i.e., the winding of `φ_t` along
`γ` measured in `2π` units — is *unchanged*:

    Q̃_t(γ)  =  Q̃_0(γ).                                     (5)

The mod-2 reduction is invariant under loop-representative choice
(Step 1, eq. 4): the well-defined `K²`-invariant `Q ∈ ℤ/2ℤ` is
the same evaluated on `γ` or any other antiperiodic loop. Hence

    Q(t)  =  Q̃_t(γ) mod 2  =  Q̃_0(γ) mod 2  =  Q(0).        (6)

### Step 4 — Non-local processes are necessary to change Q mod 2

Conversely, suppose a deformation `φ_t` changes `Q mod 2` between
`t = 0` and `t = t₁`. Pick any antiperiodic loop `γ`. The integer
winding `Q̃(γ)` is a homotopy invariant of `φ|_γ` (the discrete
vacuum set forbids continuous winding jumps within a fixed
lift). For `Q mod 2` to change, the winding along `γ` must change
parity, which requires `supp(φ_{t₁} − φ_0)` to intersect `γ`.
This must hold for **every** antiperiodic loop `γ` — there is no
representative whose mod-2 winding is unaffected, by the loop-
representative-independence of `Q mod 2`. Hence

    supp(φ_{t₁} − φ_0)  intersects every antiperiodic loop      (7)

which forces

    diam(supp(φ_{t₁} − φ_0))  ≥  L_x.                        (8)

(8) is the negation of (L2): the deformation is not local. QED.

---

## What this says (and what it does not)

**It says:** `Q mod 2` is preserved by any process that does not
encircle the antiperiodic direction. The only way to change
`Q mod 2` is a process whose support spans the antiperiodic loop —
the kink ↔ antikink global conversion of
`sine_gordon_substrate.md` §"Z_2-graded topological charge from
Klein topology," whose rate is set by the loop-traversal time
`L_x / c_loop`.

**It does not say:** there is no process that can change `Q mod 2`.
The global antiperiodic-loop traversal *is* such a process; the
theorem classifies it as non-local, not as forbidden. The
intrinsic CP-like asymmetry consequence
(`sine_gordon_substrate.md` L210-215) survives precisely because
the substrate *does* permit this non-local conversion, at a rate
fixed by its own geometry.

**Bright line.** This is a topological invariance under a
specific locality class — a classification result. It is not a
prediction of any rate, baryon-asymmetry magnitude, or empirical
observable. The consequences listed below are structural, not
quantitative; quantitative predictions are explicitly flagged as
separate open items in `sine_gordon_substrate.md` Status (Opens
1–4).

---

## Distinct from the field half-twist Z₂

The theorem governs the **coordinate antiperiodicity** Z₂ — the
gluing rule (∗) acting on the spatial coordinate `x`. The
framework's *other* Z₂, the **field half-twist** `θ → θ + π`
acting on the target space (`framework_lagrangian.py` Part 6),
is independent. The half-twist gives spin-statistics and CPT
(see `cone_twist_substrate.md` §5.2, inviolable #7); it does
not give `Q mod 2` and is not what this theorem invariant-tracks.

The mapping is `sine_gordon_substrate.md` Table at L197-199:

| Z₂ structure          | Action                              | Consequence                       |
|---|---|---|
| Coordinate antiperiodicity | `f(x+L_x, y) = −f(x, L_y−y)`       | This theorem; kink↔antikink under loop traversal |
| Field half-twist          | `θ → θ + π` on target              | Spin-statistics, CPT, AB-phase = π |

Both are forced by the Klein-bottle commitment; this theorem
relies only on the first.

---

## Exhibited consequences

1. **Soliton number is mod-2 conserved.** A region dominated by
   kinks can convert to antikink-dominated only via global
   antiperiodic-loop transit (`sine_gordon_substrate.md` L207-209).
2. **CP-like asymmetry is intrinsic to the substrate, not added
   by hand.** Any observed kink–antikink asymmetry is a residual
   of an originally larger asymmetry, reduced by mod-2
   accumulation (`sine_gordon_substrate.md` L210-212).
3. **The conversion rate is geometric, not per-sector.** It
   depends on the loop-traversal time `L_x / c_loop`, set by
   substrate geometry alone, not on sector-specific physics
   (`sine_gordon_substrate.md` L213-215).
4. **The inviolable now has its rigorous form.** Substrate
   inviolable #1 (`substrate_determinism.md` L166-167, "Z₂
   topological charge conservation (mod 2). Klein-bottle
   topological rigidity. No local process changes `Q mod 2`")
   is the statement just proved, with "local" the precise
   (L1)+(L2) definition above.
5. **The locality scale is intrinsic.** The locality threshold
   in (L2) is `L_x`, the antiperiodic-loop length itself — no
   independent scale enters. This is consistent with the
   framework's broader pattern: the substrate sets its own
   locality scale (the context window of
   `tick_continuum_construction.md`).

---

## Falsifiers

- **Direct dynamical violation.** A continuous-in-`t` deformation
  of `φ` with support `D` of diameter `< L_x` (so satisfying (L1)
  and (L2)) that nonetheless changes `Q mod 2` would falsify the
  theorem. Step 3's proof rests on the vacuum-set discreteness of
  sine-Gordon plus the well-definedness of mod-2 winding along an
  antiperiodic loop; either failing would void the result.
- **Loop-traversal-rate falsifier.** A measured kink ↔ antikink
  conversion rate that does not match `~ c_loop / L_x` (with
  `c_loop` set by substrate constants), in the absence of a
  competing global mechanism, would not falsify the *theorem*
  but would falsify the substrate's identification of
  `(L_x, c_loop)` — pushing into the same residual class as
  `sine_gordon_substrate.md` Open 2 (loop-traversal time
  computation).
- **Topology falsifier.** If the substrate were not the Klein
  bottle but a torus (both directions periodic), `Q ∈ ℤ` would
  be the conserved charge and there would be no mod-2 reduction;
  intrinsic CP-asymmetry would be lost. The theorem is
  contingent on the Klein commitment.

---

## Why this matters

The theorem closes a long-standing flag in the corpus: inviolable
#1 was load-bearing across `substrate_determinism.md`,
`k_inflation_seam_obstruction.md` L112, and the soliton-sector
arguments in `sine_gordon_substrate.md`, but no doc carried the
explicit statement-and-proof in standalone form. The Bell-evasion
argument for branch (B) of substrate determinism
(`substrate_determinism.md` L205-210: "the framework's nonlocality
is topological (Klein-bottle Z₂), not hidden-variable") rests on
this Z₂ being a *genuine* topological invariant, not a heuristic
— which is what this theorem establishes.

Class: foundational consolidation (Class 3, articulation). The
arc the doc closes is the "explicit theorem not yet articulated"
flag, not a new prediction.

---

## Cross-links

- `substrate_determinism.md` — inviolable #1 (this doc supplies
  the standalone form).
- `sine_gordon_substrate.md` — the kink↔antikink identification
  (the ingredient consumed in Step 1 / 3 / 4).
- `klein_bottle.md` — the antiperiodicity rule (∗); see L104.
- `framework_lagrangian.py` Part 6 — the *other* Z₂ (field
  half-twist), distinguished above; not used here.
- `cone_twist_substrate.md` §5.2 — AB-phase = π, the half-twist
  Z₂'s consequence (inviolable #7), parallel-but-distinct.
- `phenomenology_cross_reference.md:439` — the EPR/Bell pointer
  noting "explicit theorem not yet articulated"; this doc is the
  reference.
- `framework_status.md` Survives row for inviolable #1 — points
  here once the row is updated.
- `k_inflation_seam_obstruction.md` L112 — uses inviolable #1 in
  the `√K`-cancellation argument; the rigorous form lives here.
- `thread_chronology.md` — entry for this articulation.

## One-line summary

`Q mod 2` is preserved by any field deformation whose support
fits in an antiperiodic-loop-free chart (`diam < L_x`); the only
processes that change `Q mod 2` must encircle the antiperiodic
direction, hence are non-local by the substrate's own geometric
scale. Inviolable #1 now has a standalone theorem.
