# Gauge-Sector Dictionary Promotion

## Claim

The three identifications isolated in `klein_connection.md` for the
Klein-bottle gauge structure — `Z₂ ↪ U(1)`, `Z₃ ↪ Z(SU(3))`, and
12 mode transitions ↔ 12 gauge generators — reduce to a single
irreducible dictionary entry under the same promotion moves that
`operator_to_curvature.py` applies to the gravity chain. Two of the
three are demoted from IDENTIFIED to DEFINITION or FORCED; the third
factors, with one factor FORCED and the other merging with the
remaining identification.

Final state: **one** irreducible identification — the framework's
combinatorial gauge structure (Z₆ torsor over the mode graph) IS the
gauge theory's smooth gauge structure (principal `SU(3)×SU(2)×U(1)`
bundle with connection) — paralleling the gravity chain's single
irreducible identification `ω(x) = √(4πGρ(x))`.

## Context

`operator_to_curvature.py` reduced the gravity chain's five original
identifications to one by reclassifying four of them as DEFINITION or
FORCED:

    r = N             was IDENTIFIED, now DEFINITION
    C_ij = γ_ij       was IDENTIFIED, now FORCED
    ∂_i ψ = N_i/N     was IDENTIFIED, now FOLLOWS
    K(x,x') = Green's was IDENTIFIED, now FOLLOWS
    ω = √(4πGρ)       was IDENTIFIED, remains IDENTIFIED

This derivation applies the same move to the gauge chain's three
identifications. The promotion discipline:

- **DEFINITION**: same object, two names. Specifying one is specifying
  the other.
- **FORCED**: uniquely determined by other, already-established
  structure.
- **IDENTIFIED**: dictionary entry between two ontologies. Irreducible
  until additional structure promotes it.

## Identification #1: `Z₂ ↪ U(1)` → DEFINITION

The Klein bottle's antiperiodic identification

    (0, y) ~ (1, 1 − y)

specifies a gluing of the fundamental domain's edges. A half-integer
(spinor) wavefunction on K² transforms as

    f(x + L_x, y) = (−1) · f(x, L_y − y)

under the identification, where `(−1) ∈ {±1} ⊂ U(1)`.

**Claim.** This is a DEFINITION, not an identification.

**Proof.** H¹(K²; Z₂) = Z₂ is non-trivial and carries a canonical
generator (the class of the antiperiodic edge identification). By
definition of Čech cohomology, a class in H¹(B; G) IS the isomorphism
class of a principal G-bundle over B. The generator of H¹(K²; Z₂) is
therefore *by definition* the isomorphism class of a non-trivial
principal Z₂-bundle over K².

The inclusion Z₂ ↪ U(1) as `{±1}` is the unique subgroup of U(1)
isomorphic to Z₂ that is stable under the U(1) action by complex
conjugation. No choice: the only Z₂ subgroup of U(1) is `{±1}`.

The composition — Klein bottle's topological Z₂ class, composed with
the canonical Z₂ ↪ U(1) inclusion — gives a principal U(1)-bundle
class *by construction*, not by identification. The objects on the
two sides of "Z₂ ↪ U(1)" are the same mathematical object (a class
in H¹ under an inclusion of structure groups), not two different
objects being equated.

**Status**: was IDENTIFIED, now **DEFINITION**.

## Identification #3: 12 transitions ↔ 12 generators — factors

The Klein bottle's 4-mode graph has 12 directed edges
(`gap3_principal_bundle.py`), decomposing as:

- **8 cross-sector**: edges between modes with different `(q_1, q_2)`
  denominator assignments
- **4 within-sector**: edges preserving `(q_1, q_2)`, split 2 + 2
  between the two sectors

The gauge algebra `su(3) ⊕ su(2) ⊕ u(1)` has dimension 12,
decomposing as:

- **8 off-diagonal**: 6 roots of `su(3)` + 2 roots of `su(2)` — the
  generators that move between rep-space basis vectors
- **4 Cartan**: 2 of `su(3)` (`T₃, T₈`) + 1 of `su(2)` (`T₃'`) + 1 of
  `u(1)` (`Y`) — the diagonal generators

**Sub-claim #3a (count decomposition)**: The matching

    8 cross-sector ↔ 8 off-diagonal
    4 within-sector ↔ 4 Cartan

is FORCED by the graph / algebra structure.

**Argument for #3a.** Cross-sector edges change the mode-type
`(q_1, q_2)` — they move between distinct sectors. Off-diagonal Lie
algebra generators change the rep-space basis vector — they move
between distinct basis states. Under the correspondence "mode
transitions are gauge bosons" (sub-identification #3b, below), edges
that change sector-type MUST correspond to generators that change
basis-type. The cardinality 8 = 8 follows from the graph having 8
cross-sector edges and the algebra having 8 off-diagonal generators;
this count is determined by the Klein bottle's 4 irreducible modes
(forced by XOR + field equation, `klein_bottle.md`) and by Cartan's
classification of the simple algebras with centers Z₂ and Z₃
(forced by `gauge_factorization.md` + minimum rank).

The finer decomposition `4 = 2 + 2` on the framework side corresponds
to `4 = 2 + 1 + 1` on the gauge side (Cartan of `su(3)` + Cartan of
`su(2)` + `u(1)_Y`), with one of the framework's within-sector pairs
splitting into `(Cartan su(2), U(1)_Y)` under the electroweak mixing
that `sinw_fixed_point.md` classifies as a measure-theoretic
near-coincidence rather than a derivation. The decomposition 4 into
2+2 on the framework side and 4 into 2+1+1 on the gauge side carries
the electroweak mixing as its reconciliation.

**Sub-claim #3b (type correspondence)**: The statement "mode transitions
ARE gauge bosons" is the type-level part of Identification #3 that
remains. It is not reducible to DEFINITION or FORCED by itself: a
directed edge in a 4-vertex graph and a Lie-algebra-valued 1-form on
a smooth manifold are not the same kind of object.

Sub-identification #3b merges with Identification #2 below.

**Status of #3**: factors into #3a (FORCED by graph/algebra structure)
and #3b (IDENTIFIED, merged with #2).

## Identification #2: `Z₃ ↪ Z(SU(3))` — merged irreducible

The framework's `Z₃` arises from GCD mod 3 on the XOR-filtered
Stern-Brocot tree (`fiber_bundle.py`, `gap3_principal_bundle.py`). It
acts on the 3-element fiber of `q_2 = 3` scaling representatives by
cyclic addition `k_2 ↦ k_2 + 1 mod 3`. The object it acts on is a
**discrete Z₃-torsor** — a 3-element set with free transitive Z₃
action.

`Z(SU(3))` acts on the fundamental representation `C³` by scalar
multiplication: `ζ · v = e^{2πi/3} v` for `v ∈ C³`. The object it
acts on is a **continuous 3-dimensional complex vector space** carrying
a specific SU(3) representation.

**Observation.** These are not isomorphic as Z₃-representations. The
framework's action is the regular representation of Z₃ on its own
underlying set (one orbit of size 3, decomposes as `V_0 ⊕ V_1 ⊕ V_2`
where V_k are the three irreps of Z₃). The `Z(SU(3))` action on `C³`
is three copies of the irrep `V_1` (scalar multiplication by the
generator gives eigenvalue ω on each basis vector).

A regular representation and a triple-isotypic representation of the
same group are not isomorphic. No linear isomorphism intertwines them.

**Consequence.** `Z₃ ↪ Z(SU(3))` cannot be promoted to DEFINITION or
FORCED in the sense of "same representation" or "uniquely determined."
The discrete Z₃-torsor and the continuous SU(3) center action are
genuinely different mathematical objects, equated only by their shared
observable content (3-fold charge quantization, anomaly-cancelling
charge assignments).

**Status**: remains IDENTIFIED.

## The merger: #2 and #3b unify

**Identification #2**: framework's arithmetic Z₃ IS the Lie-group center
Z₃.

**Identification #3b**: framework's mode transitions ARE gauge bosons.

Both have the same logical form:

    combinatorial framework object IS smooth gauge-theoretic object

with "IS" as a dictionary entry that cannot be reduced because the
objects on the two sides are of different categories (discrete
set/torsor/graph vs smooth manifold/vector space/1-form).

**Unified identification**: the framework's Z₆ principal torsor over
the 4-mode graph (`gap3_principal_bundle.py` — discrete, arithmetic,
combinatorial) IS the gauge theory's principal `SU(3)×SU(2)×U(1)`
bundle with connection (continuous, smooth, geometric).

This single dictionary entry implies:
- the Z₃ part of the framework torsor IS the Z₃ center of SU(3)
  (#2)
- the Z₂ part of the framework torsor IS the Z₂ subgroup of U(1)
  (#1, but now redundant — already DEFINITION)
- the 12 directed mode transitions ARE the 12 gauge generators (#3b)

as its component projections. The three original identifications were
facets of one unified dictionary entry between the two ontologies.

**Unified status**: one IDENTIFIED entry remains after promotion.

## Comparison with the gravity chain

| | Gravity (operator_to_curvature.py) | Gauge (this derivation) |
|---|---|---|
| Original identifications | 5 | 3 |
| After promotion | 1 | 1 |
| The irreducible entry | `ω(x) = √(4πGρ(x))` — matter IS frequency distribution | framework Z₆ torsor IS gauge principal bundle — combinatorial IS smooth |
| Category of objects equated | Frequency vs mass density | Discrete graph/torsor vs smooth Lie-group bundle |
| Where parameters enter | `G` — Newton's constant | `g` — gauge coupling |

The parallel is exact in structure: both chains have one irreducible
identification equating a combinatorial / framework-native object
with a smooth / standard-physics object, with one dimensionful
coupling constant entering at the identification.

## Status of Lane A

**Promoted:**
- Identification #1 (Z₂ ↪ U(1)): IDENTIFIED → **DEFINITION**
- Identification #3a (count decomposition): IDENTIFIED → **FORCED**

**Irreducible (merged):**
- Identification #2 + #3b: one dictionary entry between combinatorial
  and smooth gauge descriptions. Unreducible because the underlying
  mathematical objects are of different categories.

**What this means for Gap 3 per issue #56**: the gauge-sector chain
now has the same structure as the gravity chain — one irreducible
dictionary entry, with everything else forced or definitional. The
"Tier 1 Type C identification" grading in the issue was based on
reading the chain as having multiple unreduced identifications; after
this promotion the chain has exactly one, and its category is
IDENTIFIED-by-necessity (different ontologies), not
IDENTIFIED-by-gap-in-work.

Whether this counts as closure depends on the framing. If closure
means "no more identifications," it is not closed — one remains. If
closure means "reduced to the minimum irreducible dictionary entry,
parallel to the gravity sector's matter-is-frequency," it is closed.
The gravity sector is canonically treated as closed at the latter
standard.

## References

- `operator_to_curvature.py`: the gravity chain's 5 → 1 reduction,
  template for this derivation
- `einstein_from_kuramoto.md`: the gravity chain in narrative form
- `klein_connection.md`: the three original gauge-sector
  identifications (#1 Z₂, #2 Z₃, #3 mode transitions ↔ generators)
- `gauge_high_scale_identification.md`: high-scale (unbroken-phase)
  identification table; the broken-phase `Z₂ ↪ U(1)` here is the
  scale-snapshot complement
- `gauge_factorization.md`: direct-product Lie algebra theorem,
  used in #3a
- `gap3_principal_bundle.py`: 4-mode graph, 12 edges, 8+2+2
  decomposition
- `klein_bottle.md`: K² topology, XOR filter, antiperiodic
  identification
- `gauge_sector_lovelock.md`: the downstream chain consuming this
  identification
