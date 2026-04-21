# Anchor-count audit: single vs multiple observational anchors

T4 claim test. The recent cleanup to `hierarchy_gaussian_lattice.md`
asserted: "one dimensional anchor, propagated via exact framework-
internal dimensionless ratios to all other dimensional scales." This
audit checks the claim against the repo's actual dimensional
predictions.

## Method

1. Enumerate framework predictions that have dimensional content.
2. For each, identify which observational anchor it is tied to.
3. Check whether a framework-derived dimensionless identity links
   that anchor to the claimed single anchor.
4. Verdict: one anchor, two anchors, or more.

## Enumeration

### Cosmological sector (anchor: H_0)

| Quantity | Identity | Derived from H_0? |
|---|---|---|
| L_H = c/H_0 | definition | yes (c is convention) |
| t_H = 1/H_0 | definition | yes |
| t_P = t_H / R, R = 6·13⁵⁴ | framework integer | yes |
| ℓ_P = L_H / R | consequence | yes |
| Λℓ_P² = 13⁻¹⁰⁸/12 = 3/R² | framework identity | yes (→ Λ) |
| M_P (natural units) = 1/ℓ_P | ℏ = c = 1 convention | yes |
| ρ_crit = 3H₀²/(8πG) | standard cosmology | yes (G from ℓ_P) |
| Ω partition 13:5:1/19 | combinatorial | dimensionless, no anchor needed |

Cosmological sector: **closes with one anchor (H_0)** + conventions.

### Particle sector (anchor: v_EW = 246 GeV)

Directly from `coupling_scales.md:231`:

| Quantity | Status | Source |
|---|---|---|
| v = 246 GeV | **Not derived** | Single dimensionful input |
| ℏ (absolute) | Not derived | Requires v |
| c (absolute) | Not derived | Requires v |
| G (absolute) | Not derived | Requires v |

Also from `address_and_quantity.md:52`, `higgs_from_tongue_boundary.md:354`,
`mass_sector_closure.md:172`, `gauge_sector_lovelock.md:426`: the
framework's particle sector consistently declares v = 246 GeV as the
single dimensionful input.

Dimensionless content of the particle sector (all framework-derived):

- α_em ≈ 1/137 from q_2³ + q_3³ = 35
- α_s / α_2 = q_3³/q_2³ = 27/8
- sin²θ_W = 8/35
- m_H / v = 1/q_2 = 1/2
- λ_Higgs = 1/(2 q_2²) = 1/8
- generation mass ratios from tongue geometry
- CKM angles from SL(2,ℤ) traces

Particle sector: **closes with one anchor (v_EW)** for absolute masses.
All dimensionless couplings/ratios are framework-derived.

### Link between sectors

This is the crux. Is there a framework-derived dimensionless identity
connecting v_EW to H_0 (or Λ, or ℓ_P)? Specifically: is v_EW / M_P
a framework-predicted pure number?

Observed: v / M_P = 246.22 GeV / 1.2209×10¹⁹ GeV = **2.017×10⁻¹⁷**.
In Fibonacci-φ² units: log_{φ²}(v/M_P) ≈ −39.94.

Searched the repo for an identity v / M_P = f(framework integers):

- No documented derivation found.
- `hierarchy_gaussian_lattice.md` links Λ ↔ ℓ_P via R (cosmological
  to Planck scales), but does NOT extend to v_EW.
- `coupling_scales.md` explicitly lists v as "Not derived" and notes
  ℏ, c, G "Require v" in absolute units.
- `planck_scale.md` notes "145.8 Fibonacci levels span the Planck-to-
  Hubble hierarchy" but no corresponding count for Planck-to-EW.

Suggestive numerology (not a derivation):

- φ⁻⁸⁰ = 1.91×10⁻¹⁷ → ratio 0.947 vs v/M_P (5.3% off)
- **13⁻¹⁵ = 1.954×10⁻¹⁷** → ratio 0.969 vs v/M_P (**3.1% off**)

The 13⁻¹⁵ match is interesting: 15 = q_3 · F_5, and 13 = |F_6| is
the framework's DE-sector integer. But this is numerology — no
structural derivation of v/M_P = |F_6|⁻ᵠ³ᶠ⁵ is in the repo. If it
existed, it would close the anchor gap (and incidentally solve the
hierarchy problem at ~3% residual, matching the C2 floor magnitude).

## Verdict

**The framework has TWO independent observational anchors:**

1. **Cosmological anchor**: H_0 (equivalently Λ_SI, ℓ_P, or M_P).
   Covers: Λ, ℓ_P, t_P, M_P, ρ_crit, cosmic-timeline scales.

2. **Particle-physics anchor**: v_EW = 246 GeV.
   Covers: ℏ, c, G in absolute units (i.e., tied to particle-physics
   mass scales), all absolute lepton/quark/gauge-boson masses, m_H.

The T4 cleanup's language was a step in the right direction (moving
from "absolute scale derived from nothing" to "one anchor propagated
via ratios"), but it still overstates slightly. The framework's
actual anchor count under current documented derivations is **two**,
not one.

## Consequence for T4 language

`hierarchy_gaussian_lattice.md` line 108–110 says:

> Given that single anchor, every other dimensional scale
> (ℓ_P, t_P, M_P, **v_EW**) follows by the framework's dimensionless
> identities.

The inclusion of v_EW here is incorrect given the current repo state.
v_EW is *not* derived from H_0 or Λ via any documented dimensionless
identity. The sentence should be softened or v_EW removed.

Similarly, any claim that the framework has "zero free parameters
except one anchor" should be restated as "zero free parameters
except two anchors (one cosmological, one particle-sector)."

## Path to closing the gap

The framework would reduce to a single anchor if one of:

1. **A framework-derived dimensionless identity v/M_P = f(integers)**
   is found. The 13⁻¹⁵ near-match at 3.1% is suggestive but not
   derived; if someone can produce a combinatorial / topological
   argument for v/M_P = 13⁻¹⁵ exactly (or with a structural
   correction), that closes the anchor gap. This would be a
   *hierarchy-problem solution* in framework terms.

2. **v_EW reinterpreted as a pure number (framework-native)** rather
   than a separate scale. E.g., if the root oscillator frequency ω_0
   = v_EW/ℏ is pinned by framework structure independently, then v
   becomes a derived quantity. Not yet done.

3. **Framework restricts to one sector at a time.** Accept two-anchor
   status as honest; re-state "zero free parameters" as sector-specific.

## Status

The anchor-count audit concludes: the framework currently has **two**
independent observational anchors (H_0 and v_EW), with a suggestive
but underived numerical near-match at v/M_P ≈ 13⁻¹⁵ (3.1% off). The
T4 language should be softened accordingly, and the missing link is
a concrete structural open item — effectively the hierarchy problem
posed framework-natively.

## Cross-references

| File | Role |
|---|---|
| `coupling_scales.md` §IV | explicit "v = 246 GeV Not derived" table |
| `address_and_quantity.md` | "single dimensionful input" phrasing |
| `hierarchy_gaussian_lattice.md` §Consequences | T4 update (slightly overstated) |
| `higgs_from_tongue_boundary.md` | v = 246 GeV as the only dimensionful input |
| `mass_sector_closure.md` | same, restated |
| `planck_scale.md` | 145.8 Planck-to-Hubble Fibonacci levels, but no Planck-to-EW count |
| `h_inf_status.md` | scale-free reframe declares one anchor; this audit shows two |
