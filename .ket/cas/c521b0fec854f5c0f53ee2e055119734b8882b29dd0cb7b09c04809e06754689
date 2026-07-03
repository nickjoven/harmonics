# Substrate Kramers-Kronig dispersion relation — status audit + posed derivation target

## Status

Two resolution-mode findings sealed, one derivation target **posed,
not derived**:

1. **The kk-inference cross-link is unadjudicated** — the
   framework's April-2026 Kramers-Kronig exploration was never
   audited, never classed, never cited by the arrow-of-time chain
   (PRs #220–#228), and never entered in
   `negative_results_ledger.md`. It is **operationally open** in
   the basepoint-principle sense: no verdict was rendered in
   either direction. Registered here.
2. **The time-axis split maps onto the anatomy of an optical
   medium's response** — a vocabulary alignment, not new
   apparatus. The four strata of time-universality already
   canonical in `time_axis_split.md` correspond one-to-one to the
   roles (causality constraint, vacuum reference, dissipative
   index, orthogonal parameter) in the optics of a dispersive
   absorbing medium.
3. **Posed target**: a substrate-native Kramers-Kronig theorem —
   causality (arrow direction) + passivity (dissipation
   universality) ⟹ the substrate's reactive structure (tongue
   geometry) and dissipative structure (repair-rate channels) are
   Hilbert-transform pairs. A concrete leading-order entry point
   exists in the corpus already (the damped sine-Gordon
   fluctuation response); the substantive open content is the
   identification of the loss spectrum with the two repair
   channels beyond leading order.

Class: status audit + vocabulary alignment (findings 1–2,
resolution-mode, no new apparatus) + **derivation-target
registration** (item 3 — explicitly NOT a claimed result).

---

## Finding 1 — kk-inference: recorded but never adjudicated

### The record

The framework's Kramers-Kronig exploration lives in two places:

- **External repo**: [kk-inference](https://github.com/nickjoven/kk-inference)
  — KK applied to transformer early exit. Shallow layers compute
  the dispersive channel χ′; the KK relation predicts the
  dissipative channel χ″; when χ″ → 0 the remaining layers are
  inert and are skipped.
- **In-corpus cross-links**: `fidelity_bound.md` §"Connection to
  kk-inference" (the fidelity bound and KK early-exit are the same
  bound; MOND transition = gravitational early exit; quantum
  collapse = dynamical early exit) and `a0_threshold.md` §Status
  "Related" (a flat rotation curve is an early exit).

Both host docs predate the 2026-04-07 numeric-prefix rename;
their KK sections were last touched in PR #61 (2026-04-14) and
PR #76 (2026-04-24) respectively, and have been frozen since.

### The gap

