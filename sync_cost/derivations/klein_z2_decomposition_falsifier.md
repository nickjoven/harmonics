# Klein-Z_2 sign-flip vs reflection decomposition — falsifier test

## Status

**Falsifier outcome: PARTIALLY PASSED.** The Klein-Z_2
identification `f(x+L_x, y) = −f(x, L_y−y)` admits a clean
mathematical decomposition into independent sign-flip (S) and
reflection (R) actions. The framework's existing
complex-amplitude apparatus uses S and R *coupled together*
(forced by the spinor bundle structure that gives `J² = −I`),
but the operations themselves are mathematically independent.

The framework's existing apparatus therefore **carries one
chirality** (the spinor-bundle-aligned one) and the **other
chirality lives on a different bundle** that the framework
hasn't explicitly invoked.

This refines the prior audit verdict from
`axial_trajectory_conservation_audit.md`:

- **Previous**: APPARATUS INSUFFICIENT (chirality requires
  structural extension)
- **Refined**: APPARATUS ASYMMETRICALLY SUFFICIENT (carries one
  chirality natively; the other chirality requires either a
  re-articulation of the existing structure into S-acting and
  R-acting components separately, or an extension introducing
  additional bundles)

For some sectors (neutrinos, chirally asymmetric by observation)
this asymmetric sufficiency may be the *correct* substrate
output. For other sectors (charged leptons, chirally symmetric
by observation) the apparatus is genuinely insufficient.

Class: foundational rigor check (Class 3, falsifier test for
prior audit).

---

## The mathematical decomposition

### Setup

Klein bottle as quotient `K = R² / ~`:

    (x, y) ~ (x + L_x, L_y − y)        [twisted x identification]
    (x, y) ~ (x, y + L_y)              [periodic y identification]

For a section `f` of a bundle over `K`, the identification on `f`
depends on the bundle's structure. Two independent operations
appear in the x-identification:

- **R (reflection)**: coordinate action `y → L_y − y`. Acts on
  the base manifold.
- **S (sign flip)**: fiber action `value → −value`. Acts on the
  bundle fiber.

### The bundle determines whether S appears

The bundle structure forces the choice:

| Bundle | x-identification | What's carried |
|---|---|---|
| Trivial scalar bundle | `f(x+L_x, y) = f(x, L_y−y)` | R only (no S) |
| Spinor bundle, sign-twisted spin structure | `ψ(x+L_x, y) = −ψ(x, L_y−y)` | S × R (Klein bottle) |
| Spinor bundle, untwisted spin structure | `ψ(x+L_x, y) = +ψ(x, L_y−y)` | R only |
| Real line bundle with non-trivial w_1 | `g(x+L_x, y) = −g(x, y)` | S only (no R) |
| Real line bundle with trivial w_1 | `g(x+L_x, y) = +g(x, y)` | neither |

S and R are independent operations. Different bundles realize
different combinations. The Klein bottle's primary topological
content lives on the spinor bundle with the sign-twisted spin
structure, which gives `S × R` together.

### Why the framework uses S × R

`complex_amplitude_uniqueness.md` derives `J² = −I` from the
single antiperiodic cycle's spinor-like sign flip. This requires
the bundle to carry the S action (`f → −f` on full x-traversal).
The R action is geometric (coordinates change under traversal);
S is the framework's content (amplitudes change sign).

The framework's complex amplitudes therefore live on the
spinor-twisted bundle where S and R appear together as the Klein
bottle's "primary" identification.

---

## What this means for the audit's chirality question

### Chirality as the R-action

Geometric chirality (the cylinder-level ± in the
`string → cylinder → cone` progression) is the **R-action's
eigenvalue**:

- R-symmetric sections: `f(x, L_y−y) = +f(x, y)` — "even
  chirality"
- R-antisymmetric sections: `f(x, L_y−y) = −f(x, y)` — "odd
  chirality"

These are well-defined operations on sections of any bundle over
`K`. The framework's R-action is the y → L_y−y reflection — it
exists in the apparatus, just not named as a chirality axis.

### Why the existing apparatus carries one chirality only

For a complex amplitude `ψ` on the spinor bundle with
identification `ψ(x+L_x, y) = −ψ(x, L_y−y)`, decomposing into
R-eigenstates:

- R-symmetric component `ψ_+`: would satisfy `ψ_+(x+L_x, y) =
  −ψ_+(x, y)` (pure S on full traversal, since R acts trivially
  on ψ_+)
- R-antisymmetric component `ψ_−`: would satisfy
  `ψ_−(x+L_x, y) = +ψ_−(x, y)` (S and R both flip sign, product
  is +1)

So under the spinor-bundle's S × R identification:

- ψ_+ (R-even, "right-handed") is *antiperiodic* in x with no R
  action (lives on a Möbius-like bundle)
