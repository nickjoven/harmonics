# Pattern-identification discipline (candidate methodology)

## Status

**Candidate methodology**, not yet sealed. Proposes a working
discipline that the framework's most successful closures have
been using implicitly — substituting **structural-identity
recognition** for **precision computation** wherever the identity
is named and forces the result. The framework's expensive
computations (boundary weight `w*`, K_STAR fixed-point, specific
mass values) are exactly the places where structural
identification has not been found, suggesting that **expensive
computation is the symptom of an unsolved structural-identity
problem**, not the price of substrate-level precision.

This doc applies the discipline to **both layers**:

1. **Substrate-side discipline** — when introducing or verifying
   a framework claim, first check whether a named structural
   identity (number-theoretic theorem, group-theoretic
   classification, modular-forms structure, algebraic primitive)
   forces the result. If yes, cite. If no, compute.

2. **Front-end discipline** — the visual layer should surface
   the framework's named structural identities as first-class
   entities, make computational-cost tiers visually distinct,
   and enable navigation by structural-identity citation. The
   dag viewer's current edge structure already supports this;
   the implementation steps are concrete and incremental.

The discipline is **substrate-admitted, not substrate-forced**
per `canonical_glossary.md` Section 8's possibility-discipline.
It refines the framework's *workflow* without changing its
apparatus. Sealing as a standing methodology would require
demonstrating consistent application across multiple iteration
arcs, parallel to `feedback_resolution_vs_reconstruction.md`'s
status.

Class: methodology candidate (Class 3, codifies an existing
implicit discipline).

---

## The principle

> **Pattern-identification before precision computation.** When
> a framework operation requires producing a value, verifying
> a uniqueness claim, or characterizing a structural object,
> first check whether a named structural identity forces the
> result. If yes, citation replaces derivation. If no, fall
> back to precision computation — and recognize that the
> expense is the symptom of an open structural problem, not
> an inherent cost of substrate work.

Equivalent framings:

- **Cite the theorem, then move on.** Mihailescu, CRT, Cartan,
  Frobenius — each is a one-line citation that replaces a
  multi-step derivation. The framework's apparatus is rich
  enough that almost every substrate-forced result has a
  structural identity behind it.

- **Expensive computation flags an open problem.** If you find
  yourself doing numerical fixed-point iteration to extract a
  substrate-claimed value, you're at the boundary where the
  framework's structural-identity coverage runs out. That's
  data — work to push the boundary.

- **Recognition > derivation > computation** as a workflow
  preference. Recognize first (free); derive if needed
  (moderate); compute only as last resort (expensive).

---

## Tiered cost map of the framework's existing operations

The framework's operations sort into clear computational tiers:

### Tier 0 (free): cite the named theorem

| Operation | Structural identity | Replaces |
|---|---|---|
| `(q_2, q_3) = (2, 3)` uniqueness | Mihailescu's theorem (2002) | Polynomial-uniqueness derivation in `mass_sector_closure.md` |
| `Z_6 = Z_2 × Z_3` | Chinese Remainder Theorem | Direct enumeration of group structure |
| `SU(n)` is unique minimum-rank for `Z_n` center | Cartan classification (1894) | Verification across all simple compact Lie groups |
| ℝ/ℂ/ℍ are the only normed division algebras | Frobenius's theorem (1878) | Direct construction of alternatives |
| Born exponent 2 | Saddle-node universality (Thom 1972) | Direct dynamical-systems verification |
| Klein-bottle H₁ = Z ⊕ Z₂ | Standard topology | Direct homology computation |

### Tier 1 (cheap): number-theoretic / combinatorial identities

| Operation | Identity | Replaces |
|---|---|---|
| `φ(6) = 2` boundary count | Euler totient `φ(pq) = (p−1)(q−1)` for distinct primes | Enumeration `{k : gcd(k, 6) = 1}` |
| Coprime classification on `Z_6` | Standard congruence arithmetic | Case-by-case gcd checks |
| Klein-antipodal pairs `{k, 6−k}` | Z_2 action on Z_6 | Direct verification of antipodal structure |
| Catalan equation status | Mihailescu (general); Lebesgue-era for `(2,3)` case | Searching the integer lattice |
| `8 = q_2³`, `9 = q_3²` | Mihailescu's solution | Verifying `2³ < 3² < 2³ + 1` |

### Tier 2 (moderate): structural recognition replaces enumeration

