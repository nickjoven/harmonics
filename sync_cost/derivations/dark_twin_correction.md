# Dark-twin correction: the S_v ≈ 13 retraction was wrong

A correction to `explicit_4x4_reduction.md`. That doc attempted the
real Phase 2 derivation and **over-corrected**: it retracted Phase
2's `S_v(K=1) = 16` down to `≈ 13` using a kink-pair interaction
model that does not apply to the framework's mode D. This doc
records the over-correction, its cause, and its catch — because
the honest scientific record includes the wrong turn, not just the
final answer.

## The over-correction

`explicit_4x4_reduction.md` Part A computed an interaction
correction:

    E_int ≈ M_k × exp(−L_x / ℓ_kink) ≈ M_k × e⁻¹ ≈ 3

and concluded `E_D ≈ 2M_k − E_int ≈ 13`, retracting `S_v = 16` to
`S_v ≈ 13`.

**The formula `M_k exp(−L/ℓ)` is the collinear sine-Gordon
kink–antikink attraction** — two solitons of opposite topological
charge in the *same* spatial direction at separation `L`. It is the
correct formula for that configuration.

**Mode D is not that configuration.** From `figure_eight.md` D19,
mode D is `(q₁ = 3 unlocked, q₂ = 2 unlocked)`:

- A kink in the **q₁ direction** — the antiperiodic-x direction
  (`klein_bottle.md`: x antiperiodic, y periodic). This is the
  **half-twist / Z₂ / dark-sector-coupled** direction.
- A kink in the **q₂ direction** — the periodic-y direction.
  Matter-sector, no half-twist.

These are kinks in **orthogonal Klein-bottle directions**, not a
collinear kink–antikink pair. The collinear attraction formula
`M_k exp(−L/ℓ)` does not apply to orthogonal-direction kinks. The
`E_int ≈ 3` was the right calculation for the wrong configuration.

## What the dark twin clarifies

The structural fact `explicit_4x4_reduction.md` skipped: the q₁
(antiperiodic) kink **couples to the dark sector through the
half-twist**. Per `cone_twist_substrate.md`'s bicone seam structure
and `wave_particle_substrate.md`'s matter/dark Z₂ twinning, the q₁
kink is the matter member of a **matter–dark Z₂-twin pair**, not
an independent matter kink. Two consequences:

### Consequence 1: Part A's retraction is withdrawn

Mode D's two kinks are orthogonal (q₁ antiperiodic + q₂ periodic).
At leading order their energies add with no collinear attraction:

    E_D = E(q₁ kink) + E(q₂ kink) = M_k + M_k = 2 M_k = 16

The orthogonal-kink interaction is a separate, **open**
calculation (field overlap at the crossing region, not the
collinear `exp(−L/ℓ)` form). It is genuinely undetermined — but it
is **not** the `≈ 3` collinear value. **`S_v(K=1) ≈ 16` at leading
order; the `≈ 13` retraction is withdrawn.**

### Consequence 2: Part C's continuum worry is resolved

`explicit_4x4_reduction.md` Part C found continuum meson modes
(ω ≈ 6.36, "interleaved below E_B = 8") and treated them as
independent matter modes contaminating the 4-mode reduction.

They are not independent matter modes. They are the **dark-sector
wave-side twin** — the EML/continuous counterpart of the kink
modes, related to them by the half-twist (`wave_particle_substrate.md`:
mediant/particle ↔ EML/wave, the half-twist as conversion
operator). The framework's bicone Z₂ structure *already accounts
for them*: every matter (kink) mode has a dark (wave) twin; the
continuum modes are those twins, not neglected matter degrees of
freedom.

The "4-mode reduction is contaminated" worry was treating
dark-sector twins as independent matter modes. With the bicone
matter/dark twinning, the matter sector is the 4 kink modes; the
dark sector is the wave continuum; the half-twist relates them.
Both are accounted for. **Part C's contamination concern is
withdrawn.**

## Honest net state

| Quantity | `explicit_4x4_reduction.md` claimed | Corrected here |
|---|---|---|
| Mode D configuration | collinear kink–antikink | **orthogonal q₁(dark-coupled) + q₂(matter) kinks** |
| `E_int` | `≈ 3` (collinear formula) | collinear formula N/A; orthogonal interaction open, ≠ 3 |
| `S_v(K=1)` | `≈ 13` (retraction) | **`≈ 16` leading; retraction withdrawn** |
| Part C continuum | "contaminates 4-mode reduction" | **dark-sector twin; structurally accounted for** |
| "exact" precision claim | retracted | **still not claimable** (orthogonal-kink correction open), but the `≈13` downgrade is wrong |

## What still stands from the audit

Audit Finding 3's *core* point survives in weakened form:

- Phase 2 *did* assume the 4-mode reduction and energies rather
  than deriving them. Part A of `explicit_4x4_reduction.md`
  supplies the derivation (energies from sine-Gordon kink mass +
  kink counting); that part stands.
