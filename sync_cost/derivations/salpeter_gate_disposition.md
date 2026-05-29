# Cascade↔Salpeter slope: dual-gate disposition

## Status

**Disposition consolidated.** The cascade↔Salpeter slope is **Class-2
with a partial structural derivation and an open dual gate** —
structural and statistical — both currently unmet. The doc names
which piece is forced, which is null, and what each gate would need
to clear.

This is not a closure. It is an honest articulation, replacing the
implicit "Salpeter slope matches at 0.33σ" framing with the explicit
dual-gate status the framework's own `imf_bowed_cascade.md` "Status"
section already records. The capstone synthesis
(`gr_qm_unification_synthesis.md`) named this as one of two
explicitly-open items remaining after PR #179; this doc supplies the
disposition.

No new primitive.

---

## The statement

**Claim.** The cascade ordering, depth selection, and the
`−1/q_3` slope correction are **structurally forced**. The
`−q_2 = −2` baseline of the slope formula is **structurally null**.
Therefore the `α_Salpeter = −7/3` match to observed Salpeter
(`α = −2.35 ± 0.05`) at 0.33σ is **one empirically-suggestive
correspondence at one cascade rung**, with two gates remaining
unmet:

- **Structural gate (open):** find a dynamically-grounded baseline
  that reproduces the `−q_2` contribution. The Farey-weight reading
  (tongue width `= 1/q²`) is null — physical critical width has
  multifractal exponent `β ≈ 2.3 > 2`, giving dynamical slope
  `≈ −1.86`, not `−2`.
- **Statistical gate (open):** the pigeonhole test
  (`cascade_slope_check.py`) returns `p ≈ 0.10` against `α = 0.05`,
  and the held-out test (`held_out_slope_test.py`) confirms low
  power with `N = 1` un-replicated match across the cascade's
  reachable slope band.

The disposition is **not** that the framework has closed the
Salpeter slope. It is that the framework has *partially closed* the
structural piece (the cascade *family* of slopes is forced; the
depth is forced; the correction is forced), and the remaining work
is named precisely.

---

## What is structurally forced

The cascade is parameterized by the master identity
`K_n^d = b^{−n}` with `(d, n, b)` drawn from `{q_2, q_3, |F_n|}`
(`master_cascade_identity.md`). The bowed cascade specifically has
`(d, n, b) = (q_3, 1, q_2) = (3, 1, 2)`, giving
`K_IMF = 2^{−1/3} ≈ 0.794`. The slope formula `α = −q_2 − n/d`
then gives `α_bowed = −2 − 1/3 = −7/3`.

Three pieces of this derivation are structurally forced:

1. **The cascade `(d, n, b)` family.** Drawn from framework
   primitives `{q_2, q_3, |F_n|}` by the master cascade identity.
   Forced.
2. **The depth `d = q_3 = 3` (Klein-orbit count of `F_3`).** Step-2
   lemma proved by `imf_step2_klein_orbit.py`: under the canonical
   Klein involution `r → 1−r`, the Farey set `F_{q_3} = F_3` has
   orbit count `3 = q_3`. **The identity
   `orbit_count(F_m) = m` holds only for `m ∈ {2, 3, 4}`**, selecting
   small-denominator cascades and *excluding* deeper Z_6 (`d = 6`)
   and K\* (`d = 14`) sectors. This is genuine forcing, not
   pigeonhole.
3. **The `−1/q_3` correction.** Follows from the Klein-orbit
   count + one non-redundant antiperiodic flip (the `{1/3, 2/3}`
   pair; boundary `{0/1, 1/1}` is redundant with periodicity;
   fixed point `{1/2}` contributes zero). So `n = 1` in the
   formula, contributing `−1/3 = −1/q_3` to the slope.

These three pieces give a *family* of slopes across cascade
stations, with the bowed cascade's correction pinned to `−1/q_3`.
This is real structural content.

---

## What is structurally null

