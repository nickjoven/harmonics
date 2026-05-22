# Complex-amplitude uniqueness (ℝ/ℂ/ℍ from antiperiodic-cycle count)

## Status

**Forcing argument articulated** for the question the EPR/Bell
assembly (`epr_bell_assembly_theorem.md`) flagged as its bright
line and left open: *is the complex amplitude field ℂ forced, or
merely consistent — i.e., why not real (ℝ) or quaternionic (ℍ)
quantum mechanics?* The corpus had `J²=−I` from the half-twist
(`figure_eight.md`, `substrate_determinism.md:67-71`) but never
asked whether that complex structure is **unique**.

This doc supplies the uniqueness argument and classifies it
honestly. It introduces no new primitive: it reads the corrected
single-antiperiodic-direction topology of `figure_eight.md`
(L18-24, L169-233) through the standard Frobenius-Schur /
commutant trichotomy.

**Classification.** Class-5 forcing **on the fermion/spinor
sector**, contingent on the Klein-bottle commitment (itself
derived: mediant + Z₂ filter → `klein_bottle.md`). **One flagged
Class-4 extension**: sector-universality (extending ℂ to the
boson sector, where `J²=+I`). Not a Basepoint-decline — the
topology forces the answer.

---

## Background — the trichotomy

A quantum theory's amplitude field is one of three division
algebras over ℝ: real (ℝ), complex (ℂ), or quaternionic (ℍ).
The standard discriminator is the **Frobenius-Schur indicator**
`ν(ρ) = (1/|G|) Σ_g χ(g²)` of the representation `ρ` the symmetry
group carries on the amplitude space, equivalently the
endomorphism algebra (commutant) `End(ρ)` by Schur's lemma:

| `ν` | `End(ρ)` | Type | Amplitude field | Invariant complex structures `J` (`J²=−I`) |
|---|---|---|---|---|
| +1 | ℝ | real | ℝ | none |
| 0 | ℂ | complex | ℂ | exactly one (up to sign) |
| −1 | ℍ | quaternionic | ℍ | a 2-sphere (quaternion triple `i,j,k`) |

The number of *independent anticommuting* complex structures is
0, 1, or 3 in the three cases — this integer is the object the
substrate must pin.

(The ℝ/ℂ/ℍ-QM trichotomy is Stueckelberg / Adler's; ℝ-QM was
experimentally excluded by Renou et al., *Nature* 2021, via a
network Bell test. It is distinct from the Wigner-Dyson "threefold
way" of antiunitary symmetries, which classifies Hamiltonian
ensembles *within* complex QM; this doc concerns the scalar field
of the Hilbert space, not the Dyson class.)

---

## The theorem

**Theorem (complex-amplitude uniqueness).** On the substrate's
amplitude space, the number of independent anticommuting complex
structures `J` (`J²=−I`) equals the number of independent
antiperiodic (orientation-reversing) cycles of the substrate
manifold. For the Klein bottle this number is **exactly one**.
Therefore the substrate's amplitude field is **ℂ** — uniquely:
ℝ is excluded (a complex structure exists) and ℍ is excluded
(only one independent one exists).

Contingencies: (i) the Klein-bottle commitment; (ii) the
fermion/spinor sector, where `J²=−I` (`figure_eight.md` L221-229).

---

## Proof

### Step 1 — Each antiperiodic cycle contributes exactly one `J²=−I`

A complex structure on the amplitude space is an operator `J`
with `J²=−I`. In the substrate, the *only* source of such an
operator is an **antiperiodic identification**: a closed cycle
along which the field picks up a sign, `φ(x + L) = −φ(x)`. By
`figure_eight.md` L182-221, traversal of the antiperiodic
x-loop acts on half-integer (fermion/spinor) wavenumber
amplitudes as `e^{i(2k+1)π} = −1`; the half-loop operator `J`
(one D-crossing, translation by `L_x/2` with loop-swap) satisfies
`J² = −I` on that sector. Each *independent* antiperiodic cycle
supplies one such `J`, and distinct antiperiodic cycles supply
*anticommuting* `J`'s (their half-loop translations along
independent directions anticommute on the spinor sector, the
standard Clifford relation for independent reflections).

