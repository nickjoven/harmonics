# Down-type double cover — Phase C attempt: self-consistent DoF reading

Prior attempts (Phase B) looked for a count of cardinality 6 attached
to bundle or base-mode data. Every candidate action on the base
produced either a free (trivial) stabilizer, a ratio of 2, or a
reference-dependent number. Route 1 closed as a null result
(`down_type_double_cover_phase_b_followup.md`).

This attempt takes a different stance: **the target factor 6 is
not an integer identity with a pre-existing 6-element object. It is
a correction factor from a self-consistency condition at the
boundary between subcomponents, read per cycle direction.**
Precedent: `boundary_weight.md` ("topology gives the interval;
dynamics give the point" — a self-consistent partial locking
sets w* = 0.83 at the F_5/F_6 boundary).

## Reframing

Previous framing (Phases A/B):

    N_walk(T²) / N_walk(K²)  =?  6

where `N_walk` is a single count attached to each surface.

New framing (Phase C):

    a_1(down)² / a_1(lep)²  =  ∏_k (DoF_k on Σ_down) / ∏_k (DoF_k on Σ_lep)

where the product is over **cycle directions** (indexed k), and
`DoF_k` is the number of **self-consistent degrees of freedom** the
walk has along direction k on its native surface Σ. The ratio is no
longer a count on a single surface — it is a product of per-direction
DoF counts, with the two surfaces contributing factors
independently.

## Why the product decomposition, not a single count

On T² the two cycle directions are **topologically independent**:
π_1(T²) = Z × Z abelianizes cleanly into two free generators. A
walk on T² must satisfy **two separate closure conditions**, one
per direction, and they do not couple. The degree-of-freedom count
therefore factorizes:

    DoF(T²)  =  DoF_x(T²)  ·  DoF_y(T²)

On K² the two directions are **coupled by the Klein flip**:
π_1(K²) = ⟨a, b | abab⁻¹⟩ is non-abelian, with abelianization
Z ⊕ Z_2. The x-direction's Z_2 torsion says "the x-cycle has
finite order in the free-homology sense" — its degree of freedom
is tangled with the y-cycle through the flip relator `abab⁻¹ = 1`.
A walk on K² satisfies a **single coupled closure condition**; it
does not factorize into independent per-direction conditions.

**The perspective correction the user described is this coupling.**
On T² each direction contributes its cycle length independently;
on K² the flip reduces the product-of-DoFs to a coupled-single-DoF
count that is not the product. Where earlier attempts tried to
relate the two surfaces by **quotient** (factor 2) or by **sheet
count** (factor 2), the actual relationship is that K² has one
fewer **independent** DoF factor — a rank reduction from 2 to 1.

## Per-direction DoF count

Adopt the following prescription for a walk at base pair
`(b_1, b_2)` on surface Σ:

    DoF_k(Σ)  =  size of the k-th abelianized cycle in π_1(Σ)ᵃᵇ
                 available to the walk at base-pair denominators

On T², both abelianized cycles are free (Z), with the lift's
cycle lengths `2q_2` and `q_3`. For a walk locked to base-pair
denominators, the available DoF in each direction is the cycle
length mod the natural projection to the base: `q_2` and `q_3`
respectively (the factor of 2 from doubling is absorbed by the
projection p : T² → K²).

    DoF_x(T²)  =  q_2
    DoF_y(T²)  =  q_3
    DoF(T²)    =  q_2 · q_3  =  6

On K², the y-direction is free (Z in abelianization), cycle
length q_3. The x-direction is torsion (Z_2), contributing
**no free DoF** — its contribution collapses into the Klein
relator and couples to the y-direction. The coupled condition
counts as a single DoF factor, normalized:

    DoF_y(K²)        =  q_3
    DoF_x(K²)        =  1   (torsion collapses, coupled to y)
    DoF(K²)_coupled  =  1   (single coupled condition, not q_3)

