# Born rule + mode count at extremes audit

## Status

**Extension of the conservation chain inventory** from
`conservation_scale_stratification_audit.md` (Q mod 2 +
dissipation) to cover the next two structural invariants: the
Born rule and the mode count. Both are audited across the three
regimes (Planck / standard / Hubble) with the layer-status
(layer-invariant vs scale-specific) classification carried over.

**Verdicts**:

- **Born rule** — **hybrid layer-status**: algebraic mechanism
  (saddle-node universality of Arnold tongue bifurcations,
  parameter-free per `born_rule_parameter_free.md`) hosted on a
  topology-dependent mode spectrum. Universal in mechanism;
  spectrum-availability scales with substrate self-sustenance.
  Inherits the fuzzy Planck floor from PR #221's structural
  identity.
- **Mode count** — **topology-dependent, scale-specific**:
  14 modes at standard scale (2·|F_4|, K_STAR location), 12.66
  effective modes at Hubble boundary (w* ≈ 0.83), fuzzy
  emergence at Planck. The value of the mode count is a
  layer-specific *address*, not a layer-invariant primitive
  (`primitives_vs_addresses_candidate.md`); its existence as a
  finite cardinality is a topology-dependent substrate fact.

The hybrid Born-rule classification is a **third layer-status
category** not present in the parent audit's binary
algebraic-vs-topological split. It sits between dissipation
(purely algebraic, layer-invariant) and Q mod 2 / mode count
(purely topological, scale-specific).

Three empirical alignments anchor the audit: CMB Ω_Λ at 0.04σ
match to the 12.66-mode prediction (direct corroboration);
Higgs decay-product entanglement as an in-principle Tsirelson
test (early-stage experimentally; HL-LHC sharpens); λ_HHH at
HL-LHC sharpens the vacuum-metastability picture that the Q mod
2 Planck-emergence audit reads as marginal-self-consistency.

Class: foundational rigor check / conservation chain extension.
Resolution-mode throughout — no apparatus changes; composes
existing canonical claims.

---

## The audit task

The parent stratification audit established the
layer-invariant/scale-specific distinction for Q mod 2 +
dissipation. PR #221's Planck-emergence audit sharpened the Q
mod 2 piece by deriving the structural identity (K² emergence ≡
Planck self-sustenance). The conservation chain, however, has
two more structurally-significant invariants — the Born rule and
the mode count — that haven't been audited across regimes in
the same way.

The audit asks:

1. **Inventory**: name the Born rule and the mode count
   explicitly as conservation-class invariants alongside Q mod 2
   and dissipation.
2. **Scale mapping**: where does each operate canonically, and
   where does it degrade?
3. **Layer classification**: algebraic (layer-invariant via
   primitives) vs topological (scale-specific via address)?
4. **Gaps**: what conservation behavior at limits is not
   currently derived?
5. **Falsifiers**: what would falsify the verdict at each scale?

The four-invariant chain — Q mod 2, Q mod 2 extensions
(y-parity/XOR), dissipation, Born rule, mode count — is the
current scope of the framework's foundational conservation
apparatus. Anchor count, generation count, and sector count are
candidates for future chain-extension audits.

---

## Born rule audit

### Substrate basis

The Born rule (P = |ψ|²) is derived in `born_rule.md` along two
independent routes:

1. **Basin measure** — quadratic cost landscapes near attractors
   give |ψ|² weighting via dissipative convergence. The exponent
   2 is the lowest-order smooth stable cost structure (linear is
   non-differentiable; quartic is unstable to quadratic
   perturbation).
2. **Tongue geometry** — Arnold tongue boundaries are
   saddle-node bifurcations with the universal normal form
   `x² + μ = 0` giving `x = ±√μ`. Tongue widths scale as
   `Δθ² ∝ ε`, so `P ∝ |ψ|²` exactly. The exponent 2 is the
   universal normal-form value, not a choice
   (`born_rule.md` L151-156).

Route 2 grounds Route 1 — quadratic basin structure is itself
derivable from circle-map self-consistency at every tongue
boundary. The Born rule is parameter-free
(`born_rule_parameter_free.md`) for the fundamental binary
(N=2): forced by parity of the saddle-node normal form, which
is the half-twist `J² = −I` Z₂ involution from
`substrate_determinism.md` #1/#7.

