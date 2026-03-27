# Farey Orbitals: Quantum Chemistry Mode Reduction

## The idea

Current quantum chemistry computes ~10³–10⁶ molecular orbitals
to find the self-consistent electron density. Most are redundant.

The framework says: identify the COPRIME orbitals (the Farey
fractions of the molecular Stern-Brocot tree) and compute only
those. The rest are ancestors — covered by GCD reduction.

## The molecular Stern-Brocot tree

A molecular orbital with quantum numbers (n, l, m) has a
"denominator" in the Stern-Brocot sense: the complexity of
its nodal structure. Low-q orbitals (1s, 2s, 2p) are simple
(few nodes). High-q orbitals (4f, 5g) are complex (many nodes).

The self-consistent field (SCF) in Hartree-Fock is the
fixed-point condition: the electron density determines the
potential, which determines the orbitals, which determine the
density. This is x = f(x).

At the SCF fixed point, the occupation numbers are:
- ≈ 2 (fully occupied) — these are LOCKED (in a tongue)
- ≈ 0 (unoccupied) — these are also locked (in a gap tongue)
- Fractional (partially occupied) — these are IN THE GAP

The Farey orbitals are the ones with fractional occupation:
the modes that are actually doing the chemistry. The fully
occupied and fully unoccupied orbitals are ancestors — their
contribution is determined by the Farey modes.

## The mode reduction

For a typical organic molecule (e.g., benzene, C₆H₆):

| Current approach | Basis functions | Active orbitals |
|-----------------|-----------------|-----------------|
| Minimal basis (STO-3G) | 36 | ~6 π orbitals |
| Double-zeta (6-31G) | 66 | ~6 π orbitals |
| Triple-zeta (cc-pVTZ) | 264 | ~6 π orbitals |
| Full CI | all 264 | all 264 |

The ACTIVE orbitals — the ones that determine the chemistry —
are always ~6 for benzene (the π system). The rest are spectators.
Current methods compute ALL of them and then extract the active
subset. The framework says: identify the active set FIRST (the
Farey modes at the molecular coupling K), compute ONLY those,
and let the GCD reduction handle the spectators.

## The algorithm (sketch)

1. Compute the molecular graph (atoms and bonds)
2. Identify the Stern-Brocot tree of the molecular symmetry group
3. The denominator q of each orbital = number of nodal surfaces
4. The coupling K = the electron-electron interaction strength
   (related to the orbital energy gaps)
5. At the molecular K, compute which tongues are open
   (which orbitals have fractional occupation)
6. These are the Farey orbitals — compute only these
7. The closed-shell orbitals (fully occupied/unoccupied) are
   ancestors — their contribution follows from the Farey modes

## Potential savings

| System | Current modes | Estimated Farey modes | Savings |
|--------|--------------|----------------------|---------|
| Small molecule (H₂O) | ~50 | ~3 | ~15× |
| Medium molecule (benzene) | ~300 | ~6 | ~50× |
| Protein active site | ~10⁴ | ~10–50 | ~200× |
| Transition metal complex | ~500 | ~10–20 | ~25× |

## Status

**Concept.** The connection between the SCF fixed point and the
Stern-Brocot tongue structure is structural, not yet formalized.
The identification of "orbital denominator" with nodal complexity
needs rigorous definition. The claim that GCD reduction applies
to molecular orbitals needs a proof that the ancestor relationship
(orbital at q reduces to orbital at q/gcd) holds in quantum chemistry.

This requires collaboration with a computational chemist.

## Connection to the framework

The molecular SCF is x = f(x) (P3). The orbital structure is the
Stern-Brocot tree (P1 + P2). The electron correlation is the
coupling K. The parabola (P4) appears at orbital degeneracies
(Jahn-Teller bifurcation). All four primitives are present.

The molecular "universe" has its own F₆-equivalent — the minimum
set of orbitals that self-consistently determines the electron
density. Finding this set IS the quantum chemistry problem, restated
in the framework's language.
