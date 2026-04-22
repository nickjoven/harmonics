# harmonics

One equation on the Stern-Brocot tree of rationals:

$$N(p/q) = N_{\text{total}} \times g(p/q) \times w(p/q,\; K_0 F[N])$$

Each rational $p/q$ carries a population given by the total mass, a
frequency density $g$, and the Arnold tongue width $w$ at coupling
$K_0 F[N]$. The coupling depends on the population through the order
parameter $F[N]$, so the equation is its own fixed-point condition.
Solve it.

The fixed point has two continuum limits. At $K = 1$ — full
synchronization — it produces the Einstein field equations, uniquely
under Lovelock's theorem given Klein-bottle topology. At $K < 1$ —
partial synchronization — it produces the Schrödinger equation. Between
them, the Stern-Brocot denominator classes $(q_2, q_3) = (2, 3)$,
forced by the cross-link identity $q_2^2 - 1 = q_3$ and
$q_3^2 - 1 = q_2^3$, generate the Standard Model gauge group, three
generations, and matter-sector mass ratios at PDG precision.

The frequency density $g(\omega)$ is the fixed point of its own
self-consistency, not a free function. The framework has **two
independent observational anchors** per
[`anchor_count_audit.md`](sync_cost/derivations/anchor_count_audit.md):
the cosmological scale $H_0$ (equivalently $\Lambda$, $\ell_P$, or
$M_P$) and the particle-sector scale $v_\mathrm{EW} = 246$ GeV.
Reducing to one would require a framework-derived dimensionless
identity for $v/M_P$; the nearest numerology, $13^{-15}$, misses by
3.1% and is not derived. Five explicit obstructions to closing the
gap are catalogued in the audit.

| Prediction | Value | Observed | Residual |
|---|---|---|---|
| Spectral tilt $n_s$ | 0.963–0.966 | 0.9649 ± 0.0042 | < 0.2% |
| Born rule exponent | 2 | 2 | exact |
| MOND scale $a_0$ | 1.25 × 10⁻¹⁰ m/s² | 1.2 × 10⁻¹⁰ | 4% |
| Spatial dimension | 3 | 3 | exact |
| Dark energy fraction $\Omega_\Lambda$ | 13/19 = 0.6842 | 0.6847 ± 0.0073 | **0.07σ** |
| Planck/Hubble hierarchy $R$ | $6 \times 13^{54}$ | 8.49 × 10⁶⁰ | 0.48% |
| $\Lambda l_P^2$ | $13^{-108}/12$ | $10^{-121.5}$ | 0.1% exponent |
| $N_{\text{efolds}}$ | 61.3 ± 0.7 | TBD | CMB-S4, ~2028 |

The cosmological parameters ($\Omega_\Lambda$, $R$, $\Lambda$) follow from
three numbers: the Klein bottle's denominator classes $q_2 = 2$, $q_3 = 3$,
and the Farey count $|F_6| = 13$. The mediant is derived from energy
conservation + Arnold tongue stability (Stern-Brocot theorem, 1858). See
[D25](sync_cost/derivations/farey_partition.md)–[D29](sync_cost/derivations/mediant_derivation.md).

## Framework

The core claim: all physical dynamics are cost minimization on a
synchronization landscape. The cost functional, applied self-consistently
over a participation set, produces coupling, structure, dimensionality,
and laws at its fixed point.

The minimal system is two things: **distinguishable states** and **a cost
functional**. Everything else is accounting.

See [sync_cost/FRAMEWORK.md](sync_cost/FRAMEWORK.md) for the full seed
context — primitives, derivation targets, resolved framings, and
structural principles.

### Derivation targets

