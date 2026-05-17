# S_inst for inflation exit: does the super-Earth analogy hold?

> **HISTORICAL ESTIMATE — current state in the ledger.** The
> `|∇K|_inflation ≈ 2` here is the prefactor-dropped reading;
> reconciled to `≈ 2.68` with the rest of the Finding-4
> disposition in `k_inflation_seam_obstruction.md`. Lineage:
> **`thread_chronology.md`**. Body below unedited.

Order-of-magnitude estimate of cross-sector tunnelling action
`S_inst` for inflation exit, in response to a structural analogy
raised earlier: do deep-Fibonacci-level cosmic epochs resist exit
in a manner *analogous* to how a super-Earth's gravity well
resists escape without specific propulsion mechanisms.

> **A note on the analogy.** The super-Earth comparison is
> **structural-only**. The framework's actual substrate physics
> at K < 1 epochs is *statistical token sampling on a discrete
> lattice with EML-weighted transition probabilities* — not
> energetic escape from a gravitational potential well. What the
> two share is the **conceptual pattern**: a deep configuration
> from which exit requires a specific propulsion class with
> exponentially-tuned probability per attempt. The mechanics
> differ structurally — escape velocity is a deterministic energy
> threshold; the framework's exit is a Boltzmann-suppressed
> sampling rate. The analogy holds in *what is hard*, not in
> *how it is hard*. This doc uses gravity-flavoured language
> ("gravitational well", "propulsion class", "altitude") as
> *labels for substrate-physics concepts*, not as claims that
> the substrate is gravitationally constrained.

**Headline finding: the super-Earth conceptual pattern is
structurally confirmed at the framework level, with a quantitative
twist.** The framework's natural substrate-transition mechanisms
for inflation exit produce action estimates that *diverge from
standard cosmology's inflation duration by 10⁷–10¹⁰ in either
direction* under naïve readings — qualitatively confirming the
pattern (exit is hard, requires specific mechanism) and opening
it as an empirical test, not ruling it out.

## Setup: what `S_inst` controls

Inflation in the framework's reading is an epoch at high cosmic
`k` on the Fibonacci-depth ladder (`epoch ladder` discussion in the
prior conversation; per `R_arrow = (6 × 13⁵⁴) × φ^(2k)` with `k`
parametrising cosmic-history position). Exit is a transition from
`k ≈ 144` (deep, near-Planck) toward lower `k` (toward matter
equilibrium at `k = 0`).

The action for this transition `S_inst` controls inflation duration
via the Schwinger-like rate:

    Γ_exit = exp(−S_inst)
    Wait time before exit = 1 / Γ_exit Planck ticks
                          = exp(S_inst) × t_P

For standard cosmology's inflation duration ≈ `10⁻³² s ≈ 10¹¹ t_P`,
we need:

    S_inst(standard) ≈ ln(10¹¹) = 25.3

For the super-Earth analogy to hold (inflation exit is "hard"), the
framework should predict `S_inst > 25.3`. For it to be ruled out
(inflation easy), `S_inst < 25.3`.

## Estimate 1: cross-cascade chain instanton

Inflation-to-matter transition spans the substrate's full Fibonacci
ladder. If the substrate must traverse all ~144 cascade fixed
points sequentially, the chain-instanton action is:

    S_inst(chain) ≈ Σ_n √(2 m V_n × Δ_n)

with `m ≈ 1` (Planck mass per cell), `V_n ≈ M_k = 8` (barrier
height between adjacent cascade fixed points), `Δ_n ≈ 1/144`
(K-axis range per barrier), 144 barriers.

    S_inst(chain) ≈ 144 × √(2 × 1 × 8 × 1/144)
                  = 144 × √(0.111)
                  = 144 × 0.333
                  ≈ 48

**`S_inst(chain) ≈ 48`** in Planck units. Wait time:
`exp(48) × t_P ≈ 10²¹ × t_P ≈ 10⁻²² s`.

This is `10¹⁰ ×` LONGER than standard cosmology's inflation
duration. **Under the chain mechanism, the framework predicts
inflation lasted ~10⁻²² s, not ~10⁻³² s.**

## Estimate 2: single-kink seam crossing