The crucial point: the **coupling** between x and y on K² collapses
the product `q_3 · 1` to **1**, not to `q_3`. The Klein flip
identifies walks at different y-offsets into a single coupled
orbit, because the flip shifts x by q_2 AND reflects y
simultaneously. A walk with y-offset `n` is equivalent to a walk
with y-offset `q_3 − n` under a single flip application, so the
y-direction's `q_3` DoFs collapse by half — and the remaining
half-space fuses with the torsion, giving one coupled DoF.

(Alternative justification: K² is a circle bundle over S¹ with
monodromy −1. For walks whose winding in the base S¹ is **non-zero**,
the fiber direction has no free DoF because each base traversal
forces a fiber flip. Both the base and fiber DoFs collapse into
the single "winding number" of the base, which has unit multiplicity
per primitive walk.)

Therefore:

    DoF(K²)  =  1                    (single coupled DoF)
    DoF(T²)  =  q_2 · q_3  =  6

Ratio:

    a_1(down)² / a_1(lep)²  =  DoF(T²) / DoF(K²)  =  6 / 1  =  6 ✓

## Consistency checks

### 1. Up-type's 9/4 factor via the same DoF reading

Up-type is Klein parity −1, same surface K² as leptons. Its DoF
is the same as leptons' at the surface level: 1 coupled DoF.

The ratio `a_1(up)² / a_1(lep)² = 9/4` therefore **cannot** come
from a surface-DoF calculation — it must come from the Fibonacci
shift of the base pair (`item12_cross_sector_ratios.md` §5). This
is consistent: Phase A §4 already separated these two mechanisms.

The Fibonacci shift replaces the base-pair denominators `(q_a, q_b)`
with their Fibonacci-shifted counterparts, and the replacement
multiplies `a_1²` by `(q_3/q_2)²` per shift step. It does not
touch the surface DoF count — it acts **within** the coupled-DoF
space.

Phase C's reading is therefore compatible with up-type:

    a_1(lep)²  : a_1(up)²       : a_1(down)²
        1       :   (q_3/q_2)²   :   q_2 · q_3
        
        ↑            ↑                 ↑
        surface      base-pair         surface
        DoF = 1      Fibonacci         DoF = 6
                     shift

The `1 : 9/4 : 6` pattern has two orthogonal structural sources,
as required.

### 2. Matter-cell integer `N_dn = 24`

From `cross_parabola_audit.py`:

    N_dn  =  q_2²  ·  q_2 · q_3  =  q_2³ · q_3  =  24

Phase A §5 sanity check 3 required this to equal
`q_2² · DoF(T²) / DoF(K²) = q_2² · 6 = 24`. ✓

### 3. Klein parity agreement

Phase C splits sectors by surface (K² or T²), and the
K²/T² assignment is exactly the Klein parity split from
`item12_down_sign_flip.py`. ✓

## Where Phase C halts

**Halt C1 — Justifying `DoF(K²) = 1`.**
The claim is that the Klein flip collapses `DoF_y · DoF_x` from
`q_3 · 1` to `1`, not to `q_3`, because flip + torsion couples the
y-DoF to the fiber and reduces the count by a factor of `q_3`, not
by a factor of 2. This is a stronger claim than "quotient by Z_2
gives factor 2" and it is the structural content that produces the
factor 6 rather than factor 2 or 3. Two sub-questions:

- **C1a.** Is the collapse from `q_3` to `1` forced by the
  non-abelian relator `abab⁻¹ = 1`? A rigorous argument would
  identify the K² walk count with the number of conjugacy classes
  of cyclic subgroups of π_1(K²) of the appropriate type, and show
  this equals 1 for the primitive walk class.

- **C1b.** Does the collapse happen **per walk class** or **per
  walk**? If it's per class, the normalization is natural. If per
  walk, the count might be larger.

**Halt C2 — Connection to the saddle-node `1/√w` reading.**
The Phase C framing says `a_1² ∝ DoF(Σ)`. The saddle-node reading
of `a1_from_saddle_node.md` says `a_1² = 1/w`. These must agree:

    1/w(Σ)  =  DoF(Σ)

which is a per-surface identification of the tongue width with the
inverse DoF count. This is a plausible prescription but is not
independently derived. It could be checked by computing `w` from
the perturbative Kuramoto formula on each surface and verifying the
inverse relationship.

