# Observer-register closure on the Klein-quotient substrate

Formalize the notion of an observer-register as a closure
condition on Farey-level subsets of the Klein-quotient substrate.
Restate `R = 6·13⁵⁴` as the resolution of the canonical register,
then test whether this demotes H_0 from a Type 1 observational
anchor to a Type 2 ratio (register span × Planck unit) and
whether it closes the v/M_P gap from the cosmological side.

## 1. Definition — well-formed observer-register

Let `L = Z[i]` be the Gaussian integer lattice (complex structure
on the Klein bottle K² = S¹ ×_{Z₂} S¹), and let
`z₀ = q₂ + i q₃ = 2 + 3i` be the canonical Gaussian integer
built from the framework's two denominator classes.

**Definition (observer-register).** A set `S ⊆ L` is a
*well-formed observer-register at depth k* (for a non-negative
integer k ≤ q₂ · q₃^d = 54) if it is closed under three
operations:

- **(O1) Gauge-center closure.** Closed under the action of the
  gauge center Z₆ = Z_{q₂·q₃}: if `w ∈ S` then `ζ·w ∈ S` for
  every ζ ∈ Z₆ acting on L by its canonical embedding in
  U(1) ⊂ GL(L).
- **(O2) Klein-antipodal closure.** Closed under the Z₂ quotient
  ι: `w ↦ w̄` (complex conjugation ≡ the Klein-antipodal
  involution on the spinor bundle, per
  `baryon_fraction.md` and `klein_antipodal_z2_rep_pattern.md`).
- **(O3) Gaussian-norm closure to depth k.** For each `w ∈ S`
  and each integer `j` with `0 ≤ j ≤ k`, the point `z₀^j · w`
  is in S.

Equivalently: `S` is a union of orbits of the group
`Z₆ × ⟨z₀⟩_k × ⟨ι⟩` acting on L, where `⟨z₀⟩_k = {z₀^0, …, z₀^k}`.
"Well-formed at depth k" bounds the orbit depth by k.

**Resolution of the register.** The resolution `|S|` counts the
distinct states the observer can resolve. For the minimal
well-formed register at depth k containing a single base point
`w₀` not fixed by any sub-action,

    |S(k)|  =  |Z₆| · (k+1) · [Z[i] : z₀^k Z[i]]      (before Klein quotient)
            =  6 · (k+1) · 13^k                         (using N(z₀) = 13)

After taking the Klein quotient (identifying `w ∼ ι(w) = w̄`),
each non-real orbit halves; at depth k the number of halved
orbits is 13^k (the full lattice layer at depth k), leaving

    |S(k)| / ~  =  6 · 13^k                             (at the k-th lattice layer,
                                                         real + complex-pair count)

The `k+1` pre-factor and the halving under Klein quotient
cancel the linear depth count; what remains is the layer index
`13^k` weighted by the gauge multiplicity 6. The number of
*distinguishable states at exactly depth k* is `6 · 13^k`.

## 2. Derivation — R = 6 · 13⁵⁴ as register resolution

**Lemma (exhaustion depth).** The maximal depth at which the
register remains well-formed without duplication is `k = 54`:

- At each depth step, `z₀·` multiplies the sublattice index by
  13 (`hierarchy_gaussian_lattice.md` §2). No duplication within
  a single gauge-cell pass.
- The gauge center Z₆ has 6 elements. Each depth step consumes
  one "gauge label" from the stratification
  `54 = q₂·q₃^d = 2·27`, where 27 is the q₃-duty-cycle
  stratification (from `duty_cycle_dictionary.md` Part I,
  proof-preserved) and 2 is the Z₂ non-orientable doubling.
- After 54 steps, every gauge cell has been visited exactly
  once: one complete pass through phase space. Step 55 would
  require a second independent Z₆ label — not available
  (`hierarchy_gaussian_lattice.md` §4).

Therefore the *canonical* register — the unique well-formed
register that exhausts the Klein bottle's gauge stratification
without over-counting — has depth `k = 54`, and resolution

    R  =  |canonical register|  =  6 · 13⁵⁴            (*)

This matches the Planck/Hubble hierarchy derivation in
`hierarchy_gaussian_lattice.md`. The only contribution of this
file is to recast `R` as the *resolution of a register* rather
than as a sublattice index: the two are mathematically
equivalent (both equal `|Z₆| · N(z₀)^{q₂·q₃^d}`) but the
register framing makes explicit what kind of object it counts.

## 3. Attempt — demote H_0 from Type 1 to Type 2

