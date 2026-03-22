# Derivation 8: High-Redshift Test of a₀(z) = cH(z)/(2π)

## The Prediction

The sync_cost framework (Derivation 03, which derives the MOND acceleration scale a_0 = cH_0/(2pi) as the point where local gravitational synchronization cost equals cosmological mean-field maintenance cost) derives the MOND acceleration scale
as the threshold where local gravitational synchronization cost equals
cosmological mean-field maintenance cost:

    a₀ = cH₀ / (2π) ≈ 1.04 × 10⁻¹⁰ m/s²

(observed: 1.2 × 10⁻¹⁰ m/s²; ratio 1.15, attributed to the exact form
of the Kuramoto frequency distribution g(ω)).

Because the derivation ties a₀ to the *instantaneous* Hubble parameter,
not to its present-day value, the framework predicts:

    a₀(z) = c H(z) / (2π)

where H(z) = H₀ √(Ω_m(1+z)³ + Ω_Λ) in flat ΛCDM.

### Numerical predictions (Planck 2018: H₀=67.4, Ω_m=0.315, Ω_Λ=0.685)

| z   | H(z) [km/s/Mpc] | a₀(z) [m/s²]  | a₀(z)/a₀(0) | Lookback [Gyr] |
|-----|------------------|----------------|--------------|----------------|
| 0   | 67.4             | 1.04 × 10⁻¹⁰  | 1.00         | 0.0            |
| 0.5 | 89.1             | 1.38 × 10⁻¹⁰  | 1.32         | 5.2            |
| 1.0 | 120.7            | 1.87 × 10⁻¹⁰  | 1.79         | 8.0            |
| 2.0 | 204.3            | 3.16 × 10⁻¹⁰  | 3.03         | 10.5           |
| 3.0 | 307.7            | 4.76 × 10⁻¹⁰  | 4.57         | 11.7           |
| 5.0 | 558.7            | 8.64 × 10⁻¹⁰  | 8.29         | 12.6           |

**Key result:** At z = 2, a₀ should be ~3× its present value.  This is a
large, in-principle-detectable effect over a redshift range now accessible
to JWST and ALMA.

### What this means observationally

The baryonic Tully-Fisher relation (BTFR) has the form:

    M_b = A × V_flat⁴

where the normalisation A ∝ 1/a₀ in MOND.  If a₀(z) increases with z, then
at fixed V_flat, the inferred baryonic mass should be *smaller* — or
equivalently, at fixed M_b, the rotation velocity should be *higher* — at
high z compared to today.  Specifically:

- The BTFR zero point should shift by ~0.5 dex in log(M_b) between z=0
  and z=2.
- Rotation curves should transition from Newtonian to MOND behaviour at a
  higher acceleration (larger radius for a given mass) at high z.


## Competing Predictions

| Framework            | a₀ at z=2        | BTFR evolution         |
|----------------------|------------------|------------------------|
| Standard MOND        | a₀ = const       | No evolution            |
| sync_cost: a₀=cH/2π | a₀ ~ 3× today   | Zero point shifts ~0.5 dex |
| ΛCDM (Magneticum)   | a₀ ~ 3× today   | Effective a₀ emerges from baryonic physics |
| Xu (2022) power law  | a₀ ∝ (1+z)^¾    | Similar at z<3, diverges at z>3 |

Notable: the sync_cost prediction and ΛCDM simulations give *similar*
a₀(z=2)/a₀(0) ratios (~3).  The discriminating lever arm is at z > 3,
where the functional forms diverge.  The sync_cost prediction
(a₀ ∝ H(z) ∝ √(Ω_m(1+z)³ + Ω_Λ)) grows faster than (1+z)^(3/4) at
high z and has a specific functional form set by cosmological parameters
with no free parameters.


## Observational Status (as of early 2026)

### Data that exist

1. **Nestor Shachar et al. (2023, ApJ 944, 78) — "RC100"**
   100 massive star-forming galaxies at z = 0.6–2.5 with Hα/CO rotation
   curves from VLT SINFONI/KMOS and ALMA.  Dark-matter fractions within
   R_e decline with redshift: f_DM ~ 0.38 at z~1, ~0.27 at z~2.  Half
   of z~2 galaxies are maximal disks.  This declining DM fraction is
   *qualitatively* consistent with a larger a₀(z) pushing the MOND
   transition to smaller radii.

2. **McGaugh et al. (2024, ApJ 976, 13) — "Accelerated Structure Formation"**
   Binned the RC100 data on the BTFR by redshift (0.6 < z < 2.5).
   Found no clear evolution of the BTFR zero point.  However, the RC100
   sample is heavily biased toward massive, fast-rotating galaxies
   (V > 200 km/s) that are deep in the Newtonian regime — exactly where
   a₀ shifts are least visible.

