# Unitless Check: ℏ = G = c = 1

A single-page demonstration that the framework's predictions are invariant under unit choice. Pedagogical companion to the Tier 5 "address" discussion.

## Claim

The independent values of ℏ, G, and c are conventions of the meter–kilogram–second system. They are not three separate inputs to the framework. Re-running every derivation with ℏ = G = c = 1 (Planck units) leaves every prediction unchanged.

## Why this is the test

A free parameter is something that, if changed, changes a prediction. If a quantity can be set to 1 without altering any prediction, it was not a parameter — it was a unit convention. Running the derivation in Planck units exposes which numbers are structural and which are anchor.

## The constants and the conversion

| Quantity | SI value | Planck-unit value |
|---|---|---|
| ℏ | 1.0546 × 10⁻³⁴ J·s | 1 |
| G | 6.6743 × 10⁻¹¹ m³/(kg·s²) | 1 |
| c | 2.9979 × 10⁸ m/s | 1 |
| Planck time t_P = √(ℏG/c⁵) | 5.391 × 10⁻⁴⁴ s | 1 |
| Planck frequency ω_P = 1/t_P | 1.855 × 10⁴³ Hz | 1 |
| Hubble constant H₀ (Planck 2018) | 67.4 km/s/Mpc = 2.184 × 10⁻¹⁸ Hz | 1.177 × 10⁻⁶¹ |

The Hubble constant in Planck units is *just a number* — the dimensionless ratio H₀ × t_P. That number is what the framework uses.

## The two-column check

Every Tier-3-and-above prediction, computed both ways:

| Prediction | SI computation | Planck computation | Identical? |
|---|---|---|---|
| **Tier 3 — Structural ratios** | | | |
| φ² self-similarity | (1+√5)²/4 = 2.6180 | (1+√5)²/4 = 2.6180 | ✓ |
| Kuramoto K_c | 2/π = 0.6366 | 2/π = 0.6366 | ✓ |
| Klein-bottle surviving modes | 4 | 4 | ✓ |
| Smallest denominators (q₂, q₃) | (2, 3) | (2, 3) | ✓ |
| **Tier 4 — Dimensionless observables** | | | |
| Farey count |F₆| | 13 | 13 | ✓ |
| Unlocked count q₂q₃ | 6 | 6 | ✓ |
| Ω_Λ = 13/(13+6) | 0.6842 | 0.6842 | ✓ |
| sin²θ_W = 8/35 | 0.2286 | 0.2286 | ✓ |
| α_s / α₂ = 27/8 | 3.375 | 3.375 | ✓ |
| Spectral tilt n_s = 1 − ln(φ²)/27.4 | 0.9649 | 0.9649 | ✓ |
| Oscillations per Hubble cycle | 49 | 49 | ✓ |
| **Tier 5 — Address (the depth-on-the-tree)** | | | |
| Frequency ratio ω_P / H₀ | 1.855×10⁴³ / 2.184×10⁻¹⁸ = 8.49×10⁶⁰ | 1 / 1.177×10⁻⁶¹ = 8.49×10⁶⁰ | ✓ |
| Tree depth N = ln(ω_P/H₀)/ln(φ²) | 140.18 / 0.9624 ≈ 145.7 | 140.18 / 0.9624 ≈ 145.7 | ✓ |
| **Tier 6 — Derived observables** | | | |
| MOND scale a₀ = cH₀/2π | 1.04 × 10⁻¹⁰ m/s² | H₀/2π = 1.873 × 10⁻⁶² (× Planck acceleration → same SI) | ✓ |
| Ω_Λ × ρ_crit | 0.6842 × ρ_crit (SI) | 0.6842 × ρ_crit (Planck) | ✓ (ratio is identical) |
| Friedmann age in Hubble times | t_age × H₀ ≈ 0.951 | t_age × H₀ ≈ 0.951 | ✓ |
| Friedmann age in years | 0.951 / H₀ = 13.78 Gyr | 0.951 / H₀(Planck) × t_P → 13.78 Gyr after re-anchoring | ✓ |

## What changes between the two columns

Only one thing. The dimensionful quantity at the bottom of each table — the Hubble constant in seconds, the age in years, the MOND acceleration in m/s² — requires multiplication by the Planck-time-in-seconds (5.391 × 10⁻⁴⁴) to recover the SI number. That single multiplicative factor *is* the anchor. It encodes "how big the universe's intrinsic addresses are when expressed in human-built units."

Every other number in both columns is identical, digit-for-digit, because the framework's content is ratios.

## What this demonstrates

1. **ℏ, G, c collapse to one quantity for the framework**: the Planck scale t_P (or equivalently ω_P, l_P, m_P). Their independent SI values are conventions of the metric system, not parameters of physics.

2. **The framework needs at most one dimensionful anchor**: a single number that says "where on the tree we sit, expressed in human units." H₀ × t_P (a dimensionless number ≈ 10⁻⁶¹) is the natural form of this anchor. Equivalently, v = 246 GeV / m_P expresses the same address in particle-physics units.

3. **The Standard Model's ~20+ dimensionful free parameters reduce to one in this framework**, because every other dimensional quantity is built from the address by ratios.

4. **The dimensionless predictions (Ω_Λ, n_s, sin²θ_W, α_s/α₂, K_c, φ², N ≈ 146) carry no unit dependence at all** — they are observer-independent in the strictest sense. An alien civilization on Tau Ceti, regardless of unit system, computes the same numbers digit-for-digit.

## Pedagogical use

Run this exercise on the day you introduce Tier 5. Hand students the two columns blank except for the SI side, ask them to fill the Planck side, and then ask: *"Which row required new physics, and which only required arithmetic?"*

The right answer: every row required only arithmetic. That is the demonstration.

## Status

Pedagogical / methodological document. Cited from the Unit III lesson plan (Week 2 — "Planck units as the floor"). No new derivations; an explicit check of dimensional invariance for results derived in `farey_partition.md`, `boundary_weight.md`, `our_address.py`, `vacuum_energy.md`, `a0_threshold.md`, and `spectral_tilt_reframed.md`.
