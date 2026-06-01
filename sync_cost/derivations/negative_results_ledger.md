# Negative-results ledger — the single archival home for failed, null, and superseded claims

**This is the one place the framework's negative results live.**
Every row is self-contained: it states what was claimed, the
settled disposition (failed / null / superseded / eliminated), and
the one-line reason. A chunk retrieved from this file in isolation
is correct without cross-referencing.

Why this file exists:

- Public surfaces (README, `index.html`, the deployed glossaries)
  must not present any of these as corroborated results. When a
  claim here appears anywhere as a "prediction," "forced value,"
  or "verified" entry, that is an overstatement to fix.
- The derivation corpus records these dispositions in scattered
  places (`numerology_inventory.md` Class 1, `framework_status.md`
  Eliminated/Fails, `thread_chronology.md`, `no_rescaling.md`).
  This ledger consolidates the *negative* dispositions so readers
  and ingestion pipelines have one authoritative, self-contained
  reference (addresses issue #157's "superseded content confuses
  readers and LLMs" problem without moving load-bearing files).

The standing predictions are catalogued separately in
`framework_status.md` (Survives) and `MANIFEST.yml` (`scorecard`);
the K=1 reference identities are in `MANIFEST.yml`
(`bare_k1_identities`). This file is the complement: what does
**not** stand.

---

## 1. Failed / null physics claims

These are arithmetic identities or proposed mechanisms that do
**not** connect to observation in a framework-consistent way. They
may be recorded elsewhere as bare K=1 reference identities, but
their use as physical predictions is disproven or unsupported.

| Claim | Value/form | Disposition | Why it failed | Canonical record |
|---|---|---|---|---|
| **sin²θ_W at M_Z** | 8/35 = q₂³/(q₂³+q₃³) = 0.22857 | **Class 1 / Fails** (stands only as a declined K=1 reference identity, *not* a prediction at M_Z) | SM 1-loop running is incompatible with "tree = Planck": the sign of `dsin²θ_W/dlnμ` is opposite to what the tree→M_Z gap requires. The 1.1% agreement is an accidental near-coincidence at the electroweak scale, not a consequence of running. | `numerology_inventory.md` §Class 1; `sinW_running_check.py`; `framework_status.md` Fails |
| sin²θ_W fixed-point hypothesis | a K* ∈ [0.93, 0.99] reproducing the M_Z value via duty dynamics | **Ruled out** | "No K in [0.93, 0.99] reproduces either constraint; the joint fixed-point question is moot." | `sinw_fixed_point.md` |
| sin²θ_W via effective dimension | 2^(80/27)/(2^(80/27)+3^(80/27)), d_eff = 80/27 (0.5σ) | **Null** (reclassified down from Class 4) | All three derivation mechanisms (box-counting dimension, width/period re-derivation, measure renormalization) fail to produce d→d_eff from primitives. An ansatz, not a derivation. | `g1_computation_result.md`; `numerology_inventory.md` §Class 2 |
| **α_s/α_2 at M_Z** | 27/8 = q₃³/q₂³ = 3.375 (stands only as a declined K=1 reference identity) | **Null at M_Z** | Same K→μ running gap as sin²θ_W: SM RG cannot connect 27/8 at tree scale to the observed M_Z value (3.2% gap) in a framework-consistent way, and no alternative derivation exists. | `numerology_inventory.md`; `duty_cycle_dictionary.md` |
| **1/α_em (tree)** | q₂³ + q₃³ = 35 (declined K=1 reference identity) | **Class 1 / null at M_Z** | SM running from Planck does not take 35 to 127.95 (factor ~3.7 off). A number-theoretic identity with no scale-consistent derivation to observation. | `numerology_inventory.md` §Class 1 |
| **+1/228 correction to λ_H** | λ_H = 1/q₂³ + 1/228, 228 = 12·19 | **Eliminated / fitted, withdrawn** | No derivation of the additive correction form exists; `framework_predictions.py:268` removes it ("fitted term, not derived"). The bare identity λ_H = 1/q₂³ = 1/8 remains a declined K=1 reference only. | `numerology_inventory.md` §Class 1; `framework_status.md` Eliminated |
| **Generation-mass hierarchy** | 26 : 7 : 1; m/m = 26^a, 7^a, a ∈ {2, 5/2, 3} | **Class 1 / null** | μ/e prediction 7^(5/2) = 129.6 vs observed 206.8 = 37% off ("fails Z1 by ~370000σ"). Multiple equivalent integer constructions (no forced base); the invoked "running correction" is an undefined post-hoc patch. | `numerology_inventory.md` §Class 1; `generation_mechanism.md` §4 |
| **Mass-function -q_2 baseline via tongue width = 1/q²** | M(p/q) ∝ w(p/q) ∝ 1/q² at K=1 ⇒ slope -2 | **Null at the width step** (mass ∝ physical width survives; width = 1/q² does not) | A complete K=1 staircase has Σ w = 1, forcing the width exponent β > 2 (Σ φ(q)/q² diverges, so β=2 over-fills [0,1]); measured β ≈ 2.3. The 1/q² is the combinatorial Stern–Brocot tree weight, not the physical Arnold-tongue width. Dynamical slope is -1-2/β ≈ -1.86, not -2 — so the bowed/Salpeter -7/3 has no grounded dynamical baseline. Does **not** affect the Farey **count** |F_n| ~ n² (Ω_Λ = 13/19), the Step-2 orbit count, or ε = const. | `farey_tongue_width_null.py`; `mass_entrained_measure.md`; `imf_bowed_cascade.md` |
| **K_STAR¹⁴ = 1/8** (τ-mass) | K_STAR_lep¹⁴ ≈ 0.12498 vs 1/8 (0.594σ) | **Class 2 coincidence** (demoted from Proposed/Class 4) | Steps 1–5 (integer 14 = q₂·|F₄| from Klein topology) stand; Step 6's exponent choice q₂^(−q₃) is one of several small-integer variants, not forced. The 0.07%-level lepton-mass ratios that ride on this closed form inherit its Class-2 status — they are not scorecard predictions. | `CHAIN_KSTAR.md` §Status; `numerology_inventory.md` §Class 4 |
| **v/M_P closed form** | 13⁻¹⁵ (3.1% off) | **Class 2 / Eliminated** | Not structurally forced; the Yukawa-mediant cascade is null (binary 2¹⁵, not 13-adic) and the Z₃₀ substrate route is a dead end. | `numerology_inventory.md` §Class 2; `framework_status.md` Eliminated |
| **φ⁻⁸⁰ ≈ v/M_P** | φ⁻⁸⁰ (5.3% off) | **Class 2 / Eliminated** | Numerical coincidence only; no structural argument attached. | `numerology_inventory.md` §Class 2; `framework_status.md` Eliminated |
| **Pythagorean comma vs K_Greene** | 1/(3¹²/2¹⁹)² = 0.97325 vs 0.97164 (0.17%) | **Class 2 / Eliminated** | K_Greene has no known closed form; no structural route connects them. Recorded from net-rejected, never-committed work. | `numerology_inventory.md` §Class 2; `framework_status.md` Eliminated |
| **Particle near-match cloud** | m_H/v, λ_H, α_s/α_2, etc. (1–3% floor) | **Pigeonhole, not signal** (Class 2 by construction) | Permutation null (10⁴ trials): the actual match count is statistically consistent with the null at α=0.05 (p ≈ 0.13 / 0.20 / 0.07). | `framework_status.md` Region C; `numerology_count_phase_b.md` |
| **Circle-map tongue-count coincidences** | N(K,ε) = 19, = 13 at framework integers | **Class 2 coincidence / pigeonhole** | The ε at which the count hits a framework integer is unforced; three forcing arguments tested, all null. | `numerology_inventory.md` §Class 2; `k_scaling_scan.md` |
| **Suspended spinning die / rotor "mode-locks"** | Spin-down of an imbalanced suspended rotor (or symmetric top) | **Resonance crossing, NOT locking** | The swing peaks as the spin:pendulum ratio *passes through* low-order rationals, but the ratio never *holds* on one — the descent is a monotone slide with no plateau, for every value of the contact/reaction drag. The coupling is one-way (spin drives swing, not vice versa), so no Arnold tongue forms; this carries none of the Stern-Brocot/mediant content, which requires a finite-width lock (a devil's-staircase plateau). A clean *crossing* example, useful only to delimit what locking is not. Genuine locking needs the bidirectional phase feedback of `driven_stribeck.py`. | `suspended_top.py` (`demo_resonance_vs_locking`); `suspended_rotor.py` module docstring |

## 2. Superseded scientific claims (do not re-assert)

These were once stated and have since been corrected. The current
value is given first; the superseded value must not be re-asserted.

| Topic | Current (settled) | Superseded claim | Canonical record |
|---|---|---|---|
| **S_v(K=1)** | ≈ 11.515 (computed: H_BB ≈ 9.580 ≠ H_CC ≈ 3.645, E_cross = −4) | "S_v = 16 exact" — do not re-assert | `discrete_reduction_computed.md`; `thread_chronology.md` |
| **Inflation duration** | Anchor-conditional, correctly declined (#INF: \|∇K\|_inflation is the Schwinger-image of an out-of-class anchor; geometric-seam route proven structurally impossible ∀K) | "Inflation duration is parameter-free from S_v = 16" — retracted | `inflation_seam_anchor_closure.md`; `thread_chronology.md` |
| **Continuous-flow fingerprint** | D ≈ 0.8700 is **not** a framework prediction; continuous flow is eliminable | "D ≈ 0.8700 is a framework prediction" | `mediant_vs_flow_calc.md`; `thread_chronology.md` #FLOW |
| **Dimensionful inputs** | **Two** anchors required (H₀ and v_EW); reduction to one is blocked by five obstructions | "single dimensionful input" — overstated the repo's actual derivation state | `MANIFEST.yml` dimensionful_input_note; `anchor_count_reaudit.md` |
| **"Zero free parameters" (framework-level)** | Retired across the repository; replaced by two-anchor minimality + per-prediction Z1–Z3 accounting. (The scoped phrase "zero free parameters *at the closure level*" for a specific closure is acceptable; the sweeping framework-level claim is not.) | "the framework has zero free parameters" (unscoped) | `numerology_inventory.md` §Implication; `statistical_conventions.md` |
| **K_c^RFE** | An explicitly-flagged conjecture (Σw(1) ≈ 1.5617 on a secondary RFE branch), never promoted to a claim | presenting K_c^RFE ≈ 1.56 as a result | `thread_chronology.md` #PROPOSED |

## 3. Eliminated visualizer-physics framings

Readings of the ψ_F visualizer / simulator that were checked and
found to be category errors (the code is gradient descent on a
static potential, not the dynamical system the framing assumed):

- **Klein nodal parity** (odd-m Möbius vs even-m arcs): null. The
  simulator uses U = Y², which is Z₂-symmetric for all ℓ; the
  (−1)^ℓ sign flip does not survive squaring, so the dynamics
  cannot discriminate parity. (`klein_nodal_parity.md`)
- **Twist-map / KAM / cantorus / Lyapunov** framings of the ψ_F
  visualizer: eliminated; source inspection confirms gradient
  descent on a static potential. (`framework_status.md` Eliminated)
- **Mean-field Ψ Arnold-tongue structure**: eliminated
  ("Adler-only"). (`framework_status.md` Eliminated)
- **H_inf (absolute value) from framework integers**: out of
  class — dimensionful, requires the cosmological H₀ anchor; only
  the ratio H_inf/M_P is framework-derivable. (`h_inf_status.md`)

## Provenance note — missing disproof artifacts

Several dispositions above are recorded only in summary form
because the original disproof artifacts are **not present in the
repository**: `v_over_mp_structural_attempt.md`,
`yukawa_mediant_cascade.py`, `z_30_substrate_check.py`,
`kam_bridge_synthesis.md` (explicitly "net-rejected work … source
doc never committed"), `klein_spectrum.py`,
`kuramoto_induced_map.py`. The dispositions are preserved here
self-containedly so each negative result stays documented even
without its source file.

## Cross-links

- `MANIFEST.yml` — `scorecard` (standing predictions) and
  `bare_k1_identities` (declined K=1 reference identities; the
  same numbers as several Section-1 rows, standing only as K=1
  references and never as M_Z predictions).
- `framework_status.md` — settled-state catalog (Survives / Floor
  / Fails / Eliminated); points here for the negative dispositions.
- `numerology_inventory.md` — Class 1–5 classification; Class 1
  and the null findings are mirrored here.
- `thread_chronology.md` — resolved-thread arcs; the superseded
  values in Section 2 are mirrored here.
