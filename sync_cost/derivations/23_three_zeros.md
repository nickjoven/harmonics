# Derivation 23: Three Zeros and the 1+3 Decomposition

## The notational confusion

The symbol "0" appears in the Klein bottle algebra in three
structurally distinct roles. Conflating them hides a decomposition
that the algebra is trying to show.

### Zero 1: The forbidden mode (0,0)

The XOR selection rule forbids mode pairs with matching parity.
The (0,0) mode — spatially uniform, temporally constant — is the
strongest instance: it has (p_x, p_y) = (0, 0), same parity in
both directions. The Klein bottle does not admit it.

This is not "nothing." It is a specific, maximally symmetric state
(all oscillators in phase, no structure, no evolution). It is the
state with the MOST information — perfect correlation everywhere.
The topology excludes it because perfect correlation requires the
orientation to be globally consistent, which the non-orientable
surface cannot provide.

### Zero 2: The vanishing order parameter |r| = 0

The field equation's self-consistent fixed point has |r| = 0.
This does not mean "no modes" — four modes are populated. It means
the four modes cancel in the mean field sum:

    r = Σ N(f₁,f₂) exp(2πi(f₁+f₂)) (-1)^{q₁} / Σ N = 0

The cancellation is exact because the modes pair symmetrically
(the twist (-1)^{q₁} ensures opposite contributions). The modes
exist with definite populations; their NET signal is zero.

This is structure without a mean field. It is NOT the absence of
structure — it is structure that is invisible to the order parameter
because the measurement (the mean field sum) is the wrong observable
for this topology. The individual mode populations are nonzero and
carry all the information.

### Zero 3: N = 0 (actual nothing)

No oscillators, no modes, no population. This is the pre-physical
state — below the Stern-Brocot tree, below the Klein bottle, below
the field equation. It is the unique state from which any
perturbation ε > 0 produces physics (D18: any perturbation from
rest reaches the same attractor).

### The hierarchy

    N = 0 (nothing) < (0,0) mode (forbidden) < surviving modes (physics)

Each level is a different "zero":
- N = 0: no substrate
- (0,0): substrate exists but topology forbids this configuration
- The 4 modes: substrate exists, topology permits, dynamics selects

## The traceless projection is the topology

### Standard Lie algebra

In standard notation, J₀ = J − (tr(J)/n)I is the traceless part of
a matrix. It removes the "scalar" component — the part proportional
to the identity. This is a mathematical operation: project out the
direction that commutes with everything.

### On the Klein bottle

The identity matrix I acts as the (0,0) mode in the mode space.
It assigns equal weight to all modes — the uniform distribution.
It is spatially uniform (same in every mode) and directionally
neutral (no preferred axis). It IS the (0,0) state of the linear
algebra on the mode space.

The Klein bottle forbids the (0,0) mode. Therefore, on the Klein
bottle, the identity component of any matrix is not physical. The
traceless projection J₀ is not a convenience — it is the RESTRICTION
of J to the Klein bottle's configuration space. The trace was never
part of the physical system.

This means: J₀ = J on the Klein bottle. The "₀" subscript is
redundant. The 4×4 matrix J has rank 1 and eigenvalues {1, 0, 0, 0}.
But its physical content — the part that lives on the Klein bottle —
is J₀ with eigenvalues {3/4, −1/4, −1/4, −1/4}.

## The 1+3 decomposition

### The eigenvalue spectrum

J₀ has eigenvalues:

    λ₀ = 3/4     (multiplicity 1)
    λ₁ = −1/4    (multiplicity 3)

The ratio: |λ₁|/|λ₀| = 1/3.

The eigenvector for λ₀ = 3/4 is (1, 1, 1, 1)/2 — the uniform
direction (total population). Perturbations in this direction
change the total but not the distribution.

The eigenspace for λ₁ = −1/4 is 3-dimensional. It is spanned by
any three independent vectors orthogonal to (1,1,1,1). These are
the redistribution directions — perturbations that change the
distribution between modes without changing the total.

### The split

The Klein bottle mode space decomposes as:

    4 = 1 + 3

- **1 dimension**: the total population (conserved by normalization)
- **3 dimensions**: the redistribution space (how population moves
  between the 4 modes subject to the conservation constraint)

The redistribution space is 3-dimensional because 4 modes with
one constraint (total = constant) have 3 degrees of freedom.

### Connection to d = 3

Derivation 14 derives d = 3 spatial dimensions from the mediant
via dim SL(2,ℝ) = 3. The Klein bottle Jacobian independently
produces a 3-dimensional eigenspace. The question: is this the
SAME 3?