The **`−q_2 = −2` baseline** of the slope formula requires the
tongue width to be the Farey weight `1/q²`. Per
`farey_tongue_width_null.py` and `tongue_width_universality.py`:

- A *complete* K=1 staircase forces the width exponent `β > 2`
  (else the tongues over-fill `[0, 1]`).
- The physical width law is **multifractal**: the `1/q` exponent
  drifts `2.18 → 2.88` with no limit; the often-quoted `β ≈ 2.3` is
  a low-q artifact.
- The universal golden-mean exponent is
  `β = ln(δ_FKS)/ln(φ) ≈ 2.164` (the
  Feigenbaum–Kadanoff–Shenker renormalization constant `δ_FKS`,
  *not* a Hausdorff dimension).
- Substituting that dynamical baseline gives slope
  `≈ −1.924 − 1/q_3 ≈ −2.26 vs. Salpeter −2.35`, *worsening* the fit.

The `1/q²` that gives `−q_2 = −2` is the **combinatorial
Stern–Brocot tree weight**, not the physical tongue width.
`farey_mass_baseline.py` computes the slope under that
combinatorial weight as a reference, not a dynamical derivation.

So the `−q_2` baseline stands *only* as a combinatorial reference.
A *grounded dynamical* `−q_2` would require either (a) showing the
substrate's cost functional selects the combinatorial weight over
the dynamical multifractal width, or (b) finding a different
structural derivation that arrives at `−q_2` from physically-grounded
primitives. Neither exists currently.

This is the *structural gate* — open.

---

## The statistical gate

`cascade_slope_check.py` runs the pigeonhole test: how often does a
random slope in the permitted band `[−2.5, −2.0]` land within `0.5σ`
of Salpeter's `−2.35`? Answer: `p ≈ 0.10`. Conventional
`α = 0.05` for promotion is not cleared.

