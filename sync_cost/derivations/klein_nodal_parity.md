# Klein nodal parity: null result

## Status

**Null.** Gradient descent on `U = Y²` is Z₂-symmetric for all ℓ,
so the proposed parity ladder cannot discriminate even from odd ℓ.
`framework_status.md` Eliminated; `numerology_inventory.md` Class 2.

## Derivation of the null

The simulator (`github.com/nickjoven/simulation`, `common.js` + `docs/5`)
uses real spherical harmonics and descent on `Y²`:

    Y = √2 · K · cos(m·φ) · P_ℓ^|m|(cos θ)     (for m > 0)
    U = Y · Y

Under antipodal identification (θ, φ) → (π − θ, φ + π):

- cos(ℓ(φ+π)) = (−1)^ℓ · cos(ℓφ)
- P_ℓ^ℓ(cos(π−θ)) = P_ℓ^ℓ(−cos θ) = (−1)^(2ℓ) · P_ℓ^ℓ(cos θ) = +P_ℓ^ℓ(cos θ)
- Y(antipode) = (−1)^ℓ · Y(θ, φ)
- **U(antipode) = [(−1)^ℓ]² · Y² = U(θ, φ)**

U is Z₂-symmetric for both even and odd ℓ. The (−1)^ℓ sign flip
appears only in the signed field Y, not in the observable U = Y².
Seeds descending gradient of U see the same landscape regardless
of parity. At ω_rot = 0, even-ℓ and odd-ℓ runs at (ℓ, ℓ, 1)
produce indistinguishable seed distributions on the same nodal
skeleton (2ℓ meridional arcs meeting at 2 poles).

## The (5, 5, 1) image

Observed at ω_rot = 0.03 (not 0) and γ = 5. A slowly-rotating
static landscape with finite descent rate lets seeds track one of
the 10 meridional arcs as the nodal set rotates — producing a
single visible line without topological content. Fully explained
by gradient descent on a rotating Z₂-symmetric landscape; not a
Möbius signature.

## What a discriminating test would require

An observable that sees the (−1)^ℓ sign flip needs one of:

1. **Gradient descent on Y (signed), not Y² (unsigned).** Picks up
   the sign flip under Z₂ directly.

2. **Seed tracking by IC-region sign.** Color seeds by the sign of
   Y at their initial position; check whether opposite-sign classes
   remain disjoint (even ℓ) or merge (odd ℓ).

3. **Berry-phase probe.** Parallel-transport a phase around a closed
   loop on the quotient space; check for π rotation (odd ℓ) vs
   trivial return (even ℓ).

None is in the current simulator; building one is out of scope for
this repository.

## Cross-references

| File | Role |
|---|---|
| `klein_bottle.md` | Z₂-quotient substrate; still-valid by other arguments |
| `framework_status.md` | Eliminated entry with pointer here |
| `numerology_inventory.md` | Class 2 entry |