The chain:
- The Klein bottle has 4 surviving modes (from XOR on the
  product tree)
- The conservation constraint removes 1 degree of freedom
- The remaining 3 degrees of freedom are the redistribution
  directions
- 4 − 1 = 3

And from D14:
- The mediant acts on 2-vectors (fractions p/q)
- SL(2,ℤ) preserves Farey adjacency
- dim SL(2,ℝ) = 2² − 1 = 3

Both give 3 as "the number of independent directions in a
4-element system with one constraint" (Klein bottle) or
"the number of independent parameters in a 2×2 matrix with
unit determinant" (SL(2)). These are the same computation:

    n² − 1 = 4 − 1 = 3

where n = 2 is the rank of the mediant / the number of
denominator classes. The 4 surviving modes are {2,3} × {2,3}
restricted by XOR = 4 modes. The conservation constraint
(total population fixed) removes 1. The result: 3 independent
directions.

This is why F₃ = F₂² − 1 = 3 (Derivation dimension_loop.py):
- F₂ = 2 (denominator classes)
- F₂² = 4 (mode pairs)
- F₂² − 1 = 3 (independent redistribution directions)
- = dim SL(2,ℝ) (the symmetry group)
- = d (the spatial dimension)

The same "3" throughout.

### Connection to D17 (rank-1 temporal causation)

D17 established that the Fréchet derivative of the Kuramoto map
has rank 1 at a codimension-1 bifurcation. The decomposition:

    ker(DU) = the past (3 decayed dimensions)
    im(DU)  = the future (1 active dimension)

The Klein bottle Jacobian has the same structure:

    eigenvalue 3/4: the active direction (total population flow)
    eigenvalue −1/4 (×3): the redistributing directions

The 1 active direction is the temporal channel (what changes).
The 3 redistributing directions are the spatial degrees of freedom
(how it's distributed). The Jacobian's 1+3 split IS the
spacetime decomposition — 1 time dimension (the eigenvalue 3/4
direction) and 3 space dimensions (the eigenvalue −1/4 eigenspace).

## The golden-peaked commutator

Under golden-peaked g at r = 0.5, the algebra generated by
{J₀, J₀ᵀ} is 4-dimensional with ‖[J₀, J₀ᵀ]‖ = 0.28. Under
uniform g, it is 1-dimensional (J₀ is symmetric, commutator = 0).

The golden g breaks the symmetry between the 4 modes. This
breaking lifts J₀ from symmetric (so it commutes with its
transpose) to asymmetric (nontrivial commutator). The asymmetric
part has norm 0.137 — about 15% of the total.

The 15% antisymmetric component is the part of J₀ that does NOT
commute with itself under transposition. In physical terms: the
part that distinguishes "mode A coupling to mode B" from "mode B
coupling to mode A." This asymmetry is absent when all modes have
equal weight (uniform g) and present when the golden ratio
preferentially weights the (1/2, 2/3) modes.

Whether this 4-dimensional algebra has physical content — whether
it maps to a known gauge algebra — requires identifying its
structure constants. The commutator [J₀, J₀ᵀ] is nonzero, rank-2,
and block-diagonal in the (class A, class B) decomposition.
The block structure suggests two coupled 2-dimensional sectors,
but the algebra dimension (4) does not match any simple Lie
algebra (su(2) is 3-dimensional, so(4) is 6-dimensional).

## Status

**Established**:
- Three distinct zeros identified and separated
- The traceless projection J₀ = J on the Klein bottle (the identity
  component is the forbidden (0,0) mode)
- The 1+3 eigenvalue decomposition: {3/4, −1/4, −1/4, −1/4}
- The 3-dimensional redistribution space = n² − 1 = dim SL(2,ℝ) = d
- Connection to D17 rank-1 temporal causation: 1 temporal + 3 spatial

**New structure**:
- The golden-peaked commutator ‖[J₀, J₀ᵀ]‖ = 0.28 produces a
  4-dimensional algebra with nontrivial bracket. This exists only
  when the golden ratio breaks the mode symmetry AND r ≠ 0.
  Whether this is physical or an artifact of the specific g(ω)
  choice is open.

**Open**:
- Identify the 4-dimensional algebra's structure constants
- Determine whether the 15% antisymmetric component encodes
  gauge structure or is simply the golden ratio's asymmetry
  projected onto the mode space
- The 1+3 decomposition gives 3 spatial dimensions from the
  Jacobian eigenspace. Does the METRIC on this 3-space (induced
  by the Jacobian's eigenvalue ratio 3:1) match the spatial metric
  from D12-D13?
