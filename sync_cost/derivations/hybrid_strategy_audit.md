# Hybrid strategy audit — Floor residuals against |r|^n closures

Parallel audit of the three Floor items against the hybrid
(`discrete Farey count × continuous decoherence tax`) closure
strategy proposed in `omega_b_residual_phase_b.md`. Applies the
triage in `ansatz_audit_policy.md`.

## What the hybrid strategy proposes

Each Floor item sits at `prediction_integer · |r|^n` with `|r|`
the Kuramoto order parameter and `n` an exponent specific to
the observable. In `omega_b_residual_phase_b.md` the proposed
form is

    Ω_b  =  (1/19) · |r|²            (cross-sector reading, n = 2)

with `|r| = 0.968` at M_Z, imported from `duty_cycle_dictionary.md`
via `|r| = 27 / (8 · α_s/α_2)`.

## Numerical results

Using `|r| = 0.9676` (from `27/(8 · 3.488)`, α_s/α_2 at M_Z):

| Item | Pred (raw) | Exponent that closes | Residual after |r|^n | Notes |
|---|---|---|---|---|
| Ω_b | 1/19 = 0.05263 | n = 2 | 0.03% (0.1σ) | Phase B claim |
| Ω_c/Ω_b | 5 | (matter conservation on Ω_b) | 0.6% (0.5σ) | derivative of Ω_b |
| A_s | 2.33 × 10⁻⁹ | n = 3 | 0.64% (< 1σ) | different n from Ω_b |

Alternative exponents tested for each:

| Item | n = 1 | n = 2 | n = 3 | n = 4 |
|---|---|---|---|---|
| Ω_b residual | −3.3% | **−0.03%** | +3.2% | +6.3% |
| A_s residual | −7.4% | −4.0% | **−0.6%** | +2.6% |

Only one `n` per observable matches ≤ 1σ. The matching `n`
differs between Ω_b (n = 2) and A_s (n = 3).

## Triage under `ansatz_audit_policy.md`

**Step 1 — Enumerate alternatives.** Done. `|r|^n` with integer
`n ∈ {1, 2, 3, 4}` produces a one-parameter family of candidate
closures. Each observable selects one `n`; the selections differ.

**Step 2 — Identify the forcing argument.**

- Ω_b: Phase B offers "baryons are cross-sector modes; joint
  coherence is `|r|_2 · |r|_3 = |r|²` in the symmetric limit."
  This is a reading, not a forcing argument. The symmetric limit
  is assumed; the cross-sector identification selects n = 2 over
  n = 3 (which would require three-sector coupling) but the
  baryonic mode ψ_+(1, 5) is already Klein-singlet in the
  `baryon_fraction.md` derivation, without needing a sector
  product. The `|r|²` story does not follow from a theorem about
  the Klein-singlet; it is added to explain the numerical gap.
- A_s: no structural story for n = 3. A three-sector coherence
  would be `|r|_2 · |r|_3 · |r|_?` — the framework has no third
  independent sector. An alternative reading as "scalar variance
  on d = 3 dimensions carries `|r|^d`" is post-hoc.
- Ω_c/Ω_b: not an independent closure; follows by matter
  conservation once Ω_b is corrected.

**Step 3 — Contrast with Klein-antipodal Z₂ rep machinery.** The
structural derivations passing Z1-Z3 (Ω partition 13:5:1/19,
down-type factor 6, up-type factor 9) force their specific
factorization from the (sym, antisym) eigenmode decomposition.
The hybrid strategy does not: the exponent `n` is read off
observation rather than from a theorem.

**Step 4 — Default to Class 2 if no forcing mechanism in one
sitting.** No forcing mechanism produced.

## Circularity of `|r|` at M_Z

`|r| = 0.968` is derived in `duty_cycle_dictionary.md` §2 as

    |r|  =  27 / (8 · α_s/α_2)        at M_Z

i.e., the ratio of the **declined** bare K=1 identity (α_s/α_2 = 27/8,
Class 3 numerology, 3.2% off) to the **observed** value at M_Z.
The framework does not independently compute `|r|`'s value at M_Z;
`|r|` is defined from the α_s/α_2 gap.

Using `|r|` to close Ω_b therefore restates one observational
deviation (α_s/α_2 miss) in terms of another (Ω_b miss). The
relation `1 − |r|² ≈ 2 · (1 − |r|) ≈ 6.3%` is algebraically
close to the observed Ω_b deviation of 6.33%, but the mechanism
tying the two deviations across sectors (particle → cosmological)
is not specified.