**Claim under test.**
`H_0  =  (register span)⁻¹ × (Planck unit)⁻¹  =  1 / (R · t_P)`,
making H_0 a register-intrinsic ratio rather than an
observational anchor.

**What succeeds.** The *dimensionless* part is register-intrinsic:

    t_H / t_P  =  R  =  6 · 13⁵⁴

is derived from `(q₂, q₃, d)` without observational input. The
hierarchy *ratio* was already register-intrinsic in
`hierarchy_gaussian_lattice.md`; the register framing does not
change that.

**What fails.** The *absolute* scale of either `t_P` or `t_H`
still requires a dimensionful input:

1. The register counts states; it does not carry units. `R` is
   a pure number.
2. `t_P = √(ℏG/c⁵)` requires `ℏ`, `G`, `c`. In natural units
   (`ℏ = c = 1`), `t_P = √G`. `G` is dimensionful and the
   framework does not supply its value from register structure.
3. The Planck unit is therefore *itself* an anchor, not a
   substrate-intrinsic constant. Its absolute value is fixed by
   the choice of `H_0` (via `t_P = t_H / R`) or by the choice of
   `M_P` (via `M_P = 1/ℓ_P = R/L_H`).

Under the register framing, the content is:

    pick any one of {H_0, Λ, ℓ_P, M_P, t_P};
    the register R determines all the others via pure ratios.

This is exactly the existing Type 1 / Type 2 structure from
`anchor_count_audit.md`. The register formalism *restates*
the single-cosmological-anchor condition without reducing it.
H_0 does not get demoted: it (or any equivalent) remains a
Type 1 anchor because the register alone supplies no absolute
time or length unit.

**Status of this attempt:** null. The dimensionless hierarchy
was already register-intrinsic; the absolute scale remains
anchor-dependent. Obstruction #4 of `anchor_count_audit.md`
("coordinate/frame decomposition not established") is
re-expressed more sharply — the register *is* the frame; it
does not supply coordinates on its own — but not resolved.

## 4. Attempt — close v/M_P from the register's cosmological side

**Claim under test.** If the register has a stratification of
54 levels, each contributing a factor `13`, then v/M_P sits at
some level `ℓ` with `v/M_P ≈ 13⁻ℓ`. A structural argument
identifying ℓ would close v/M_P and reduce the anchor count.

**Numerical fact.** `log_{13}(v/M_P) = −14.988`, closest integer
`ℓ = 15`. Near-match `13⁻¹⁵ = 1.95·10⁻¹⁷` vs `v/M_P = 2.02·10⁻¹⁷`,
residual 3.1%. Already logged as Class 2 in
`numerology_inventory.md`.

**Ansatz-audit triage** (per `ansatz_audit_policy.md`).

*Step 1 — enumerate alternatives.* Adjacent depths:
- ℓ = 14: `13⁻¹⁴ = 2.54·10⁻¹⁶`, off by factor 12.6 (~1160% miss).
- ℓ = 15: 3.1% miss (the candidate).
- ℓ = 16: `13⁻¹⁶ = 1.50·10⁻¹⁸`, off by factor 0.075 (~93% miss).

Only ℓ = 15 is a viable integer. That narrows the selection,
but the question is whether ℓ = 15 is *forced* from the
register's structure.

*Step 2 — forcing argument for ℓ = 15.* Enumerate
framework-integer expressions evaluating to 15:

| Expression | Value | Note |
|---|---|---|
| `q₃·(q₂ + q₃)` | `3·5 = 15` | clean; but `q₂ + q₃ = 5` is not register-native |
| `q₂·q₃ + q₃²` | `6 + 9 = 15` | gauge count + spatial-dim square |
| `(q₂² + q₃²) + q₂` | `13 + 2 = 15` | Gaussian norm + q₂ |
| `q₃·d + q₃² − q₂² + q₂` | `9 + 9 − 4 + 2 = ...` wait, = 16 | close but not exactly 15; illustrates easy over/under-fit |

Multiple framework-integer expressions yield 15, none forced by
register structure. The depth 54 admits a natural
`54 = 6 · 9 = |Z₆| · q₃²` block decomposition (six cycles of
nine steps each). In that decomposition, the depth-15 label
would need to land at a specific position within the
stratification — e.g., `15 = q₃² + q₂·q₃` as "one complete
`q₃²`-cycle plus a gauge-prefactor offset." This is
constructible but not forced.