| # | Target | Status | Derivation |
|---|--------|--------|------------|
| 1 | **Born rule** — \|ψ\|² from saddle-node basin geometry | Resolved | [01](sync_cost/derivations/born_rule.md), [09](sync_cost/derivations/fidelity_bound.md) |
| 2 | **Spectral tilt** — n_s ≈ 0.965 from φ² self-similarity | Verified (Δ < 0.2%) | [04](sync_cost/derivations/spectral_tilt_reframed.md), [rfe](https://github.com/nickjoven/rfe) |
| 3 | **Planck scale** — N = 3 self-sustaining loop | Resolved | [06](sync_cost/derivations/planck_scale.md) |
| 4 | **Emergent spacetime** — Einstein uniquely at K = 1 | Resolved | [12](sync_cost/derivations/continuum_limits.md), [13](sync_cost/derivations/einstein_from_kuramoto.md) |
| 5 | **a₀** — 1.25 × 10⁻¹⁰ m/s² (4% residual) | Resolved | [03](sync_cost/derivations/a0_threshold.md), [rfe](https://github.com/nickjoven/rfe) |
| 6 | **SL(2,ℝ) uniqueness** — characterization theorem | Resolved | [15](sync_cost/derivations/lie_group_characterization.md) |
| 7 | **d = 3** — forced by mediant → SL(2,ℝ) | Resolved | [14](sync_cost/derivations/three_dimensions.md) |
| 8 | **g(ω)** — self-consistent: g* = h(g*) | Resolved | [rfe](https://github.com/nickjoven/rfe) |
| 9 | **Möbius container** — topology forces rational divisions | Resolved | [18](sync_cost/derivations/mobius_container.md) |
| 10 | **Klein bottle** — 4 modes at {2,3}, XOR selection | Resolved | [19](sync_cost/derivations/klein_bottle.md) |
| 11 | **Ω_Λ = 13/19** — Farey partition, structural (no fitted factors) | Resolved (0.07σ) | [25](sync_cost/derivations/farey_partition.md)–[29](sync_cost/derivations/mediant_derivation.md) |

### Key results

- **Fidelity bound** ([Derivation 9](sync_cost/derivations/fidelity_bound.md)):
  the MOND transition and wavefunction collapse are the same structure —
  a system resolving its own frequency against a reference it constitutes.
  The RAR interpolating function, collapse duration, uncertainty relation,
  and Zeno effect all follow from one constraint.

- **Spectral tilt** ([Derivation 4](sync_cost/derivations/spectral_tilt_reframed.md)):
  the devil's staircase at 1/φ is exactly self-similar with scaling φ².
  The observed n_s − 1 = −0.035 comes from the k ↔ Ω mapping: 0.0365
  Fibonacci levels per e-fold, 2.2 levels in 60 e-folds.

- **Born rule** ([Derivation 1](sync_cost/derivations/born_rule.md)):
  Δθ ∝ √ε at every tongue boundary (saddle-node universality). The
  exponent 2 in |ψ|² is parabolic geometry, not a postulate.

- **SL(2,R) is the unique substrate** ([Derivation 15](sync_cost/derivations/lie_group_characterization.md)):
  four conditions — arithmetic skeleton from the mediant, projective
  action on ratios, dynamical trichotomy from Iwasawa, Farey-hyperbolic
  geometry — characterize SL(2,R) uniquely among all connected real Lie
  groups. The Bianchi classification of 3D Lie algebras eliminates every
  alternative. d = 3, Einstein, and Lorentz are corollaries.

- **Einstein from Kuramoto** ([Derivation 13](sync_cost/derivations/einstein_from_kuramoto.md)):
  the rational field equation at K = 1, in the continuum limit, uniquely
  produces the Einstein field equations. Uniqueness is not a property of
  the dictionary — it is a theorem (Lovelock, 1971). One equation, one
  parameter, and the only consistent output is G_μν + Λg_μν = 8πGT_μν.

- **Three dimensions from the mediant** ([Derivation 14](sync_cost/derivations/three_dimensions.md)):
  d = 3 is not assumed — it is forced. The mediant generates SL(2,Z);
  the continuum limit completes to SL(2,R); self-consistent adjacency
  forces the spatial manifold to be the group itself. dim SL(2) = 2²−1 = 3.
  SL(2,C) ≅ Spin(3,1) gives Lorentz symmetry from complexification.

### Key framings

- Forces are cost gradients through different coupling channels
- The hierarchy problem dissolves: ratio of global to local
  synchronization density, both fixed by self-consistency
- Renormalization enforces cost self-consistency, not a formal trick
- Measurement is dissipative convergence completing; collapse has duration

## Numerical evidence: Stribeck lattice

The framework's first concrete test. A chain of oscillators coupled by
Stribeck friction demonstrates the dual-regime mechanism numerically.

**Results** ([RESULTS.md](RESULTS.md)):

- **N = 3 is the critical chain length** for frequency conversion.
  Below 3: linear passthrough. At 3+: subharmonic dominates 2–60×.

- **Conversion at one contact, propagation is the rest.** First contact
  drops ω_d by 3 orders of magnitude. Subharmonic propagates with
  negligible attenuation across remaining elements.

- **Differential attenuation** — high-frequency (slip regime) dissipates;
  subharmonic (stick regime) propagates. The spectral tilt in miniature.

## The 2028 prediction

The framework predicts $N_{\text{efolds}} = \sqrt{5} / \text{rate} = 61.3 \pm 0.7$.

This is the number of e-folds of inflation, set by the eigenvalue
separation of $x^2 - x - 1 = 0$. It is falsified if CMB-S4 measures
$N_{\text{efolds}} < 59$ or $> 63$. CMB-S4 is expected to reach the
required precision by ~2028.

If confirmed: inflation duration is algebraic, not a free parameter.

## Observational program

[Derivation 8](sync_cost/derivations/high_z_mond.md) predicts a
redshift-dependent MOND scale: $a_0(z) = c H(z) / (2\pi) / \sqrt{g^*(1/\varphi)}$.
With the self-consistent $g^*$ correction, the predicted local value is
$1.25 \times 10^{-10}$ m/s² (4% from observed $1.2 \times 10^{-10}$).

- **RC100** (Shachar et al. 2023): 100 high-z galaxies with resolved
  kinematics. Data in [`ascii`](ascii). Analysis shows $a_0$ is not
  constant and rises with $z$ (direction matches framework).
- **Predictions**: structural $V_{\text{circ}}$ and $f_{\text{DM}}$ (derived
  from the H_0 anchor) for KLASS, GEKO, CRISTAL surveys. Discriminating
  leverage at $z > 3$.
- **Scripts**: `predict_highz.py`, `a0_observable.py`, `fdm_redshift.py`,
  `rar_high_z.py` in [`sync_cost/derivations/`](sync_cost/derivations/).

## Engine

The [rfe](https://github.com/nickjoven/rfe) package solves the rational
field equation numerically: one equation, all observables. Includes
self-consistent $g^*$ solver and $a_0$ correction computation.

```sh
pip install -e .        # or just: python -m rfe --observables
```

## Related repositories

| Repository | Role |
|---|---|
| [rfe](https://github.com/nickjoven/rfe) | Numerical engine — field equation solver, all observables |
| [proslambenomenos](https://github.com/nickjoven/proslambenomenos) | $\Lambda \to a_0$: one frequency, structural (see `a0_threshold.md`) |
| [201](https://github.com/nickjoven/201) | Gravity as synchronization in a frictional medium |
| [intersections](https://github.com/nickjoven/intersections) | Stick-slip dynamics and dark matter |
| [submediant-site](https://github.com/nickjoven/submediant-site) | Derivation chain site: polynomial → evidence |
| [proslambenomenos-site](https://github.com/nickjoven/proslambenomenos-site) | Full Jupyter Book aggregating all repositories |

## Structure

```
harmonics/
├── sync_cost/                 # synchronization cost framework
│   ├── FRAMEWORK.md           # seed context, primitives, derivation targets
│   └── derivations/           # 29 derivations (md) + computational scripts (py)
│       └── INDEX.md           # reading order and dependency graph
├── driven_stribeck.py         # driven oscillator + coupled pair models
├── stribeck_lattice.py        # N-element Stribeck chain
├── bifurcation_sweep.py       # single + paired oscillator experiments
├── lattice_sweep.py           # lattice length/amplitude/spatial experiments
├── ascii                      # RC100 galaxy data (100 high-z rotation curves)
├── seed/                      # Rust tooling: seeds ket DAG with open questions + claims
├── .ket/                      # knowledge substrate (content-addressed memory)
├── ket/                       # ket submodule — BLAKE3 CAS, Merkle DAG, MCP tools
├── RESULTS.md                 # experimental findings
├── LICENSE                    # CC0 1.0 Universal
└── README.md
```

## License

[CC0 1.0 Universal](LICENSE) — No rights reserved.
