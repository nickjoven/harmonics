# Equivalence dissolution

## Status

**Inviolable-companion dissolution articulated** — the equivalence
principle (weak + strong) reduces to a substrate identity on the
framework's apparatus. Not a new derivation; a synthesis of
ingredients already in the corpus.

The substrate Lagrangian has one mass parameter `m` per mode, used
twice — as the kinetic coefficient and as the sync-cost coupling.
Inertial mass and "gravitational" mass cannot be distinct because
the framework offers only one slot for them.

No new primitive.

---

## The statement

**Claim (equivalence dissolution).** On the framework's substrate
the equivalence principle is not a postulate but a near-tautology:
the inertial mass and the gravitational mass of any mode are the
same symbol entering the same Lagrangian. Local Lorentz invariance
(the metric piece of strong equivalence) follows separately from
the `(3,1)`-signature derivation. Together, weak and strong
equivalence are consequences of substrate structure, not
independent empirical inputs.

The dissolution is structural, not numerical: it removes the
*identity* claim (`m_inertial = m_gravitational`) from the import
ledger and lands it as a substrate identity. The *magnitude* of
gravity (Newton's `G`, the cosmological scale) remains anchor-
declined per the Basepoint Principle (`no_rescaling.md`).

---

## Derivation

### Step 1 — One mass per mode in the substrate Lagrangian

The framework's substrate is an inertial Kuramoto chain (and its
higher-dimensional embeddings; `dispersion_K1.py` derives the
wavefront speed `c = √(K/m)` from this Lagrangian). The mode
Lagrangian is, schematically,

    ℓ[θ] = (m/2)(∂_t θ)² − (K/2)(∂_x θ)² − V(θ)
            ────────────  ─────────────
              kinetic       coupling/sync

with `m` the inertia of one oscillator at the root level
(`coupling_scales.md:94`) and `K` the local stiffness/coupling
strength to nearest neighbours (`framework_lagrangian.py`). The
framework carries *one* parameter `m`; the corpus has no second
parameter for "gravitational response" coexisting with it.

Independently, `mass_entrained_measure.md:68` identifies *mass =
synchronization cost* in the static / equilibrium sector — the
cost of forcing this mode into the locked configuration. The two
readings are not "matched"; they are the same `m` viewed once on
the kinetic side and once on the sync-cost side.

### Step 2 — Weak equivalence is the LHS/RHS identity of step 1

Weak equivalence: any two bodies fall the same in a gravitational
field, independent of mass. In the substrate Lagrangian the
Euler–Lagrange equation reads

    m ∂_t² θ  =  K ∂_x² θ − V'(θ) + (substrate-distortion source)

with the substrate-distortion source proportional to the *same* `m`
on both sides (because the distortion couples through the kinetic
term to the mode, and the kinetic term carries `m`). Dividing
through by `m`:

    ∂_t² θ  =  (K/m) ∂_x² θ − V'(θ)/m + (distortion)/m

The right-hand side's dependence on `m` is what makes the trajectory
*independent* of the particular `m`: the distortion enters scaled by
`1/m`, the inertial response divides by `m`, and the two cancel
identically in the geodesic.

Weak equivalence is the *cancellation*, not a coincidence to be
explained. Equality of inertial and gravitational mass is the
statement that "the `m` on the left of the EOM is the same `m`
that scales the distortion source" — which is just the statement
that the Lagrangian has one `m`, not two.

### Step 3 — Strong equivalence: local Lorentz from `(3,1)`

Strong equivalence: locally, gravity is indistinguishable from
uniform acceleration; physics in a freely-falling frame looks
locally inertial. This requires (a) the inertial-gravitational
identity (step 2) **and** (b) local Lorentz invariance.

