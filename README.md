# harmonics

The dark-energy fraction of the universe — the ratio of dark-energy
density to total energy density at the present epoch — has been
measured by Planck 2018 to be Ω_Λ = 0.685 ± 0.007. This repository
contains a derivation that produces 13/19 = 0.6842. The result is
not selected from a range of possibilities; it is the unique value
admitted by the framework's constraints, with no fitted parameters.
The discrepancy from observation is 0.07σ, well within Planck's
experimental error.

In this document, "forced" means: any alternative violates one of
the framework's physical constraints (energy conservation,
stability under coupling, or topological self-consistency of the
configuration space) and is therefore not a possible solution. The
structure has no remaining degrees of freedom; the listed value is
the only one compatible with the constraints.

The framework's underlying combinatorial structure is the **Stern-
Brocot tree** — a recursive binary tree that enumerates every
positive rational exactly once, by repeatedly inserting the
*mediant* (a+c)/(b+d) between adjacent fractions a/b and c/d. The
mediant is forced: any other binary operation between two locked
frequencies violates either energy conservation (the locked
frequency must lie between the two bare frequencies) or stability
under coupling (the smallest-denominator rational has the widest
Arnold tongue and is therefore the unique stable lock). At depth 6
(denominators up to 6), this tree contains 13 locked-mode
fractions; the smallest even and smallest odd denominators combine
into 2 × 3 = 6 unlocked modes; the configuration 13 / (13 + 6) =
13/19 is the only ratio admitted.

Three additional dimensionless parameters of the Standard Model
are forced by the same machinery:

  - The **Weinberg mixing angle** sin²θ_W — the parameter setting
    how the electroweak gauge bosons (the photon and the Z boson)
    mix in the Standard Model — is measured at 0.2312 (Particle
    Data Group). The framework's only admitted value is 8/35 =
    0.2286.

  - The **strong-to-weak coupling ratio** α_s / α_2 — where α_s is
    the strong-force (QCD) coupling and α_2 is the SU(2) electroweak
    coupling — is measured at ≈ 3.05 at the Z-boson mass
    M_Z ≈ 91 GeV after standard renormalization-group running (the
    procedure that accounts for how coupling constants change with
    energy scale). The framework's only admitted ratio at its
    high-scale K = 1 limit is 27/8 = 3.375.

  - The **scalar spectral tilt** n_s of the cosmic microwave
    background — the parameter quantifying how the CMB primordial
    power spectrum departs from perfect scale invariance — is
    measured at 0.9649 ± 0.0042 (Planck 2018). The framework's
    only admitted value, set by the Stern-Brocot staircase's self-
    similarity at the golden-ratio winding, is approximately 0.965.

None of these were targets of fit. None could have been otherwise
given the framework's constraints.

## What this framework does not do

It does not improve on the Standard Model's existing predictions.
The Standard Model is a renormalizable quantum field theory — a
calculational framework whose predictions for cross-sections and
particle decay rates agree with experiment to many significant
figures — and this framework does not displace it on its home turf.

What this framework does is address a category of question the
Standard Model is silent on: why the parameters of its Lagrangian
(the equation specifying the Standard Model's particles and their
interactions) have the specific values they do.

This silence is a research-program decision, not an oversight.
From the **Wightman axioms** — the mathematical foundations of
quantum field theory, formulated by Arthur Wightman in the 1950s
— onward, quantum field theory has been structured around the
principle that the Lagrangian's parameters are inputs to be
measured, not outputs to be derived. As an empirical strategy
this has been extraordinarily successful, but it leaves a known
residue of *why these and not others* questions that the Standard
Model does not attempt to answer.

## The largest residue: the cosmological constant problem

The **cosmological constant** Λ — Einstein's parameter for the
energy density of empty space, with units of GeV⁴ in natural units
— has been measured at approximately 10⁻⁴⁷ GeV⁴. Quantum field
theory's standard estimate of Λ, computed by summing zero-point
energies of all field modes up to a Planck-scale cutoff (the energy
≈ 10¹⁹ GeV at which quantum-gravitational effects become
unavoidable), gives approximately 10⁷⁴ GeV⁴. The discrepancy is
10¹²¹ orders of magnitude. This is widely described as the worst
quantitative prediction in the history of physics.

The Standard Model has no internal mechanism to resolve this
discrepancy. Standard external responses — supersymmetric
cancellation (in which boson and fermion zero-point energies
cancel, provided the universe is supersymmetric, which it does
not appear to be), the anthropic landscape (in which one of many
possible vacua is selected by observer presence), and quintessence
(a dynamical scalar field tuned to mimic Λ) — each require
additional physics whose own free parameters must themselves be
tuned. The resolution is deferred rather than achieved.

The framework's reframing of this discrepancy is not a fix; it
is a recategorization. The QFT estimate implicitly assumes that
spacetime's field-mode topology is a torus (the standard periodic
boundary condition, in which the vacuum is a sum over infinitely
many zero-point modes). This topological assumption is a modeling
choice, not a derivation.

