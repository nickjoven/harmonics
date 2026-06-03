# Horn-branch iteration 1 — regime-change flare in y-parity vocabulary

> **SUPERSEDED IN VOCABULARY by `horn_branch_iteration_2_step_1.md`
> (q₂-axis revision).** This doc frames the horn-branch flare in
> *y-parity (cos/sin)* vocabulary. Iteration 2 step 1 found that
> y-parity is orthogonal to the generation classification and
> not the axis the flare actually acts on; the framework-native
> axis is **q₂ locked/unlocked**. The flare hypothesis and
> regime-change framing in this doc are preserved; the *sector
> vocabulary* (y-parity) is the wrong axis. Read step 1 before
> using this doc's "y-parity flare" framing.

> **CLOSURE CLAIMS WALKED BACK by `horn_branch_iteration_3_step_1.md`
> (PRODUCTIVE NULL).** This doc proposes a "target factor 1.595
> ≈ √(5/2)" reading that motivated subsequent iterations. The
> horn-branch arc through iteration 3 step 1 has surfaced a
> clustered candidate around 0.83 for `f_locked / f_unlocked`
> without substrate-forcing mechanism. The arc's substrate
> closure on the m_μ 37% gap is **operationally open**, not
> closed; the pattern-match candidates (5/6 from substrate-internal
> readings; 0.8281 from observation-inversion) span a 1% band
> consistent with coincidence at the framework's general
> precision tier.

## Status

**First-pass exploration.** This is iteration 1 of the
horn-branch arc. Apparatus-level unblock is in place
(`klein_z2_decomposition_falsifier_2.md`: modal y-parity
sufficiency), and the chirality-extension fallback is closed
(`klein_bottle_restructure_price.md`: structurally declined by
empirical falsifier). This doc frames the regime-change-as-horn
hypothesis in substrate y-parity vocabulary (not chirality,
**but see vocabulary-revision notice above**), connects to the
existing depth-correction and SL(2,Z)-trace work in
`fermion_mass_running.md`, sets up a falsifiable first-pass
hypothesis for the m_μ 37% bare-tree residual, and documents
what would constitute closure vs further iteration.

No closure is attempted in this iteration. The aim is to
articulate the hypothesis carefully enough that subsequent
iterations have a defined target.

Class: first-iteration substrate derivation attempt for an open
Class B residual (Class 3, iteration-arc opener).

---

## Background — what is already known

### Class B residual: m_μ / m_e bare-tree 37% gap

`fermion_mass_running.md` §2-4:

- Tree-level prediction: m_μ/m_e = 7^(5/2) = 49√7 = 129.6
- Observed: 206.8
- Gap: −37% (bare prediction too small)
- τ/e and τ/μ ratios behave differently — the gap is specifically
  in the **middle generation (C state, weight 7)**, not in the
  extreme ratios.

`fermion_mass_running.md` §3:

- Standard gauge anomalous dimension is flavor-universal; cannot
  close a flavor-dependent gap.
- Yukawa self-coupling for muon: y_μ² ≈ 4×10⁻⁷, gives O(10⁻⁵)
  correction over Planck-to-muon running. Negligible.
- The 37% gap is therefore **tree-level**, not RG-running.

`fermion_mass_running.md` §4 documented two attempts:

- **Depth-correction**: W_C → W_C × φ² = 18.33 → mass ratio
  18.33^(5/2) = 1440. Overshoots; wrong magnitude.
- **SL(2,Z) trace mixing (30° angle)**: W_C^{mixed} = W_C(1 +
  tan²30°) = 28/3 = 9.33 → mass ratio (28/3)^(5/2) = 266.
  Right direction, closes ~8% of the 37% gap. Insufficient.

`koide_form_substrate_iteration_14.md` Closing note:

- The earlier "Koide closure" giving m_μ/m_e = 205 with 1%
  residual is now demoted to **empirical Koide import**, not
  framework derivation. The framework's actual substrate prediction
  for m_μ/m_e is the bare-tree value 129.6 — the 37% gap is open.
- The observation that m_μ_observed / m_μ_bare ≈ 1.595 ≈ √(5/2)
  is flagged as **numerology / selection-bias risk** without a
  mechanism. Pattern-match only.

### Class C residual: PMNS θ_12 10% gap

- Framework bare prediction: 30° (from SL(2,Z) trace structure)
- Observed: 33.4°
- Gap: ~10% (close, structurally similar to Class B in the sense
  that the bare framework gets the right scale but misses by a
  generation-dependent factor)

### What the audit said

`axial_trajectory_conservation_audit.md` (now superseded by the
falsifier chain) said Task 105 is blocked pending a chirality
extension. The third-caveat test refined this: apparatus is
modally sufficient in y-parity vocabulary, so the horn-branch
can proceed without chirality extension (which is structurally
declined anyway).

