# The Feigenbaum route to a_1(lep) and K_STAR

## Claim the route proposes

The framework's lepton identity `a_1(lep) · K_STAR = q_2 = 2` pins
`a_1(lep)` from PDG mass ratios. If instead `a_1(lep)` were, independently,
a universal scaling constant of the rational field equation restricted
to the lepton sector's Fibonacci backbone, then `K_STAR = 2 / a_1(lep)`
would be derivable from the framework's substrate alone — no PDG.

The natural universality class to look at is the **golden-mean critical
circle map** (Shenker 1982; Feigenbaum-Kadanoff-Shenker 1982; MacKay 1982;
Rand 1987; de Faria-de Melo 1999), because the lepton sector's base pair
`(3/2, 5/3) = (F_4/F_3, F_5/F_4)` is the first two inverted Fibonacci
convergents of `φ`, and the framework's rational field equation uses
Arnold tongue widths which are exactly the objects Shenker's
renormalization group acts on.

## Why the Fibonacci restriction is the right move

`K_star_iteration.py` shows that the field equation `r → |Σ g·w·e^(2πip/q)|`
iterated on any ensemble (Fibonacci, Stern-Brocot, Farey) has local
linearization `r_{n+1} = (K_0/2)² · r_n² + O(r_n^3)` near `r = 0`. The
exponent 2 equals `q_min = q_2`, the prefactor is the q=2 tongue width.
`r = 0` is a quadratic-superstable fixed point of the map, and
`K_STAR = 0.862` sits **below** the upper-branch nucleation (~K_0 = 3)
that would give a nontrivial `r`. The iteration's fixed point therefore
cannot be `K_STAR` — `K_STAR` is not a synchronization order parameter
of this map at all, it is the parabola primitive's coordinate scale at
the matter sector.

But that argument kills `K_STAR` as a **fixed point**, not as a **scaling
exponent**. The Feigenbaum route proposes that `a_1(lep)` is the latter:
not where the iteration settles, but the universal ratio governing how
successive Fibonacci terms contribute to the sum. This is the object
Shenker's RG computes for critical circle maps — and Shenker's constants
`α_GM` and `δ_GM` are known numbers in the right ballpark.

## Shenker's constants for the golden-mean critical circle map

Define `f_K(θ) = θ + Ω - (K/2π) sin(2πθ)`. At `K = 1` the map is critical.
Fix `Ω` such that the rotation number is `1/φ` (golden mean). The Shenker
renormalization `T[f] = α · f ∘ f(·/α)` has a fixed-point functional `f*`
with two universal scaling constants:

    α_GM ≈ 1.288574...         (spatial scaling)
    δ_GM ≈ 2.833612...         (parameter scaling)

These are the golden-mean analogs of Feigenbaum's period-doubling `α` and
`δ`. They govern the self-similarity of the critical circle map under
successive Fibonacci-level rescalings: an F_n-orbit rescales to an
F_{n+1}-orbit by factor `α_GM` in space and `δ_GM` in parameter.

`K_star_iteration.py` verifies that the framework's `r → 0` approach has
quadratic form `(K/2)² r²`, which is the leading local expansion of the
framework's map. The framework's map is a Fourier-like sum, not a
functional iterate, so it is not literally Shenker's map — but its
**universality class may be related**, because both are built on Arnold
tongue widths at Fibonacci convergents to `1/φ`.

## Candidate relations

The route's hope is that some clean combination of `α_GM`, `δ_GM`, and
framework primitives produces `a_1(lep)` at PDG precision. The candidates
tested in `feigenbaum_route.py`:

### Candidate 1: `a_1 = |δ_GM| / (d · log(b_1))`

Reads `a_1` as "`|δ_GM|` per unit of the lepton generation step":

    a_1(lep) ?= |δ_GM| / (d · log(3/2))
             = 2.833612 / (3 · 0.405465)
             = 2.329516

Observed: `a_1(lep) = 2.320292`. **Gap: 0.40%**.

This is equivalent to claiming `log(m_τ / m_μ) = |δ_GM|`:

    log(1776.86 / 105.66) = 2.82225
    |δ_GM|                = 2.83361

Gap 0.40%. Suggestive but well outside PDG precision on `a_1` (~0.002%).

### Candidate 2: `α_GM · δ_GM = d · q_3 · log(b_1)`

Reads the product of Shenker's two constants as the framework's
dimensionful lepton-sector measure:

    |α_GM| · |δ_GM| ?= d · q_3 · log(3/2)
                    = 9 · 0.405465
                    = 3.649186

Shenker product: `1.288574 · 2.833612 = 3.651519`. **Gap: 0.064%**.

This gap is at the edge of the tabulated precision of Shenker's
constants — `α_GM` and `δ_GM` are typically quoted to 6 or 7 digits in
the standard literature, so a 0.06% difference is within tabulation
noise. It is **not yet ruled out that the relation is exact**; a rigorous
bound on Shenker's constants tighter than 10⁻⁴ is needed to settle it.

If exact, this gives `a_1` via `α_GM = (d · q_3 · log(3/2)) / δ_GM`,
which is a constraint on `δ_GM` alone once you accept Candidate 1's
form. The two candidates together over-determine the system if both
are exact, so they cannot both be exact unless Shenker's `(α_GM, δ_GM)`
satisfy both relations simultaneously.

### Candidate 3: Jensen-Bak-Bohr Hausdorff dimension ≈ K_STAR

The Cantor set of non-mode-locked rotations of the critical circle map
at `K = 1` has Hausdorff dimension (Jensen, Bak, Bohr 1984;
Cvitanović-Shraiman-Söderberg 1985):

    D_H ≈ 0.870055...

