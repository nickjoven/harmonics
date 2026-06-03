# Vocabulary-bridge iteration 2 step 2 — labeling constraint check

## Status

**Verdict: THREE "NO" ANSWERS. Path δ' closes.** Reading the
three docs named in iteration 2 step 1's plan
(`gauge_sector_lovelock.md`, `q_mod2_conservation_theorem.md`,
`gell_mann_nishijima.md`) for any substrate constraint on the
L vs R labeling of the lepton doublet/singlet structure, all
three return "no constraint": the substrate forces the
kinematic split (doublet sector vs singlet sector) but does not
prefer one orientation as "L" over the other.

The vocabulary-bridge arc closes with the disposition:

> **Substrate-forced**: the lepton sector has a doublet/singlet
> kinematic split (the SU(2)-coupled doublet sector and the
> Z₂-fixed-point singlet sector are structurally distinct
> substrate objects).
>
> **Observation-fixed**: which sector is labeled "L-handed"
> (coupling to W bosons) and which is labeled "R-handed" is the
> SM's empirical choice, not substrate-forced.

This is the framework's honest position on SM chirality. The
apparatus-extension fallback was structurally declined by
empirical floor (`klein_bottle_restructure_price.md`). The
vocabulary-bridge cannot do more than this — and doesn't need to.
The remaining commitment is *binary* (which of the two substrate
sectors corresponds to "L"), narrowed from iteration 1's "is
chirality substrate at all?"

