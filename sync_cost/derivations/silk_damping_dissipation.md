# Silk damping from substrate dissipation

## Status

**Identification, not a new prediction.** This note identifies the
standard-cosmology Silk damping scale (λ_S ≈ 10 Mpc comoving,
ℓ_S ≈ 1500 in the CMB) as a *specific manifestation* of the
framework's universal dissipation invariant at the photon-baryon
coupling scale during recombination. The numerical value is supplied
entirely by standard recombination physics (Thomson scattering,
n_e(z), H(z)) with H₀ and Ω_b as observational inputs; the framework
contributes the structural reading — that this damping length is the
dissipation invariant's address-side rate at the matter sector — not
a new derivation of the damping physics.

It is therefore **not a scorecard claim** and is not entered in
`MANIFEST.yml` or the README predictions table. It makes no framework
integer or dimensionless-ratio assertion, so it is outside the
Class 1–5 numerology taxonomy (`numerology_inventory.md`): there is
no numerical residual to audit. Modal yes / generative
identification-only (see the diagnostic below).

Class: structural identification (phenomenology cross-reference;
no quantitative claim).

---

## Standard cosmology setup

At recombination (z ≈ 1100, T ≈ 3000 K), photons and baryons were
tightly coupled via Thomson scattering. As the universe cooled and
electrons combined with protons, the photon mean free path λ_γ grew
rapidly, eventually exceeding the Hubble radius — the moment of "last
scattering."

During the transition, photons diffused out of overdense regions,
damping density perturbations at scales below the Silk damping length:

    λ_S² ≈ ∫ dt · λ_γ · c / a²

For ΛCDM cosmology with standard parameters, this integral gives

    λ_S ≈ 10 Mpc (comoving)

corresponding to multipole ℓ_S ≈ 1500 in the CMB power spectrum —
where the spectrum's exponential damping begins.

These are standard results; none of the inputs above is a framework
quantity.

---

## Substrate basis: dissipation universality + photon-baryon coupling

The framework's dissipation is the **rank-1 Fréchet algebraic
invariant** (D46, `rank1_temporal_causation.md`; structural source
`born_rule.md` L26–46). Per the scale-stratification audit
(`conservation_scale_stratification_audit.md`), dissipation is the
clean case: its *structure* (the rank-1 factorization of the Kuramoto
map's Fréchet derivative at the synchronized state, which is the arrow
of time) is **algebraic and layer-invariant across all three scales**
(Planck / standard / Hubble); only its *rate* (`K · r · α_k` per
complex dimension) is layer-specific — an address quantity that
varies with the coupling K, mode density, and basin geometry.

The Silk damping length is a specific manifestation of this universal
dissipation at the photon-baryon coupling scale during recombination.

### Composition chain

**Link 1 — substrate dissipation rate at matter scale.** The rank-1
Fréchet structure is universal; its rate at our pocket is fixed by
K = K_STAR ≈ 0.86196 (the standard-scale coupling,
`conservation_scale_stratification_audit.md` L56–58, L120). Algebraic
rate × K_STAR matter-scale coupling = matter-sector dissipation rate.

**Link 2 — photon-baryon coupling.** Photons interact with baryons via
Thomson scattering; the cross-section
σ_T = (8π/3)·(e²/m_e c²)² ≈ 6.65 × 10⁻²⁹ m². This is standard QED
input to the framework — what the framework treats as observational
matter-sector input, not a derived quantity.

**Link 3 — recombination physics.** Electron density n_e(z), Hubble
rate H(z), and recombination duration Δt all come from standard
cosmology with H₀ and Ω_b as observational inputs.

**Link 4 — diffusion integration.** The photon mean free path
λ_γ = 1/(n_e σ_T) increases through recombination; the diffusion
length scales as √(N) · λ_γ where N is the number of scatterings
during the transition.

### Composition

    λ_S ≈ √( ∫ dt · c · λ_γ / a² ) ≈ 10 Mpc (comoving at recombination)

