# Torus-branch iteration 2 step 2 — downstream clarity + swap robustness

## Status

**Verdict: PASSES with substantive clarification.** Step 2 tests
whether the torus reading clarifies downstream derivations on
Ω_b and Ω_b α/β closures, and whether the toroidal/poloidal
assignment is convention-only.

Three sub-tests:

- **(a) Ω_b closure clarity**: the φ(6) = 2 coprime-to-6 count
  becomes geometrically natural under the torus reading. The
  formula φ(pq) = (p-1)(q-1) = (q_2-1)(q_3-1) = 2 maps to
  "interior torus modes off both gauge-center axes." Substantive
  clarification.

- **(b) Ω_b α/β cusp identification clarity**: the two non-trivial
  cusps of X_0(6) at 1/2 and 1/3 correspond geometrically to
  poloidal-direction degeneration and toroidal-direction
  degeneration respectively. w_+ ↔ cusp 1/2 ↔ poloidal cusp.
  The torus reading unifies Z_6 = Z_2 × Z_3 algebra + X_0(6)
  cusp structure + Klein-antipodal action + boundary mode count
  in a single geometric picture.

- **(c) Assignment robustness**: swapping poloidal/toroidal
  labels (poloidal = q_3, toroidal = q_2) preserves all
  substrate-forced content (SU(3) ↔ q_3 unchanged, cusp 1/2 ↔
  q_2-rep unchanged). Only the geometric labels swap; standard
  torus-geometry convention (toroidal = longer cycle) would be
  violated, but that's a labeling violation, not a substrate
  violation. **Assignment is convention-only.**

This is **resolution-mode** clarification — the torus reading
adds a unifying geometric picture without modifying any
derivation. Per `canonical_glossary.md` Section 8, the torus
reading is **substrate-admitted** (consistent with the
apparatus) and **does not add substrate-forced content** beyond
what's already in Z_6 + X_0(6) + Klein-antipodal apparatus. The
clarification is real but vocabulary-level.

Importance for `primitives_vs_addresses_candidate.md`: this step
confirms more apparatus is **layer-invariant** — Γ_0(6)
preservation, X_0(6) cusp structure, w_+ ↔ cusp 1/2
identification are all number-theoretic + group-theoretic facts
that recur at any layer. The specific value w_+ = 13/14 (and
its mapping to Ω_b ≈ 0.0493) is **layer-specific**.

Class: foundational rigor check (Class 3, iteration step
verifying clarity + robustness).

---

## Sub-test (a): Ω_b closure clarity

### Existing apparatus (`baryon_fraction.md` L65-126)

The baryon-coupling derivation uses:

- 6 modes of Z_6 = {0, 1, 2, 3, 4, 5}
- Coprime-to-6 filter: gcd(k, 6) = 1 gives {1, 5}, count = **φ(6) = 2**
- Klein-singlet × coprime-to-6 = ψ_+(1, 5) = unique baryonic mode
- **Ω_b = 1/19**

The algebraic step "**φ(6) = 2**" is the count of coprime-to-6
modes. Why 2 specifically? Per Euler's totient formula for
n = pq with p, q prime:

    φ(pq) = (p−1)(q−1) = (q_2−1)(q_3−1) = 1 × 2 = 2

### Torus reading clarification

Under the torus reading (Z_6 = Z_2 × Z_3 = poloidal × toroidal):

- **Poloidal direction** has q_2 = 2 positions: {0, 1}
- **Toroidal direction** has q_3 = 3 positions: {0, 1, 2}
- **k coprime to 6** ⟺ k ≢ 0 mod 2 AND k ≢ 0 mod 3
- Geometrically: k is **off the poloidal-zero axis AND off the
  toroidal-zero axis**

The coprime-to-6 condition becomes:

    "interior torus point — off both gauge-center axes"

Count:

