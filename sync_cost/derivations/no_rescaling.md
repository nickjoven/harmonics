# No-rescaling principle: cosmic = substrate, under natural units

A methodological commitment, parallel in level to `unitless_check.md`,
`expressibility_split.md`, `comparison_class.md`, and
`wave_particle_substrate.md`. Formalises a structural anticipation
that has been implicit in the framework since the audit landed.

## Claim

Under the framework's natural unit convention (`σ = m = c = 1`,
`L_x = ℓ_P`, `τ_tick = t_P` — `unitless_audit.md`), every framework
prediction relating a substrate-internal rate or ratio to a
cosmological observable is an **identity**, not a proportionality.

    cosmic observable  =  substrate observable    (Planck units)

with **no structural prefactor**. This is what one should anticipate
given the substrate-Planck commitment; it is not an empirical
coincidence. The audit's `κ_pair = 1` Planck volume result is the
flagship instance, but the principle is general.

## The lattice basis (why no rescaling)

The principle is naturally stated in lattice terms. The substrate
hosts several **discrete integer-counted lattices**, and the
framework's cosmic predictions live on the same lattices:

| Substrate lattice | What it counts | Cosmic readout |
|---|---|---|
| **Stern–Brocot tree** | Rational `K = p/q` values; the cascade tree of admissible coupling fixed points | Sequence of cosmic-history K-tokens; `Ω_Λ = 13/19` channel partition |
| **K-zoo / master cascade** | `(d, n, b)` triples giving `K = b^(−n/d)` | Cascade-locked configuration at each epoch; matter equilibrium at `K* = 2^(−3/14)` |
| **Klein-bottle mode lattice** | 4 modes after XOR collapse (`figure_eight.md`) | Particle-physics mode structure (gauge sector, fermions / bosons) |
| **Breather tower** | `N_max = ⌊8π√K⌋` modes per cascade sector (`unitless_audit.md`) | Predicted bound-state count per sector (25 at K=1, 23 at K*, ...) |
| **Arrow-time integer lattice** | `Δτ_arrow = N_events × τ_tick` (`time_axis_split.md`) | Discrete cosmic-clock advance; one tick per Z₂-repair event |
| **Fibonacci depth lattice** | 146 levels from Planck to Hubble (`half_twist_dynamics.md`) | `R_Planck-to-Hubble = 6 × 13⁵⁴` Klein arithmetic |

**Lattice-matched observables are identities.** When a cosmic
observable is integer-counted on one of these lattices, its
substrate counterpart is the same integer count, and the two are
literally equal in Planck units.

This is *why* no rescaling appears: lattices have no continuous
modulus, no overall normalisation, no degrees of freedom that could
be tuned. They are what they are. An integer count is an integer
count. The framework's content is the lattice; the cosmic readout is
the same lattice.

## Examples already in the framework

| Cosmic observable | Substrate equivalent | Identity status |
|---|---|---|
| Hubble rate `H_0` | `⟨Γ_pair⟩_substrate` | ✓ identity (audit pinned `κ_pair = 1`) |
| Cosmic age | `N_events × τ_tick` | ✓ identity at `k = 0` (audit) |
| Planck-to-Hubble ratio | `6 × 13⁵⁴` Klein arithmetic | ✓ identity to sub-percent (`half_twist_dynamics.md`, `unitless_audit.md`) |
| Cosmological constant ratio | `Ω_Λ = 13/19` channel partition | ✓ identity (`half_twist_dynamics.md`) |
| Kink-mass cross-sector ratios | `√K_a / √K_b` | ✓ identity (`master_cascade_identity.md`) |
| Spectral tilt `n_s` | `1 − ln(φ²)/27.4` | ✓ identity (`unitless_check.md`) |
| Weak-mixing angle | `8/35` | ✗ falsified by SM running (`figure_eight.md` disposition flag 1) |
| MOND scale `a_0` | `cH_0/2π` | ✓ identity (`unitless_check.md`) |

The single failed entry (`sin²θ_W = 8/35`) is preserved as a record
of where the principle does not hold — and is the framework's only
currently-known violation, which is itself a falsifier signal.

## Why this is anticipated

Three layers of argument that the principle should hold structurally:

1. **Dimensional analysis under the audit's convention.** In Planck
   units, the only intrinsic substrate scale is Planck. Any framework
   prediction expressible in Planck units is dimensionless by
   construction. A structural prefactor would introduce a hidden
   additional scale, contradicting the audit's substrate-primitives-
   at-Planck commitment.

2. **Lattice match (as above).** Integer-counted observables admit
   no continuous prefactor. Lattice structure forces identity.

