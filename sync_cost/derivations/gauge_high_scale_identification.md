# High-scale gauge identification

The substrate-feature-to-gauge-sector assignment for the Standard
Model gauge group `SU(3)_C × SU(2)_L × U(1)_Y` at the unbroken
(high-scale) phase. Synthesizes the existing structural derivations
(`gauge_factorization.md`, `gell_mann_nishijima.md`,
`klein_connection.md`, `gauge_dictionary.md`) into a single
identification table, with what's forced vs. what's free made
explicit, and the rejected alternative assignments documented.

This is the high-scale companion to the broken-phase `Z_2 ↪ U(1)`
identification in `gauge_dictionary.md` §"Identification #1"; the
two are scale-snapshots of the same underlying structure (Z_2 center
of SU(2)_L surviving as `{±1} ⊂ U(1)_EM` after electroweak
symmetry breaking).

## The identification

| Klein-substrate feature | Physical sector | Status |
|---|---|---|
| Antiperiodic x-direction (half-twist, Z_2 monodromy) | Weak isospin `SU(2)_L` gauge group | FORCED at substrate level + free physical labeling |
| Periodic y-direction (continuous U(1) loop isometry) | Hypercharge `U(1)_Y` gauge group | FORCED at substrate level + free physical labeling |
| Denominator class q_3 = 3 in periodic direction (Z_3 fiber scaling) | Color `SU(3)_C` gauge group | FORCED at substrate level + free physical labeling |
| Half-twist eigenvalues `±1/2` | Weak isospin `T_3 = ±1/2` doublet | FORCED |
| Reflection `y ↦ 1 − y` (order 2) | Generates `Y/2` at the identification boundary | FORCED |
| Surviving fractions `{1/3, 1/2, 2/3}` from XOR filter | Electric-charge magnitudes | FORCED |

## What's forced

The substrate-level correspondences are FORCED by the existing
derivations:

1. **Direct-product Lie algebra structure** (`gauge_factorization.md`
   theorem): any gauge algebra compatible with K²'s topological
   decomposition admits `g = g_x ⊕ g_y` with `[g_x, g_y] = 0`.
   Simple algebras (including `su(6)` whose center is `Z_6`) are
   excluded.

2. **Minimum-rank selection per direction**
   (`gauge_factorization.md` §"Minimum-rank selection"):
   - `g_x` (antiperiodic) center ⊇ `Z_2` from `q_2 = 2` fiber
     scaling. Minimum-rank simple compact algebra with center
     `Z_2` is `su(2)`, rank 1.
   - `g_y` (periodic) center ⊇ `Z_3` from `q_3 = 3` fiber
     scaling. Minimum-rank simple compact algebra with center
     `Z_3` is `su(3)`, rank 2.

