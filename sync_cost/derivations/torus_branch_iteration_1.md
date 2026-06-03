# Torus-branch iteration 1 — Z_6 mode lattice as toroidal/poloidal substrate

## Status

**First-pass exploration, resolution-mode.** This is iteration 1
of the torus-branch arc per Task 106, the remaining untouched
item from the original next-leg plan (horn-branch + torus-branch
+ axial-trajectory audit). Horn-branch closed productive null at
iteration 3 step 1; the axial-trajectory audit became the
falsifier-chain → vocabulary-bridge arc and closed at path δ'.
Torus-branch is the last open item.

The hypothesis to be framed: **the framework's already-canonical
Z_6 mode lattice has a natural torus T² = Z_2 × Z_3 reading,
with toroidal direction = q_3 = 3 cycle and poloidal direction
= q_2 = 2 cycle. The surviving evenly-spaced nodes after the
coprime-to-6 filter are exactly the boundary modes
`{1, 5} = φ(6) = 2`, mirror-symmetric about 1/2 — equivalently
the `{1/6, 5/6}` Farey pair at depth 6 in `boundary_weight.md`
L39.**

This is **resolution-mode** work per the canonicalized methodology
(`canonical_glossary.md` Section 8, `feedback_resolution_vs_reconstruction.md`):
the torus reading clarifies existing apparatus (Z_6 lattice +
CRT decomposition + Klein-antipodal action + gauge factor
identification + boundary weight Farey structure), rather than
adding new substrate primitives. The torus is NOT proposed as
the substrate's physical surface (`klein_bottle_derivation.md`
argues the torus is structurally declined at the substrate
level because it lacks an antiperiodic cycle → no fermion
sector). The torus reading lives at the **mode-lattice layer**,
not the physical-surface layer.

No closure is attempted in this iteration. The aim is to
articulate the hypothesis carefully enough that subsequent
iterations have a defined target — comparable to
`horn_branch_iteration_1.md` and `vocabulary_bridge_iteration_1.md`
in scope and structure.

Class: substrate-derivation survey for an open-task arc
(Class 3, iteration-arc opener).

---

## The canonical Z_6 mode lattice

The framework's substrate carries a Z_6 mode lattice as a
canonical object (`canonical_glossary.md` L53;
`klein_antipodal_z2_rep_pattern.md`; `baryon_fraction.md`). The
six modes `{0, 1, 2, 3, 4, 5}` decompose via the Chinese Remainder
Theorem:

    Z_6 = Z_2 × Z_3

with the explicit isomorphism `k → (k mod 2, k mod 3)`:

| k ∈ Z_6 | (k mod 2, k mod 3) |
|---|---|
| 0 | (0, 0) |
| 1 | (1, 1) |
| 2 | (0, 2) |
| 3 | (1, 0) |
| 4 | (0, 1) |
| 5 | (1, 2) |

The Z_6 structure is substrate-forced through the chain:

- **Cube identity** `q_3² − q_2³ = 1` ⇒ `(q_2, q_3) = (2, 3)` (the
  unique Catalan pair via Mihailescu; `mass_sector_closure.md`
  "Connection to the Catalan equation / Mihailescu's theorem")
- **CRT decomposition** `Z_6 = Z_2 × Z_3` follows from
  `gcd(2, 3) = 1`
- **Klein-antipodal Z_2 + Color triplet Z_3** are derived from
  these primitives (`klein_antipodal_z2_rep_pattern.md`)
- **The composite Z_6 = q_2 × q_3 = INTERACT** is the substrate's
  basic mode count (`canonical_glossary.md` L50)

