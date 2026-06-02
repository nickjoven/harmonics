# Horn-branch iteration 2 step 1 — sector-assignment falsifier

## Status

**Falsifier outcome: PASSES with vocabulary revision.** Step 1
of iteration 2 (`horn_branch_iteration_1.md` §"Plan for
iteration 2") was to determine the y-parity sector assignment
for the three observable generations and check whether the
horn-branch hypothesis is apparatus-consistent. Reading the
apparatus produces a sharp result that **passes** the falsifier
but **revises the vocabulary**: the distinguishing sector
the flare acts on is not cos-y / sin-y y-parity but
**locked / unlocked at q₂** (the antiperiodic x-direction).
The y-parity (cos/sin) classification is orthogonal to the
generation classification and was the wrong sector axis to
hypothesize on in iteration 1.

The revised hypothesis is **apparatus-consistent** (matches the
observed pattern: τ/e preserved, m_μ/m_e shifted) and **carries
the correct sign** (q₂-locked modes suppressed by regime-change,
q₂-unlocked C state enhanced relative to A and B).

Class: foundational rigor check (Class 3, iteration-step
falsifier on the horn-branch hypothesis).

---

## What the apparatus actually carries

### The two relevant classifications

The framework's Klein-bottle apparatus has at least two distinct
binary classifications that have been conflated in earlier
discussion:

**Classification 1 — y-parity (cos / sin), from the third-caveat
test.** R-eigenvalue of the y-mode under y → L_y − y:

- cos y-modes (R-even, p_y = 0) pair with antiperiodic-x
  wavenumbers (2k+1)π/L_x
- sin y-modes (R-odd, p_y = 1) pair with periodic-x wavenumbers
  2kπ/L_x

Both sectors are populated under the XOR rule p_x + p_y ≡ 1
(mod 2) (`klein_bottle.md` L107-152). The third-caveat test
(`klein_z2_decomposition_falsifier_2.md`) confirmed modal
sufficiency.

**Classification 2 — locked / unlocked at q₂ × q₃, from the
generation mechanism.** Whether a mode sits at a tongue (locked,
rational) or in a gap (unlocked, irrational) at each of the two
denominator levels q₂ = 2 and q₃ = 3 (`generation_mechanism.md`
L17-26):

| State | q₂ status | q₃ status | Weight | Observability |
|---|---|---|---|---|
| A | locked (duty) | locked (duty) | 1 | observable (e) |
| B | locked (duty) | unlocked (gap) | 26 | observable (τ) |
| C | unlocked (gap) | locked (duty) | 7 | observable (μ) |
| D | unlocked (gap) | unlocked (gap) | — | dark |

### The directional assignment (`klein_bottle_derivation.md` L553-558)

The framework forces a specific assignment of q₂ and q₃ to the
Klein-bottle's directional structure:

> "The smallest surviving denominators on the Klein bottle are
> q₂ = 2 (even, antiperiodic/temporal) and q₃ = 3 (smallest odd
> admitting non-trivial probability, periodic/spatial). The
> assignment {q₂ = 2 ↔ temporal, q₃ = 3 ↔ spatial} is not a
> labeling convention — it is forced by the divisibility
> condition 2|q on the antiperiodic direction."

So:
- **q₂ = 2 ↔ antiperiodic / x-direction** (carries the twist,
  the arrow of time in the substrate sense, the single coupled
  J = S × R)
- **q₃ = 3 ↔ periodic / y-direction** (carries the cyclic clock
  counter, the cos/sin y-parity decomposition)

### Why y-parity is orthogonal to generation

Classification 2 (locked/unlocked) is about whether a mode's
FREQUENCY sits at a rational tongue center or in an irrational
gap. Classification 1 (cos/sin) is about whether a mode's WAVE
FORM is R-even or R-odd under y-reflection.

These are independent. A q₃-locked mode at frequency p/3 has
a complex amplitude exp(2πi p y / 3 L_y) with both real (cos)
and imaginary (sin) components — both R-parity sectors
populated, on the same locked frequency. A q₃-unlocked mode at
an irrational frequency in the q₃ gap likewise has both R-parity
components.

The y-parity sector decomposition therefore does not pick out
a specific generation. Each of A, B, C carries modes in both
the cos-y and sin-y sub-spectra.

**Iteration 1 hypothesized the wrong axis.** The horn-branch
flare cannot distinguish generations by acting on cos vs sin
sectors, because each generation has both.

---

## The revised hypothesis — q₂ locked/unlocked

### Which axis distinguishes the generations?

Inspecting the generation table:

- **q₂-locked sector**: A, B (the lightest and heaviest)
- **q₂-unlocked sector**: C (middle), D (dark)
- **q₃-locked sector**: A, C
- **q₃-unlocked sector**: B, D

For the horn-branch flare to produce the observed pattern
(τ/e = B/A unchanged at 0.9% residual, m_μ/m_e = C/A shifted
by 37%), the flare must act *the same way* on B and A but
*differently* on C. This requires:

- B and A share a flare-sector → both q₂-locked ✓
- C and {A,B} differ in flare-sector → C is q₂-unlocked ✓

The **q₂ axis** (= x-antiperiodic locked/unlocked) matches.

The q₃ axis fails: under q₃ classification, A and C share a
sector (both q₃-locked) and B is on the other (q₃-unlocked).
This would predict the gap in the B/A ratio (τ/e, observed
at 0.9% residual) rather than the C/A ratio. Falsified by
existing observation.

### Apparatus consistency

The revised hypothesis (q₂ locked/unlocked) requires no
extension to the framework. It uses the existing generation
classification directly. The Klein-bottle directional assignment
(q₂ ↔ x-antiperiodic) is already established
(`klein_bottle_derivation.md` L553-558).

The y-parity modal sufficiency from the third-caveat test is
preserved as a separate finding about substrate apparatus —
it just isn't the axis the horn-branch flare acts on.

### Sign check

Observed: m_μ / m_e = 206.8 vs bare prediction 129.6 — observed
is **larger** by factor 1.595. The flare must therefore enhance
C (q₂-unlocked) relative to A and B (q₂-locked), or equivalently,
suppress q₂-locked modes relative to q₂-unlocked modes.

Mechanism reading: q₂-locked modes commit to a specific tongue
phase and are subject to phase-resolved dissipation during the
substrate→tree regime-change. q₂-unlocked (gap) modes are
quasiperiodic at q₂ scale and have no specific phase to dissipate
against — they propagate substrate→tree more cleanly. The
flare suppresses locked modes more than unlocked.

This is opposite to a naive Webster's-flare reading where
"locked = stable, unlocked = lossy." For substrate→tree
regime-change, *locked* means "phase-committed and therefore
exposed to phase-flip-mediated dissipation," while *unlocked*
means "phase-incoherent and therefore unaffected by
phase-flip dissipation." The flare's coupling is to the
single (S × R) coupled J, which acts on coherent phase-locked
modes.

This sign convention is mechanistically natural and matches the
observed direction.

---

## Quantitative target, revised

The target factor identified in iteration 1 was R_weight = 1.205
on W_C alone. Under the revised hypothesis (q₂-locked suppression
rather than q₂-unlocked enhancement), the same target is
re-expressed as:

> The flare's suppression factor on q₂-locked modes vs q₂-unlocked
> modes is f_locked / f_unlocked = 1 / 1.205 ≈ 0.83.

Equivalently, q₂-locked modes lose ~17% of their substrate
amplitude during regime-change relative to q₂-unlocked modes.
A and B are both q₂-locked, so both lose this factor; the
B/A ratio is preserved. C is q₂-unlocked and retains its
substrate amplitude, so C/A and C/B both shift by the same
ratio — specifically the 17% upshift on C relative to A
and B.

Effective weights at tree scale:

- W_A^{eff} = W_A × f_locked = 1 × 0.83 = 0.83
- W_B^{eff} = W_B × f_locked = 26 × 0.83 = 21.6
- W_C^{eff} = W_C × f_unlocked = 7 × 1.00 = 7.0

Effective ratios:
- (W_B^{eff} / W_A^{eff})^{5/2} = (21.6/0.83)^{5/2} = 26^{5/2} = 3447
  ✓ unchanged from bare (τ/e residual stays at 0.9%)
- (W_C^{eff} / W_A^{eff})^{5/2} = (7.0/0.83)^{5/2} = 8.43^{5/2} = 207
  ✓ matches observed m_μ/m_e = 206.8 within 0.1%

The arithmetic works exactly. The horn-branch hypothesis, under
the revised q₂-axis vocabulary, would close the Class B 37% gap
to <0.1% if the substrate forces f_locked / f_unlocked = 0.83.

**This is striking but does not constitute closure.** Step 1
only checks apparatus-consistency; it does not derive 0.83 from
substrate primitives. The result is **a target value**, not a
**derived value**.

---

## What this iteration step DOES establish

1. **Apparatus consistency for the horn-branch hypothesis under
   the q₂-axis vocabulary.** The framework already has the
   sector structure (locked/unlocked at q₂) that the flare needs
   to act on. No extension required.

2. **Iteration-1's y-parity framing was the wrong vocabulary
   for horn-branch.** The y-parity sectors are populated and
   modally sufficient but orthogonal to the generation
   classification. The right axis is q₂ locked/unlocked.

3. **The quantitative target for the flare's substrate-derived
   suppression ratio is 0.83 = f_locked / f_unlocked.** This is
   the number iteration 2 step 2 needs to derive (or fail to
   derive) from substrate primitives.

4. **The sign of the flare effect is natural under the (S × R)
   coupled J.** q₂-locked modes have specific phase to dissipate
   against; q₂-unlocked modes are quasiperiodic and propagate
   cleanly. The flare suppresses q₂-locked, not q₂-unlocked.

---

## What this iteration step does NOT establish

- **The 0.83 ratio is not derived.** It is required by the
  observed pattern; substrate derivation is iteration 2 step 2.
- **Whether 0.83 comes from sync-cost dynamics, geometry, or
  another mechanism.** Not yet attempted.
- **The PMNS θ_12 10% cross-check.** Iteration 2 step 4 work.
  However, the revised vocabulary now constrains it: θ_12
  mixing between A and C generations is subject to the
  C-vs-{A,B} sector split, which may produce a 30° → 33° shift
  via the same f_locked / f_unlocked ratio.
- **The exponent 5/2 dependence.** The sector exponent
  a_lepton = d − 1/2 = 5/2 is taken as bare-tree-derived
  (`generation_mechanism.md` §3); the flare's interaction with
  this exponent is assumed multiplicative on weights, not
  altering the exponent. This assumption merits checking in
  step 3.

---

## Falsifiers for step 1's verdict

The revised hypothesis (q₂-axis flare) is itself falsifiable:

1. **Apparatus-mapping falsifier.** If a closer reading of
   `klein_bottle_derivation.md` reveals that q₂ ↔ antiperiodic
   is contingent on a derivation step that is itself open or
   contested, the directional assignment may not be as forced
   as the L553-558 quote suggests. The corollary depends on
   "the divisibility condition 2|q on the antiperiodic
   direction" — checking the divisibility claim is one
   load-bearing read-back.

2. **Locked/unlocked-vs-flare interaction falsifier.** The
   mechanism reading ("locked phases dissipate, unlocked
   phases propagate") is plausible but unverified by simulation
   or independent derivation. If the substrate's actual
   regime-change dynamics suppress unlocked modes (gap-mode
   suppression rather than tongue-mode suppression), the sign
   flips and the hypothesis would predict m_μ < m_μ_bare,
   inverting observation.

3. **The 0.83 arithmetic-vs-derivation gap.** That the
   arithmetic closes to 0.1% on the q₂-axis is suggestive but
   could be coincidence. The exponent 5/2 introduces nonlinear
   sensitivity to the weight ratio; small variations in
   f_locked / f_unlocked produce different residuals. Without
   substrate derivation of the specific ratio 0.83, the apparent
   closure is numerology-at-risk (per the framework's
   numerology-discipline policy). Step 2 must derive 0.83 from
   substrate primitives or this finding remains pattern-match
   only.

4. **Charge-sector universality.** The same flare acting on
   quarks would predict a similar 17% locked-vs-unlocked
   suppression on quark weight ratios. m_b/m_d at 24% (largely
   QCD running) and m_t/m_u at 78% (also QCD running) have
   running-dominated residuals — but the *bare* tree predictions
   may also receive an analogous flare correction. Cross-check
   the quark-sector arithmetic for whether the same 0.83 ratio
   is consistent or contradicts. (Likely step 4 or 5 work.)

---

## Plan for iteration 2 step 2

The revised step 2 target:

**Derive f_locked / f_unlocked = 0.83 from substrate primitives.**

Plausible mechanisms to attempt:

- **Sync-cost minimization on the regime-change transition.**
  q₂-locked modes have synced phases and the sync-cost
  functional includes a phase-coherence term that the
  regime-change action might break. The exact factor 0.83
  could come from a balance between coherence cost and
  decoherence rate at the substrate→tree boundary.

- **Klein-bottle ratio Q = q₂/q₃ = 2/3.** The framework
  already has 2/3 as the population ratio between (q_x, q_y) =
  (2, 3) and (3, 2) families. Some product or ratio involving
  Q might give 0.83 directly. Candidates:
  - (1 + Q)/2 = (1 + 2/3)/2 = 5/6 ≈ 0.833 ✓ — striking pattern
  - Q × (1 + Q^{-1}) = 2/3 × 5/2 = 5/3 (rejected)
  - 1 − Q^2/4 = 1 − 1/9 = 8/9 ≈ 0.889 (rejected)
  - 1 − 1/2(1 − Q) = 1 − 1/6 = 5/6 ≈ 0.833 ✓ (same as first)

  The candidate **5/6 = (1 + Q)/2** matches 0.833 vs the
  required 0.83 within 0.4%. This is a single-parameter
  formula in Q with no fitting freedom — if substrate
  derivable, it would close the Class B gap.

- **Saddle-node geometry of the regime-change boundary.** The
  Born exponent 2 came from saddle-node universality
  (`born_rule.md`). The same universality may constrain the
  flare's suppression ratio.

Iteration 2 step 2 should investigate whether **f_locked /
f_unlocked = (1 + Q)/2 = 5/6** is substrate-forced or pattern-
matched, and either way derive the corrected mass formula:

    m_μ/m_e^{predicted} = (W_C / (W_A × 5/6))^{5/2}
                        = (7 × 6/5)^{5/2}
                        = 8.4^{5/2}
                        = 204.6

vs observed 206.8 — residual ~1% under the 5/6 candidate.

This residual is comparable to the Koide-imported 1% closure
from `fermion_mass_running.md` §4c, but here the closure comes
from a substrate-internal candidate (Q = 2/3, Klein-bottle
ratio) rather than an empirical Koide import. If 5/6 is
substrate-derivable, this is **iteration 2's closure target**.

---

## Cross-links

- `horn_branch_iteration_1.md` — iteration 1 framing (y-parity
  vocabulary, now corrected).
- `klein_z2_decomposition_falsifier_2.md` — modal y-parity
  sufficiency (preserved as separate finding; not the horn-branch
  axis).
- `klein_bottle_derivation.md` L553-558 — directional
  assignment q₂ ↔ antiperiodic, q₃ ↔ periodic.
- `generation_mechanism.md` L17-26 — generation classification
  (locked/unlocked at q₂ × q₃).
- `klein_bottle.md` D19 / L674-705 — Klein-bottle ratio
  Q = q₂/q₃ = 2/3.
- `fermion_mass_running.md` §2-4 — existing depth and SL(2,Z)
  trace attempts; this step's revised closure target competes
  with §4c (Koide closure) at the 1% level but without
  empirical import.
- `koide_form_substrate_iteration_14.md` — closing note that
  honestly demoted the m_μ gap to 37% bare-tree; the (1+Q)/2 = 5/6
  candidate, if substrate-derivable, would close this gap.
- `born_rule.md` — saddle-node universality; potential
  source for substrate derivation of f_locked / f_unlocked.
- `basepoint_principle.md` — operationally-open status pending
  step 2 substrate derivation.

---

## One-line summary

Iteration 2 step 1 passes the sector-assignment falsifier but
with a vocabulary revision: the horn-branch flare's
distinguishing axis is not cos-y / sin-y y-parity (iteration 1's
framing) but **q₂ locked/unlocked = x-antiperiodic tongue/gap**,
under which A and B share a sector (q₂-locked, both suppressed
identically, τ/e ratio preserved) while C sits alone in the
q₂-unlocked sector (enhanced relative to A, B); the
quantitative target translates to a substrate-derived
suppression ratio f_locked / f_unlocked ≈ 0.83 with the
candidate (1 + Q)/2 = 5/6 (where Q = q₂/q₃ = 2/3 is the
Klein-bottle ratio) matching to 0.4%, which iteration 2 step 2
must verify is substrate-forced rather than pattern-matched
before this closure is treated as anything more than
suggestive.