- (q_2 − 1) non-zero poloidal positions × (q_3 − 1) non-zero
  toroidal positions = (q_2 − 1)(q_3 − 1) = **φ(6) = 2**

The two interior points are:
- k = 1: (poloidal = 1, toroidal = 1) → off-poloidal-zero, off-toroidal-zero
- k = 5: (poloidal = 1, toroidal = 2) → off-poloidal-zero, off-toroidal-zero

Both at poloidal = 1 (the only non-zero poloidal position), and
at the two non-zero toroidal positions {1, 2}.

### Clarification value

The torus reading gives Euler's totient formula a clean
geometric meaning:

- Algebraic: φ(6) = (2−1)(3−1) = 2 (Euler totient for coprime
  product)
- Geometric: 2 = "1 non-zero poloidal × 2 non-zero toroidal =
  count of interior torus points off both axes"

The geometric reading makes the "boundary mode" terminology
(`baryon_fraction.md`'s "boundary modes {1, 5}") *literally
geometric* — these are the modes at the **boundary between
gauge sectors**, off both gauge-center axes, located in the
torus interior. The Klein-singlet filter (Z_2-invariant)
then selects ψ_+(1, 5) as the symmetric combination.

**Verdict (a)**: PASSES with substantive clarification. The
torus reading makes the φ(6) = 2 boundary mode count
geometrically natural rather than algebraically arbitrary.

---

## Sub-test (b): Ω_b α/β cusp identification clarity

### Existing apparatus

`psl2z_subgroup_phase_b.md` L95-141 establishes:

> "**w_+ inhabits cusp 1/2 independently** [of the EM-MOND
> reading]:
> 1. w_+ is the partial-locking weight of the sym ψ_+(1, 5)
>    boundary mode
> 2. Trivial Klein Z_2 rep is the q_2-equivariant ground state
> 3. Hecke T_2 cusp action sends trivial-rep modes to the q_2-cusp
>    of X_0(6) — cusp 1/2
> 4. Conclusion: w_+ ↔ cusp 1/2 of Γ_0(6)"

The cusps of X_0(6) (where X_0(N) is the modular curve at level
N) are parameterized by Γ_0(N)-orbits on ℙ¹(ℚ). For N = 6,
there are four cusps: ∞ (or 1/0), 0 (or 1/6), 1/2, 1/3.

- Cusp ∞ (1/0): trivial / "level 1" cusp
- Cusp 0 (or 1/6): "level 6" cusp (both prime factors)
- Cusp 1/2: q_2-active (denominator carries factor 2)
- Cusp 1/3: q_3-active (denominator carries factor 3)

### Torus reading clarification

Under the torus reading:

- **Cusp 1/2** ↔ q_2-active ↔ **poloidal direction's degeneration**
- **Cusp 1/3** ↔ q_3-active ↔ **toroidal direction's degeneration**
- Cusp ∞ and cusp 0 are the "non-direction" cusps (trivial and
  composite)

The two non-trivial direction-cusps of X_0(6) correspond
*directly* to the two torus directions:

| Cusp of X_0(6) | Direction | Substrate identification |
|---|---|---|
| 1/2 | poloidal | q_2-active (Z_2 reduction) |
| 1/3 | toroidal | q_3-active (Z_3 reduction) |
| ∞ | trivial | level 1 (no reduction) |
| 0 | composite | level 6 (both reductions) |

This is a **geometric unification** of previously-separate
framings:

1. **Z_6 = Z_2 × Z_3 algebra** (CRT decomposition)
2. **X_0(6) cusp structure** (modular forms theory)
3. **Klein-antipodal action geometric reading** (identity on
   poloidal, inversion on toroidal — `torus_branch_iteration_1.md`)
4. **Coprime-to-6 boundary count** = interior torus points

All four are unified by the toroidal/poloidal vocabulary. The
torus reading provides a single geometric picture in which:

