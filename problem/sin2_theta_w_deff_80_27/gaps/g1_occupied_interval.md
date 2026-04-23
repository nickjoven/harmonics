# Gap 1: Occupied-interval → effective-dimension reduction

## What must be proven

Derive

    d_eff = d − 1/q₃^d

as the effective dimension seen by the electroweak mixing-angle
measurement at K = 1, starting from the geometric statement that
the q₃ Arnold tongue occupies a fraction `1/q₃^d` of the frequency
axis and extends uniformly across the (d−1)-dimensional spatial
manifold.

## What is given (from `../context/`)

- Configuration space at the root (1/1) of the Stern-Brocot tree
  decomposes as `Ω × M^{d−1}`, where Ω ∈ [0, 1] is the frequency
  (rotation-number) axis and M^{d−1} is the remaining spatial
  manifold (`context/three_dimensions.md`, d = 3).
- The q₃ = 3 tongue is a strip in this space
  (`context/klein_bottle.md`): width `1/q₃^d = 1/27` in Ω, full
  extent in M^{d−1}.
- The duty-cycle formula `duty(q) = 1/q^d` at K = 1
  (`context/duty_dimension.md`).

## What is currently heuristic

`sinw_effective_dimension.md` §"Effective dimension" argues:

> The q₃ tongue locks a fraction `1/q₃^d` of the frequency axis,
> removing it from the available degrees of freedom for the
> mixing-angle measurement. The remaining frequency interval has
> effective length `L_eff(Ω) = 1 − 1/q₃^d = 26/27`. The (d−1)
> spatial dimensions are unaffected ... The total effective
> dimension is therefore `d_eff = (d − 1) + L_eff(Ω) = d − 1/q₃^d`.

This is a **dimensional-analysis hand-wave**. Three specific
claims are asserted without derivation:

1. The mixing-angle integral **reduces** to an integration over
   the complement of the q₃ tongue (i.e., `Ω \ tongue`). Why not
   a weighted average? Why not the full Ω with a density
   correction?

2. The "effective length" of the Ω interval **enters as an
   exponent** in the duty-cycle formula (`q^d_eff` not `q^d ·
   L_eff` or `q^d + f(L_eff)`). The substitution `d → d_eff =
   (d − 1) + L_eff` is a specific ansatz that hasn't been
   derived from first principles.

3. The (d − 1) **spatial dimensions are unaffected**. This is
   asserted because the tongue is spatially uniform — but a
   full calculation would show integrations over M^{d−1} do not
   pick up correction factors either, or if they do, those would
   shift d_eff further.

## Success criterion (structural)

Produce a derivation with the form:

    Integrand of the mixing-angle ratio = f(Ω, M^{d−1}, q_i)
    ∫_{Ω × M^{d-1}} [integrand] dΩ dM^{d-1}
      = [sin²θ_W at effective dimension]
      = q₂^{d_eff} / (q₂^{d_eff} + q₃^{d_eff})

with `d_eff = d − 1/q₃^d` emerging from the explicit computation
of the integral, not posited. Every step derived from (q₂, q₃, d)
and the tongue geometry; no fitted factors.

## Failure criterion

Any of:

- The integration produces `d_eff = d − c/q₃^d` with `c ≠ 1`.
  Would kill Z2: the coefficient is a fitted factor.
- The integration produces a different functional form (e.g.,
  `sin²θ_W = f(q₂, q₃, d) · g(L_eff)` with g not expressible as
  an exponent substitution). Would kill the d_eff ansatz.
- The (d−1) spatial dimensions turn out to contribute a
  non-trivial correction. Would shift d_eff to some other value;
  Z1 would have to be re-tested.

## Consistency check

With `d_eff = 80/27` and the bare formula:

    sin²θ_W = 2^{80/27} / (2^{80/27} + 3^{80/27}) = 0.23123

matches PDG 0.23121 ± 0.00004 at 0.5σ. Any derivation that
produces a DIFFERENT d_eff (e.g., from correcting the
"(d−1) unaffected" step) must then either:
- Also match PDG within 1σ, or
- Demote the claim from "structural" back to Class 4 or lower.

## Suggested derivation path

The natural direction is an explicit Fubini-style computation of
the mixing-angle observable as an integral:

    sin²θ_W = ∫ (Ω ∖ tongue_{q₃}) × M^{d−1} (q₂ contribution)
             / ∫ (Ω ∖ tongue_{q₃}) × M^{d−1} (q₂ + q₃ contribution).

This requires:
- A precise definition of "the mixing-angle integrand" from the
  duty-cycle dictionary.
- The explicit form of the q₃ tongue-strip geometry in
  Ω × M^{d−1}.
- Evaluation of the volume integrals and extraction of the
  functional form in d_eff.

A concrete attempt would live in `../attempts/g1_integral_derivation.md`.

## Cross-references

- `../claim.md`
- `../context/duty_dimension.md`
- `../context/three_dimensions.md`
- `../context/klein_bottle.md`
- `../nulls/null_3_k_scan.md` (why finite-K alternatives won't work)
- `../../../sync_cost/derivations/sinw_effective_dimension.md:51-95`
