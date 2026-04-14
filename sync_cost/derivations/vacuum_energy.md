# Cosmological Constant in the Framework

## Status (2026-04-09)

The framework addresses the cosmological constant problem on two
levels.

1. **Ω_Λ = 13/19 = 0.6842**, the dark-energy fraction, is derived
   from the Farey partition at scale q₂q₃ = 6: |F_6| = 13 locked
   modes, 6 unlocked modes. Observed value 0.685 ± 0.007. Residual
   0.07σ. See `farey_partition.md`.

2. **The 10¹²¹ problem itself is reframed**, not solved. QFT's
   divergent sum over zero-point energies assumes the torus mode
   spectrum. On the Klein bottle, the XOR filter leaves 4 modes.
   The ratio of configuration-space sizes (torus ~10¹⁸³ modes vs.
   Klein bottle 4) times the frequency scale ratio (Planck / Hubble
   ~10⁶¹) reproduces the observed 121 orders of magnitude as a
   counting statement, not a fine-tuning.

The numerical value Λl_P² ≈ 13⁻¹⁰⁸/12 is self-consistent (solving
the 4-mode fixed-point equation with the tree depth at 19 Hubble
cycles) but not independently predicted.

## The standard problem

QFT sums zero-point energies up to a cutoff Λ_UV:

    ρ_vac = Σ_k (ℏω_k / 2) ∝ Λ_UV⁴

With Λ_UV = M_Pl: ρ_vac ~ 10⁷⁴ GeV⁴.
Observed: ρ_Λ ~ 10⁻⁴⁷ GeV⁴.
Ratio: 10¹²¹.

Standard attempts (SUSY cancellation, anthropic landscape,
quintessence) assume the modes exist and look for a mechanism to
suppress or cancel their contribution by 121 orders of magnitude.

## The Klein bottle reframing

### Configuration space, not cancellation

On a torus (or flat space with periodic BC), modes are indexed by
all integer wavevectors k. Infinitely many, sum diverges.

On the Klein bottle, the self-consistent field equation with XOR
parity selects exactly 4 surviving modes at denominators q=2, q=3
(D19, `klein_bottle.md`). Not 4 per unit volume, not 4 below a
cutoff — 4 total. The excluded modes are not suppressed solutions
or massive states; they are non-functions on the surface.

The vacuum energy is:

    ρ_vac^{KB} = Σ_{i=1}^{4} (ℏω_i / 2) × N_i / V

Finite. No UV divergence. No regularization.

### The 121 orders of magnitude as counting

On the torus, the number of modes up to the Planck frequency in a
Hubble volume is ~(ω_Pl/H₀)³ ~ 10¹⁸³. Each contributes ~ω_Pl of
zero-point energy:

    ρ_vac^{torus} ~ 10¹⁸³ × ω_Pl / V ~ 10⁷⁴ GeV⁴

On the Klein bottle, 4 modes, each at frequency ~H₀:

    ρ_vac^{KB} ~ 4 × H₀ / V ~ 10⁻⁴⁷ GeV⁴

The ratio 10¹²¹ is the ratio of mode counts times the ratio of
characteristic frequencies. The "coincidence" is the difference
between two configuration spaces, not a fine-tuning of parameters.

### Why Λ > 0

The Klein bottle forbids the (0,0) mode (no variation in space or
time). It does not forbid all modes. Four survive. These four have
nonzero frequency and therefore nonzero zero-point energy. Λ = 0
would require no dynamics, which requires the (0,0) state, which
is forbidden. Therefore Λ > 0.

### Why the value is ~H₀²

The 4 mode frequencies are rational multiples ({1/3, 1/2, 2/3}) of
a fundamental frequency ν_Λ = c√(Λ/3). This is self-referential:
Λ enters ν_Λ, ν_Λ sets the mode energies, the mode energies must
sum to Λc²/(8πG). The fixed point of this self-reference is the
observed value.

The cosmological "coincidence" (Λ ~ H₀² today) follows from the
tree depth being ~19 Hubble cycles (D16): the lowest modes on a
Farey tree of depth 19 have denominators up to F₁₉ = 4181, giving
frequencies of order H₀. The epoch sets the resolution; the
resolution sets the modes; the modes set Λ.

## Ω_Λ from the Farey partition

`farey_partition.md` derives:

    Ω_Λ = |F_6| / (|F_6| + q₂q₃) = 13 / (13 + 6) = 13/19 = 0.6842

where |F_6| = 13 is the Farey count at the interaction scale
q₂q₃ = 6. The 13 locked modes at this scale are the dark-energy
fraction; the 6 unlocked are the matter fraction.

Observed: 0.685 ± 0.007. Residual: 0.07σ.

This is independent of the 10¹²¹ reframing. It comes from the
scale q₂q₃ = 6 being the lowest non-trivial Farey count, not from
the Klein bottle's 4 surviving modes directly.

## What the framework claims and does not claim

### Claims (conditional on Klein bottle identification)

- The vacuum energy sum has 4 terms, not 10¹⁸³.
- The sum is finite without regularization.
- The ratio 10¹²¹ is counting, not fine-tuning.
- Λ > 0 because (0,0) is topologically forbidden.
- Ω_Λ = 13/19 independently, from the Farey partition.

### Does not claim

- That Λ is derived from first principles. The 4-mode frequencies
  are expressed in terms of ν_Λ, which is defined in terms of Λ.
  The argument is self-consistent, not predictive of the numerical
  value.
- That the configuration space is demonstrably the Klein bottle.
  D19 marks this as a conjectural identification for the particle
  sector; D20 shows it does not emerge from the continuum frame
  bundle. The reframing stands or falls on this identification.

### Open

- Compute the self-consistent Λ from the 4-mode equation at tree
  depth 19 with the correct denominator conversion. `lambda_fixed_point.py`
  shows the self-consistency closes when q_eff = F₁₉ × (ν_P/H₀),
  which is the Planck/Hubble ratio D16 derives from the operational
  bound. The circularity is explicit.
- Connect the 13/19 Farey derivation to the 4-mode vacuum energy
  derivation. Both give Ω_Λ ≈ 0.685 by different arguments; the
  relation between them is not formalized.

## Summary

The cosmological constant problem in this framework is not a
suppression mechanism. It is a change of configuration space:
from the torus (∞ modes, 10⁷⁴ GeV⁴) to the Klein bottle (4 modes,
10⁻⁴⁷ GeV⁴). The 121 orders of magnitude are the counting
difference between the two. Whether this is the physical
configuration space is open; if it is, the problem dissolves into
a statement about which modes are functions on the surface.
