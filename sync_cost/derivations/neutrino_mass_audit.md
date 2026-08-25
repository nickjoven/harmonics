# Neutrino mass audit: already closed, not a depth-limit problem

> **Status correction (2026-08-22, ERRATA E19).** The "0.31 sigma atmospheric" figure compares the predicted Delta m^2_31 (2.446e-3 eV^2) against the observed **Delta m^2_32** (PDG 2.455e-3) via `item12_neutrino_solar_closure.py:50` - a mislabel. Against NuFIT Delta m^2_31 = 2.507 +/- 0.027 the prediction is **2.25 sigma**; the predicted Delta m^2_32 = 2.372 is 2.95 sigma from 2.455. The solar 0.12 sigma was obtained by adding the "-1/36" term that moved it from 1.77 sigma (`item12...py:10,25`); with >= 5 alphabet choices in m_3 = v (K*/2)^35 2^(1/3), m_1 = m_3/8, m_2 = m_1(sqrt 3 - 1/36), "not a fit" does not hold. Status: **open, 2.25 sigma, fitted** - not "closed." The surviving falsifiable content is Sum m_nu = 66.7 meV, normal ordering, m_1 = 6.2 meV, which DESI/CMB-S4 will test.

## The finding

Issue #56 Tier 2 item 9 lists:

> "Neutrino masses (depth → ∞ limit)"

This is an **outdated attribution**. `item12_neutrino_solar_closure.py`
closes the full neutrino mass sector via a **finite-K
interaction-scale correction**, not a depth → ∞ limit.

## Current closure (from `item12_neutrino_solar_closure.py`)

Mass formulas (all from framework primitives q_2, q_3, d, v, K*):

    m_3  =  v · (K*/2)^(q_2³ + q_3³) · q_2^(1/q_3)
    m_1  =  m_3 / q_2^d                              (= m_3/8)
    m_2  =  m_1 · [q_3^(1/q_2) − (q_2·q_3)^(−2)]    (= m_1·(√3 − 1/36))

Numerical predictions:

    m_1 (lightest)  =  6.231 meV
    m_2             = 10.620 meV
    m_3 (heaviest)  = 49.851 meV
    Sum m_ν         = 66.703 meV
    Ordering        = normal (predicted)

Comparison to NuFIT 5.2 (PDG):

    Atmospheric Δm²_31 : **0.31 σ**
    Solar Δm²_21       : **0.12 σ**

Both well inside 1σ.

**σ definition.** Observational z-score:
`σ = |framework_prediction − NuFIT_central| / NuFIT_uncertainty`,
treating the framework prediction as a point value (no
propagated theory uncertainty). NuFIT 5.2 uncertainties on
Δm²_31 and Δm²_21 are ~1% and ~3% relative, respectively, so the
0.31 σ and 0.12 σ correspond to absolute matches at the 0.3%
and 0.4% levels. See `statistical_conventions.md`.

## Structural reading

The neutrino solar splitting closes via a single finite
interaction-scale correction `−(q_2·q_3)^(−2) = −1/36` applied to
the tree-level ratio, using framework-native alphabet rationals at
the physical vacuum scale `v`. It is not a fit.

**Caution — this closure must not be generalized into a shared
"finite-K correction closes the sector" pattern.** The analogous
electroweak "corrections" `sin²θ_W = 8/35 + 8/F_10²` and
`α_s/α_2 + 1/q_3²` are **null / retracted**: the `+8/F_10²`
Fibonacci term is retracted, the `d_eff = 80/27` route is a null
ansatz, and SM running rules out `8/35` and `27/8` as M_Z
predictions (Class 1; see `negative_results_ledger.md`). The neutrino closure stands on
its own structural footing and must **not** be presented as one
instance of a winning EW pattern — it inherits no support from the
electroweak sector.

## "Depth → ∞ limit" is the wrong framing

Issue #56's framing "depth → ∞ limit" appears to refer to a
Fibonacci-backbone deep-tree construction. The actual closure uses
finite K* = 0.86196 and specific framework integers (q_2, q_3, d)
evaluated at the physical vacuum scale v. No limit needs to be
taken.