| Operation | Recognition | Replaces |
|---|---|---|
| Cusp 1/2 ↔ q_2-rep at X_0(6) | Modular forms theory + Hecke action | Direct cusp computation |
| 4 XOR-survivors at `(q_x, q_y) ∈ {(2,3), (3,2)}` | Klein-bottle XOR rule + field-equation dynamics (the rule reduces 3,969 pairs to 1,764; dynamics collapses to 4 — corrected 2026-08-10) | Searching 3,969 candidate mode pairs |
| Pauli stabilizer / SNMC class membership | D2 SNMC formalization | Direct multi-mode state characterization |
| Toroidal/poloidal direction identification with SU(3)/SU(2) | Gauge-sector chain (Cartan + 4 criteria) | Per-context re-derivation |
| Mass-sector vocabulary closure (3×3 matrix) | Substrate vocabulary enumeration | Per-claim substrate verification |

### Tier 3 (expensive): structural identification not found — open problem flag

| Operation | Status | Open problem |
|---|---|---|
| `K_STAR ≈ 0.86196` | Numerical from joint matter-sector self-consistency | No structural identity forces this value |
| Boundary weight `w* ≈ 0.83` | Observation-inverted from Ω_obs | Audit (`boundary_weight.py` L13-56) — no substrate-internal forcing |
| Specific mass values (m_μ ≈ 206.77, etc.) | Substrate forces possibility-space; observation selects | Horn-branch arc productive null (PR #211) |
| Effective Farey depth 5.83 / effective mode count 12.66 | Numerical from boundary-weight machinery | Layer-specific address per primitives-vs-addresses candidate |
| PMNS θ_13 8.6° | Framework predicts 28.13°; gap 3.3× | Open structural-identity gap |

**The diagnostic value of the tier table**: every framework
closure that has *worked* falls into Tier 0-2. Every framework
operation that has *failed to close* falls into Tier 3. The
pattern is exact: structural-identity recognition is the
framework's productive mode; expensive computation marks the
boundary of current substrate-derivation reach.

---

## Where this discipline has worked historically

The most powerful framework closures have been *recognitions*,
not computations:

- **Ω_b two-component closure** (PR #178 area): recognized as
  Γ_0(6) cusp 1/2 identification → w_+ = 13/14 forced
- **Cube identity uniqueness** (PR #214): recognized as
  Catalan/Mihailescu → `(q_2, q_3) = (2, 3)` forced
- **Gauge group** (D41-42): recognized as Cartan minimum-rank
  given Z_2 × Z_3 center → SU(3) × SU(2)
- **Z_6 mode lattice** (canonical): recognized as CRT
  decomposition of Z_6 = Z_2 × Z_3
- **Born exponent 2** (`born_rule.md` L151-156): recognized as
  saddle-node universality (Thom)
- **Complex amplitude ℂ-uniqueness** (`complex_amplitude_uniqueness.md`):
  recognized as Frobenius-Schur trichotomy plus one antiperiodic
  cycle
- **Klein-bottle vs T² vs RP²** (`klein_bottle_derivation.md`):
  recognized as H₁ structure (free + torsion) classification

In each case, the framework's contribution wasn't to derive the
specific value from first principles — it was to **identify
which named structural fact forces the result**.

---

## Where this discipline has NOT worked — and why that's data

The framework's open problems are precisely the places where
structural-identity recognition has not been found:

- **m_μ 37% bare-tree gap**: horn-branch productive null. The
  framework's substrate has the apparatus to predict
  `7^(5/2) = 129.6`; the gap to observed 206.77 has no
  identified structural identity. (Iteration arcs surfaced
  cluster candidates at f_locked ≈ 0.83 but no forcing
  mechanism — Tier 3.)
- **PMNS θ_13**: 3.3× gap, structural failure of bare
  Fritzsch-form. Same status — no identity forces the gap.
- **K_STAR ≈ 0.86196**: numerical, no structural identity. The
  primitives-vs-addresses candidate suggests it's a
  layer-specific address rather than a layer-invariant
  primitive.
- **Boundary weight w***: observation-inverted per the audit.
  No structural identity gives the specific value.

**These are not failures of the framework** — they're locations
where the discipline has correctly identified that the answer
isn't structurally forced. Per the possibility-discipline,
they're substrate-admitted with observation supplying the
selection. The expensive-computation symptom is the
methodology working correctly: it flags where structural
content has been exhausted.

---

## Front-end discipline

The visual layer should surface what the substrate-side
discipline organizes — making structural-identity recognition
visually obvious so that future framework readers absorb the
discipline by inspection rather than having to derive it
themselves from the corpus.

### Current state vs the discipline

The framework's existing front-end:

- **`docs/dag.html`** — interactive derivation graph. Edges
  carry types (`grounds`/`derives`/`proposes` per `## Lineage`
  blocks, untyped `references` otherwise). Nodes are derivation
  docs.
- **`docs/claim-chain.html`** — scorecard view, MANIFEST.yml
  rows with sigma deltas.
- **`docs/glossary.html`** — canonical-glossary entries.
- **`docs/derivations.html`** — full derivation text view.

What the front-end currently doesn't surface:

- **Named structural identities as first-class entities.**
  Mihailescu, CRT, Cartan, Frobenius, saddle-node universality
  — these are *cited* throughout the corpus but not surfaced as
  the framework's main load-bearing infrastructure.
- **Computational cost tiers.** A reader can't quickly
  distinguish a Tier 0 cited-theorem closure from a Tier 3
  numerical-only fixed-point.
- **Navigation by structural identity.** No way to ask "which
  docs cite Mihailescu?" without grep.
- **Open-problem flags.** Tier 3 operations look the same as
  Tier 0-2 in the current viewers.

### Concrete front-end proposals

In order of effort/impact:

**(a) `docs/identities.html` — Structural identities catalog**

New HTML viewer paralleling `glossary.html`. One entry per named
structural identity used in the framework:

```
Mihailescu's theorem (2002)
  Statement: x^p − y^q = 1 with p, q ≥ 2 has unique
             positive-integer solution (x, p, y, q) = (3, 2, 2, 3)
  Forces:    (q_2, q_3) = (2, 3) [via cube identity]
  Cited in:  mass_sector_closure.md
             canonical_glossary.md
             framework_status.md
  Tier:      0 (free citation)
```

Data source: hand-curated JSON file (initially ~10-15 entries),
extended as the discipline lands more closures. Renders like
`glossary.html` — a structured-entries list with cross-links to
derivation docs.

This is the single highest-impact addition. Makes the framework's
load-bearing structural foundations visible at a glance.

**(b) Cost-tier badges in existing viewers**

Add a `tier` field to derivation-graph nodes (computed from the
docs' content — e.g., parse for "cite", "by [theorem]", "we
compute", "numerical from", etc., or hand-tag in a
`## Lineage` block extension).

Render as a small badge in `dag.html` and `claim-chain.html`:
- 🟢 Tier 0 — cites named theorem
- 🟡 Tier 1 — number-theoretic / combinatorial
- 🟠 Tier 2 — structural recognition
- 🔴 Tier 3 — expensive computation / open problem

Makes the discipline visible without requiring docs to be
re-tagged en masse. Tier 3 nodes are immediately the framework's
visible open-problem queue.

**(c) Filter views on `dag.html`**

Add filters:
- "Show only docs citing Mihailescu" (or any structural identity)
- "Show only Tier 0/1 closures" (the productive backbone)
- "Show only Tier 3 nodes" (the open-problem queue)

Implementation: extends `dag.html`'s existing search box with
structured filters. Data source: the structural-identities JSON
+ tier badges.

**(d) Methodology page (substrate + front-end discipline reference)**

A `docs/methodology.html` page documenting the discipline
itself — what's free, what's expensive, when to cite, when to
compute. Companion to the methodology notes in the corpus
(`feedback_resolution_vs_reconstruction.md`,
`feedback_null_promotion.md`, this doc).

### What surfaces the discipline gives the front end

The pattern-identification discipline turns the front-end into
an active methodology tool rather than just a viewer:

- **Pattern-discoverability**: readers find Mihailescu, CRT,
  Cartan as named load-bearing identities without needing to
  read the full corpus
- **Open-problem visibility**: Tier 3 nodes are the framework's
  *visible* open-problem queue, not buried in dense prose
- **Workflow guidance**: a reader unfamiliar with the discipline
  picks it up by inspection — they see the tier badges and the
  identities catalog and understand the framework's "cite first,
  compute last" workflow without being told
- **Cross-arc cumulativity**: each new closure that lands in
  Tier 0-2 (via newly-identified structural identity) becomes
  immediately visible as the framework's structural-identity
  catalog grows

---

## Concrete proposal for sealing

The discipline's value is workflow-shaping, not substrate-claiming.
Sealing this as a standing methodology would require:

(a) **Demonstrate consistent application** across at least one
additional iteration arc — when introducing a new substrate
claim, the structural-identity check is performed and recorded.

(b) **Build the `docs/identities.html` viewer** with the initial
~10-15 entries. This is the single highest-impact front-end
move. ~200-300 lines of HTML + JSON.

(c) **Tier the existing claim-chain entries.** Either via
content-parsing of derivation docs or via hand-tagging in a
`## Tier` block. Surfaces the cost map visually.

(d) **Methodology memory entry** parallel to
`feedback_resolution_vs_reconstruction.md` and
`feedback_null_promotion.md` — capturing the discipline as
standing user preference for future sessions.

These can be staged: (a) and (d) are cheap (cite-and-record);
(b) is moderate (HTML+JSON); (c) is moderate-to-large depending
on how much existing-content tagging is wanted.

---

## What this doc does NOT establish

- **No new substrate apparatus.** Pure resolution-mode.
- **No new conservation laws or structural derivations.** The
  discipline is *about how to use* existing apparatus.
- **No specific numerical predictions.** Tier 3 operations
  remain expensive; the discipline just flags them as the
  open-problem queue rather than treating them as substrate
  precision exercises.
- **No automatic seal of the discipline.** Candidate status
  pending demonstrated consistent application + front-end
  implementation.

---

## Falsifiers

1. **Structural identity coverage runs out unexpectedly.** If a
   future framework closure that's clearly substrate-forced
   produces a value with no identifiable structural identity,
   the tier table's correlation ("expensive computation = open
   problem") weakens.

2. **Open problems close without new structural identities.**
   If the m_μ 37% gap or K_STAR value closes via something other
   than identifying a new structural identity (e.g., from an
   explicit field-equation simulation), the discipline's
   "recognition > computation" priority would need refinement.

3. **Front-end tier-tagging produces noise.** If the
   computational-tier badges don't cluster cleanly — Tier 3 docs
   turn out to mix open-problem flags with valid expensive
   computations — the discipline's diagnostic value degrades.

4. **Discipline citation becomes ceremony.** If "by Mihailescu"
   becomes a reflexive citation without the substantive
   recognition behind it, the discipline degrades to
   pattern-matching rather than structural understanding.

---

## Cross-links

- `feedback_resolution_vs_reconstruction.md` (memory) —
  structural parallel; methodology candidate
- `feedback_null_promotion.md` (memory) — methodology parallel
- `canonical_glossary.md` Section 8 — possibility-discipline
  vocabulary; this discipline refines workflow within that
  framework
- `mass_sector_closure.md` "Connection to the Catalan equation
  / Mihailescu's theorem" — model case of cite-replaces-derive
- `boundary_weight.py` L13-56 — audit revealing that w* is
  observation-inverted; canonical Tier-3 honest acknowledgment
- `primitives_vs_addresses_candidate.md` — first methodology
  candidate; tier-3 operations are typically layer-specific
  addresses
- `surface_uniqueness_audit.md` — substrate-admitted vs
  observation-fixed; Tier 3 ≈ observation-fixed selections
- `conservation_scale_stratification_audit.md` — algebraic
  invariants are Tier 0-1 universal; topological invariants are
  scale-contingent (the tiers help organize the audit's
  findings)
- `bicyclist_observer_sequence.md` — presentation-layer pattern
  this discipline extends to the front-end
- `gauge_sector_lovelock.md` — Cartan classification +
  4-criteria chain as Tier 0/1 closure
- `docs/dag.html` — current connections viewer; would gain
  tier badges and identity-cited filters under proposal (b)/(c)
- `docs/glossary.html` — current entries viewer; structural
  parallel for the proposed `docs/identities.html`
- `Makefile` `make preview` target — local-server access for
  the visual layer; would expose the new viewers immediately
  upon implementation

---

## One-line summary

This doc proposes a candidate **pattern-identification before
precision computation** discipline that codifies the framework's
most successful closure pattern (cite Mihailescu, CRT, Cartan,
Frobenius, Euler totient, saddle-node universality, modular cusps
— named structural identities that force results in one
citation rather than precision computation), applies the
discipline to both **substrate-side** (recognize first, derive
if needed, compute as last resort; expensive computation flags
an open structural-identity problem rather than substrate
precision cost) and **front-end** (concrete proposals: a
`docs/identities.html` structural identities catalog paralleling
`glossary.html`, computational-cost-tier badges in `dag.html` and
`claim-chain.html`, filter views enabling navigation by
structural-identity citation, and a methodology reference page
documenting the discipline), tiers existing framework operations
into four cost levels (Tier 0 = cited theorem, Tier 1 = number-
theoretic identity, Tier 2 = structural recognition, Tier 3 =
expensive computation = open problem flag), demonstrates the
discipline has been implicitly working in every successful
framework closure (Ω_b cusp identification, cube identity
Catalan/Mihailescu, gauge group Cartan, Z_6 CRT, Born exponent
saddle-node, ℂ-uniqueness Frobenius-Schur, K²/T² H₁
classification) while every framework open problem (m_μ 37%,
PMNS θ_13, K_STAR, w*) is precisely a Tier 3 location where
structural identity has not been found — making the discipline's
"recognition > derivation > computation" workflow into a
diagnostic tool that flags the framework's actual open problems
visibly rather than burying them in numerical prose; four
falsifiers named; sealing requires (a) consistent demonstrated
application, (b) implementation of `docs/identities.html`, (c)
tier-tagging of existing claim-chain entries, and (d) a
methodology memory entry parallel to the existing
`feedback_resolution_vs_reconstruction.md` and
`feedback_null_promotion.md` preferences; resolution-mode
throughout (no apparatus modification); the discipline turns the
front-end from passive viewer into active methodology
infrastructure — making pattern-identification visually obvious
so future readers absorb the framework's "cite first, compute
last" workflow by inspection rather than by reading the
complete corpus.
