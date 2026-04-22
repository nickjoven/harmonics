# Numerology inventory

Compilation of framework predictions / observations that are confirmed
numerology, noted coincidences, or suspects — so we know what to stop
chasing as if it were structural.

Motivated by the two-floor finding (`particle_sector_audit.py`) which
separated cosmological-partition residuals (7–11 %, multiply-audited
as structural) from particle-sector residuals (1–3 %, some already
flagged in-repo as numerology).

## Classification

**Class 1 — Confirmed numerology.** Framework's own tooling has shown
no structural basis, or the claimed structural derivation is explicitly
contradicted elsewhere in the repo.

**Class 2 — Noted coincidences.** Numerical near-matches with no
framework claim of derivation; recorded in the repo as coincidences.

**Class 3 — Suspect by association.** Predictions from the same
framework substructure (e.g., duty-cycle dictionary) as a confirmed
Class 1 item; likely share the same status pending individual audit.

**Class 4 — Needs individual audit.** Predictions where the type (A
= tight structural, B = numerology, C = structural with running
derivation) is unresolved.

**Class 5 — Explicitly NOT numerology.** Repo contains evidence the
match is structural, distinguishing it from superficially similar
coincidences.

---

## Class 1 — Confirmed numerology

Identities that the framework computes at the bare K=1 level but
that do not connect to observation through any derivation in the
repo. Each is a null finding: the match is a coincidence, not a
structural prediction. `MANIFEST.yml` records these under
`bare_k1_identities`, not `scorecard`.

### `sin²θ_W = 8/35 = 0.22857`

- Bare K=1 identity: `sin²θ_W = q_2³ / (q_2³ + q_3³) = 8/35`
  from `duty_dimension_proof.md`, `three_dimensions.md`,
  `klein_bottle_derivation.md`, `gauge_dictionary.md`.
- Gap vs MS-bar 0.23121 at M_Z: −1.15 %.
- **Null findings (no framework prediction at M_Z):**
  - `sinW_running_check.py`: SM 1-loop running is incompatible with
    the framework's "tree = Planck" identification — the sign of
    `dsin²θ_W / dlnμ` is opposite to what the tree → M_Z gap requires.
  - `sinw_fixed_point.md`: no K* ∈ [0.93, 0.99] reproduces sin²θ_W
    at M_Z via finite-K duty dynamics.
  - `sinw_effective_dimension.md`: the d_eff = 80/27 proposal is
    conditional on three unformalized steps (see Class 4).

### `1/α_em (tree) = q_2³ + q_3³ = 35`

- Bare K=1 identity from `duty_cycle_dictionary.md` §9,
  `duty_dimension_proof.md`, `three_dimensions.md`,
  `klein_bottle_derivation.md`.
- Observed 1/α_em(M_Z) ≈ 127.95.
- **Null finding:** SM running from Planck does not take 35 to
  127.95 over the Planck-to-M_Z range (factor 3.7 off). The
  "tree = 35" is a number-theoretic identity (sum of two cubes of
  framework primes) with no scale-consistent derivation to observation.

### `+1/228` correction to λ_H

- Form: `λ_H = 1/q_2³ + 1/228`, with `228 = q_2²·q_3·|F_7| = 12·19`.
  Gives close match to observed λ_H ≈ 0.1294 at M_Z.
- **Null finding:** the prime factorization uses framework integers,
  but no derivation of the *additive* correction form
  `+1/(q_2²·q_3·|F_7|)` from tree-scale running, loop-correction
  structure, or substrate combinatorics exists.
  `framework_predictions.py:268` removes the correction with the
  verdict "fitted term, not derived." The bare K=1 identity
  `λ_H = 1/q_2³ = 1/8` stands (see Class 3).

---

## Class 2 — Noted coincidences (no framework claim)

### `v/M_P ≈ 13⁻¹⁵` (3.13 % near-match)

- Explicitly tested in `v_over_mp_structural_attempt.md`.
- Yukawa-mediant cascade (`yukawa_mediant_cascade.py`) found the
  SB subtree at depth 15 is binary (2¹⁵), not 13-adic — no structure
  match.