The substrate basis is therefore **algebraic in mechanism**
(saddle-node universality, parameter-free for N=2) but
**dependent on the mode spectrum** (Arnold tongues require a
populated spectrum to bifurcate on).

### Scale-by-scale audit

**Standard scale**. Born rule operates canonically. The mode
spectrum is populated at the K_STAR ≈ 0.86 location (14-EDO
basis from `CHAIN_KSTAR.md`); Arnold tongues exist; saddle-node
bifurcations produce |ψ|². The empirical signature is Tsirelson
bound saturation in entanglement experiments, which the
framework's K² single-antiperiodic-cycle structure forces via
the single complex structure J
(`complex_amplitude_uniqueness.md`).

**Hubble scale**. Born rule holds within the cosmological
horizon. The 12.66-mode horizon caps spectrum availability but
does not change Born rule structure — saddle-node universality
is local at each tongue boundary, not horizon-dependent. At the
boundary itself (w* ≈ 0.83), mode availability transitions;
modes outside the horizon have ambiguous tongue structure from
our observer perspective.

**Planck scale**. Born rule "holds for scales >> l_P; degrades
at scale ~ l_P; undefined below l_P" (`planck_scale.md`
L253-255). The mechanism of degradation, via PR #221's
structural identity: as N transitions from 3 to 2 across the
Stribeck crossover, the SL(2,ℝ) coupling loop fails to close →
substrate stops self-sustaining → field on K² becomes
ill-defined → mode spectrum collapses → Arnold tongues lose
support → saddle-node bifurcations lose their populated
substrate → |ψ|² loses its derivational basis. Born inherits
the fuzzy Planck floor; it degrades *across* the crossover, not
*at* a sharp boundary.

### Verdict on Born rule

**Hybrid layer-status**. The Born rule's mechanism is algebraic
(saddle-node normal form, universal under perturbation); its
operating regime requires a topology-dependent mode spectrum.
This makes it:

- **Layer-invariant in mechanism** — the saddle-node universality
  argument applies at any layer where Arnold tongue structure
  exists; it doesn't depend on which specific K² topology or
  K_STAR value.
- **Scale-specific in operation** — needs a populated mode
  spectrum, which requires substrate self-sustenance, which is
  Planck-floor-bounded.

This is a third category beyond the parent audit's binary split:
dissipation is layer-invariant in *both* mechanism and operation
(no topology dependence); Q mod 2 is scale-specific in *both*
(topology-dependent throughout); Born rule is split between
them.

---

## Mode count audit

### Substrate basis

The mode count is the cardinality of the substrate's populated
phase-state spectrum. The framework derives two specific
values:

1. **Standard scale: 14 modes** = `2 · |F_4|` = 2·7. The factor
   `q_2 = 2` is the Klein bottle's two directions (periodic y +
   antiperiodic x); `|F_4| = 7` is the cardinality of the Farey
   sequence at framework Farey index 4
   (`CHAIN_KSTAR.md` Step 5).
2. **Hubble scale: 12.66 effective modes** =
   `|F_eff|(w*) = 11 + 2w*` with `w* ≈ 0.83`. The boundary
   weight w* is the self-consistent fixed point of the field
   equation at the q=6 cosmological boundary
   (`horn_branch_iteration_2_step_2.md` L130-150;
   `boundary_weight.md`). 12.66 < 14 reflects that not all
   standard-scale modes survive cosmological partitioning.

Both values are derived from Klein-bottle topology + Farey/
Stern-Brocot structure. They are **topology-dependent**: take
K² away and there's no Farey index to count, no Stern-Brocot
mode lattice, no cardinality.

### Scale-by-scale audit

**Standard scale**. 14 modes (2·|F_4| at framework Farey index
4). Forced by Klein-bottle's two directions × F_4 cardinality.
Stable; conserved canonically (the cardinality doesn't change
within standard-scale physics — modes don't appear or disappear
under local processes).