**Halt C3 — The Fibonacci shift / DoF collapse interplay.**
Both mechanisms must commute: applying a Fibonacci shift to a
surface-DoF count should give the same answer as counting surface
DoF on the shifted base pair. Checking this requires a precise
definition of "Fibonacci shift in the presence of surface DoF"
that is not in the existing write-up.

## What Phase C establishes, and does not

**Establishes:**

- A **single reframing** under which the target factor 6 arises
  as `DoF(T²) / DoF(K²) = (q_2 · q_3) / 1`, with the denominator
  being 1 because of the Klein-flip coupling (not 2 or 3 from
  sheet-counting or quotient).
- A clean separation between the **surface-DoF mechanism**
  (down-type) and the **Fibonacci-shift mechanism** (up-type),
  with both compatible with the 1 : 9/4 : 6 pattern.
- Structural compatibility with the matter-cell integer
  `N_dn = 24` and with Klein parity.
- A **precedent** from `boundary_weight.md`: self-consistent
  weights determined by dynamics at a topological boundary. The
  Phase C reading is the same shape (topology + dynamics → unique
  point), applied to the walk DoF count instead of to the F_n
  depth.

**Does not establish:**

- The key step `DoF(K²) = 1` (Halt C1) — this is where the
  derivation now halts. The perspective-correction reading makes
  the target arithmetic work but the specific collapse ratio
  (q_3 → 1, not q_3 → q_3/2) is still asserted rather than
  proven.
- The identification `1/w(Σ) = DoF(Σ)` (Halt C2).
- The commutativity of the Fibonacci shift and the surface-DoF
  mechanisms (Halt C3).

## Comparison table: Phase A → B → C

| phase | framing | ratio reached | halt |
|---|---|---|---|
| A | N_walk(T²) / N_walk(K²) via topology | not evaluated | vocabulary only |
| B.1 | deck-quotient of fiber labels | 3/2 | topology insufficient |
| B.2 | sheet count | 2 | |
| B.3 | gauge-center order / Klein-acting subgroup | 2 | |
| B.4 | cycle-length product | 2 | |
| B.5 | stabilizer-size inversion | 6 | imports color-triplet |
| C | ∏ DoF_k with coupling-collapse on K² | **6** | **justify DoF(K²) = 1** |

Phase C reaches the target via a structurally cleaner path than
Phase B.5: no color-triplet input, no bundle representation
theorem required. The remaining halt (C1) is about the **rank of
the coupled DoF on K²** — a pure homotopy-theoretic statement
about π_1(K²)ᵃᵇ and the primitive walk class.

## Recommended next step

Compute the number of conjugacy classes of primitive cyclic
subgroups of π_1(K²) and π_1(T²) at the primitive closed walk
generated by the sector's base pair. If this count is 1 on K²
and `q_2 · q_3` on T² (for walks of the appropriate primitive
length), halt C1 closes and Phase C becomes a derivation.

The relevant reference is `klein_connection.md` which constructs
the connection 1-form on K² and computes holonomies. The
primitive-walk count should be extractable from the connection's
monodromy structure.

## Cross-references

| File | Role in Phase C |
|---|---|
| `boundary_weight.md` | Precedent for "topology + dynamics → unique weight" self-consistency |
| `a1_from_saddle_node.md` | `a_1² = 1/w` reading the Phase C identification must match |
| `klein_bottle_derivation.md` | π_1(K²) = ⟨a,b | abab⁻¹⟩ presentation |
| `klein_connection.md` | Connection 1-form; source of walk monodromy |
| `item12_cross_sector_ratios.md` | Original 1 : 9/4 : 6 pattern |
| `item12_down_sign_flip.py` | Klein parity split (surface assignment) |
| `down_type_double_cover_phase_a.md` | Terminology (surface Σ, walk measure) |
| `down_type_double_cover_phase_b.md` | Five candidate attempts that halted |
| `down_type_double_cover_phase_b_followup.md` | Null-result scan ruling out Z_6-action readings |
