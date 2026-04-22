# Simulation dynamics audit: retractions from the 2026-04-22 session

## Summary

The visualization simulator at `github.com/nickjoven/simulation` was
examined to verify parameter semantics after a session produced
suggestive observational claims. The examination revealed the
simulator is a **gradient-descent evaluator on a static potential**,
not a twist-map / area-preserving iteration. Several session claims
framed in twist-map / KAM / Lyapunov language are therefore
mechanistically incorrect and are retracted here.

## What the simulator actually does

Core update rule (from `docs/7/index.html`):

    tmpP.addScaledVector(tmpG, -S.σ * S.γ * dt)

where:
- `tmpG = ∇ψ_F(p)` via finite differences (step H = 1e-3)
- `ψ_F` is a static sum of Gaussian peaks at Farey angles, weight
  K/q² per peak (from `bakeFareySum(Q, K, ...)`)
- σ ∈ {+1, −1} flips descent direction
- γ is the gradient-descent step size (not a coupling)
- ω_rot rotates the potential frame: `q.setFromAxisAngle(axVec, ωrot · t)`

### Corrected parameter semantics

| Parameter | Session interpretation | Actual role |
|---|---|---|
| K | Arnold-tongue coupling strength | Amplitude weight on each Farey peak in the static potential |
| γ | Drive rate, KAM coupling | Gradient-descent step size (numerical stride) |
| σ | Attractor-type label (±antinode, ±node) | Sign of gradient (±1): seek min or max |
| ω_rot | Drive frequency on a twist map | Rotation rate of the whole potential in time |
| gain | "Lock depth" | **Cosmetic only** — render-brightness multiplier |
| STEPS | Time-step count | Ray-marching fragment-shader quality |
| τ_max | Lifetime budget | Dwell-time colour/size encoding for visualization |
| bake N | Lattice depth | Potential pre-evaluation grid resolution |

Only K, γ, σ, ω_rot, σ_θ, σ_r, r_eq affect dynamics. The rest are
visualization-only.

## Session claims retracted

### Retracted outright (twist-map-specific, no analog in gradient descent)

1. **"K_c ≈ K_Greene measurement."** The visible transition between
   K = 0.66 and K = 1.07 is not the standard-map critical coupling.
   In pure gradient descent on a static potential, there is no
   KAM-destruction transition. The observed change is most likely a
   ratio of peak depth to (γ, ω_rot) — seeds can or cannot cross
   between basins as the landscape depth changes relative to their
   step size and the potential's rotation rate. Different phenomenon,
   different scaling, different physics.

2. **"Cantorus formation."** The filament structure observed at
   K = 1.07 is not a Cantor-set remnant of a broken KAM torus. Pure
   gradient descent has no invariant tori to break. What was visible
   is more likely **stable-manifold structure of saddle points**
   between Farey basins — real geometry, but not fractal cantori.
   Mis-identified by name and mathematical object.

3. **"KAM torus survival / Greene's last torus."** The diagonal
   streak structures were not KAM invariant circles. No such
   structures exist in gradient descent. The streaks are likelier
   **stable-manifold paths** or transient trajectories along the
   rotating ψ_F landscape's crest lines.

4. **"Island chains / Poincaré-Birkhoff sub-islands."** These are
   twist-map phenomena. The cluster-of-clumps structures observed
   are **secondary basins** around local maxima of ψ_F at
   mediant rationals — real, but obeying gradient-flow geometry,
   not Birkhoff theorems.

5. **"Lyapunov exponent / escape rate / λ_unlock measurement."** The
   "dying out" of seeds is basin-absorption under gradient descent
   (seeds descend into the dominant basin or other nearby basins),
   not Lyapunov-driven escape from a chaotic region.
   `kam_bridge_synthesis.md`'s λ_unlock is a claim about a different
   dynamical setting (Arnold-Lyapunov on Klein quotient); identifying
   it with any K-threshold in this sim was a category error.

6. **"Relativistic beaming / null cones / length contraction."** Pure
   visual shape-coincidence. No Lorentz symmetry in the dynamics.
   Already-hedged in session; made explicit-retraction here.