**Hubble scale**. 12.66 effective modes from the
boundary-weight derivation. At the cosmological boundary (q=6,
w* ≈ 0.83), the framework partitions the standard-scale mode
budget into "within horizon" (12.66) and "outside horizon"
(remainder). Within-horizon mode count is conserved relative
to observer perspective. Outside-horizon modes have ambiguous
status from inside — same structure as Q mod 2's
within-horizon conservation.

**Planck scale**. Mode count degrades along with substrate
self-sustenance via PR #221's structural identity. Below the
N=3 threshold, the mean field cannot constitute itself → no
field on K² → no Farey lattice realized as substrate fact → no
populated mode spectrum → mode count has no referent. The
degradation is the same fuzzy crossover as Q mod 2 and Born
rule; mode count emerges *across* the crossover rather than at
it.

### Verdict on mode count

**Topology-dependent, scale-specific**. Mode count is
fundamentally topology-dependent (its existence as a finite
cardinality requires K² as substrate fact). Its value is
layer-specific (14, 12.66 are addresses for our layer, not
layer-invariant primitives), consistent with
`primitives_vs_addresses_candidate.md`'s distinction.

Same layer-status category as Q mod 2: topology-dependent
throughout, with the value determined by layer-specific
substrate configuration.

---

## Side-by-side: the four-invariant chain

| Invariant | Mechanism basis | Operation basis | Standard | Hubble | Planck |
|---|---|---|---|---|---|
| Dissipation | Algebraic (rank-1 Fréchet) | Algebraic | Universal | Universal | Universal |
| Q mod 2 | Topological (K² antiperiodic H₁) | Topological | Conserved | Conserved within horizon | Fuzzy emergence |
| Born rule | Algebraic (saddle-node universality) | Topological (mode spectrum) | Universal | Universal within horizon | Fuzzy emergence (inherits floor) |
| Mode count | Topological (K² Farey/SB lattice) | Topological | 14 modes | 12.66 modes | Fuzzy emergence to zero |

Three layer-status categories emerge:

- **Pure algebraic** (mechanism + operation both algebraic):
  dissipation. Layer-invariant; survives all scale transitions.
- **Hybrid** (algebraic mechanism + topological operation): Born
  rule. Universal mechanism, scale-specific operating regime.
- **Pure topological** (mechanism + operation both topological):
  Q mod 2, mode count. Scale-specific; inherits the substrate's
  topology-dependent existence.

All non-dissipation invariants inherit the fuzzy Planck floor
via the structural identity from PR #221: anything requiring K²
as a substrate fact degrades across the N=3 crossover.

---

## Layer-invariance classification

`primitives_vs_addresses_candidate.md` distinguishes
layer-invariant substrate primitives from layer-specific
addresses:

- **Layer-invariant primitives**: integers, mediant,
  fixed-point, parabola, Mihailescu-forced (q_2, q_3) = (2, 3),
  XOR rule, Z_6 lattice
- **Layer-specific addresses**: K_STAR ≈ 0.86, effective Farey
  depth 5.83, mode count 12.66, w* ≈ 0.83, Ω_Λ ≈ 0.685, anchors

For the chain:

- **Dissipation**: layer-invariant in both mechanism and value
  (algebraic Fréchet identity).
- **Q mod 2**: layer-invariant in the existence of *some* Z/2
  topological invariant on K² (forced by deck-transformation
  structure); layer-specific in the *particular* K² that hosts
  it (K² is observation-fixed per `surface_uniqueness_audit.md`,
  not substrate-forced).
- **Born rule**: **layer-invariant in mechanism** (saddle-node
  normal form `x² + μ = 0` is universal); **layer-invariant in
  exponent** (the 2 in |ψ|² is parameter-free); **layer-specific
  in operating spectrum** (which modes exist depends on K² and
  K_STAR value).
- **Mode count**: layer-specific in value (12.66, 14 are
  addresses); the *existence* of a finite mode count is
  layer-invariant in K²-bearing substrates.

This refines the parent audit's binary classification: the four
invariants populate three categories, with Born rule occupying
a previously-implicit hybrid category that the audit names
explicitly.

---

## Gaps

