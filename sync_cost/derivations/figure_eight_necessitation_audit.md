# Figure-8 necessitation audit — basepoint-principle inspection

## Status

**Audit verdict: CLASS 2 (re-description / useful frame), NOT
SUBSTRATE-FORCED.** The figure-8 topology in `figure_eight.md` is
adopted as an organizing frame for the substrate's 4 surviving
Klein-bottle modes; it is **not** structurally forced by the
substrate apparatus.

The substrate forces:
- 4 modes at `(q_x, q_y) ∈ {(2, 3), (3, 2)}` (XOR rule on Klein
  bottle)
- Two-family grouping by `(q_x, q_y)` denominator pair
- D-state's uniqueness (only mode with both directions unlocked)
- D-crossing's geometric placement at antipodal `L_x / 2` on the
  antiperiodic x-cycle (a property of the Klein-bottle Z₂
  topology, independent of the figure-8 reading)

The substrate **does not force**:
- The "two loops" continuous S¹ interpretation (the 4 modes are
  discrete points, not continuous loops)
- The figure-8 graph structure (4 vertices + edges arrangement is
  an interpretive choice; alternatives like complete graph K_4,
  disjoint loops, or directed graph K_4 would not break anything
  in the substrate apparatus)
- The "crossing point" interpretation of D
- The downstream C/P/T identification chain insofar as it
  depends on the figure-8 reading being substrate-forced

Under the framework's own `ansatz_audit_policy.md` L47-49 test —
"what would change if the f were slightly different? If nothing
in the framework breaks, the f is not forced" — the figure-8
fails the forcing test. The substrate would have the same 4
modes, the same 2 families, the same D-uniqueness without the
figure-8 frame.

This audit was prompted by the user's observation during the
vocabulary-bridge iteration 1 work that the figure-8 "was a bit
of a fit," and the request to inspect its necessitation per the
basepoint principle's discriminator (operationally-open vs
structurally-declined vs substrate-forced).

Class: foundational rigor check (Class 3, meta-audit on an
existing load-bearing apparatus claim).

---

## The basepoint-principle test

The basepoint principle distinguishes:

- **Structurally-forced** — a forcing argument is exhibited with
  a mechanism that breaks under perturbation. The forcing's
  inverse ("what if the f were slightly different?") produces
  something inconsistent with the substrate's primitives.
- **Operationally open** — no derivation produced, no obstruction
  proven. The status is undecided.
- **Structurally declined** — a torsorial-decline argument has
  been exhibited showing the alternative is structurally
  incompatible.
- **Adopted-by-fit / Class 2 (re-description)** — the proposal
  organizes existing structure in a useful way but doesn't add
  forcing. Multiple alternative organizations would work equally
  well; the choice is interpretive.

The figure-8 is in the fourth category, per the test below.

---

## Applying the "what would change?" test

### What the figure-8 reading asserts

`figure_eight.md` L33-39:

> "The Klein bottle's self-intersection in 3D embedding is a
> figure-8 (lemniscate). Two loops sharing one crossing point.
> This is the physical topology of the four Klein bottle modes
> (D19). **The figure-8 is not an artifact of embedding — it is
> the structure.** The crossing point is where observation
> happens. The loops are the two sectors. The traversal is
> time. The twist is imaginary number."

`figure_eight.md` L41-60:

> "From Derivation 19, the Klein bottle's XOR parity constraint
> collapses 1,764 candidate mode pairs to exactly 4 survivors
> at `(q_1, q_2) in {(2,3), (3,2)}`. These organize into two
> sectors:
>
> - **Loop 1** = sector (2,3): modes A and B.
> - **Loop 2** = sector (3,2): modes C and D.
>
> Each loop is a circle (S^1) parameterized by the phase in
> the respective sector. The two loops share exactly one point:
> the D state (both unlocked), where the trajectories on both
> loops pass through the same phase configuration.
>
> The figure-8 = Loop 1 ∪ Loop 2, with Loop 1 ∩ Loop 2 = {D}."

