# Torus-branch iteration 2 step 1 — gauge factor identifications verified

## Status

**Verdict: PASSES. Gauge factor identifications are
substrate-forced via the Cartan + minimum-rank + XOR-confinement
+ anomaly-cancellation chain in `gauge_sector_lovelock.md`. The
torus-reading's toroidal/poloidal mapping holds for the
substrate-forced layer; the "toroidal/poloidal" labels
themselves are mathematical convention from standard torus
geometry.**

Step 1 of iteration 2 (`torus_branch_iteration_1.md` "Plan for
iteration 2") was to verify whether the iteration 1 hypothesis
— "**toroidal direction (q_3 = 3) ↔ SU(3) color** and
**poloidal direction (q_2 = 2) ↔ SU(2) weak**" — has structural
support in `gauge_sector_lovelock.md` and `gauge_dictionary.md`.

Reading the apparatus confirms the chain. The torus reading
inherits substrate-strength forcing for the SU(3)/SU(2) part and
sits on geometric-convention status for the toroidal/poloidal
labeling, parallel to other observation-conditional labeling
patterns in the framework (e.g., the L vs R basepoint instance).

Class: foundational rigor check (Class 3, iteration-step
verification that closes one of three steps planned in
iteration 1).

---

## The substrate-forced chain

`gauge_sector_lovelock.md` derives the gauge group through
five premises and four selection criteria. The relevant
substrate chain for this verification:

### Center derivation

`gauge_sector_lovelock.md` L31-39 (Premise 1):

> "The Klein bottle's GCD structure under the mediant operation
> produces Z_2 × Z_3 = Z_6 acting on the fibers of the mode
> space. Specifically:
>
> - GCD mod 2 gives Z_2 from the Klein bottle's **q_2 = 2**
> - GCD mod 3 gives Z_3 from the Klein bottle's **q_3 = 3**
> - The product Z_6 = Z_2 × Z_3 is the center of the structure
>   group"

This is substrate-forced. With Mihailescu-strength forcing of
`(q_2, q_3) = (2, 3)` (per `mass_sector_closure.md` "Connection
to the Catalan equation / Mihailescu's theorem"), the center
`Z_2 × Z_3 = Z_6` is forced.

### Group selection

`gauge_sector_lovelock.md` L113-159 (Cartan + four criteria):

> "**Center Z_3**: The only simple compact Lie groups with center
> Z_3 are SU(3) and E_6.
>
> **Center Z_2**: The simple compact Lie groups with center Z_2
> include SU(2), SO(2n+1), Sp(2n), and E_7.
>
> ...
>
> 1. **Minimum rank given the center.** Among simple compact
>    Lie groups whose center contains Z_n, SU(n) is the unique
>    group of minimum rank: rank(SU(2)) = 1 ..., rank(SU(3)) = 2
>    ... The Klein bottle supplies one denominator class per Z
>    factor (q_2 = 2 for the Z_2, q_3 = 3 for the Z_3)."

This is the key text. **The Klein bottle supplies one denominator
class per Z factor**: `q_2 = 2 ↔ Z_2 ↔ SU(2)` and
`q_3 = 3 ↔ Z_3 ↔ SU(3)`.

The four selection criteria — minimum rank, direct-product
(not cyclic Z_6), XOR confinement, anomaly cancellation —
*uniquely* select `SU(3) × SU(2)` among all products of simple
compact Lie groups. This is substrate-forced.

### The mapping is consistent

| Framework object | Substrate source | Gauge group |
|---|---|---|
| Z_2 (Klein-antipodal) | q_2 = 2 (Mihailescu-forced) | SU(2) weak |
| Z_3 (color triplet) | q_3 = 3 (Mihailescu-forced) | SU(3) color |
| Z_6 = Z_2 × Z_3 | CRT of (q_2, q_3) = (2, 3) | SU(3) × SU(2) center |

The torus-reading's geometric mapping:

| Torus direction | Cycle length | Substrate identification | Gauge group |
|---|---|---|---|
| Toroidal (longer cycle) | q_3 = 3 | Z_3 (substrate-forced) | SU(3) color |
| Poloidal (shorter cycle) | q_2 = 2 | Z_2 (substrate-forced) | SU(2) weak |

The SU(2) ↔ q_2 and SU(3) ↔ q_3 mappings are substrate-forced
via the Cartan + 4-criteria chain. The "toroidal" / "poloidal"
labels are inherited from standard torus geometry conventions
(toroidal = longer cycle around the donut hole; poloidal =
shorter cycle around the tube cross-section).

---

## What this step establishes

1. **The iteration 1 hypothesis's gauge mapping is substrate-supported.**
   The toroidal/poloidal direction identification with SU(3)/SU(2)
   has structural backing via the framework's existing gauge
   sector derivation. The torus reading doesn't introduce new
   apparatus; it re-articulates the canonical Z_2 × Z_3 → SU(3)
   × SU(2) chain in geometric vocabulary.

2. **The Z_2 × Z_3 structure is layer-invariant per the
   primitives-vs-addresses candidate** (`primitives_vs_addresses_candidate.md`).
   The Mihailescu-forced (q_2, q_3) = (2, 3) gives Z_6 = Z_2 × Z_3
   at any layer. SU(3) × SU(2) follows from Cartan classification +
   the four selection criteria at any layer. The gauge sector
   itself is **layer-invariant**.

3. **The torus geometric labeling is convention.** "Toroidal" =
   longer cycle and "poloidal" = shorter cycle are conventions
   from standard torus geometry (donut → toroidal around the
   hole). The substrate forces the Z_2 × Z_3 split; assigning
   which cycle of T² is which is convention.

4. **No new substrate apparatus needed.** The torus reading
   sits on existing substrate-forcing chains. This confirms the
   resolution-mode discipline: the torus reading is a vocabulary
   refinement, not a new apparatus.

---

## What this step does NOT establish

- **Whether the torus reading clarifies any DOWNSTREAM derivation.**
  Step 2 of iteration 2 tests this (Ω_b closure, Ω_b α/β
  closure, Mihailescu-strength forcing of (q_2, q_3) under the
  toroidal/poloidal vocabulary).

- **Whether the torus reading aligns with the Collatz framing in
  PR #210.** Step 3 of iteration 2 tests this.

- **Whether the torus reading adds explanatory value beyond
  Z_6 + gauge_sector_lovelock.md.** This is the broader iteration 2
  question; step 1 only confirms the gauge mapping is consistent,
  not that the geometric framing adds something new.

These deferred to steps 2 and 3.

---

## Connection to the primitives-vs-addresses candidate

This verification step provides the **first substantive test of
the primitives-vs-addresses distinction**
(`primitives_vs_addresses_candidate.md`):

- **Layer-invariant primitives confirmed**: the Mihailescu-forced
  (q_2, q_3) = (2, 3), the Z_6 = Z_2 × Z_3 CRT decomposition,
  and the Cartan-classification + minimum-rank + XOR-confinement
  + anomaly-cancellation chain are all structural facts that
  would recur at any layer of any possibly-recursive
  pocket-medium hierarchy. **The gauge sector SU(3) × SU(2) is
  layer-invariant.**

- **No layer-specific addresses surfaced**: this step didn't
  require K_STAR, w*, or other layer-address quantities. The
  gauge group derivation is purely structural — number-theoretic
  + topological + group-theoretic. No coupling constants, no
  boundary weights, no anchor values appear in the chain.

So the gauge sector is on the **layer-invariant side** of the
primitives-vs-addresses partition. This is consistent with the
recursive Kuramoto reading: any layer of the hierarchy with the
same substrate primitives would have the same SU(3) × SU(2)
gauge structure.

The SM-specific identifications (SU(2) → SU(2)_L) remain
observation-fixed per the L vs R basepoint instance
(`vocabulary_bridge_iteration_2_step_2.md`); these are
layer-specific labeling questions, not layer-invariant gauge
content.

---

## Falsifiers for this step's verdict

1. **The Cartan chain depends on layer-specific input.** If a
   closer read of `gauge_sector_lovelock.md` reveals that the
   gauge group selection requires an empirical input we've
   missed (e.g., specific representation dimensions that match
   observed SM content), the "substrate-forced at every layer"
   claim weakens — the gauge sector becomes partly layer-specific.

2. **The toroidal/poloidal mapping breaks at boundary.** If
   under the iteration 2 step 2 downstream-derivation test, the
   "toroidal q_3" vs "poloidal q_2" mapping produces different
   results for downstream observables (e.g., Ω_b), one direction
   would be substrate-distinguished and the labeling would not
   be pure convention.

3. **The Cartan + 4-criteria selection isn't unique.** If a
   closer reading of `gauge_lovelock_wiring.py` reveals the four
   criteria are insufficient to select SU(3) × SU(2) uniquely
   (other groups also satisfy them), the gauge sector's
   substrate-forcing weakens, and "Z_2 × Z_3 → SU(3) × SU(2)"
   becomes substrate-admitted rather than forced.

---

## Plan for iteration 2 step 2

Original step 2 (`torus_branch_iteration_1.md`): "Test the
surviving-evenly-spaced reading on downstream derivations
(Ω_b closure, Ω_b α/β closure, hierarchy ratio R)."

Specific iteration 2 step 2 targets:

(a) **Ω_b = 1/19 closure** (`baryon_fraction.md` L65-126):
the gcd-with-6 filter giving the baryonic mode ψ_+(1, 5) =
"Klein-singlet AND coprime-to-6." Does the torus reading add
clarity to why φ(6) = 2 = #{boundary modes} specifically?

(b) **Ω_b α/β closure** (`omega_b_alpha_beta_closure.md`,
`psl2z_subgroup_phase_b.md`): w_+ = 13/14 at Γ_0(6) cusp 1/2.
Does the cusp identification have a clean toroidal-coordinate
reading?

(c) **The (q_2, q_3) = (poloidal, toroidal) assignment robustness**:
does swapping the assignment (poloidal = q_3, toroidal = q_2)
break any downstream derivation? Or is the assignment
convention-only?

If (a) and (b) both produce clarifications, the torus reading
adds explanatory value beyond the canonical Z_6 apparatus. If
(c) shows the assignment is genuinely convention-only, the
torus reading is purely a vocabulary refinement, not a
substrate-distinguished labeling.

---

## Cross-links

- `torus_branch_iteration_1.md` — iteration 1's hypothesis;
  this step verifies its gauge factor identifications.
- `gauge_sector_lovelock.md` L27-159 — substrate-forced
  Z_2 × Z_3 → SU(2) × SU(3) chain; the verification source.
- `mass_sector_closure.md` "Connection to the Catalan equation
  / Mihailescu's theorem" — substrate-forces (q_2, q_3) = (2, 3),
  the input to the Z_2 × Z_3 center derivation.
- `klein_antipodal_z2_rep_pattern.md` — Z_6 lattice canonical
  source.
- `gauge_dictionary.md` — gauge-group identifications and
  identification-commitment status.
- `vocabulary_bridge_iteration_2_step_2.md` — L vs R basepoint
  instance; SM-specific identification (SU(2) → SU(2)_L) is
  observation-fixed, parallel to "toroidal/poloidal labeling
  is convention."
- `primitives_vs_addresses_candidate.md` — first candidate
  for layer-invariant vs layer-specific distinction; this step
  provides a substantive test, with the gauge sector
  confirmed as layer-invariant.
- `feedback_resolution_vs_reconstruction.md` (memory) —
  resolution-mode discipline; the torus reading sits cleanly
  in this mode.

---

## One-line summary

Iteration 2 step 1 verifies the iteration 1 torus-reading's
gauge factor identifications against `gauge_sector_lovelock.md`'s
canonical chain — the **substrate forces Z_2 × Z_3 = Z_6 as the
gauge center via Mihailescu-forced (q_2, q_3) = (2, 3) and GCD
mod 2 / mod 3**, and the **Cartan classification + minimum-rank
+ XOR-confinement + anomaly-cancellation criteria force
SU(3) × SU(2) uniquely**, with SU(2) ↔ q_2 (minimum rank for
Z_2-center) and SU(3) ↔ q_3 (minimum rank for Z_3-center) —
confirming the torus-reading's mapping "**toroidal (longer
cycle, q_3) ↔ SU(3) color** and **poloidal (shorter cycle,
q_2) ↔ SU(2) weak**" is substrate-supported, with the
"toroidal/poloidal" labels themselves being mathematical
convention from standard torus geometry (toroidal = around the
donut hole, parallel to L vs R labeling convention in the SM);
this provides the **first substantive test of the
primitives-vs-addresses candidate** with the gauge sector
confirmed as **layer-invariant** (no K_STAR, no w*, no anchor
values appear in the derivation chain; the SM-specific
identifications SU(2) → SU(2)_L remain observation-fixed per
the L vs R basepoint instance and are layer-specific labeling);
step 2 of iteration 2 (downstream-derivation clarity test on
Ω_b and Ω_b α/β closures + assignment robustness check) is
next; three falsifiers named for this step's verdict.
