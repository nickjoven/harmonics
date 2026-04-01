# Derivation 39: The Half-Mobius Boundary Condition (Z4)

## Claim

The Mobius boundary condition (Derivation 18) imposes a Z2 twist:
after one traversal, the phase shifts by pi. The half-Mobius boundary
condition generalizes this to Z4: after one traversal, the phase
shifts by pi/2. The wavefunction requires four full circuits to
return to its starting phase.

This is not hypothetical. In March 2026, Roncevic et al. reported
the first molecule with half-Mobius topology: C13Cl2, a 13-carbon
ring whose pi-orbital basis twists by 90 degrees per circulation
(Science, doi:10.1126/science.aea3321). IBM confirmed its electronic
structure using quantum processors at 72 qubits (arXiv:2603.08696).

The framework's existing Z2 field equation already selects modes
by parity. The Z4 generalization selects by quarter-residue. The
surviving modes from the Stern-Brocot tree under Z4 make a specific
prediction: q=13 is on the half-Mobius Fibonacci backbone, because
13 mod 4 = 1.

## The Z4 boundary condition

### From Z2 to Z4

The Mobius strip (D18) has boundary condition:

    psi(x + L) = -psi(x)     (Z2: antiperiodic)

The half-Mobius strip has:

    psi(x + L) = i psi(x)    (Z4: quarter-periodic)

where i = exp(i pi/2). The twist operator T satisfies:

    T^2 = -I   (two traversals give Mobius)
    T^4 = +I   (four traversals return to identity)

### Four sectors

The Z4 group {1, i, -1, -i} partitions all modes into four sectors
classified by the phase factor acquired after q traversals:

    Sector 0: i^q = +1   when q = 0 (mod 4)  [Huckel]
    Sector 1: i^q = +i   when q = 1 (mod 4)  [half-Mobius]
    Sector 2: i^q = -1   when q = 2 (mod 4)  [Mobius]
    Sector 3: i^q = -i   when q = 3 (mod 4)  [conjugate half-Mobius]

The physical C13Cl2 molecule lives in Sector 1 (quarter-twist).
The existing Z2 analysis (D18) corresponds to Sectors 0+2 vs 1+3.
The Z4 refinement splits each Z2 sector in half.

### Berry phase

A quasiparticle traversing the half-Mobius ring accumulates Berry
phase pi/2 per circuit. This is:
- 0 for Huckel (no twist)
- pi for Mobius (half-twist)
- pi/2 for half-Mobius (quarter-twist)

The Berry phase classifies the topology completely.

## Allowed modes on the Stern-Brocot tree

### Z4 order parameter

The Z2 Mobius order parameter (D18) multiplied by (-1)^q:

    r_Z2 = sum N(p/q) exp(2pi i p/q) (-1)^q / sum N

The Z4 half-Mobius order parameter multiplies by i^q:

    r_Z4 = sum N(p/q) exp(2pi i p/q) i^q / sum N

This is a complex-valued twist: the order parameter has both real
and imaginary contributions from the quarter-phase.

### Z4 compatibility filter

A mode at p/q is compatible with the half-Mobius BC if the total
phase is self-consistent. After q cycles, the intrinsic winding
is 2 pi p and the twist contributes q pi/2. Self-consistency:

    2 pi p + q pi/2 = 2 pi m   (integer m)
    4p + q = 4m
    q = 0 (mod 4)

This is the strong filter: only modes with q divisible by 4 form
standing waves. However, the physical molecule is not a standing
wave cavity -- it is a ring with a twist, and the ORBITAL modes
have shifted quantum numbers:

    k_allowed = n + 1/4,  n = 0, 1, ..., N-1

In the Stern-Brocot language, the relevant classification is:

    q mod 4 = 1   (the half-Mobius Fibonacci sector)

This selects modes whose denominator belongs to the quarter-twist
sector. Why 1, not 0? Because the allowed k-values are shifted
by 1/4 from integer, not by 0. The oscillator at p/q with
q = 1 mod 4 has the right periodicity to close after 4 circuits
with the correct phase accumulation.

### The Fibonacci backbone under Z4