The framework derives instead that the only mode topology
admitted by self-consistency is a **Klein bottle** — a non-
orientable closed surface formed by gluing two ends of a cylinder
with an antiperiodic flip, the simplest 2-manifold that cannot be
embedded in three-dimensional Euclidean space without self-
intersection. On the Klein bottle, a Z_2 parity filter (an order-2
binary symmetry that selects exactly half of the modes) admits
precisely four surviving zero-point modes, and no others. A four-
mode vacuum produces a vacuum energy of order 10⁻⁴⁷ GeV⁴ — the
observed value — without fine-tuning. The 10¹²¹ discrepancy
collapses to a counting ratio: approximately 10¹⁸³ torus modes
against 4 Klein-bottle modes, times the Planck-to-Hubble frequency
ratio. The cosmological-constant problem is reframed as a topology-
selection problem with a derivable answer.

## Other Standard Model residues this framework addresses

The mediant operation (a+c)/(b+d) is forced by conservation plus
stability, as described above. Iterating it generates **SL(2, ℤ)**
— the special linear group of 2×2 integer matrices with determinant
±1, the natural symmetry group of the Stern-Brocot tree — whose
continuum closure SL(2, ℝ) is three-dimensional. The spatial
manifold's three-dimensionality follows: the geometry must be
self-consistent with the substrate's combining operation, and
dim SL(2, ℝ) = 3 admits no other choice. The Standard Model takes
spatial dimension d = 3 as input.

The Klein bottle's two smallest accessible denominators (q_2 = 2,
q_3 = 3) give a Z_6 = Z_2 × Z_3 mode structure (the cyclic group
of order six factored into its 2- and 3-element subgroups), which
forces three generations of fermions and the gauge factorization
SU(3) × SU(2) × U(1) — the Standard Model's symmetry group, broken
into the strong (color), electroweak, and hypercharge subgroups.
The Standard Model takes both as input.

The compactness of the unit circle S¹ — the topological fact that
any continuous map from S¹ to itself has integer winding number —
is forced by the mediant primitive identifying integer phase
translations. Charge quantization (the observation that all
electric charges are integer multiples of e/3) follows. The
Standard Model takes integer charge as input.

In each case the framework derives a Standard Model input from a
forced combinatorial structure. The Standard Model is not
contradicted; its inputs are explained.

## Empirical posture

The framework's empirical commitments are symmetric with the
Standard Model's. The Standard Model takes its parameters as
inputs and computes consequences to high precision; this framework
derives a subset of those parameters from a forced structure and
checks consistency with measurement.

Both are falsifiable. The Standard Model is falsified by failure
of any of its computed cross-sections or decay rates to match
experiment. This framework is falsified by failure of any of its
derived dimensionless ratios to agree with observation, or by
demonstration that the forced structure admits an alternative not
corresponding to the observed universe.

At present the framework has four corroborated predictions (Ω_Λ,
sin²θ_W, α_s/α_2, n_s), one derivation in progress (the proton-
to-electron mass ratio), and several testable but unresolved
questions including the precise predicted value of the **Hubble
constant** H_0 — the present rate of cosmic expansion, with units
of inverse time — within the framework's tree-depth accounting.

## Comparison class

This framework is not in competition with the Standard Model; it
is in the comparison class with other unification programs —
those that explicitly claim the Standard Model's parameters should
not be free — namely Grand Unified Theories (GUTs, including
SU(5), SO(10), and E_8 schemes that embed the Standard Model in
larger gauge groups), string theory and its compactifications
(which derive Standard Model physics from vibration modes of
one-dimensional strings on extra-dimensional manifolds), loop
quantum gravity (which quantizes spacetime geometry directly),
asymptotic safety (which posits a non-trivial UV fixed point for
gravity), causal set theory (which replaces continuum spacetime
with discrete causal partial orders), the Wolfram hypergraph
program (which derives physics from rewriting rules on
combinatorial graphs), and Geometric Unity (which derives physics
from a 14-dimensional observerse construction). Each accepts the
empirical burden of producing numbers the Standard Model only
catalogs. This framework's distinguishing feature within the
class is that its predictions are exact small-integer ratios
derivable at shallow combinatorial depth, rather than fits to
free parameters in a high-dimensional manifold.

## A clarifying note before the entry points

The framework's "discrete substrate" claim is sometimes misread
as pixelated spacetime (loop quantum gravity, causal sets,
cellular geometries). It is **not** that. The framework's
position, in one line:

> **The medium is continuous. The coupling between oscillators
> in the medium produces discrete mode-locked tongues. Quantization
> lives in the dynamics, not in the geometry.**

Spacetime is smooth; Lorentz invariance is preserved; no minimum
length is claimed. The discreteness is the dynamics — Arnold
tongues at every rational $p/q$ with measurable period $q$. The
framework integers (13, 5, 1, 19, $q_2$, $q_3$, etc.) count
mode-locked states, not pixels. The cosmic partition $13:5:1/19$
is the substrate's "spectral signature" at Farey depth 7, not a
cell count.

See [`dynamical_quantization.md`](sync_cost/derivations/dynamical_quantization.md)
for the headline articulation, including the prism / spectral
analogy: Stern-Brocot is the substrate's prism, decomposing the
continuous coupling into discrete locked frequencies (tongues
$\sim$ spectral lines, $(K/2)^q$ widths $\sim$ line widths,
mode counts $\sim$ atomic structure constants).