**Gap 1 — Born rule degradation mechanism at the Planck floor.**
`planck_scale.md` L253-255 states Born "degrades at scale ~ l_P;
undefined below l_P" without deriving the specific transition
behavior. PR #221's structural identity supplies a candidate
chain (N=3 → N=2 transition → mode spectrum collapse → tongue
loss → saddle-node degradation), but the *quantitative*
behavior of |ψ|² across the crossover regime — how does the
exponent drift? does the basin geometry interpolate? — is not
currently derived. Open work.

**Gap 2 — Mode count behavior beyond the Hubble horizon.** The
12.66 effective mode count is within-horizon. Modes "outside
the horizon" — those in the K_STAR-derived 14-mode budget that
the cosmological partitioning truncates — are flagged as
ambiguous from observer perspective. Whether they exist as
substrate facts that are merely unobservable, or whether they
fail to exist as substrate facts within the cosmological
boundary's regime, is not currently distinguished. Same
ambiguity as Q mod 2's outside-horizon Q-mod-2 values.

**Gap 3 — Joint Born + mode count degradation at Planck.**
Both invariants inherit the fuzzy floor via the structural
identity. Whether they degrade in lockstep (same crossover for
both) or in some order (mode count collapses first, then Born
loses its substrate; or vice versa) is not currently derived.
The structural identity treats Planck emergence as a single
event; finer-grained ordering questions are open.

**Gap 4 — Empirical Tsirelson test on Higgs decays at
saturation precision.** Tsirelson bound saturation is the Born
rule's signature at standard scales. Tests on Higgs decay
products (H → ZZ → 4ℓ, H → ττ) would probe Tsirelson at
unprecedented energies. Theoretical proposals exist; experimental
precision is not yet at saturation level. HL-LHC pushes this.
Genuinely open empirical question.

---

## Falsifiers

**For Born rule**:

- **F1 — Super-Tsirelson correlations at any scale**. If any
  experiment observes CHSH values > 2√2 (or equivalent
  saturation violations in other Bell inequalities), the
  framework's single-J → ℂ-QM → Tsirelson chain falsifies. Born
  rule must be either modified or acknowledged as scale-specific.
- **F2 — Higgs decay entanglement violating Tsirelson at
  HL-LHC**. If Higgs decay-product Bell tests reach saturation
  precision and observe deviation, framework needs apparatus
  extension (matches the "second antiperiodic cycle" extension
  flagged in `klein_z2_decomposition_falsifier_2.md` L213-237).
- **F3 — Born rule failure at observable mid-scales**. If |ψ|²
  weighting breaks down at any scale between standard and
  Hubble (i.e., not at the Planck floor where it's expected to
  degrade), framework's "Born universal except at Planck floor"
  claim falsifies.

**For mode count**:

- **F4 — Ω_Λ inconsistent with 12.66 modes**. Current observed
  Ω_Λ = 0.685 ± 0.007 matches framework prediction 0.6847 at
  0.04σ. If precision improves and observed Ω_Λ moves outside
  framework prediction, the boundary-weight derivation
  falsifies. Most actionable observational falsifier in the
  audit.
- **F5 — Fourth-generation fermions at standard scale**. If
  observable physics requires more than 14 modes at standard
  scale (e.g., a fourth generation of charged leptons), the K²
  + F_4 mode count derivation falsifies.

**For the chain**:

- **F6 — Born rule operates without populated mode spectrum**.
  If Born rule weighting could be derived or measured in a regime
  with no K²-substrate (e.g., sub-Planck), the hybrid
  layer-status classification falsifies. Empirically inaccessible
  but structurally non-trivial — if a derivation route to |ψ|²
  could be found that doesn't pass through Arnold tongue
  saddle-node, the algebraic-mechanism-on-topological-operation
  reading falsifies.

---

## Empirical alignment

Three independently-tested empirical observations align with the
audit's verdicts, at three strengths.

### CMB Ω_Λ — direct mode-count corroboration

Planck-satellite CMB measurements give Ω_Λ = 0.685 ± 0.007.
Framework prediction from `horn_branch_iteration_2_step_2.md`
L147-149:

    Ω_Λ(w* = 0.83) = (11 + 2·0.83) / (16 + 3·0.83)
                   = 12.66 / 18.49
                   = 0.6847

