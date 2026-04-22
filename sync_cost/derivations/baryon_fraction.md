# The Baryon Fraction

## Claim

The cosmic energy budget partitions into three sectors from the
single number 19 (the Klein bottle's total budget from D25):

    Lambda : dark matter : baryonic = 13 : 5 : 1

All three fractions follow from the Farey partition and the Klein
bottle's denominator structure. No fitted factors; uses only
framework integers (q₂, q₃, d) plus the Farey count.

---

## The partition

### The total budget (D25, D28)

The Farey partition at the Klein bottle's resolution gives:

    Total budget = |F_6| + q_2 * q_3 = 13 + 6 = 19

The locked modes (|F_6| = 13) are dark energy. The product modes
(q_2 * q_3 = 6) are matter. This gives Omega_Lambda = 13/19 and
Omega_m = 6/19 (D25).

### The matter subdivision

The 6 matter modes live at the product scale q_2 * q_3 = 6. Under
the Farey reading they are the q=7 class {1/7, 2/7, 3/7, 4/7, 5/7,
6/7} (= φ(7) new fractions at F_6 → F_7); under the residue reading
they are Z_6 = {0, 1, 2, 3, 4, 5}. Either way, indexed by
p ∈ {1, 2, 3, 4, 5, 6}.

Of these 6 modes, how many are electromagnetically coupled
(baryonic) and how many are dark? The answer follows from two
independent structural criteria applied jointly.

### The EM coupling criterion (cross-sector)

A mode is electromagnetically coupled if it participates in the
gauge interaction — if it carries charge under SU(3) × SU(2) × U(1).
In the Klein bottle framework (D41, D42), the gauge coupling is
mediated by the GCD fiber structure. A mode at position k mod 6
couples to the gauge fields if and only if it has a nontrivial
projection onto BOTH the q=2 and q=3 sectors. From
`gell_mann_nishijima.md`: α_em = α_2 · sin²θ_W requires cross-sector
participation.

The modes that are coprime to 6 — those with gcd(k, 6) = 1 — are
the cross-sector modes. These interact with BOTH the q=2 and q=3
sectors simultaneously (they are not reducible to either sector
alone):

    Elements coprime to 6: {1, 5}     (count: φ(6) = 2)

The modes that are NOT coprime to 6 — those with gcd(k, 6) > 1 —
factor through either q=2, q=3, or both:

    gcd(k, 6) = 2: {2, 4}     (factor through q=2)
    gcd(k, 6) = 3: {3}        (factors through q=3)
    gcd(k, 6) = 6: {0} (≡ {6}) (factors through both = the identity)

### The Z₂ representation-theory criterion (Klein-singlet)

The Klein bottle has H₁(K²; Z) = Z ⊕ Z₂ (`fermion_spinors_from_z2.py`).
The Z₂ torsion makes the antipodal action a non-trivial Z₂
representation on the spinor bundle, not a simple identification.
An antipodally-swapped pair of modes {ψ_p, ψ_{6−p}} does not merge
into one mode; it decomposes into two irreducible Z₂ eigenmodes:

    ψ_+ = ψ_p + ψ_{6−p}   (trivial Z₂ rep — Klein-singlet)
    ψ_- = ψ_p − ψ_{6−p}   (sign Z₂ rep — monodromy −1)

The symmetric mode ψ_+ has single-valued phase around the Klein
loop. Definite EM charge is possible. The antisymmetric mode ψ_-
has two-valued phase (monodromy −1 around the loop): its net EM
coupling integrates to zero, though gravitational coupling
(universal, energy-density only) persists.

Klein-antipodal pairing on Z_6 residues sends k ↔ 6−k:

| Pair | Structure | Eigenmodes |
|---|---|---|
| {1, 5} | antipodal pair | ψ_+(1,5), ψ_−(1,5) |
| {2, 4} | antipodal pair | ψ_+(2,4), ψ_−(2,4) |
| {3} | self-paired | ψ_3 (Klein-singlet) |
| {0} (≡ {6}) | self-paired | ψ_0 (Klein-singlet) |

Six physical modes: four antipodal-pair eigenmodes (two pairs × two
eigenmodes each) plus two self-paired modes.

### Baryonic = Klein-singlet AND coprime-to-6

A mode carries net EM coupling iff it satisfies BOTH criteria: it
must be a Klein-singlet (so its phase is well-defined around the
Klein loop) AND coprime-to-6 (so it couples to both gauge sectors).

Combining:

| Mode | Klein-singlet? | Coprime-to-6? | Baryonic? |
|---|---|---|---|
| ψ_+(1,5) = ψ_1 + ψ_5 | yes | yes | **YES** |
| ψ_−(1,5) = ψ_1 − ψ_5 | no (sign rep) | yes | no (no EM via monodromy) |
| ψ_+(2,4) = ψ_2 + ψ_4 | yes | no (gcd = 2) | no |
| ψ_−(2,4) = ψ_2 − ψ_4 | no | no | no |
| ψ_3 | yes (self-paired) | no (gcd = 3) | no |
| ψ_0 | yes (self-paired) | no (gcd = 6) | no |

Exactly one baryonic mode: ψ_+(1,5), the symmetric combination of
the coprime pair.

### Counts

The count of baryonic modes is the intersection of Klein-singlet
and coprime-to-6:

    # baryonic = 1  (just ψ_+(1,5))
    # dark     = 5  (the remaining five modes)
    # matter   = 6  ✓

Therefore:

    **Ω_b = 1/19**
    **Ω_DM = 5/19**
    **Ω_b / Ω_m = 1/6**

### The dark-matter remainder (detail)

| Mode | gcd criterion | Klein character | Dark reason |
|---|---|---|---|
| ψ_0 | gcd(0,6)=6 | singlet (self-paired) | no cross-sector coupling |
| ψ_+(2,4) | gcd(2,6)=2 | singlet (sym) | only q=2 sector |
| ψ_−(2,4) | gcd(2,6)=2 | sign rep | only q=2 sector + no global phase |
| ψ_3 | gcd(3,6)=3 | singlet (self-paired) | only q=3 sector |
| ψ_−(1,5) | gcd(1,6)=1 | sign rep | cross-sector, but monodromy −1 kills net EM |

Five dark modes. Note that ψ_−(1,5) is dark *despite* being
coprime-to-6 — it has the cross-sector coupling but its
antisymmetric character under Klein-antipodal means no globally
single-valued phase, so no net EM charge. This is the
Klein-rep-theory reason the baryonic count is 1, not 2.

### Why dark modes gravitate but don't radiate

The gravitational coupling is universal — it depends on the
energy density (ω², from D46), not on the gauge charge or phase
structure. All 6 matter modes contribute to the stress-energy
tensor.

The electromagnetic coupling requires BOTH cross-sector
participation (α_em = α_2 · sin²θ_W) AND Klein-singlet status
(single-valued phase). The unique intersection is ψ_+(1,5).

This is not an ad hoc distinction. It is forced by the Klein
bottle's topology: H₁(K²) = Z ⊕ Z₂ gives the antipodal Z₂
representation on the spinor bundle, which in turn separates
Klein-singlet from Klein-fermion eigenmodes on every antipodal
pair.

---

## Comparison with observation

| Quantity | Computed | Observed (Planck 2018) | Residual |
|----------|----------|------------------------|----------|
| Omega_Lambda | 13/19 = 0.6842 | 0.6847 +/- 0.0073 | **0.07 sigma** |
| Omega_DM | 5/19 = 0.2632 | 0.265 +/- 0.007 | **0.7%** |
| Omega_b | 1/19 = 0.0526 | 0.0493 +/- 0.0003 | **6.7%** |
| Omega_DM / Omega_b | 5 | 5.41 | **7.5%** |

The partition 13 : 5 : 1 = 19 gives all three cosmic fractions
from a single integer. The dark energy and dark matter fractions
are within 1% of observation. The baryon fraction has a 6.7%
residual — the largest in the framework's scorecard, but still
a structural prediction from the framework's combinatorial vocabulary (q_2, q_3, d) plus the Farey partition.

### The 6.7% residual

The residual in Omega_b is the largest among the framework's
predictions. Possible sources:

1. **The boundary weight correction** (D38): the effective Farey
   depth is 5.83, not 6. At fractional depth, the partition
   becomes Omega_b(w) = (1 - epsilon(w)) / 19, where epsilon
   is a correction from the partial locking of q=6 modes. At
   w* = 0.83, this correction reduces Omega_b by approximately
   0.003, bringing the prediction closer to 0.049.

2. **The decoherence tax** (D33): the order parameter |r| = 0.968
   at the observation scale. The baryonic fraction is reduced by
   (1 - |r|) = 3.2% from the tree-scale value. This accounts
   for part of the residual.

3. **Klein-eigenmode width asymmetry**: the two eigenmodes
   ψ_+(1,5) and ψ_−(1,5) sit on slightly different tongue widths
   due to the twist's effect on sym vs antisym combinations. If
   this asymmetry leaks between the EM-coupled and EM-decoupled
   sides, the effective baryonic fraction is slightly less than
   1/6.

---

## The dark matter interpretation

### What dark matter IS in this framework

Dark matter is not a particle. It is the set of matter modes
at the product scale q_2 * q_3 = 6 that are reducible to a
single sector. They gravitate (universal coupling) but do not
participate in the cross-sector (electromagnetic) interaction.

They are:
- The q=2 reducible modes: dark matter that "knows about" the
  weak sector but not the strong sector
- The q=3 reducible mode: dark matter that "knows about" the
  strong sector but not the weak sector
- The identity mode (k=0): dark matter that is trivial under
  both sectors

### Predictions

1. **Omega_DM / Omega_b = 5** (observed: 5.41, residual 7.5%).

2. **No dark matter particle** with Standard Model quantum
   numbers. The dark modes are not "particles" in the usual
   sense — they are population modes of the Stern-Brocot tree
   that do not form irreducible composites.

3. **Dark matter clusters gravitationally but does not self-interact
   strongly.** The reducible modes interact within their own
   sector (weak self-interaction for q=2 modes, confined for
   q=3 modes), but the gravitational clustering dominates at
   cosmological scales.

4. **The MOND transition at a_0** (D3, D8) is where the baryonic
   and dark sectors are distinguished. Below a_0, the enhanced
   Stribeck coupling (D3) compensates for the missing cross-sector
   contribution. The "dark matter effect" at galactic scales IS
   the deficit of cross-sector coupling below a_0.

5. **a_0(z) = c H(z) / (2 pi)** (D8): the MOND scale evolves
   with redshift. This is testable with JWST-era kinematic
   surveys. If confirmed, it validates the framework's identification
   of dark matter as a coupling deficit rather than a substance.

---

## Status

**Derived.** Omega_b = 1/19, Omega_DM = 5/19 from the Farey
partition and Z_6 irreducibility. The full cosmic energy budget
13:5:1 follows structurally from one integer (19) via the Farey count and the Klein-antipodal Z_2 rep; no fitted factors.

**Dependencies**: D25 (Farey partition), D28 (partition derivation),
D41 (gauge structure, Z_6 center), D42 (SU(3) x SU(2) x U(1)).

**Adds to scorecard**: Omega_b = 1/19 (6.7% residual),
Omega_DM = 5/19 (0.7% residual), Omega_DM/Omega_b = 5 (7.5%).
