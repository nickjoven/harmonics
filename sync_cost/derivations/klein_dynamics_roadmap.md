# Klein-bottle dynamics roadmap for Ω_b C2 closure

## What this file is

A structural roadmap for the machinery needed to close the Ω_b
residual via the C2 (sym/antisym Klein eigenmode asymmetry)
mechanism. **Surprise finding before sketching**: substantial
Klein-bottle dynamical machinery already exists in the framework.
The "new machinery" question reframes from "build Klein-bottle
dynamics" to "apply existing Klein-bottle dynamics to the
partition formula."

This sketch maps:
- What exists in the framework
- What's been ruled out (null cross-references)
- What's missing (the bridge layer)
- What new probe sequence would close C2

## Existing Klein-bottle dynamics machinery

Framework has more than I'd remembered:

| File | What it does | Relevance to C2 |
|---|---|---|
| `klein_bottle_kuramoto.py` | Kuramoto oscillators on Klein-bottle lattice (3×3 minimum), with antiperiodic+reflect BC in x-direction | **Direct Klein-bottle dynamics; the substrate-level computation needed for C2** |
| `klein_kuramoto_sweep.py` | K-sweep on Klein-bottle Kuramoto (5×5, K from 2 to 20); measures \|r\|, phase gradients, dominant rationals, (2,3) vs (3,2) asymmetry | **Already does the K-sweep on Klein dynamics; needs only sym/antisym extraction** |
| `klein_topological_keff.py` | Derives K_eff = K_0/2 from x-direction topological winding W_x = 1/2 | **Critical constraint: \|r\| ≡ 0 on Klein bottle; sym/antisym must respect this** |
| `klein_within_sector.py` | Field-equation x↔y symmetry; asymmetry comes from Kuramoto twist not field equation | **Already identifies sym-breaking mechanism: lattice twist breaks x↔y in dynamics** |
| `klein_phase_diagram.py` | Phase diagram for Klein-Kuramoto | Background |
| `klein_slip_structure.py` | Slip dynamics on Klein lattice | Possibly relevant for finite-K corrections |
| `klein_symmetric_coupling.py` | Symmetric coupling regime on Klein | Sets baseline against asymmetric |
| `klein_connection.md` | Connection 1-form on Klein bottle | Relevant for monodromy (N16) |
| `klein_bottle_tower.py` | Tower of Klein bottles | Multi-scale structure |
| `klein_device_exploration.py` | Device-level exploration | Background |

**Critical existing finding** (from `klein_topological_keff.py`):
the Klein bottle's antiperiodic twist makes the standard Kuramoto
order parameter `|r| ≡ 0`. The framework already established
that **sym-only Kuramoto dynamics on Klein bottle do not have a
nontrivial order parameter**. The effective mean field is the
topological invariant `W_x = 1/2`, not a dynamical `|r|`.

This is structurally important for C2: if `|r| = 0` from
sym-only contribution, then the sym/antisym asymmetry might not
manifest as "sym tongue width vs antisym tongue width" — it
might manifest as "topological winding vs dynamical winding"
or "ψ_+ population vs ψ_- population" or similar.

## What's actually missing (the bridge layer)

Given the existing machinery, the **missing piece** is concrete
and well-scoped:

> **A bridge that takes the output of `klein_kuramoto_sweep.py`
> at given K and computes (w_+, w_-) for use in the
> two-component partition formula
> (`omega_b_two_component_sketch.md` Step 3).**

Specifically:
- Run Klein-bottle Kuramoto at K = 1 (or K_STAR, or K-sweep)
- Decompose the lattice's phase configuration into Klein-antipodal
  Z_2 eigenmodes (sym, antisym) — this is well-defined for the
  finite lattice
- Compute the partial-locking weight for each eigenmode
  separately: w_+ from sym population, w_- from antisym
- These (w_+, w_-) are the two-component inputs

The bridge is ~50 lines of code reusing existing primitives.
**Not a structural extension; an integration step.**

## Cross-reference with prior nulls

Six of the seven nulls in `continuity_in_K_nulls.md` interact
directly with this approach:

### N9 — K(t) Friedmann pending S3-S5

The Klein-bottle Kuramoto sweep IS a direct K-axis probe of
substrate dynamics. It doesn't derive K(t) cosmologically (S3-S5
of `k_of_t_friedmann.md` remain pending), but it DOES produce
K-dependent observables on the Klein topology — which is what
S3 (lock fraction F_locked(K) as Ω_m(K)) needs as input.

**Status**: existing Klein-bottle Kuramoto could feed S3
directly. Bridge work needed.

### N10 — K_STAR is coordinate, not synchronization order parameter

The Klein-bottle Kuramoto's `|r| ≡ 0` finding (per
`klein_topological_keff.py`) is the structural reason behind
N10. K_STAR is not a Kuramoto K_c because Klein topology kills
`|r|`. **This null is consistent with the existing Klein-bottle
dynamics, not at odds with it.**

