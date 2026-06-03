# Vocabulary-bridge iteration 1 — substrate → particle chirality survey

## Status

**First-pass survey.** This is iteration 1 of the
vocabulary-bridge arc per Task 110. Apparatus context:

- Substrate y-parity is modally populated but **not** the
  generation-distinguishing axis
  (`klein_z2_decomposition_falsifier_2.md`,
  `horn_branch_iteration_2_step_1.md`).
- The apparatus-extension fallback (Klein-bottle restructure) is
  structurally declined by empirical floor
  (`klein_bottle_restructure_price.md`: would predict
  empirically-falsified ℍ-QM).
- This vocabulary-bridge is therefore the **sole route** to a
  substrate-chirality story at all.

Reading the apparatus surfaces a sharper finding than expected:
**the framework already has multiple "chirality-like" structures
in place, with internal inconsistencies between them, and the
SU(2)_L identification is an explicit identification commitment
rather than a substrate derivation.** Iteration 1's job is to
survey these structures, name the inconsistencies, identify the
load-bearing gap, and articulate paths forward.

No closure is attempted. The arc may be substantial (comparable
to Koide's 14-iteration scope) or it may close earlier if the
existing apparatus admits a forced unification under careful
reading.

Class: substrate-derivation survey for the load-bearing
chirality identification gap (Class 3, iteration-arc opener).

---

## The load-bearing gap

`gauge_high_scale_identification.md` L106-113 (canonical statement):

> "These commitments are *partially* constrained: the structural
> arguments below rule out specific alternative labelings as
> inconsistent. They are not fully forced, in that no theorem
> selects 'weak isospin SU(2)_L specifically' rather than another
> SU(2) gauge sector with the same algebraic structure. The
> residual freedom is one *identification* commitment in the
> sense of `gauge_dictionary.md`."

The framework's SU(2) gauge sector emerges from the substrate's
Z₂ center (`gauge_sector_lovelock.md`). What is **not** derived
is **why this SU(2) is the LEFT-chiral one** (acting only on
left-handed components in the SM sense). Parity violation in
weak interactions — left-handed neutrinos couple to W bosons,
right-handed neutrinos do not — is currently an identification
commitment, not a substrate-forced consequence.

The vocabulary-bridge's substantive task is to close this
identification commitment: show that one of the framework's
existing chirality-adjacent axes maps onto observed L/R
asymmetry, OR determine that the framework's substrate operates
on a different axis and L/R chirality is framework-downstream/
empirical, not substrate-primitive.

---

## Survey of the framework's existing chirality-adjacent apparatus

The framework currently uses "chirality" or related language in
at least **five** distinct loci. These are not unified:

### (1) y-parity (cos vs sin)

Source: `klein_z2_decomposition_falsifier_2.md` (third-caveat
test); `klein_bottle.md` L107-152 (mode decomposition under
XOR rule).

- y-modes split into R-eigenstates under the y-reflection
  `y → L_y − y`:
  - cos(2πny/L_y) is R-even (p_y = 0)
  - sin(2πny/L_y) is R-odd (p_y = 1)
- Modally populated: both sectors carry mode content, paired
  complementarily with antiperiodic-x (for cos-y) and periodic-x
  (for sin-y) wavenumber ladders by the XOR rule
  `p_x + p_y ≡ 1 (mod 2)`.

Framework status: **modal sufficiency confirmed** by the
third-caveat test. The y-parity axis is orthogonal to the
generation classification.

### (2) Loop orientation (figure-8 P operation)

Source: `figure_eight.md` L283-285.

> "**P (parity)** = mode swap within each loop. Exchange the
> locked and unlocked states within a sector. This swaps left
> and right chirality (the two orientations of the loop)."

This identifies L/R chirality with "the two orientations of the
loop" — i.e., the direction of traversal around each S¹ loop
of the figure-8. Combined with `figure_eight.md` L41-58, each
loop is the (q_x, q_y)-family S¹ parameterized by phase, and
"the two orientations" presumably refers to the two ways to
traverse this S¹.

Framework status: **explicit chirality identification**, but
note that this is mode-level (within-loop) and not generation-
level.

### (3) Locked/unlocked at q₂ (horn-branch step 1 axis)

Source: `horn_branch_iteration_2_step_1.md` (q₂-axis sector
assignment); `figure_eight.md` L47-53 (Loop 1 vs Loop 2 in the
{A, B, C, D} apparatus).

- A and B are q₂-locked (= q_x = 2 locked); they are on Loop 1
  (sector (2, 3)).
- C and D are q₂-unlocked (= q_x = 3 unlocked, in the (3, 2)
  family naming); they are on Loop 2.
- This is the distinguishing axis for the horn-branch flare:
  flare suppresses q₂-locked modes (A, B) relative to
  q₂-unlocked (C).

Framework status: **horn-branch step 1 finding**, preserved
through iteration 3. It is the generation-discrimination axis
in the framework's mass apparatus. **NOT** explicitly chirality,
but co-located with reading (2)'s identification.

### (4) Chirality-doubling in `k_lepton = q_3²`

Source: `mass_sector_closure.md` L46-65 vs
`fourth_generation_revisited.md` L63 — **inconsistent
explanations.**

`mass_sector_closure.md` L54-64:
> `k_lepton = (chiral copies) × (adj dim) = 2 × 3 = 6 ?`
> "No. The formula is *squared*, not doubled... The squaring
> comes from the walker needing to traverse the adjoint *twice*
> — once to reach the doublet partner, once to return."

`fourth_generation_revisited.md` L63:
> "`k_lepton = 9 = (dim adj SU(2))²` is fixed by the
> **chirality-squared gauge structure**."

These give different readings:
- mass_sector_closure: squaring is walker round-trip (NOT
  chirality)
- fourth_generation_revisited: squaring is chirality-squared
  (IS chirality)

Framework status: **internal inconsistency**. Either the
"chirality-squared" reading in fourth_generation is loose
language describing the walker round-trip, or
mass_sector_closure's rejection of "chiral copies × adj dim"
is loose language describing the same thing differently. This
should be resolved in iteration 2 step 1.

### (5) SU(2)_L identification commitment

Source: `gauge_high_scale_identification.md` L88-113.

The framework's substrate derives an SU(2) gauge group from
the Z₂ center of the antiperiodic x-direction. The SM has
SU(2)_L (weak isospin, left-chiral). The framework **commits**
SU(2) ↔ SU(2)_L without forcing this identification structurally.

Framework status: **acknowledged identification commitment**.
The framework's own canonical doc names this as "not fully
forced" and lists it as residual freedom in the gauge dictionary.

---

## What a successful vocabulary-bridge would do

The substantive question is: can one of (1)-(5) be promoted from
identification commitment / orthogonal axis / inconsistent
reading into a **substrate-forced derivation of SM L/R
asymmetry**?

A successful bridge would:

1. **Pick one chirality-axis as the framework-native one.** Either
   y-parity, loop-orientation, locked-unlocked, or something else
   yet to be named — but not all five simultaneously.

2. **Show that this axis maps onto the SM L/R distinction.** This
   means: under the chosen mapping, left-handed components couple
   to W bosons and right-handed do not (the V-A structure of
   weak currents).

3. **Reproduce parity violation in weak interactions.** The
   crucial test: does the framework's chosen axis, when applied
   to the figure-8 SU(2) sector, naturally produce the SM's
   left-only weak coupling?

4. **Resolve the k_lepton = q_3² internal inconsistency** —
   either by showing the walker round-trip and chirality-squared
   readings are the same in substrate terms, or by demoting one
   to "informal description" status.

A successful bridge would NOT:

- Add new substrate apparatus (the apparatus-extension fallback
  is structurally declined).
- Modify the existing gauge derivation or mass sector closures.
- Predict observables the SM doesn't already have, unless the
  prediction is testable.

---

## First-pass hypothesis paths

Iteration 2 may try one of these paths. None is currently
forced; the survey only names which are conceptually consistent
with the existing apparatus.

### Path α: y-parity ↔ chirality

Identify substrate y-parity (cos vs sin) directly with L/R.

Pro: y-parity is the cleanest mathematical decomposition (genuine
R-eigenvalue split, both populated).
Con: y-parity is orthogonal to the generation classification, so
this mapping would imply each generation has both L and R
components — which IS the SM picture, but the framework hasn't
demonstrated that the cos-y modes specifically couple to the
weak SU(2) generators differently from the sin-y modes.

Testable consequence: the framework's SU(2) gauge derivation
(`gauge_sector_lovelock.md`) should single out one of {cos-y, sin-y}
as the weak-coupling carrier. If it doesn't, path α fails.

### Path β: Loop orientation ↔ chirality (figure-8 reading)

Take `figure_eight.md` L283-285 at face value: chirality is the
direction of traversal around the S¹ loops.

Pro: This is the framework's own statement; iteration 1's job
would just be to verify it produces SM L/R asymmetry.
Con: "Orientation of the loop" is mode-level (within a single
S¹), not particle-level. The SM L/R distinction is per-particle.
Need to derive how mode-orientation maps to particle-handedness.

Testable consequence: the W± boson asymmetry. W+ goes Loop 1 →
Loop 2, W− goes the other way (`figure_eight.md` L140-146). If
"left-handed coupling" corresponds to one direction of loop
traversal and not the other, the framework's existing apparatus
already produces parity violation — just not in vocabulary
unified with the SM.

### Path γ: Locked/unlocked at q₂ ↔ chirality

Adopt horn-branch step 1's q₂-axis as the chirality axis.

Pro: Already substrate-derived (it's the generation-
discriminating axis). The substrate-vs-tree dichotomy in
locked/unlocked is mechanistically familiar.
Con: This makes A, B both "L-handed" and C "R-handed" (or vice
versa) at the GENERATION level. The SM treats each generation
as having both L and R components. Path γ would have to explain
why the framework's chirality structure operates at the
inter-generation level rather than intra-generation, and what
the SM's intra-generation L/R then is.

Testable consequence: if A, B are L-handed and C is R-handed in
some substrate sense, then PMNS mixing between A and C should
show parity-violating features. Need cross-check.

### Path δ: The framework has NO substrate-level chirality

Accept that none of (1)-(5) is the framework-native chirality.
SM chirality is then a framework-downstream / framework-empirical
fact: the substrate produces the gauge sector, the mass sector,
and the figure-8 dynamics; SM L/R asymmetry is a labeling
convention overlaid on the substrate's gauge identification.

Pro: This is the framework's CURRENT honest position per
`gauge_high_scale_identification.md` L106-113. It's the
discipline-default.
Con: It leaves an apparently-substrate-natural concept (chirality)
as empirical-shelf. Combined with the apparatus-extension being
structurally declined, this would mean **the framework
structurally declines substrate-level chirality** — the
disposition is closed-as-declined, not closed-as-derived.

Testable consequence: cross-check whether the existing framework
makes any prediction that would fail without explicit chirality
input. If the framework already reproduces all chirality-dependent
SM observables (parity violation, V-A structure, etc.) from its
existing apparatus without explicit chirality, path δ is
sustained. If not, path δ fails and one of α/β/γ must be
investigated.

---

## What this iteration step DOES establish

1. **Survey of the framework's existing chirality-adjacent
   apparatus** with five distinct loci named.

2. **The load-bearing gap is identification**, not absence:
   SU(2)_L vs SU(2) generic. Already acknowledged in
   `gauge_high_scale_identification.md` L106-113.

3. **Internal inconsistency surfaced** between
   `mass_sector_closure.md` (walker round-trip) and
   `fourth_generation_revisited.md` (chirality-squared) on the
   meaning of `k_lepton = q_3²`. To be resolved in iteration 2.

4. **Four hypothesis paths named** (α, β, γ, δ), with discipline-
   default being δ (no substrate-level chirality, SM L/R is
   framework-downstream/empirical).

5. **The arc's bounds**: the apparatus-extension fallback is
   structurally declined, so the bridge cannot add new substrate
   structure. Any successful bridge must use one of the existing
   five chirality-adjacent loci.

---

## What this iteration step does NOT establish

- No bridge is proposed as derived.
- No identification of any specific chirality axis with SM L/R.
- No resolution of the internal inconsistency in (4).
- No cross-check against parity violation phenomenology.

These are iteration 2+ work.

---

## Falsifiers for this iteration's survey

The survey itself is falsifiable:

1. **Missed chirality locus.** If a sixth distinct
   chirality-adjacent structure exists in the framework (e.g.,
   embedded in the Klein-Z₂ Z2 structure, the (S × R) coupled J
   action, or somewhere else in the apparatus) and was not
   surfaced by this survey, the iteration is incomplete and the
   sixth structure may be the natural bridge candidate.

2. **Misread inconsistency.** If the apparent inconsistency in
   (4) is actually a difference of framing rather than substance
   — i.e., walker round-trip and chirality-squared describe the
   same substrate object — the inconsistency dissolves and (4)
   becomes a single chirality identification rather than two
   competing ones.

3. **Path classification error.** If the four paths α/β/γ/δ
   miss a viable fifth path (perhaps a hybrid using two of the
   five loci together), the iteration's plan is incomplete.

4. **SU(2)_L already-forced.** If
   `gauge_high_scale_identification.md` L106-113's statement
   "not fully forced" is overly modest — if the structural
   arguments listed there actually force SU(2)_L as the unique
   SU(2) identification — then the gap is smaller than this
   iteration claims, and the bridge may be local to that
   derivation rather than a separate arc.

---

## Plan for iteration 2

Iteration 2 should attempt, in order:

**Step 1 — Resolve the k_lepton = q_3² internal inconsistency
(reading 4).** Cross-check `mass_sector_closure.md` and
`fourth_generation_revisited.md`; determine whether
"chirality-squared" and "walker round-trip" describe the same
substrate object. Outcome: either two distinct readings of the
same fact, in which case the inconsistency dissolves; or two
genuinely different readings, in which case the iteration must
pick one as canonical for the arc going forward.

**Step 2 — Determine if any of α, β, γ has structural support
beyond statement.** Specifically: does the framework's SU(2)
gauge derivation single out cos-y over sin-y (testing α), or
single out a particular loop direction over the other (testing
β), or single out one of q₂-locked vs q₂-unlocked (testing γ)?
If exactly one path has structural support, that becomes the
substrate-chirality candidate. If none does, path δ becomes the
verdict.

**Step 3 — Cross-check the favored path against parity violation
phenomenology.** Specifically: under the chosen mapping, does
the framework predict V-A structure of weak currents? Does it
predict left-handed neutrinos? If yes, the bridge closes (with
appropriate cross-checks on other chirality-dependent
observables). If not, the path fails and iteration moves to the
next.

---

## Cross-links

- `klein_bottle_restructure_price.md` — apparatus-extension
  fallback closed; vocabulary-bridge is sole route.
- `klein_z2_decomposition_falsifier_2.md` — modal y-parity
  finding (locus 1).
- `figure_eight.md` L283-285 — chirality as loop orientation
  (locus 2).
- `horn_branch_iteration_2_step_1.md` — q₂-locked/unlocked
  axis (locus 3).
- `mass_sector_closure.md` L46-65 — walker round-trip reading
  of k_lepton = q_3² (locus 4a).
- `fourth_generation_revisited.md` L63 — chirality-squared
  reading of k_lepton = q_3² (locus 4b).
- `gauge_high_scale_identification.md` L106-113 — explicit
  SU(2)_L identification commitment (locus 5; load-bearing gap).
- `gauge_sector_lovelock.md` — SU(3) × SU(2) × U(1) gauge
  derivation; need to read for path α/β/γ structural-support
  test in iteration 2 step 2.
- `gauge_dictionary.md` — referenced by L113 for the
  identification commitment formalism.
- `basepoint_principle.md` — operationally-open vs
  structurally-declined; the vocabulary-bridge is operationally
  open with path δ as the default discipline-declined outcome.
- `ansatz_audit_policy.md` — Class 2 (re-description) vs
  Class 3 (forced) policy; current SU(2)_L identification is
  Class 2.

---

## One-line summary

Iteration 1 of the vocabulary-bridge surveys the framework's
existing chirality-adjacent apparatus and finds **five distinct
loci** — y-parity (cos/sin), loop orientation, q₂-locked/unlocked,
the inconsistent walker-round-trip-vs-chirality-squared readings
of `k_lepton = q_3²`, and the SU(2)_L identification commitment
— along with an internal inconsistency between
`mass_sector_closure.md` and `fourth_generation_revisited.md`
that needs resolution, and identifies the load-bearing gap as
the explicit SU(2)_L identification commitment named in
`gauge_high_scale_identification.md` L106-113 ("not fully forced
... residual freedom is one identification commitment"); four
hypothesis paths α/β/γ/δ are named for iteration 2 to attempt
in order, with path δ (no substrate-level chirality; SM L/R is
framework-downstream/empirical) being the discipline-default
verdict if no substrate path produces SU(2)_L as forced, and
the **substrate-chirality status closing as structurally
declined** in that case — a cleaner disposition than current
"identification commitment" status.
