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

### Derivation targets (open)

1. **Born rule** — |ψ|² as basin measure of the cost landscape
2. **Spectral tilt** (n_s ≈ 0.965) — cost gradient across scales
3. **Planck scale** — minimum self-sustaining synchronization domain
4. **Emergent spacetime** — large-N limit of synchronization structure
5. **a₀** — MOND acceleration from synchronization cost threshold

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

### Application: wireless power transfer

The lattice results reframe Tesla's wireless charging vision. The medium's
friction is not the obstacle — it is the frequency converter. Drive at
2ω₀, let the Stribeck nonlinearity convert to ω₀, and the subharmonic
propagates coherently through the stick regime. Copper wire was chosen
because it linearizes the medium — eliminating the conversion mechanism
that would make the medium itself useful.

## Prior work

| Repository | Focus |
|---|---|
| [proslambenomenos](https://github.com/nickjoven/proslambenomenos) | Cosmological constant as fundamental frequency; Kuramoto synchronization → MOND transition |
| [201](https://github.com/nickjoven/201) | Gravity as synchronization in a frictional medium; metric tensor ↔ friction coefficient mapping |
| [intersections](https://github.com/nickjoven/intersections) | Stick-slip dynamics and dark matter; Stribeck friction ↔ MOND interpolating function; bifurcation analysis |

## Structure

```
harmonics/
├── .ket/                  # knowledge substrate (content-addressed memory)
├── ket/                   # ket submodule — BLAKE3 CAS, Merkle DAG, MCP tools
├── sync_cost/             # synchronization cost framework
│   ├── FRAMEWORK.md       # seed context and derivation targets
│   └── derivations/       # formal derivation attempts
├── driven_stribeck.py     # driven oscillator + coupled pair models
├── stribeck_lattice.py    # N-element Stribeck chain
├── bifurcation_sweep.py   # single + paired oscillator experiments
├── lattice_sweep.py       # lattice length/amplitude/spatial experiments
├── RESULTS.md             # experimental findings
├── LICENSE                # CC0 1.0 Universal
└── README.md
```

## License

[CC0 1.0 Universal](LICENSE) — No rights reserved.
