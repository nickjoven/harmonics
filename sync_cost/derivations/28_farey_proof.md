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

The partition C/(C+S) is unique given:

(a) The two independent quantities at resolution n are C = |F_n|
    and S = n. There is no third quantity.

(b) The combining operation is addition (from the mediant). There
    is no other operation available in the framework's primitive
    alphabet that takes two integers and produces a total.

(c) The partition must be a fraction (a value in [0,1] representing
    a proportion). The only way to form a fraction from two integers
    A and B using addition is A/(A+B) or B/(A+B).

If any other combining operation were used:

- **Multiplication**: C × S = 78. Then Ω = C/(C×S) = 13/78 = 1/6.
  This does not match observation (0.167 vs 0.685). Moreover,
  multiplication is not the mediant's operation — the mediant adds,
  not multiplies.

- **Maximum**: max(C, S) = 13. Then Ω = C/max = 1. This is trivial
  and uninformative.

- **Exponentiation**: C^S or S^C. These are not mediant operations
  and produce quantities that are not commensurable with the inputs.

The mediant (addition) is the only primitive operation that:
1. Combines two integers into a total
2. Produces a total that is commensurable with both inputs
3. Gives a nontrivial partition in [0,1]
4. Is the framework's foundational operation (D10)

Therefore the partition is unique. □

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