For C2: K_STAR being a coordinate scale (not a running coupling)
means the sym/antisym asymmetry must come from FIXED-K
populations on the Klein-bottle lattice, not from K-running of
the order parameter. Constrains the bridge: should work at
fixed K (e.g., K = 1 or K = K_STAR), not via K-running.

**Status**: refines what the bridge should compute. Not a
blocker.

### N11 — Tongue coverage discontinuity at K=1 (single circle map)

This null was about the STANDARD circle map (S¹ topology). The
Klein-bottle Kuramoto might have **continuous behavior at K=1**
because the topology is different: `|r|` is already 0 for any
K, so there's no discontinuous jump at K=1.

If true, this is a structural advantage of Klein-bottle dynamics
over standard circle map for the C2 probe.

**Status**: needs verification. The `klein_kuramoto_sweep.py`
output at K near 1 should show whether the Klein-bottle case
avoids the standard circle map's discontinuity. **Concrete probe.**

### N14 — Tongue-width convention split (μ vs μ/π)

Klein-bottle Kuramoto uses lattice phases, not continuous Ω, so
the "tongue width" object is differently defined. The 3×3 or
larger lattice has discrete modes labeled by lattice momenta;
sym/antisym refers to those modes' Klein eigenvalues.

**Status**: convention question becomes more concrete (lattice-
mode population vs lattice-mode tongue width); should resolve
N14 in the Klein-bottle case via explicit lattice computation.

### N15-N16 — Phase C halts on DoF and monodromy

The Phase C halt resolved via S_3 orbit dimensions (Phase D, commit
`fa7515f`). The same orbit-counting pattern would apply to the
sym/antisym asymmetry: count the orbits under the Klein
involution and weight by their populations.

**Status**: precedent for the kind of derivation needed.
`klein_within_sector.py`'s framework is closely related.

### N12-N13 — A_s prefactor and α_2 ambiguities

These are about A_s, not Ω_b. Less directly relevant. But the
multi-candidate ansatz pattern they exhibit IS relevant: any C2
closure via the bridge must produce a UNIQUE answer, not
multiple candidates.

**Status**: warning, not blocker.

## What's genuinely new vs derivative

Re-evaluating after the cross-reference:

**Genuinely new** (not in framework):
- The bridge layer connecting Klein-bottle Kuramoto output to the
  two-component partition formula. ~50 lines.
- The interpretation step: showing that lattice-mode populations
  on Klein bottle correspond to (w_+, w_-) in the partition.

**Derivative/integrative** (uses existing machinery):
- Klein-bottle Kuramoto dynamics (klein_bottle_kuramoto.py)
- K-sweep on Klein topology (klein_kuramoto_sweep.py)
- |r| = 0 / W_x = 1/2 substitution (klein_topological_keff.py)
- Within-sector asymmetry mechanism (klein_within_sector.py)
- Two-component partition formula
  (`omega_b_two_component_sketch.md`)

This is a much smaller "new machinery" footprint than I was
assuming. The framework has done most of the building; the
remaining work is integration.

## Sketch of the new probe

Three steps (implementation deferred per user request):

### Step A — Lattice setup

Use `klein_bottle_kuramoto.py` on a `q_2 × q_3 = 2 × 3 = 6`
lattice (the Z_6 fundamental domain). This is the smallest
lattice that captures the Klein-antipodal Z_6 structure of
the Ω partition.

Each lattice site corresponds to one of the 6 Klein-quotient
modes {0, 1, 2, 3, 4, 5} = Z_6.

### Step B — Sym/antisym eigenmode decomposition on the lattice

Klein involution τ acts on the lattice as a specific
permutation. For 2×3 (or related) lattice with Klein BC, τ
maps each site to its antipodal partner.

Decompose the lattice phase configuration `θ(site)` into:
- ψ_+(site) = (θ(site) + θ(τ·site)) / 2 (Klein-singlet)
- ψ_-(site) = (θ(site) − θ(τ·site)) / 2 (Klein-sign-rep)

For singletons (sites where τ·site = site): ψ_+ only.
For pairs: both ψ_+ and ψ_-.

Z_6 has orbits {0}, {3} (singletons) and {1,5}, {2,4} (pairs).
Total: 4 sym modes (2 singletons + 2 from pairs) + 2 antisym
modes (from pairs).

### Step C — Compute (w_+, w_-)

For each eigenmode at given K:
- Run Klein-bottle Kuramoto until equilibrium
- Measure the partial-locking weight (e.g., Kuramoto-style |r|
  computed within the eigenmode subspace)
- Average over sym modes: w_+
- Average over antisym modes: w_-
- Compute asymmetry δ = w_+ - w_-

### Step D — Predict observables

Plug (w_+, w_-) into the two-component partition formula
(`omega_b_two_component_sketch.md` Step 3 with α = β = 1):