*[2026-08-10 correction at source: the quoted "collapses 1,764
candidate mode pairs to exactly 4 survivors" misattributes the
collapse — the XOR filter reduces 3,969 pairs to 1,764; the
field-equation dynamics collapses those to 4. `figure_eight.md` has
been corrected; the quote is preserved as it stood.]*

So the figure-8 reading asserts:
1. Each (q_x, q_y) family is a continuous S¹ (a loop).
2. The two loops share exactly one point: D.
3. The resulting graph is a figure-8.

### What the substrate independently forces

The substrate, per the XOR derivation in `klein_bottle.md` L570-590,
produces:
- 4 discrete modes at specific lattice points: `(1/2, 1/3)`,
  `(1/2, 2/3)`, `(1/3, 1/2)`, `(2/3, 1/2)`.
- These 4 modes split into 2 families by denominator pair:
  - Family (q_x=2, q_y=3): `(1/2, 1/3)`, `(1/2, 2/3)`
  - Family (q_x=3, q_y=2): `(1/3, 1/2)`, `(2/3, 1/2)`
- The D state (both directions unlocked, no specific tongue) is
  unique by the classification.

### The forcing test

**What would change if instead of a figure-8, the framework
adopted a different organization?**

Consider three concrete alternatives:

**Alternative (i): Two disjoint loops (no shared crossing).** The
4 modes split as before, but D is not treated as a "shared
crossing" — it is just a separate mode (the dark state). Under
this reading:
- The 4-mode XOR derivation is unchanged.
- Mass sector closure (`k_lepton = q_3²`, etc.) is unchanged.
- Gauge sector derivation (SU(3) × SU(2) × U(1)) is unchanged.
- The `J² = −I` derivation in `figure_eight.md` L155-228 would
  need a different geometric justification (the antipodal L_x/2
  placement comes from the Klein-bottle Z_2 directly, not from
  the figure-8 reading per se — see below).
- The framework's existing C/P/T identification in
  `figure_eight.md` L275-301 would lose its "figure-8 symmetry"
  motivation but the underlying 4-mode symmetry group is the
  same.
- The downstream `sin²θ_W = 8/35` derivation would lose its
  "crossing probability" motivation — but `figure_eight.md`'s own
  disposition note at L6-13 already records `sin²θ_W = 8/35` as
  Fails / coincidence, so this loss is not new.

**Alternative (ii): Complete graph K_4 (all modes connected).**
The 4 modes are vertices; pairwise edges connect all of them.
Under this reading:
- Substrate apparatus unchanged.
- The dark state D loses its special "crossing" status (it is
  just one of 4 vertices), but D-uniqueness (only doubly-unlocked
  mode) is preserved at the substrate level.
- The figure-8's downstream "two-loop" interpretation breaks,
  but the 4-mode-substrate-forced structure is preserved.

**Alternative (iii): Directed graph with arrows from locked to
unlocked.** The 4 modes are vertices; arrows from {A, B} →
{C, D} based on dropping the q₂-lock. Under this reading:
- Substrate apparatus unchanged.
- The horn-branch step 1's q₂-locked vs q₂-unlocked distinction
  becomes the "primary" organization rather than the figure-8's
  "by-loop" organization.
- This reading is more consistent with the generation-
  classification work but loses the figure-8's symmetry-frame
  utility.

In all three alternatives, **the substrate's forced structure
(4 modes, 2 families, D-uniqueness) is unchanged**. The figure-8
reading is one of several possible organizing frames. Under
`ansatz_audit_policy.md` L47-49 — "what would change if the f
were slightly different? If nothing in the framework breaks,
the f is not forced" — the figure-8 fails the forcing test.

---

## What survives the audit as substrate-forced

The audit is not destructive. Specific findings survive:

### (i) The 4 modes at (q_x, q_y) ∈ {(2, 3), (3, 2)} 

