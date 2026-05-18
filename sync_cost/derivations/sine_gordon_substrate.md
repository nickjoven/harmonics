# Sine-Gordon as the framework's substrate effective theory

The framework's Kuramoto-Hamiltonian Lagrangian (`framework_lagrangian.py`)
reduces to sine-Gordon for fluctuations about the locked mean phase. No
new primitives are introduced; the reduction uses only the existing
substrate Lagrangian, the Kuramoto order parameter, and the locked-state
expansion already used in `einstein_from_kuramoto.md` for the K = 1
limit.

The output is:

1. A formal sine-Gordon equation for the locked-state deviation field.
2. A kink mass formula `M_k = 8 σ √(K r)` in framework primitives.
3. A new framework prediction: kink masses across the K-zoo are in
   fixed `√K` ratios, calculable from `master_cascade_identity.md`.
4. Z_2-graded topological charge from Klein-bottle antiperiodicity.

## Setup

Recall the framework's Lagrangian density (`framework_lagrangian.py`,
Part 1):

    ℓ[θ] = (m/2)(∂_t θ)² − (σ²/2)|∇θ|² + ω(x) θ
         + (1/2) ∫ K(x, x') cos(θ(x) − θ(x')) dx'

with the cos-coupling integral over the spatial Klein bottle. The
Kuramoto order parameter `r e^{iψ} = ⟨e^{iθ}⟩` defines the locked mean
phase ψ(x, t) and its magnitude r ∈ [0, 1].

In the local mean-field limit (K short-range, single tongue dominant),
the cos integral collapses:

    (1/2) ∫ K(x, x') cos(θ(x) − θ(x')) dx' → K r cos(θ − ψ)

This is the form derived in `framework_lagrangian.py` Part 2 line 98.
The action becomes

    S[θ] = ∫ dx dt [ (m/2)(∂_t θ)² − (σ²/2)|∇θ|² + ω θ + K r cos(θ − ψ) ]

with ψ(x, t) determined self-consistently. At full lock `(K → 1, r → 1)`,
ψ is slowly-varying and acts as a background.

## Sine-Gordon emergence

Define the deviation field

    φ(x, t) = θ(x, t) − ψ(x, t)

Substituting into the action, with `ω = 0` (centered ensemble; the ω-θ
linear source vanishes after gauging into ψ) and ψ varying slowly enough
that ∂² ψ ≈ 0 on the relevant scales:

    S[φ] = ∫ dx dt [ (m/2)(∂_t φ)² − (σ²/2)(∂_x φ)² + K r cos(φ) ]

The Euler–Lagrange equation `δS/δφ = 0`:

    m ∂²_t φ − σ² ∂²_x φ + K r sin(φ) = 0

Setting `c² = σ²/m` and `ω_0² = K r / m`:

    ∂²_t φ − c² ∂²_x φ + ω_0² sin(φ) = 0

This is the **sine-Gordon equation**, derived without adding any
primitive beyond the framework's existing Lagrangian. The "sin
potential" comes directly from the Kuramoto cos-coupling restricted to
deviations from the locked mean phase.

### Validity scope