## A second clarifying note: address vs. structure

The framework predicts two categorically different kinds of
constants, and conflating them is the most common reading error.
*Dimensionless ratios* — Ω_Λ = 13/19, sin²θ_W = 8/35, α_s/α_2
= 27/8, K_c = 2/π — are structural; they are forced by the
combinatorial structure and would be the same for any observer at
any cosmic epoch, in any unit system. *Dimensionful constants* —
H_0, ℏ, v_EW, the Planck mass — are addresses; they tell you
where on the structure we are, not what the structure is.

The cleanest physical demonstration of this distinction is the
helium-chamber test. A tuba's pitch lives in the medium (the air
that resonates inside it), and changes when the medium changes —
in helium, a tuba sounds about three semitones higher (the
Donald-Duck-effect for instruments). A contrabass's pitch lives
in the structure (the string itself); the medium is irrelevant,
and a contrabass sounds the same in air and in helium. The
framework's claim is that the universe has *both* registers. The
Standard Model treats every constant as a tuba-pitch, which is
why it has roughly 20 dimensionful free parameters; this
framework recovers a contrabass-pitch — Ω_Λ = 13/19 — that does
not change under any "medium swap" you could imagine.

See [`medium_change_demo.md`](sync_cost/derivations/medium_change_demo.md)
for the full walkthrough, including the tuba/contrabass/speaker
comparison table and the framework interpretation.

## Entry points

Each entry is a single intellectual move. Accept it and the
framework's content becomes consequential. Refuse it and the
framework reads as numerology.

Pick the entry that matches your existing intuitions. The first
two are empirical (numerical residuals against published data);
the next three are structural (each gates one classical "open
problem"); the last is methodological (justifies the framework's
declined claims).

### E1 — $\Omega_\Lambda = 13/19 = 0.6842$ at 0.07σ on Planck

The mental shift: accept that 0.07σ on the most precisely measured
cosmological parameter, from a small-integer ratio with zero
fitted parameters, is too clean to be coincidence.

**If accepted**: the framework's [`baryon_fraction.md`](sync_cost/derivations/baryon_fraction.md)
derivation of the cosmic partition $13:5:1/19$ from $Z_6$ mode
counting becomes the natural reading. The two-component refinement
([`omega_b_alpha_beta_closure.md`](sync_cost/derivations/omega_b_alpha_beta_closure.md))
sharpens to $\Omega_b = 13/264$ at 0.12%, $\Omega_{DM} = 35/132$
at 0.06%, $\Omega_\Lambda = 181/264$ at 0.13% — full Class 5
closure with zero free parameters.

See: [Lemma 4](sync_cost/derivations/structural_lemmas.md) (cosmic
partition) and [Lemma 1](sync_cost/derivations/structural_lemmas.md)
(two-component closure).

### E2 — MOND $a_0 = c H_0 / (2\pi)$ at 4% on Lelli 2017 RAR

The mental shift: accept that the empirical MOND scale is
structurally derived from $\Lambda$ via $a_0 = cH_0/(2\pi)$, and
that MOND is a substrate feature (the partial-locking dynamics
at the EM coupling threshold), not a modification of gravity.

**If accepted**: galactic rotation curves at low acceleration
follow from the substrate's partial-decoupling dynamics; no
dark-matter halo at galactic scale. The cosmological "dark
matter" abundance $\Omega_{DM} = 5/19$ is a substrate sector
(sign-rep antisym modes, Klein-monodromy −1, no EM coupling)
rather than a particle species.

See: [`a0_threshold.md`](sync_cost/derivations/a0_threshold.md)
and [Lemma 2](sync_cost/derivations/structural_lemmas.md)
(sign-rep no-EM).

### E3 — Spatial dimension $d = 3$ is forced, not observed

The mental shift: accept that 3D space is a substrate consequence
of the color triplet structure $Z_3 \subset Z_6 = q_2 \times q_3$,
not an empirical input.

**If accepted**: the framework's structural derivations of the
SM gauge group $SU(3) \times SU(2) \times U(1)$ and anomaly
cancellation (all 6 conditions $= 0$) follow from the same
$Z_6$ substrate machinery. Spatial dimension, gauge group, and
anomalies become one derivation rather than three observations.

See: [`three_dimensions.md`](sync_cost/derivations/three_dimensions.md)
and [Lemma 8](sync_cost/derivations/structural_lemmas.md).

### E4 — Cosmological constant from depth, not fine-tuning

The mental shift: accept that $\Lambda \cdot \ell_P^2 =
13^{-108}/12$ is the *expected* behavior of multiplicative
depth-54 stratification, not a fine-tuning. The smallness
$10^{-122}$ is the natural output of a depth machine.

**If accepted**: the cosmological constant problem dissolves.
Standard QFT estimates of $\Lambda \sim M_P^4$ assume Wilsonian
RG with quadratic divergences; a discrete substrate has neither.
The "naturalness problem" framing was an SM-specific import that
doesn't apply.