This entire chain is substrate-forced (Mihailescu-strength at
the foundation per the PR #214 connection).

---

## The torus reading

### Direction identification

The Z_6 lattice has a natural **2D torus T² geometric realization**
with the two cycles given by the CRT factors:

- **Poloidal direction** (shorter cycle, period q_2 = 2): the
  Z_2 axis. Two evenly-spaced positions `{0, 1}` per cycle.
- **Toroidal direction** (longer cycle, period q_3 = 3): the
  Z_3 axis. Three evenly-spaced positions `{0, 1, 2}` per cycle.

The 6 mode positions are arranged on the torus as a `2 × 3`
lattice, with each Z_6 mode occupying one lattice point:

```
            toroidal q_3 = 3
                 ▾
    poloidal     ●─────●─────●     ← poloidal = 0 ("even")
    q_2 = 2:     │     │     │
                 ●─────●─────●     ← poloidal = 1 ("odd")

       (poloidal=0): {0, 4, 2}  (positions in Z_6: 0, 4, 2 at toroidal 0, 1, 2)
       (poloidal=1): {3, 1, 5}  (positions in Z_6: 3, 1, 5 at toroidal 0, 1, 2)
```

These are exactly the six Z_6 modes laid out by the CRT
decomposition.

### Gauge factor identification

The toroidal/poloidal directions correspond to the framework's
existing gauge factor identifications
(`gauge_sector_lovelock.md`, `klein_antipodal_z2_rep_pattern.md`):

- **Poloidal Z_2** ↔ **SU(2) weak gauge factor** (Klein-antipodal
  Z_2 action τ : k → −k mod 6 acts on the poloidal coordinate as
  involution)
- **Toroidal Z_3** ↔ **SU(3) color gauge factor** (Color triplet
  Z_3 action σ acts on the toroidal coordinate as cyclic shift)

This mapping is consistent with `gauge_sector_lovelock.md`'s
center derivation (`Z_2 × Z_3 = Z_6` from the GCD structure of
the SM gauge centers). The torus reading is a **geometric
re-articulation** of the existing gauge-factor identification,
not a new derivation.

### The Klein-antipodal action in toroidal/poloidal coordinates

The Klein-antipodal involution τ : k → −k mod 6 acts on the
torus as:

| Z_6 mode | Poloidal | Toroidal | τ(Z_6 mode) | New poloidal | New toroidal |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 5 | 1 | 2 |
| 2 | 0 | 2 | 4 | 0 | 1 |
| 3 | 1 | 0 | 3 | 1 | 0 |
| 4 | 0 | 1 | 2 | 0 | 2 |
| 5 | 1 | 2 | 1 | 1 | 1 |

In toroidal/poloidal coordinates:
- **Poloidal coordinate is fixed** by τ (acts as identity on Z_2 because Z_2 is self-inverse: −0 = 0, −1 = 1 mod 2)
- **Toroidal coordinate is inverted** by τ (acts as Z_3 inversion: −0 = 0, −1 = 2, −2 = 1 mod 3)

So Klein-antipodal acts cleanly: it's the identity on the
poloidal direction and inversion on the toroidal direction.

This gives a sharp toroidal/poloidal asymmetry under τ:
- **Toroidal-asymmetric modes** (toroidal ≠ 0) are paired by τ:
  `1 ↔ 5`, `2 ↔ 4`. These are the antipodal pairs.
- **Toroidal-symmetric modes** (toroidal = 0) are self-paired:
  `0` and `3`. These are the Klein-singlets that don't decompose
  into antipodal eigenmodes (`baryon_fraction.md` L102-103).

The toroidal/poloidal vocabulary makes this structure transparent.

---

## Surviving evenly-spaced nodes

### The coprime-to-6 filter

The framework's baryon-coupling criterion requires a mode to be
**coprime to 6** (cross-sector coupling; `baryon_fraction.md`
L65-78). This filter selects:

- **Surviving**: `{1, 5}` (gcd(1, 6) = gcd(5, 6) = 1)
- **Filtered out**: `{0, 2, 3, 4}` (all share a non-trivial
  factor with 6)

Count: `φ(6) = 2` surviving modes — exactly the Euler totient.

### Even spacing in the relevant sense

The surviving pair `{1, 5}` is evenly spaced in two complementary
readings:

**(i) Mirror-symmetric about the midpoint.** On the Z_6 cycle,
positions 1 and 5 are symmetric about 3 (the cycle's center).
Equivalently, `1/6` and `5/6` are mirror-symmetric about `1/2`.
This is the "evenly spaced about a center" reading.

**(ii) Equal angular spacing from the gauge-center axis.** In
toroidal/poloidal coordinates, both `{1, 5}` modes are at
**poloidal = 1** (the "odd" Z_2 position). Their toroidal
positions are `{1, 2}` — adjacent on the Z_3 cycle, with one
at toroidal `1` and one at toroidal `2`. They flank the
toroidal-zero axis (toroidal = 0) symmetrically.

The two surviving modes are therefore on the **same poloidal
parity** (odd) and on **complementary toroidal positions**
flanking the gauge-center axis. This is the geometric picture
the torus reading gives to the algebraic gcd-with-6 filter.

### Connection to the Farey boundary at depth 6

`boundary_weight.md` L39 names the new Farey fractions at depth
6:

> "phi(6) = 2: there are exactly two new Farey fractions at
> depth 6 (namely 1/6 and 5/6), since the others (2/6, 3/6, 4/6)
> reduce to lower denominators by GCD."

These are exactly the `{1/6, 5/6}` fractions corresponding to
the `{1, 5}` boundary modes. The framework's two readings are
the same object:

- **Modular reading** (`baryon_fraction.md`): `{1, 5}` are the
  coprime-to-6 modes that mediate cross-sector EM coupling.
- **Farey reading** (`boundary_weight.md`): `{1/6, 5/6}` are the
  new Farey fractions at the F_5/F_6 boundary; the partial
  locking of these mediates the cosmological boundary weight w*.
- **Torus reading** (this iteration): the same pair are the
  surviving evenly-spaced nodes at poloidal=1, flanking the
  toroidal-zero axis.

This is a three-way confluence on a single substrate object: the
`{1, 5}` boundary mode pair is the framework's matter-coupling
boundary AND the cosmological coupling boundary AND the surviving
torus-flanking pair.

---

## What the torus reading adds

The hypothesis under test is whether the torus reading adds
**explanatory content** beyond what's already in `Z_6 mode
lattice` (`canonical_glossary.md`), `klein_antipodal_z2_rep_pattern.md`,
and `gauge_sector_lovelock.md`.

### What's genuinely new

1. **Geometric vocabulary**: "toroidal" and "poloidal" make the
   Z_2 × Z_3 decomposition spatially intuitive. The poloidal
   direction is the SU(2) "short cycle"; the toroidal direction
   is the SU(3) "long cycle." Standard physics imports these
   from MHD / tokamak / modular-form contexts; the framework
   already has the underlying structure but not the vocabulary.

2. **Klein-antipodal action geometric reading**: τ acts as
   identity on poloidal and inversion on toroidal. This makes
   the antipodal-pair structure (`baryon_fraction.md` L96-103)
   spatially transparent: pairs are flanking the toroidal-zero
   axis; self-paired modes are ON the axis.

3. **Surviving-pair geometric reading**: the `{1, 5}` boundary
   modes are pair-symmetric about the gauge-center axis in the
   torus picture; equivalently mirror-symmetric about `1/2` in
   the fraction picture. The geometric and algebraic readings
   match.

4. **Three-way confluence sharpened**: matter coupling
   (`baryon_fraction.md`) + cosmological boundary
   (`boundary_weight.md`) + torus flanking pair (this iteration)
   are all the same `{1, 5}` object. The torus reading makes
   this geometric unification natural rather than coincidental.

### What's not new (already canonical)

- The Z_6 mode lattice (canonical via `klein_antipodal_z2_rep_pattern.md`)
- The CRT decomposition Z_6 = Z_2 × Z_3 (number-theoretic fact)
- The gauge factor identification SU(3) ↔ Z_3 sector, SU(2) ↔
  Z_2 sector (canonical via `gauge_sector_lovelock.md` and
  `gauge_dictionary.md`)
- The boundary mode pair `{1, 5}` and the baryon = Klein-singlet
  AND coprime-to-6 derivation (canonical via `baryon_fraction.md`)
- The `{1/6, 5/6}` Farey fractions at depth 6 (canonical via
  `boundary_weight.md`)

The torus reading is a **vocabulary refinement** more than a
new derivation. This is consistent with the resolution-mode
discipline.

---

## Critical caveat: the torus is NOT the substrate's physical surface

`klein_bottle_derivation.md` argues at length that the torus is
**structurally declined** as the substrate's physical surface:

- The torus has H_1(T²) = Z ⊕ Z (both free generators)
- The Klein bottle has H_1(K²) = Z ⊕ Z_2 (free + torsion)
- The Z_2 torsion is what makes the substrate's fermion sector
  possible (complex amplitudes from the antiperiodic-cycle count)
- Without the Z_2 torsion, no fermions

The substrate is the Klein bottle, not the torus. The torus
reading proposed here lives at the **mode-lattice layer** (the
Z_6 quotient of the Klein-bottle mode space), not the physical
surface layer.

This distinction matters because:

1. **Both readings are consistent**: the Klein bottle (physical)
   carries the Z_6 mode lattice (quotient) which admits a torus
   geometric realization (T² = Z_2 × Z_3). No conflict.

2. **Different roles**: the Klein bottle is the substrate's
   physical surface for trajectories; the torus is the geometric
   realization of the mode quotient. They live at different
   layers.

3. **Resolution-mode discipline**: the torus reading does not
   propose to *replace* the Klein bottle. It re-articulates an
   existing canonical structure (Z_6 lattice) in geometric
   vocabulary.

If a future iteration were to propose the torus AS the substrate's
physical surface, that would be a **reconstruction-mode** move
(modifying substrate apparatus), which `feedback_resolution_vs_reconstruction.md`
flags as empirically barred via `klein_bottle_restructure_price.md`'s
ℍ-QM exclusion. The current iteration stays strictly in
resolution mode.

---

## What this iteration step does NOT establish

- **No claim that the torus reading is forced.** The Z_6 mode
  lattice is substrate-forced (Mihailescu chain); the *torus
  geometric realization* of this lattice is a re-articulation
  (substrate-admitted), not a forcing of new content.
- **No quantitative new prediction.** The downstream observables
  (Ω_b, Ω_DM, Ω_Λ, mass hierarchy, etc.) are unchanged. The
  torus reading does not refine numerical values.
- **No new substrate apparatus.** Per the resolution discipline,
  this iteration does not add primitives.
- **No closure of the arc.** Subsequent iterations are needed
  to test the explanatory value of the torus vocabulary.

---

## Falsifiers for this iteration's hypothesis

1. **Gauge-factor identification falsifier.** If the toroidal Z_3
   does NOT correspond to SU(3) color and the poloidal Z_2 does
   NOT correspond to SU(2) weak, the geometric reading
   misalligns with the canonical gauge identification. Iteration
   2 step 1 verifies this against `gauge_sector_lovelock.md` and
   `gauge_dictionary.md` in detail.

2. **Klein-antipodal action falsifier.** If τ does NOT act as
   identity on poloidal and inversion on toroidal in the
   detailed apparatus, the clean direction-asymmetric reading
   fails.

3. **Boundary-mode-survival falsifier.** If the `{1, 5}` pair's
   "evenly spaced" character is not preserved under any
   substrate dynamics that we test against (e.g., if sync-cost
   minimization preferentially populates one of the pair), the
   surviving-evenly-spaced framing breaks down.

4. **Reconstruction smuggle falsifier.** If implementing the
   torus reading requires modifying ANY substrate apparatus
   beyond vocabulary, the resolution-mode claim is violated and
   the iteration enters reconstruction territory (which is
   empirically barred). This is the discipline-default falsifier:
   any tempted modification triggers re-check against
   `klein_bottle_restructure_price.md`.

5. **Vocabulary-closure falsifier.** If a substantive downstream
   claim made under the torus reading uses a property NOT in the
   substrate's enumerable vocabulary (per the 3×3 matter-sector
   matrix or its torus analog), the new vocabulary smuggles
   information and the resolution-mode discipline is violated.

---

## Plan for iteration 2

Three concrete steps to attempt in order:

**Step 1 — Verify gauge factor identifications structurally.**
Read `gauge_sector_lovelock.md` and `gauge_dictionary.md` to
confirm:
- The SU(3) color identification with the Z_3 toroidal sector
  rests on what specific substrate-forcing chain
- The SU(2) weak identification with the Z_2 poloidal sector
  similarly
- Whether the toroidal/poloidal distinction makes the SU(2)_L
  identification commitment (path δ' in
  `vocabulary_bridge_iteration_2_step_2.md`) sharper or weaker

**Step 2 — Test the surviving-evenly-spaced reading on downstream
derivations.** Specifically:
- The Ω_b = 1/19 closure (`baryon_fraction.md`) currently uses
  the gcd-with-6 filter algebraically. Does the torus reading
  add clarity to why φ(6) = 2 specifically gives the boundary?
- The Ω_b α/β closure (`omega_b_alpha_beta_closure.md`) uses
  w_+ = 13/14 at the Γ_0(6) cusp 1/2. Does the cusp
  correspondence have a clean toroidal-coordinate reading?
- The Mihailescu-strength forcing of `(q_2, q_3) = (2, 3)`
  makes the (q_2, q_3) = (poloidal, toroidal) assignment more
  robust. Verify that swapping (poloidal = q_3, toroidal = q_2)
  breaks something specific.

**Step 3 — Connect to PR #210's Collatz/Catalan framing.** PR
#210's `vocabulary-studies/collatz_minimal_chaos.md` reads
Collatz as minimal discrete chaos using framework primitives
(integers = q=1 boundary, {2, 3} incommensurability). The torus
reading and the Collatz reading share substrate primitives. A
joint check: does the toroidal/poloidal vocabulary clarify why
the {2, 3} incommensurability is load-bearing for Collatz's
single-cycle uniqueness?

If steps 1-3 produce useful clarifications, the arc continues.
If they all return "nothing new beyond canonical Z_6
apparatus," the arc closes as productive null at iteration 2,
with the torus vocabulary surviving only as a pedagogical /
documentation aid (substrate-admitted, not substrate-forced).

---

## Cross-links

- `klein_antipodal_z2_rep_pattern.md` — canonical Z_6 mode
  lattice apparatus; this iteration re-articulates its
  geometric reading.
- `baryon_fraction.md` L65-126 — the coprime-to-6 filter,
  boundary modes `{1, 5}`, Klein-singlet structure, baryon =
  Klein-singlet AND coprime-to-6 = ψ_+(1,5).
- `boundary_weight.md` L39 — Farey fractions at depth 6:
  `{1/6, 5/6}` = the same surviving pair in fractional form.
- `gauge_sector_lovelock.md` — gauge factor derivation; SU(3) ×
  SU(2) × U(1) from Z_6 = Z_2 × Z_3 center structure.
- `gauge_dictionary.md` — gauge group identifications and
  "identification commitments" status.
- `klein_bottle_derivation.md` Part II — torus structurally
  declined as substrate's physical surface; this iteration's
  torus reading is at the *mode-lattice* layer, NOT the
  physical surface.
- `mass_sector_closure.md` "Connection to the Catalan equation
  / Mihailescu's theorem" — substrate-forces (q_2, q_3) = (2, 3),
  the cycle lengths in the torus reading.
- `klein_bottle_restructure_price.md` — empirical decline of
  apparatus-extension; any temptation to make the torus reading
  reconstruction-mode triggers this gate.
- `vocabulary_bridge_iteration_2_step_2.md` — path δ' closure
  for substrate-chirality; provides the doublet/singlet
  kinematic split that the torus reading must respect.
- `basepoint_principle.md` — L vs R orientation as 7th verified
  instance; relevant for whether the torus reading admits a
  similar Z_2-torsor at the labeling layer (poloidal "side"
  labeling).
- `canonical_glossary.md` Section 8 — possibility-discipline
  distinctions; substrate-forced (the Z_6 lattice) vs
  substrate-admitted (the geometric torus realization).
- `feedback_resolution_vs_reconstruction.md` (memory) —
  methodology guard against reconstruction-mode drift.
- `vocabulary-studies/collatz_minimal_chaos.md` (PR #210) —
  adjacent Class 2 reading using same substrate primitives;
  iteration 2 step 3 cross-checks the toroidal/poloidal reading
  against the Collatz framing.
- `horn_branch_iteration_1.md`, `vocabulary_bridge_iteration_1.md`
  — comparable iteration-arc-opener structure and scope.

---

## One-line summary

Iteration 1 of the torus-branch arc frames the hypothesis that
the framework's already-canonical Z_6 mode lattice has a natural
torus T² geometric realization with **toroidal direction = q_3 =
3 cycle ↔ SU(3) color** and **poloidal direction = q_2 = 2 cycle
↔ SU(2) weak**, with the Klein-antipodal involution τ acting as
identity on poloidal and inversion on toroidal; the **surviving
evenly-spaced nodes** after the coprime-to-6 filter are the
`{1, 5} = φ(6) = 2` boundary modes (mirror-symmetric about 1/2,
geometrically flanking the toroidal-zero axis), which are
simultaneously (a) the matter-sector boundary modes
(`baryon_fraction.md`'s ψ_+(1,5) = the unique baryonic mode),
(b) the `{1/6, 5/6}` Farey fractions at the F_5/F_6 cosmological
boundary (`boundary_weight.md` L39), and (c) the torus-flanking
pair in this iteration's geometric reading — a three-way
confluence on one substrate object; this is **resolution-mode**
work (no new substrate apparatus; the torus reading
re-articulates the existing Z_6 lattice in geometric vocabulary
rather than proposing a new substrate surface, which would be
reconstruction-mode and is empirically barred per
`klein_bottle_restructure_price.md`); five falsifiers named, with
iteration 2 planning three concrete checks (gauge-factor
identification structural verification, downstream-derivation
clarity test on Ω_b and Ω_b α/β closure, cross-link with PR
#210's Collatz framing) whose three "no" outcomes would close
the arc as productive null with the torus vocabulary surviving
only as pedagogical/documentation aid (substrate-admitted, not
substrate-forced).