---

## The horn-branch hypothesis — Webster's flare in substrate→tree

### Acoustic analog

Webster's horn equation describes 1-D wave propagation in a
variable-cross-section tube:

    ∂²p/∂t² = (c²/A(x)) ∂/∂x(A(x) ∂p/∂x)

For an exponential flare A(x) = A_0 e^{βx}, the equation reduces
to a Klein-Gordon-like form:

    ∂²p/∂t² − c² ∂²p/∂x² + (cβ/2)² p = 0

This produces a **cutoff frequency** ω_c = cβ/2 below which
waves are evanescent (cannot propagate). Above ω_c they
propagate with a phase velocity that increases as ω → ω_c⁺.

### The substrate→tree analog

Framework regime-change framing:

- **Substrate end**: high-frequency / mode-rich / Stern-Brocot
  tree depth → ∞
- **Tree end**: low-frequency / coarse / discrete observable
  modes at the framework's tree scale (K = 1)
- **The "flare"**: the geometric profile A(x) along the regime
  direction x from substrate to tree

The hypothesis: regime-change dissipation acts as a Webster-style
flare with **y-parity-distinguishing cross-section A_±(x)**.
The two y-parity sub-spectra (cos-y, sin-y) propagate through
different effective cross-sections, get different cutoffs, and
arrive at the tree scale with different effective weights.

### What y-parity gets us that chirality cannot

The audit's original blocker was that the framework's existing
Klein-Z_2 cannot distinguish chirality (audit verdict APPARATUS
INSUFFICIENT). The falsifier chain showed that:

- The framework has populated y-parity sectors (cos-y, sin-y)
  paired complementarily with x-mode types by XOR
  (`klein_bottle.md` L107-152).
- These two sectors live on **different x-mode wavenumber
  ladders** — (2k+1)π/L_x for cos-y, 2kπ/L_x for sin-y.
- Sector-dependent regime-change dissipation can act differently
  on these two ladders without requiring an independent
  R-generator.

The horn-flare hypothesis is therefore well-defined in y-parity
vocabulary: A_+(x) and A_−(x) are two cross-section profiles,
one per y-parity sector, that the regime-change dissipation
applies to substrate modes as they propagate to the tree scale.

---

## First-pass hypothesis — flare shape from Klein-bottle apparatus

### What the substrate already determines

Without choosing a specific A(x), the framework apparatus
already provides several constraints any horn-flare must satisfy:

1. **Asymptotic mode count at tree scale.** The tree-level
   weights (W_A, W_C, W_B) = (1, 7, 26) for generations
   (A, C, B) are *already* substrate-derived from XOR mode
   counting on the Klein bottle (`generation_mechanism.md` D34).
   The flare cannot move these — it can only redistribute
   *between* generations or *between* y-parity sectors at fixed
   total.

2. **τ/e ratio is already correct at 0.9%.** The flare's
   integrated effect on the extreme ratio (B/A = 26/1) is
   either zero or perfectly self-cancels. This means the flare
   acts *generation-dependently*, sparing the extremes.

3. **The gap is in the middle (C, weight 7).** The flare's
   y-parity-distinguishing dissipation must produce a
   net upweighting of W_C in the lepton sector. Quantitatively,
   from m_μ^{observed} / m_μ^{bare} = 1.595 ≈ √(5/2), the
   weight correction is W_C → W_C × 1.595^(2/5) ≈ 8.43, a
   factor of ~1.205 upweight on W_C.

4. **Charge-sector exponent a_lepton = 5/2.** The flare's
   regime-change dissipation must commute with the charge
   exponent. Whatever it does to W_C, it does at the *weight*
   level, leaving the (5/2) raising operation intact.

### The middle-generation specificity

Why does the gap appear in C (middle, weight 7) but not in B/A
(extremes, weights 26/1)? Two non-equivalent readings:

(i) **C is on the antiperiodic-x ladder**, while B and A are on
    the periodic-x ladder (or vice versa). The flare's y-parity
    cross-section dissipates these ladders asymmetrically, and
    the asymmetric dissipation happens to land on C.

(ii) **C is the deepest in the Stern-Brocot tree** (gen=2, vs
     gen=1 for τ and gen=0 for e in the framework's chain
     signature), and the depth-dependent flare cross-section
     A(depth) attenuates middle generations more than extremes.

These are not exclusive. Reading (i) is the new horn-branch
contribution (y-parity flare); reading (ii) is the existing
depth-correction attempt in `fermion_mass_running.md` §4b that
overshot by giving a φ² factor.

The horn-branch's first-pass move: **combine (i) and (ii) such
that y-parity-distinguishing depth-dependent flare gives the
right magnitude correction on W_C without overshooting**.