- Z_30 substrate check (`z_30_substrate_check.py`) found Z_30 = Z_2
  × Z_3 × Z_5 does not naturally live on the Klein-Kuramoto lattice
  — dead end.
- Status: numerology with framework-native integer factorization
  (15 = q_3·(q_2+q_3)), no structural derivation.

### `φ⁻⁸⁰ ≈ v/M_P` (5.32 % near-match)

- Noted in `anchor_count_audit.md`.
- No structural argument attached.
- Numerical coincidence only.

### Klein nodal parity (single connected curve at (5, 5, 1) σ=+node)

- Observation at (5, 5, 1), σ=+node, ω_rot=0.03, γ=5: a single
  connected diagonal line of seeds on the sphere.
- **Null finding:** simulator uses `U = Y²`, which is Z₂-symmetric
  for all ℓ — the (−1)^ℓ sign flip on Y doesn't survive squaring.
  Dynamics cannot discriminate parity. The observed single curve
  is gradient descent on a slowly-rotating static landscape
  (ω_rot=0.03 ≠ 0) tracking one meridional arc; no topological
  content. See `klein_nodal_parity.md` for the derivation.
- Status: visual coincidence.

### Pythagorean comma vs K_Greene (0.17 % near-match)

- `kam_bridge_synthesis.md` §6, recorded as:
  "1/(3¹²/2¹⁹)² = 0.97325 vs K_Greene = 0.97164, offset 0.17 %.
  K_Greene has no known closed form; Pythagorean comma is from
  musical temperament. No structural route connects them."
- Status: recorded coincidence with explicit "not a framework lever"
  note.

---

## Class 3 — Suspect by association (duty-cycle dictionary)

The duty-cycle dictionary (`duty_cycle_dictionary.md`) produces
multiple particle-sector identities from `(q_2, q_3)` at an
unspecified scale. Since the key item (sin²θ_W = 8/35) is Class 1
numerology, the others share the same vulnerability — bare K=1
identities without a scale-consistent derivation to M_Z.
`MANIFEST.yml` records all four under `bare_k1_identities`.

### `m_H / v = 1/q_2 = 1/2`

- Bare K=1 identity from `duty_cycle_dictionary.md` §8: "m_H is
  the lowest excitation of the q = 2 tongue."
- Gap vs 0.5087: −1.71 %.
- **Null finding:** no derivation connects the K=1 identity to the
  observed value at M_Z.

### `λ_Higgs = 1/q_2³ = 1/8`

- Bare K=1 identity: duty of the q=2 sector,
  `duty(q_2) = 1/q_2^3 = 1/8` (`duty_cycle_dictionary.md` §8).
- Gap vs 0.1294: −3.36 %.
- **Null finding:** no derivation connects the K=1 identity to M_Z.
  The `+1/228` correction that would close the gap is itself a
  null (Class 1).

### `α_s / α_2 = q_3³ / q_2³ = 27/8`

- Bare K=1 identity: ratio of bare duty cycles at K=1
  (`duty_cycle_dictionary.md` §2).
- Gap vs 3.488 at M_Z: −3.24 %.
- **Null finding:** same K → μ mapping gap as sin²θ_W. SM RG
  cannot connect 27/8 at tree scale to 3.488 at M_Z in a
  framework-consistent way, and no alternative derivation exists.

---

## Class 4 — Needs individual audit

### `sin²θ_W` via effective dimension d_eff = 80/27

- Proposed in `sinw_effective_dimension.md`. Replaces d → d_eff
  in the bare formula, giving
  sin²θ_W = 2^(80/27) / (2^(80/27) + 3^(80/27)) = 0.23123,
  0.5σ from PDG MS-bar at M_Z.