Substrate-forced via the XOR derivation in `klein_bottle.md`. No
audit needed; this is downstream of the Klein-bottle topology.

### (ii) The 2-family split

Substrate-forced via the (q_x, q_y) denominator pair structure.
The two families have different physical roles (one is
(antiperiodic, periodic), one is (periodic, antiperiodic)
relative to the Klein-bottle directional asymmetry).

### (iii) D-state's uniqueness

Substrate-forced via the locked/unlocked classification: D is
the unique mode with both directions unlocked (per
`generation_mechanism.md` D32 reference to
`minkowski_signature.md`).

### (iv) The L_x/2 antipodal placement in the J² = −I derivation

This survives as substrate-forced because it depends on the
**Klein-bottle's Z_2 antipodal structure** (the antiperiodic
x-cycle has order 2; after one traversal you return with sign
flip; after two traversals you return to original), NOT on the
figure-8 reading per se.

`figure_eight.md` L196-203 attributes the placement to "the
figure-8's symmetric self-intersection" — under the audit, this
attribution is **re-traced**: the actual forcing comes from the
Klein-bottle Z_2 directly, with the figure-8 just being the
useful frame for visualization.

The corrected J² = −I derivation in `figure_eight.md` L155-228
therefore survives the audit, with the load-bearing forcing
coming from the Klein-bottle apparatus (not the figure-8
interpretation overlay).

### (v) The C/P/T identifications as symmetries of the 4-mode
structure

`figure_eight.md` L275-301 identifies C, P, T as symmetries of
the figure-8. Under the audit:
- These ARE symmetries of the 4-mode structure (loop swap,
  mode swap, twist reversal).
- The 4-mode structure has them as substrate-forced symmetries
  independent of the figure-8 frame.
- The figure-8 frame provides clean geometric visualization but
  doesn't FORCE the symmetries themselves.

So C/P/T survive as substrate-forced symmetries of the 4-mode
apparatus; their identification with figure-8 geometric symmetries
is Class 2 framing.

---

## What does NOT survive as substrate-forced

### (a) The figure-8 as "physical topology" claim

`figure_eight.md` L37: "The figure-8 is not an artifact of
embedding — it is the structure." This claim does not survive
the audit. The figure-8 IS a useful frame for organizing the
4-mode substrate; calling it "the structure" overclaims its
status.

### (b) The "two loops as continuous S¹" interpretation

The 4 modes are discrete points. The S¹ continuity is an
interpretive overlay (presumably parameterizing each family's
internal phase). The continuous S¹ is not substrate-forced.

### (c) The figure-8 reading of P (parity) as "loop orientation"
swap

`figure_eight.md` L283-285:

> "**P (parity)** = mode swap within each loop. Exchange the
> locked and unlocked states within a sector. This swaps left
> and right chirality (the two orientations of the loop)."

Under the audit:
- The "mode swap within each loop" IS a substrate-forced
  symmetry of the 4-mode apparatus.
- The identification of this swap with "left and right
  chirality" and "the two orientations of the loop" is **Class
  2** — it is an interpretive overlay on the substrate symmetry,
  not a substrate-forced identification of chirality.

This is directly load-bearing for **vocabulary-bridge iteration
1 path β** (`vocabulary_bridge_iteration_1.md`): if the figure-8
reading is Class 2, then path β (loop orientation ↔ chirality)
is also Class 2. Path β cannot force substrate-chirality; it
merely identifies one identification commitment with another.

### (d) The sin²θ_W = 8/35 "crossing probability" derivation

Already noted as Fails / coincidence in `figure_eight.md`'s own
disposition note L6-13. The audit confirms: this derivation
depended on the figure-8 reading's "crossing event" interpretation,
which is Class 2.

### (e) The W±/Z gauge boson identification via figure-8
crossings

`figure_eight.md` L124-148 identifies photon, Z, W± with
specific traversal patterns at the figure-8 crossing. This is
Class 2 motivational frame; the actual substrate forcing of the
gauge bosons comes from `gauge_sector_lovelock.md`'s SU(3) ×
SU(2) × U(1) derivation, not from the figure-8 traversal
picture.