Part (b) is supplied separately by the framework's `(3,1)`-
signature derivation (`minkowski_signature.md`): at every substrate
point the tangent algebra is `Cl(3,1)`, with `SL(2,ℂ) ≅ Spin(3,1)`
as the local Lorentz group (`one_chain.py` ≈ L267). The substrate's
locally-Minkowski character is a derived consequence of the four
phase states {A, B, C, D} minus the single dark state, not an axiom
introduced for this purpose.

Combined with step 2, strong equivalence reduces to two derived
statements on the framework's substrate. Neither is postulated.

---

## What this says (and what it does not)

It **says**:

- The equivalence principle is structurally trivial on this
  substrate: one Lagrangian, one `m`, used twice.
- The `(3,1)` derivation supplies the local-Lorentz piece of strong
  equivalence without further input.
- No experimentally observable violation of universality of free
  fall is predicted *at scales where the single-`m` Lagrangian is
  the right description.*

It does **not** say:

- That the framework predicts gravity. The substrate gives the
  *structure* of equivalence; the absolute magnitude of gravitational
  coupling (Newton's `G`, the cosmological scale, the absolute mass
  values) remains anchor-declined per the Basepoint Principle.
- That MOND-regime departures from Newtonian universality violate
  equivalence. At accelerations below the MOND scale
  `a₀ = cH₀/(2π)` (Survives in `free_parameter_scorecard.md`), the
  system's self-measurement of which attractor it belongs to
  becomes fidelity-limited (`fidelity_bound.md`). Apparent
  equivalence deviations in the MOND regime are a *measurement*
  effect on a substrate where equivalence still holds exactly —
  not a true violation.
- That the framework derives the Einstein field equations or the
  geodesic-from-curvature picture. Those remain open, in the same
  column as the magnitude of gravity.

This is the same discipline the framework applies elsewhere: derive
*form* (Born exponent `= 2`, `(3,1)` signature, equivalence), decline
*scale* (absolute amplitudes, Planck mass, Newton's `G`).

---

## Distinct from the magnitude problem

The framework dissolves the *identity* equivalence `m_i ≡ m_g`, not
the *magnitude* of gravity. Newton's `G`, the cosmological scale,
the absolute mass values — all remain anchor-declined.

In the corpus's existing taxonomy this is the same status as the
Born exponent: the exponent `= 2` is forced (`figure_eight.md`, via
`J² = −I`); the absolute amplitudes of wavefunctions are not. Here
the structural identity `m_i ≡ m_g` is forced (single-Lagrangian
parameter); the absolute mass values are not.

---

## Exhibited consequences

- **Universality of free fall** is structurally trivial; no
  fine-tuning is required to explain it.
- **The Einstein-elevator argument** is a tautology on the
  framework's substrate: a freely-falling frame is exactly a frame
  in which the substrate distortion's contribution to the EOM
  vanishes because `m` divides through identically.
- **Geodesic motion = free trajectory under sync-cost coupling**:
  the geodesic is the trajectory that extremizes sync cost along
  the path, with `m` entering identically on inertial and coupling
  sides.
- **One pillar of GR-QM unification is in place**. The Tier-C
  capstone (`lesson_epr_gr_qm_unification.md`) rests on two pieces:
  this equivalence dissolution (the GR side) and the EPR/Bell
  assembly (`epr_bell_assembly_theorem.md`, the QM side). The
  capstone becomes writable when both pieces are this consolidated.

---

## Falsifiers

- **Direct violation of universality of free fall above the MOND
  threshold.** A measured composition-dependent acceleration ratio
  `η = (a_A − a_B)/a > 0` between bodies `A` and `B` in the same
  gravitational field, at accelerations `a > a₀`, would falsify the
  single-`m` identification. Current bounds: MICROSCOPE's final
  result (Touboul et al. 2022) constrains the Eötvös parameter at
  the `10⁻¹⁵` level with no violation observed — consistent with
  this doc. Any positive `η` at that sensitivity, at high
  acceleration, would void step 2.
- **Failure of local Lorentz invariance.** A measured Lorentz
  violation at substrate scales would void step 3 and the
  strong-equivalence dissolution along with it. Step 3 inherits
  the `(3,1)`-derivation's falsifiers as listed in
  `minkowski_signature.md`.
- **A second mass parameter.** A demonstration that the substrate
  Lagrangian *must* carry two independent mass parameters — one
  kinetic, one for substrate-distortion response — at any scale,
  would void the single-`m` identity. Introducing a second
  independent parameter would require a new substrate primitive,
  which inviolable #4 (two-primitive closure,
  `substrate_determinism.md`) prohibits without a derivation that
  the new primitive is itself derived.