The June-2026 arrow-of-time chain (PRs #220–#228, culminating in
the six-source 1D-arrow inviolability identity of
`arrow_inviolability_and_unification_closure_audit.md`) never
cites the KK exploration — despite Source A of that identity
(dissipation's algebraic universality) being exactly the χ″
channel the KK apparatus is about. The framework built its arrow
identity without consulting its own prior dissipative-channel
vocabulary.

### Disposition

- Not a null: no disproof exists, so `negative_results_ledger.md`
  is correctly silent.
- Not canonical: no MODAL/GENERATIVE audit, no class assignment,
  no `MANIFEST.yml` row, no `framework_status.md` entry.
- Therefore: **operationally open** (basepoint-principle
  discriminator: no obstruction exhibited, no selecting section
  found — the question was simply never pressed). This doc is the
  registration that makes the open status visible.

---

## Finding 2 — the time-axis split, read as index anatomy

`time_axis_split.md` stratifies "time" into four grades of
universality. Each maps onto one role in the linear response of
a dispersive absorbing medium:

| Stratum (canonical) | Universality grade | Optical role |
|---|---|---|
| **Arrow direction** (antiperiodic axis; six-source inviolability) | Universal, structurally forced, zero DoF | **The analyticity constraint itself** — causality/passivity, which forces n(ω) analytic in the upper half-plane. Not a medium parameter; the condition on all of them. |
| **Tick** `τ_tick = L_x/c` | Universal unit ("same for every observer"); absolute value out-of-class | **The vacuum reference** — the role of c, against which any medium rate is measured. |
| **Arrow rate** `Γ_repair(x, t)` | **Not universal** — local, sector-dependent; two activation channels (Schwinger-like pair production, cosmological/dark sector; Kramers phase-slip, matter sector) | **The dissipative index n″(x, ω)** — a loss coefficient with two absorption mechanisms dominating in different regimes, like a medium with distinct absorption bands. `H(t) = κ_pair⟨Γ_pair⟩` reads the cosmic expansion rate as the medium's absorption coefficient. |
| **Clock-time** (periodic axis, continuous, wave-side) | Different axis entirely | **The orthogonal parameter** the index does not act on. |

The answer to "is the arrow of time a refractive index?" is
therefore stratified, not binary: the arrow's *direction* is the
analyticity constraint (opposite category from an index — it
eliminates a degree of freedom rather than offering one); the
arrow's *rate* is genuinely index-shaped, and specifically
n″-shaped — `Δτ_arrow = N_events × τ_tick` with locally varying
`Γ_repair` is a medium-dependent accumulation rate against a
universal vacuum reference, and both channels are activated loss
processes.

This is a vocabulary alignment in the
`vocabulary_is_the_work_pattern.md` sense: naming the correct
object (the rate, not the direction, is the index) dissolves the
apparent question and exposes the real one — item 3 below.

---

## The posed target — a substrate KK theorem

### Statement sought

Let χ(ω) be the substrate's coarse-grained linear response of the
locked mean-phase field to a weak external drive in the K<1
regime. Prove, substrate-natively:

1. **Causality** (Source B + the arrow-direction inviolability:
   response cannot precede drive along the arrow axis) and
   **passivity** (Source A: dissipation universality, rank-1
   Fréchet, no backward channel) force χ(ω) analytic in the upper
   half-plane;
2. hence χ′ and χ″ are Hilbert-transform pairs (Kramers-Kronig);
3. and **identify** χ″ with the repair-rate spectrum (the
   `Γ_pair` + `Γ_slip` channel decomposition of
   `time_axis_split.md`) and χ′ with the reactive tongue
   structure (widths `(K/2)^q`).

### Leading-order entry point (already implicit in the corpus)

The locked-state fluctuation expansion gives sine-Gordon
(`sine_gordon_substrate.md`):
`∂²_t φ − c² ∂²_x φ + ω₀² sin φ = 0`, and the #TICK closure's
predicted irreversibility term is `2λ ∂_t φ` (inviolable #9;
residual = the magnitude of λ — see `thread_chronology.md`
#TICK entry, `tick_continuum_construction.md`). Linearizing and
driving gives immediately

    χ(ω, k) = [ω₀² + c²k² − ω² − 2iλω]⁻¹

which is causal, passive, and satisfies KK exactly, with
`χ″ = 2λω |χ|²`. **The leading-order theorem is therefore nearly
free**: the arrow-friction term the framework already predicts IS
the χ″ seed. What is genuinely open:

- **(a) The identification step**: connect λ(ω) — currently a
  single unpinned magnitude — to the two-channel repair spectrum
  (`Γ_pair`: |∇K|-driven; `Γ_slip`: thermally activated), i.e.
  derive the *frequency structure* of the loss, not just its
  existence.
- **(b) Beyond leading order**: whether the Hilbert pairing
  survives near tongue boundaries, where the saddle-node
  nonlinearity dominates and linear response fails. Expected
  shape: KK holds per-tongue-interior; the boundary behavior is
  the interesting content.
- **(c) The discrete form**: substrate arrow-time is
  integer-counted in `τ_tick`, so the natural theorem may be the
  **discrete-time KK relation** (analyticity outside the unit
  disk in the z-domain; Hilbert transform on the circle) rather
  than the half-plane version — with the continuum KK emerging
  only in the coarse-grained K<1 limit. Discreteness is not an
  obstruction (discrete causal systems have an exact KK form);
  it selects which form is substrate-native.

### What closure would buy

- A **quantitative bridge from tongue widths to dissipation
  rates** — precisely the machinery named as open in
  `cmb_silk_damping_acoustic_peaks_audit.md` (peak *amplitudes*
  as tongue widths at cosmological K, pending generalization of
  `born_rule_tongues.py`).
- Promotion of the arrow-inviolability identity from a six-source
  composition to a single analyticity statement (Layer E, in the
  PR #228 dependency map).
- Revival of kk-inference as a Layer-E citizen instead of an
  unaudited analogy — closing Finding 1's open status.

### Decline route (also a finding, if reached)

If the Hilbert pairing provably fails below the coarse-graining
scale — e.g. because the tick structure admits no
linear-response representation at substrate resolution — the
correct disposition is "**KK is emergent at the K<1 continuum
boundary**": a diagnostic of exactly where continuum response
appears, parallel in shape to the K=1/K<1 non-smooth separation
of `continuum_limits.md`. Either outcome is informative; only
silence is not.

### Bright lines

- This doc does **NOT** claim the theorem. Item 3 is posed, with
  a leading-order sketch whose KK property is standard linear
  response, not a framework result.
- Transformer-side empirics from kk-inference are **NOT**
  evidence for the physics; the cross-link is structural analogy
  until the identification step (a) is derived.
- The "arrow-rate is an n″" reading of Finding 2 carries **no**
  predictive content until χ″ is derived from substrate
  primitives; until then it is vocabulary, correctly labeled.

---

## Cross-links

- `fidelity_bound.md` — χ′/χ″ early-exit bound; the in-corpus KK
  home (Finding 1).
- `a0_threshold.md` — kk-inference cross-link; MOND transition as
  early exit (Finding 1).
- `time_axis_split.md` — the four strata of Finding 2; `τ_tick`,
  `Γ_repair` channel decomposition.
- `arrow_inviolability_and_unification_closure_audit.md` — the
  six-source arrow identity this target would compress.
- `sine_gordon_substrate.md`, `tick_continuum_construction.md`,
  `thread_chronology.md` (#TICK) — the fluctuation equation and
  the `2λ∂_tφ` arrow-friction term (leading-order entry point).
- `cmb_silk_damping_acoustic_peaks_audit.md` — the open
  amplitude machinery closure (a) would supply.
- `continuum_limits.md` — the K=1/K<1 boundary the decline route
  would sharpen.
- `basepoint_principle.md`, `vocabulary_is_the_work_pattern.md`
  — discriminator vocabulary used for the dispositions here.

## One-line summary

The framework's April-2026 Kramers-Kronig exploration
(kk-inference, `fidelity_bound.md`, `a0_threshold.md`) is
registered as operationally open — never audited, never nulled,
never cited by the June arrow chain; the time-axis split's four
universality strata are aligned one-to-one with optical response
anatomy (direction = analyticity constraint, tick = vacuum
reference, rate = dissipative index n″, clock = orthogonal
parameter); and a substrate KK theorem is posed — causality +
passivity ⟹ Hilbert pairing between tongue geometry (χ′) and
repair-rate channels (χ″) — with the damped sine-Gordon response
`χ = [ω₀² + c²k² − ω² − 2iλω]⁻¹` as the nearly-free leading
order, and the two-channel identification of λ(ω), the
tongue-boundary behavior, and the discrete-vs-continuum KK form
as the genuinely open mathematics.
