# Gap 3: The Gauge Center Promotion and the Bundle Construction

## Status

**Open.** Issue #56 (2026-04-08) grades this as a Tier 1 structural gap
— specifically, the promotion of "GCD-of-mediant-outcomes produces
Z₂ × Z₃" to "this Z₂ × Z₃ is the center of the Standard Model gauge
group" is classified as a Type C identification. Subsequent work in
`gauge_sector_lovelock.md` (2026-04-13) asserts closure via a principal
Z₆-bundle construction plus Cartan's classification plus Utiyama's
theorem. This document reconciles the two views by identifying exactly
what the existing construction does and does not prove.

The other two Tier 1 gaps received honest-open treatment in
`gap_1_christoffel.md` and `gap_2_spatial_diffusion.md`. This document
gives Gap 3 the same treatment — restating the remaining problem
precisely so it can be attacked rather than rewritten.

---

## What is derived

Three independent results survive the 2026-04-13 reconciliation and
contribute to the gauge-sector chain:

### 1. The discrete Z₆ structure is real

`fiber_bundle.py`, `gap3_principal_bundle.py`, and the XOR analysis
together establish:

- The GCD of mediant outcomes on the Klein bottle factors as
  `GCD mod 2 × GCD mod 3`, producing a Z₂ × Z₃ = Z₆ residue structure.
- The 4 irreducible Klein bottle modes {A, B, C, D} carry a free
  transitive Z₆ action on their fiber coordinates (scaled
  representatives of the base rationals).
- The 12 directed transitions in the mode graph carry Z₆ holonomies
  satisfying `g_αβ · g_βγ · g_γα = e` on all 24 triangles.

**Status of this result**: a verified arithmetic statement about a
finite group action on a finite set. `gap3_principal_bundle.py` proves
it computationally with no approximation.

### 2. The Klein bottle denominator classes are {2, 3}

D19 derives the XOR parity filter and the uniqueness of the denominator
pair (q₂, q₃) = (2, 3) from the Klein bottle's antiperiodic boundary
conditions. This is a topological result, not an identification.

### 3. Anomaly cancellation

`anomaly_check.py` verifies that the Klein bottle fractions
{1/3, 1/2, 2/3} with the Gell-Mann-Nishijima assignment satisfy all six
Standard Model anomaly conditions exactly. This is a non-trivial
consistency check of the identification, not a derivation of it.

---

## What is not derived

The gauge-sector chain asserted in `gauge_sector_lovelock.md` has four
logical links:

    (a) Klein bottle  →  Z₆ residue on discrete 4-mode graph
    (b) Z₆ residue    →  principal G-bundle with connection
    (c) Principal G-bundle  →  unique G = SU(3) × SU(2) × U(1)
    (d) G-bundle + Lorentz + 2nd order  →  Yang-Mills (Utiyama)

Link (a) is derived (see §"What is derived"). Link (d) is a theorem
with well-understood hypotheses. Links (b) and (c) are where the
Type C identifications sit.

### Break 1: Discrete torsor ≠ Lie-group principal bundle

`gap3_principal_bundle.py` verifies that the GCD-reduction fiber is a
**principal Z₆-bundle**: a finite set with a free transitive Z₆
action, fibered over a discrete 4-point base space.

Utiyama's theorem requires a **principal G-bundle** in the
differential-geometric sense: a smooth manifold E with a free smooth
right action of a Lie group G, projecting onto a Lorentzian 4-manifold
M, equipped with a Lie-algebra-valued connection 1-form A. The
connection's curvature F = dA + A ∧ A is what appears in the Yang-Mills
Lagrangian.

The two objects are not the same:

| Object | `gap3_principal_bundle.py` | Utiyama's hypothesis |
|--------|----------------------------|----------------------|
| Base space | 4-point discrete set | Lorentzian 4-manifold |
| Structure group | Z₆ (finite, abelian) | Lie group G (continuous) |
| Fiber | 6-element torsor | Lie-group-diffeomorphic smooth fiber |
| Connection | — | Lie-algebra-valued 1-form A_μ |
| Curvature | — | F_μν = ∂_μA_ν − ∂_νA_μ + [A_μ, A_ν] |
| Field equation | — | D_μ F^μν = J^ν |

The script's "cocycle condition" check is the statement that assigning
a Z₆ holonomy to each edge of the K_4 mode graph is consistent around
every triangle. This is a vacuous condition for any bundle over a
discrete base space: such bundles are always trivial, and the cocycle
is the triviality witness.

**The gap**: there is no construction in the repository of a continuous
principal bundle over a continuous spacetime whose structure group has
center Z₆ and whose action is compatible with the Klein bottle's Z₆
residue. The sentence in `gauge_sector_lovelock.md` Premise 4 — *"A
principal G-bundle with a connection IS a gauge structure; the cocycle
verification makes this formal rather than informal"* — elides this
step by using "principal G-bundle" to refer to the finite object
verified by the script and to the continuous object needed by
Utiyama's theorem.