The framework's contribution: identifying this λ_S as the dissipation
invariant's specific rate at the photon-baryon coupling scale during
recombination. Dissipation universality (rank-1 Fréchet) forces *some*
specific damping length given the photon-baryon coupling; standard
recombination physics supplies the inputs that set its value.

---

## MODAL / GENERATIVE diagnostic

- **Modal**: can the framework state the composition? Yes — dissipation
  universality + photon-baryon coupling + recombination physics +
  diffusion integration give λ_S.
- **Generative**: does the framework FORCE the specific value
  λ_S ≈ 10 Mpc? Yes — *given the inputs* (which are observational
  standard-QED + standard-cosmology), the composition derives the
  specific value. But the framework's contribution is **identifying**
  the result as a specific manifestation of substrate dissipation, not
  a new derivation of damping physics. The number is standard
  cosmology's; the reading is the framework's.

---

## Empirical alignment

- **Observed Silk damping scale**: ℓ_S ≈ 1500 in the CMB power
  spectrum (where exponential damping begins); λ_S ≈ 10 Mpc comoving
  at recombination.
- **Framework reading**: the same value, identified as the dissipation
  invariant's photon-baryon-coupling-scale rate.
- **Match**: standard cosmology and the framework reading agree at
  ~10 Mpc by construction; the framework's value is **not** a new
  prediction but a specific instance of substrate dissipation at the
  photon-baryon coupling scale.

---

## Relation to the existing Silk treatment

The framework already addresses Silk damping from a *different,
sharper* angle in `denomination_boundary.md` ("Connection to the CMB"):
there the Silk damping scale is the **denomination boundary** for the
baryon-photon system — acoustic peaks are modes that switched
denomination (entropy-denominated, locked, classical), the damping
tail is modes that hadn't (energy-denominated, unlocked, quantum).
That treatment yields *testable* structure (discrete structure at
rational ℓ-ratios in the damping tail, Farey-fraction peak-height
ratios, a staircase rather than a smooth envelope across the
peak/tail transition).

The two readings are compatible and complementary:

- **This note (dissipation universality)**: identifies the *length
  scale* λ_S as the rank-1 dissipation invariant's address-side rate
  at the photon-baryon coupling scale. Identification only; no new
  testable structure.
- **`denomination_boundary.md` (denomination boundary)**: identifies
  the *boundary itself* as the lock/unlock (entropy/energy
  denomination) transition, and carries the framework's actual
  falsifiable content for the damping tail.

If a falsifiable Silk-damping prediction is wanted, it lives in
`denomination_boundary.md`, not here. This note is the dissipation-side
identification of the same scale.

---

## Cross-links

- `rank1_temporal_causation.md` (D46) — the rank-1 Fréchet dissipation
  structure (arrow of time); the algebraic invariant this note
  instantiates.
- `conservation_scale_stratification_audit.md` — dissipation as the
  clean case: structure layer-invariant across Planck/standard/Hubble,
  rate layer-specific; K_STAR ≈ 0.86196 as the standard-scale rate.
- `born_rule.md` L26–46 — Kuramoto dissipation rate structure
  (`dψ/dt = −γ ∇_ψ* C(ψ)`).
- `denomination_boundary.md` ("Connection to the CMB") — the
  sharper, falsifiable framework treatment of Silk damping as the
  baryon-photon denomination boundary.
- `numerology_inventory.md` — Class taxonomy; this note carries no
  numerical framework claim and so sits outside it (identification,
  not numerology).

---

## One-line summary

The standard-cosmology Silk damping scale (λ_S ≈ 10 Mpc comoving,
ℓ_S ≈ 1500) is identified as a specific manifestation of the
framework's universal rank-1 Fréchet dissipation invariant (D46) at
the photon-baryon coupling scale during recombination — its
address-side rate at K = K_STAR with standard QED (σ_T) and standard
recombination physics (n_e, H, Δt) as observational inputs; the value
is standard cosmology's and the identification is the framework's, so
this is a structural cross-reference, not a new prediction (the
falsifiable framework content for the damping tail lives in
`denomination_boundary.md`).
