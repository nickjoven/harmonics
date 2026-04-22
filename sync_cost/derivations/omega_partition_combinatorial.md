# Ω partition: combinatorial derivation at depth 19

## Scope

Derive the cosmic energy partition Ω_Λ : Ω_DM : Ω_b = 13 : 5 : 1 at
the Klein bottle's Farey depth q_2·q_3 + 1 = 7. Both halves of the
partition (Ω_Λ : Ω_m = 13 : 6 and Ω_b : Ω_DM = 1 : 5) are derived
combinatorially from the Klein bottle's Z₂ torsion (H₁(K²; Z) =
Z ⊕ Z₂) plus the EM-coupling criterion of `gell_mann_nishijima.md`.

## Result summary

| Split | Status | Mechanism |
|---|---|---|
| Ω_Λ : Ω_m = 13 : 6 | **Derived** | `|F_6|` vs `φ(7)` Farey count |
| Ω_b : Ω_DM = 1 : 5 | **Derived** | Z₂ representation theory on coprime-pair antisym mode + EM-coupling criterion |

The previous Proposed-item framing ("XOR-parity proof of 1:5:13 at
depth 19") was wrong on two counts: XOR-parity (from
`xor_derivation.md`) operates on mode pairs (q_1, q_2), not on
single-fraction subdivision; and the actual 1:5 mechanism is Z₂
representation theory on Klein-antipodal pairs, which is distinct
from the mode-pair XOR filter. Both halves of the partition are
now structurally derived.

## Part I: Ω_Λ : Ω_m = 13 : 6 (Farey)

### Statement

Under the Farey partition at depth q_max = q_2·q_3 + 1 = 7:

- Dark-energy sector count = |F_6| = 13
- Matter-sector count = |F_7| − |F_6| = φ(7) = 6

### Proof

|F_n| = 1 + Σ_{k=1}^{n} φ(k).

    |F_6| = 1 + φ(1) + φ(2) + φ(3) + φ(4) + φ(5) + φ(6)
          = 1 + 1 + 1 + 2 + 2 + 4 + 2 = 13.

    |F_7| = |F_6| + φ(7) = 13 + 6 = 19.

The 6 new fractions at F_6 → F_7 are exactly the q=7 class
{1/7, 2/7, 3/7, 4/7, 5/7, 6/7}, since 7 is prime and all numerators
in {1..6} are coprime to it.

The framework fixes (q_2, q_3) = (2, 3) via the cross-link
identities `q_2² − 1 = q_3` and `q_3² − 1 = q_2³`, so the depth
q_2·q_3 + 1 = 7 is forced. The partition 13:6 is structurally
determined.

## Part II: Ω_b : Ω_DM = 1 : 5 (Z₂ representation theory)

### Setup

The 6 q=7 matter modes are indexed by p ∈ {1, 2, 3, 4, 5, 6}.
Klein-antipodal identification on Z_6 residues sends k → 6 − k,
producing pairs:

| Pair | Type | Sector reduction (gcd with 6) |
|---|---|---|
| {1, 5} | coprime-to-6 | 1 (cross-sector q_2 × q_3) |
| {2, 4} | gcd = 2 | q_2 only |
| {3} | self-paired | q_3 only |
| {6} | self-paired (≡ {0}) | trivial |

### Step 1: Z₂ acts non-trivially on the spinor bundle

The Klein bottle has H₁(K²; Z) = Z ⊕ Z₂ (`fermion_spinors_from_z2.py`).
The Z₂ torsion makes the Klein-antipodal action a non-trivial Z₂
representation on the bundle of fields. For a swapped pair
{ψ_p, ψ_{6−p}}, Z₂ representation theory produces **two**
eigenmodes:

- Symmetric: ψ_p + ψ_{6−p} — trivial Z₂ rep
- Antisymmetric: ψ_p − ψ_{6−p} — sign Z₂ rep

The antipodal identification does not merge the pair into one
mode. It decomposes the 2-dimensional pair-space into two
1-dimensional irreps.

### Step 2: Klein-singlet (sym) modes carry global phase

The symmetric mode is invariant under the antipodal action:
its phase around the Klein loop is single-valued. This is the
condition for definite charge under any continuous symmetry —
in particular, for definite EM charge.

The antisymmetric mode picks up a sign under the antipodal
action: its phase is two-valued (monodromy −1) around the
Klein loop. Globally, it has no single phase value, so its
EM coupling integrates to zero around the loop. It carries
gravitational coupling (universal, energy-density only) but
no net EM coupling.

### Step 3: EM coupling requires cross-sector (coprime-to-6)

From `gell_mann_nishijima.md`: α_em = α_2 · sin²θ_W requires
participation in BOTH the q_2 (SU(2)) and q_3 (SU(3)) sectors.
A mode at numerator p couples to both sectors iff gcd(p, 6) = 1
— i.e., iff p is coprime to 6. Of the 6 matter modes, only
p ∈ {1, 5} satisfy this.