### Break 2: Center determines group only up to Cartan selection

Cartan's classification assigns a center to each simple compact Lie
group. Given a desired center, multiple groups are candidates:

- Center Z₂: SU(2), SO(2n+1), Sp(2n), E₇, ...
- Center Z₃: SU(3), E₆

`gauge_sector_lovelock.md` selects SU(2) and SU(3) via four criteria:

1. **Minimum rank given the center.** SU(n) has rank n−1, which is
   minimum among groups with center Z_n.
2. **Direct product Z₂ × Z₃ vs cyclic Z₆.** Rules out SU(6) (which has
   cyclic Z₆ center).
3. **Confinement pattern.** q=3 locked, q=2 open.
4. **Anomaly cancellation.** Fixes charges uniquely given the groups.

Criterion 1 is justified by: *"the Klein bottle supplies one
denominator class per Z factor; a gauge group of higher rank would
require additional Cartan generators that the topology does not
provide."* This argues that the framework has no source of extra
generators, not that extra generators are mathematically forbidden.
A physical theory with center Z₂ and rank 2 (say Sp(4)) is not
excluded by Klein-bottle topology — it is excluded because the
framework identifies "Klein bottle denominators supply rank." This is
an identification, not a proof of impossibility.

Criterion 2 distinguishes the direct product Z₂ × Z₃ from the cyclic
Z₆ on the basis of the two modes being "distinguishable" (different
denominator classes). Z₂ × Z₃ ≅ Z₆ as abstract groups (CRT). The
choice of realization depends on whether the framework reads the two
Klein-bottle denominators as independent factors or as one cyclic
structure. Both readings are available; the framework commits to the
direct-product reading because it matches observation.

Criteria 3 and 4 are consistency checks that the selected groups fit
observation, not derivations of the groups from the center.

**The gap**: Cartan's classification gives uniqueness *once rank and
realization are fixed*. Fixing rank from "denominator classes counted"
and fixing the direct-product realization from "denominators are
distinguishable" are identifications, not theorems. The step from
"the Klein bottle has residue Z₂ × Z₃" to "the gauge group is
SU(3) × SU(2) × U(1)" goes through these identifications.

### Break 3: The U(1)_Y identification is explicitly a posteriori

`gauge_sector_lovelock.md` §M5 already acknowledges this:

> The topology gives *a* U(1), not specifically U(1)_Y. Its identity
> as hypercharge is downstream: the Gell-Mann-Nishijima relation ties
> the abelian charge to the non-abelian T_3, and with that relation
> the Klein bottle fractions fix the hypercharge assignment uniquely.

This is an honest flag, not a hidden step. But it means the chain
closes only with the GNN relation (D43) as an additional input, and
D43 itself asserts the form Q = T₃ + Y/2 — a relation about charges,
not a derivation of the abelian factor from the Klein bottle's
periodic direction.

---

## The precise mathematical problem

The gap decomposes into three progressively stronger statements. Each
closes a distinct piece of the chain.

### Level A: Bundle construction

**What needs to be proved**: construct a principal G-bundle in the
differential-geometric sense over the Klein bottle (or its continuum
descendant in the 4-manifold sense), with structure group G a Lie
group whose center contains Z₂ × Z₃, such that the discrete Z₆
residue verified by `gap3_principal_bundle.py` is the induced action
of the center subgroup on the fibers of a trivialization adapted to
the 4 irreducible mode classes.

Without this, Utiyama's theorem has no bundle to apply to. The
theorem's output (D_μ F^μν = J^ν) is not in evidence until the bundle
exists.

### Level B: Rank selection

**What needs to be proved**: that the choice of rank-1 for the Z₂
factor and rank-2 for the Z₃ factor is forced by the Klein-bottle
dynamics rather than selected by an identification.

One candidate route: show that the Cartan subalgebra is generated by
the simultaneous eigenvalues of the locked-mode projectors, and that
the Klein bottle's denominator classes produce exactly rank-1 and
rank-2 subalgebras under the XOR constraint. This would promote the
"one denominator class per Z factor" identification to a statement
about how many independent locked-mode directions the topology
supports.

Without this, Cartan selects SU(2) and SU(3) only among rank-1 and
rank-2 candidates — it does not prove the ranks are 1 and 2.

### Level C: Direct product vs cyclic

**What needs to be proved**: that the Klein-bottle residue realizes
Z₂ × Z₃ as a direct product (center of SU(2) × SU(3)) rather than
cyclic Z₆ (center of SU(6)).

