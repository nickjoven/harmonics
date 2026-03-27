# d = 3 — Spatial Dimension

**Layer 1 derived type.** Proved from Layer 0 primitives: Z, mediant, fixpoint.

## Hypothesis

The spatial dimension is determined by the number of components in a fraction and the self-consistency of adjacency.

## Derivation

From **Z** + **mediant** + **fixpoint**:

1. **Fractions have 2 components**: a fraction `p/q` is a pair `(p, q)` of integers from Z.
2. **Adjacency is a 2x2 determinant**: the mediant adjacency condition `|ad - bc| = 1` is the condition that the matrix `[[a, c], [b, d]]` has determinant ±1.
3. **This generates SL(2, Z)**: the set of all 2x2 integer matrices with determinant 1. Every element of SL(2, Z) corresponds to a path in the Stern-Brocot tree (from rationals.md).
4. **Self-consistent adjacency** (fixpoint): the adjacency structure must be preserved under its own transformations. This is the fixed-point condition applied to the group action: the group that preserves adjacency must act on a manifold where it *is* the isometry group.
5. **Continuum limit**: SL(2, Z) embeds in SL(2, R) as a lattice. The self-consistency condition forces the manifold to equal the group manifold of SL(2, R).
6. **Dimension**: dim SL(2, R) = dim(2x2 real matrices) - dim(det = 1 constraint) = 4 - 1 = **3**.

Equivalently: dim SL(n, R) = n² - 1. For n = 2: d = 2² - 1 = **3**.

## Prediction

**d = 3** spatial dimensions.

## Test

Observed spatial dimensions = **3** ✓

This is not a fit — it is a derivation. The number 3 appears because fractions have exactly 2 components (numerator and denominator), and 2² - 1 = 3. If fractions had 3 components, we would predict d = 8.

## Dependencies

- `primitives/z.md` — provides the integers that form fraction components
- `primitives/mediant.md` — provides the adjacency condition `|ad - bc| = 1`
- `primitives/fixpoint.md` — provides self-consistent adjacency (the group must act on its own manifold)
- `derived/rationals.md` — provides the Stern-Brocot tree whose symmetry group is SL(2, Z)
