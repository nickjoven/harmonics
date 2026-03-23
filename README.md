# harmonics

Synchronization cost framework for physical dynamics. Systems converge to
lowest-cost attractors. Force is cost gradient. Structure is what settled
cost minimization looks like.

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
| 1 | **Born rule** — |ψ|² as basin measure of the cost landscape | Resolved | [01](sync_cost/derivations/01_born_rule.md), [09](sync_cost/derivations/09_fidelity_bound.md) |
| 2 | **Spectral tilt** (n_s ≈ 0.965) — mode-locking self-similarity at 1/φ | Resolved | [04](sync_cost/derivations/04_spectral_tilt_reframed.md) |
| 3 | **Planck scale** — N = 3 minimum self-sustaining synchronization domain | Resolved | [06](sync_cost/derivations/06_planck_scale.md) |
| 4 | **Emergent spacetime** — large-N limit of synchronization structure | Resolved | [12](sync_cost/derivations/12_continuum_limits.md), [13](sync_cost/derivations/13_einstein_from_kuramoto.md) |
| 5 | **a₀** — MOND acceleration from synchronization cost threshold | Resolved | [03](sync_cost/derivations/03_a0_threshold.md), [08](sync_cost/derivations/08_high_z_mond.md) |

### Key results

- **Fidelity bound** ([Derivation 9](sync_cost/derivations/09_fidelity_bound.md)):
  the MOND transition and wavefunction collapse are the same structure —
  a system resolving its own frequency against a reference it constitutes.
  The RAR interpolating function, collapse duration, uncertainty relation,
  and Zeno effect all follow from one constraint.

- **Spectral tilt** ([Derivation 4](sync_cost/derivations/04_spectral_tilt_reframed.md)):
  the devil's staircase at 1/φ is exactly self-similar with scaling φ².
  The observed n_s − 1 = −0.035 comes from the k ↔ Ω mapping: 0.0365
  Fibonacci levels per e-fold, 2.2 levels in 60 e-folds.

- **Born rule** ([Derivation 1](sync_cost/derivations/01_born_rule.md)):
  Δθ ∝ √ε at every tongue boundary (saddle-node universality). The
  exponent 2 in |ψ|² is parabolic geometry, not a postulate.

- **Einstein from Kuramoto** ([Derivation 13](sync_cost/derivations/13_einstein_from_kuramoto.md)):
  the rational field equation at K = 1, in the continuum limit, uniquely
  produces the Einstein field equations. Uniqueness is not a property of
  the dictionary — it is a theorem (Lovelock, 1971). One equation, one
  parameter, and the only consistent output is G_μν + Λg_μν = 8πGT_μν.

- **Three dimensions from the mediant** ([Derivation 14](sync_cost/derivations/14_three_dimensions.md)):
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

## Observational program

[Derivation 8](sync_cost/derivations/08_high_z_mond.md) predicts a
redshift-dependent MOND scale: a₀(z) = cH(z)/(2π). This is testable
against high-z kinematic surveys.

- **RC100** (Shachar et al. 2023): 100 high-z galaxies with resolved
  kinematics. Data in [`ascii`](ascii).
- **Predictions**: zero-free-parameter V_circ and f_DM for KLASS, GEKO,
  CRISTAL surveys. Discriminating leverage at z > 3 where sync_cost
  diverges from constant-a₀ and power-law models.
- **Scripts**: `predict_highz.py`, `a0_observable.py`, `fdm_redshift.py`,
  `rar_high_z.py` in [`sync_cost/derivations/`](sync_cost/derivations/).

## Prior work

| Repository | Focus |
|---|---|
| [proslambenomenos](https://github.com/nickjoven/proslambenomenos) | Cosmological constant as fundamental frequency; Kuramoto synchronization → MOND transition |
| [201](https://github.com/nickjoven/201) | Gravity as synchronization in a frictional medium; metric tensor ↔ friction coefficient mapping |
| [intersections](https://github.com/nickjoven/intersections) | Stick-slip dynamics and dark matter; Stribeck friction ↔ MOND interpolating function; bifurcation analysis |

The [proslambenomenos site](https://github.com/nickjoven/proslambenomenos-site)
aggregates all four repositories into a unified Jupyter Book. Pushes to
`sync_cost/` on main trigger a site rebuild via CI.

## Structure

```
harmonics/
├── sync_cost/                 # synchronization cost framework
│   ├── FRAMEWORK.md           # seed context, primitives, derivation targets
│   └── derivations/           # 14 derivations (md) + computational scripts (py)
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
