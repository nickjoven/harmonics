# Open Items (9 remaining as of 2026-04-09)

## 1. Base exponent a₁ ≈ 2.320
- **Status:** Numerically determined to 0.06% of 2 + 1/π, but no closed-form proof.
- **What would close it:** Derive a₁ = 2 + 1/π (or the correct exact value) from the Stern-Brocot / mediant structure. Likely requires an analytic number-theory identity connecting the continued-fraction statistics of mediants to π.

## 2. Quark masses (QCD running)
- **Status:** Pipeline exists (`quark_mass_pipeline.py`), maps lepton-sector exponents through QCD running. Not yet executed end-to-end with physical αₛ running.
- **What would close it:** Run the full pipeline at physical scales, compare predicted quark pole masses to PDG values. If agreement is < 1%, item is closed.

## 3. A_s amplitude (scalar power spectrum)
- **Status:** The mapping rate (spectral tilt nₛ) is derived. The absolute amplitude A_s ≈ 2.1 × 10⁻⁹ is not.
- **What would close it:** Connect the overall normalization of the Farey-graph fluctuation spectrum to the dimensionful scale v = 246 GeV (item 6). This likely requires solving item 6 first.

## 4. Cosmological dynamics K(t)
- **Status:** Friedmann-like structure identified in the coupling flow K(t). Not derived from first principles.
- **What would close it:** Show that the Kuramoto coupling K on the Klein bottle, evolved under the rational field equation, satisfies the Friedmann equations with the correct equation-of-state sequence (radiation → matter → Λ).

## 5. Measurement outcome problem
- **Status:** The mechanism for measurement (decoherence via Farey-graph branching) is derived. Which outcome actually occurs in a given instance is traced to a hidden initial condition in the Stern-Brocot address.
- **What would close it:** Either (a) prove that the initial condition is formally undecidable (making this the irreducible kernel of quantum randomness), or (b) find an observable consequence that distinguishes this from standard Born-rule randomness.

## 6. One dimensionful scale v = 246 GeV
- **Status:** The framework produces all dimensionless ratios but requires one dimensionful input. v = 246 GeV (the Higgs VEV) is the conventional choice.
- **What would close it:** This is likely irreducible -- any physical framework needs at least one scale to connect pure numbers to SI units. Closing it would require showing that v is fixed by a self-consistency condition (e.g., anthropic or dynamical attractor), or proving it must be a free parameter.

## 7. Planck-scale non-metricity prediction: O(1/√N)
- **Status:** The Christoffel gap (gap 1) predicts a deviation from Riemannian geometry at order 1/√N, where N is the Stern-Brocot depth. At Planck scale this is O(1).
- **What would close it:** Compute the predicted non-metricity tensor components at accessible scales (e.g., tabletop torsion-balance experiments or pulsar timing). If the prediction is below current sensitivity, state the required improvement factor.

## 8. 4th generation lepton prediction: ~7.3 GeV
- **Status:** The generation exponent law (`generation_exponent_law.py`) predicts a 4th-generation charged lepton at ~7.3 GeV. This is below the LEP Z-width bound (which excludes a 4th light neutrino, not necessarily a 4th heavy charged lepton with a heavy neutrino partner).
- **What would close it:** Detailed phenomenological analysis -- does a 7.3 GeV charged lepton with a heavy (> mZ/2) neutrino partner evade all existing collider bounds? If yes, propose a search strategy at Belle II or LHCb. If no, the prediction is falsified and the exponent law needs revision.

## 9. N_efolds = 61.3 (CMB-S4 testable ~2028)
- **Status:** The framework predicts exactly 61.3 e-folds of inflation, which shifts the spectral tilt prediction to a specific value distinguishable from the generic slow-roll band.
- **What would close it:** CMB-S4 data (expected ~2028) will measure nₛ and r to sufficient precision. If the measured values match the 61.3 e-fold prediction, this becomes a confirmed prediction. If not, the inflationary mapping needs revision.