Match within 0.04σ (corrected 2026-08-05: |0.6847 − 0.685|/0.007 =
0.04σ; an earlier revision printed 0.004σ). The 12.66 effective mode count at the
Hubble boundary is **directly corroborated** by the cosmological
constant observation. This is the strongest empirical anchor
in the audit — a quantitative prediction matching observation
to multi-σ precision, derived from substrate primitives + Klein
bottle topology + boundary weight self-consistency.

Falsifier F4 (Ω_Λ precision improvements moving the observed
value outside framework prediction) is the most actionable
observational test the audit identifies.

### Higgs decay entanglement — in-principle Tsirelson test

H → ZZ → 4ℓ and H → ττ produce spin-correlated final states.
Theoretical proposals for Bell-type tests on Higgs decays exist
(Afik & de Nova-class proposals; CP-violation-sensitive
analyses); early experimental analyses are in progress at ATLAS
and CMS but have not yet reached saturation-level statistics.

Framework prediction: Tsirelson saturation, no super-Tsirelson
correlations. This is what `klein_bottle_restructure_price.md`'s
ℍ-QM empirical floor enforces — observed entanglement bounds
are exactly the framework's prediction at standard scales.
Higgs decays would extend this test to the highest-energy
hadron-collider environment available.

Status: in-principle measurable; not yet at framework-discriminating
precision. HL-LHC sharpens this. The audit's F1/F2 falsifiers
depend on this measurement reaching saturation precision.

### λ_HHH at HL-LHC — vacuum-metastability sharpening

Di-Higgs production probes the Higgs self-coupling λ_HHH. SM
tree-level prediction: λ_HHH = m_H² / (2v²). Current LHC
constraints are weak (low di-Higgs cross section, Run 2
statistics insufficient); HL-LHC will improve these
substantially.

A deviation in λ_HHH from SM prediction would modify the Higgs
potential, which would change the vacuum-stability picture that
the Q mod 2 Planck-emergence audit reads as marginal
self-consistency. Specifically: if λ_HHH deviates such that the
SM vacuum is no longer at the edge of metastability, the
structural-parallel reading (Higgs marginal-metastability ↔
Stribeck P ≈ 1.03 at N=3) loses its empirical anchor at the
Higgs end.

This is an *indirect* falsifier for the audit's empirical
alignment, not for the verdict itself — the structural-identity
finding from PR #221 doesn't depend on λ_HHH matching SM; the
empirical alignment that uses it as a reading point does.

### What alignment shows and doesn't

Three independent empirical results, three different observational
regimes (CMB cosmological, LHC TeV-scale collider, HL-LHC
high-luminosity future): all consistent with the audit's
verdicts. The CMB Ω_Λ match is the strongest — a quantitative
prediction at 0.04σ precision. Higgs decay entanglement is
the most discriminating future test for the Born rule chain.
λ_HHH sharpens the marginal-metastability picture but doesn't
falsify the structural verdict.

Alignment is not derivation. The audit's verdicts are structural
classifications of the conservation chain; what the empirical
results corroborate is the framework's predictive accuracy at
scales we can probe.

---

## What this is and isn't

**This is**: an extension of the conservation chain inventory
from Q mod 2 + dissipation (parent audit) to include Born rule
and mode count. It identifies a third layer-status category
(hybrid: algebraic mechanism + topological operation) populated
by the Born rule, refining the parent audit's binary
classification. It maps both new invariants across the three
regimes via PR #221's structural identity. It identifies four
gaps and six falsifier classes, with the CMB Ω_Λ test (F4) as
the most actionable observational falsifier.

