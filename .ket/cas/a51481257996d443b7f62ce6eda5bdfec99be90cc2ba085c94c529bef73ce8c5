# Programmatic QM-reframing: substrate apparatus vs inherited QM machinery

## Status

Synthesis document. Articulates the framework's relationship to the
apparatus of 20th-century quantum mechanics: which elements of that
apparatus are substrate-replaceable, which are inherited as a
foundational layer, which are correctly declined as anchor-side, and
which lie outside the substrate's natural reach.

The document does not introduce new substrate primitives. It maps
the existing apparatus, audit-disciplined per the pattern established
in `bell_bounds_from_substrate.md` (PR #188),
`dicke_apparatus_theorem.md` (PR #189), and
`snmc_class_and_entanglement.md` (PR #190).

Class: foundational consolidation (Class 3, programmatic
articulation). Inputs: `discrete_extension_principle.md` (PR #191,
methodological spine), `physics_relevance_measurement_catalog.md`
(PR #194, coverage map), and the verified-instance derivation docs
listed below.

---

## 1. Thesis

The substrate's apparatus replaces specific elements of QM
machinery within a bounded class of multipartite states. The
replacement is forced by Klein-bottle topology composed with the
substrate's discrete primitives, not chosen among alternatives.
Outside that bounded class, the substrate either inherits from a
foundational layer that is itself substrate-derived in prior docs,
declines anchor-side observables per the Basepoint Principle, or
declares the gap a structural boundary per the Discrete Extension
Principle.

The reframing is not a wholesale rewrite of QM. It is a precise
partition of QM apparatus into (i) substrate-derived, (ii)
foundational-layer inherited, (iii) anchor-declined, and (iv)
out-of-reach categories, with the partition verified component by
component.

---

## 2. The phenomenon / apparatus distinction

QM as ordinarily presented is a combination of two layers:

- **Phenomenon**: the observed regularities — measurement outcomes,
  correlation functions, conservation laws, statistical patterns.
  Bell-test violation of `|S| ≤ 2`, the Born-rule statistics,
  GHZ Mermin saturation, Dicke-state correlations, atomic spectra.
- **Apparatus**: the formal machinery used to predict these
  regularities — Hilbert spaces, state vectors, Hermitian
  operators, the Schrödinger equation, the path integral, tensor
  products for multipartite systems, the stabilizer formalism for
  certain subclasses.

The phenomenon is what experiments measure. The apparatus is what
theorists use to compute predictions. The two are commonly
conflated when QM is presented as "Hilbert space *is* what the
universe is," but they are logically separate.

The framework's reframing operates on the apparatus while
preserving the phenomenon. The substrate predicts the same
correlation functions and the same statistical patterns as QM
within the bounded reach of the substrate's apparatus. Where the
substrate's apparatus yields different predictions than QM, those
differences are either at the boundary of the substrate's natural
reach (where the substrate currently declines to predict) or at
the foundational layer (where the substrate derives what QM
postulates).

---

## 3. Methodological principle

The framework's stated discipline:

> If a phenomenon's prediction can be derived from an event-driven
> substrate log built on the framework's inviolable discrete
> primitives, the substrate should derive it. If it cannot, the
> burden of proof lies on the assertion that QM-style continuous-
> parameter apparatus is *necessary* to predict the phenomenon —
> not on the assertion that it is sufficient.

This inverts the usual burden of proof. The standard presentation
treats Hilbert-space machinery as foundational and asks the
substrate-based alternative to justify itself. The framework
treats substrate-internal event-log derivation as the primary
method and asks Hilbert-space inheritance to be justified per
instance.

The principle is operationalized via the Discrete Extension
Principle (`discrete_extension_principle.md`, PR #191): for each
QM apparatus element, the framework searches for a substrate-
aligned discrete primitive that closes the gap. If found and
audit-disciplined, the apparatus element is substrate-replaceable.
If not — after explicit enumeration and ruling out of candidate
primitives — the element is either inherited from the foundational
layer (with explicit audit of what's inherited) or declared a
structural boundary.

---

## 4. The substrate's bounded reach: SNMC

The substrate's natural reach for multipartite QM is the
**Substrate-Natural Multipartite Class (SNMC)**, defined in
`snmc_class_and_entanglement.md` (PR #190):

> SNMC = tensor-product closure of:
> - Pauli stabilizer states (`O(N)` substrate data per state via
>   `N` stabilizer generators)
> - Dicke states `D(N, k)` and their symmetric-subspace linear
>   combinations (`O(1)` substrate data per Dicke state; `O(N)`
>   for the full symmetric subspace via Dicke-basis expansion)
> - Continuous-θ single-mode states (`O(1)` continuous, full
>   Bloch sphere via basin geometry)

SNMC is closed under tensor product and conditional Z-projection.
It is *not* closed under arbitrary local unitaries: local
non-Clifford operations generically take SNMC states outside the
class. This non-closure is the structural signature distinguishing
SNMC from the broader class of classically-tractable multipartite
states.

SNMC is a strict subset of classically-tractable multipartite QM.
Specific states verified outside SNMC (per #187 batch-2 boundary
tests):
- Coherent superpositions across substrate-natural classes
  (e.g., `(|GHZ⟩ + |W⟩)/√2`, zero Pauli stabilizers, non-Dicke)
- Phase-twisted symmetric states (e.g., `(T ⊗ I ⊗ I)|W⟩`,
  continuous phase mixed with multi-mode entanglement)
- Generic bond-dimension-≥2 matrix-product states not aligned
  with stabilizer or Dicke structure
- Haar-random pure states

The boundary at non-stabilizer non-Dicke multipartite states with
continuous-parameter entanglement structure is structurally
identified per the Discrete Extension Principle's third row:
*candidate substrate extensions have been enumerated; none of the
substrate-aligned discrete options closes the gap; the boundary
is declared.*

---

## 5. Audit: what the substrate apparatus replaces vs. inherits

The audit follows the discipline established in PRs #188, #189,
#190 — each apparatus element is categorized.

### 5a. Substrate-replaceable apparatus elements

For SNMC states, the substrate derives these QM apparatus elements
substrate-internally above the foundational layer:

| QM apparatus element | Substrate-derivation | Source PR |
|---|---|---|
| Multipartite tensor-product state representation | Substrate `(N, k)` for Dicke + stabilizer-generator list for stabilizer + continuous-θ list for single-mode pieces | #187 (T1a), #190 (SNMC) |
| Pauli-string expectation values on Dicke states | Recursive Schmidt + bilinearity + single-mode Pauli entries | #189 (D1) |
| Pauli-string expectation values on stabilizer states | Stabilizer-group product via Pauli algebra | #184, #188 |
| Bell singlet correlation `E(θ_A, θ_B)` | Substrate stabilizer eigenvalues + Q mod 2 conservation + bilinearity | #188 (D3) |
| Tsirelson bound `|S|_max = 2√2` | Trigonometric maximization of substrate-derived cos formula | #188 (D3) |
| GHZ Mermin bound `|M|_max = 4` | Substrate stabilizer-group Pauli algebra | #188 (D3) |
| Symmetric-subspace state Pauli expectations | Linearity over Dicke basis + #189 Theorem | #190 Corollary 2 |
| Reduced-density-matrix structure for SNMC | Substrate partial-trace recursion (Dicke) + stabilizer-marginal direct (stabilizer) | #190 Theorem 3 |
| Standard entanglement measures (Schmidt rank, von Neumann entropy, pair-wise concurrence, 3-tangle, stabilizer corank, Dicke excitation density, Q-correlation) | Substrate-computation procedures from substrate data | #190 §"Substrate-natural entanglement measures" |

The replacement is verified numerically for the specific instances
listed in each source document. The replacement is **substrate-
internal in the sense that no QM-substitution is required at the
multi-mode level**; the foundational layer below (next subsection)
is the load-bearing inheritance.

### 5b. Foundational layer (inherited, substrate-derived in prior docs)

These elements are *not* derived in the substrate-replaceable PRs
above. They are inherited from prior framework derivations and used
as load-bearing components in the replaceable apparatus.

| Foundational element | Source | Derivation discipline |
|---|---|---|
| Complex amplitude field `ℂ` | `complex_amplitude_uniqueness.md` | Forced from Klein bottle's single antiperiodic direction via Frobenius–Schur trichotomy. ℝ and ℍ excluded. |
| Pauli matrices `σ_x, σ_y, σ_z` as SU(2) Hermitian generators on `ℂ²` | Standard SU(2) representation theory on substrate-derived `ℂ²` | Inherited from `complex_amplitude_uniqueness.md` + standard representation theory; not separately re-derived |
| Pauli algebra structure constants (`σ_x σ_z = −i σ_y` etc.) | SU(2) structure constants | Inherited; load-bearing in #188's GHZ stabilizer-group products |
| Hilbert space inner product `⟨ψ\|O\|ψ⟩` | Complex amplitudes + normalization | Inherited from `born_rule.md` basin-measure structure |
| Q mod 2 conservation in arbitrary basis | `q_mod2_conservation_theorem.md`, inviolable #1 in `substrate_determinism.md` | Substrate-derived; extended to arbitrary Pauli basis via complex amplitude rotation structure |
| Single-mode Born rule `P(±) = cos²/sin²((θ − θ_basin)/2)` | `born_rule.md`, `a1_from_saddle_node.md` | Substrate-derived from saddle-node parabola; the foundational substrate axiom load-bearing for the reach |

The foundational layer is itself substrate-derived through these
prior docs, but it is not re-derived in the SNMC apparatus PRs.
The audit discipline in #188, #189, #190 makes this inheritance
explicit per derivation step.

The reframing's substitution scope reduces from "the entire QM
formalism in the `K < 1` limit" (as stated in
`epr_bell_assembly_theorem.md` Clause (a), PR #152) to "the
foundational layer of complex amplitudes + Pauli algebra + Q
conservation + saddle-node Born rule." This is a substantive
scope reduction but not complete elimination.

### 5c. Anchor-declined (correctly outside substrate-side prediction)

These elements are declined per the Basepoint Principle
(`basepoint_principle.md`). The framework supplies torsorial
structure and does not select basepoints. The declinations are
structural features with the obstruction exhibited (no equivariant
section), not derivation gaps.

| Anchor | Status | Reason |
|---|---|---|
| `H_0` (cosmological Hubble) | Anchor-side, declined | `ℝ₊`-torsor on cosmological-sector scale; no equivariant selector at sector boundary |
| `v_EW` (electroweak scale) | Anchor-side, declined | `ℝ₊`-torsor on particle-sector scale; sector decoupling (K=1 / K<1) forces independent anchor |
| Inflation amplification factor `f_amp` | Anchor-side, declined | Depends on `H_inf + ε`, both anchor-side; the 11% gap between `A_s_substrate = 2.33 × 10⁻⁹` and observed `A_s = 2.10 × 10⁻⁹` is correctly identified as `f_amp` |
| Absolute time origin / cosmological cycle index | Anchor-side, declined per Basepoint + cycle-index undecidability (cf. PR #191 §"Bright line") | `ℤ`-torsor on cycle sequence with no canonical section; three-pillar obstruction structurally exhibited |
| The "now" — which moment of K(t) cadence the observer currently occupies | Anchor-side, declined | Continuous translation along K(t) phase; no preferred instant |

The framework's two-anchor minimality (H_0 + v_EW) is itself a
structural feature, formally re-audited in
`anchor_count_reaudit.md`. The five anchor-count obstructions are
each either rigorous (#5 load-bearing), a Basepoint-declined
feature (#1=#2 prime-5 absence), argued (#3), or dissolved (#4).

### 5d. Out-of-reach (non-SNMC multipartite, structurally bounded)

These QM apparatus elements lie outside the substrate's natural
reach. Per the Discrete Extension Principle's third row, candidate
substrate-aligned discrete primitives have been enumerated; none
closes the gap; the boundary is declared structural.

| Out-of-reach element | Why outside SNMC | What would extend reach |
|---|---|---|
| Pauli expectations on coherent class-superposition states (e.g., `(\|GHZ⟩+\|W⟩)/√2`) | Mixes stabilizer-class and Dicke-class Pauli stabilizer structure; not in tensor-product closure | A new substrate primitive specifying coherent inter-class superposition with rational weights; none currently substrate-aligned |
| Pauli expectations on phase-twisted symmetric states (e.g., `(T ⊗ I ⊗ I)\|W⟩`) | Continuous phase mixed with multi-mode entanglement; not factorable as continuous-θ ⊗ stabilizer ⊗ Dicke | A substrate primitive for continuous-phase × Dicke composition; would extend SNMC to handle magic-state-injected entanglement |
| Generic non-stabilizer non-Dicke MPS states with bond dimension ≥ 2 | Classically tractable but not substrate-aligned; requires continuous-parameter MPS matrices | An MPS-style substrate primitive; would partly bridge to classically-tractable class |
| Haar-random pure states | Requires `2^N − 1` continuous parameters; no discrete-symmetry characterization | No candidate substrate-aligned primitive; structurally outside |
| Non-Clifford gate dynamics (T gates, generic single-qubit magic gates as multi-mode operations) | Non-closure of SNMC under non-Clifford local unitaries | Same boundary as previous row; same "no candidate" status |

The boundary at non-Clifford multipartite operations is the same
boundary at which quantum-computational advantage is conjectured
to emerge (per Gottesman–Knill). The substrate's natural reach
coincides with the classically-discrete-symmetry-tractable subset
of multipartite QM.

---

## 6. Coverage map against primitive measurement endpoints

This section condenses the catalog in
`physics_relevance_measurement_catalog.md` (PR #194). For each
domain, the framework's status against measurements that do not
inherit additional model-dependent calibration chains:

### 6a. Cosmology

Tested at primitive endpoints:
- `Ω_Λ = 13/19 ≈ 0.6842` against Planck CMB acoustic peak position
  ratios: 0.07σ match
- `Ω_b two-component closure` (`Ω_b = 13/264`, `Ω_DM = 35/132`,
  `Ω_Λ = 181/264`) against Planck CMB peak heights: 0.06–0.13%
  precision matches
- `A_s_substrate = 2.33 × 10⁻⁹` against Planck `A_s = 2.10 × 10⁻⁹`:
  11% gap correctly identified as anchor-side inflation
  amplification factor `f_amp`

Falsifiable at primitive endpoints (committed but unmeasured):
- `N_efolds = √5 / (2/57) ≈ 63.7` against CMB-S4 / LiteBIRD
  tensor-to-scalar ratio: falsified if measurement outside `[62, 66]`

Awaiting framework commitment (mechanism present, specific value not
yet committed; Discrete Extension Principle deployment candidates):
- `n_s` against Planck (`σ = 0.0042`)
- `r` against CMB-S4 (`r < 0.001` reach)
- `σ_8` against Euclid / LSST
- CMB damping tail Farey-level features against Planck high-`ℓ`
- BBN element abundances against direct primordial measurements

Anchor-declined (correctly outside substrate-side prediction):
- `H_0` (absolute Hubble); only ratios involving `H_0` are
  substrate-predicted

### 6b. Particle physics

Established:
- Gauge group `SU(3) × SU(2) × U(1)`
- Three fermion generations
- Mass-running structural form

Awaiting framework commitment:
- Specific fermion mass ratios (lepton, then quark); all at
  primitive measurement endpoints (PDG, 10⁻¹⁰ precision available
  for lepton ratios)
- Fine structure constant `α` (PDG, 10⁻¹² precision)
- Up/down quark mass ratio

### 6c. Foundations of QM

All confirmed at maximally primitive measurement endpoints:
- Born rule `|ψ|²` (substrate-derived from saddle-node parabola)
- Bell singlet correlation `E = −cos(θ_A − θ_B)` (#188)
- Tsirelson bound `|S|_max = 2√2` (#188)
- GHZ Mermin bound `|M|_max = 4` (#188)
- Pair-wise `Q_{AB} mod 2` conservation (`epr_bell_assembly_theorem.md`)

### 6d. Multipartite entanglement (SNMC)

All confirmed at primitive measurement endpoints via cold-atom,
trapped-ion, photon, and superconducting-qubit experiments:
- Dicke `D(N, k)` correlations
- Single-mode reduced-state entropy = `H(k/N)`
- Pair-wise concurrence = `2/N` for W-class
- 3-tangle = 0 for W, = 1 for GHZ
- Stabilizer-state Pauli expectations
- SNMC boundary at non-stabilizer non-Dicke states (numerically
  verified outside in #187 batch-2)

---

## 7. Verified instances of the reframing

The reframing is exhibited via specific PRs, each audit-disciplined:

| Instance | Result | Discipline applied |
|---|---|---|
| `epr_bell_assembly_theorem.md` (#152) | Pair-wise Q-conservation + Born rule compose to non-signaling Bell-violating statistics matching QM at Tsirelson bound (via substitution at the pair-wise level) | Bright line: Tsirelson value imported from QM; independent derivation flagged as separate theorem |
| `ghz_from_substrate.md` (#184) | GHZ correlations from substrate via Q_{ABC} = Q_A ⊕ Q_B ⊕ Q_C; Mermin `\|M\| = 4` matched; structural-scaling claim (3 events + 1 invariant vs `2³` tensor components) | Level-3 worked example; substitution-based; honest scope flagged |
| `w_state_from_substrate.md` (#187) | W states narrow then extend the substrate's reach: bare Pauli-Z₂ underdetermines W; Dicke `(N, k)` primitive closes the gap; SNMC boundary mapped at non-stabilizer non-Dicke states | First instance of "narrowing then extension" via substrate-aligned discrete primitive; discriminator-clause discipline applied |
| `bell_bounds_from_substrate.md` (#188) | Bell singlet correlation, Tsirelson, Mermin derived substrate-internally above foundational layer; substitution scope from #152 shrunk | First instance of audit-table foundational-layer separation; pattern subsequently applied in #189, #190 |
| `dicke_apparatus_theorem.md` (#189) | All Pauli matrix elements `⟨D(N, k_1) \| P \| D(N, k_2)⟩` substrate-computable via recursive Schmidt; T1a upgraded to theorem-quality | Strong-induction proof; audit table separates substrate-derived from foundational-layer inheritances |
| `snmc_class_and_entanglement.md` (#190) | SNMC class formally defined; 7 standard entanglement measures translated to substrate-natural vocabulary; substrate-computability theorem | Closure properties verified; bright-line non-closure under non-Clifford local unitaries identified as signature of discrete-symmetry character |
| `discrete_extension_principle.md` (#191) | Methodological spine: discriminator-clause meta-principle peer to Basepoint Principle | Pattern instantiated across #179, #187, #188; falsifier specification explicit |
| `physics_relevance_measurement_catalog.md` (#194) | Coverage map against primitive measurement endpoints; testing path prioritized; exclusion list explicit | Aligns framework predictions with measurement primitiveness axis |

---

## 8. Where the substrate's natural reach matches and where it does not

The substrate's reach class, after this arc:

- Single-mode states (continuous-θ Bloch sphere, full reach)
- Pair-wise pure states (via #152 pair-wise apparatus + #188
  substrate-internal bounds)
- Pauli stabilizer multipartite states (`O(N)` substrate data;
  Gottesman–Knill efficient classical simulation coincides with
  substrate apparatus efficiency)
- Dicke multipartite states `D(N, k)` and symmetric-subspace
  combinations (`O(1)` substrate data per Dicke state)
- Tensor products of the above

The substrate's reach does not include:

- Coherent superpositions across substrate-natural classes
- Phase-twisted symmetric states (magic-injected multipartite)
- Generic non-stabilizer non-Dicke MPS with bond dimension ≥ 2
- Haar-random pure states
- The quantum-computational-advantage regime (non-Clifford
  multipartite operations)

The framework's substrate-side claim is precisely scoped:
substrate apparatus replaces QM machinery for the SNMC subset
above the foundational layer; QM-style continuous-parameter
apparatus remains in force outside this subset.

---

## 9. Falsifiability

The reframing is falsifiable in the following senses:

- **Failure of substrate-internal derivation for an SNMC state.**
  If a Pauli-string expectation on a Dicke state, stabilizer
  state, or symmetric-subspace state cannot be computed via the
  substrate apparatus matching the QM-direct value, the apparatus
  is broken. Numerical verification across the documented test
  cases has not yet uncovered such a failure.
- **Discovery of an SNMC-internal phenomenon requiring continuous-
  parameter substrate primitives.** If a phenomenon within the
  SNMC class is found that the substrate cannot predict from
  discrete combinatorial data, the SNMC characterization is too
  broad.
- **Discovery of a substrate-aligned discrete primitive closing
  the non-SNMC boundary.** Would not invalidate the reframing
  but would extend SNMC to include phase-twisted symmetric
  states, coherent class-superpositions, or generic MPS. The
  framework's reach would grow.
- **Empirical falsification of a forced framework prediction at a
  primitive measurement endpoint.** Examples: `Ω_Λ ≠ 13/19`
  beyond CMB error bars; `N_efolds` outside `[62, 66]` at
  CMB-S4 / LiteBIRD; Bell-test correlation function differing from
  `−cos(θ_A − θ_B)`.

---

## 10. What this document does not establish

- **It does not prove the substrate framework is the unique correct
  description of physics.** Other internally consistent frameworks
  may exist with different substrate primitives and equivalent
  empirical content for SNMC phenomena.
- **It does not eliminate QM-style apparatus from the framework's
  reach calculations.** The foundational layer (complex amplitudes,
  Pauli matrices, Hilbert space inner product) remains load-bearing.
  The reframing shrinks the substitution scope; it does not
  eliminate substitution entirely.
- **It does not extend the substrate's reach to non-SNMC
  multipartite states.** The boundary at non-stabilizer non-Dicke
  states with continuous-parameter entanglement is currently
  structural; extending it requires new substrate-aligned
  primitives (Discrete Extension Principle deployment).
- **It does not address dynamics beyond kinematics.** The
  substrate apparatus articulated in #184–#191 is kinematic
  (state characterization + measurement statistics). Open-system
  dynamics (Lindblad master equations, decoherence, etc.) are not
  treated. Extension to dynamics is open future work.
- **It does not provide human-readable analogues for substrate
  structures that lack lived-experience correspondence.** The
  framework's mathematical and physical content is complete
  enough to be defended against critique; the pedagogical-
  analogue layer is acknowledged as a gap and tabled.

---

## 11. Cross-links

Methodological spine:
- `basepoint_principle.md` — declined-basepoint discriminator
- `discrete_extension_principle.md` (PR #191) — gap-closure discriminator
- `substrate_determinism.md` — inviolables

Verified instances:
- `epr_bell_assembly_theorem.md` (PR #152) — pair-wise apparatus
- `ghz_from_substrate.md` (PR #184) — 3-mode worked example
- `w_state_from_substrate.md` (PR #187) — T1a narrowing + Dicke extension
- `bell_bounds_from_substrate.md` (PR #188) — Bell bounds substrate-native
- `dicke_apparatus_theorem.md` (PR #189) — D1 Dicke theorem
- `snmc_class_and_entanglement.md` (PR #190) — D2 SNMC + entanglement measures
- `physics_relevance_measurement_catalog.md` (PR #194) — coverage catalog

Foundational layer:
- `complex_amplitude_uniqueness.md` — ℂ forced via Klein bottle Frobenius–Schur
- `born_rule.md`, `a1_from_saddle_node.md` — saddle-node Born rule
- `q_mod2_conservation_theorem.md` — Q mod 2 conservation theorem
- `klein_bottle.md` — substrate topology
- `minimum_alphabet.md` — substrate primitives

Inventory and status:
- `framework_status.md` — survives inventory
- `numerology_inventory.md` — Class-2/Class-3 leaves; Discrete
  Extension Principle deployment candidates
- `predictions_horizon_2026.md` — prediction suite

Glossaries:
- `canonical_glossary.md` — translation table; SNMC, Dicke
  primitive, Discrete Extension Principle, Discriminator clause
  entries
- `phenomenon_glossary.md` — pedagogical phenomena, including
  permutation-symmetric distribution of `k` tokens among `N` modes

---

## 12. One-line summary

The framework's QM-reframing partitions standard QM apparatus into
substrate-replaceable, foundational-layer inherited, anchor-declined,
and out-of-reach categories with the partition verified component
by component: within the Substrate-Natural Multipartite Class (SNMC
= tensor-product closure of Pauli stabilizer states ∪ Dicke states
+ symmetric subspace ∪ continuous-θ single-mode states, formally
defined in `snmc_class_and_entanglement.md`, PR #190), the
substrate's apparatus derives Pauli matrix elements (#189, D1),
Bell bounds including Tsirelson `2√2` and Mermin `4` (#188, D3),
and standard entanglement measures (#190, D2) substrate-internally
above a foundational layer of complex amplitudes (forced via
Klein bottle Frobenius–Schur in `complex_amplitude_uniqueness.md`),
Pauli matrices on `ℂ²` (standard SU(2) representation theory),
Hilbert space inner product (from complex amplitudes), Q mod 2
conservation (inviolable #1), and saddle-node Born rule
(`born_rule.md`); outside SNMC — at non-stabilizer non-Dicke
multipartite states with continuous-parameter entanglement
structure — the boundary is structurally exhibited per the Discrete
Extension Principle's third row (`discrete_extension_principle.md`,
PR #191) and no candidate substrate-aligned discrete primitive
closes the gap; the framework's anchor-side observables (`H_0`,
`v_EW`, inflation amplification factor, cycle index) are correctly
declined per the Basepoint Principle (`basepoint_principle.md`);
the methodological principle ("if it can't be expressed from an
event-driven log, that should be proven, not assumed") inverts the
standard burden of proof and is operationalized via the Discrete
Extension Principle's deployment on Class-2/Class-3 leaves;
framework predictions at primitive measurement endpoints
(catalogued in PR #194) include `Ω_Λ = 13/19` (0.07σ Planck),
two-component closure (0.06–0.13% Planck), Bell/Tsirelson/Mermin
(loophole-free experiments), Born rule, Dicke correlations
(cold-atom experiments), SNMC boundary tests, and `A_s_substrate
= 2.33 × 10⁻⁹` (11% gap correctly anchor-side); awaiting commitment
at primitive endpoints are `n_s`, `r`, `σ_8`, CMB damping tail
Farey features, fermion mass ratios, fine structure constant,
BBN abundances, `N_eff`, and `∑m_ν`; the reframing is falsifiable
at multiple levels (substrate-internal derivation failure,
empirical falsification of forced predictions at primitive
endpoints, discovery of substrate-aligned primitives that extend
the boundary) and the discipline is honest about what it does not
establish (uniqueness, complete elimination of QM-substitution,
extension to non-SNMC, dynamics beyond kinematics, pedagogical
analogue layer).