Compare to `K_STAR = 0.861961`. **Gap: 0.93%**.

A worse fit than the Shenker candidates, but structurally cleaner: the
Hausdorff dimension of the framework's own non-locked set would be
exactly the kind of universal constant the route needs. The 1% gap may
reflect either (a) the framework's set is not literally the JBB Cantor
set, or (b) the tabulated `D_H` is imprecise (it has been revised
several times in the literature).

### Candidate 4: Gauss map entropy ≈ a_1(lep)

The Gauss map `T(x) = {1/x}` has metric entropy

    h_Gauss = π² / (6 log 2) ≈ 2.373138

Compare to `a_1(lep) = 2.320292`. **Gap: 2.28%**.

Rejected — too large a gap to be the sharp answer, though it is
suggestive that the Gauss map's entropy (the natural scaling of continued
fraction convergents) is in the same ballpark.

## Summary of the candidate gaps

| candidate | prediction | observed | gap |
|---|---|---|---|
| `δ_GM/(d·log(3/2))` → a_1 | 2.3295 | 2.3203 | **0.40%** |
| `α_GM·δ_GM/(d·log(3/2))` → q_3 | 3.0018 | 3.0000 | **0.06%** |
| `D_JBB` → K_STAR | 0.8700 | 0.8620 | **0.93%** |
| `h_Gauss` → a_1 | 2.3731 | 2.3203 | **2.28%** |

None of them matches `a_1(lep)` or `K_STAR` at PDG precision
(~0.002%). The sharpest (Candidate 2) is 30× PDG but at the edge of
Shenker's tabulated precision, so it cannot yet be confirmed or ruled
out without higher-precision values of `α_GM` and `δ_GM`.

## What the Feigenbaum route still has not produced

The route's milestones are:

1. Identify a framework-internal renormalization operator (analogous
   to Shenker's T). **Not done.** The framework's field equation is a
   sum over modes, not a functional iterate; the analog of Shenker's T
   is not yet written down.

2. Prove that the framework's RG has a fixed point with universal
   scaling constants. **Not done.** This requires the operator from
   step 1.

3. Compute the framework's own `α` and `δ` analogs. **Not done.**
   In the absence of step 1, we can only compare to Shenker's constants,
   which live in a neighbouring universality class.

4. Relate the framework's universal constants to `a_1(lep)` by a clean
   structural identification. **Open.** Several algebraic forms have
   been tried (Candidates 1-4); none match at PDG precision.

Step 1 is the blocker. Until the framework's own RG operator is defined,
the "Feigenbaum route" is a motivated conjecture that pattern-matches
to Shenker's constants at the 0.1-1% level, not a derivation.

## What a successful closure would look like

- A framework-internal RG operator `T` acting on the Fibonacci-restricted
  field equation.
- A proof (or numerical demonstration at high precision) that `T` has a
  fixed point with universal scaling constants.
- A clean algebraic relation between those constants and `a_1(lep)` or
  `K_STAR`, verified to at least PDG precision (~10⁻⁵ relative).
- Ideally: `a_1(lep) = 2.3202917...` to 7+ digits, falling out without
  any PDG input.

If this closure exists and Shenker's universality class is the right
one, Candidate 2's 0.06% gap should collapse to zero under higher-precision
Shenker values, and the relation `α_GM · δ_GM = d · q_3 · log(b_1)`
should be provable. That is the single most testable prediction of the
route's current form.

## What a failure would look like and what it would mean

- Higher-precision Shenker constants confirm the 0.06% gap in
  Candidate 2. In that case `α_GM · δ_GM` is not the right structural
  object, and the framework's RG (if it exists) is in a different
  universality class from Shenker's.
- The framework's own RG operator has no fixed point, or has one but
  with scaling constants that are not expressible in framework primitives.
- No natural algebraic combination produces `a_1(lep)` at PDG precision.

Any of these would mean `K_STAR` cannot be derived from a Feigenbaum-style
iteration of the field equation, and the framework's only remaining
route to `K_STAR` without PDG would have to come from somewhere else
entirely — for example, from a direct self-consistency of the parabola
primitive's coordinate scale at `x² = μ = q_2²`, which is a different
kind of structural argument.

The honest current state is that **the Feigenbaum route has not closed
K_STAR**, has several suggestive near-matches at the 0.1-1% level, and
is blocked on the definition of the framework's own RG operator. The
probe script `feigenbaum_route.py` quantifies all four candidates and
the Fibonacci-backbone tongue-width scaling numerically.

## References

- Shenker, S. (1982). "Scaling behavior in a map of a circle onto
  itself: empirical results." *Physica D* **5**, 405–411.
- Feigenbaum, M. J., Kadanoff, L. P., Shenker, S. J. (1982).
  "Quasiperiodicity in dissipative systems: a renormalization group
  analysis." *Physica D* **5**, 370–386.
- MacKay, R. S. (1982). *Renormalisation in area-preserving maps.*
  PhD thesis, Princeton.
- Jensen, M. H., Bak, P., Bohr, T. (1984). "Transition to chaos by
  interaction of resonances in dissipative systems." *Phys. Rev. A*
  **30**, 1960.
- Rand, D. A. (1987). "Global phase space universality, smooth
  conjugacies and renormalisation." *Nonlinearity* **1**, 181–202.
- de Faria, E., de Melo, W. (1999). "Rigidity of critical circle
  mappings I." *J. Eur. Math. Soc.* **1**, 339–392.
- Cvitanović, P., Shraiman, B., Söderberg, B. (1985). "Scaling laws
  for mode lockings in circle maps." *Physica Scripta* **32**, 263.