### Quantitative target

The framework's target factor is W_C → W_C × R where
R ≈ 1.205 (~20.5% upweight). This is much smaller than φ² =
2.618 (the depth-1-overshoot factor) and significantly larger
than (1 + tan²30°) = 4/3 = 1.333 applied as W_C × 4/3 then
to the 5/2 power.

Actually, let me recompute the SL(2,Z) trace correction's
implication for R:

    W_C^{mixed} = W_C × 4/3
    (W_C^{mixed} / W_e^{mixed})^{5/2} = (4/3)^{5/2} × (7/1)^{5/2} = 2.05 × 129.6 = 266

so SL(2,Z) trace gives R = 4/3 = 1.333 on weight, and 2.05 on
mass ratio. Observed needs R_mass = 1.595, so:

    R_weight^{5/2} = 1.595 → R_weight = 1.595^(2/5) = 1.205

The first-pass hypothesis target is therefore:

> **Y-parity flare correction to W_C = 1.205 (= 1.595^(2/5)).**

Equivalently, the flare's relative dissipation between the two
y-parity sectors on the C state's x-mode ladder produces a 20.5%
upweight on W_C.

This is a quantitatively specified hypothesis. Iteration 2's job
is to derive R_weight from substrate primitives.

---

## Connecting to the existing substrate apparatus

### What sector is W_C on?

The C state's chain signature in the Stern-Brocot tree is
**gap(2) × duty(3)**. From `klein_bottle.md`'s XOR rule:

- Even / odd parity of the denominator chain determines mode
  type.
- For C = gap(2) × duty(3), q_x corresponds to gap(2) and q_y
  to duty(3). The numerator path through the Stern-Brocot tree
  for C lands at p/q = 2/3, which has p+q = 5 (odd) at numerator
  parity.

Mapping this to (p_x, p_y) parity: needs to be checked against
the XOR rule. If C lands at (p_x = 1, p_y = 0) = (odd, even),
then C is on the **antiperiodic-x × cos-y (R-even) sector**.

If C lands at (0, 1), then it is on the periodic-x × sin-y
(R-odd) sector.

Iteration 2's first concrete derivation step: **determine which
of the two y-parity sectors W_C lives on, and verify B/A live on
the opposite sector (so the gap-only-in-C pattern follows
naturally from y-parity-distinguishing flare).**

### What's the flare cross-section?

If A_+(x) and A_−(x) differ in cross-section along the regime
direction, the relative attenuation of modes is governed by:

    ψ_±(tree) / ψ_±(substrate) = exp(− ∫ μ_±(x) dx)

where μ_±(x) is the y-parity-dependent attenuation rate
determined by A_±(x). The substrate→tree integration is over
the regime direction.

For Webster's exponential flare A_±(x) = A_0 exp(β_± x), the
cutoff frequency is ω_c,± = c β_± / 2. Substrate modes with
frequency above ω_c propagate; modes below are evanescent.

The framework analog: substrate modes at depth d in the
Stern-Brocot tree have "frequency" inversely proportional to
their tree-scale mode density. The cutoff in y-parity sector ±
selects which depth-d modes survive to tree level. If β_+ ≠ β_−,
the two sectors have different effective tree-level mode counts.

Iteration 2's second concrete derivation step: **derive β_+ and
β_− from the Klein-bottle XOR structure**. The substrate doesn't
choose β arbitrarily — it should be forced by sync-cost
minimization or topology.

---

## What this iteration does NOT establish

- **No derivation of R_weight = 1.205.** This is the target,
  not the result.
- **No determination of which y-parity sector hosts W_C.** Stated
  as iteration-2 step 1.
- **No flare profile β_± derived from substrate.** Stated as
  iteration-2 step 2.
- **No PMNS θ_12 10% gap analysis.** Class C residual is on
  the horn-branch agenda but not addressed in iteration 1; the
  m_μ / m_e gap is the cleaner first target because it's
  larger and the bare prediction is cleanly named.
- **No verification that y-parity is observable.** The
  identification of substrate y-parity with anything observable
  (chirality? generation? something else?) is part of the
  Task 110 vocabulary-bridge work, which runs adjacent.

---

## Falsifiers for the horn-branch hypothesis itself

The horn-branch hypothesis (y-parity-distinguishing
regime-change flare closes the Class B 37% gap) is falsifiable
in several ways:

1. **Sector-assignment falsifier.** If both W_C and W_B (or both
   W_C and W_A) land on the *same* y-parity sector under the
   Klein-bottle XOR rule, then a sector-dependent flare cannot
   produce the observed pattern (gap-only-in-C). The hypothesis
   would be inconsistent with the existing apparatus and need
   to be abandoned at the apparatus level.