One candidate route: show that the q=2 and q=3 mode classes carry
orthogonal irreducible representations of the residual symmetry, so
the residue action commutes with a direct sum decomposition of the
mode space. The "distinguishability" argument in
`gauge_sector_lovelock.md` M3 would then follow from this
decomposition as a theorem, not an identification.

Without this, SU(6) is a viable alternative structure group with
the same center (as an abstract group).

---

## Connection to other gaps

- **Gap 1 (Christoffel)** and **Gap 2 (spatial diffusion)** are in the
  *continuum* sector — both concern the K=1 limit, the manifold
  structure of the base, and the promotion of discrete mode
  interactions to differential operators. A continuum principal bundle
  construction for Gap 3 Level A would plausibly share machinery with
  the "tree adjacency → spatial Laplacian" problem in Gap 2, because
  both need the same discrete-to-continuous promotion.

- **sin²θ_W = 8/35, α_s/α_2 = 27/8, m_H/v = 1/2, λ = 1/8**: after
  `sinw_fixed_point.md`, these are explicitly downgraded to
  "measure-theoretic near-coincidences" at 1–4% agreement. They are
  not part of Gap 3 as defined here — they are accepted as
  unexplained structural rationals. If Gap 3 closes at Level A or
  better, the near-coincidence status of the coupling ratios is not
  affected.

- **K\* = 2^(-3/14)** (`CHAIN_KSTAR.md`): the K\_star chain's Step 6
  is a separate conjectural closed form in the mass sector, not a
  gauge-sector identification. Closing Gap 3 neither confirms nor
  refutes Step 6.

- **Cross-sector mass ratios** (`item12_cross_sector_ratios.md`): the
  "orientation-preserving walk has mode volume q₂ q₃" conjecture for
  down-type quarks is in the mass sector. Independent of Gap 3.

---

## What closing this gap means

If Level A closes: `gauge_sector_lovelock.md` Premise 4 becomes a
theorem. Utiyama's theorem applies unambiguously. The dynamics
(Yang-Mills) is derived.

If Level B closes additionally: Cartan's classification applies
unambiguously to select SU(2) × SU(3) rather than requiring rank to
be fixed by identification. The gauge group's rank is derived.

If Level C closes additionally: the direct-product realization is
forced rather than chosen. SU(6) is excluded.

The gauge-sector chain would then read:

    Klein bottle topology                    (derived, D19)
    → Z₆ residue on discrete mode graph      (derived, this gap §"What is derived")
    → continuous principal G-bundle           (Level A)
    → rank fixed by XOR structure             (Level B)
    → direct-product realization forced       (Level C)
    → Cartan classification: G = SU(3) × SU(2) × U(1)  (theorem)
    → Utiyama + 2nd order → Yang-Mills        (theorem)

This would fully promote Gap 3 from the Type C grading in issue #56
to Type A/B in the framework's own classification — forced by
uniqueness or conditionally derived, not "structural match" via
identification.

## What leaving this gap open means

The current state is internally consistent and observationally
successful: the derivation produces SU(3) × SU(2) × U(1) and
Yang-Mills dynamics with the right charges and anomaly cancellation.
But the bridge from the Klein bottle to the continuum gauge structure
passes through three identifications (Level A, B, C above) that are
each plausible but not forced.

This is the gauge-sector analog of the Christoffel connection in
`gap_1_christoffel.md`: the answer is almost certainly right, the
supporting calculations work out, and the remaining step is a
structural proof rather than a phenomenological fit. The gap is
labeled open not because the framework is wrong about the gauge
group but because the word "derived" in `gauge_sector_lovelock.md`
currently covers three steps that are identifications.

## References

- Issue #56 (2026-04-08): original Gap 3 grading as Tier 1 Type C
- `gauge_sector_lovelock.md`: the closure claim, rewritten 2026-04-13
- `gap3_principal_bundle.py`: the finite Z₆ cocycle verification
- `fiber_bundle.py`: the GCD residue structure
- `discrete_gauge_resolution.md`: honest D21 result that the Klein
  bottle produces charges + center + confinement but "NOT the full
  Lie algebras" and "NOT Yang-Mills dynamics" from the continuum limit
- `xor_asymmetry.py`: q=3 confinement, q=2 deconfinement
- `anomaly_check.py`: six SM anomaly conditions satisfied exactly
- `sinw_fixed_point.md`: the parallel honest downgrade in the
  coupling-ratio sector — model for the treatment here
- `gap_1_christoffel.md`, `gap_2_spatial_diffusion.md`: sibling Tier 1
  gap documents
- Utiyama, R. (1956). Invariant theoretical interpretation of
  interaction. Physical Review, 101(5), 1597–1607.
- Cartan, É. (1894). Sur la structure des groupes de transformations
  finis et continus.