---

## Implications for vocabulary-bridge iteration 1

The vocabulary-bridge survey identified five chirality-adjacent
loci in `vocabulary_bridge_iteration_1.md`. The figure-8 audit
affects locus (2) and path β directly:

| Locus | Pre-audit status | Post-audit status |
|---|---|---|
| (1) y-parity (cos/sin) | Modally populated | Unchanged |
| (2) Loop orientation | Explicit chirality identification | **Class 2** (interpretive overlay) |
| (3) q₂-locked/unlocked | Generation axis | Unchanged |
| (4) k_lepton = q_3² internal inconsistency | Open | Unchanged |
| (5) SU(2)_L identification commitment | Load-bearing gap | Unchanged |

Path β (Loop orientation ↔ chirality) is now Class 2, NOT a
viable substrate-forcing route. The vocabulary-bridge's iteration
2 should eliminate path β from consideration and proceed with
α (y-parity), γ (q₂-locked/unlocked), or δ (no substrate-level
chirality).

The probabilistic weight on path δ (substrate-chirality is
structurally declined) increases under the audit — the framework's
existing "explicit chirality identification" (locus 2) turns out
to be Class 2, leaving substrate-chirality with only paths α
and γ as live forcing-candidate routes.

---

## What this audit DOES establish

1. **The figure-8 is Class 2 (re-description), not
   substrate-forced.** Per `ansatz_audit_policy.md` L47-49's
   forcing test, the figure-8 fails: substrate apparatus is
   unchanged under alternative organizing frames.

2. **The 4-mode substrate apparatus is preserved.** The XOR
   derivation, the 2-family split, D-uniqueness, the
   Klein-bottle Z_2 antipodal structure — all substrate-forced,
   unchanged by the audit.

3. **The C/P/T symmetries survive as 4-mode-substrate symmetries.**
   Their identification with figure-8 geometric symmetries is
   Class 2 framing, but the symmetries themselves are
   substrate-forced.

4. **The J² = −I derivation survives** by re-tracing the
   geometric forcing to the Klein-bottle Z_2 (which IS
   substrate-forced) rather than the figure-8 interpretation
   (which is Class 2).

5. **The vocabulary-bridge's locus (2) and path β are demoted to
   Class 2.** The framework's "explicit chirality identification"
   in `figure_eight.md` L283-285 is interpretive overlay, not
   substrate-forcing of chirality.

6. **The sin²θ_W = 8/35 derivation is confirmed Class 2/Fails**
   (already in the disposition note; audit re-derives this
   conclusion via the forcing test).

---

## What this audit does NOT establish

- The audit does not invalidate the figure-8 as a useful
  visualization tool or pedagogical frame.
- The audit does not invalidate any specific downstream
  derivation that uses substrate-forced apparatus, even if the
  derivation also invokes the figure-8 frame.
- The audit does not rule out a future derivation that would
  PROMOTE the figure-8 from Class 2 to Class 3 — e.g., if a
  substrate-forced topological invariant (Euler characteristic,
  some homotopy class) singled out the figure-8 graph uniquely
  among possible 4-mode organizations.

---

## Falsifiers for this audit's verdict

The Class 2 verdict is itself falsifiable:

1. **Substrate forcing of figure-8 found.** If a future derivation
   shows that a specific substrate-forced topological invariant
   selects the figure-8 graph uniquely among alternative
   organizations (e.g., the only 4-vertex graph compatible with
   the Klein-bottle Z_2 + XOR rule), the verdict promotes from
   Class 2 to Class 3/4/5. The "what would change?" test then
   passes because the audit can no longer construct alternatives
   that preserve substrate apparatus.

