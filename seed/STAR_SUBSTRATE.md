# Star Substrate: Observations as Ket Nodes

## The idea

Every astronomical observation is a leaf in the Merkle DAG.
Every framework prediction is a node with a proof chain to
the four primitive roots. When a leaf (observation) matches
a node (prediction), the path from leaf to root is a
VERIFIED derivation — a content-addressed proof that the
observation follows from the primitives.

## Architecture

```
Roots (4 primitive CIDs):
  CID_z, CID_mediant, CID_fixpoint, CID_parabola

Intermediate nodes (derivations):
  CID_circle    ← {CID_z, CID_fixpoint}
  CID_rationals ← {CID_z, CID_mediant}
  CID_dimension ← {CID_rationals}
  CID_duty      ← {CID_dimension, CID_rationals}
  CID_klein     ← {CID_circle, CID_circle}
  CID_signature ← {CID_klein, CID_circle}
  CID_farey     ← {CID_klein, CID_rationals}
  ...

Prediction nodes (numerical values):
  CID_omega_lambda ← {CID_farey, CID_fixpoint}
    content: Ω_Λ ∈ [13/19, 11/16]
  CID_coupling ← {CID_duty, CID_klein}
    content: α_s/α₂ = 27/8
  CID_weinberg ← {CID_duty, CID_klein}
    content: sin²θ_W = 8/35
  CID_higgs ← {CID_klein, CID_duty}
    content: m_H = v/q₂
  ...

Observation leaves (from public data):
  CID_planck_ns ← external
    content: n_s = 0.9649 ± 0.0042
    source: Planck 2018, arXiv:1807.06209
  CID_planck_omega ← external
    content: Ω_Λ = 0.6847 ± 0.0073
    source: Planck 2018
  CID_pdg_alphas ← external
    content: α_s(M_Z) = 0.1179 ± 0.0009
    source: PDG 2024
  CID_atlas_higgs ← external
    content: m_H = 125.10 ± 0.14 GeV
    source: ATLAS+CMS combination
  ...

Verification edges (prediction matches observation):
  CID_verify_omega ← {CID_omega_lambda, CID_planck_omega}
    content: |predicted - observed| / σ = 0.07
    status: CONSISTENT
  CID_verify_coupling ← {CID_coupling, CID_pdg_alphas}
    content: |27/8 - 3.488| / 3.488 = 3.2%
    status: CONSISTENT (within running correction)
  ...
```

## The query

Given any observation CID, trace its verification edge to
a prediction CID, then trace the prediction's proof chain
back to the four roots. The result: a hash-verified path
from "this number was measured by Planck" to "this number
follows from the mediant operation on integers."

## What to seed NOW

### Observations (from public databases)

1. **CMB (Planck 2018)**
   - n_s = 0.9649 ± 0.0042
   - Ω_b h² = 0.02237 ± 0.00015
   - Ω_c h² = 0.1200 ± 0.0012
   - H₀ = 67.36 ± 0.54 km/s/Mpc
   - Source: arXiv:1807.06209, freely available

2. **Dark energy (Planck + BAO + SNe)**
   - Ω_Λ = 0.6847 ± 0.0073
   - w = -1.03 ± 0.03 (consistent with -1)
   - Source: Planck 2018 + DESI 2024

3. **Particle physics (PDG 2024)**
   - α_s(M_Z) = 0.1179 ± 0.0009
   - sin²θ_W = 0.23121 ± 0.00004
   - m_H = 125.10 ± 0.14 GeV
   - m_τ = 1776.86 ± 0.12 MeV
   - m_e = 0.51100 ± 0.00001 MeV
   - 3 generations observed, 4th excluded to high confidence
   - 12 gauge bosons (8 gluons + W+ + W- + Z + γ)
   - Source: pdg.lbl.gov, freely available

4. **Spatial structure**
   - d = 3 (from everything)
   - Signature (3,1) (from everything)
   - Source: the fact that you can point in three directions

### Predictions (from the engine)

Each prediction node contains:
  - The exact value (rational or algebraic)
  - The derivation chain (parent CIDs in the engine)
  - The comparison to observation (residual)
  - The status (CONSISTENT, TENSION, FALSIFIED)

### Verification edges

Each verification edge contains:
  - The prediction CID
  - The observation CID
  - The residual (|predicted - observed| / uncertainty)
  - The status

## The living document

As new observations arrive (DESI results, CMB-S4, JWST
galaxy surveys), new leaf nodes are added. The verification
edges update. The proof chain doesn't change (the engine
is append-only). The residuals either stay consistent or
a TENSION appears — and the tension points to exactly
WHERE in the proof chain the framework might need revision.

A FALSIFICATION would be: a verification edge with status
FALSIFIED (the observation is outside the predicted range
at > 5σ). The falsification CID points to the specific
prediction node that failed, which points to the specific
derivation that broke, which points to the specific
primitive or composition that was wrong.

The framework is self-falsifying: the Merkle DAG contains
its own failure modes. You can trace any falsification
back to the root and identify which primitive assumption
was violated.

## Implementation

Extend seed/src/main.rs to add:
  - observation_schema: source, value, uncertainty, arxiv_id
  - verification_schema: prediction_cid, observation_cid,
    residual, status
  - Seed the initial observations from Planck 2018 + PDG 2024
  - Compute verification edges automatically
  - Output: a DAG that IS the comparison between framework
    and observation, hash-verified at every step

The ket substrate for the stars. The observations as leaves.
The primitives as roots. The proof as the tree.