Class: substrate-derivation arc closure (Class 3, vocabulary-bridge
final step producing path δ' as honest disposition).

---

## Check (a): `gauge_sector_lovelock.md`

**Question**: does the SU(2) gauge derivation distinguish the two
SU(2) representations (doublet vs singlet) by something other
than SM convention?

**Reading**:

The doc derives the gauge group `SU(3) × SU(2) × U(1)` from
substrate primitives (Cartan classification, Z₂ × Z₃ center,
Utiyama's theorem). On the question of which SU(2) — i.e.,
SU(2)_L vs SU(2)_R — L191-196 states:

> "So the topology supplies a U(1), and the charge table + GNN
> + anomaly cancellation promotes it to U(1)_Y. **This is the
> weakest link in the chain** — the U(1) group exists a priori
> from the periodic direction, but its **identity** as
> hypercharge is fixed by the charge constraints, not by the
> topology alone. D43 formalises GNN; until then, U(1)_Y is
> identified a posteriori."

By the same structure: the SU(2) group exists a priori from the
Z₂ center of the antiperiodic direction, but its identity as
SU(2)_L specifically (rather than SU(2)_R or a generic SU(2)) is
*identification*, not topology-forced.

The doc explicitly names this in its own terms: "U(1)_Y is
identified a posteriori." The same reasoning applies to SU(2)_L.

**Verdict (a)**: NO substrate constraint on the L vs R labeling.
The framework derives an SU(2) gauge group; identification as
SU(2)_L is a posteriori, consistent with
`gauge_high_scale_identification.md` L106-113's "identification
commitment."

---

## Check (b): `q_mod2_conservation_theorem.md`

**Question**: does Q mod 2 have a sign convention or
orientation-dependent structure that fixes which sector is L vs R?

**Reading**:

Q mod 2 is a Z₂-valued invariant — it takes values in {0, 1}.
It is the parity of the winding number along the antiperiodic
x-loop. The doc derives its conservation under local processes
and the impossibility of changing it without a non-local
operation.

Q mod 2 has **no sign**. The Z₂ structure is `{even winding, odd
winding}`, which is symmetric under the relabeling `0 ↔ 1` in
the sense that the invariant is the mod-2 reduction of an
integer winding count. There is no "positive Q" vs "negative Q"
distinction — Q mod 2 is unsigned.

Therefore Q mod 2 cannot fix an L vs R labeling on the lepton
doublet, because there is no L vs R-style sign in Q mod 2 to
match against.

**Verdict (b)**: NO substrate constraint on the L vs R labeling.
Q mod 2 is a Z₂ scalar invariant; no sign convention to fix L vs R.

---

## Check (c): `gell_mann_nishijima.md`

**Question**: is hypercharge Y substrate-signed in a way that
would fix the L vs R labeling?

**Reading**:

This doc was the most carefully relevant. Three load-bearing
findings:

### (c.1) Charge sign is detector-relative

L29-30:

> "The Klein bottle fractions {1/3, 1/2, 2/3} give |Q| = {1/3,
> 1/2, 2/3} directly. **The sign comes from the direction of
> winding relative to the detector's reference phase.**"

Charge sign (positive vs negative Q) is *detector-reference-relative*,
not substrate-absolute. If charge sign were substrate-forced,
this would be the place to derive it — but the doc explicitly
identifies it as relative.

### (c.2) Doublet/singlet split IS substrate-forced

L32-48:

> "The smallest half-integer is 1/2. The fundamental
> representation of the SU(2) gauge group acting on the
> antiperiodic-x sector is the doublet, with components labeled
> by `T_3 = ±1/2`. **Singlet modes (`T_3 = 0`) do not transform
> under the antiperiodic identification — they live in the
> integer-wavenumber sector forbidden in this direction by the
> BC, so they appear as fixed points of the Z_2 action rather
> than as carriers of T_3.**"

This is the substrate-forced doublet/singlet split:
- **Doublet sector**: half-integer x-wavenumbers (antiperiodic),
  carries T_3 = ±1/2, SU(2)-coupled.
- **Singlet sector**: integer-wavenumber (Z₂ fixed points),
  T_3 = 0, NOT SU(2)-coupled.

These are structurally distinct substrate sectors. The substrate
forces this kinematic split.

### (c.3) The R-action on Y reverses sign — but doesn't fix L vs R

L107:

> "The reflection sends Y → -Y. It reverses the hypercharge."

Under the Klein-bottle reflection y → L_y − y, hypercharge sign
flips. This is a substrate-symmetry transformation, not a sign
convention.

This *could* have been a substrate constraint on which sector is
L vs R if the substrate had a preferred direction for R (a
canonical orientation of the reflection). But the framework's
reflection is a *symmetry* — both forward and reversed actions
are present in the substrate. There is no preferred orientation
that the substrate forces.

### (c.4) The "right-handed singlets" labeling at L169 is SM convention

L169-172:

> "**Right-handed singlets** (T_3 = 0):
> - u_R: Q = 2/3, Y = 2(2/3) = 4/3
> - d_R: Q = -1/3, Y = 2(-1/3) = -2/3
> - e_R: Q = -1, Y = 2(-1) = -2"

The doc uses "Right-handed singlets" labeling — this is SM
convention applied to the framework's singlet sector. The
framework forces "singlets exist as Z₂-fixed-point modes"; the
SM labels these as "right-handed." Whether to call them R or L
is not a substrate question.

**Verdict (c)**: NO substrate constraint on the L vs R labeling.
The doublet/singlet split is substrate-forced; the hypercharge
sign is detector-relative; the reflection's Y → -Y is a symmetry
without preferred orientation; the "L vs R" labels in the doc
are SM convention.

---

## Three "no" answers → path δ' closes

All three docs return "no substrate constraint on the labeling."
The path enumeration from iteration 1, as refined through
iteration 2:

| Path | Status at iteration 1 | Status at iteration 2 step 2 |
|---|---|---|
| α (y-parity) | Operationally open | Remains separate possibility (not lepton-specific; does not align with doublet structure) |
| β (loop orientation) | Operationally open | Eliminated (figure-8 audit Class 2) |
| γ (q₂ locked/unlocked) | Operationally open | Generation discriminator, NOT chirality (not lepton-specific) |
| δ (no substrate-level chirality) | Discipline-default | **Refined to δ': closed** |
| ε (lepton at saddle-node tangent) | Surfaced conversationally | Converges with δ' |

**Path δ' final form**:

> The substrate **substrate-forces** the lepton sector's
> doublet/singlet kinematic split (the antiperiodic-x half-integer
> wavenumber sector hosting the SU(2)-coupled doublet, and the
> integer-wavenumber Z₂-fixed-point sector hosting the
> SU(2)-decoupled singlet). The substrate **does not force** the
> L vs R *labeling* of which sector is "left-handed" — this is
> fixed by parity-violation experiments (which chirality couples
> to W bosons), an observation-determined identification
> commitment.

This is the framework's honest disposition on SM chirality.
Combined with the price ledger's empirical exclusion of the
apparatus-extension fallback, the **substrate-chirality
disposition is fully closed**:

- **Apparatus-extension fallback**: structurally declined by
  empirical floor (would predict ℍ-QM).
- **Vocabulary-bridge**: substrate-forces doublet/singlet
  kinematic structure; the L vs R labeling is observation-fixed.

The full disposition: substrate has the kinematic *structure*
that the SM's chirality apparatus uses, but the framework neither
forces nor needs to derive *which* chirality couples to weak
bosons. That binary fact is observation.

---

## What this iteration closes

1. **The vocabulary-bridge arc closes at iteration 2 step 2.**
   Three checks return "no constraint"; path δ' is the honest
   disposition.

2. **The SU(2)_L identification commitment narrows to a binary
   observation-fixed question.** From iteration 1's "is
   chirality substrate at all?" to iteration 2 step 1's "which
   substrate sector is the L doublet?" — a question answered by
   parity-violation experiments, not by the framework.

3. **The framework's honest position on SM chirality is now
   explicit**: kinematic structure substrate-forced (doublet/singlet
   split), labeling observation-fixed. This is *more than*
   iteration 1's path δ admitted (substrate has more chirality-
   adjacent forcing than "none at all") and *less than* full
   substrate-chirality (the SM labeling is not in the substrate).