- Z_2 × Z_3 = poloidal × toroidal cycles
- {1/2, 1/3} cusps = direction-degenerations
- Klein-antipodal = poloidal-identity × toroidal-inversion
- {1, 5} = interior modes off both gauge-center axes

### Clarification value

This is the strongest case for substantive clarification value.
The torus reading does not introduce new apparatus, but it
**unifies four previously-separate framings** in a single
geometric picture. That's a real vocabulary-level contribution
to the framework's exposition.

**Verdict (b)**: PASSES with strong substantive clarification.

---

## Sub-test (c): Assignment robustness under swap

### What "swap" means

Original assignment (per `torus_branch_iteration_1.md`):
- Poloidal (shorter cycle, period q_2 = 2) ↔ Z_2 ↔ SU(2)
- Toroidal (longer cycle, period q_3 = 3) ↔ Z_3 ↔ SU(3)

Swapped assignment:
- Poloidal (now longer cycle, period q_3 = 3) ↔ Z_3 ↔ SU(3)
- Toroidal (now shorter cycle, period q_2 = 2) ↔ Z_2 ↔ SU(2)

### What's substrate-forced (invariant under swap)

The substrate-forced content:

- **Z_2 substrate origin**: GCD mod 2 from q_2 = 2 — *unchanged*
- **Z_3 substrate origin**: GCD mod 3 from q_3 = 3 — *unchanged*
- **SU(2) ↔ q_2**: Cartan + minimum-rank for Z_2 center —
  *unchanged*
- **SU(3) ↔ q_3**: Cartan + minimum-rank for Z_3 center —
  *unchanged*
- **Cusp 1/2 ↔ q_2-rep**: standard modular-forms fact —
  *unchanged*
- **Cusp 1/3 ↔ q_3-rep**: standard modular-forms fact —
  *unchanged*
- **w_+ ↔ cusp 1/2**: trivial Klein Z_2 rep argument —
  *unchanged*
- **φ(6) = 2 boundary modes {1, 5}**: number-theoretic fact —
  *unchanged*

All substrate-forced identifications and downstream derivations
are *invariant under swap*. Nothing breaks.

### What changes under swap

The only changes are:

- The geometric label "toroidal" is applied to the q_2 cycle
  rather than the q_3 cycle
- The geometric label "poloidal" is applied to the q_3 cycle
  rather than the q_2 cycle
- **Standard torus geometry convention** (toroidal = longer
  cycle around the donut hole) is violated

The substrate doesn't care about the violation. Standard torus
geometry conventions exist for mathematical exposition; they
have no substrate-internal forcing power.

### Verdict (c)

**Assignment is convention-only**, exactly parallel to:

- L vs R orientation labeling (`vocabulary_bridge_iteration_2_step_2.md`):
  substrate forces the doublet/singlet split; labeling is
  observation-fixed
- Toroidal/poloidal labeling: substrate forces the q_2 × q_3
  structure; "toroidal" = "longer cycle" is geometric
  convention

The torus reading's substrate-forced content survives swap; the
convention can be applied either way.

**Verdict (c)**: PASSES. Assignment is purely conventional.

---

## Combined verdict

All three sub-tests pass. The torus reading:

- **(a) Clarifies** φ(6) = 2 as interior torus modes count
- **(b) Unifies** Z_6 algebra + X_0(6) cusp structure +
  Klein-antipodal action + boundary mode count in a single
  geometric picture; identifies the two non-trivial X_0(6) cusps
  with the two torus directions
- **(c) Survives swap**: substrate-forced content invariant;
  toroidal/poloidal labels are convention

### Importance for primitives-vs-addresses partition

This step provides a second substantive test of the
`primitives_vs_addresses_candidate.md`. The apparatus surfaced
in this step is all **layer-invariant**:

- Γ_0(6) substrate preservation (Mihailescu + CRT + Γ_0(N)
  intersection)