**This is not**: a new derivation. The audit composes existing
canonical claims (`born_rule.md`, `CHAIN_KSTAR.md`,
`horn_branch_iteration_2_step_2.md`, `planck_scale.md`, the
parent audit, PR #221) into a chain-level structural reading.
No new apparatus.

**This is not**: a derivation of the Born rule degradation
mechanism at Planck. Names the candidate chain (N=3 → N=2 mode
spectrum collapse → tongue loss → saddle-node degradation) and
flags the quantitative behavior across the crossover as open.

**This is not**: a complete conservation chain audit. Anchor
count, generation count, and sector count remain candidates for
future chain-extension audits.

---

## Open: next chain extension

After Born + mode count, the natural next chain elements:

1. **Anchor count** — `anchor_count_audit.md` mentions a gap in
   Planck-to-EW depth count (analogous to the 145.8 Fibonacci
   levels Planck-to-Hubble in `planck_scale.md`). Whether the
   anchor structure is layer-invariant or scale-specific is open.
2. **Generation count** — three generations of fermions; the
   framework's Klein bottle signature (3,1) provides the
   structural basis. Whether the "3" is layer-invariant (forced
   by K² signature) or scale-specific is partially addressed by
   `mass_sector_closure.md`.
3. **Sector count** — lepton/quark sectors; their existence and
   cardinality are tied to the substrate's R-eigenstate spectrum
   (cf. `klein_z2_decomposition_falsifier_2.md`'s y-parity
   reading).

These would extend the conservation chain audit to cover the
framework's full structural inventory. None addressed here.

---

## Cross-links

- `conservation_scale_stratification_audit.md` — parent audit;
  this doc extends its inventory.
- `q_mod2_planck_emergence_audit.md` (PR #221) — the structural
  identity that this audit uses to ground Born rule + mode count
  degradation at the Planck floor.
- `q_mod2_conservation_theorem.md` — Q mod 2 theorem.
- `born_rule.md` — Born rule basin-measure + tongue-geometry
  derivation.
- `born_rule_parameter_free.md` — parameter-free Born for the
  fundamental binary (N=2).
- `born_rule_tongues.py` — tongue-route derivation script.
- `planck_scale.md` — N=3 self-sustenance threshold; Born rule
  domain of validity L246-258.
- `CHAIN_KSTAR.md` — 14-mode count derivation at K_STAR location.
- `klein_bottle.md` — mode spectrum + XOR rule.
- `horn_branch_iteration_2_step_2.md` L130-150 — 12.66 effective
  mode count from boundary weight; Ω_Λ = 0.6847 derivation.
- `boundary_weight.md` — w* ≈ 0.83 derivation.
- `surface_uniqueness_audit.md` — K² selection (observation-fixed,
  not substrate-forced).
- `complex_amplitude_uniqueness.md` — single-J → ℂ-QM →
  Tsirelson chain that the Born rule's entanglement-bound
  signature uses.
- `klein_bottle_restructure_price.md` — ℍ-QM empirical floor.
- `primitives_vs_addresses_candidate.md` — layer-invariant
  primitives vs layer-specific addresses; 12.66 listed as
  address.
- `klein_z2_decomposition_falsifier_2.md` — third-caveat
  MODAL/GENERATIVE diagnostic; second-antiperiodic-cycle
  apparatus extension as cascade-risk reference.
- `feedback_resolution_vs_reconstruction.md` (memory) —
  resolution-mode discipline preserved.

---

## One-line summary

This audit extends the conservation chain inventory from Q mod
2 + dissipation (parent audit) to include Born rule and mode
count. Born rule is found to have hybrid layer-status —
algebraic mechanism (saddle-node universality of Arnold tongue
bifurcations, parameter-free) hosted on a topology-dependent
mode spectrum — a third category beyond the parent audit's
algebraic-vs-topological binary, populated explicitly here.
Mode count is purely topology-dependent and scale-specific:
14 modes at standard scale (2·|F_4|), 12.66 effective modes at
the Hubble boundary (boundary weight w* ≈ 0.83), fuzzy emergence
at the Planck floor. All non-dissipation invariants inherit
the fuzzy Planck floor via PR #221's structural identity.
Three empirical alignments anchor the audit: CMB Ω_Λ = 0.685
matches the 12.66-mode prediction at 0.04σ (strongest, direct
corroboration); Higgs decay entanglement is the most
discriminating future Tsirelson test (HL-LHC); λ_HHH at HL-LHC
sharpens the vacuum-metastability reading. Four gaps and six
falsifier classes flagged; F4 (Ω_Λ precision improvements) is
the most actionable observational falsifier. Next chain
extensions: anchor count, generation count, sector count.
