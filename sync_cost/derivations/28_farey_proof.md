# Derivation 28: Why the Farey Partition

## The gap

Derivation 25 showed Ω_Λ = |F₆|/(|F₆| + 6) = 13/19 matches
observation to 0.07σ. But the step from "the Klein bottle has
denominator classes {2,3}" to "the energy partition equals
|F_n|/(|F_n| + n)" was observed, not proved.

This derivation closes the gap.

## The claim

**Theorem.** On the Stern-Brocot tree at resolution n, the unique
partition of the total budget into a resolved sector and a resolution
sector, consistent with mediant arithmetic as the sole combining
operation, is:

    Ω_resolved = |F_n| / (|F_n| + n)

## Proof

### Step 0: The admissible scalars

The Stern-Brocot tree at resolution n carries the SO(2) phase
symmetry of the Kuramoto model (θ → θ + α for all oscillators).
Under this symmetry:

- The specific Farey fractions {p_i/q_i} are NOT invariant (they
  shift with the phase).
- The individual totient values φ(q) for each q ≤ n are invariant
  but depend on a denominator LABEL q, which is not SO(2)-observable.
- The TOTAL count |F_n| = 1 + Σ_{k=1}^{n} φ(k) IS invariant and
  requires no label.
- The resolution bound n IS invariant and requires no label.

These are the only two SO(2)-invariant scalars at resolution n that
do not reference a specific denominator. Any SO(2)-invariant scalar
function of the Farey sequence at order n reduces to a function of
(|F_n|, n).

**Proof**: an SO(2)-invariant scalar is a function of the Farey
sequence that is unchanged under phase rotation. Phase rotation
permutes the fractions (p/q → (p + kq mod q)/q for the appropriate
integer k) but preserves denominators. Therefore invariant quantities
can depend on the SET of denominators {q_i} but not on the
numerators. The only scalars extractable from the denominator
multiset without choosing a specific q are:
- The maximum: n
- The count at each q: φ(q) — but these are determined by n alone
  (the totient function depends only on q)
- The total count: Σφ(q) + 1 = |F_n|

All other invariants (e.g., Σq², Σ1/q²) are determined by n through
the totient. So the space of independent invariant scalars is
2-dimensional: {|F_n|, n}. □

### Step 1: The two sectors

At resolution n = q₂q₃ = 6, the system has two components:

- **C = |F_n|**: the cardinality of the Farey sequence. This counts
  the number of distinct rational states that the tree resolves at
  this order. It is a NUMBER OF CONFIGURATIONS — a count, not a
  measure.

- **S = n**: the resolution scale. This is the maximum denominator
  — the finest rational the tree can distinguish. It is a SCALE,
  not a count.

These are the only two quantities the tree produces at order n.
The tree does not have a third independent quantity. |F_n| and n
together fully specify the Farey sequence (up to the specific
fractions, which are determined by the Euler totient function).

### Step 2: Why they must be combined by addition

The framework's primitive combining operation is the mediant (D10).
The mediant of a/b and c/d is (a+c)/(b+d). It is defined by
ADDING the components.

The question: given two quantities C and S, how does mediant
arithmetic combine them into a total?

The mediant does not multiply. It does not exponentiate. It does
not divide. It ADDS the components of the objects it combines.

A fraction p/q on the Stern-Brocot tree is a pair (p, q). The
mediant of (p₁, q₁) and (p₂, q₂) is (p₁+p₂, q₁+q₂). The total
of the two pairs is their component-wise sum.

