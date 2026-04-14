# Fourth Generation Revisited Under the Integer Conservation Law

**Status:** Closed — a 4th charged lepton generation is **forbidden**
by the integer conservation law `depth × |3Q| = k_sector`. The old
empirical prediction of ~7.3 GeV is superseded.

This note reconciles the original generation-exponent-law prediction
with the structural constraint that emerged from the mass-sector
closure (`mass_sector_closure.md`, `integer_conservation_law.py`).

---

## 1. The original ~7.3 GeV prediction

Before the integer conservation law was recognized, the generation
exponent law (`generation_exponent_law.py`) was treated as an open
extrapolation along the **Fibonacci backbone**:

    1/1 → 2/1 → 3/2 → 5/3 → 8/5 → 13/8 → 21/13 → …
    depth: 0     1     2    3    4     5      6   …

The three known lepton generations were read as the pair of steps
(3/2, 5/3) at backbone depths 2 and 3:

| Step | Base | Backbone depth | Exponent |
|------|------|----------------|----------|
| τ → μ | (3/2)³ = 27/8 | 2 | a₁ ≈ 2.320 |
| μ → e | (5/3)³ = 125/27 | 3 | a₂ = (3/2)a₁ ≈ 3.481 |

The generation exponent law fixes `a₂/a₁ = q₃/q₂ = 3/2`. The natural
extrapolation to a hypothetical 4th generation was to take one more
step along the backbone to mode **13/8 at depth 5**, with exponent
`a₃ = (3/2)² a₁ ≈ 5.22`. A naïve one-step extrapolation from the
known lepton tower to mode 13/8 gave a mass scale around

    m_L4 ~ m_τ × (something involving (13/8)^(3 a₃))
         ~ few GeV

and specific numerical choices of the step structure put the
estimate near **~7.3 GeV**. This was recorded as empirical
prediction #8 ("No 4th gen lepton below 7.3 GeV"), with status
"consistent with LEP bound (<45 GeV)" — the prediction was "not
observed" but also below LEP's exclusion, so it lived as an open
question awaiting either direct search or a structural resolution.

## 2. The new constraint: integer conservation

The mass-sector closure replaced the empirical exponent law with a
structural integer identity:

    depth × |3Q| = k_sector

where `|3Q|` is the electric charge in units of e/3 (an integer) and
the sector constants are the dual gauge adjoint dimensions:

| Sector | |3Q| | k_sector | depth (max) |
|--------|-----|----------|-------------|
| Lepton | 3 | q₃² = 9 | **3** |
| Up-type quark | 2 | q₂³ = 8 | 4 |
| Down-type quark | 1 | q₂³ = 8 | 8 |

For **charged leptons**, `|3Q| = 3` is fixed by the charge, and
`k_lepton = 9 = (dim adj SU(2))²` is fixed by the chirality-squared
gauge structure. Therefore **every charged lepton must live at
tree depth exactly 3** — no more, no less — and the three generations
saturate that depth budget.

This is not a bound on mass values but a **bound on tree positions**:
a charged lepton is a walker whose total tree depth is 3, period.

## 3. Does a 4th generation exist?

Under the integer law, a 4th charged lepton would have to satisfy
both `depth × |3Q| = 9` and `|3Q| = 3`, i.e. it would have to sit at
tree depth 3 like the first three generations. But it would also
have to be at a **distinct walk position** (otherwise it would be
one of the existing generations).

So the question reduces to: how many distinct walk positions exist
at depth ≤ 3 on the lepton Fibonacci backbone?

### The lepton Fibonacci backbone at depth ≤ 3

The backbone is the Stern-Brocot path

    1/1 → 2/1 → 3/2 → 5/3 → 8/5 → 13/8 → …
    depth: 0     1     2    3    4     5

Below the cap `depth = 3`, only **two nontrivial base positions** are
available:

- **3/2 at depth 2** — the (τ → μ) step
- **5/3 at depth 3** — the (μ → e) step

Together with the root, the backbone has exactly **three sector
base slots** in the accessible region: `{e, μ, τ}`. The base pair
`(3/2, 5/3)` is completely consumed by the three known generations.

### Could there be a non-backbone base pair at depth ≤ 3?