- X_0(6) cusp structure (modular forms theory)
- Cusp 1/2 ↔ q_2-rep identification (Hecke T_2 action)
- w_+ ↔ cusp 1/2 (trivial Klein Z_2 rep argument)
- φ(6) = (q_2 − 1)(q_3 − 1) = 2 boundary count (Euler totient)

All are number-theoretic + group-theoretic + modular-forms
facts that recur at any layer. The specific value w_+ = 13/14
(and its mapping to observed Ω_b ≈ 0.0493) is layer-specific —
it depends on which rational representative our layer picks
within cusp 1/2's orbit.

Combined with step 1's finding that SU(3) × SU(2) gauge sector
is layer-invariant, **the framework's cosmological closure
machinery is mostly layer-invariant; only the specific
boundary-weight value is a layer-address**.

This is consistent with the recursive Kuramoto reading: a
different layer would have its own boundary weight w_+
inhabiting its own cusp 1/2 (or analog), but the cusp
identification and the φ(6) = 2 boundary count would be the
same.

---

## What this step DOES establish

1. **The torus reading clarifies Ω_b's φ(6) = 2 count
   geometrically** without modifying the derivation.

2. **The torus reading unifies four previously-separate framings**
   (Z_6 algebra + X_0(6) cusps + Klein-antipodal action +
   boundary mode count) in a single geometric picture.

3. **The toroidal/poloidal assignment is convention-only**,
   parallel to L vs R labeling.

4. **More apparatus is confirmed layer-invariant** per the
   primitives-vs-addresses candidate: Γ_0(6) preservation,
   X_0(6) cusp structure, w_+ ↔ cusp 1/2 identification, φ(6)
   boundary count.

5. **Resolution-mode discipline preserved**: no apparatus
   modification; the torus reading adds vocabulary, not
   structure.

---

## What this step does NOT establish

- **Whether the torus reading provides PREDICTIONS** that the
  canonical Z_6 apparatus doesn't. Step 3 of iteration 2 (cross
  with PR #210's Collatz framing) might surface predictions; or
  the arc may close as productive null with vocabulary
  clarification only.

- **Whether the specific value w_+ = 13/14** has a clean
  torus-coordinate reading. The geometric direction-identification
  works; the specific orbit representative within cusp 1/2 is
  layer-specific per the primitives-vs-addresses candidate and
  doesn't have a torus-geometric forcing argument.

- **Sealing of the primitives-vs-addresses candidate.** Two
  substantive tests (steps 1 and 2) have surfaced
  layer-invariant content; sealing per the candidate's four
  criteria still requires (a) demonstrating the layer-invariant
  set closes under all derivations, (b) demonstrating layer-
  specific set closure under substitution, (c) at least one
  additional substantive instance beyond the two surfaced here,
  and (d) compatibility with empirical constraints.

---

## Falsifiers

1. **The X_0(6) cusp identification depends on layer-specific
   input.** If a closer reading of `psl2z_subgroup_phase_b.md`
   reveals the cusp 1/2 ↔ q_2-rep argument needs empirical input
   we've missed, the "layer-invariant" credit weakens.

2. **The (q_2 − 1)(q_3 − 1) factorization isn't substrate-internal.**
   The formula is standard Euler totient; if the (q_2 − 1) and
   (q_3 − 1) factors don't decompose naturally in the framework's
   substrate apparatus, the geometric clarification is just
   pattern-matching number theory onto torus pictures.

3. **The Γ_0(6) substrate preservation is itself observation-conditional.**
   If `psl2z_subgroup_phase_b.md`'s B1 argument has hidden
   empirical inputs (Hecke level-6 preservation in observed
   physics), the framework's modular structure on the substrate
   is layer-specific rather than layer-invariant.

---

## Plan for iteration 2 step 3

Original step 3 (`torus_branch_iteration_1.md`): "Cross-check
against PR #210's Collatz framing — does the toroidal/poloidal
vocabulary clarify why the {2, 3} incommensurability is
load-bearing for Collatz's single-cycle uniqueness?"