Specifically, `duty_cycle_dictionary.md` §Status declines the
decoherence-tax reading at the particle scale:

> "Originally, the 1-3% residuals to M_Z observations were
> attributed to a 'decoherence tax' from unlocked modes at
> K < 1. That attribution has since been ruled out."

Phase B reintroduces the decoherence-tax reading at the
cosmological scale while the framework has ruled it out at the
particle scale. The same `|r|`, same interpretation, opposite
retention status across sectors — structurally inconsistent.

## Verdict

| Item | Hybrid closure | Status |
|---|---|---|
| Ω_b = (1/19)·|r|² | numerical match 0.1σ | **Class 2** (numerology cloud). Exponent 2 ansatz-selected; `|r|` observation-derived; decoherence-tax reading inconsistent across sectors. |
| Ω_c/Ω_b via matter conservation | numerical match 0.5σ | **Not independent**; inherits Ω_b's status. |
| A_s = 2.33·|r|³ × 10⁻⁹ | numerical match < 1σ | **Class 2** (numerology cloud). Exponent 3 ansatz-selected; no cross-sector / cross-dimension theorem forces it. The G1-G5 structural gaps in `a_s_geometric_proof.md` remain the framework's acknowledged obstruction. |

The hybrid strategy produces numerical matches but fails the
Z2 criterion (un-derived O(1) factors — here, the O(1) exponent
`n` chosen per observable). It joins the list of Class 2 items
alongside `d_eff = 80/27`, Klein nodal parity, `K_STAR^14 = 1/8`,
26:7:1, and `N_efolds = √5/rate`.

## What this audit does not say

- **Not**: the numerical matches are wrong. They are real to the
  stated precision.
- **Not**: `|r|` is un-physical. It is a legitimate reading of
  the α_s/α_2 gap; it simply is not structurally derived in the
  framework's current form.
- **Not**: the Ω_b residual is closed. The `omega_b_enumeration`
  Floor item remains at 6.7%/11σ, same as before this audit.
- **Not**: A_s is closed. The geometric proof's `%-only` status
  at 11% / 7.7σ (per `a_s_geometric_proof.md` §Status) is the
  framework's current claim, with G1 (horizon-crossing
  amplification) identified as the dominant structural gap.

## What closure would require

For the hybrid strategy to pass Z1-Z3:

1. **Structural derivation of `|r|` at M_Z from framework
   primitives.** Currently `|r|` is defined from the α_s/α_2
   observation; it must instead be computed independently and
   then *checked* against observation. The framework does not
   yet supply this.
2. **Forcing argument for the exponent `n` per observable.** For
   Ω_b, a theorem showing the Klein-singlet ψ_+(1, 5) experiences
   exactly `|r|²` suppression (as opposed to `|r|`, `|r|³`, or
   any other power), stated in terms of the (sym, antisym) eigenmode
   decomposition. For A_s, a theorem showing `|r|³` rather than
   `|r|²` or `|r|⁴`.
3. **Cross-sector consistency with the particle-scale null.**
   Either the decoherence tax is structurally real (in which case
   `duty_cycle_dictionary.md` §Status must be revised) or it is
   not (in which case Phase B must be withdrawn).

None of these three are supplied. Until they are, the hybrid
strategy is a Class 2 numerology match, not a structural closure.

## Propagation

- `framework_status.md` Floor table: unchanged — the Floor items
  are not closed by this audit.
- `numerology_inventory.md` Class 2: add `Ω_b = (1/19)·|r|²`,
  `A_s = 2.33·|r|³ × 10⁻⁹` with this file as source.
- `omega_b_residual_phase_b.md`: add Status header noting Class 2
  demotion and pointing here.

## Cross-references

| File | Role |
|---|---|
| `ansatz_audit_policy.md` | Triage procedure applied here |
| `omega_b_residual_phase_a.md` | Three-way inconsistency setup |
| `omega_b_residual_phase_b.md` | Hybrid closure proposal (demoted here) |
| `a_s_geometric_proof.md` | A_s structural proof; G1-G5 structural gaps |
| `duty_cycle_dictionary.md` | `|r|` definition at M_Z; decoherence-tax null |
| `baryon_fraction.md` | Klein-singlet ψ_+(1, 5) derivation; Ω_b = 1/19 |
| `klein_antipodal_z2_rep_pattern.md` | Positive pattern contrast |
| `numerology_inventory.md` §Class 2 | Receiving class |
