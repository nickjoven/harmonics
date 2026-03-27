# Engine Architecture

## Layers

The engine is built in four layers. Each layer composes elements from the layer below. No layer borrows definitions from outside the engine.

### Layer 0: Primitives (Axioms)

**Location**: `primitives/`

Four irreducible building blocks: Z, Mediant, Fixed Point, Parabola.

**Tested by**: necessity — remove one and show what breaks.

### Layer 1: Derived Types (Compositions of Primitives)

**Location**: `derived/`

Binary and ternary compositions of the four primitives. Examples:

- Z + Mediant = Q (the rationals, the Stern-Brocot tree)
- Z + Fixed Point = S^1 (the circle, periodicity)
- Z + Parabola = phi (the golden ratio, the Fibonacci sequence)
- Fixed Point + Parabola = saddle-node bifurcation
- Mediant + Parabola = Arnold tongue boundaries
- Mediant + Fixed Point = the locking condition

**Tested by**: consistency — each derived type must be well-defined and agree with all other derivations that produce the same object.

### Layer 2: Structures (Compositions of Derived Types)

**Location**: `structures/`

Compositions of Layer 1 objects into the full geometric and dynamical structures:

- Coupling constants from duty cycles (`coupling.md`)
- The Weinberg angle (`weinberg.md`)
- Three generations of fermions (`generations.md`)
- 12 gauge bosons (`gauge.md`)
- Clifford algebra Cl(3,1) (`clifford.md`)
- Conservation from compactness (`conservation.md`)
- Higgs mass from crossing curvature (`higgs.md`)

**Tested by**: self-consistency — the structure must satisfy the fixed-point condition globally, not just locally.

### Layer 3: Predictions (Numerical Outputs)

**Location**: `predictions/`

Concrete numbers derived from the structures, compared against observation. 12 predictions, all under 3.5% residual, no free parameters:

- α_s/α₂ = 27/8 (3.2%), sin²θ_W = 8/35 (1.1%), m_H = v/q₂ (1.6%)
- m_τ/m_e = 26^(5/2) (0.9%), Ω_Λ ∈ [13/19, 11/16] (within band)
- d = 3, signature (3,1), generations = 3, gauge bosons = 12 (all exact)
- Born exponent = 2, Cl(3,1), conservation (all exact)

**Tested by**: observation — the predicted number must match the measured number within stated precision.

## Design Principles

### Content-Addressable

Every node in the engine is identified by its definition, not by an arbitrary label. The definition IS the address. Two nodes with identical definitions are the same node, regardless of where they appear.

### Proof Chains

Every derivation carries a proof chain: a sequence of composition steps terminating at Layer 0 primitives. No derived object exists without an explicit path back to the four primitives.

### The Scientific Method

The engine follows one loop:

1. **Hypothesis**: state the claim (a primitive, a composition rule, a prediction).
2. **Prediction**: derive the numerical consequence.
3. **Test**: compare against observation or internal consistency.
4. **Refine**: if the test fails, the hypothesis is wrong — update it.

No hypothesis is protected from revision. The primitives themselves are hypotheses.

### Forward-Only Construction

The engine builds FORWARD from the four primitives. It never starts from a known result and works backward to justify it. If a result cannot be reached by forward composition, it is either (a) not yet derived or (b) outside the scope of the engine.