4. **Path δ' is a productive null at the arc level**, in the
   refined sense from `canonical_glossary.md`: substrate is
   admitting what it forces (the doublet/singlet split) and
   correctly not forcing what observation fixes (the labeling).
   No derivation failure — substrate doing its job.

---

## What this iteration does NOT close

- **Path α (y-parity) and path γ (q₂ locked/unlocked) remain
  operationally open** as separate possibilities at iteration
  arc closure. They are not chirality candidates per the
  resolved framing; they may be other substrate structures with
  independent significance.

- **Specific parity-violation derivations from substrate**
  remain framework-downstream / observation-anchored. The
  framework derives the structure that the parity-violation
  apparatus acts on; it does not derive the parity-violation
  itself.

- **Whether the lepton-doublet's L-labeling has any further
  substrate reflection** in observables. E.g., does the framework
  predict cross-section asymmetries in parity-violating processes
  beyond what the SM does? Not currently — but the question
  isn't structurally closed either.

---

## Falsifiers for path δ' closure

The closure verdict is itself falsifiable:

1. **Missed substrate constraint.** If a closer reading of
   `gell_mann_nishijima.md`'s "reflection sends Y → -Y" or
   `q_mod2_conservation_theorem.md`'s winding-number structure
   reveals a substrate-preferred orientation that fixes L vs R
   (not just a symmetry but a *broken* symmetry forced by
   topology), the closure inverts and substrate-chirality
   becomes substrate-forced. The doc's authors do not currently
   identify such a forcing; future audits could.

2. **Path α or γ produces a labeling constraint.** If a future
   iteration shows that y-parity (cos vs sin) OR q₂-locked/unlocked
   correlates with the L vs R labeling through a downstream
   derivation, the labeling constraint exists at a different
   layer than checked here. Closing α and γ as separate
   possibilities (this step) is the discipline-correct move; if
   they re-enter as chirality candidates later, the arc reopens.