7. **"Quantum–classical split at coherence threshold."** The locked
   vs jittery seed populations are both deterministic gradient-
   descent trajectories in different basins. No quantum mechanics
   applies. `born_rule.md` is the framework's Born-rule derivation
   and is independent of this sim.

### Claims that survive with corrected framing

1. **Farey-peak attractor structure.** Confirmed by source: ψ_F is
   literally a sum of Gaussian bumps at Farey rationals p/q with
   weight K/q². Low-q peaks dominate. Fibonacci-denominator peaks
   (1/2, 1/3, 2/3, 3/5, 5/8, ...) are genuinely more attractive than
   generic peaks with the same q. That's a landscape fact.

2. **Ω-partition test at Q = 19.** Still well-defined. Under gradient
   descent, seed density at equilibrium at each Farey peak scales
   with the basin-of-attraction measure. If the framework's 1:5:13
   partition shows up as a three-tier density histogram across F_19
   peaks, that is structurally meaningful. The test doesn't require
   twist-map dynamics.

3. **Klein nodal parity test.** The test (see `klein_nodal_parity.md`)
   is about the **topology of the nodal set** Re[Y_ℓ^ℓ] = 0, which is
   a mathematical property of the spherical harmonic — independent of
   the dynamics that lands seeds on it. Gradient descent to |ψ|² = 0
   lands seeds on the nodal set; the Möbius-vs-disjoint-circles
   distinction remains observable.

4. **Spokes-vs-torus at low/high ω_rot.** Real observation, simpler
   mechanism than adiabatic-vs-sudden KAM: at low ω_rot the potential
   is nearly static and seeds descend to specific angular minima
   (spokes); at high ω_rot the potential rotates faster than seeds
   can track, so seeds effectively see an azimuthally-averaged
   potential and distribute uniformly in φ (torus).

5. **γ as intra-vs-inter basin selector.** Observation stands:
   small γ keeps seeds inside one basin where they resolve its
   substructure; large γ lets seeds jump between basins where they
   sample multiple peaks. The mechanism is gradient-descent step
   size relative to basin width, not tongue-scale vs drive scale.

## Action taken on previous derivations

- `klein_nodal_parity.md`: language cleaned to avoid twist-map
  phrasing; mechanism note added that dynamics is gradient descent
  on |ψ|² (σ = +node) or climb to |ψ|² maximum (σ = −antinode).

- `framework_status.md`: no retracted items to remove — the Klein
  nodal parity test's upgrade criterion is topology-based, unaffected
  by the dynamics correction.

- `numerology_inventory.md`: Klein parity entry unchanged; Class 4
  pending parity-ladder collection.

## Note on the session audit file

`session_audit.md` was from an earlier session and is unrelated to
this correction. This file (`simulation_dynamics_audit.md`) is the
audit pass for the 2026-04-22 session's simulator-interpretation
claims.

## What further work is appropriate

Two tests remain well-posed under the corrected mechanism:

1. **Klein nodal parity ladder** (`klein_nodal_parity.md`):
   five runs at (ℓ, ℓ, 1) for ℓ = 2..6 with σ = +node, ω_rot = 0.
   Test is about topology of the nodal set, not dynamics.

2. **Ω partition histogram at Q = 19**: seed-density histogram
   across F_19 peaks at equilibrium under gradient descent. Check
   for 1:5:13 tiering.

One new exploration is proposed in
`basin_11_connection_exploration.md`: a local study of the 1/1 peak
and its connections to neighboring basins, which is the correctly-
framed version of what the "cantorus" observation was trying to
capture.

## Cross-references

| File | Role |
|---|---|
| `klein_nodal_parity.md` | Parity-ladder test spec, mechanism-clarified |
| `basin_11_connection_exploration.md` | New local-basin study, proposed |
| `framework_status.md` | Proposed items, unchanged |
| `numerology_inventory.md` | Class 4 entries, unchanged |
| `session_audit.md` | Unrelated prior-session audit |