- **MOND-regime departure that is *not* fidelity-limited.** An
  observed MOND-regime deviation whose magnitude or pattern is
  *inconsistent* with the `fidelity_bound.md` self-measurement
  framing — for example, a residual that depends on body
  composition rather than on the attractor-identification scale —
  would force the apparent deviation back onto the equivalence
  ledger as a true violation, voiding the "measurement effect"
  reading offered above.

---

## Why this matters

The equivalence principle had been sitting unmarked on the import
ledger: a structural postulate the framework consumed without
comment, in the same column as the Hilbert-space formalism or the
Born exponent before its derivation. This doc moves it to the
derived column, where it sits on already-installed apparatus
(`(3,1)` signature, single-`m` Lagrangian, sync-cost-as-mass).

It also clarifies the framework's relationship to MOND. The MOND
scale is *not* an equivalence-principle anomaly to be explained
away; it is a fidelity-bound limit on the system's self-measurement
of attractor membership, riding on a substrate where equivalence
holds exactly. That distinction matters because it directs the
MOND-derivation work to `fidelity_bound.md`'s self-referential
apparatus rather than to a modification of the gravitational
coupling.

Class: foundational consolidation (Class 3, articulation). The arc
closed is the unstated reliance on equivalence across the
framework's gravitational and inertial readings.

---

## Cross-links

- `substrate_determinism.md` — the 10 inviolables; this dissolution
  is consistent with #2 (no-rescaling) and #4 (two-primitive
  closure, which prohibits introducing a second mass parameter).
- `mass_entrained_measure.md:68` — *mass = synchronization cost*;
  the static-side reading of the single `m`.
- `coupling_scales.md:94` — *the mass `m` is the inertia of one
  oscillator at the root level*; the kinetic-side reading.
- `dispersion_K1.py` — *inertial Kuramoto chain*; the substrate
  Lagrangian's wavefront-speed derivation `c = √(K/m)`.
- `framework_lagrangian.py` — the Lagrangian's formal definition,
  containing `(m/2)(∂_t θ)²` explicitly.
- `minkowski_signature.md` — the `(3,1)`-signature derivation; the
  metric piece of strong equivalence.
- `one_chain.py` (≈ L267) — `SL(2,ℂ) ≅ Spin(3,1)` local-Lorentz
  identification used in step 3.
- `no_rescaling.md` — inviolable #2; the magnitude side of gravity
  remains anchor-declined.
- `fidelity_bound.md` — the apparent MOND-regime equivalence
  deviation as a self-measurement effect, not a violation.
- `free_parameter_scorecard.md` — `a₀ = cH₀/(2π)` is Survives; the
  MOND scale enters as a substrate-derived rate, not as a new
  mass parameter.
- `q_mod2_conservation_theorem.md` — companion inviolable-companion
  doc; same house style.
- `lesson_epr_gr_qm_unification.md` — Tier-C capstone; this
  dissolution is one of the two pieces of GR-QM unification.
- `epr_bell_assembly_theorem.md` — the EPR-side piece of the same
  capstone.

---

## One-line summary

There is one `m` in the substrate Lagrangian, used twice — as
inertia and as sync-cost coupling — so the equivalence principle is
not a principle but an identity, and the `(3,1)`-signature
derivation supplies the metric piece of strong equivalence without
further input.
