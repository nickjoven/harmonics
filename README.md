# harmonics

One equation on the Stern-Brocot tree of rationals:

$$N(p/q) = N_{\text{total}} \times g(p/q) \times w(p/q,\; K_0 F[N])$$

Each rational $p/q$ carries a population given by the total mass,
a frequency density $g$, and the Arnold tongue width $w$ at
coupling $K_0 F[N]$. The coupling depends on the population
through the order parameter $F[N]$, so the equation is its own
fixed-point condition. Solve it.

The fixed point has two continuum limits. At $K = 1$ (full
synchronization) it produces the Einstein field equations,
uniquely under Lovelock's theorem given Klein-bottle topology.
At $K < 1$ (partial synchronization) it produces the Schrödinger
equation. The two limits are non-smoothly separated by the
$K = 1$ critical-line tongue-coverage discontinuity, which forces
two independent dimensional anchors — cosmological ($H_0$) and
particle ($v_{\text{EW}}$) — as a structural feature, not a
derivation gap.

Between the two limits, the Stern-Brocot denominator classes
$(q_2, q_3) = (2, 3)$ generate the Standard Model gauge group,
three generations, the cosmic partition $\Omega_\Lambda :
\Omega_{DM} : \Omega_b = 13 : 5 : 1 / 19$, and matter-sector
mass ratios at PDG precision.

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
