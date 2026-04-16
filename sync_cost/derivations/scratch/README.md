# scratch

Exploration scripts from the K_STAR investigation. They are kept here
because the ruminating demonstrates mental-model evolution, not because
they derive the current canonical chain. None of these files is required
reading. The canonical walk-through lives in
[`../CHAIN_KSTAR.md`](../CHAIN_KSTAR.md), and the three load-bearing
scripts are:

- [`../step3_step5_klein_proof.py`](../step3_step5_klein_proof.py) —
  Steps 3 and 5 derived from canonical Klein bottle topology.
- [`../tau_mass_prediction.py`](../tau_mass_prediction.py) —
  the forward prediction for `m_τ` from the closed form and `m_μ`.
- [`../K_star_precision_check.py`](../K_star_precision_check.py) —
  Step 6 verification against PDG 2024 (0.594 σ).

The files below are working notes and should be read only if you are
trying to reconstruct the reasoning process, not the result.

## Contents

| file | role | relevance to the canonical chain |
|---|---|---|
| `variational_matter_native.py` | survey of matter-sector-native variational candidates | none of them closed; cleanest near-miss was `log_φ(3/2)` at 2.25 % |
| `axis5_reciprocity_and_logratio.py` | discovery of the Axis 5 reciprocity (lep–dn exact mirror) | the first concrete framework-level Z₂ structure used in Step 5 |
| `reciprocity_sweep.py` | sweep of all per-sector axes for reciprocity | confirms Axis 5 is the unique reciprocity-carrying axis |
| `twin_swap_formalization.py` | Möbius-involution formalisation of the twin swap | produces the phantom fixed points `{13/9, 21/10, −6}` |
| `klein_topology_phantoms.py` | search for a Klein-topology derivation of the phantoms | partial hierarchy for N and b₂; b₁ does not fit cleanly |
| `low_index_structure.py` | harmonic-series first crossings and the Pythagorean comma | `3^12 / 2^19` at framework-alphabet exponents |
| `string_nodes_and_pitches.py` | matter-sector base pairs as just-intonation intervals | reframes the sectors as harmonics of a string |
| `harmonic_threshold.py` | Arnold tongue widths vs simultaneous-fundamentals threshold | justifies `q* ≈ 4` at `K_STAR` |
| `subharmonic_series.py` | physical reality of the subharmonic series, Kawano et al. 2025 | confirms the nonlinear mechanism the framework uses |
| `klein_vocabulary.py` | decomposition of overloaded terms ("Klein parity", "depth", …) | reference glossary for the chain |
| `step3_proof.py` | unique match of signature (3,1) to `F_n` under `x → 1−x` at `n = 4` | subsumed by `step3_step5_klein_proof.py` (Klein L0 derivation) |
| `farey_depth_proof.py` | three convergent definitions of framework depth | subsumed by `step3_step5_klein_proof.py` |
| `deriving_14.py` | early six-step chain scaffold | superseded by `step3_step5_klein_proof.py` + `CHAIN_KSTAR.md` |
| `octave_doubling.py` | first derivation of the closed form `K_STAR^14 = 1/8` | logic absorbed into `CHAIN_KSTAR.md` |
| `connection_tree.py` | two-system Stern-Brocot tree with the root as connection | supporting intuition for Step 5 |

Each script is self-contained and runnable. They import from
`framework_constants` in the parent directory, so they need to be
invoked from the `sync_cost/derivations/` level:

    python scratch/axis5_reciprocity_and_logratio.py
