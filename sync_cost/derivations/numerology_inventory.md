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

### `sin²θ_W = 8/35 = 0.22857`

- Residual vs MS-bar 0.23122: −1.15 %.
- Source: `duty_cycle_dictionary.md` §3, claimed derivation
  `sin²θ_W = q_2³/(q_2³+q_3³) = 8/35`.
- **Disproof-of-structural evidence:** `sinW_running_check.py` final
  verdict: "The tree-scale value 8/35 is a number-theoretic identity
  (q_2³/(q_2³+q_3³)), and its 1.1% agreement with M_Z observation is
  an accidental near-coincidence at the electroweak scale, not a
  consequence of running from a high energy scale." SM 1-loop running
  from Planck gives sin²θ_W ≈ 0.47 at M_Pl, running to ≈ 0.21 at
  1 GeV — the 8/35 value appears naturally at ~54 GeV (unstructured
  scale), not at the framework's declared "tree = Planck."

### `1/α_em (tree) = q_2³ + q_3³ = 35`

- Claimed at tree scale, observed 1/α_em(M_Z) ≈ 127.95.
- Same problem as sin²θ_W: if tree = Planck, SM running does NOT take
  35 to 127.95 over the Planck-to-M_Z range (factor 3.7 off).
- Type B by the same analysis as sin²θ_W. The "tree = 35" is a
  number-theoretic identity (sum of two cubes of framework primes)
  without a scale-consistent derivation to observation.

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
multiple particle-sector predictions from `(q_2, q_3)` at an
unspecified scale. Since the key item (sin²θ_W = 8/35) from this
dictionary is Class 1 numerology, the others from the same ansatz
share the same vulnerability.

### `m_H / v = 1/q_2 = 1/2`

- Residual vs 0.5087: −1.71 %.
- Same "tree scale" issue: at what specific physical scale does the
  framework predict m_H/v = 1/2? If Planck, running takes m_H
  relative to v; if at M_Z (observed), the 1.7 % residual is what's
  actually seen, which is the C2a particle floor.
- Pending: individual audit of whether a running-couplings argument
  derives m_H/v at some specific framework-internal scale.

### `λ_Higgs = 1/(2 q_2²) = 1/8`

- Residual vs 0.1294: −3.36 %.
- Derived in `duty_cycle_dictionary.md` from same (q_2) structure.
- Same status pending.

### `α_s / α_2 = q_3³ / q_2³ = 27/8`

- Residual vs 3.488 at M_Z: −3.24 %.
- Derived from same duty ratios.
- Suspect same status; possibly running-coupling artifact.

---

## Class 4 — Needs individual audit

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

### Higgs self-coupling corrections (e.g. `1/q_2³ + 1/228`)

- `framework_predictions.py` line 268: "m_H = sqrt(2 lambda v²),
  lambda = 1/q_2³ + 1/228".
- The `1/228` correction: 228 = 12·19 = 4·3·19. Not obviously
  framework-native. Might be a fitted/post-hoc correction.
- Needs derivation check — if `228` is framework-derived, structural;
  if fitted to match observation, numerology.

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

- Derived in `baryon_fraction.md` via Farey partition + Z_6 residue
  classes + antiperiodic identification. Structural (though the
  internal Ω_b = 1/19 has the C2b floor at 11σ — that's a finite-
  depth structural residual, not numerology).

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

## Implication for "zero free parameters"

The framework's "zero free parameters" language should be qualified
as **"zero free parameters beyond two observational anchors, with
particle-sector numerology setting a ~3 % cloud of Class 1 and
Class 3 items that have no structural derivation."**

The honest statement is more modest than "all predictions are
framework-derived." Some are, and some are clean; the particle-
sector dictionary predictions are partly numerology. That is an
important distinction for the framework's credibility.

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