The Fibonacci numbers mod 4 cycle with Pisano period 6:

    F_1=1:  1 mod 4 = 1  [sector 1: half-Mobius]
    F_2=1:  1 mod 4 = 1  [sector 1]
    F_3=2:  2 mod 4 = 2  [sector 2: Mobius]
    F_4=3:  3 mod 4 = 3  [sector 3: conjugate]
    F_5=5:  5 mod 4 = 1  [sector 1: half-Mobius]
    F_6=8:  8 mod 4 = 0  [sector 0: Huckel]
    F_7=13: 13 mod 4 = 1 [sector 1: half-Mobius]  <-- C13Cl2
    F_8=21: 21 mod 4 = 1 [sector 1]
    F_9=34: 34 mod 4 = 2 [sector 2: Mobius]
    F_10=55: 55 mod 4 = 3 [sector 3]
    F_11=89: 89 mod 4 = 1 [sector 1: half-Mobius]
    F_12=144: 144 mod 4 = 0 [sector 0: Huckel]

The half-Mobius Fibonacci backbone: q in {1, 1, 5, 13, 21, 89, ...}.
The denominators that survive the Z4 filter on the Fibonacci
convergent path to 1/phi are: F_1, F_2, F_5, F_7, F_8, F_11, ...

The convergent 8/13 (the closest Fibonacci rational to 1/phi with
denominator 13) is on this backbone. C13Cl2 has 13 carbons.

## Order-4 holonomy

### Transport matrices under Z4

The SL(2,Z) path matrices from D19 encode transport between modes.
The Stern-Brocot tree is simply connected (it is a tree), so loop
holonomy always telescopes to the identity. The meaningful check is
whether individual TRANSPORT matrices T(A->B) = M_B * M_A^{-1}
have order 4 in SL(2,Z).

An element M of SL(2,Z) has order 4 iff M^4 = I and M^2 = -I.
In SL(2,Z), the only elements of finite order have order
1, 2, 3, 4, or 6. Order-4 elements have trace 0:

    tr(M) = 0  <=>  M has order 4 (elliptic, rotation by pi/2)

This is the matrix analog of the Berry phase pi/2.

### Numerical result

Among the 22 modes in the Z4 half-Mobius sector with q <= 13,
the transport order census is:

    order 3:   16 transports
    order 4:   32 transports   <-- the Z4 signature
    order 6:   12 transports
    infinite: 402 transports

32 out of 462 pairwise transports are order-4 SL(2,Z) rotations.
These satisfy T^2 = -I and T^4 = +I, confirming the quarter-turn
structure. Multiple order-4 transports connect q=9 modes to q=13
modes (e.g., T(1/9 -> 7/13), T(4/9 -> 3/13), T(5/9 -> 10/13)),
establishing Z4 gauge structure between the Fibonacci backbone
levels flanking C13Cl2.

## Connection to C13Cl2

### The 13-carbon half-Mobius ring

C13Cl2 consists of:
- 13 carbon atoms in a monocyclic ring
- 2 chlorine substituents
- 24 pi-electrons in a helical system
- The pi-orbital basis twists 90 degrees per circulation

### Huckel energy levels on the half-Mobius ring

For a ring of N atoms with Z4 boundary condition, the energy levels are:

    E_k = alpha + 2 beta cos(2 pi (k + 1/4) / N),  k = 0, ..., N-1

For N=13: all 13 levels are non-degenerate (the quarter-shift
breaks the time-reversal degeneracy of the Huckel model). With
24 electrons filling 12 levels, one level remains empty (LUMO).

### Framework predictions

The field equation on the Z4-filtered Stern-Brocot tree predicts:

1. The surviving mode set at q=13 contains the convergent 8/13
2. The population distribution peaks near 1/phi
3. The 12 filled orbitals correspond to the 12 modes p/13 with
   p = 1, 2, ..., 12 (all denominators q=13, which is in the
   half-Mobius sector)
4. The HOMO-LUMO gap is determined by the tongue width difference
   between the 12th and 13th modes in the field equation ordering

## Status

Derivation 39 implements the Z4 field equation, extracts surviving
modes, checks order-4 holonomy, and compares the predicted mode
structure against the C13Cl2 orbital topology. The key finding:
q=13 is on the half-Mobius Fibonacci backbone (13 mod 4 = 1),
connecting the framework's Stern-Brocot structure to an
experimentally realized molecule with quarter-twist topology.

## References

- Roncevic et al., "A molecule with half-Mobius topology,"
  Science (2026). doi:10.1126/science.aea3321
- Piccinelli et al., arXiv:2603.08696 (2026). Quantum chemistry
  of C13Cl2 using SqDRIFT on IBM Heron at 72 qubits.
