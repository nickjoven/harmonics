# Vocabulary-bridge iteration 2 step 1 — resolve locus (4) inconsistency

## Status

**Verdict: APPARENT INCONSISTENCY DISSOLVES.** Close reading of
the two source docs shows `mass_sector_closure.md` L46-64 and
`fourth_generation_revisited.md` L165-171 describe the **same
substrate fact in complementary vocabularies**. The "rejection
of chirality" in mass_sector_closure rejects a *naive doubling
formula* (`chiral copies × adj dim = 2 × 3 = 6`), not chirality
involvement; the chirality framing in fourth_generation_revisited
names the *kinematic structure* (L doublet vs R singlet) that
enables the walker round-trip mass_sector_closure formalizes.

Both readings substrate-force: **the lepton sector has a doublet
structure whose round-trip traversal produces the squaring
`k_lepton = q_3² = 9`**. The two docs disagree about emphasis,
not substance.

This is the cleanest resolution of vocabulary_bridge_iteration_1
locus (4) — and a substantive narrowing of the path enumeration
that follows.

Class: foundational rigor check (Class 3, vocabulary-bridge
iteration step resolving an apparent internal inconsistency).

---

## The two readings, side by side

### `mass_sector_closure.md` L46-64

> "A lepton sits in an SU(2) doublet with hypercharge but no
> color. Its walk through the Klein bottle's mode tower is
> bounded by the number of 'gauge mediators' it can interact
> through. Leptons couple through SU(2) weak bosons, and **the
> left-handed and right-handed components each contribute an
> SU(2) adjoint worth of interactions**:
>
> `k_lepton = (chiral copies) × (adj dim) = 2 × 3 = 6 ?`
>
> **No**. The formula is *squared*, not doubled:
>
> `k_lepton = (dim adj SU(2))² = 9`
>
> The squaring comes from the walker needing to traverse the
> adjoint *twice* — **once to reach the doublet partner, once to
> return**. This is the 'walk before repetition' structure: the
> walker covers the adjoint space and comes back, and the total
> path length is the square of the adjoint dimension."