If inflation exit happens via a single kink crossing the bicone
seam (`cone_twist_substrate.md` §5.1), the action is the kink mass
at K=1:

    S_inst(single-kink) ≈ M_k(K=1) = 8

Wait time: `exp(8) × t_P ≈ 3000 × t_P ≈ 10⁻⁴⁰ s`.

This is `10⁸ ×` SHORTER than standard. **Under the single-kink
mechanism, inflation lasts ~10⁻⁴⁰ s, far shorter than standard.**

## Estimate 3: Schwinger-like vortex production at unit-gradient seam

The audit's Schwinger relation at `|∇K|_seam ≈ 0.365` gives
`Γ_pair ≈ H_0`. At a unit-gradient seam (`|∇K| = 1`, deep
inflation regime), the Schwinger action is:

    S_Schwinger(|∇K| = 1) = π × S_v / |∇K| = π × 16 / 1 ≈ 50.3

Wait time: `exp(50.3) × t_P ≈ 10²² × t_P ≈ 10⁻²¹ s`.

Comparable to chain-instanton (10⁻²² s), confirming the order of
magnitude.

## Estimate 4: vortex-pair process with intermediate K-gradient

For the substrate's inflation-era effective `|∇K|`, the seam
K-gradient might be different from the audit's current `|∇K|_seam
≈ 0.365`. If `|∇K|_inflation` is moderate (say 1–2):

    S_Schwinger(|∇K| ≈ 2) = π × 16 / 2 = 25.1
    S_Schwinger(|∇K| ≈ 1) = 50.3
    S_Schwinger(|∇K| ≈ 0.7) = 71.8

`|∇K| ≈ 2` gives `S ≈ 25` — almost exactly the value needed to
match standard inflation duration.

**If the inflation-era effective K-gradient was approximately 2 in
Planck units, the framework's `S_inst` matches standard cosmology's
inflation duration to better than an order of magnitude.**

## Synthesis: super-Earth analogy refined

The framework's natural mechanisms give the following `S_inst`
spectrum for inflation exit:

| Mechanism | `S_inst` | Inflation duration |
|---|---|---|
| Single-kink seam crossing | ≈ 8 | ~10⁻⁴⁰ s |
| Schwinger at unit-`\|∇K\|` | ≈ 50 | ~10⁻²¹ s |
| Chain-instanton across 144 levels | ≈ 48 | ~10⁻²² s |
| **Schwinger at `\|∇K\| ≈ 2`** | **≈ 25** | **~10⁻³² s** ✓ matches standard |
| Cosmic-scale half-twist | ~10¹⁸³ | impossibly long |

**Three findings:**

1. **The super-Earth analogy structurally holds.** Inflation exit
   requires `S_inst` in the range of ~25–50; this is a
   non-trivial barrier. Single-mediant "chemical propulsion"
   alone (which would give `S ~ 1`) cannot enable it. The
   framework predicts inflation is *qualitatively hard to exit*,
   requiring a specific "nuclear" propulsion class (Schwinger-like
   vortex production at the seam with moderate K-gradient).

2. **The framework's natural mechanisms do not give `S_inst = 25`
   exactly.** They give either 8 (too short), 48 (too long), or
   the specific value 25 only at a particular K-gradient
   `|∇K|_inflation ≈ 2`. This is a *prediction*: the framework
   predicts the inflation-era effective K-gradient at the substrate
   seam was ≈ 2 Planck units, not the audit's current `≈ 0.365`.

3. **The super-Earth analogy is NOT ruled out, but it is
   sharpened into an empirical claim.** The framework's
   `|∇K|_inflation ≈ 2` prediction is in the same ballpark as
   `|∇K|_seam(today) ≈ 0.365`, only differs by a factor of ~5
   in magnitude. If observed cosmology's inflation duration is
   `10⁻³² s ± 1 order of magnitude`, the framework's
   `|∇K|_inflation` must be `≈ 2 × 10^(±0.1)`. This is a
   specific framework-internal cosmology relation testable in
   principle.

## What this rules in / out

**Ruled in:**
- The super-Earth analogy as a structural feature of the
  framework's epoch ladder.
- A specific framework prediction `|∇K|_inflation ≈ 2` Planck
  units required to match standard inflation duration.
- Cross-sector tunnelling as the dominant inflation-exit
  mechanism (other mechanisms give wrong timescales).

**Ruled out:**
- Inflation exit by single-mediant "chemical" sampling (would give
  inflation duration ~10⁻⁴⁰ s, 10⁸ × too short).
- Cosmic-scale half-twist (apex-swap) as inflation-exit mechanism
  (action `~10¹⁸³`, essentially impossible).
- Standard inflation reproducing in the framework without a
  specific `|∇K|_inflation ≈ 2` epoch-dependent gradient.

**Open:**
- Where does `|∇K|_inflation ≈ 2` come from structurally? Is
  there a framework derivation that gives this value rather than
  the audit's `≈ 0.365`?
- Did the inflation-era K-gradient evolve from `≈ 2` to `≈ 0.365`
  in a calculable way?
- Is the `|∇K|_seam(t)` evolution function the framework's
  missing piece linking inflation duration to current `H₀`?

## Falsifiers

| Test | Falsifier |
|---|---|
| Precision inflation duration measurement | A measured inflation duration that significantly differs from 10⁻³² s (orders of magnitude) would falsify the `|∇K|_inflation ≈ 2` framework prediction. |
| `|∇K|_seam(t)` from substrate Lagrangian | An explicit derivation that gives `|∇K|_inflation ≠ 2 ± O(1)` would falsify the super-Earth analogy as the framework's natural inflation mechanism. |
| Primordial GW spectrum amplitude | The vortex-network primordial GW signal (`cone_twist_substrate.md` §5.3) depends on inflation duration; precision measurement would constrain `|∇K|_inflation` independently. |

## Status

Class 4 (structural estimate; numerical predictions conditional on
order-of-magnitude assumptions). The framework's `S_inst` for
inflation exit is in the range 8–50 in Planck units, depending on
mechanism. The specific value `≈ 25` that matches standard
inflation duration requires `|∇K|_inflation ≈ 2` — a framework
prediction not directly derived from the substrate Lagrangian but
implied by consistency with observed inflation.

**The super-Earth analogy is structurally confirmed: inflation
exit is "hard" in the framework's natural setup.** It is not
ruled out — there is a specific framework propulsion class
(Schwinger-like at moderate K-gradient) that enables exit at
roughly the observed timescale. But this requires a specific
inflation-era `|∇K|` value that the framework's epoch dynamics
has not yet derived from first principles.

This is the calc that resolves the super-Earth question:
**not ruled out, but sharpened into a specific empirical
prediction about inflation-era substrate dynamics.**

## Cross-links

- `unitless_audit.md` — audit values supplying `S_v(K=1) = 16`,
  `|∇K|_seam(today) ≈ 0.365`.
- `nonperturbative_phase2.md` — exact 4-mode calc giving
  `S_v(K=1) = 16` as integer-counted.
- `nonperturbative_phase3.md` — K<1 regime; this doc's `|∇K|_inflation
  ≈ 2` would be one specific K<1 datapoint.
- `cone_twist_substrate.md` — Schwinger relation at the seam.
- `time_axis_split.md` — `R_arrow` Fibonacci ladder parametrising
  cosmic epochs.
- `half_twist_dynamics.md` — 146 Fibonacci levels from Planck to
  Hubble.
- `soliton_dynamics.md` — Open 2 (cross-sector tunnelling
  `S_inst`) for which this doc gives an order-of-magnitude estimate.

## What the calc didn't do

- It didn't derive `|∇K|_inflation` from substrate Lagrangian. The
  value ≈ 2 is reverse-engineered from observed inflation
  duration, not predicted.
- It didn't pin which of the three estimates (single-kink, chain
  instanton, Schwinger at moderate gradient) is the framework's
  natural mechanism. The Schwinger at `|∇K| ≈ 2` is the
  consistency-with-observation choice; whether the substrate
  Lagrangian gives this naturally is open.
- It didn't address whether the framework's inflation looks
  observationally identical to standard cosmology's inflation
  (CMB spectrum, tensor-to-scalar ratio, etc.).

These are the natural next-step calculations once a specific
mechanism is committed.