*Step 3 — contrast with positive pattern.* The canonical
derivations that pass Z1-Z3 on the Klein substrate (Ω partition
13:5:1/19, down-type factor 6, up-type factor 9) all force their
specific integer from the Klein-antipodal Z₂ rep machinery
(`klein_antipodal_z2_rep_pattern.md`) — a theorem that
decomposes each antipodal pair into sym/antisym eigenmodes of
specific count. The register's depth-15 identification has no
analogous decomposition theorem: there is no sub-orbit of
length 15 in the Z₆ × ⟨z₀⟩₅₄ × ⟨ι⟩ action that is forced to
correspond to the electroweak scale.

*Step 4 — default verdict.* Class 2. The depth-15 match is a
near-coincidence; the framework-integer expression evaluating to
15 is an ansatz selected because the observation sits near
`13⁻¹⁵`.

**Status of this attempt:** null. The register framework
exposes the depth-stratification question cleanly but supplies
no forcing argument for depth 15 (or any specific depth) for
v_EW. Obstruction #2 of `anchor_count_audit.md` ("no Fibonacci-
depth count for the electroweak hierarchy") is re-expressed in
register-intrinsic terms — "no forced register-depth label for
v_EW" — but not resolved.

## 5. Consequences

**What this derivation supplies.**

- A formal closure condition for observer-registers on the
  Klein-quotient substrate (§1).
- A restatement of `R = 6·13⁵⁴` as register resolution rather
  than as sublattice index (§2). Mathematically equivalent, but
  register framing is structurally explicit about the kind of
  object R is.
- A sharper expression of the two outstanding obstructions to
  anchor-count reduction: the register supplies dimensionless
  ratios but no absolute unit (§3), and no forced depth label
  for v_EW (§4).

**What this derivation does not supply.**

- A reduction of the anchor count from 2 to 1. The register
  framing does not demote H_0 to a Type 2 ratio; it only
  restates the existing single-cosmological-anchor picture.
  The *absolute* time (or length, or mass) unit remains a
  Type 1 anchor choice.
- A structural closure of `v/M_P`. The depth-15 match retains
  its Class 2 status. The register formalism does not force
  depth 15.

**Canonical statement.** After this derivation, the framework's
anchor count is unchanged at two (H_0 cosmological, v_EW
particle-sector). The register formalism is adopted as the
preferred language for stating the dimensionless hierarchy —
`R = 6·13⁵⁴` is the resolution of the canonical well-formed
observer-register at maximal depth 54 — but the two-anchor
minimum stated in `anchor_count_audit.md` stands.

## 6. What would close the hierarchy in register terms

For the anchor count to reduce to one via the register, one of
the following would need a structural derivation:

A. **Substrate-intrinsic Planck unit.** A theorem showing that
   the canonical register's step size carries an absolute time
   (or length) unit from the Klein substrate's own geometry —
   not from a chosen anchor. Currently no such unit is supplied
   by O1-O3; all that is supplied is a dimensionless count.

B. **Forced depth identification for v_EW.** A theorem giving
   a specific well-formed sub-register at depth `ℓ` with
   `ℓ ∈ {14, 15, 16}` as the unique register compatible with
   the electroweak sector's Klein-antipodal Z₂ rep structure.
   Same pattern as the 13:5:1/19 closure at ℓ = 7 (Farey
   depth 7, count 19), but for the Planck-to-EW scale gap.
   The closest near-match is ℓ = 15 at 3.1% residual, but no
   forcing argument is available (§4).

C. **Cross-sector register identity.** A theorem exhibiting a
   single well-formed register whose stratification simultaneously
   counts cosmological states (up to depth 54) and particle-
   sector states (at depth 15-ish), with the ratio between them
   forced to equal `v/M_P`. The cosmological and particle
   sectors currently close separately (`coupling_scales.md`,
   `baryon_fraction.md`, `hierarchy_gaussian_lattice.md`); no
   shared register has been constructed.

None of A, B, C are supplied by the register formalism alone.
Each is a structural open item and sits as an obstruction.

## 7. Cross-references

| File | Role |
|---|---|
| `hierarchy_gaussian_lattice.md` | R = 6·13⁵⁴ as sublattice index (equivalent derivation) |
| `anchor_count_audit.md` | Two-anchor minimum; five obstructions |
| `ansatz_audit_policy.md` | Triage applied to depth-15 v/M_P closure |
| `klein_antipodal_z2_rep_pattern.md` | Positive structural pattern (Z₂-rep forcing) |
| `numerology_inventory.md` §Class 2 | v/M_P ≈ 13⁻¹⁵ logged here |
| `duty_cycle_dictionary.md` | q₃²-stratification component (27 cells) |
| `baryon_fraction.md` | Klein-antipodal Z₂ rep machinery on coprime pairs |