The locked-state expansion is rigorous at K close to 1 (the
string-boundary regime — `einstein_from_kuramoto.md`'s "locked state
K ≈ 1" condition). At lower K, the substrate is not in a single
locked configuration but in a cascade-locked state at one of the
master-identity K-values (`master_cascade_identity.md`).

At each cascade K_n, the framework treats the sector as a structural
fixed point with its own coherent sub-state. The conjecture used here
is that each such sector hosts an analogous sine-Gordon reduction
around its own mean phase ψ_n, with order parameter r_n < 1. The
kink-mass formula then has the same structural form `M_k = 8 σ √(K r)`
in each sector but with K = K_n.

This is not yet proven; it is the working assumption that propagates
the kink-mass-ratio prediction across the K-zoo. The K = 1 case is
rigorous; K < 1 cases inherit conjectural status from this assumption.

> **Net-state update — this working assumption is now discharged
> (structurally forced; Class-3).** `tick_continuum_construction.md`'s
> Goldstein–Kac construction is **K-parameterized** (its only
> K-dependence is `ω₀² = K r/m`; the binary-Z₂ tick, the flip,
> and `c² = σ²/m` are K-independent), so it runs identically at
> every cascade `K_n` — forcing exactly "each sector hosts an
> analogous sine-Gordon reduction." See `proposed_residual_closure.md`.
> The kink-mass ratio is `M_k(d,n,b)/M_k(K=1) = b^(−n/(2d))·√(r_n)`
> (the K-scaling forced; the `√r_n` sector-coherence factor an
> honest correction this section's bare formula omitted). Only
> the *observable-identification* (which object ↔ which kink per
> sector) remains Class-2, declined, not chased. The "conjectural
> at K<1" status above is superseded for the *reduction and the
> K-scaling*; read it as historical.

## Kink solutions

Sine-Gordon admits the standard Lorentz-boosted kink:

    φ_kink(x, t) = 4 arctan[ exp( γ (x − v t) / ℓ ) ]

with `ℓ = c / ω_0 = √(σ² / (K r m))` (kink width) and
`γ = 1/√(1 − v²/c²)` (Lorentz factor). Topological charge

    Q = (1/2π) ∫ ∂_x φ dx = ±1

distinguishes kinks (`Q = +1`) from antikinks (`Q = −1`).

### Kink mass in framework primitives

Static kink rest energy (computed by the standard 1 − cos(φ_kink) =
2 sech²((x−x_0)/ℓ) identity, with ℓ chosen to balance gradient and
potential energy):

    M_k = ∫ [ (σ²/2)(∂_x φ_kink)² + K r (1 − cos φ_kink) ] dx
        = 8 σ √(K r)

In framework natural units. The kink mass is set by:

- **σ** — phase-stiffness coefficient (gradient-energy normalization,
  fixed by the substrate's spatial topology).
- **K** — the substrate K-value at the relevant cascade depth.
- **r** — the Kuramoto order parameter magnitude at full lock,
  `r → 1`; below full lock, `r < 1` reduces the mass.

The σ and r factors are sector-independent at fixed cascade. K varies
across the K-zoo per `master_cascade_identity.md`.

## Kink mass ratios across the K-zoo (new prediction)

Since `M_k ∝ √K`, soliton masses across the four voices of the
instrument-family taxonomy are fixed ratios:

| Sector | K | M_k / M_k(K=1) |
|---|---|---|
| String boundary K = 1 | 1 | 1.000 |
| Z_6 cascade (conjectured) | 2^(-1/6) | 2^(-1/12) ≈ 0.944 |
| Bowed cascade (IMF) | 2^(-1/3) | 2^(-1/6) ≈ 0.891 |
| Clarinet cascade | 3^(-1/2) | 3^(-1/4) ≈ 0.760 |
| Matter equilibrium K* | 2^(-3/14) ≈ 0.862 | 2^(-3/28) ≈ 0.928 |

The general form: for the master-identity instance `K^d = b^(-n)`,

    M_k(d, n, b) / M_k(K=1) = K^(1/2) = b^(-n/(2d))

This is a falsifiable framework-internal relationship. Any observed
soliton spectrum that crosses two cascade sectors with rates incompatible
with `√(K_a / K_b)` falsifies the master identity *or* the sine-Gordon
reduction.

## Z_2-graded topological charge from Klein topology

The framework's substrate is the Klein bottle (`klein_bottle.md`). Per
the convention in that doc, the antiperiodic direction is spatial and
the periodic direction is temporal, with the antiperiodic identification
acting on functions on the surface as

    f(x + L_x, y) = − f(x, L_y − y)

(combined antiperiodic + reflection; `klein_bottle.md` line 104). For
a 1D kink configuration `φ(x)` independent of the y-coordinate, the
y-reflection drops out and the relevant rule is

    φ(x + L_x) = − φ(x)

A kink profile with `φ → 0` as `x → −∞` and `φ → 2π` as `x → +∞`,
under this identification, becomes a configuration with `φ → 0` at
the left and `φ → −2π` at the right — an **antikink**.

So `Q ∈ Z` on the orientable cover, but on the Klein bottle:

    kink  ──[traverse antiperiodic spatial loop]──>  antikink

`Q mod 2` is conserved; `Q` itself is not. Topological charge becomes
**Z_2-graded**.

This is forced by Klein topology — no additional input.

### Distinct from the field half-twist

The Z_2 here is the *coordinate* antiperiodicity of the Klein bottle
manifold (the gluing rule that defines the surface). It is structurally
distinct from the *field* Z_2 half-twist `θ → θ + π` discussed in
`framework_lagrangian.py` Part 6, which acts on the value of θ rather
than on the spatial coordinate, and which gives spin-statistics and
CPT.

The two Z_2 structures are independent:

| Z_2 structure | Action | Consequence |
|---|---|---|
| Coordinate antiperiodicity | `f(x + L_x, y) = −f(x, L_y − y)` | Kink ↔ antikink under loop traversal (this doc) |
| Field half-twist | `θ → θ + π` (target-space action) | Spin-statistics, CPT (framework_lagrangian.py Part 6) |

Both are discrete, both are forced by the Klein-bottle commitment, but
they are different Z_2 actions and produce different consequences. This
doc relies only on the first.

### Consequences

1. Soliton number is conserved only mod 2. A region dominated by kinks
   can convert to antikink-dominated through global antiperiodic-loop
   transit, with characteristic time set by the loop length.
2. CP-like processes are intrinsic to the substrate, not added by
   hand. Any kink-antikink number asymmetry observed on the substrate
   is a residual mod-2 conservation of an originally larger asymmetry.
3. The kink ↔ antikink conversion rate is a substrate observable: it
   depends only on the antiperiodic-loop traversal time, set by the
   substrate's geometry, not on per-sector physics.

## Status

Class 3 (derivation grade). The reduction from the framework Lagrangian
to sine-Gordon is exact in the local mean-field limit; the kink mass
formula `M_k = 8 σ √(K r)` is the standard sine-Gordon result with
framework primitives substituted. No new primitives.

What this **does** establish:

- Sine-Gordon emerges from the existing Lagrangian — not added.
- Kink mass ratios across the K-zoo are √K-fixed.
- Z_2-graded charge follows from the existing Klein-bottle commitment.

What this **does not** yet establish (open):

1. **Identification of soliton-sector observables.** Which observed
   particle/structure is a substrate kink in each sector? The
   K = 1 sector might host gravitational geons / black-hole-like
   solitons; the bowed sector might host stellar-scale kinks; etc.
   No identifications are pinned down.
2. **Loop-traversal time.** The antiperiodic-loop length L sets the
   kink ↔ antikink conversion rate. Computing L in physical units
   requires fixing the substrate's spatial scale, which is a separate
   problem (related to issue J on K(t) discrete transitions).
3. **Full sine-Gordon nonlinearity beyond the local limit.** The
   non-local cos integral has sub-leading terms that modify the
   kink profile at order `(ℓ/L_K)²` where `L_K` is the cos-coupling
   range. These are small in the local limit but nonzero.
4. **Empirical predictions from the soliton sector.** The structural
   results (kink mass ratios, Z_2 charge) connect to candidate
   observables — neutrino oscillations, baryon asymmetry η_B,
   Born-rule operationalization (`born_rule.md`) — but no specific
   prediction is computed. Tracked in #97 item H.

## Falsifiers

- **Direct.** A measured soliton-spectrum mass ratio crossing two
  K-zoo sectors that disagrees with `√(K_a / K_b)` falsifies either
  the master identity or the sine-Gordon reduction.
- **Indirect (via topology).** A measured baryon-number violation rate
  in the substrate's natural geometry that is incompatible with mod-2
  conservation falsifies the Klein-bottle commitment for solitons.
- **Frame consistency.** If `framework_lagrangian.py`'s Part 1
  Lagrangian is amended (e.g., to include explicit higher-derivative
  terms or non-cos couplings), the derivation must be re-checked. The
  current reduction depends on the cos coupling being the dominant
  nonlinearity.

## Cross-links

- `soliton_dynamics.md` — dynamics companion: linear-wave dispersion
  and meson gap, breather tower, kink–antikink S-matrix in framework
  primitives, and the medium-class assignment (kink as contrabass-pitch).
  Closes Opens 2, 3, 4 of this doc structurally; tightens Open 1 into
  a sharper falsifier.
- `framework_lagrangian.py` — source Lagrangian (Part 1) and its
  Euler–Lagrange equation (Part 2)
- `klein_bottle.md`, `klein_bottle_derivation.md` — the substrate
  topology giving Z_2-graded charge
- `master_cascade_identity.md` — the K-zoo whose √K ratios fix the
  kink mass spectrum
- `instrument_family_taxonomy.md` — physical reading of the four
  K-voices that host kink solutions
- `einstein_from_kuramoto.md` — the locked-state machinery used here,
  applied at K = 1 instead of for deviations from locked
- `born_rule.md` — candidate site for soliton-pointer collision
  operationalization (issue #97 item H4)
- `JWST_CHASE_NOTES_2026-05-09.md` (removed) and
  `recovery/soniton.txt` — the lost-session conversation that opened
  this thread