3. **Four-object closure** (`wave_particle_substrate.md`). The
   framework permits exactly four objects (mediant + EML +
   half-twist + Klein bottle). A structural prefactor would be a
   fifth element, violating the closure. Rejecting it is forced.

These three are mutually reinforcing: each rules out structural
rescaling for a different reason, and all three agree.

## Practical consequence for new derivations

When a new framework derivation produces a prediction relating a
substrate observable to a cosmological observable, the **first
check** is:

    Does the prediction take the form  cosmic = substrate, identity?

If yes: the derivation is consistent with the no-rescaling principle
and the four-object closure. Mark the prediction contrabass-class.

If no — if a structural prefactor appears — one of three things is
true:

1. The substrate-primitive pinning is wrong (one of `σ, m, c, L_x,
   τ_tick` is not at the Planck scale).
2. The cosmic observable is tuba-class (address-dependent, requires
   anchor).
3. The framework has a fifth-object violation.

Each option is testable. The derivation is not finished until one is
selected.

## Falsifiers

| Test | What would falsify the principle |
|---|---|
| Independent derivation of `\|∇K\|_seam` from substrate Lagrangian | Value significantly different from `≈ 0.365` falsifies `κ_pair = 1` and the no-rescaling principle for the Hubble identity. |
| Cosmic observable requiring non-lattice description | If any precision cosmological observable is structurally non-rational and not expressible in `{integer, φ, π, e, √n}`, the framework's natural-irrationals set is incomplete and the lattice claim fails. |
| Fifth-object structural prefactor required | If any framework prediction can only be expressed with a structural prefactor beyond the four objects, both the no-rescaling principle and the four-object closure fail. |
| New observation outside the framework's lattice support | A cosmic observable whose precision value cannot be expressed on any framework lattice — neither Stern-Brocot, nor K-zoo, nor Klein mode, nor Fibonacci-depth — falsifies the framework's lattice coverage. |

## What to keep an eye out for

When examining a new derivation, three lattice-related diagnostics
that signal whether the principle holds:

1. **Integer counts.** If a quantity is an integer (e.g., `N_breathers`,
   token positions, mode counts), the lattice reading applies and no
   rescaling is anticipated. Confirm the integer matches a substrate
   lattice.

2. **Small-prime + `{φ, π, e, √n}` decomposition.** If a quantity is
   a rational of small primes times one of the framework's natural
   irrationals, the lattice reading still applies. Confirm the
   decomposition.

3. **Structurally-non-lattice quantities** (continuous parameters
   not derivable from the substrate's lattices) signal **tuba-class**
   observables — they are anchors, not framework predictions. Treat
   accordingly.

The framework's empirical content is **only the lattice-derivable
observables**. Everything else is anchor or fitting and not the
framework's claim.

## Status

Class 3 (methodological), parallel to `unitless_check.md`,
`expressibility_split.md`, `comparison_class.md`,
`wave_particle_substrate.md`.

The principle is a consequence of the substrate-primitives-at-Planck
convention (`unitless_audit.md`) plus the four-object closure
(`wave_particle_substrate.md`), not an additional postulate.
Formalising it makes explicit a commitment that was already implicit
in those two pieces — and provides a single check applicable to any
new framework derivation.

The principle was articulated structurally during the audit's
`κ_pair = 1` decision; this doc registers it as the framework's
canonical anticipation.

## Cross-links

- `unitless_audit.md` — the audit that pinned substrate primitives
  at Planck scale and committed to `κ_pair = 1`, the principle's
  flagship instance.
- `unitless_check.md` — parent methodological doc on unit
  invariance; this doc extends to the *content* of predictions
  beyond just unit choice.
- `wave_particle_substrate.md` — the four-object closure that
  rules out fifth-object structural prefactors.
- `expressibility_split.md` — the lambda / EML split that produces
  the framework's natural irrationals `{φ, π, e, √n}`, the
  permitted non-integer content of lattice observables.
- `medium_change_demo.md` — the contrabass-class / tuba-class
  partition that this doc's "framework observables vs. anchor
  observables" distinction depends on.
- `master_cascade_identity.md` — the K-zoo lattice on which several
  identity examples sit.
- `half_twist_dynamics.md` — `R_Planck-to-Hubble = 6 × 13⁵⁴` is the
  cleanest single instance of the no-rescaling identity at
  sub-percent precision.
- `time_axis_split.md` — the arrow-time integer lattice; identity
  reading of `N_events × τ_tick = cosmic-age`.
- `figure_eight.md` — Klein-bottle mode lattice (4 modes after XOR
  collapse), the framework's particle-sector lattice; also home of
  the only-known-falsified identity (`sin²θ_W = 8/35`,
  disposition flag 1).
- `framework_status.md` — registry of contrabass-class observables
  to which this principle applies.