- Uses only {q₂, q₃, d} — no new dimensional input or free parameter.
- Currently conditional on three unformalized steps
  (`sinw_effective_dimension.md:179–200`):
  1. "Occupied frequency interval → effective dimension reduction"
     is geometrically motivated but not derived from integrating the
     coupling over the complement of the q₃ tongue.
  2. The asymmetric choice "only q₃ correction, not q₂" is
     heuristic — a systematic perturbative expansion including the
     q₂ correction and cross-terms has not been performed.
  3. The identification of the root-level formula with MS-bar at M_Z
     is motivated but not mapped onto the MS-bar subtraction procedure.
- If all three steps are formalized, sin²θ_W should be promoted back
  into `MANIFEST.yml:scorecard` with source
  `[sinw_effective_dimension, duty_dimension_proof, three_dimensions,
  klein_bottle_derivation, gauge_dictionary]`. Until then, not a
  framework prediction.

### Generation-mass hierarchy 26 : 7 : 1

- `generation_mechanism.md` claims `26^a : 7^a : 1` with rational a
  for m_e : m_μ : m_τ (or similar). Framework integers: 26 = q_2·|F_6|,
  7 = q_2² + q_3.
- Observed m_μ/m_e = 206.77; m_τ/m_μ = 16.82.
- If `26^a = 206.77`, a ≈ ln(206.77)/ln(26) ≈ 1.635 (not clean).
- If `7^a = 16.82`, a ≈ ln(16.82)/ln(7) ≈ 1.451 (not clean, and
  different from 1.635).
- Likely numerology unless a = exactly (q_2 + q_3)/q_3 or similar
  framework-derived exponent; needs specific derivation check.

### `K_STAR^14 = 1/8` conjecture (τ-mass related)

- Flagged in `CHAIN_KSTAR.md` §Status as **conjectured, testable**.
  Decision criteria stated: future m_τ precision of σ < 0.03 MeV
  would confirm or refute.
- Status explicit: "If refuted, the specific closed form `K^14 = 1/8`
  is a high-precision coincidence; Steps 1–5 still hold."
- Honest about numerology risk; awaiting experimental data.

### `N_efolds = √5 / rate ≈ 61.3`