3. **Übler, Nestor Shachar et al. (2024, A&A) — TFR at 0.6 ≤ z ≤ 2.5**
   Stellar TFR slope α = 3.03 ± 0.25.  "Subtle deviation" from local
   studies.  Modest evidence for evolution; not yet decisive.

4. **JADES / JWST rotation field (2025, MNRAS 538, 76)**
   Distribution of galaxy rotation in JWST Advanced Deep Extragalactic
   Survey.  Provides kinematic classifications but not yet precision
   rotation curves for low-mass systems.

### What the data do NOT yet constrain

- **Low-mass galaxies at z > 1.5** (V_flat ~ 50–120 km/s): These are the
  systems where MOND effects dominate and where a₀ shifts would be most
  visible.  Current high-z rotation curve samples are biased toward the
  most massive disks.

- **The BTFR at z > 2.5**: Beyond the RC100 redshift range.  Only a
  handful of individual kinematic measurements exist (e.g., Neeleman et al.
  2020 at z = 4.26, a single cold rotating disk).

- **Precision at the 0.2 dex level**: Current high-z V_flat measurements
  have ~20–40% uncertainties, comparable to the predicted signal.


## What Needs to Be Measured

To test a₀(z) = cH(z)/(2π) at 3σ significance:

### 1. Target selection
Low-mass disk galaxies at z = 1.5–3, with V_flat ~ 50–120 km/s.  These
are faint (H ~ 25–27 mag) but detectable with JWST behind lensing
clusters or in deep fields.

### 2. Rotation curves
- JWST NIRSpec IFU at R ~ 2700–4000 for Hα (rest-frame) at z ~ 1.5–3.
- Spatial resolution < 1 kpc required — gravitational lensing
  magnification of 5–10× or JWST diffraction limit (0.1" ~ 0.8 kpc at
  z = 2) may suffice.
- ALMA CO or [CII] lines for independent kinematic cross-check.

### 3. Baryonic masses
- Stellar mass from JWST NIRCam multi-band photometry + SED fitting
  (rest-frame near-IR at z ~ 2 maps to observed 4–5 μm).
- Gas mass from ALMA dust continuum (Band 6/7) or molecular line emission.
- Target accuracy: 0.2 dex in total baryonic mass.

### 4. Sample size
- Predicted signal: ~0.5 dex shift in BTFR zero point between z = 0 and
  z = 2.
- With intrinsic scatter ~0.3 dex, need N > 20 galaxies per redshift bin
  to beat systematics (beam smearing, pressure support, inclination).
- Minimum programme: ~60 galaxies across z = 0–1, 1–2, 2–3 bins.

### 5. Discriminating between models
The sync_cost prediction diverges from the (1+z)^(3/4) power law at z > 3:

| z   | cH(z)/(2π) ratio | (1+z)^(3/4) ratio |
|-----|-------------------|--------------------|
| 2   | 3.0               | 2.3                |
| 3   | 4.6               | 3.0                |
| 5   | 8.3               | 4.6                |

A single well-measured BTFR at z ~ 5 (feasible with JWST [CII] + ALMA)
would strongly discriminate.


## Relation to Other Predictions

- **Derivation 03**: This test directly probes the a₀ = cH₀/(2π) relation
  by checking its redshift extension.

- **Derivation 05 (Two Forces)**: If a₀(z) varies, the effective dark
  matter fraction within galaxies should also be z-dependent in a
  calculable way — providing a second, correlated observable.

- **Galaxy clusters**: The cluster-scale anomaly noted in Derivation 03
  -- galaxy clusters show convergence failure in Lagrangian relaxation because they operate above the single-body MOND transition but below the multi-body synchronization threshold -- may also evolve with z.  Cluster
  dynamics at z > 1 (accessible via Sunyaev-Zel'dovich + X-ray with
  SPT-3G and eROSITA) provide an independent test channel.


## Status

**Prediction**: Concrete, parameter-free, and falsifiable.  a₀(z) is fully
determined by H₀, Ω_m, and Ω_Λ — all independently measured.

**Data**: Tantalisingly close but not yet decisive.  The RC100 sample
covers the right redshift range but the wrong mass range.  JWST Cycle 3+
programmes targeting low-mass lensed disks at z > 1.5 are the critical
next step.

**Timeline**: Feasibility demonstration with ~10 galaxies could come from
existing JWST archival data (JADES, GLASS, UNCOVER lensed fields) within
1–2 years.  A definitive test (N > 60, z = 0–3) likely requires a
dedicated JWST programme (Cycle 5+, ~100 hours) or ELT first light
(~2028+).

## Computation

See `a0_high_z.py` in this directory for the full numerical computation
and detailed observational comparison.