Key points:
- The doublet structure is explicitly invoked (L47: "A lepton
  sits in an SU(2) doublet").
- L50-52 explicitly mentions "left-handed and right-handed
  components each contribute an SU(2) adjoint."
- The "No" rejects the **naive multiplicative formula**
  `2 × 3 = 6`, not the chirality content.
- The squaring's mechanism is "traverse the adjoint *twice* —
  once to reach the doublet partner, once to return."
- The doublet partner is what makes the traversal a *round-trip*
  (two adjoint-dimension traversals composed).

### `fourth_generation_revisited.md` L165-171

> "The lepton sector constant `k_lepton = q₃² = 9` comes from
> the **square** of the SU(2) adjoint dimension — the doubling
> reflects **lepton chirality asymmetry** (`mass_sector_closure.md`).
> Leptons have DIFFERENT SU(2) reps for L and R (doublet vs.
> singlet), so their walk budget is `(dim adj SU(2))² = 9`.
> Quarks, whose color is chirality-blind, use a single copy:
> `k_quark = dim adj SU(3) = 8`."

Key points:
- Explicitly cross-references `mass_sector_closure.md` as the
  source.
- Names the chirality structure as the doublet vs singlet
  asymmetry (which IS the kinematic structure mass_sector_closure
  was invoking).
- Quarks contrast: "chirality-blind" → no analogous round-trip
  → `k_quark = q_2³` (cube, not square).

---

## Why these are the same fact in different vocabularies

The substrate-forced content both docs are pointing at:

1. **The lepton sector has a doublet structure**: there is an
   SU(2) doublet representation whose two components share an
   adjoint coupling structure. Both docs invoke this.

2. **The doublet enables a walker round-trip**: a substrate
   mode in the lepton sector can traverse from one doublet
   component to its partner and return. This produces "two
   adjoint-dimension traversals composed" = squaring.

3. **There also exist singlet components**: complementary to
   the doublet, the lepton sector has SU(2)-singlet
   representations that don't share the doublet coupling.

4. **The doublet/singlet asymmetry IS what mass_sector_closure
   calls "the doublet partner" route**: the round-trip is
   between doublet components (not from doublet to singlet,
   because singlets don't pair).

Both docs are describing the same kinematic geometry. The
difference:

- mass_sector_closure emphasizes the **dynamical reading**:
  the walker traverses the adjoint twice through the doublet
  structure. The chirality content is implicit in "doublet
  partner" but not foregrounded as a chirality claim.

- fourth_generation_revisited emphasizes the **kinematic
  reading**: the doublet vs singlet asymmetry IS lepton chirality
  asymmetry, named explicitly.

The naive doubling formula `2 × 3 = 6` that mass_sector_closure
rejects is a **wrong** dynamics on the same kinematic structure
(it would treat L and R as parallel copies rather than as
doublet-and-singlet with round-trip). Both docs agree this
formula is wrong; they agree the right formula is the squaring;
they describe the geometric reason (the doublet structure
enabling the round-trip) in different words.

---

## The vocabulary divergence, named explicitly

| Aspect | `mass_sector_closure.md` | `fourth_generation_revisited.md` |
|---|---|---|
| Doublet | "lepton sits in SU(2) doublet" (explicit) | "DIFFERENT SU(2) reps for L and R (doublet vs. singlet)" (explicit) |
| Round-trip | "traverse the adjoint *twice* — once to reach the doublet partner, once to return" (explicit) | implicit in "(dim adj SU(2))²" |
| Chirality language | implicit (doublet partner = L-doublet's other component) | explicit ("lepton chirality asymmetry") |
| Naive formula rejection | explicit ("No. The formula is *squared*, not doubled") | not addressed |
| Quark contrast | none | explicit ("chirality-blind, use a single copy") |

The two docs cover **complementary aspects** of the same
substrate fact. Neither is wrong; each emphasizes a different
view. Reading them as "competing forcings" was my iteration 1
misreading; the cross-reference (`fourth_generation_revisited.md`
L168 explicitly cites `mass_sector_closure.md`) actually makes
them a paired exposition.

---

## What survives as substrate-forced

The substrate apparatus forces:

- **The lepton sector has both doublet and singlet SU(2)
  representations.** This is the kinematic precondition for the
  round-trip mechanism.
- **The walker round-trip produces `k_lepton = (dim adj SU(2))²
  = q_3²`.** This is the dynamical consequence.
- **Quarks lack this round-trip** because color is chirality-
  blind (no doublet/singlet split at the SU(3) level for color
  rep). Hence `k_quark = q_2³ = 8` (cube, not square).

This forcing is at the **kinematic structure** level (doublet vs
singlet). It is substrate-forced, not substrate-admitted.

---

## What does NOT follow

The substrate does **not** force:

- **The L vs R labeling.** The doublet is called "L-doublet" and
  the singlet "R-singlet" by SM convention; the framework's
  doublet/singlet split does not by itself select which is "L"
  and which is "R."
- **Parity violation in weak interactions.** The phenomenology
  that left-handed components couple to W bosons and right-handed
  do not is a downstream consequence of the SM's labeling, not
  directly derived from the framework's doublet-vs-singlet
  kinematic split.
- **Specific Yukawa coupling asymmetry** between L and R.

These remain operationally open or framework-downstream.

---

## Implications for vocabulary-bridge iteration 2

The path enumeration from iteration 1 was:
- α: y-parity (cos/sin) ↔ chirality
- β: Loop orientation ↔ chirality (figure-8 reading)
- γ: q₂ locked/unlocked ↔ chirality
- δ: NO substrate-level chirality

Iteration 1 added the figure-8 audit (β demoted to Class 2 →
eliminated from forcing-candidate paths). This step adds:

**Refined path δ' — substrate-forced doublet/singlet kinematic
structure for leptons, with L/R labeling as observation.**

The substrate forces a chirality-adjacent structure (the
doublet/singlet split that enables the round-trip → `q_3²`),
but does **not** force the SM's specific L/R identification.
Path δ from iteration 1 (no substrate-level chirality at all)
is **strengthened**: the substrate has more than iteration 1
credited (the kinematic doublet/singlet split), but still less
than full SM chirality (the L/R labeling).

The SU(2)_L identification commitment in
`gauge_high_scale_identification.md` L106-113 narrows:

- **Substrate-forced**: the SU(2) gauge sector acts on the lepton
  doublet (one of the kinematic structures forced by `k_lepton
  = q_3²` squaring).
- **Identification commitment** (what remains): whether the SM's
  "SU(2)_L" labels the doublet (with the singlets as "R") or
  vice versa.

The labeling commitment is much narrower than iteration 1
framed: it's not "is chirality substrate?" but "which of the
substrate's two reps is L vs R?" That's a binary choice that
observation has already fixed via parity violation experiments.

---

## Implications for paths α and γ

The substrate-forced doublet/singlet structure is **specific to
the lepton sector**. It is not the same axis as:

- **Path α (y-parity)**: y-parity is a Klein-bottle-wide
  classification (cos vs sin y-modes), not specific to lepton.
  If y-parity ↔ chirality, the identification would have to act
  on quarks as well — but quarks are chirality-blind in the
  framework's apparatus. Path α therefore **does not align with
  the substrate-forced lepton chirality** and remains operationally
  open as a *separate* possibility.

- **Path γ (q₂ locked/unlocked)**: q₂ axis is the
  generation-distinguishing axis (A, B locked; C, D unlocked).
  It is not lepton-specific (applies to quarks too). Path γ
  remains the **generation discriminator**, not the chirality
  discriminator. Conflating them was iteration 1's framing
  error.

Path **ε** (lepton at saddle-node tangent, conversational from
earlier) aligns with this resolution: the doublet's round-trip
*is* the local `x²` saddle-node geometry; the saddle-node
tangent reading and the doublet-round-trip reading converge
at the same substrate object.

---

## What this iteration step establishes

1. **Locus (4) inconsistency dissolves.** Both docs describe the
   same substrate fact (lepton doublet enabling walker round-trip
   to produce `k_lepton = q_3²`) in complementary vocabularies.

2. **Path δ' — substrate-forced doublet/singlet, observation-fixed
   L/R labeling — is the cleanest reading.** Substrate forces
   *more* than iteration 1 credited; SM chirality phenomenology
   sits at a sharply-narrowed identification commitment.

3. **The SU(2)_L identification commitment narrows** from
   "is there substrate chirality at all?" to "which of the
   substrate's two reps is L?"

4. **Paths α and γ do not align with the lepton-specific
   doublet structure.** They remain operationally open as
   separate possibilities, not as the chirality candidates
   iteration 1 framed them as.

5. **Path ε (saddle-node tangent) converges with path δ'.**
   The lepton's round-trip squaring is the local `x²` geometry;
   both readings point at the same substrate object.

---

## What this iteration step does NOT establish

- **Why the doublet is on L rather than R.** The substrate forces
  the doublet/singlet split; the L vs R labeling remains
  observation. Whether the substrate has any further constraint
  that would fix the labeling is open (probably no, given the
  figure-8 audit demoted the chirality-as-loop-orientation
  reading).
- **Parity violation derivation from substrate.** The framework
  has the doublet structure; parity violation in weak interactions
  follows from how SU(2)_L acts on the doublet (which is the
  identification commitment). The framework does not derive the
  parity violation directly.
- **Closure of the vocabulary-bridge arc.** The arc continues:
  the labeling commitment remains, and whether further substrate
  apparatus narrows it (or whether it stays operationally open as
  observation-fixed) is iteration 3's question.

---

## Falsifiers for this step's verdict

1. **Mis-read coupling between docs.** If `mass_sector_closure.md`
   L60-64's "walker round-trip" is not actually the same fact as
   `fourth_generation_revisited.md` L165-171's "chirality
   asymmetry" — e.g., if the walker traverses *between* L and R
   chirality components (a chirality round-trip) rather than
   within the L-doublet (a doublet round-trip) — the resolution
   fails. Verification would require a closer look at what
   "doublet partner" means in `generation_mechanism.md`'s D34
   chain apparatus.

2. **Doublet structure not substrate-forced.** If the framework's
   apparatus does not actually substrate-force the lepton-doublet
   structure (only describes it as a phenomenological starting
   point), the path-δ' refinement weakens to "substrate is
   consistent with doublet but doesn't force it" — i.e., the
   labeling-commitment narrowing doesn't happen and the SU(2)_L
   gap remains as wide as iteration 1 framed.

3. **The L/R labeling has a substrate constraint we missed.**
   If there's apparatus in `gauge_sector_lovelock.md` or
   elsewhere that fixes which rep is L vs R (e.g., a hypercharge
   sign convention forced by topology), the labeling commitment
   isn't observation-fixed and the closure differs.

---

## Plan for iteration 2 step 2

Original step 2 plan: "test whether SU(2) gauge derivation
structurally singles out one of α/β/γ." This step's resolution
changes the target: paths α, β, γ are not the chirality
candidates. The new step 2 target:

**Determine whether the substrate's lepton-doublet structure
(from k_lepton = q_3² squaring) has any further substrate
constraint that fixes the L vs R labeling, or whether the
labeling is genuinely observation-only.**

This is a tighter question than iteration 1's. Three sub-checks:

(a) Read `gauge_sector_lovelock.md` for any structural step that
distinguishes the two SU(2) reps by something other than convention.
(b) Read `q_mod2_conservation_theorem.md` for whether the Q mod 2
invariant has a sign convention that fixes L vs R.
(c) Read `gell_mann_nishijima.md` (the framework's Q = T_3 + Y/2
derivation) for whether hypercharge is substrate-signed.

If all three return "no substrate constraint on L vs R," path δ'
is the closure: substrate-forced doublet/singlet, observation-fixed
labeling. If any returns "substrate constraint exists," the
constraint becomes the substantive content of the bridge.

---

## Cross-links

- `vocabulary_bridge_iteration_1.md` — locus (4) inconsistency
  named there; resolved here.
- `mass_sector_closure.md` L46-64 — walker round-trip reading.
- `fourth_generation_revisited.md` L165-171 — chirality
  asymmetry reading.
- `figure_eight_necessitation_audit.md` — figure-8 reading
  demoted to Class 2; path β eliminated.
- `klein_z2_decomposition_falsifier_2.md` — modal y-parity
  finding; path α status unchanged (operationally open as a
  separate possibility).
- `horn_branch_iteration_2_step_1.md` — q₂ locked/unlocked as
  generation axis; path γ status clarified as generation
  discriminator, not chirality.
- `gauge_high_scale_identification.md` L106-113 — SU(2)_L
  identification commitment; narrows under this resolution.
- `gauge_sector_lovelock.md` — iteration 2 step 2 (a)
  target.
- `q_mod2_conservation_theorem.md` — iteration 2 step 2 (b)
  target.
- `gell_mann_nishijima.md` — iteration 2 step 2 (c) target.
- `basepoint_principle.md` — operationally-open vs
  structurally-declined; path δ' status determination.
- `canonical_glossary.md` — possibility-discipline distinctions
  (substrate-forced doublet vs substrate-admitted labeling).

---

## One-line summary

Iteration 2 step 1 resolves the iteration-1 locus (4) "internal
inconsistency" by close reading of `mass_sector_closure.md`
L46-64 and `fourth_generation_revisited.md` L165-171 — the two
docs describe the same substrate fact (the lepton SU(2) doublet
enabling a walker round-trip that produces `k_lepton = q_3²`) in
complementary vocabularies, with mass_sector_closure rejecting a
NAIVE doubling formula (`2 × 3 = 6`) while implicitly invoking
chirality through "doublet partner," and fourth_generation_revisited
naming the chirality content explicitly; both substrate-force the
doublet/singlet kinematic split for leptons (chirality-adjacent
structure), but neither forces the SM's specific L/R labeling,
which remains an identification commitment narrowed from "is
chirality substrate?" (iteration 1 framing) to "which rep is L?"
(observation-fixed); paths α (y-parity) and γ (q₂-locked) remain
operationally open as *separate* possibilities (they are not
lepton-specific and do not align with the doublet-structure
forcing), path β remains eliminated by the figure-8 audit, and
path ε (lepton at saddle-node tangent) converges with the
refined path δ' (substrate-forced doublet, observation-fixed
labeling) — iteration 2 step 2 narrows to checking whether
`gauge_sector_lovelock.md`, `q_mod2_conservation_theorem.md`, or
`gell_mann_nishijima.md` provide any further substrate
constraint on the L vs R labeling, with three "no" answers
closing the arc at path δ' and any "yes" answer becoming the
bridge's substantive content.