- `alphabet_depth21.py` output.
- The appearance of √5 = φ − ψ from the fixed-point polynomial is
  structural, BUT the matching to observed ~60 inflation e-folds
  depends on the observed n_s tilt as input (framework didn't
  predict N_efolds independently; it's inverted from n_s).
- Borderline: structural math, but numerical match requires
  observational anchor.

---

## Class 5 — Explicitly NOT numerology per repo evidence

### `a_0 = c H₀ / (2π)` (MOND acceleration scale)

- `a0_threshold.md` §line 246: explains the "cosmic coincidence"
  a_0 ≈ c H_0 as a *structural* consequence of `a_0² ∝ Λ` — both a_0
  and c H_0 are set by Λ. Not a coincidence per framework.
- Cross-reference: `a0_observable.py` and related derivations.

### Saddle-node → Born rule `|ψ|²`

- `a1_from_saddle_node.md` §line 16: explicitly "not a numerical
  coincidence but an instance of the framework's parabola primitive
  acting at an Arnold-tongue boundary — the same primitive that gives
  `|ψ|²` in `born_rule.md`." Structural via saddle-node universality
  from pure math.

### `λ_unlock = (4G − π ln 2)/π` at K = 1

- `lambda_unlock_closed_form.py`: numerical integration matches
  closed form to 1e-15. Algebraic identity via integration-by-parts.
  `kam_bridge_synthesis.md` §4: identified as the Arnold Lyapunov on
  the Z_2 quotient. Structural.

### `R = 6·13⁵⁴`, `Λ·ℓ_P² = 13⁻¹⁰⁸/12`

- Derived in `hierarchy_gaussian_lattice.md` via the cell-counting
  formula `R = q_2 q_3 · (q_2² + q_3²)^(q_2 q_3^d)`. Structural.

### Ω partition 1:5:13/19

- Derived in two stages, both combinatorial, no fitted factors:
  - 13:6 (Ω_Λ:Ω_m) from Farey count |F_6|, φ(7), |F_7|
    (`farey_partition.md`)
  - 1:5 (Ω_b:Ω_DM) from Z₂ representation theory on coprime-pair
    antisym modes + EM cross-sector criterion
    (`omega_partition_combinatorial.md`, `baryon_fraction.md`)
- The two mechanisms (Farey counting, Klein-antipodal Z₂ rep) are
  distinct from the mode-pair XOR filter in `xor_derivation.md`,
  which is a separate Z₂ structure.
- Ω_b = 1/19 has a 6.7% observational residual attributed to
  Klein-eigenmode width asymmetry (sym/antisym tongue widths) and
  boundary-weight / decoherence corrections — finite-depth
  structural residual, not numerology.

---

## What to stop chasing

Based on this inventory:

1. **Stop looking for "tree scale" structural derivations of the
   duty-cycle-dictionary predictions** (sin²θ_W = 8/35, 1/α_em = 35,
   m_H/v = 1/2, λ_H = 1/8, α_s/α_2 = 27/8). They are Class 1 or
   Class 3 numerology. The particle-sector ~1-3 % floor is
   attributable to this ensemble, not to a structural residual.

2. **Stop looking for a framework-integer closed form for v/M_P**.
   The 13⁻¹⁵ match is Class 2 coincidence. No structural route
   survived the attempts (Yukawa cascade, Z_30 substrate).

3. **Stop looking for Pythagorean-comma / K_Greene connection**.
   Class 2, explicitly recorded.

4. **Stop looking for φ-power match to v/M_P**. Class 2.

## What remains genuinely structural

1. Cosmological predictions with explicit derivations: R, Ω partition,
   Λ·ℓ_P², Friedmann form at r = 1.
2. The cosmological C2b floor (A_s, Ω_b, Ω_c/Ω_b at 7-11 %): *real*
   structural residual from finite-depth partition counting,
   multiply-audited.
3. λ_unlock closed form, the Z₂-quotient identification, R = 6·13⁵⁴
   — all with explicit derivations.
4. Born rule from saddle-node, a_0 = cH_0/(2π) from Λ — structurally
   derived per repo.

## Implication for closure language

The phrase "zero free parameters" is retired across this repository
(see `statistical_conventions.md`). Individual predictions are
classified under Z1–Z3 directly; nothing is labelled "zero free
parameters" anymore.

Framework-level status: **two dimensional anchors** (H_0, v_EW) —
see `anchor_count_audit.md` for the five obstructions preventing
closure to one.

Per-prediction status: specific structural predictions (the Ω
partition, R, Λℓ_P², MOND a₀, gauge group, anomaly cancellation,
etc.) pass Z1–Z3. The particle-sector ~3% numerology cloud
(Class 1 and Class 3 items) does not pass Z2 and is declined in
`MANIFEST.yml:bare_k1_identities`.

The accurate statement: specific predictions pass Z1–Z3; the
framework as a whole uses two dimensional anchors plus a
vocabulary of framework integers (q_2, q_3, d), and has a ~3%
particle-sector numerology cloud alongside the structurally
derived content.

## Cross-references

| File | Role |
|---|---|
| `sinW_running_check.py` | Class 1 disproof for sin²θ_W = 8/35 |
| `CHAIN_KSTAR.md` | Class 4 explicit testability statement |
| `v_over_mp_structural_attempt.md` | Class 2 documentation for v/M_P |
| `yukawa_mediant_cascade.py` | structural null for Class 2 v/M_P candidate |
| `z_30_substrate_check.py` | dead end for Class 2 v/M_P candidate |
| `kam_bridge_synthesis.md` | Class 2 Pythagorean comma recording |
| `duty_cycle_dictionary.md` | source of many Class 3 items |
| `a1_from_saddle_node.md` | Class 5 structural counter-claim |
| `hierarchy_gaussian_lattice.md` | Class 5 cell-counting derivations |
| `anchor_count_audit.md` | Class 2 numerology + anchor analysis |
| `particle_sector_audit.py` | particle-sector floor measurement |