`held_out_slope_test.py` runs a sharper held-out test (Region-C
Phase C #3): of 10 independent control slopes, none land within
Salpeter's `0.017` gap of the informative `−7/3` rung. The one
control near a rung sits at `−2.0` — pigeonhole-rich, matched by
the initial-cluster MF rather than a discriminating signal.

Net statistical reading: **N = 1 un-replicated match (Salpeter)**.
Suggestive of real targeting, not statistically decisive. The
ladder's range `[−2.5, −2.0]` is too narrow and too sparsely
populated by independent controls for statistics alone to decide.

This is the *statistical gate* — open.

---

## Why both gates matter

The cascade↔Salpeter match could plausibly clear via either gate
clearing independently:

- **Structural gate clears alone:** if a grounded dynamical
  derivation of `−q_2` lands (e.g., by deriving the substrate's
  cost-functional selection of the combinatorial weight over the
  dynamical multifractal width), the slope formula becomes
  structurally complete; the 0.33σ Salpeter match would then be a
  forced consequence of substrate dynamics + the master cascade
  identity. The statistical gate would be irrelevant because the
  prediction was *forced*, not chosen post-hoc.
- **Statistical gate clears alone:** if independent additional
  cascade-rung observations (more mass-function rungs, e.g., subhalo
  MF matching `−13/6` from Z_6 or `−5/2` from clarinet) accumulate
  with sufficient statistical power, the slope-family structure
  alone could become decisive (even if the `−q_2` baseline remains
  structurally ungrounded). The cascade family would be empirically
  confirmed across multiple rungs; the un-grounded baseline would
  become a separate open question.

Both clearing is the strong case: structurally forced *and*
empirically confirmed across the family.

Both *not* clearing means the cascade↔Salpeter match stays where
it is now: a real structural framework (the cascade family) with
one near-rung match (`−7/3 ≈ −2.35` at 0.33σ) and a remaining
baseline derivation gap.

---

## What this says (and what it does not)

It **says**:

- The cascade *ordering*, *depth selection*, and *`−1/q_3`
  correction* are structurally forced — real apparatus, not
  numerology.
- The `−q_2` baseline is structurally *null* — the Farey-weight
  reading was assumed, the physical width is multifractal, and the
  dynamical reading worsens the fit.
- The Salpeter match (0.33σ) is therefore *one* empirical
  correspondence at one rung — suggestive, not decisive — and the
  framework's structural claim is properly the *family of slopes
  across cascade stations*, not the specific `−7/3` to Salpeter
  match.
- Two gates remain unmet, and naming them precisely directs future
  work.

It does **not** say:

- That the framework has closed the cascade↔Salpeter question. It
  has not. The structural derivation is partial; the statistical
  test does not clear.
- That `−7/3` is wrong. The Salpeter match at 0.33σ is real; what
  is missing is the *forcing* argument for the `−q_2` piece.
- That the cascade framework is a fit. Three of four pieces of the
  derivation are structurally forced (cascade family, depth,
  correction). One piece (`−q_2` baseline) is currently null. The
  framework correctly distinguishes these.

This is the same shape as the framework's other partial closures: the
forced pieces stay forced; the null pieces are marked null; the
empirical evidence is named for what it is (one match, not multiple
independent confirmations).

---

## Parallel to the K(t) closure

The K(t) cadence closure (`k_of_t_residual_disposition.md`, PR #179)
moved its open piece from "Class-2 statistical" to "structurally
closed" by finding a structural discriminator (Q-mod-2 + #6 +
bicone bridge) that operated above the precision floor. The
Salpeter case is structurally *different*: the analogous discriminator
work has been done (Klein-orbit count for `n/d`), but the *baseline*
piece is not analogous — it is a width-law derivation, structurally
null, with no current integer-graded resolution.

The Salpeter case may have its own win-kill path — perhaps a different
kind of structural argument we haven't tried — but it is *not* the
same shape as the K(t) closure and we should not expect the same
kind of breakthrough. Honest reading: the gates are different from
each other, and the cascade↔Salpeter problem is at a different
maturity than K(t) was at the moment of its closure.

---

## What would close each gate

**Structural gate (currently null):**

A dynamical derivation of the `−q_2` baseline from primitives. Three
candidate routes (none currently closed):

1. **Cost-functional selection.** Show the substrate's cost
   functional (`mass_entrained_measure.md`'s mass↔width step) selects
   the combinatorial Stern-Brocot weight `1/q²` over the dynamical
   multifractal width `~1/q^β` with `β ≈ 2.16`. This would require
   exhibiting a substrate constraint that vetoes the multifractal
   reading.
2. **Alternative -q_2 source.** A different structural mechanism
   that produces `−q_2 = −2` from primitives (not via tongue width).
   Candidate: the Klein-bottle Z₂ might constrain the slope contribution
   directly via a kink-counting argument, parallel to the
   `q_mod2_mediant_projection.md` work.
3. **Replace `−q_2` with the dynamical baseline** (`≈ −1.924`),
   accept the corresponding slope (`≈ −2.26`) as the framework's
   structural prediction, and acknowledge the 3.9% gap to Salpeter
   `−2.35` as the empirical residual. This is the *honest decline*
   route — preserves structural cleanness at the cost of giving
   up the exact `−7/3 ↔ −2.35` match.

**Statistical gate (currently `p ≈ 0.10`):**

Independent additional cascade-rung observations. Candidates:

1. **Subhalo mass function at `α ≈ −13/6` (Z_6 cascade,
   conjectural).** Would test the cascade family beyond the bowed
   rung. Subhalo MF measurements from satellite censuses of nearby
   galaxies are an active observational target.
2. **Untested intermediate-rung MFs.** Globular cluster MF (`α = −2`
   = K=1 rung) is at the pigeonhole-rich limit and provides no
   discrimination; subhalo and other intermediate MFs do.
3. **High-`z` IMF observations.** JWST is beginning to constrain
   the IMF at high redshift; framework structure does not predict
   z-evolution at the slope level (the cascade is K-locked), so
   constant-with-z observations would be consistent; z-varying slopes
   would require explanation.

Either gate clearing materially advances the disposition. Neither
clearing leaves the cascade↔Salpeter where it currently is:
structurally partial, empirically suggestive at one rung.

---

## Falsifiers

- **`−q_2` baseline derived from primitives at a dynamically-grounded
  value different from `−2`** would falsify the bowed `α = −7/3`
  prediction and replace it with a different cascade-rung
  prediction. The framework would have to adopt the new baseline as
  the structural reading.
- **Additional cascade-rung observations falsifying the slope
  family** (e.g., subhalo MF measured at a slope incompatible with
  the Z_6 cascade's `−13/6` *and* not at any other framework
  cascade rung) would void the family-structure claim, not just the
  Salpeter match.
- **A pigeonhole audit that explicitly *clears* `α = 0.05`** (e.g.,
  via more independent rung observations) would *resolve* the
  statistical gate without requiring the structural gate to close.
- **A statistically decisive match across multiple rungs** would
  move the family to Class-5 (structurally forced + empirically
  confirmed across the family) regardless of the baseline status.

---

## Why this matters

The capstone synthesis (`gr_qm_unification_synthesis.md`, PR #181)
named the cascade↔Salpeter as one of two explicitly-open items
remaining. This doc supplies the disposition: the open piece is
*structural+statistical dual gate*, not a single statistical
shortfall. Naming this precisely directs future work to the right
target (find the structural discriminator for `−q_2`, or accept the
dynamical baseline and adopt the corresponding slope) rather than
the wrong one (just collect more Salpeter data — that improves the
statistical gate but not the structural one).

This is the framework's discipline applied: don't conflate two
different kinds of open work, name each for what it is.

Class: foundational consolidation (Class 3, articulation), with an
honest negative result on the baseline + a precise open-work
specification.

---

## Cross-links

- `imf_bowed_cascade.md` — the primary slope claim and its
  "Status" section (which already names the dual-gate situation;
  this doc consolidates and elaborates).
- `master_cascade_identity.md` — the `(d, n, b)` family and the
  cascade structure.
- `cascade_slope_check.py` — the pigeonhole test (`p ≈ 0.10`).
- `held_out_slope_test.py` — the held-out test (Region-C Phase C #3).
- `imf_step2_klein_orbit.py` — the Klein-orbit-count argument for
  depth `= q_3` and `n = 1`.
- `farey_tongue_width_null.py`, `tongue_width_universality.py` —
  the multifractal-width null that makes `−q_2` structurally
  ungrounded.
- `farey_mass_baseline.py` — the combinatorial Stern-Brocot baseline
  used as reference.
- `mass_entrained_measure.md` — mass ∝ entrained measure; the
  candidate cost-functional route for clearing the structural gate.
- `mass_function_family.md` — the broader cascade-MF family the
  Salpeter rung sits within.
- `negative_results_ledger.md` — the framework's consolidated home
  for null results; the `−q_2` baseline's null status belongs there.
- `gr_qm_unification_synthesis.md` (PR #181) — names the
  cascade↔Salpeter as explicitly open; this doc dispositions it.
- `k_of_t_residual_disposition.md` (PR #179) — parallel closure
  achieved via different discriminator structure; useful contrast.

---

## One-line summary

The cascade↔Salpeter slope is Class-2 with a *dual-gate* open
status — the cascade family + depth + `−1/q_3` correction are
structurally forced, the `−q_2 = −2` baseline is structurally null
(physical tongue width is multifractal `β ≈ 2.16`, not `1/q²`), and
the pigeonhole/held-out tests give `p ≈ 0.10` and `N = 1` —
suggestive at 0.33σ but neither structurally end-to-end nor
statistically decisive; closure requires either the structural gate
(grounded `−q_2` derivation) or the statistical gate (independent
cascade-rung confirmations) to clear, and naming both gates
precisely directs future work.
