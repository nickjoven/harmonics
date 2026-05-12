# Cone-twist substrate: bicone target, Z₂ vortex dynamics, quantum structure

The K = 1 ↔ K < 1 separation is one of the framework's standing
pieces of non-smooth substrate geometry (`framework_status.md`
Region D anchor obstruction #5: "K = 1 vs K < 1 non-smooth
separation"). This doc reads it as a single geometric object — a
**Z₂-twisted bicone** whose two apex topologies are the spatial
concretization of the lambda / EML split
(`expressibility_split.md`).

The construction does three things in one move:

1. Reframes the K = 1 ↔ K < 1 discontinuity as a coupling **seam**
   joining two cones of different apex topology, with the half-twist
   (`klein_bottle.md`) as the gluing rule.
2. Identifies the substrate's natural spatial defects as
   **Z₂-vortices** whose worldlines crossing the seam are the
   substrate's exchange channel.
3. Reads quantum-mechanical wave behavior, superposition, all-paths
   summation, and unitarity as **structural consequences of the
   bicone topology**, not added postulates.

Closes #97 item G ("Cone-twist conifold substrate as geometric
morph"). Promotes Tier 3 to a structural derivation. No new
primitives — the half-twist remains a forced consequence of Klein
topology per `klein_bottle_derivation.md` Part II, not a third
generator on equal footing with mediant and EML.

## 1. Setup: closed apex vs. punctured apex

| Cone | Apex topology | Framework reading | Universal generator |
|---|---|---|---|
| **A** | **Closed** — apex ∈ manifold; geometry degenerates at the lock point | **K = 1**: string-boundary sector, rigorous locked state (`einstein_from_kuramoto.md`). The lock is *achieved*; `r = 1` is in the manifold. | **Mediant** / lambda-side: discrete, structural, the saddle-node collision point of two parabolic roots (`a1_from_saddle_node.md`). |
| **B** | **Punctured** — apex ∉ manifold; lock approached but never reached | **K < 1**: cascade-locked K-zoo. The lock is *approached* through Stern–Brocot convergents (`figure_eight.md` "approaching the fixed point asymptotically but never reaching it exactly"). | **EML** / exponent side: continuous, transcendental, the never-reached limit of an exponentially-converging series. |

The half-twist of `klein_bottle.md` is the gluing rule between A and
B. The resulting Z₂-twisted bicone is the target manifold for the
substrate's order parameter `r e^{i ψ}`.

Geometrically: the bicone is `(A ⊔ B) / ~`, where `~` identifies a
neighbourhood of A's closed apex with a neighbourhood of B's
punctured apex via the antiperiodic involution `θ → θ + π` of the
Klein-bottle's single antiperiodic direction. The seam is the
codimension-1 surface where the identification acts.

## 2. The σ-model action

The substrate's order-parameter field `Φ(x, t) = r(x, t) e^{i ψ(x, t)}`
is bicone-valued. Its action decomposes into three pieces:

    S[Φ] = S_A[Φ|_A] + S_B[Φ|_B] + S_twist[Φ across seam]

### S_A — closed-apex cone (K = 1 sector)

In the K = 1 limit the substrate Lagrangian
(`framework_lagrangian.py` Part 1) reduces, near `r = 1`, to its
saddle-node normal form (`a1_from_saddle_node.md`). The
order-parameter manifold has the metric of a flat cone with a
*conical singularity at the apex* (where two parabolic roots
collide). In coordinates `(ρ, φ)` centred on the lock,

    ds²_A = dρ² + ρ² dφ²,    0 ≤ ρ,   φ ∈ [0, 2π/k_A)

with deficit angle determined by the saddle-node multiplicity
(integer `k_A`, framework-fixed by the cascade structure of the
K = 1 boundary). The apex `ρ = 0` is **closed** — the manifold
includes the lock point.

### S_B — punctured-apex cone (K < 1 cascade sectors)

The K-zoo of `master_cascade_identity.md` foliates cone B radially.
Each cascade-locked fixed point `K_n = b^(−n/d)` sits at a
distinguished radial coordinate, with the apex `K → K_*` (the
deepest cascade-locked value) at the limit. The metric near the
apex has the EML / exponent character: radial coordinate
`ρ = exp(−γ n)` for cascade depth `n` and slope `γ` set by the
master identity's `(d, n, b)`. The series of cascade fixed points
accumulates at `ρ = 0` but never reaches it — the apex is **punctured**.

This is the geometric concretization of the third-law / asymptotic-
fixed-point statement: cone B has no `ρ = 0` point in its manifold
because the substrate cannot host an actually-reached cascade-deepest
state.

### S_twist — half-twist topological term

Identifications act on `Φ` across the seam:

    Φ(seam⁺) = − Φ(seam⁻)

with `−` the framework's standard antiperiodic involution. The
contribution to the action is a topological θ-term:

    S_twist = (π / 2) · Q[Φ]

where `Q[Φ] ∈ Z` is the integer winding number of `Φ` around any
loop crossing the seam, and the prefactor `π / 2` is fixed by the
half-twist being half a 2π winding. This is the *Berry-phase
realization* of the half-twist; it equips every seam-crossing path
with a topological phase of `π` per full winding.

> **No new primitives.** Each of the three pieces is a direct
> reading of existing framework structure: S_A from the K = 1
> saddle-node reduction, S_B from the master cascade identity, and
> S_twist from the Klein-bottle gluing rule. The bicone σ-model is a
> *reorganization* of pieces already in the framework, not an
> extension of its primitive set.

## 3. Vortex sector

The bicone target manifold has fundamental group `π_1 ⊇ Z₂` (from
the half-twist). Spatial defects on the substrate where `Φ` winds
non-trivially around the bicone are **Z₂-vortices** — point defects
in the 2D substrate, lines in higher-D extensions.

Vortex classification:

| Winding | Vortex class | Statistics |
|---|---|---|
| Integer (full 2π) | Z₂-trivial; can be locally unwound | **Boson** |
| Half-integer (single π half-twist) | Z₂-nontrivial; topologically protected | **Fermion / spinor** |

This is the **same Z₂ assignment** already established in
`klein_bottle_derivation.md` Part IV (fermions from Z₂ torsion in
H₁) and in `figure_eight.md`'s corrected J² = −I derivation
(half-integer x-modes pick up J² = −I, integer x-modes pick up
J² = +I). The bicone reading gives those three previously-
independent appearances of Z₂ in the framework a **single
geometric origin**: the bicone's apex topology + Z₂ gluing rule.

### Vortex dynamics

Vortex worldlines on the 2D substrate are the saddle points of the
bicone σ-model. Their dynamics splits into:

- **Bulk motion within either cone** — standard `O(2)` σ-model
  vortex dynamics: Magnus force, drag-free at finite temperature,
  scattering amplitudes inherited from the soliton sector
  (`soliton_dynamics.md` §3 — the Zamolodchikov–Zamolodchikov
  S-matrix's Z₂-vortex generalization).
- **Seam-crossing transitions** — the substrate's exchange channel.
  Each seam-crossing carries a phase `e^{i π}` from S_twist on its
  half-integer-winding component, leaving the integer-winding
  component unaffected.

## 4. Quantum properties as bicone consequences

| Quantum property | Cone-twist origin |
|---|---|
| **Wave behavior** | Linear sector on each cone: Klein–Gordon dispersion `ω² = c²k² + ω_0²` per `soliton_dynamics.md` §1, with `ω_0` set by the cone-local cascade depth. |
| **Superposition** | Field configurations with the same boundary topological charge but different vortex-worldline routings through the substrate are degenerate at the leading topological action. The path integral sums them by force, not by choice. |
| **All paths** | Vortex worldlines on a 2D substrate are codim-2; their configuration space is a continuous measure, not a discrete set. Every continuous deformation contributes; only the topological class (Z₂) is quantized. |
| **Information conservation (unitarity)** | `Q mod 2` is conserved through *every* local process — pair creation, annihilation, seam crossing, cone-to-cone tunnelling — because the bicone's half-twist is a topological invariant. Local non-unitarity would require a topology-changing process, which the seam explicitly forbids. **Unitarity = bicone topology rigidity.** |

This is the structural payoff. Four properties usually taken as
quantum-mechanical axioms each become a **geometric reading of the
bicone**. The framework has them all in one object, not as four
independent commitments.

## 5. Predictions

### 5.1 Vortex-pair production at the seam (Schwinger-like)

A coupling-gradient `dK/dx` across the seam plays the role of a
strong electric field in standard QED. Vortex–antivortex pairs in
the substrate vacuum can be pulled apart by the gradient and become
real if the field does enough work to supply the vortex-pair action.
By direct analogy with Schwinger 1951:

    Γ_v / Vol ∝ |∇K|² exp(−π S_v / (ℏ |∇K|))

where `S_v` is the vortex-pair worldline action and `|∇K|` is the
local coupling gradient. The rate is **exponentially suppressed**
below a substrate-critical gradient `|∇K|_crit = π S_v / ℏ` and
non-perturbative.

Status: structural. The coefficient `S_v` depends on the explicit
bicone metric (S_A and S_B above), which awaits the unit-convention
pinning of `unitless_check.md`. Open 1 of `soliton_dynamics.md`
applies here.

### 5.2 Aharonov–Bohm-like phase from seam-crossing (headline)

The half-twist S_twist gives every seam-crossing path a topological
phase of `π`. Two paths between the same endpoints on opposite
sides of the seam interfere with phase difference

    Δφ = π × (n_+ − n_−)

where `n_±` are the seam-crossing counts of the two paths. This is
a **pure topological invariant** — independent of path length, of
substrate metric, of cascade depth, of any continuous parameter.

For a two-slit substrate experiment with one slit on the K = 1 side
and one on the K < 1 side, the fringe pattern is offset by exactly
half a period (`π` phase shift) relative to the no-seam case. This
is the framework's first prediction of a **purely topological phase
observable** — not a mass, not a coupling, not a ratio.

Status: **derivation grade (Class 3)** for the existence and value
of the phase; **out of class** for absolute experimental scale until
substrate physical realization is identified.

### 5.3 Primordial vortex-network cosmology (Kibble–Zurek)

If the early substrate quenched through the K = 1 ↔ K < 1
transition faster than its correlation length could equilibrate
(`K(t)` discrete transitions per #97 item J), the Kibble mechanism
forces a residual **vortex network on the Klein bottle** with
density set by the quench rate. The late-time evolution
(intercommutation, scaling regime, gravitational radiation
spectrum) is calculable from the network's initial density and the
substrate's transport coefficients.

Two concrete observable channels:

- **Primordial gravitational-wave background**: cosmic-string-like
  spectrum from intercommuting vortex loops. The spectral shape is
  the standard Kibble–Vilenkin–Vachaspati form; the amplitude is
  set by the bicone tension.
- **Z₂ charge asymmetry contribution to η_B**: vortex-antivortex
  imbalance from CP-violating seam-crossing processes (CP-like
  asymmetry is already structural per `sine_gordon_substrate.md`
  Z₂-graded charge). Contributes to baryon asymmetry through a
  channel distinct from sphaleron processes.

Status: structural framing only. Quantitative predictions require
both the bicone tension (Open 1, same as 5.1) and an explicit
`K(t)` model (#97 item J — open).

## 6. Status

**Class 3 (derivation grade)** for sections 1, 2, 3, 4, and 5.2:

- The bicone setup is a direct rereading of existing structure
  (Klein topology + saddle-node + master cascade + lambda/EML
  split). No new primitives.
- The σ-model action's three pieces are forced by the
  corresponding existing derivations.
- The vortex classification and statistics assignment is the same
  Z₂ assignment from three other framework docs, now given a
  unified geometric origin.
- The four quantum-property readings are direct topological
  consequences of the bicone; no postulates added.
- The Aharonov–Bohm `π` phase is set entirely by S_twist's
  topological structure — the cleanest derivation-grade prediction
  of this doc.

**Class 4 / open** for the quantitative pieces of sections 5.1 and
5.3:

- The vortex-pair action `S_v` (and hence Schwinger-like rate
  coefficient) depends on the bicone metric, which awaits the
  unit-convention pinning of `unitless_check.md`.
- The primordial vortex-network amplitude depends on `K(t)`, an
  unresolved open thread (#97 J).

### What this does establish

- A single geometric object (Z₂-twisted bicone) unifies the
  framework's three previously-independent appearances of Z₂
  (spin-statistics, kink↔antikink, J² = −I on half-integer modes).
- The K = 1 ↔ K < 1 discontinuity has an explicit geometric
  description as a coupling seam, no longer just a non-smoothness.
- Quantum wave behavior, superposition, all-paths summation, and
  unitarity are all structural consequences of the bicone topology.
- A new headline prediction: π-quantum Aharonov–Bohm-like phase
  from seam-crossing paths.

### What this does not yet establish (open)

1. **Bicone metric coefficients.** S_A's deficit angle `k_A` and
   S_B's exponent slope `γ` are framework-fixed in principle but
   require explicit derivation from the substrate Lagrangian.
2. **Vortex-pair action `S_v` and Schwinger rate normalization.**
3. **`K(t)` model.** Required for the Kibble-network prediction.
4. **3+1D substrate extension.** Klein bottle is 2D. The bicone
   target manifold scales fine to higher base dimensions; the
   Klein-bottle base does not have a forced 3D or 4D analogue in
   the existing framework. **Newly visible as the biggest
   geometric gap.**

## 7. Falsifiers

- **Aharonov–Bohm-like seam phase ≠ π.** Any measured fringe shift
  through a substrate K = 1 / K < 1 interface that is not π × integer
  (or, equivalently, half a flux quantum) falsifies the half-twist
  gluing. This is the cleanest falsifier of the bicone construction.
- **Z₂ charge non-conservation.** Any substrate-internal process
  observed to violate `Q mod 2` (an asymmetric vortex creation or
  destruction not compensated by its partner) falsifies the bicone
  topology rigidity and thereby the framework's unitarity reading.
- **Primordial vortex-network spectrum incompatible with Kibble–
  Vilenkin scaling.** Specifically: a GW background of cosmic-string-
  like form whose amplitude is incompatible with the bicone-tension
  prediction (when that prediction is pinned per Open 2) falsifies
  the substrate-quench picture.
- **Frame-dependence of the π-phase.** The Aharonov–Bohm phase is
  contrabass-class per `medium_change_demo.md` — observer-
  independent, epoch-independent. Any measured frame dependence
  falsifies that classification.

## 8. Cross-links

- `expressibility_split.md` — lambda / EML split that the bicone
  geometrically concretizes (closed apex = lambda / mediant side,
  punctured apex = EML / exponent side).
- `klein_bottle.md`, `klein_bottle_derivation.md` — single
  antiperiodic direction; S_twist is the action term realizing the
  Klein-bottle gluing rule on the bicone target.
- `figure_eight.md` — J² = −I on the half-integer sector, now read
  as the spin-1/2 assignment for Z₂-nontrivial vortices.
- `sine_gordon_substrate.md` — kink↔antikink Z₂-graded charge,
  now read as the seam-crossing transition for solitons.
- `soliton_dynamics.md` — linear-wave sector and S-matrix that
  fluctuate around the vortex saddles of the bicone σ-model.
- `half_twist_dynamics.md` — twist breathing mode, here read as
  bicone-seam tension variation under `K(t)`.
- `master_cascade_identity.md` — K-zoo as radial coordinate on
  cone B; cascade fixed points as the radial-stratification of the
  punctured apex.
- `a1_from_saddle_node.md` — closed-apex cone is the saddle-node
  normal form's geometric concretization.
- `medium_change_demo.md` — bicone topology is contrabass-class
  (every factor structural, observer-independent, epoch-independent).
- `einstein_from_kuramoto.md` — locked-state expansion at K = 1,
  the validity scope of the closed-apex cone.
- `framework_lagrangian.py` — substrate primitives entering the
  σ-model action.