3. **U(1)_Y attachment** (`gauge_factorization.md` §"Minimum-rank
   selection", consequence): the periodic direction's continuous
   `U(1)` loop isometry attaches a `U(1)_Y` factor; the
   Gell-Mann–Nishijima relation `Q = T_3 + Y/2`
   (`gell_mann_nishijima.md`) fixes the `Y/2` coefficient via the
   reflection's order 2.

4. **Gauge group**: `G = SU(3) × SU(2) × U(1)` (up to discrete
   quotients). This is the Standard Model gauge group.

5. **Centers**: `Z(G) ⊇ Z_2 × Z_3 = Z_6` directly factored, not
   cyclic — matching the framework's `Z_2 × Z_3` residue structure
   (`klein_connection.md` §"The three identifications") rather than
   the cyclic `Z_6` of `SU(6)`.

## What's free

The substrate forces the abstract gauge group `SU(3) × SU(2) ×
U(1)` and the assignment of each factor to a substrate feature
(direction or denominator class). What remains free is the
*physical-sector labeling*:

- The antiperiodic direction's `SU(2)` could in principle be
  identified with weak isospin `SU(2)_L`, with a hidden gauge
  factor, or with a spectator. The framework commits to
  `SU(2)_L` (the Standard Model's electroweak sector).
- The periodic direction's `U(1)` could be hypercharge `U(1)_Y`,
  `B − L`, or any other `U(1)` factor. The framework commits to
  `U(1)_Y`.
- The `q_3 = 3` denominator class's `SU(3)` could be color or
  generation index or some other `SU(3)`. The framework commits
  to color `SU(3)_C`.

These commitments are *partially* constrained: the structural
arguments below rule out specific alternative labelings as
inconsistent. They are not fully forced, in that no theorem
selects "weak isospin SU(2)_L specifically" rather than another
SU(2) gauge sector with the same algebraic structure. The
residual freedom is one *identification* commitment in the sense
of `gauge_dictionary.md` (specifically, the `Z_3 ↪ Z(SU(3))` entry
that remains IDENTIFIED after the promotion discipline).

## Rejected alternative labelings

Three alternative assignments fail structural compatibility checks
and are ruled out:

### Swap: `q_2 ↔ SU(3)`, `q_3 ↔ SU(2)`

The denominator class `q_2 = 2` carries fiber scaling `Z_2`; the
class `q_3 = 3` carries `Z_3`. Swapping the gauge-group assignment
to `q_2 ↔ SU(3)` would require `SU(3)`'s center `Z_3` to match
`q_2`'s `Z_2` fiber — Cartan's classification of simple Lie group
centers rules this out: `Z(SU(2)) = Z_2`, `Z(SU(3)) = Z_3`, and
the centers do not match across the swap. **Rejected by Cartan
classification.**

### Periodic direction ↔ color `SU(3)_C`

If `SU(3)_C` were attached to the periodic direction *as the
continuous gauge symmetry* (rather than via the discrete
`q_3 = 3` fiber), then color would be unbroken at all scales (the
periodic direction is unbroken at all scales) without
confinement. But `SU(3)_C` confines: at low energies, color
charges are confined into singlets. The framework's identification
puts `SU(3)_C` on the *discrete* `q_3 = 3` fiber, where the
confinement scale arises from tongue-width dynamics (narrow
tongues at high q correspond to confined modes), not on the
continuous periodic direction. **Rejected by confinement
phenomenology.**

### Swap: `Y ↔ T_3` in the Gell-Mann–Nishijima relation

`gell_mann_nishijima.md` derives `Q = T_3 + Y/2` from the
boundary identification, with the factor `1/2` being the order
of the y-reflection `y ↦ 1 − y`. Swapping `Y` and `T_3` would
give `Q = Y + T_3/2`, with `1/2` on the half-twist eigenvalue
rather than the reflection eigenvalue. But the half-twist has
order 2 already by construction (it's the antiperiodic
identification), so there's no separate "order-2 generator"
factor of `1/2` to apply to it; the factor `1/2` arises
specifically from the *reflection* having order 2, which acts
on the *periodic-direction* `Y`-eigenvalue. **Rejected by the
order-2 argument: the `1/2` coefficient identifies its source
generator uniquely.**

## Relation to the broken-phase identification

After electroweak symmetry breaking, the high-scale
`SU(2)_L × U(1)_Y` mixes via the Weinberg angle into
`U(1)_EM × {massive gauge bosons}`. The Z_2 center of `SU(2)_L`
survives as the `{±1}` subgroup of `U(1)_EM`. The harmonics
identification

    Z_2 ↪ U(1)         (`gauge_dictionary.md` §Identification #1, DEFINITION)

describes this broken-phase consequence: the post-EWSB `Z_2 ⊂
U(1)_EM` is the same `Z_2` that carried the antiperiodic
monodromy at the high scale. The two readings are scale-snapshots
of one structure:

| Scale | Identification |
|---|---|
| High-scale (unbroken) | Antiperiodic Z_2 monodromy ↔ `Z_2` center of `SU(2)_L` |
| Post-EWSB (broken) | Same Z_2 ↪ `U(1)_EM` as `{±1}` subgroup |

No conflict; the `Z_2` is the same algebraic object viewed at
different scales of the gauge symmetry breaking.

## Dependencies

- `klein_bottle.md` / `klein_bottle_derivation.md`: K² topology,
  XOR filter, half-twist + reflection identifications.
- `gauge_factorization.md`: direct-product Lie algebra theorem,
  exclusion of simple algebras, minimum-rank selection.
- `gell_mann_nishijima.md`: `Q = T_3 + Y/2` from boundary geometry.
- `klein_connection.md`: the three original identifications
  chain (Z_2 ↪ U(1), Z_3 ↪ Z(SU(3)), 12 transitions ↔ 12
  generators).
- `gauge_dictionary.md`: promotion of identifications to
  DEFINITION / FORCED / IDENTIFIED grades; broken-phase Z_2 ↪ U(1).

## Status

**Synthesis-derivation.** The substrate-feature-to-gauge-group
correspondence is forced by the cited harmonics derivations, with
one remaining IDENTIFIED commitment (per `gauge_dictionary.md`)
about the physical-sector labeling. The high-scale assignment
table above is the single explicit reference for what the
identification commits to.

The companion textbook entry in the `derivation` repo
(`gauge_identification.md`, kind: identification, input_types:
[4]) carries the same content under the six-type input taxonomy
of `derivation/derivations/inputs_taxonomy.md`. Cross-reference
is bidirectional; harmonics provides the structural derivations
the textbook cites, the textbook provides the input-type
classification harmonics does not use.

## Cross-references

| File | Role |
|---|---|
| `gauge_factorization.md` | Direct-product theorem; minimum-rank selection |
| `gell_mann_nishijima.md` | `Q = T_3 + Y/2`; T_3, Y substrate origins |
| `klein_connection.md` | Three identifications chain |
| `gauge_dictionary.md` | Promotion grades; broken-phase Z_2 ↪ U(1) |
| `klein_bottle_derivation.md` Part VIII | Hierarchy table by denominator |
| `discrete_gauge_resolution.md` | Negative results on continuum gauge derivation |
| `gauge_sector_lovelock.md` | Yang-Mills downstream chain |