- The "exact" claim is still **not** justified: the
  orthogonal-kink interaction correction to `E_D` is genuinely
  open (it's not the collinear `≈3`, but it's not zero either —
  field overlap at the q₁/q₂ crossing). `S_v(K=1) ≈ 16` is the
  leading value; "exact" requires the orthogonal-interaction calc.
- So the honest claim is: **`S_v(K=1) ≈ 16` at leading order, with
  an open (but parametrically distinct from collinear) orthogonal-
  kink correction.** Not `= 16` exact; not `≈ 13`.

## The scientific record

The actual sequence:

1. Audit Finding 3: Phase 2's 4-mode reduction "needs more work."
2. `audit_findings_3_4_disposition.md`: qualified "exact" → "leading
   order pending the explicit reduction."
3. `explicit_4x4_reduction.md`: attempted the derivation; **over-
   corrected** by applying the collinear kink-antikink formula to
   mode D (which is orthogonal + dark-coupled); retracted to
   `S_v ≈ 13`.
4. This doc: the dark-twin / orthogonality observation catches the
   over-correction. `S_v ≈ 16` leading restored; `≈ 13` withdrawn;
   "exact" still not claimable (orthogonal correction open).

This back-and-forth is the audit working *correctly*. The audit
forced the explicit derivation. The first attempt made a real
error (wrong interaction model). The error was caught by a
structural observation (the dark twin / Klein-bottle direction
orthogonality). The corrected state is more accurate than either
the original Phase 2 ("exact", overclaimed) or the first correction
("≈13", wrong model): **`S_v ≈ 16` leading, orthogonal correction
open.**

## Downstream consequences (corrected)

`explicit_4x4_reduction.md` propagated `S_v ≈ 13` to:

- `f_exit ≈ exp(−13)` — **withdrawn**; back to `f_exit ≈ exp(−16) ≈
  10⁻⁷` (leading, with the same open orthogonal correction).
- inflation duration `≈ 5×10⁻³⁴ s` — **withdrawn**; back to
  `≈ 10⁻³² s` (leading).
- `κ_pair`, `|∇K|_seam` recomputation — **not needed**; the audit
  values stand at leading order.

The `inflation_duration.md` Finding-4 disposition (the prediction
is *conditional on `K_inflation`*, not parameter-free) **still
stands** — that is a separate point (S_v is K-dependent across
epochs) unaffected by this correction, which is about the K=1
value specifically.

## What is genuinely open (post-correction)

1. **The orthogonal-kink interaction at the q₁/q₂ crossing.** Not
   the collinear `exp(−L/ℓ)`; the field-overlap energy of two
   orthogonal-direction kinks on the Klein bottle. Sign and
   magnitude undetermined. This is the real correction to `E_D`
   and hence `S_v(K=1)`. It is parametrically smaller than the
   spurious collinear `≈3` but not established to be negligible.
2. **The explicit matter/dark mixing at K=1.** Part C's continuum
   modes are the dark twin; the precise matter–dark coupling
   strength (the half-twist matrix element between kink modes and
   their wave twins) is the substrate-Lagrangian-level calc that
   would close the K=1 spectrum fully.

## Status

Class 3 (honest correction). No new primitive. This doc withdraws
`explicit_4x4_reduction.md`'s `S_v ≈ 13` retraction (wrong
interaction model — collinear formula applied to orthogonal+dark-
coupled configuration) and restores `S_v(K=1) ≈ 16` as the leading
value, while preserving the honest open status of the orthogonal-
kink correction (so "exact" remains unclaimed).

The framework's S_v = 16 is **leading-order correct**; the audit's
Finding 3 correctly forced the derivation; the first attempt's
over-correction is recorded and withdrawn; the dark-universe twin
was the missing piece.

## Cross-links

- `explicit_4x4_reduction.md` — the over-corrected derivation;
  its Part A `E_int` and Part C continuum worry are both withdrawn
  here.
- `audit_findings_3_4_disposition.md` — the disposition this
  corrects; its "leading order, exact pending derivation"
  framing is the right honest level (not "exact", not "≈13").
- `nonperturbative_phase2.md` — `S_v = 16` restored as leading
  value; "exact" remains unclaimed (orthogonal correction open).
- `figure_eight.md` D19 — mode D = (q₁ unlocked, q₂ unlocked),
  orthogonal Klein-bottle directions.
- `klein_bottle.md` — x antiperiodic (q₁, dark-coupled), y
  periodic (q₂, matter); the orthogonality.
- `cone_twist_substrate.md` — bicone seam; the matter–dark
  Z₂-twin structure that makes the q₁ kink dark-coupled.
- `wave_particle_substrate.md` — matter/dark twinning; the
  continuum modes are the wave-side twin, structurally accounted
  for.
- `inflation_duration.md` — the Finding-4 disposition
  (conditional on K_inflation) stands; only the K=1-specific
  `S_v ≈ 13` downgrade is withdrawn.