### Step 4: Combine — exactly one baryonic mode

A mode is **baryonic** (carries net EM coupling) iff it satisfies
both:

(a) Klein-singlet (sym mode of an antipodal pair, or self-paired
    fixed mode), AND

(b) coprime-to-6 numerator (cross-sector EM coupling).

Working through the 6 q=7 matter modes:

| Mode | Klein-singlet? | Coprime-to-6? | Baryonic? |
|---|---|---|---|
| ψ_1 + ψ_5 (sym of coprime pair) | yes | yes | **YES** |
| ψ_1 − ψ_5 (antisym of coprime pair) | no | yes | no (no EM via sign rep) |
| ψ_2 + ψ_4 (sym of gcd=2 pair) | yes | no | no (no cross-sector) |
| ψ_2 − ψ_4 (antisym of gcd=2 pair) | no | no | no |
| ψ_3 (self-paired) | yes | no | no (no cross-sector) |
| ψ_6 (self-paired) | yes | no | no (trivial sector) |

**Exactly one baryonic mode**: the symmetric combination of the
coprime pair {1, 5}. The remaining five are dark.

### Step 5: Count

- Baryonic: 1 (sym mode of {1, 5})
- Dark: 1 (antisym of {1, 5}) + 2 (sym, antisym of {2, 4})
        + 1 ({3}) + 1 ({6}) = **5**
- Total matter: 1 + 5 = 6 ✓
- Plus dark energy: 13 (|F_6|) → grand total 19 = |F_7| ✓

### Result

Ω_b : Ω_DM : Ω_Λ = 1 : 5 : 13. **Structural**, derived from:

1. Klein bottle Z₂ torsion in H₁(K²; Z) — `fermion_spinors_from_z2.py`
2. Z₂ representation theory: antipodal pair → (sym, antisym)
3. EM coupling requires Klein-singlet (sym/self-paired) AND
   cross-sector coupling (coprime-to-6) — `gell_mann_nishijima.md`

No free parameters; the partition is forced.

## Why the previous "Proposed" framing was wrong

The original target said "XOR-parity proof of 1:5:13." Two issues:

1. **XOR-parity** (from `xor_derivation.md`) is a filter on mode
   pairs (q_1, q_2): "exactly one of q_1, q_2 is even." It applies
   to *which Klein-bottle modes survive at all*, not to which
   q=7 matter mode is baryonic.

2. **The 1:5 split** comes from a different Z₂ structure: the
   antipodal action's representation theory on coprime pairs.
   This is a sign-rep eigenmode argument, not an XOR filter.

Both belong to the broader Z₂-torsion physics of the Klein bottle
but are operationally distinct mechanisms.

## Status

**Derived.** Both halves of the Ω partition follow from independent
combinatorial arguments rooted in the Klein bottle's Z₂ structure:

- 13 : 6 from Farey counting at depth 7
- 1 : 5 from Z₂ representation theory on coprime-pair antisym modes
  combined with the EM-coupling criterion

Promote `framework_status.md` entry for the full 1 : 5 : 13 partition
to **Survives**.

## Connection to existing derivations

- `farey_partition.md`: 13:6 Farey argument (existing).
- `baryon_fraction.md`: 1:5 was previously argued via coprime-to-6
  + Klein identification, with "merge vs split" ambiguity. The Z₂
  representation theory argument here resolves the ambiguity:
  Klein identification produces (sym, antisym) eigenmodes, not a
  merge. The sym mode of the coprime pair is the unique baryonic
  mode. Update `baryon_fraction.md` to use this language.
- `xor_derivation.md`: XOR-parity filter on mode pairs (separate
  Z₂ structure from the antipodal-pair sym/antisym decomposition).
- `gell_mann_nishijima.md`: EM-coupling-requires-cross-sector
  criterion.
- `fermion_spinors_from_z2.py`: H₁(K²) = Z ⊕ Z₂ torsion that
  makes the antipodal Z₂ action non-trivial.

## Open follow-ups

- The 6.7% Ω_b residual (`baryon_fraction.md` Status) is unaffected
  by this derivation — that's a separate boundary-weight / decoherence
  correction issue, not a partition-counting issue.
- A full update to `baryon_fraction.md` to replace "merge" language
  with the "(sym, antisym) eigenmode decomposition" language is
  appropriate but out of scope here. This file documents the
  structural derivation; consumer files can be updated subsequently.

## Cross-references

| File | Role |
|---|---|
| `farey_partition.md` | 13:6 Farey count derivation |
| `baryon_fraction.md` | Earlier 1:5 derivation with merge-vs-split ambiguity, now resolved |
| `xor_derivation.md` | XOR-parity filter (different Z₂ structure) |
| `gell_mann_nishijima.md` | EM coupling = cross-sector criterion |
| `fermion_spinors_from_z2.py` | H₁(K²) = Z ⊕ Z₂ torsion source |
| `framework_status.md` | Promoted 1:5:13 entry to Survives |