2. **Magnitude falsifier.** If the substrate-derived
   y-parity-sector flare cross-section ratio β_+/β_− leads to
   a weight correction R_weight ≠ 1.205 by more than ~5% (the
   slack the framework has on saddle-node / substrate-tree
   transition geometry), the hypothesis fails to close the
   gap and would join the Koide arc as a productive null.

3. **Cross-check falsifier.** Whatever β_+/β_− the substrate
   forces, it must also produce the correct PMNS θ_12 closure
   (Class C residual). If the same flare profile that closes
   the muon gap *worsens* the θ_12 prediction (the same
   asymmetry as the failed self-field NLO attempt that worsened
   θ_13), the hypothesis fails cross-check.

4. **Sign falsifier.** Webster's flare can only dissipate
   (reduce amplitude) downstream. If the substrate-derived flare
   needs to *amplify* the C state's weight at tree level rather
   than dissipate others, the Webster-acoustic analog is
   inverted and the hypothesis would need to invert with it
   (substrate is "downstream," tree is "upstream").

---

## Plan for iteration 2

Concrete derivation steps to attempt next:

1. **Determine W_C's y-parity sector** under the Klein-bottle
   XOR rule. Use the chain signature gap(2) × duty(3) to compute
   (p_x, p_y) and check the XOR parity. Same for W_A (duty(2) ×
   duty(3)) and W_B (duty(2) × gap(3)). Verify that W_C is on
   one sector while W_A and W_B are on the other (the condition
   for the y-parity flare hypothesis to be apparatus-consistent).

2. **Derive β_+/β_− from substrate primitives.** Sync-cost
   minimization on the regime-change transition, with the
   constraint that the two y-parity ladders carry their
   respective populated modes. The cube identity q_2³ = q_2 +
   2q_3 is a natural source of asymmetric ratios; the Klein
   ratio Q = 2/3 is another.

3. **Compute R_weight = (β_+ / β_−)^... .** Compare with target
   1.205. The exponent in the formula comes from the saddle-node
   / regime-transition geometry, which `born_rule.md`'s
   saddle-node universality may constrain.

4. **Cross-check on PMNS θ_12.** Use the same β profile to
   compute the implied correction to the mixing angle; check
   against observed 33.4°.

If step 1 fails (W_C and W_B on same sector), iteration 2 ends
at "apparatus does not support the hypothesis" and the horn-branch
arc closes as a productive null. If step 1 passes but step 2/3
overshoot or undershoot by >5%, the arc continues with the
mismatch as a residual to address. If both close cleanly, the
horn-branch produces its first substantive substrate-level
derivation result.

---

## Cross-links

- `klein_z2_decomposition_falsifier_2.md` — modal y-parity
  sufficiency; apparatus unblock for this branch.
- `klein_bottle_restructure_price.md` — apparatus-extension
  fallback closed; vocabulary-bridge (Task 110) is the only
  substrate-chirality route and runs adjacent to horn-branch.
- `axial_trajectory_conservation_audit.md` — original audit
  that named horn-branch as Task 105.
- `fermion_mass_running.md` §2-4 — existing depth and SL(2,Z)
  trace attempts on the Class B gap; horn-branch is the third
  attempt and operates at a different layer (regime-change
  dissipation, not in-tree correction).
- `koide_form_substrate_iteration_14.md` — closing note that
  honestly demoted the m_μ gap to 37% bare-tree; this iteration
  is built against that honest baseline, not the
  Koide-imported 1% number.
- `klein_bottle.md` L107-152 — mode decomposition and XOR rule
  (load-bearing for the sector-assignment step).
- `generation_mechanism.md` D34 — phase-state weight derivation
  (sets W_A, W_C, W_B and chain signatures).
- `born_rule.md`, `born_rule_parameter_free.md` — saddle-node
  universality; may constrain the regime-transition geometry's
  natural exponent.
- `basepoint_principle.md` — operationally-open status for
  the horn-branch hypothesis pending iteration 2 closure.

---

## One-line summary

Horn-branch iteration 1 frames the regime-change-as-Webster-flare
hypothesis in substrate y-parity vocabulary (apparatus-consistent
per the falsifier chain; chirality vocabulary is empirically
declined per the price ledger), connects to the existing
depth-correction and SL(2,Z) trace attempts in
`fermion_mass_running.md` (which closed ~8% of the 37% gap),
identifies the quantitative target as a y-parity flare weight
correction R_weight = 1.205 on W_C, and defines four falsifiable
iteration-2 steps (sector assignment, β derivation, R_weight
computation, PMNS θ_12 cross-check) whose outcomes determine
whether the horn-branch arc closes the Class B gap, produces a
productive null like the Koide arc, or surfaces a new substrate
mechanism along the way.