2. **Alternative organization breaks the substrate.** If
   alternative organizations (i)-(iii) named above actually do
   break some substrate-forced result that this audit overlooked
   (e.g., a specific gauge-sector or mass-sector derivation that
   depends on the figure-8 frame in a way the audit missed),
   the audit is incomplete and the verdict shifts.

3. **The "4-mode-symmetry-substrate-forced" claim itself fails.**
   The audit claims C/P/T are substrate-forced symmetries of
   the 4-mode apparatus independent of the figure-8 frame. If
   a closer reading shows that the 4-mode symmetries themselves
   depend on the figure-8 organization for their identification,
   the audit's "what survives" list shortens.

---

## Discoverability propagation (per `feedback_null_promotion.md`)

The figure-8 audit affects multiple framework docs. Per the
session's null-promotion methodology:

- `figure_eight.md` should carry a top-of-doc audit notice
  pointing here. The existing disposition note (top of
  `figure_eight.md`) already flags sin²θ_W = 8/35 as Open/Fails;
  the audit adds the figure-8-as-frame finding.

- `vocabulary_bridge_iteration_1.md` should note that path β
  (Loop orientation ↔ chirality) is demoted to Class 2 per this
  audit, and that iteration 2's path enumeration narrows to
  {α, γ, δ}.

- Other docs that cite figure_eight.md's chirality identification
  or other Class 2 figure-8 readings should carry inline notices
  pointing to this audit. The propagation sweep can follow the
  same pattern as commit `a9d3fa4` (downstream w* misreading
  audit notices) — though the figure-8 has more usage points
  than `boundary_weight.md` did, so the sweep may be larger.

---

## Cross-links

- `figure_eight.md` — the audited doc.
- `ansatz_audit_policy.md` L47-49 — forcing test used in this
  audit ("what would change if the f were slightly different?").
- `basepoint_principle.md` — operationally-open vs
  structurally-declined vs substrate-forced discriminator.
- `klein_bottle.md` L570-590 — XOR derivation that substrate-
  forces the 4 modes.
- `klein_bottle_derivation.md` L553-558 — Klein-bottle Z_2
  directional assignment (load-bearing for the J² = −I
  derivation's geometric forcing).
- `gauge_sector_lovelock.md` — the actual substrate forcing of
  gauge sector (independent of figure-8 frame).
- `vocabulary_bridge_iteration_1.md` — path β now Class 2 per
  this audit; locus (2) status update.
- `mass_sector_closure.md`, `generation_mechanism.md` — survive
  the audit as substrate-forced; their figure-8 references are
  Class 2 framing on top of substrate-forced derivations.
- `feedback_null_promotion.md` (memory) — methodology for
  discoverable propagation of audit findings.

---

## One-line summary

The figure-8 in `figure_eight.md` is audited under the basepoint
principle's discriminator and found to be **Class 2
(re-description / useful frame), NOT substrate-forced**: the
substrate apparatus produces 4 modes at `(q_x, q_y) ∈ {(2,3), (3,2)}`
with D-state uniqueness via the XOR derivation, but the figure-8's
specific "two loops sharing one crossing" organization is one of
several possible frames (disjoint loops, K_4, directed graph all
preserve the substrate apparatus) and fails the
`ansatz_audit_policy.md` L47-49 forcing test "what would change
if the f were slightly different?"; what survives as substrate-
forced is the 4-mode structure, the 2-family split, D-uniqueness,
and the C/P/T symmetries (as substrate symmetries of the 4-mode
apparatus, with the figure-8 frame being Class 2 visualization
overlay); what does NOT survive is the figure-8 as "the structure"
claim, the "two loops as continuous S¹" interpretation, the
"chirality = loop orientation" reading (which becomes Class 2,
demoting vocabulary-bridge path β and increasing probabilistic
weight on path δ = no substrate-level chirality), and the
sin²θ_W = 8/35 derivation (already flagged Fails in the
disposition note); the J² = −I derivation survives by re-tracing
the geometric forcing to the Klein-bottle Z_2 antipodal structure
directly rather than the figure-8 interpretation overlay.
