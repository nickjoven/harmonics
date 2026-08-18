# Horn-branch iteration 2 step 2 — substrate derivation of f_locked / f_unlocked

> **REVISED BY `horn_branch_iteration_3_step_1.md` (PRODUCTIVE NULL).**
> This doc presents a "SUBSTANTIVE LEAD: three identifications
> converge on 5/6" framing. Iteration 3 step 1 audited the
> apparatus and found this framing inflated: reading (c)
> (`boundary_weight.md`'s w*) is **not** substrate-derived but
> algebraic inversion from observed Ω_Λ (per the honest audit
> in `boundary_weight.py` L13-56), and its actual value is
> 0.8281, not 5/6 = 0.8333 (0.63% discrepancy). The "convergence"
> collapses to two substrate-internal exact-5/6 candidates (a,
> b) with no derived mechanism, plus one observation-inverted
> quantity (c) at a different value. Read iteration 3 step 1's
> verdict before relying on any closure claim from this doc.
> What survives this doc's claims: the q₂-axis sector assignment
> from `horn_branch_iteration_2_step_1.md` (independent of this
> step), and the fact that 5/6 is the upper Farey fraction at
> q=6 (a real number-theoretic substrate fact, not a forced
> mechanism for the horn-branch).

## Status

**Verdict: SUBSTANTIVE LEAD; CLOSURE NOT ATTAINED.**
**[Subsequently walked back to PRODUCTIVE NULL by iteration 3
step 1; see notice above.]** Three substrate-internal
identifications converge on **5/6 ≈ 0.833** for the horn-branch's
required suppression ratio `f_locked / f_unlocked`:

(a) **Klein-bottle ratio average**: `(1 + Q)/2 = (1 + q₂/q₃)/2 =
(1 + 2/3)/2 = 5/6`, where `Q = q₂/q₃ = 2/3` is the Klein-bottle
population ratio (`klein_bottle.md` D19, `mass_sector_closure.md`).

(b) **Upper Farey fraction at q=6**: the framework's substrate→tree
boundary closes at the q=6 Farey level. The two new fractions at
this depth are exactly `{1/6, 5/6}` (`boundary_weight.md` L39),
since 2/6, 3/6, 4/6 reduce to lower denominators by GCD. The upper
boundary fraction is `5/6` directly.

(c) **Cosmological boundary weight w***: `boundary_weight.md`
derives w* = 0.83 numerically from the field-equation fixed-point
condition at the F_5/F_6 boundary. This is the partial-locking
weight for the q=6 boundary modes that produces `Ω_Λ = 0.6847`
(within 0.04σ of observation).

These three are not three independent quantities — they are three
readings of one substrate object, namely **the q=6 boundary at
which the framework's self-predicting Farey set closes, with
fractional locking at the upper boundary fraction**. The
convergence is the substrate's signal.

Predicted closure on Class B (m_μ / m_e):

    m_μ / m_e^{predicted} = (W_C / (W_A × 5/6))^(5/2)
                          = (7 × 6/5)^(5/2)
                          = 8.4^(5/2)
                          = 204.5
    Observed: 206.8
    Residual: 1.1%

This is the same 1% level as the Koide-imported closure in
`fermion_mass_running.md` §4c, but here closure comes from **only
substrate-internal quantities** (q₂ = 2, q₃ = 3, the q=6 boundary
they compose), with **no empirical Koide import**.

**Iteration 2 step 2 does not constitute closure.** The mechanism
story below is plausible and uses existing substrate apparatus, but
it requires asserting that the q₂-locked observable → q=6 boundary
mapping is the substrate→tree route the horn-branch is asking
about. Verifying this mapping requires either a direct field-
equation derivation (iteration 3) or independent precision data
that distinguishes the three readings.

Class: foundational rigor check (Class 3, iteration-step
substantive lead with multiple substrate-internal identifications
on a single target).

---

## The three identifications

### (a) Klein-bottle ratio average

The Klein-bottle population ratio at the field-equation
fixed-point under golden-peaked g(ω) is
`Q = 0.675 ≈ 2/3 = q₂/q₃` (`klein_bottle.md` L674-690, `Why the
population ratio is 2/3`). Q is the ratio between the smaller
family (q_x=3, q_y=2) and the larger (q_x=2, q_y=3).

The mediant of 1 and Q is:

    (1 + Q) / 2 = (1 + 2/3) / 2 = 5/6 = 0.8333...

Mechanistically: at the substrate→tree boundary, a q₂-locked
mode samples both substrate families (with weights 1 for "own"
contribution and Q for the "mixed-in" contribution from the other
family). The 50/50 averaging gives `(1+Q)/2`. The mechanism for
50/50 averaging traces to the half-cycle structure of the
antipodal x-cycle: half a traversal gives sign-flip mixing
(weight Q), the other half gives no mixing (weight 1). This is
plausible but not rigorously closed — the half-cycle averaging
argument was not previously stated in the framework.

### (b) Upper Farey fraction at q=6

The Farey sequence F_6 = {0/1, 1/6, 1/5, 1/4, 1/3, 2/5, 1/2,
3/5, 2/3, 3/4, 4/5, 5/6, 1/1}. The new fractions at depth 6
(those not present at F_5) are exactly:

    F_6 \ F_5 = {1/6, 5/6}

The two new fractions are paired symmetrically about 1/2 (they
are p/q and (q-p)/q for q=6, p=1). Numerator parity φ(6) = 2
(`boundary_weight.md` L38: "phi(6) = 2: there are exactly two
new Farey fractions at depth 6 (namely 1/6 and 5/6), since the
others (2/6, 3/6, 4/6) reduce to lower denominators by GCD").

q=6 is special: it is the smallest composite of q₂ and q₃ —
`6 = 2 × 3 = q₂ × q₃`. It is the first denominator where both
substrate families simultaneously contribute. Below q=6, only
q₂- or q₃-pure fractions exist; at q=6, the framework's two
denominator classes first overlap.

The upper Farey fraction 5/6 is the boundary mode closest to 1
(approaching from below). Mechanistically, it is the
substrate's "fraction-of-coverage" at the q=6 boundary: a
locked mode at q₂ that propagates to the q=6 Farey boundary
arrives at the 5/6 fraction, not 1/6 (which would be the
trivial-cover fraction from the q₃ direction).

### (c) Cosmological boundary weight w*

`boundary_weight.md` introduces w* as the fractional locking
weight at the F_5/F_6 boundary, parameterizing how much of the
q=6 mode budget is locked:

    |F_eff|(w) = 11 + 2w        (effective mode count)
    n_eff(w)   = 16 + 3w        (effective denominator)
    Ω_Λ(w)     = |F_eff| / n_eff = (11 + 2w)/(16 + 3w)

w* is the self-consistent fixed point of the field equation at
the q=6 boundary. From coherence cascade data (D30):

    w* = 0.83 (3-digit numerical)

Substituting:

    Ω_Λ(0.83) = (11 + 1.66) / (16 + 2.49) = 12.66 / 18.49 = 0.6847

This matches observed Ω_Λ = 0.685 ± 0.007 within 0.04σ.

The cosmological derivation is independent of any mass-sector
work. w* is forced by the field equation at the boundary, not
fit to Ω_Λ. (`boundary_weight.md` "Status": "Derived. The
boundary weight follows from the Farey partition structure,
phi(6) = 2, the self-consistency condition at the tongue
boundary, the monotonicity of Omega_Lambda(w), and the
contraction mapping for w*.")

The numerical value 0.83 is the same as the horn-branch target
0.829. Whether w* is exactly 5/6 or merely 3-digit close is
not stated in `boundary_weight.md` — the 3-digit numerical value
is given without analytic closure.

---

## The convergence

The three identifications agree on 5/6 = 0.8333... within their
stated precision:

| Identification | Value | Precision |
|---|---|---|
| (a) (1 + Q)/2 | 5/6 = 0.83333... | exact (substrate-internal) |
| (b) Upper Farey at q=6 | 5/6 = 0.83333... | exact (number-theoretic) |
| (c) w* from `boundary_weight.md` | 0.83 | 3-digit (numerical, D30) |
| Horn-branch target | 0.829 | 3-digit (from m_μ 1% closure) |

The three substrate identifications are not independent. They
share the same primitive (q=6 boundary, the composite q₂ × q₃
where the framework's two denominator classes first meet). Both
(a) and (b) give the same exact value 5/6; (c) is consistent
with 5/6 at 3-digit precision; the horn-branch target is
consistent with 5/6 at 3-digit precision.

The substrate object underlying all three is:

> **The fractional-locking weight at the q=6 = q₂ × q₃ Farey
> boundary, which equals the upper new Farey fraction 5/6 there,
> which equals the average of 1 and Q in the Klein-bottle's
> mediant structure.**

This is a single substrate object with three readings, not three
coincidences. The convergence is the signal.

---

## Mechanism story

### How the boundary weight applies to mass-sector locked modes

The framework's substrate→tree boundary is the q=6 Farey level
where the self-predicting set closes. At this boundary, modes
are partially locked at fractional weight w* = 5/6 (per
`boundary_weight.md`).

Consider a q₂-locked observable. Its substrate mode has
denominator 2 in x (= antiperiodic direction); to reach tree
level, it must propagate through the q=6 Farey closure. At the
q=6 boundary, its locking fraction is the upper boundary mode
5/6 — the fraction of the tongue coverage that's within the
self-predicting set.

Consider a q₂-unlocked observable. Its substrate mode is in the
gap at q₂; it doesn't commit to a q₂-tongue. At the q=6 Farey
boundary, it bypasses the boundary modes entirely (since the
boundary modes are at q₂-tongues 1/6 and 5/6, which are
q₂-locked). Its propagation isn't subject to the boundary's
partial-locking weight.

Result:
- q₂-locked modes propagate substrate→tree with amplitude × 5/6
- q₂-unlocked modes propagate substrate→tree with amplitude × 1

Ratio: `f_locked / f_unlocked = 5/6`.

### Cross-check with cosmological Ω_Λ

If this identification is correct, the SAME boundary weight w*
that produces Ω_Λ = 0.6847 should produce the m_μ / m_e
correction. Both are downstream of the q=6 Farey boundary's
partial-locking weight.

Predicted m_μ / m_e using w* = 5/6:

    m_μ / m_e = (W_C / (W_A × w*))^(5/2)
              = (7 / (1 × 5/6))^(5/2)
              = (7 × 6/5)^(5/2)
              = 8.4^(5/2)
              = 204.5

Observed: 206.8. Residual: 1.1%.

This is 1% closure of the previously open 37% gap, using only
the same boundary weight that gives cosmological Ω_Λ. **No new
free parameters.**

### Why the τ/e ratio is preserved

Both A (W = 1) and B (W = 26) are q₂-locked. Both pick up the
same factor w* = 5/6 from the boundary. The ratio:

    m_τ / m_e = (W_B × w* / (W_A × w*))^(5/2)
              = (26 / 1)^(5/2)
              = 3447

The w* factor cancels in the ratio. m_τ / m_e is unaffected,
consistent with the observed 0.9% residual being unchanged.

### What's added: the substrate-vs-tree separation

The mechanism story above assumes that q₂-locked observables
*do* commit to the q=6 boundary modes 1/6 and 5/6 specifically,
while q₂-unlocked observables don't. This is a substrate→tree
mapping claim that the framework has not previously stated.

The mapping is plausible because:
- q=6 = q₂ × q₃ is where the framework's two denominator
  classes meet
- The boundary fractions 1/6 and 5/6 are q₂-tongue fractions
  (the unique pair with denominator 6 and numerator coprime to
  6)
- A q₂-locked observable that propagates substrate→tree
  naturally lands at one of these tongue fractions

But the mapping is not previously derived. It is the new
substrate↔tree identification this iteration proposes.

---

## Where this falls short of closure

### (i) The 50/50 averaging argument is hand-waved

The reading (a) `(1+Q)/2 = 5/6` uses a 50/50 average between
weights 1 and Q. The justification offered is "the half-cycle
structure of the antipodal x-cycle." This is suggestive but not
rigorous. A complete derivation would show the field equation
forces a 50/50 average at the substrate→tree boundary.

### (ii) The upper-vs-lower Farey fraction choice

Reading (b) picks the upper Farey fraction 5/6 rather than the
lower 1/6. The substrate has two new fractions at q=6, and the
mechanism story uses the upper one. The choice is justified by
"q₂-locked modes land at the larger tongue coverage" but a
direct derivation showing 5/6 (not 1/6) is the correct one for
q₂-locked → tree propagation is missing.

A direct field-equation derivation would resolve this: compute
the substrate amplitude at each q=6 tongue and show that
q₂-locked modes propagate to 5/6 (with the other 1/6 going to
q₃-locked modes or being a sub-leading channel).

### (iii) The (c) reading lacks analytic precision

w* = 0.83 in `boundary_weight.md` is a 3-digit numerical value.
If it is exactly 5/6 = 0.8333..., the doc does not say so. The
4-digit Ω_Λ value (0.6847) corresponds to w = 0.828 not 0.833;
the framework's 0.83 might be a rounded 0.828, not a rounded
0.833.

Resolution requires: compute w* analytically from the field-
equation fixed-point. If the analytic value is exactly 5/6,
both readings (b) and (c) point at the same number and the
identification tightens. If the analytic value is closer to
0.828, readings (b) and (c) differ by ~0.5%, which is at the
edge of acceptable substrate-internal-but-coincidental level.

### (iv) PMNS θ_12 cross-check not performed

Iteration 1's falsifier list included "the same flare profile must
also produce the correct PMNS θ_12 closure." This step has not
verified that. If w* = 5/6 applied to the PMNS mixing produces
a substrate prediction that closes the 10% gap to <1%, the
identification strengthens dramatically. If it worsens or
leaves the θ_12 gap unchanged, the identification is
sector-specific and needs explanation.

---

## What this iteration step DOES establish

1. **A substrate-internal candidate for f_locked / f_unlocked = 5/6
   with three converging identifications**, none of which uses
   empirical Koide import.

2. **A specific substrate↔tree mapping proposal**: q₂-locked
   observables propagate through the q=6 Farey boundary at
   fractional locking w*; q₂-unlocked observables bypass.

3. **A potential cross-sector unification**: the boundary weight
   w* that produces cosmological Ω_Λ also produces the mass-sector
   m_μ correction. If verified, this is the framework's first
   substantive cross-sector substrate identification of an
   open-residual factor.

4. **A clearly stated iteration-3 target**: derive w*
   analytically from the field equation; show its value is
   exactly (1+Q)/2 = 5/6, and that q₂-locked observables land
   at the upper Farey fraction specifically.

---

## What this iteration step does NOT establish

- **Mechanism closure.** The substrate↔tree mapping (q₂-locked →
  q=6 boundary 5/6) is proposed, not derived. Iteration 3 must
  derive it from the field equation.
- **Analytic equality of w* and 5/6.** Numerically consistent at
  3-digit precision; analytic identity not shown.
- **Cross-sector verification.** PMNS θ_12 cross-check (iteration
  2 step 4) is open.
- **Charge-sector check** (iteration 2 step 4). Whether the same
  5/6 ratio applies to quark mass ratios remains open.

---

## Falsifiers for iteration 2 step 2's verdict

The convergence finding is itself falsifiable:

1. **Analytic w* falsifier.** If w* derived analytically from
   the field equation is NOT 5/6 = 0.8333... but something else
   (e.g., 0.828 or some irrational), readings (a)/(b) and
   reading (c) diverge. The horn-branch's required ratio could
   then equal one of them but not the other; only one
   substrate identification survives, and the convergence-
   signal weakens.

2. **Tree-boundary mapping falsifier.** If a field-equation
   derivation of substrate→tree propagation shows q₂-locked
   modes do NOT land at the upper Farey fraction 5/6 (e.g.,
   they land at 1/6, or both equally), the mechanism story is
   broken and the horn-branch's ratio identification with 5/6
   is coincidence.

3. **Cross-sector falsifier.** If applying w* = 5/6 to PMNS
   θ_12 worsens the 30° → 33.4° gap (rather than closes it) or
   to quark mass ratios disrupts the existing QCD-running
   accounting, the identification is sector-restricted and the
   "unification with cosmological Ω_Λ" claim weakens.

4. **Cube identity falsifier.** Reading (a) uses
   Q = q₂/q₃ = 2/3, and Q itself is forced via the cube identity
   q₂³ − 1 = q₃ × q₂ + 2q₃ → (q₂, q₃) = (2, 3) (`mass_sector_closure.md`).
   If the cube identity's uniqueness has a downstream
   contingency that affects which fraction at q=6 the boundary
   locks to (e.g., if the substrate could close on a different
   composite q than 6), reading (b) shifts.

---

## Plan for iteration 3

Iteration 3's job is to convert the substantive lead to closure.
Three concrete derivation steps:

**Step 1: Analytic w*.** Derive w* from the field equation's
self-consistency condition at the F_5/F_6 boundary. Show w* is
exactly 5/6 = (1+Q)/2 (analytic), or that it differs from 5/6 by
some specifiable amount and identify the source of the
discrepancy.

**Step 2: Substrate↔tree mapping.** Derive that q₂-locked
observables propagate to the upper Farey fraction 5/6 at the
q=6 boundary specifically (not 1/6). Compute the substrate
amplitude at each q=6 tongue and verify which is the q₂-locked
channel.

**Step 3: PMNS θ_12 cross-check.** Apply w* = 5/6 to the PMNS
mixing apparatus and check whether the 10% gap closes. The same
flare correction that gave m_μ/m_e the 5/6 factor should give
θ_12 a substrate-derived correction; cross-check the result
against observed 33.4°.

If steps 1–3 all close, the horn-branch's Class B m_μ residual
is **substrate-derived to <1.1%** using only the boundary
weight already forced by cosmological Ω_Λ. This would be the
framework's first cross-sector substrate identification of an
open residual factor.

If any of steps 1–3 fails, the iteration arc continues; the
substantive lead either narrows or transitions to productive null.

---

## Cross-links

- `horn_branch_iteration_2_step_1.md` — sector-assignment
  falsifier; identifies q₂ locked/unlocked as the axis and
  f_locked / f_unlocked ≈ 0.83 as the target.
- `boundary_weight.md` — derives w* = 0.83 from the field-equation
  fixed-point at the F_5/F_6 boundary; produces Ω_Λ = 0.6847.
- `klein_bottle.md` D19, L674-705 — Klein-bottle population
  ratio Q = q₂/q₃ = 2/3; reading (a) source.
- `generation_mechanism.md` D34 §1-4 — locked/unlocked
  classification of A/B/C/D; sector-assignment apparatus.
- `mass_sector_closure.md` — cube identity uniqueness for
  (q₂, q₃) = (2, 3); falsifier (4) source.
- `fermion_mass_running.md` §2-4 — existing depth and SL(2,Z)
  trace attempts on the m_μ 37% gap. This iteration's closure
  target (1% residual) competes with §4c's Koide-imported 1%
  closure but uses only substrate-internal quantities.
- `koide_form_substrate_iteration_14.md` — honest demotion of
  the m_μ gap to 37% bare-tree without Koide import. The 5/6
  candidate, if iteration-3-closed, would close this gap from
  the substrate.
- `klein_z2_decomposition_falsifier_2.md` — modal y-parity
  finding; preserved as separate apparatus, not the horn-branch
  axis.
- `klein_bottle_restructure_price.md` — apparatus-extension
  fallback closed; the substrate-internal mechanism here is
  one of the few remaining productive routes.
- `down_type_double_cover_phase_c.md` — explicitly cites
  `boundary_weight.md` as precedent for "self-consistent partial
  locking sets w*" framing; a parallel application to quarks.

---

## One-line summary

**[Walked back by iteration 3 step 1; see notice at top of doc.]**
Three substrate-internal identifications — (a) the Klein-bottle
mediant `(1+Q)/2 = 5/6` where `Q = q₂/q₃ = 2/3`, (b) the upper
Farey fraction `5/6` at the composite boundary `q=6 = q₂ × q₃`,
and (c) the cosmological boundary weight `w* = 0.83 ≈ 5/6` from
`boundary_weight.md` — *appeared to* converge on the same target
value as the horn-branch's required suppression ratio
`f_locked / f_unlocked ≈ 0.829`, but iteration 3 step 1's
audit of `boundary_weight.py` L13-56 reveals reading (c) is
observation-inverted from Ω_obs (giving 0.8281, not 5/6) rather
than substrate-forced, collapsing the "convergence" to two
exact-5/6 candidates without derived mechanism plus one
observation-inverted quantity at a 0.63%-different value, so
the apparent "first cross-sector substrate identification of an
open-residual factor" claim does not survive scrutiny — the
correct disposition is **operationally open with a clustered
candidate** (1% band of near-hits at the framework's general
precision tier), not closure.