```
Ω_b = w_+ / N
Ω_DM = (5 - δ) / N  
Ω_Λ = (11 + 2w_+ - δ) / N
N = 16 + 3w_+ - 2δ
```

Compare predictions to Planck observations.

**Decisive outcomes**:
- If predicted (Ω_b, Ω_DM, Ω_Λ) match Planck within ≤ 1% with
  δ ≈ 0.063 (matching the empirical asymmetry from the sketch),
  the C2 closure is **structurally derived** — Class 5/Survives.
- If δ ≪ 0.063 or wrong sign, C2 mechanism is wrong; back to
  C5 or alternative.
- If δ matches but predictions don't, there's a missing
  third correction; flag and continue.

## The α = β = 1 question

The two-component sketch left (α, β) as free parameters with
(1, 1) as minimal-structural choice. The bridge layer might
RESOLVE this: if the lattice-Kuramoto-derived (w_+, w_-) plug
into a SPECIFIC partition formula (derived from lattice mode
counting), the coefficients (α, β) become forced by the lattice
structure rather than chosen ad hoc.

This is the C2 analog of the down-type Phase D resolution
(commit `fa7515f`): Phase C halted on a coefficient ambiguity;
Phase D resolved it via S_3 orbit dimensions on Z_2 × Z_3.
Same pattern would apply here: orbit dimensions on the Klein
quotient force (α, β).

**Status**: candidate forcing mechanism for (α, β) exists in
the Klein-bottle Kuramoto setup. Would close in conjunction
with the bridge.

## What this changes about the framework's status

If the bridge is built and the probe runs:

- **C2 closure becomes a concrete test**, not a sketch. Either
  closes (Class 5) or surfaces a specific mechanism failure
  (Class 2 with diagnostic).
- **The C5/C2 duality** (per `omega_b_two_component_sketch.md`)
  is testable: if C2 closes structurally, C5 doesn't need its
  own derivation — the same machinery covers both.
- **The framework's Klein-bottle infrastructure** gains a
  load-bearing application beyond its current use in derivation
  audits.

## Recommended next session

The bridge layer is a discrete, well-scoped implementation task:

1. **Read `klein_bottle_kuramoto.py` and `klein_kuramoto_sweep.py`
   carefully** — understand the lattice convention and output
   format.

2. **Implement the eigenmode decomposition** (Step B above):
   define τ for the chosen lattice, build ψ_+ and ψ_- projection
   matrices.

3. **Compute (w_+, w_-)** for K in {K_STAR, 1.0, ...} via the
   eigenmode-projected order parameter.

4. **Plug into two-component partition** (Step D).

5. **Check Planck predictions**.

This is one focused implementation session, ~200-400 lines of
code. Outcome is decisive (closes C2 or surfaces specific
failure).

## What this does NOT solve

Even if C2 closes:
- Anchor count remains two (per `path_a_walkthrough.md`,
  `vocabulary_is_the_work_pattern.md`)
- A_s remains category statement (per `a_s_g1_closure_attempt.md`)
- Cross-sector v/M_P remains independent input
- Shape C obstructions #2-#5 remain to re-audit

C2 closure improves Ω_b specifically; doesn't generalize.

## What this DOES solve (if it works)

- The Ω_b 6.7% Floor as substantive substrate-side closure
  (Class 5)
- The framework's "first remaining substrate-side structural
  gap" per `omega_b_substrate_side_audit.md`
- The C5/C2 duality: structural derivation that covers both
  formulations
- The framework's claim that ALL its dimensionless predictions
  derive structurally (currently has Floor exceptions; this
  removes the largest one)

## Cross-references

- `omega_b_two_component_sketch.md` — the (w_+, w_-) framework
  this implements
- `omega_b_c5_closure.md`, `omega_b_c5_beta_audit.md` — the
  parallel single-w closure with β ansatz
- `continuity_in_K_nulls.md` — N9-N16 nulls cross-referenced above
- `klein_bottle_kuramoto.py` — primary existing machinery
- `klein_kuramoto_sweep.py` — K-sweep on Klein topology
- `klein_topological_keff.py` — `|r| ≡ 0` constraint;
  `K_eff = K_0/2`
- `klein_within_sector.py` — within-sector x↔y asymmetry
  mechanism
- `klein_phase_diagram.py` — phase diagram baseline
- `klein_connection.md` — connection 1-form (relevant for
  N16 monodromy halt)
- `klein_bottle_derivation.md` — foundational Klein-bottle topology
- `down_type_double_cover_phase_d` (commit `fa7515f`) — precedent
  for orbit-dimension forcing of (α, β)
- `baryon_fraction.md` — partition derivation that single-w
  formula came from
- `omega_b_residual_phase_a.md` — three-way inconsistency that
  motivates two-component reading
- `vocabulary_is_the_work_pattern.md` — disambiguation pattern
  in which this probe sits as Instance 8 candidate

## Status

Roadmap complete. Implementation deferred per user request.
Bridge layer is well-scoped (~200-400 lines). Decisive
outcome expected.