This is the last open sub-step in iteration 2's plan. If step 3
returns "the torus vocabulary doesn't add new clarity beyond
substrate-internal modular structure," iteration 2 closes with
the torus reading sealed as a **substantive vocabulary
clarification** (Class 2 with unifying-picture value) but not as
a new substrate-derivation. If step 3 finds substantive content
in the Collatz cross-reference, iteration 2 continues.

---

## Cross-links

- `torus_branch_iteration_1.md` — hypothesis frame; this step
  tests its downstream-clarity prediction.
- `torus_branch_iteration_2_step_1.md` — gauge identifications
  verified; companion verification for step 2's downstream test.
- `baryon_fraction.md` L65-126 — Ω_b derivation; φ(6) = 2
  boundary count clarified by step 2 sub-test (a).
- `omega_b_alpha_beta_closure.md` — Ω_b α/β closure; w_+ = 13/14
  at cusp 1/2; downstream of step 2 sub-test (b).
- `psl2z_subgroup_phase_b.md` L95-141 — w_+ ↔ cusp 1/2
  independent argument; verified consistent with torus reading.
- `klein_antipodal_z2_rep_pattern.md` — Z_6 mode lattice
  canonical apparatus.
- `mass_sector_closure.md` "Connection to the Catalan equation
  / Mihailescu's theorem" — substrate-forces (q_2, q_3) = (2,
  3), grounding the entire chain at Mihailescu-strength.
- `primitives_vs_addresses_candidate.md` — first methodology
  candidate; this step provides the second substantive test
  (Γ_0(6) cusp structure confirmed layer-invariant).
- `vocabulary_bridge_iteration_2_step_2.md` — L vs R basepoint
  instance; structurally parallel to the toroidal/poloidal
  labeling-convention finding here.
- `feedback_resolution_vs_reconstruction.md` (memory) —
  resolution-mode discipline preserved throughout this step.

---

## One-line summary

Iteration 2 step 2 tests three sub-claims of the torus-reading
hypothesis — (a) Ω_b closure φ(6) = 2 boundary count, (b) Ω_b
α/β closure cusp identification, (c) assignment robustness
under poloidal/toroidal swap — and finds the torus reading
PASSES with substantive clarification: (a) the φ(6) =
(q_2 − 1)(q_3 − 1) = 2 boundary count maps geometrically to
"interior torus modes off both gauge-center axes," (b) the two
non-trivial X_0(6) cusps {1/2, 1/3} correspond *directly* to
the two torus directions (poloidal-degeneration vs
toroidal-degeneration), unifying Z_6 = Z_2 × Z_3 algebra +
X_0(6) cusp structure + Klein-antipodal action +
coprime-to-6 boundary count in a single geometric picture,
and (c) the assignment is convention-only — substrate-forced
content (SU(3) ↔ q_3, cusp 1/2 ↔ q_2-rep, w_+ ↔ cusp 1/2,
φ(6) = 2) is invariant under swap, only the "toroidal" =
"longer cycle" geometric convention is conventionally
violated; the torus reading is **substantive vocabulary
clarification** (Class 2 with unifying-picture value), not
new substrate-derivation; resolution-mode discipline preserved;
provides the **second substantive test of the
primitives-vs-addresses candidate** (commit 352359c) with
Γ_0(6) preservation + X_0(6) cusp structure + cusp 1/2 ↔ q_2-rep
identification + φ(6) boundary count all confirmed
**layer-invariant** — combined with step 1's gauge sector
result, the framework's cosmological closure machinery is
mostly layer-invariant with only the specific value w_+ = 13/14
being layer-specific; three falsifiers named; iteration 2 step 3
(Collatz cross-reference) is the last open sub-step before
iteration 2 closes with the torus reading sealed as a
substantive vocabulary clarification (if step 3 also adds no
new substrate-derivation content).