- ψ_− (R-odd, "left-handed") is *periodic* in x (lives on a
  cylinder-like trivial bundle)

These are sections of *different* line bundles, not just
different eigenstates of the same bundle. The framework's
existing apparatus carries amplitudes on the spinor-bundle, which
mixes both — but the two chirality components live on different
sub-bundles.

**The "one chirality" claim refined**: the spinor bundle is the
direct sum of the R-even sub-bundle (antiperiodic Möbius-like)
and the R-odd sub-bundle (periodic cylinder-like). Both
chiralities are *present* in the spinor bundle, but each in a
different sub-structure.

This is actually **more favorable than the prior audit
suggested**.

### What this means for chirality-distinguishing dynamics

For regime-change Class B/C work that needs chirality-distinguishing
dissipation, the framework's apparatus *can* host it if substrate
dynamics is formulated in terms of R-eigenstate projections of
the existing complex amplitude:

- Define `ψ_+` = R-symmetric projection of ψ
- Define `ψ_−` = R-antisymmetric projection of ψ
- ψ_+ lives on antiperiodic Möbius-like sub-bundle
- ψ_− lives on periodic cylinder-like sub-bundle
- Sync-cost dynamics can have different couplings on `ψ_+` and
  `ψ_−` — chirality-distinguishing dissipation is hostable

This requires **no structural extension** of the framework — only
explicit naming of the R-eigenstate decomposition already present
in the spinor bundle.

---

## Revised verdict

### What the falsifier showed

The decomposition `Klein-Z_2 = S × R` exists mathematically and
is structurally meaningful. The framework's complex amplitudes
live on the spinor bundle, which decomposes as a direct sum of
R-even and R-odd sub-bundles. Both chiralities are present in
the existing apparatus; they live on different sub-bundles.

### What this changes from the prior audit

- **Previous**: "APPARATUS INSUFFICIENT — chirality requires
  extension (V_4 promotion, cascade-attached Z_2, or klein-bottle
  restructure)"
- **Revised**: "APPARATUS CARRIES BOTH CHIRALITIES IMPLICITLY
  via the R-eigenstate decomposition of the spinor bundle. Naming
  the decomposition explicitly is a re-articulation, not an
  extension."

### What this means for Task 105 (horn-branch)

**Unblocked.** Horn-branch dissipation work can proceed by:

1. Decomposing the substrate's complex amplitude field into
   R-even (ψ_+) and R-odd (ψ_−) components.
2. Allowing horn-branch dissipation profiles to depend on the
   R-eigenstate (chirality).
3. Cross-checking that this chirality-distinguishing dissipation
   closes Class B (m_μ at 37%) and Class C (PMNS θ_12 at 10%)
   *without* breaking the moat (m_τ at 0.9%, θ_23 at <1%).

The dependency that previously blocked 105 (Task 110 — chirality
extension arc) becomes **conditional**: if the R-eigenstate
re-articulation suffices, no extension iteration arc is needed.
If horn-branch attempts using this re-articulation fail to close
Class B/C, the extension paths from Task 110 become live.

### What this means for Task 110 (chirality extension)

**Conditionally cancelled.** The three extension paths (V_4
promotion, cascade-attached Z_2, klein-bottle second cycle) are
not needed *if* the R-eigenstate re-articulation suffices. They
remain on standby if horn-branch attempts demonstrate that the
re-articulation is genuinely insufficient.

This is a productive falsifier outcome: it identifies that the
apparent insufficiency was a vocabulary gap, not a structural
gap. The framework has the structure; it just hasn't named it.

---

## Remaining caveats

### Spin vs chirality conflation

The R-eigenstate decomposition gives chirality, but spin in the
framework comes from the same Klein-Z_2 via the S action on the
spinor bundle. R-even and R-odd sub-bundles both carry S
(spin) — they differ only in chirality.

This means in the revised apparatus:
- Spin ± = sign of fermion under S
- Chirality ± = R-eigenvalue (R-even vs R-odd sub-bundle)

These are independent (S is on fibers, R is on base) but they
share the *substrate generator* (the Klein-Z_2). Whether substrate
dynamics can vary them independently depends on whether the
sync-cost machinery can couple to S and R separately.

This is a *coupling question*, not a structural one: does
sync-cost see ψ_+ and ψ_− differently, or does it see only the
S × R combined identification? Answering it requires writing
out sync-cost in R-eigenstate basis explicitly and checking
whether the chirality projection produces distinct dynamics.

This is the *operational* test that horn-branch work would
perform. The falsifier test answered the *structural* question
(decomposition exists); the operational question is
hostable-but-untested.

### Arrow of time vs chirality