The other mediants at depth ≤ 3 in the Stern-Brocot tree are
`1/2, 1/3, 2/3` and their reciprocals — all used elsewhere (the
quark sectors' base pairs, and the root 1/1). None is available to
host a 4th charged lepton; in particular, the "walk-before-
repetition" / Farey-partition argument
(`sector_base_pairs.py`, `integer_conservation_law.py`) already
distributes the depth ≤ 3 budget exhaustively across leptons +
up-type quarks + down-type quarks via the depth-sum totals

    lepton sum    = 5   = q₂ + q₃
    up-type sum   = 6   = q₂ q₃
    down-type sum = 12  = 2 q₂ q₃

There is no unused depth-≤-3 slot available.

### What about the old 13/8 prediction at depth 5?

The original ~7.3 GeV prediction used mode `13/8` at **depth 5**.
Plugging this into the integer law:

    depth × |3Q| = 5 × 3 = 15 ≠ 9

which **violates** `k_lepton = 9`. Similarly, depth 4 gives
`4 × 3 = 12 ≠ 9`. Any depth ≥ 4 is excluded for charged leptons
by the integer law. The old backbone extrapolation was a linear
guess that did not see the mod-9 constraint.

## 4. Result: 4th charged lepton is forbidden

**A fourth charged lepton generation is structurally forbidden.**

The integer conservation law `depth × |3Q| = 9` caps charged
leptons at tree depth 3, and the Fibonacci backbone has exactly
three base slots at depth ≤ 3, all consumed by the known `{e, μ, τ}`.
No free position remains. Generating one would require breaking
either:

- the integer law (violating the gauge cross-link
  `q₃² − 1 = q₂³` that selects `(q₂, q₃) = (2, 3)` as the unique
  Klein-bottle integer pair), or
- the walk-before-repetition principle (giving up tree acyclicity,
  i.e. destroying the Stern-Brocot structure itself).

Neither is available without tearing down the entire framework.

### The old ~7.3 GeV prediction is superseded

The old empirical prediction #8 is now upgraded from

> "No 4th gen lepton below 7.3 GeV (consistent with LEP)"

to

> "**No 4th charged lepton at any mass, ever**, as a structural
> consequence of the integer conservation law."

This is a stronger and falsifiable statement: detection of **any**
charged lepton beyond τ — at any mass — would falsify the
integer conservation law and, by the cross-link identity, the
uniqueness of `(q₂, q₃) = (2, 3)`.

## 5. Physical interpretation: why 3 is the maximum

### Why leptons specifically get depth 3

The lepton sector constant `k_lepton = q₃² = 9` comes from the
**square** of the SU(2) adjoint dimension — the doubling reflects
lepton chirality asymmetry (`mass_sector_closure.md`). Leptons have
DIFFERENT SU(2) reps for L and R (doublet vs. singlet), so their
walk budget is `(dim adj SU(2))² = 9`. Quarks, whose color is
chirality-blind, use a single copy: `k_quark = dim adj SU(3) = 8`.

Combining `k_lepton = 9` with `|3Q_lepton| = 3` forces
`depth = 9/3 = 3`. There is no slack.

### Why 3 generations, stated three ways

The integer law gives a direct structural reading of "3 generations,"
complementing the three earlier derivations:

1. **Phase-state counting**: 2² − 1 = 3 observable phase states
   (one is dark/unobservable via Klein-bottle antipode)
   — `generation_mechanism.md`, Category A.
2. **Chain topology**: the D-link (gap-gap link) severs the chain
   at path length 4, leaving exactly three surviving chain lengths
   at our K — `generation_mechanism.md §7`.
3. **Integer conservation**: the lepton walk budget `k_lepton = 9`
   and charge quantum `|3Q| = 3` jointly cap walk depth at 3, and
   the Fibonacci backbone has exactly three base slots at depth ≤ 3.
   **This note.**

All three readings return the same integer 3. They are three
projections of the same fact: the Klein-bottle denominators `(2, 3)`
are the unique integer pair where SU(2)² and SU(3) adjoint
dimensions cross-link, and this pair carries exactly three lepton
slots.

### A stronger claim

The depth-3 cap is saturated but not arbitrary. Any extension
of the sector would require either:

- a **new denominator class** beyond `(q₂, q₃) = (2, 3)` — excluded
  by the uniqueness of the cross-link identity `q₂² − 1 = q₃` and
  `q₃² − 1 = q₂³`, which has only the `(2, 3)` solution in positive
  integers; or
- a **new charge quantum** below the elementary step `|3Q| = 3`
  for leptons — excluded by Gell-Mann–Nishijima on the Klein
  bottle (`gell_mann_nishijima.md`), which sets charge in
  integer units of `e/3` with `|3Q| = 3` for any particle carrying
  full electric charge.

Neither hook is available. The count of charged lepton
generations is structurally and uniquely three.

---

## Summary

| Question | Old answer | New answer |
|----------|-----------|-----------|
| Is there a 4th lepton? | "Below 7.3 GeV, predicted absent" | **Forbidden at any mass** |
| Where would it sit? | Backbone mode 13/8, depth 5 | Integer law forces depth 3, no slot left |
| What rule is operative? | Exponent law a₃ = (3/2)a₂ | depth × \|3Q\| = 9 |
| Can LHC/future colliders falsify? | Yes, if found below ~45 GeV | Yes, if found at **any** mass |
| Does the mass prediction still apply? | ~7.3 GeV | N/A; the slot doesn't exist |

The generation exponent law `a₂/a₁ = 3/2` remains true as a
**reading of the integer law within the 3-slot lepton subspace**.
Extrapolating it one more step beyond depth 3 was a linear
extension that didn't respect the integer constraint. The
constraint is now the primary object; the exponent law is its
projection onto the logarithm of mass.

**Closure status:** The 4th generation question is resolved in
the negative: 4th charged lepton is forbidden by the integer
conservation law `depth × |3Q| = 9`.