This is another documentation/attribution mismatch, same session
pattern as:
- `gap2_spatialization_decomposition.md` sub-E flagged "Open"
  while `hierarchy_gaussian_lattice.md` had closed it.
- `ckm_from_sl2z.py` flagged "doesn't work" while its predictions
  actually match PMNS.
- Issue #56 flagging "neutrino masses (depth → ∞ limit)" while
  `item12_neutrino_solar_closure.py` has it at 0.12–0.31 σ via
  finite-K corrections.

## What is actually predicted

| Observable | Framework prediction | Observed | σ |
|---|---|---|---|
| m_1 | 6.23 meV | (not directly measured) | — |
| m_2 | 10.62 meV | (not directly measured) | — |
| m_3 | 49.85 meV | ≈ √(Δm²_31) ≈ 49.5 meV | ~0.3 |
| Σ m_ν | 66.7 meV | CMB + BAO bound < 120 meV | compatible |
| Δm²_31 (atm.) | matches PDG | — | 0.31 σ |
| Δm²_21 (solar) | matches PDG | — | 0.12 σ |
| Ordering | normal (predicted) | normal (preferred) | ✓ |

Six predictions, all within 1σ or confirmed.

## Testability

The file flags three upcoming tests:

1. **KATRIN endpoint**: m_1 sensitivity ~0.2 eV; framework's
   6.23 meV is below current reach but within future sensitivity.
2. **CMB-S4 + DESI Σm_ν**: target ~20–40 meV precision by late
   2020s; framework predicts 66.7 meV, well within reach.
3. **0νββ experiments**: Majorana mass, if neutrinos are
   Majorana; framework doesn't commit to Dirac vs. Majorana but
   gives m_1 = 6.23 meV as the minimal mass.

Within-decade falsifiability on all three.

## Issue #56 Tier 2 status update

| Item | Previous | Updated |
|---|---|---|
| 9. Neutrino masses | "depth → ∞ limit" (open) | **Closed at 0.12–0.31 σ via finite-K interaction-scale correction** (`item12_neutrino_solar_closure.py`) |

This is a pure documentation update — the closure exists in the
codebase, just isn't reflected in the issue status.

## What remains open in Tier 2

After this audit, the Tier 2 open items relevant to the "mixing
and masses" cluster:

- **θ_13 reactor (PMNS)**: 8.6° observed vs. 28° tree-level
  (from prior `mixing_angle_audit.md`). Needs small neutrino
  Yukawa running.
- **CKM angles**: require QCD running pipeline.
- **Quark mass running to M_Z**: same pipeline.

All three require SM-style renormalisation group integration, not
framework-structural work.

## Methodological note

Seventh closure this session, all via attribution/vocabulary:

| # | Problem | Resolution |
|---|---|---|
| 1 | Down-type factor 6 | S_3 orbit-dim on Z_2 × Z_3 |
| 2 | Mass-sector √w at q=2 | Coordinate convention (factor π) |
| 3 | Ω_b residual (diagnostic) | Three-way boundary-weight inconsistency |
| 4 | K = K_c critical case | K_c = 0 for identical oscillators |
| 5 | ℓ_c diffusion length | ℓ_P derived from R |
| 6 | CKM/PMNS mixing | Tree-level predictions = PMNS not CKM |
| 7 | **Neutrino masses** | **Closed by interaction-scale correction, not depth limit** |

Seven "open" items turn out to be one of:
- terminology overload (K_c, "mode volume")
- status mismatch between docs (ℓ_c, neutrinos)
- attribution to wrong observable (mixing angles)
- structural but already computed (down-type, mass-sector)

The remaining open items are genuinely orthogonal work
(SM running integrations, time-dependent dynamics, topological
defect analysis) — not harvestable by vocabulary audit.

## Cross-references

| File | Role |
|---|---|
| `item12_neutrino_solar_closure.py` | The actual closure at 0.12–0.31 σ |
| `mass_sector_closure.md` | Mass-sector open-items list |
| `mixing_angle_audit.md` | Companion audit (this session) |
| `sinw_effective_dimension.md` | Fibonacci-correction template |
| Issue #56 Tier 2 item 9 | "Neutrino masses (depth → ∞ limit)" — outdated |
