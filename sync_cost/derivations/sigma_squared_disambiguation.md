# σ² disambiguation

The symbol σ² appears in three distinct framework quantities. This
document defines each precisely and gives the reconciliation
between them. Use this as the reference when reading any framework
file that mentions "σ²".

## The three quantities

| Symbol | Meaning | Value | Source |
|---|---|---|---|
| σ²_kernel | per-direction kernel normalization | 1/4 | `continuum_limits.md` §5a / `adm_prefactor_verification.py` |
| K_eff | summed coupling at the Hubble scale (over 2d neighbors) | 3/2 | `sigma_squared.py` from K_eff = 4πG ρ_crit L_H²/c² |
| σ²(d) | tree-measure constraint at Stern-Brocot depth d | depth-dependent | `alphabet_depth21.py` from 1/Σ(1/q²) |

## Reconciliation

**σ²_kernel ↔ K_eff**: in d = 3 spatial dimensions, each
oscillator couples to 2d = 6 nearest neighbors. The total
coupling is the per-direction kernel summed over neighbors:

    K_eff = σ²_kernel × 2d  =  (1/4) × 6  =  3/2.

This is C-structural — both sides forced by the Gauss-Codazzi
embedding plus standard cubic-lattice coordination.

**σ²(d)**: a tree-side quantity obtained by summing 1/q² over
all rationals in the Stern-Brocot tree of depth d, then taking
the reciprocal. Its physical interpretation depends on the
choice of dynamical question (measure-one constraint at K=1,
running with d, etc.); not directly equal to either σ²_kernel
or K_eff at any specific depth.

## Common misuse: sigma_squared.py "three routes" framing

`sigma_squared.py` discusses three "routes to σ²" (measure-one,
A_s amplitude, gravitational coupling) and notes they give
"compatible values after unit conversion". The unit conversion
is the cross-walk above: σ²_kernel and K_eff differ by a factor
of 2d = 6, and σ²(d) is a different (tree-side) object that
does not match either at the relevant depth.

The script's § "self-consistency" references "the prefactor
verification identified in Derivation 12 Part I §7". That
reference points to `continuum_limits.md` §5a — which closes
the **ADM prefactor verification** (σ²_kernel giving 16πG and
8πG via Gauss-Codazzi), not the A_s amplitude prefactor. Two
distinct problems:

| Prefactor problem | Quantity | Status |
|---|---|---|
| ADM prefactor verification | σ²_kernel giving 16πG, 8πG | closed (`continuum_limits.md` §5a) |
| A_s amplitude assembly | full chain in `a_s_geometric_proof.md` | %-only at 11% |

The two should not be conflated.

## Cross-references

| File | Role |
|---|---|
| `continuum_limits.md` §5a | σ²_kernel = 1/4 derivation |
| `adm_prefactor_verification.py` | σ²_kernel ↔ K_eff = 3/2 reconciliation |
| `sigma_squared.py` | the "three routes" script; carries the symbol overload |
| `alphabet_depth21.py` | σ²(d) running on the SB tree |
| `a_s_geometric_proof.md` | the canonical A_s derivation using σ²_kernel |
| `lambda_unlock_closed_form.py` | closed form for λ_unlock(K=1), used in A_s |