Periodic cycles contribute nothing: `e^{i k_y L_y} = +1` for the
periodic y-direction (`figure_eight.md` L223), so no `J` arises
from it.

### Step 2 — The Klein bottle has exactly one antiperiodic cycle

The Klein bottle's identifications are (`klein_bottle.md` L27-35,
`figure_eight.md` L174-176):

    (x, 0) ∼ (x, L_y)            periodic in y
    (0, y) ∼ (L_x, L_y − y)      antiperiodic + reflection in x

Exactly one of the two generating cycles is orientation-reversing
(the x-cycle); the y-cycle is periodic. This is not incidental —
it is the *defining* distinction between the Klein bottle (one
antiperiodic cycle) and the torus (zero). `figure_eight.md`
L18-24 records the correction of an earlier error that wrongly
posited "a half-twist in *each* antiperiodic direction"; the
Klein bottle has only one.

### Step 3 — Therefore exactly one `J`, hence ℂ

By Step 1 and Step 2, the substrate carries **exactly one**
independent complex structure `J`, with `J² = −I` (Step 1, fermion
sector). Hence:

- **ℝ excluded**: a complex structure exists (`J² = −I ≠ +I`), so
  the commutant is not ℝ.
- **ℍ excluded**: a quaternionic structure needs *three*
  anticommuting `J`'s, requiring three independent antiperiodic
  cycles; the Klein bottle has one. So the commutant is not ℍ.

The only remaining case is `End = ℂ` (FS indicator 0): the
amplitude field is **complex, uniquely**. QED (on the fermion
sector, contingent on the Klein commitment).

---

## What this says (and what it does not)

**It says:** the substrate's commitment to the Klein bottle —
a single antiperiodic cycle — forces the amplitude field to be
ℂ, not ℝ or ℍ, on the fermion/spinor sector. The complex
structure is not merely *present* (which `J²=−I` already gave);
it is *unique*, because the antiperiodic-cycle count is exactly
one. This closes the load-bearing link of the strong
QM-reconstruction spine (`epr_bell_assembly_theorem.md`
"What this says"): once ℂ is forced, the Born exponent 2 is
already in hand (`born_rule.md`) and the Tsirelson bound `2√2`
follows as a theorem of complex Hilbert space.

**It does not say:**
- *that ℂ holds on the boson sector.* `J² = +I` there
  (`figure_eight.md` L223-229). The corpus asserts complex
  amplitudes universally via "the operator algebra of D-crossings"
  (`figure_eight.md` L235-244), but the rigorous extension of the
  fermion-sector `J` to a universal ℂ-structure is **flagged
  Class-4, not closed here**. This is the one soft spot.
- *that the Klein commitment is unconditional.* It is derived
  (mediant + Z₂ filter → `klein_bottle.md`), so this result is
  forcing **relative to** that derivation, not from nothing.
- *that the Tsirelson bound is derived from non-quantum axioms
  independently.* It follows from ℂ-Hilbert-space structure once
  ℂ is forced; the numerical value `2√2` is complex QM's.

**Bright line.** This is a forcing argument with an exhibited
mechanism (antiperiodic-cycle count), passing the discriminator's
"what breaks if different?" test (torus→ℝ, two-antiperiodic→ℍ).
It is not a re-description ("ℂ because `J²=−I` exists"), which
`ansatz_audit_policy.md` would default to Class 2. The forcing is
contingent (Klein commitment) and sector-restricted (fermion);
both contingencies are stated, not hidden.

---

## Exhibited consequences

1. **ℝ-QM is excluded as a framework prediction.** The substrate
   predicts complex (not real) amplitudes on the fermion sector.
   This *predicts* the Renou et al. (2021) network-Bell exclusion
   of real QM — a falsifiable, already-confirmed consequence.

