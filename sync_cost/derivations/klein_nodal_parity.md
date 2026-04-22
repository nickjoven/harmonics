# Klein nodal parity: a direct test of substrate non-orientability

## Status

**Retracted (2026-04-22).** The test as formulated cannot discriminate
even from odd ℓ, because the potential the simulator uses is Z₂-
symmetric for all ℓ. The derivation below shows why; the
parity-ladder control runs would have been uninformative even if
collected. This file is kept as a record of the null result.

## Why retracted

The simulator (`github.com/nickjoven/simulation`, `common.js` + `docs/5`)
uses **real** spherical harmonics and descent on `Y²`:

    Y = √2 · K · cos(m·φ) · P_ℓ^|m|(cos θ)     (for m > 0)
    U = Y · Y

Under antipodal identification (θ, φ) → (π − θ, φ + π):

- cos(ℓ(φ+π)) = (−1)^ℓ · cos(ℓφ)
- P_ℓ^ℓ(cos(π−θ)) = P_ℓ^ℓ(−cos θ) = (−1)^(2ℓ) · P_ℓ^ℓ(cos θ) = +P_ℓ^ℓ(cos θ)
- Y(antipode) = (−1)^ℓ · Y(θ, φ)
- **U(antipode) = [(−1)^ℓ]² · Y² = U(θ, φ)**

So the potential U is Z₂-symmetric for *both* even and odd ℓ. Seeds
descending gradient of U see the same landscape regardless of parity.
The (−1)^ℓ distinction appears only in the signed field Y, not in
the observable U = Y² the sim evolves against.

At ω_rot = 0 (the test-spec condition), even-ℓ and odd-ℓ runs at
(ℓ, ℓ, 1) should produce indistinguishable seed distributions on the
same nodal skeleton — 2ℓ meridional arcs meeting at 2 poles — for
every ℓ. No parity alternation is predicted by the actual dynamics.

## Status of the suggestive (5, 5, 1) image

The single connected diagonal line observed in-session at (5, 5, 1)
was at **ω_rot = 0.03, not 0**, and γ = 5 (non-zero drift). With
rotating potential and finite descent rate, seeds can track one of
the 10 meridional arcs as the potential slowly rotates the nodal set
around the axis — producing a single visible line without any
topological content.

That observation does not support the Möbius prediction and is fully
explained by: gradient descent on a slowly-rotating static landscape,
with seeds following whichever arc the initial conditions placed
them nearest to.

## What would be needed for a real test

An observable that distinguishes even from odd ℓ via the Z₂ quotient
would require one of:

1. **Gradient descent on Y (signed), not Y² (unsigned).** The signed
   field picks up the (−1)^ℓ sign flip under Z₂. Not what the current
   simulator does.

2. **Seed tracking by IC-region sign.** Color seeds by the sign of
   Y at their initial position, then observe whether seeds with
   opposite initial signs remain in disjoint classes (even ℓ,
   Z₂-invariant basins) or merge (odd ℓ, sign-flipping Z₂).
   Requires sim changes.

3. **Berry-phase probe.** Parallel-transport a phase around a closed
   loop on the quotient space and check whether it returns to itself
   (even ℓ) or picks up a π rotation (odd ℓ). Requires a different
   observable altogether.

None of the above is in the current simulator, and constructing any
of them is outside the scope of this repository.

## Retraction category

- `framework_status.md`: moved from Proposed → Eliminated.
- `numerology_inventory.md`: moved to Class 2 (suggestive coincidence
  with no structural derivation — the suggestive (5, 5, 1) image is
  accounted for by gradient descent on a rotating static potential,
  not by Z₂ non-orientability).

## Cross-references

| File | Role |
|---|---|
| `klein_bottle.md` | Z₂-quotient substrate; still-valid by other arguments |
| `framework_status.md` | Eliminated entry with pointer here |
| `numerology_inventory.md` | Class 2 entry |
| `basin_11_connection_exploration.md` | Sibling study, unaffected — that test concerns basin-area tiering, not Z₂ parity |
