# Open Items (status updated 2026-04-09, after mass sector closure)

## UPDATE: Mass sector closure

The integer conservation law `depth × |3Q| = k_sector` has been
connected to the gauge adjoint dimensions through the cross-link
identity (`mass_sector_closure.md`):

- $k_{\text{lepton}} = 9 = (\dim \text{adj SU(2)})^2$
- $k_{\text{quark}} = 8 = \dim \text{adj SU(3)}$
- Cross-link: $q_2^2 - 1 = q_3$ and $q_3^2 - 1 = q_2^3$
- **Uniqueness: $(q_2, q_3) = (2, 3)$ is the unique integer pair**

This closes item 2 (quark masses) at the structural level and
resolves the "selection rule" open question that had been implicit
throughout the session. Items 1, 3-9 are updated below.

---

## 1. Base exponent a₁ ≈ 2.320
- **Status (updated):** Still a fixed-point output of the rational field equation, not a closed form. Now understood as a reading through Fibonacci backbone coordinates. The integer conservation law fixes the structural form; the specific numerical value of a₁ is the projection of that law onto the observed lepton masses.
- **What would close it:** Compute a₁ by high-precision iteration of the field equation at the Klein bottle's extended mode tower. This is a computation, not a derivation of a closed form (Feigenbaum-like).

## 2. Quark masses (QCD running) — PARTIALLY CLOSED
- **Status (updated):** The quark sector base pairs are now derived (within PDG uncertainty) from the integer conservation law + adjoint cross-link. The algebraic forms (8/5, 3/2), (5/4, 9/8) in terms of $(q_2, q_3)$ are in `sector_base_pairs.py`. QCD running from tree scale through flavor thresholds remains standard SM physics applied to these boundary conditions.
- **What would close it fully:** Execute the RG running pipeline end-to-end with the tree-scale quark masses as boundary conditions, compare to PDG pole masses. Expected agreement: within QCD uncertainty (few percent).

## 3. A_s amplitude (scalar power spectrum)
- **Status:** Unchanged. The mapping rate is derived; the absolute amplitude needs v = 246 GeV.
- **What would close it:** Solve item 6 first.

## 4. Cosmological dynamics K(t)
- **Status:** Unchanged. Still structural, not derived from first principles.
- **Connection to new work:** The mass sector closure doesn't touch K(t) evolution. This remains a separate problem in the gravity/cosmology sector.

## 5. Measurement outcome problem
- **Status:** Unchanged. Mechanism derived, specific outcome requires hidden initial condition.

## 6. One dimensionful scale v = 246 GeV
- **Status:** Unchanged. Still the single dimensionful input.
- **Connection to new work:** The mass sector derives all dimensionless ratios from $(q_2, q_3)$ and the gauge adjoints. The dimensionful scale remains the single input needed to connect these ratios to GeV units.

## 7. Planck-scale non-metricity prediction: O(1/√N)
- **Status:** Unchanged. Prediction from Gap 1 (Christoffel connection).

## 8. 4th generation lepton prediction: ~7.3 GeV
- **Status (updated):** The generation exponent law is now embedded in the integer conservation law. A 4th generation would require extending the walk beyond the current pattern. The prediction of ~7.3 GeV from the original exponent law now needs re-examination: does the integer conservation law permit a 4th generation at all? Since the 4th lepton walk would require depth × |3Q| = 9 with a deeper position, the walker would need to find a mode at depth 9 with the same q constraint. Whether such a mode exists on the Fibonacci backbone is a tree-geometry question.
- **What would close it:** Check whether depth 9 on the lepton Fibonacci backbone hosts a viable base pair element. If yes, 4th gen lepton exists at predicted mass. If no, 4th gen is forbidden.

## 9. N_efolds = 61.3 (CMB-S4 testable ~2028)
- **Status:** Unchanged. Independent of mass sector closure.

---

## Items NO LONGER open (resolved by mass sector closure)

### Selection rule: why each sector picks its specific walk
- **Was:** depth × |Q| = k was an empirical pattern
- **Now:** k_sector is the dual gauge adjoint dimension, cross-linked to the gauge group via unique integer identities. Resolved structurally.

### Why 9/8 factor appears between lepton/quark readings
- **Was:** Observed numerical coincidence
- **Now:** $9/8 = (\dim \text{adj SU(2)})^2 / \dim \text{adj SU(3)}$. Resolved.

### Why sector base pairs involve specific algebraic combinations
- **Was:** (3/2, 5/3), (8/5, 3/2), (5/4, 9/8) found by search
- **Now:** The Stern-Brocot positions of these fractions are selected by the integer conservation law, which in turn is set by gauge adjoint dimensions. Resolved at the structural level; specific computational verification remains.

---

## New questions raised by the mass sector closure

### Q1: Neutrino mass scale from depth → ∞ limit
- **Problem:** |Q| = 0 for neutrinos, so depth × 0 = 0 is trivially satisfied. Neutrinos have no finite walk constraint from the integer law.
- **Rough estimate:** m_ν ~ m_Planck × (K*/2)^145.8 ~ 10⁻²⁶ eV. Below observational bound (0.12 eV) by 25 orders.
- **Status:** Very rough, needs proper treatment of the finite tree cutoff.

### Q2: Why is the lepton budget squared but quark budget linear?
- **Problem:** $k_{\text{lepton}} = (\text{adj SU(2)})^2$ but $k_{\text{quark}} = \text{adj SU(3)}$. The asymmetry is empirical.
- **Hypothesis:** Chirality — leptons need two copies of the adjoint for left and right components, quarks don't because color is chirality-blind.
- **Status:** Plausible but not formally derived.

### Q3: Dark twin as budget reservoir
- **Problem:** The framework's "dark twin" absorbs degrees of freedom our universe doesn't manifest. Its budget should match the deficit.
- **Hypothesis:** The twin's walk budget is the complement of ours — whatever gauge bosons our sector doesn't interact with becomes available to the twin.
- **Status:** Speculative, flagged by user as next.