See: [`hierarchy_gaussian_lattice.md`](sync_cost/derivations/hierarchy_gaussian_lattice.md)
and [`hierarchy_problem_translation.md`](sync_cost/derivations/hierarchy_problem_translation.md).

### E5 — Strong CP $\theta = 0$ from substrate symmetry

The mental shift: accept that the QCD vacuum angle vanishes
exactly because of the substrate's Klein-antipodal $Z_2$
invariance, not because of an undetected Peccei-Quinn axion.

**If accepted**: the strong CP problem is resolved structurally.
The 40-year search for axions becomes unnecessary at the
substrate level (axions can still exist as effective theory
constructs, but the strong CP "problem" doesn't motivate them).

See derivation chain D45 referenced in
[`framework_status.md`](sync_cost/derivations/framework_status.md).

### E6 — SM hierarchy problem doesn't translate

The mental shift: accept that the SM hierarchy problem requires
three ingredients (small ratio + naturalness + Wilsonian RG),
only the first translates to a discrete substrate, so the
"problem" dissolves rather than needing a small-Higgs mechanism.

**If accepted**: $v / M_P \approx 2 \times 10^{-17}$ is anchor-side
input requiring no further mechanism. SUSY, technicolor, and
extra-dimensional resolutions to the hierarchy problem become
unmotivated by this concern (they may still be motivated by
others). The framework's two-anchor minimum is the structurally
correct shape.

See: [`hierarchy_problem_translation.md`](sync_cost/derivations/hierarchy_problem_translation.md)
and [`path_a_walkthrough.md`](sync_cost/derivations/path_a_walkthrough.md).

### Recommended starting pair

E1 and E2 together. Both empirical, both with explicit numerical
residuals, both falsifiable. Together they establish that
cosmology has a small-integer structure (E1) and that galactic
dynamics has the substrate's MOND threshold derived from
cosmology (E2). Accepting both as non-coincidental opens the
framework's full content; the structural and methodological
entries (E3-E6) follow as natural extensions.

## Predictions

| Prediction | Framework | Observed | Residual | Source |
|---|---|---|---|---|
| Spectral tilt $n_s$ | 0.963–0.966 | 0.9649 ± 0.0042 | < 0.2% | [`spectral_tilt_reframed.md`](sync_cost/derivations/spectral_tilt_reframed.md) |
| Born rule exponent | 2 | 2 | exact | [`born_rule.md`](sync_cost/derivations/born_rule.md), [Lemma 7](sync_cost/derivations/structural_lemmas.md) |
| MOND scale $a_0$ | $1.25 \times 10^{-10}$ m/s² | $1.2 \times 10^{-10}$ | 4% | [`a0_threshold.md`](sync_cost/derivations/a0_threshold.md) |
| Spatial dimension | 3 | 3 | exact | [`three_dimensions.md`](sync_cost/derivations/three_dimensions.md) |
| Lorentz symmetry | Spin(3,1) | SO⁺(3,1) | exact | [`lie_group_characterization.md`](sync_cost/derivations/lie_group_characterization.md) |
| Strong CP $\theta$ | 0 | $< 10^{-10}$ | exact | substrate symmetry |
| SM gauge group | SU(3) × SU(2) × U(1) | SU(3) × SU(2) × U(1) | exact | structural |
| SM anomaly cancellation | all 6 = 0 | all 6 = 0 | exact | substrate identities |
| Down-type quark factor | 6 | 6 | 0.04σ | [`down_type_double_cover_closed.md`](sync_cost/derivations/down_type_double_cover_closed.md) |
| Up-type quark factor | 9 | 9 | 0.34σ | [`item12_K_star_closure.py`](sync_cost/derivations/item12_K_star_closure.py) |
| $\Omega_\Lambda$ (single-w) | $13/19 = 0.6842$ | $0.6847 \pm 0.0073$ | **0.07σ** | [`baryon_fraction.md`](sync_cost/derivations/baryon_fraction.md) |
| $\Omega_b$ (two-component) | $13/264 = 0.04924$ | $0.0493 \pm 0.0003$ | **0.12%** | [`omega_b_alpha_beta_closure.md`](sync_cost/derivations/omega_b_alpha_beta_closure.md) |
| $\Omega_{DM}$ (two-component) | $35/132 = 0.26515$ | $0.265 \pm 0.007$ | **0.06%** | same |
| $\Omega_\Lambda$ (two-component) | $181/264 = 0.68561$ | $0.6847 \pm 0.0073$ | **0.13%** | same |
| Planck/Hubble ratio $R$ | $6 \times 13^{54}$ | $8.49 \times 10^{60}$ | 0.48% | [`hierarchy_gaussian_lattice.md`](sync_cost/derivations/hierarchy_gaussian_lattice.md) |
| $\Lambda \ell_P^2$ | $13^{-108}/12$ | $\sim 10^{-121.5}$ | 0.1% in exponent | same |
| $A_s$ substrate-side | $2.33 \times 10^{-9}$ | $2.10 \times 10^{-9}$ | 11% (anchor-side gap, [Instance 7](sync_cost/derivations/vocabulary_is_the_work_pattern.md)) | [`a_s_geometric_proof.md`](sync_cost/derivations/a_s_geometric_proof.md) |
| $N_{\text{efolds}}$ | 61.3 ± 0.7 | TBD | CMB-S4, ~2030 | [`numerology_inventory.md`](sync_cost/derivations/numerology_inventory.md) |

The two-component closure ([`L1_substrate_cusp_ground_state.md`](sync_cost/derivations/L1_substrate_cusp_ground_state.md))
gives the cosmic partition with **zero free parameters at the
closure level**: $w_+ = 13/14$ is the substrate's cusp-1/2
ground state on $X_0(6)$, derived from the Hecke modular
structure (Direction 4, 2026-04 closure round).

## Reading paths

The framework's docs are available at three depths.

### One-minute skim

This README + the [predictions table](#predictions) above. If
the entry-point pair (E1 + E2) is sufficient as a hook, proceed.

### Ten-minute orientation

Read in order:

1. [`structural_lemmas.md`](sync_cost/derivations/structural_lemmas.md) — nine load-bearing lemmas, ~10 pages
2. [`canonical_glossary.md`](sync_cost/derivations/canonical_glossary.md) — vocabulary translation, ~10 pages
3. [`phenomenology_cross_reference.md`](sync_cost/derivations/phenomenology_cross_reference.md) — observation/prediction comparison, ~12 pages

Together: framework's full claim set in citation-ready form.

### Dissertation reading

[`derivation_atlas.md`](sync_cost/derivations/derivation_atlas.md) — single linear walkthrough from primitives to predictions, 11 parts, ~50 pages.

### Methodological notes

- [`dynamical_quantization.md`](sync_cost/derivations/dynamical_quantization.md) — medium / dynamics distinction; spectral / prism analogy
- [`statistical_conventions.md`](sync_cost/derivations/statistical_conventions.md) — Z1-Z3 discipline
- [`ansatz_audit_policy.md`](sync_cost/derivations/ansatz_audit_policy.md) — Class 4 → Class 2 triage
- [`vocabulary_is_the_work_pattern.md`](sync_cost/derivations/vocabulary_is_the_work_pattern.md) — recurring closure pattern (9 instances)
- [`numerology_count_phase_b.md`](sync_cost/derivations/numerology_count_phase_b.md) — Region C pigeonhole calibration

## Interactive resources

The deployed site under [`docs/`](docs/) and the supplementary
directories [`prototype/`](prototype/) and
[`sync_cost/applications/`](sync_cost/applications/) hold a number
of interactive pages. Grouped by intent:

### Pedagogy and reference

- [`docs/questions.html`](docs/questions.html) — searchable teaching-question views over entry prompts, concept mastery, derivation review, demos, falsifiers, transfer, and claim hygiene.
- [`docs/index.html`](docs/index.html) — quick-reference supplement: predictions table, symbols, two-anchor minimum.
- [`docs/glossary.html`](docs/glossary.html) — interactive chalkboard glossary: every numerical expression in the canonical glossary worked out on click.
- [`docs/phenomenon-glossary.html`](docs/phenomenon-glossary.html) — description-first glossary by phenomenon, with literature names relegated to an *also called* tagline.
- [`docs/derivations.html`](docs/derivations.html) — narrative index of the numbered derivations.
- [`docs/preprint.html`](docs/preprint.html) — preprint-ready presentation aggregating the 2026-04 closure round.

### Interactive graphs

- [`docs/dag.html`](docs/dag.html) — full derivation dependency graph (~150 nodes), with selectable lineage and per-node git history.
- [`docs/mastery-graph.html`](docs/mastery-graph.html) — pedagogical concept graph: 83 plain-language nodes across 13 clusters wired by prerequisite edges.
- [`docs/claim-chain.html`](docs/claim-chain.html), [`docs/claim-chain-views.html`](docs/claim-chain-views.html) — canonical claim chain (one view + three filtered views) generated from `MANIFEST.yml`.
- [`docs/a_s_proof.html`](docs/a_s_proof.html) — three-dimensional layout of the scalar-amplitude proof.
- [`docs/cmb-s4.html`](docs/cmb-s4.html) — CMB-S4 forecast page for the framework's $n_s$ prediction.

### Demos and explainers

- [`prototype/index.html`](prototype/index.html) — Metronome wall: a live simulation of $N$ coupled oscillators on $S^1$, with the devil's-staircase order parameter $W(\Omega)$ plotted alongside.
- [`docs/knobs/coupling.html`](docs/knobs/coupling.html), [`docs/knobs/frames.html`](docs/knobs/frames.html), [`docs/knobs/phase.html`](docs/knobs/phase.html) — single-knob explainer pages isolating coupling strength, reference frames, and phase respectively.

### Applications

- [`sync_cost/applications/stern_brocot_walk.html`](sync_cost/applications/stern_brocot_walk.html) — walk through the Stern-Brocot tree by mediant steps.
- [`sync_cost/applications/mobius_projector.html`](sync_cost/applications/mobius_projector.html), [`mobius_views.html`](sync_cost/applications/mobius_views.html) — the modular-group action on the upper half plane, with selectable projections.
- [`sync_cost/applications/ontology.html`](sync_cost/applications/ontology.html) — framework ontology browser.
- [`sync_cost/applications/double_pendulum.html`](sync_cost/applications/double_pendulum.html) — driven double-pendulum dynamics: a chaotic-coupling reference.
- [`sync_cost/applications/three_body_catalog.html`](sync_cost/applications/three_body_catalog.html) — catalogued periodic three-body orbits.
- [`sync_cost/applications/index.html`](sync_cost/applications/index.html) — landing page for the applications directory.

### Archive

- [`docs/archive/colony.html`](docs/archive/colony.html) — a smooth zoom through the framework's closed state (parabola, Stern-Brocot fractal, Farey tongues, terminal lattice).
- [`docs/archive/collatz.html`](docs/archive/collatz.html) — Collatz conjecture proof attempt via rational extension, with reproducible verification scripts.

## Two independent anchors (structural)

The framework requires two independent observational anchors per
[`anchor_count_audit.md`](sync_cost/derivations/anchor_count_audit.md):
the cosmological scale $H_0$ (equivalently $\Lambda$, $\ell_P$,
or $M_P$ via $R = 6 \times 13^{54}$) and the particle-sector
scale $v_{\text{EW}} = 246$ GeV.

This is a **structural feature**, not a derivation gap. Per the
D.3 closure ([`path_closures_iter3.md`](sync_cost/derivations/path_closures_iter3.md)),
the substrate's $K = 1$ (Einstein) and $K < 1$ (Schrödinger)
continuum limits are non-smoothly separated by the $K = 1$
critical-line tongue-coverage discontinuity. Each regime requires
its own anchor; reduction to one anchor is structurally obstructed.

The nearest numerology for $v / M_P \approx 2 \times 10^{-17}$
is $13^{-15} \approx 1.95 \times 10^{-17}$ (3.1% off), not derived
([`path_a_walkthrough.md`](sync_cost/derivations/path_a_walkthrough.md)
shows why: the framework's prime support $\{q_2, q_3\} = \{2, 3\}$
cannot reach $15 = 3 \cdot 5$ via the canonical register).

See [Lemma 3](sync_cost/derivations/structural_lemmas.md) for
the formal statement.

## Status snapshot (2026-04 closure round)

The framework completed a substantial closure round in 2026-04:

- **Ω_b two-component closure** to full Class 5 — zero free
  parameters at closure level; $w_+ = 13/14$ derived in
  recognize mode via Hecke modular structure on $X_0(6)$
  ([`L1_substrate_cusp_ground_state.md`](sync_cost/derivations/L1_substrate_cusp_ground_state.md))
- **D.3 sector decoupling** to Class 5 — anchor obstruction #5
  closed structurally
- **D.1 Klein π_1 sector assignment** to Class 5
- **A_s Instance 7 closure ACCEPTED** — substrate-side prediction
  is complete; gap to observed value is anchor-side amplification
  (parallel to lattice QCD bare-vs-renormalized distinction)
- **Region C pigeonhole verdict** at α = 0.05 — multi-candidate
  framework-integer ansatz patterns calibrated as statistical
  pigeonhole, not signal; substrate-structural derivation modes
  remain the productive direction
- **Shape F primitive-completeness audit** — four primitives
  verified sufficient through the round's closures

After the round: the Floor section is empty; all five anchor-count
obstructions are reframed/closed; the framework's open list
contains only optional Q4 follow-ups (Instance 7-style status
tagging for tensor-to-scalar r, τ_unlock, etc.) and periodic
audit re-runs.

See [`framework_status.md`](sync_cost/derivations/framework_status.md)
for the current at-a-glance map.

## Numerical evidence: Stribeck lattice

A chain of oscillators coupled by Stribeck friction demonstrates
the dual-regime mechanism numerically.

**Results** ([RESULTS.md](RESULTS.md)):

- **N = 3 is the critical chain length** for frequency conversion.
  Below 3: linear passthrough. At 3+: subharmonic dominates 2–60×.
- **Conversion at one contact, propagation is the rest.** First
  contact drops $\omega_d$ by 3 orders of magnitude. Subharmonic
  propagates with negligible attenuation across remaining elements.
- **Differential attenuation** — high-frequency (slip regime)
  dissipates; subharmonic (stick regime) propagates. The spectral
  tilt in miniature.

## The 2030 prediction

The framework predicts $N_{\text{efolds}} = \sqrt{5} / \text{rate}
= 61.3 \pm 0.7$.

This is the number of e-folds of inflation, set by the eigenvalue
separation of $x^2 - x - 1 = 0$. Falsified if CMB-S4 measures
$N_{\text{efolds}} < 59$ or $> 63$. CMB-S4 is expected to reach
the required precision by ~2030.

If confirmed: inflation duration is algebraic, not a free
parameter.

## Observational program

[Derivation 8](sync_cost/derivations/high_z_mond.md) predicts a
redshift-dependent MOND scale: $a_0(z) = c H(z) / (2\pi) /
\sqrt{g^*(1/\varphi)}$. With the self-consistent $g^*$
correction, the predicted local value is $1.25 \times 10^{-10}$
m/s² (4% from observed $1.2 \times 10^{-10}$).

- **RC100** (Shachar et al. 2023): 100 high-z galaxies with
  resolved kinematics. Data in [`ascii`](ascii). Analysis shows
  $a_0$ is not constant and rises with $z$ (direction matches
  framework).
- **Predictions**: structural $V_{\text{circ}}$ and
  $f_{\text{DM}}$ (derived from the $H_0$ anchor) for KLASS,
  GEKO, CRISTAL surveys. Discriminating leverage at $z > 3$.
- **Scripts**: `predict_highz.py`, `a0_observable.py`,
  `fdm_redshift.py`, `rar_high_z.py` in [`sync_cost/derivations/`](sync_cost/derivations/).

## Engine

The [rfe](https://github.com/nickjoven/rfe) package solves the
rational field equation numerically: one equation, all
observables. Includes self-consistent $g^*$ solver and $a_0$
correction computation.

```sh
pip install -e .        # or: python -m rfe --observables
```

## Related repositories

| Repository | Role |
|---|---|
| [rfe](https://github.com/nickjoven/rfe) | Numerical engine — field equation solver, all observables |
| [proslambenomenos](https://github.com/nickjoven/proslambenomenos) | $\Lambda \to a_0$: one frequency, structural |
| [201](https://github.com/nickjoven/201) | Gravity as synchronization in a frictional medium |
| [intersections](https://github.com/nickjoven/intersections) | Stick-slip dynamics and dark matter |
| [submediant-site](https://github.com/nickjoven/submediant-site) | Derivation chain site: polynomial → evidence |
| [proslambenomenos-site](https://github.com/nickjoven/proslambenomenos-site) | Full Jupyter Book aggregating all repositories |

## Deployed assets (GitHub Pages)

The repository deploys to GitHub Pages on every push to `main` via
[`.github/workflows/pages.yml`](.github/workflows/pages.yml). The
published site lives at `https://nickjoven.github.io/harmonics/`
(default Pages URL for this repository; no custom CNAME). The
`validate` job runs on every PR and is the required status check;
the `deploy` job is gated on it and runs only on push to `main`.

The `Assemble _site` step copies a strict allow-list into the deploy
bundle:

| Source | Served at |
|---|---|
| `index.html` | `/index.html` |
| `docs/` | `/docs/` |
| `teaching/` | `/teaching/` |
| `sync_cost/` | `/sync_cost/` |
| `LICENSE` | `/LICENSE` |

Anything outside that allow-list will 404 in production; the link
checker at [`.github/scripts/check_links.py`](.github/scripts/check_links.py)
enforces this against a hand-curated list of entry-point HTML files.

### What ships to Pages

- **Root entry**: [`index.html`](index.html). The catalog under
  [Interactive resources](#interactive-resources) enumerates the
  per-section entry points.
- **`docs/`** — rendered pedagogical surface:
  - Top level: `index.html`, `questions.html`, `glossary.html`, `phenomenon-glossary.html`,
    `derivations.html`, `dag.html`, `mastery-graph.html`,
    `claim-chain.html`, `claim-chain-views.html`, `a_s_proof.html`,
    `cmb-s4.html`, `preprint.html`, plus shared `style.css` and the
    `*.json` graph payloads (`derivation-graph.json`,
    `mastery-graph.json`, `a_s_proof_graph.json`, `ket-graph.json`,
    `view-labels.json`).
  - [`docs/knobs/`](docs/knobs/) — three single-knob explainers
    (`coupling.html`, `frames.html`, `phase.html`).
  - [`docs/archive/`](docs/archive/) — `colony.html`, `collatz.html`.
- **`teaching/`** — source teaching artifacts served for Pages views:
  `async-presentation-model.md`, `entrypoint-teaching-reference.md`, and
  `question-atlas.md`. The deployed [`docs/questions.html`](docs/questions.html)
  view parses `question-atlas.md` directly.
- **`sync_cost/`** — framework working tree, served verbatim:
  - [`sync_cost/applications/`](sync_cost/applications/) — seven
    interactive applications (`stern_brocot_walk.html`,
    `mobius_projector.html`, `mobius_views.html`, `ontology.html`,
    `double_pendulum.html`, `three_body_catalog.html`, plus the
    `index.html` landing page) and the artifact-explorer JS bundle
    with its supporting data.
  - [`sync_cost/derivations/`](sync_cost/derivations/) — ~220 markdown
    derivation notes and ~237 Python scripts. Pages serves both as
    raw bytes: a browser will display the `.md` files as plain text
    (or download them) and the `.py` files as source. The curated
    reading order is [Reading paths](#reading-paths).
  - [`sync_cost/FRAMEWORK.md`](sync_cost/FRAMEWORK.md),
    [`sync_cost/MINIMUM_SELF_PREDICTING_UNIVERSE.md`](sync_cost/MINIMUM_SELF_PREDICTING_UNIVERSE.md),
    `staircase_forming.svg`, `minimum_self_predicting_universe.svg`.
- **`LICENSE`** — served at site root.

### What is NOT deployed via Pages

The following are in the repository but excluded from the deploy
bundle. Each has either a separate deployment, a GitHub-only
rendering path, or is deliberately out-of-band.

- **[`prototype/`](prototype/)** — the metronome wall (interactive
  $N$-oscillator simulation with live $W(\Omega)$ staircase). Validated
  by its own workflow ([`prototype-validate.yml`](.github/workflows/prototype-validate.yml))
  and configured for a separate Vercel deployment via
  [`prototype/vercel.json`](prototype/vercel.json). It does **not**
  appear under `nickjoven.github.io/harmonics/`. References from the
  Pages site point to the GitHub tree; the README in
  [`prototype/README.md`](prototype/README.md) explains how to run it
  locally with `python3 -m http.server`.
- **[`MANIFEST.yml`](MANIFEST.yml)** — canonical claim manifest
  consumed by the claim-chain pages. The rendered chain ships; the
  source yaml does not. The deployed site links to the GitHub blob
  URL.
- **Repository-root prose** — [`README.md`](README.md),
  [`RESULTS.md`](RESULTS.md),
  [`VISUAL_ONTOLOGY_PROMPT.md`](VISUAL_ONTOLOGY_PROMPT.md). Rendered
  by GitHub itself, not republished under Pages.
- **Root-level Python scripts** — `animate_genesis.py`,
  `animate_mediants.py`, `bifurcation_sweep.py`, `clarinet_lattice.py`,
  `driven_stribeck.py`, `lattice_sweep.py`. Source-only; reachable
  through the GitHub tree.
- **Root-level animations** — `genesis.gif`, `orbit.gif`. Tracked in
  git but not in the deploy bundle.
- **[`problem/`](problem/)** and **`ket/`** (empty placeholder) —
  internal areas, not part of the published surface.
- **`.ket/`** — local ket-substrate ledger (CAS, log, manifest).
  Tracked partially per [`.gitignore`](.gitignore) and intentionally
  not served.
- **[`Makefile`](Makefile)** and `ascii` — build-side artifacts.

### Gaps worth flagging

Things that look like they ought to be reachable from the Pages site
but aren't:

- **The metronome wall has no Pages presence and no published URL
  recorded.** Vercel hosting is configured (`prototype/vercel.json`),
  but no deployment URL is checked into the repo, so the catalog
  entry resolves only to source. Either record the Vercel URL next
  to the catalog entry or extend the `Assemble _site` step to copy
  `prototype/` and add it to the link allow-list.
- **`MANIFEST.yml` is sourced externally from the deployed site.**
  The claim-chain pages reach out to GitHub for the source-of-truth
  manifest. Copying `MANIFEST.yml` into `_site/` (and adding it to
  the link allow-list) would keep the chain self-contained.
- **`RESULTS.md` is not surfaced from the Pages site.** Top-level
  results live only on GitHub-rendered markdown; a dedicated rendered
  page (or a copy into `docs/`) would make them discoverable to
  Pages-only readers.
- **Markdown under `sync_cost/derivations/` is served as raw text.**
  Pages does not render `.md`. Readers arriving via a derivation link
  see plain source. The narrative entry points
  ([`docs/derivations.html`](docs/derivations.html), `preprint.html`)
  partially mitigate this, but the underlying derivations themselves
  do not render. A static `.md → .html` pass (e.g. Jekyll, mdBook,
  or a small build step) would close this gap.
- **Root-level animations (`genesis.gif`, `orbit.gif`) are not
  referenced by any deployed page.** They are evidence assets that
  could carry weight in the landing page or the preprint view if
  surfaced.

If something belongs on Pages but isn't, the change lives in the
`Assemble _site` step of [`.github/workflows/pages.yml`](.github/workflows/pages.yml)
and the entry-point list in
[`.github/scripts/check_links.py`](.github/scripts/check_links.py).

## Structure

```
harmonics/
├── sync_cost/                                    # synchronization cost framework
│   ├── FRAMEWORK.md                              # seed context, primitives, derivation targets
│   └── derivations/                              # ~150 derivation docs + scripts
│       ├── framework_status.md                   # at-a-glance status map
│       ├── structural_lemmas.md                  # nine load-bearing formal lemmas
│       ├── canonical_glossary.md                 # framework ↔ standard physics vocabulary
│       ├── phenomenology_cross_reference.md      # observation vs prediction
│       ├── derivation_atlas.md                   # end-to-end chain (primitives → predictions)
│       ├── numerology_inventory.md               # Class 1–5 classification
│       └── statistical_conventions.md            # Z1–Z3 operational criteria
├── docs/                                          # GitHub Pages deployed assets
├── driven_stribeck.py                             # driven oscillator + coupled pair models
├── stribeck_lattice.py                            # N-element Stribeck chain
├── ascii/                                         # RC100 galaxy data (100 high-z rotation curves)
├── seed/                                          # Rust tooling: seeds ket DAG with claims
├── .ket/                                          # knowledge substrate (content-addressed memory)
├── ket/                                           # ket submodule — BLAKE3 CAS, Merkle DAG, MCP tools
├── MANIFEST.yml                                   # canonical quantitative-claim registry
├── RESULTS.md                                     # experimental findings
├── LICENSE                                        # CC0 1.0 Universal
└── README.md                                      # this file
```

## License

[CC0 1.0 Universal](LICENSE) — No rights reserved.