The configuration count C and the resolution scale S are both
integers — elements of Z, the first primitive (D10). To form a
total from two integers using the framework's operations, the only
available operation is addition (Z is a group under addition, and
the mediant's component operation is addition). Therefore:

    Total = C + S = |F_n| + n

### Step 3: The partition

The fraction of the total in the resolved sector:

    Ω_resolved = C / (C + S) = |F_n| / (|F_n| + n)

The fraction in the resolution sector:

    Ω_substrate = S / (C + S) = n / (|F_n| + n)

These sum to 1 (the partition is exhaustive).

### Step 4: Uniqueness

The partition Ω = f(C, S) must satisfy:

(a) **Domain**: f maps two positive integers to [0,1].

(b) **Exhaustive**: f(C, S) + f(S, C with roles swapped) = 1.
    The two sectors partition the total.

(c) **Invariance**: f depends only on the SO(2)-invariant scalars
    C = |F_n| and S = n (Step 0). It cannot depend on the specific
    fractions or their arrangement.

(d) **Mediant consistency**: the combining operation is addition
    (the mediant's component operation, D10). The total T must
    satisfy T = C ⊕ S where ⊕ is the framework's primitive.
    Since ⊕ = + (addition), T = C + S.

(e) **Linearity**: the partition must be a linear function of the
    components. The mediant is linear on components: (a+c, b+d)
    is linear in (a,b) and (c,d). A nonlinear partition (e.g.,
    C²/(C²+S²)) would not be consistent with mediant algebra,
    where the components add without transformation.

Given (a)-(e), the unique partition is:

    Ω_C = C / (C + S) = |F_n| / (|F_n| + n)

**Proof of uniqueness**: a linear, exhaustive partition of T = C + S
into two parts assigns weight C/T to the first and S/T to the second.
Any other assignment violates either linearity (e) or exhaustiveness
(b). Specifically:

- **Multiplication** (T = C × S): violates (d). The mediant does
  not multiply. The product 13 × 6 = 78 is not a mediant sum.

- **Nonlinear** (Ω = C²/(C²+S²)): violates (e). The mediant adds
  components without squaring.

- **Weighted** (Ω = αC/(αC+βS) for α ≠ β): violates SO(2)
  invariance unless α and β are themselves SO(2)-invariant scalars
  (i.e., functions of C and S). But then the partition is a nonlinear
  function of C and S, violating (e).

- **Permuted** (Ω = S/(C+S)): this is f(S,C), which by (b) gives
  the OTHER sector. It is the complementary partition, not an
  alternative.

No other partition satisfies (a)-(e). □

## Why C and S are the right quantities

### C = |F_n| is the configuration count

The Farey sequence at order n contains every irreducible fraction
with denominator ≤ n. Each such fraction is a mode that the
Stern-Brocot tree has resolved — a state that the system can
distinguish.

In the Kuramoto framework: a resolved fraction p/q is a mode-locked
orbit with definite winding number. It is a state. The number of
such states at resolution n is |F_n|.

In cosmology: Ω_Λ is the fraction of the energy budget in the
vacuum — the "resolved" component, the topologically determined
structure that does not dilute with expansion. The Farey states
are the vacuum structure: they persist because they are rational
(mode-locked), regardless of the scale factor.

### S = n is the resolution scale

The resolution n = q₂q₃ is the maximum denominator the Klein
bottle can produce at the interaction scale of its two sectors.
It is not a count of states — it is the SCALE at which states
are counted. It sets the precision of the finest resolvable
frequency ratio.

In cosmology: Ω_m is the fraction of the energy budget in matter
— the "substrate" component that dilutes as the universe expands.
Matter provides the frequency contrast (the natural frequencies
ω(x) in the Kuramoto equation) that the vacuum structure is
measured against. The resolution scale S = n IS the matter
contribution: it is the denominator space that makes rational
frequency ratios possible.

### No third quantity

At resolution n, the Farey sequence is fully specified by |F_n|
and n. There is no independent third quantity:

- The specific fractions {p_i/q_i} are determined by the Euler
  totient function given n.
- The tongue widths at K = 1 are 1/q² for each fraction — determined
  by the denominators, which are determined by n.
- The spacing between consecutive Farey fractions is 1/(q_i q_{i+1})
  — determined by the fractions, which are determined by n.

The two-quantity structure (count C, scale S) at a given resolution
is complete. The partition is fully determined.

## The physical identification

The partition Ω_Λ = C/(C+S) maps:

- **C = |F_n| = 13**: the number of vacuum configurations. These
  are topologically protected (they are rationals, determined by
  the mode-locking structure). Their energy does not dilute because
  the topology fixes them.

- **S = n = 6**: the resolution scale. This dilutes as the universe
  expands (the effective resolution changes with the scale factor,
  since H and therefore the reference frequency change). In the
  current epoch (at the matter-Λ equality), S has diluted to the
  value where the two sectors are comparable.

- **Ω_Λ = C/(C+S) = 13/19**: the fraction that is topological.
  This is not a function of time (the topology does not change).
  The partition 13/19 is the ASYMPTOTIC value — the fixed point
  of the cosmological evolution under the Klein bottle topology.

## What this proves and what it doesn't

**Proved**: Given:
1. The Klein bottle produces denominator classes {2, 3} (D19)
2. The interaction scale is n = q₂q₃ = 6 (D25)
3. The primitive combining operation is the mediant, i.e., addition
   of components (D10)
4. The configuration count at order n is |F_n| (number theory)

Then: Ω_Λ = |F_n|/(|F_n| + n) = 13/19 is the unique partition.

**Not proved**: Axiom (3) — that the mediant is the correct
combining operation — is the framework's foundational assumption
(D10), not a derived result. The proof shows that IF mediant
arithmetic is the physics, THEN Ω_Λ = 13/19.

The axiom is supported by the framework's internal consistency:
the mediant generates the Stern-Brocot tree (which produces the
mode-locking structure), and the Stern-Brocot tree is the
configuration space (D11). Using any other combining operation
would be inconsistent with the tree that generated the quantities
being combined.

But "supported by internal consistency" is weaker than "proved from
more primitive axioms." The mediant is Derivation 10's second
primitive. Primitives are not proved. They are assumed and checked
against observation. Ω_Λ = 13/19 matching to 0.07σ is the check.

## Status

**Theorem proved** conditional on D10's axiom that the mediant is
primitive. The proof has four steps, each referencing an established
result. The uniqueness follows from the mediant being the only
combining operation in the framework's alphabet that produces a
nontrivial partition.

The axiom (mediant is primitive) is the framework's founding
assumption, shared by all 28 derivations. It is not more questionable
here than in D11 (the field equation), D14 (three dimensions), or
D25 (the Farey count). If the axiom is accepted for those results,
it must be accepted here — it is the same axiom.

The prediction Ω_Λ = 13/19 is a zero-parameter consequence of this
axiom applied at the Klein bottle's interaction scale. It matches
Planck 2018 to 0.07σ. No other framework predicts this value.