3. **The Klein-bottle restructure reads differently under finer
   resolution.** If the apparatus-extension's empirical decline
   is found to apply only to a specific class of restructures
   (not all second-antiperiodic-cycle constructions), the
   reconstruction option could partially reopen. Currently no
   evidence for this; the price ledger's verdict stands.

---

## Updated disposition table

For `framework_status.md` and `canonical_glossary.md` consistency:

| Item | Disposition |
|---|---|
| Apparatus extension to substrate-chirality | Structurally declined by empirical floor (`klein_bottle_restructure_price.md`) |
| Vocabulary-bridge to substrate-chirality | Closed at path δ': kinematic structure substrate-forced, labeling observation-fixed (this doc) |
| Lepton SU(2) doublet/singlet split | Substrate-forced (`mass_sector_closure.md`, `gell_mann_nishijima.md`) |
| SU(2)_L identification | Observation-fixed (parity violation experiments); previously "identification commitment" in `gauge_high_scale_identification.md` |
| Substrate-level chirality | Closed as: structure forced, labeling not forced |

---

## Cross-links

- `vocabulary_bridge_iteration_1.md` — five-loci survey;
  identification commitment named.
- `vocabulary_bridge_iteration_2_step_1.md` — locus (4)
  resolution; refined path δ' introduced.
- `klein_bottle_restructure_price.md` — apparatus-extension
  fallback structurally declined.
- `gauge_sector_lovelock.md` L191-196 — check (a); identification
  a posteriori.
- `q_mod2_conservation_theorem.md` — check (b); Z₂ scalar
  invariant, no sign.
- `gell_mann_nishijima.md` L29-48, L107, L169 — check (c);
  doublet/singlet split substrate-forced, labeling SM convention.
- `gauge_high_scale_identification.md` L106-113 — SU(2)_L
  identification commitment narrowed by this resolution.
- `mass_sector_closure.md` L47-64 — walker round-trip on doublet
  structure.
- `fourth_generation_revisited.md` L165-171 — chirality-asymmetry
  vocabulary.
- `figure_eight_necessitation_audit.md` — figure-8 Class 2; path
  β eliminated.
- `canonical_glossary.md` — chirality entry (Section 10);
  possibility-discipline distinctions (Section 8).
- `basepoint_principle.md` — operationally-open vs structurally-
  declined; path δ' is "substrate-admitted with observation-
  determined labeling" rather than declined.

---

## One-line summary

Iteration 2 step 2 reads `gauge_sector_lovelock.md` (check a),
`q_mod2_conservation_theorem.md` (check b), and
`gell_mann_nishijima.md` (check c) for any substrate constraint
on the L vs R labeling of the lepton's substrate-forced
doublet/singlet split; all three return **no constraint** — (a)
the SU(2) is derived but the SU(2)_L identification is "a
posteriori" per L191-196, (b) Q mod 2 is a Z₂ scalar invariant
with no sign, (c) charge sign is detector-relative per L29-30,
the reflection's Y → -Y is a symmetry not a forced orientation,
and the "right-handed singlets" labeling at L169 is SM convention
applied to the substrate's Z₂-fixed-point sector; **path δ'
closes the vocabulary-bridge arc**: the substrate forces the
doublet/singlet kinematic structure (more than iteration 1's
path δ admitted), but the L vs R labeling is observation-fixed
(less than full substrate-chirality), narrowing the SU(2)_L
identification commitment from iteration 1's "is chirality
substrate?" to "which substrate sector is L?" — a binary fact
fixed by parity-violation experiments, not by the framework;
combined with the price ledger's empirical exclusion of the
apparatus-extension, **the full substrate-chirality disposition
closes**: kinematic structure substrate-forced, labeling
observation-fixed, no further bridge work indicated within
current apparatus, paths α and γ persist as separate
operationally-open possibilities unrelated to chirality, and
the framework's honest position on SM chirality is now
explicit in the disposition table.