2. **The EPR/Bell bright line is upgraded.** `epr_bell_assembly_theorem.md`
   declined to derive the Tsirelson bound from non-quantum
   axioms, resting at "reproduce QM." With ℂ forced (this doc),
   the Tsirelson bound `2√2` becomes a *consequence* (it is a
   theorem of complex Hilbert space), not an import — on the
   fermion sector, modulo the flagged universality extension.

3. **The trichotomy is geometric, not axiomatic.** "Why complex?"
   has the answer "because the substrate manifold has exactly one
   orientation-reversing cycle." A different topology gives a
   different field; the Klein bottle gives ℂ.

---

## Falsifiers

- **Topology falsifier.** If the substrate were a torus (both
  cycles periodic), `J` would not exist and the field would be ℝ;
  if it carried a second independent antiperiodic cycle, a second
  anticommuting `J` would force ℍ. The result is contingent on the
  Klein bottle's exactly-one-antiperiodic-cycle topology.

- **Sector-universality falsifier.** If the boson-sector amplitude
  field were shown to be ℝ (not ℂ) — i.e., if the D-crossing
  complex structure does *not* extend off the fermion sector —
  the universal-ℂ claim would fail while the fermion-sector result
  stood. (This is the flagged Class-4 extension.)

- **Empirical.** A confirmed real-amplitude or quaternionic-amplitude
  quantum phenomenon (contra Renou 2021 for ℝ; contra all extant
  tests for ℍ) would falsify the prediction.

- **Independent-`J` count falsifier.** If a second anticommuting
  `J²=−I` were exhibited on the substrate *without* a second
  antiperiodic cycle (breaking the Step-1 correspondence), the
  count argument would fail.

---

## Why this matters

The strong QM-reconstruction question — "is QM forced as unique
from non-quantum substrate axioms?" — reduces, per
`epr_bell_assembly_theorem.md`, to one load-bearing link: force ℂ
over ℝ/ℍ. This doc supplies that link on the fermion sector via
a topological count (antiperiodic cycles = complex structures =
exactly one for the Klein bottle), turning "why complex amplitudes"
from an unexamined assumption into a contingent forcing argument
with falsifiers. The honest residual is sector-universality, now
explicitly the single flagged Class-4 step rather than a diffuse
gap.

Class 3 (foundational articulation) with a Class-5 forcing core
on the fermion sector; parallel in discipline to
`q_mod2_conservation_theorem.md` and `epr_bell_assembly_theorem.md`.

---

## Cross-links

- `figure_eight.md` L18-24, L169-244 — corrected single-antiperiodic
  -direction `J²=−I` derivation (the input; Step 1, Step 2).
- `epr_bell_assembly_theorem.md` — the bright line this addresses
  (force ℂ → Tsirelson follows).
- `born_rule.md` — Born exponent 2 (the in-hand piece downstream
  of ℂ).
- `substrate_determinism.md` L67-71 — Born from `J²=−I`.
- `klein_bottle.md` — the antiperiodic/periodic identification
  (one antiperiodic cycle).
- `continuum_limits.md` Part II (D12) — K<1 → Schrödinger; where
  the complex wavefunction is currently *assumed* (this doc
  supplies the missing forcing).
- `canonical_glossary.md`, `phenomenon_glossary.md` — Frobenius-
  Schur / ℝ-ℂ-ℍ trichotomy entries.
- `phenomenology_cross_reference.md` — "why complex amplitudes"
  row, to be updated to cite this doc.

## One-line summary

The substrate's amplitude field is ℂ uniquely because the Klein
bottle has exactly one antiperiodic cycle, hence exactly one
complex structure `J²=−I` (fermion sector) — zero would give ℝ,
three would give ℍ; the Frobenius-Schur trichotomy realized as a
topological count, contingent on the Klein commitment, with
sector-universality the one flagged extension.