`klein_bottle.md` L274 identifies the antiperiodic axis as the
arrow-of-time carrier. Under the S × R decomposition, arrow of
time is the S action specifically — the sign flip on traversal.
Chirality is R (the reflection). These are now distinguished:
arrow of time is fiber-side, chirality is base-side.

This is a clean separation. The audit's prior conflation of
chirality with arrow of time is dissolved by the decomposition.

### Cascade-direction question unchanged

The third ± axis (scale direction / apex-ward) is not addressed
by the S × R decomposition. Cascade depth remains a scalar index
without ± structure. If horn-branch work requires scale-direction
± explicitly, additional apparatus is still needed.

For Class B/C, the chirality axis is the more important
precondition (matches the SM's chirality-distinguishing running);
scale-direction may be less critical. To be confirmed by
horn-branch attempts.

---

## Implications for the next-leg work

### Task 105 (horn-branch) — unblocked conditionally

Proceed with horn-branch dissipation work using the R-eigenstate
decomposition. Track whether chirality-distinguishing dissipation
closes Class B and C residuals.

### Task 107 (audit) — verdict revised

The audit's "APPARATUS INSUFFICIENT" verdict is **revised to
"APPARATUS HAS DECOMPOSITION IMPLICIT, NAMING REQUIRED."** The
audit doc itself stands as historical record; this falsifier test
serves as the revision.

### Task 110 (chirality extension) — conditionally cancelled

Held in standby. If horn-branch attempts using the R-eigenstate
decomposition fail to close Class B and C, Task 110 becomes
live with the three extension paths previously named.

### Task 106 (torus-branch) — unaffected

Still independent, can proceed.

---

## Falsifier-of-the-falsifier

The decomposition test could itself be wrong if:

- **The R-eigenstate decomposition doesn't preserve sync-cost
  dynamics.** If projecting onto ψ_+ and ψ_− components breaks
  the sync-cost machinery's structure (e.g., couples them in a
  way that prevents independent dissipation), the decomposition
  exists topologically but doesn't host independent chirality
  dynamics. Operational test required.
- **The R action isn't well-defined on the framework's complex
  amplitudes.** If the framework's amplitude field doesn't admit
  a y-reflection symmetry (e.g., because its base structure
  doesn't have a global y-axis), the R-eigenstate decomposition
  isn't physically meaningful. Klein-bottle topology forces a
  global y-axis (one of the two cycles), so this is unlikely to
  fail — but should be confirmed.
- **The framework's "complex amplitude" is more constrained than
  the generic spinor bundle.** If the framework's apparatus
  selects only the R-even or only the R-odd sub-bundle (one
  chirality, not both), then the falsifier's "both chiralities
  carried implicitly" claim is wrong. Need to check whether the
  framework's apparatus has implicit chirality selection.

The third caveat is the most likely to be a real issue. If the
framework's substrate dynamics naturally produces only one
chirality of amplitude (because of, e.g., a sign convention in
the field equation or a discrete-step preference in the cascade),
then the R-eigenstate decomposition exists topologically but
substrate dynamics only populates one side.

**This is the next test to run before proceeding to horn-branch
work**: confirm that the substrate's complex-amplitude field
admits both R-eigenstate components, not just one.

---

## Cross-links

- `axial_trajectory_conservation_audit.md` — prior audit verdict
  (revised by this test).
- `klein_bottle.md` — Klein bottle x-identification, y-axis
  structure.
- `complex_amplitude_uniqueness.md` — spinor bundle / single
  antiperiodic cycle → ℂ derivation.
- `mass_sector_closure.md` — `k_lepton = q_3²` chirality
  invocation.
- `framework_lagrangian.py` — sync-cost dynamics that would need
  to couple to R-eigenstates differently to host chirality-
  distinguishing dissipation.

---

## One-line summary

The Klein-Z_2 identification `f(x+L_x, y) = −f(x, L_y−y)` admits
a clean mathematical decomposition into sign-flip (S, fiber
action) and reflection (R, base coordinate action) that are
independent — S × R appears together specifically because the
framework's complex amplitudes live on the spinor bundle, but the
spinor bundle itself is the direct sum of R-even and R-odd
sub-bundles, meaning **both chiralities are present in the
existing apparatus** via the R-eigenstate decomposition; this
revises the prior audit's "APPARATUS INSUFFICIENT" to "APPARATUS
HAS THE DECOMPOSITION IMPLICIT, NAMING REQUIRED" — Task 105
horn-branch work is conditionally unblocked (proceed with
R-eigenstate-projected dissipation; if it doesn't close Class B
and C, extension paths re-emerge), Task 110 chirality extension
is conditionally cancelled (held in standby), Task 107 audit
verdict is revised in-place by this falsifier test, and the
remaining test before proceeding is whether the framework's
substrate dynamics actually populates both R-eigenstate
components or only one — a test that horn-branch work itself
would perform operationally.
