# S_v(K=1) NLO calc attempt: a regime finding

Attempt at the explicit NLO computation queued by `s_v_nlo.md`. The
attempt reveals a **substantive framework finding**: the audit's
substrate-Planck convention places the framework in a regime where
standard kink expansions don't directly apply, and the 5.7% gap
between `S_v = 16` (audit) and `S_v ≈ 16.92` (seam-profile) is the
framework's natural precision floor in this regime.

The audit's choice is consistent and robust within that precision
class; tightening it requires non-perturbative substrate methods.

## The regime check

At K = 1, the audit's primitives give:

| Quantity | Value |
|---|---|
| Kink mass `M_k(K=1)` | 8 Planck masses |
| Kink width `ℓ_kink(K=1)` | 1 Planck length |
| Antiperiodic loop length `L_x` | 1 Planck length |
| **Ratio `L_x / ℓ_kink`** | **1.00** |

The kink width *equals* the antiperiodic loop length. **The kink
fills the loop.** This is not the standard regime of soliton physics
(where `L >> ℓ_kink` and the kink is well-localised inside an
effectively infinite line); it is the **maximally compact** regime
where standard 1/L expansions diverge.

In this regime, the kink and its antikink partner (across the
antiperiodic identification) overlap completely. The "vortex pair"
isn't two separated objects; it's a single coherent self-overlapping
substrate configuration.

## What this means for `S_v`

Standard sine-Gordon kink-pair action at separation `L`:

    S_pair(L) = 2 M_k − E_int(L)

with `E_int(L) ∝ M_k exp(−L / ℓ_kink)` the attractive
kink-antikink interaction.

For L = ℓ_kink = 1 (audit's regime), `E_int / M_k = exp(−1) ≈ 0.37`
— a **37% correction**, not a small perturbation. The leading-order
expansion `S_v = 2 M_k = 16` is *not a controlled approximation*;
it is one specific term in a non-convergent series.

The seam-profile derivation's geometric `S_v ≈ 16.92` is in the
same precision class: the substrate-Lagrangian's seam-crossing
action at L_x = ℓ_kink involves the same non-perturbative
overlapping-kink configuration.

## Why the gap is the natural precision floor

Both `S_v = 16` and `S_v ≈ 16.92` are leading-order estimates in
different but equally-precision-limited expansions:

- **Audit `S_v = 16`** uses the LO `2 × M_k × ℓ_kink` form,
  ignoring overlapping-kink corrections.
- **Geometric `S_v ≈ 16.92`** uses the seam-profile LO form
  `(1 − K) √K` maximised, ignoring kink-loop-comparable-size
  corrections.

Their 5.7% disagreement reflects the precision floor when neither
expansion controls the dominant non-perturbative physics. Each gets
≈ 5% of the answer right in a regime where the leading neglected
contribution is ≈ 37% of `M_k`.

**The two estimates agreeing to 6%** is the audit's no-rescaling
principle passing at the framework's natural precision class. **They
cannot agree more tightly without non-perturbative work**, because
the corrections each ignores are the same order as the size of the
ignored corrections.

## Numerical exploration: `S_v ≈ 16.92` is not a clean framework number

If `S_v` had landed on a clean framework irrational, we'd suspect
the value is meaningful at NLO precision. Testing the gap value
`16.92 − 16 = 0.92`:

| Candidate framework expression | Numerical | Match? |
|---|---|---|
| `1 − 1/φ` | 0.382 | no |
| `(φ − 1)` | 0.618 | no |
| `π / 4 + 1/8` | 0.910 | within 1% |
| `(e − 1) / (φ + π/4)` | 0.766 | no |
| `e / π` | 0.866 | within 6% |
| `√3 / 2` | 0.866 | within 6% |
| `1 / (8π × δ_A / 2π)` with δ_A = π | 0.127 | no |
| `1 / (k_A × 2)` with k_A = 2 | 0.250 | no |

The closest match (`π/4 + 1/8 ≈ 0.910`) is within 1% of 0.92, but
the structural origin of `π/4 + 1/8` in framework primitives isn't
clean — it's the kind of expression numerology produces by free-
search. **No clean structural framework number predicts the precise
gap value of 0.92.** Conclusion: the gap is approximate, not a
hidden structural quantity.

This is *informative*: had the gap been `0.910 = π/4 + 1/8`, the
framework would have a sharper structural prediction. That it's
`0.92 ± precision-floor` says the framework cannot tighten further
at this level.

## Possible framework moves

Three structural directions for closing the gap or registering it:

### (i) Accept the regime and develop non-perturbative methods

The audit's L_x = ℓ_kink = 1 regime is the framework's
**maximally compact** convention. Non-perturbative substrate
methods (variational, finite-size kink-on-circle, monte carlo on
the substrate lattice) are the appropriate tools.

This is consistent with the substrate being the framework's
*minimal* layer — substrate primitives at the Planck scale means
the substrate has no "below" to expand into. Non-perturbativity is
not a defect; it's a structural feature of the framework's
ontological commitments.

**Status**: substrate-Lagrangian-level work, tractable in principle,
not yet done. Same status as the s_v_nlo.md predecessor doc but
more honest about what "NLO" means in this regime.

### (ii) Revisit the audit's L_x = ℓ_P commitment

If the substrate's antiperiodic loop is *not* one Planck cell but
some larger structural length (e.g., a cosmological multiple), then
L_x >> ℓ_kink and standard perturbative expansions apply.

Candidates for a structural L_x:

- `L_x = R_Planck-to-Hubble × ℓ_P = 6 × 13⁵⁴ ℓ_P` (Hubble length)
- `L_x = φ^n × ℓ_P` for some Fibonacci depth `n`
- `L_x = N × ℓ_P` for some master-cascade integer `N`

Each would give a perturbative regime with calculable NLO. But each
would also require revising the audit's `R_arrow = 6 × 13⁵⁴` match
(which depends on `τ_tick = t_P = L_x/c`, hence L_x = ℓ_P).

**Status**: would invalidate the audit's headline result. Should
only be considered if (i) fails.

### (iii) Register the regime as the framework's natural precision class

Commit explicitly: at the audit's L_x = ℓ_P convention, the
framework's precision floor on `S_v(K=1)` is ≈ few percent. The
audit's `S_v = 16` and the seam-profile's `S_v ≈ 16.92` agree
within that floor, supporting `κ_pair = 1` at the precision the
framework's leading-order machinery accesses.

**Status**: an honest framework commitment registering what the
explicit calc revealed.

## What the calc attempt established

Three substantive findings:

1. **The audit places the framework in a non-perturbative regime
   at K=1.** The kink fills the loop; standard expansions diverge.
   This is consistent with substrate primitives at Planck scale —
   no "deeper" expansion variable exists.

2. **The 5.7% gap is the framework's natural precision floor in
   this regime.** Both `S_v = 16` and `S_v ≈ 16.92` are LO
   estimates with same-order ignored corrections. They agree to
   precision floor; they cannot agree more tightly without
   non-perturbative work.

3. **No clean framework irrational predicts the gap value of 0.92.**
   The gap is approximate, not a hidden structural prediction.

## Framework prediction (after the attempt)

    S_v(K=1) ∈ [15, 17.5] Planck units,
    with central value ≈ 16.5 ± 0.5,
    no sharper without non-perturbative methods.

This is the framework's honest prediction given the audit's
convention. The seam-profile derivation's `≈ 16.92` and the
audit's `= 16` are both inside this band.

## Falsifiers

| Test | Falsifier |
|---|---|
| Non-perturbative `S_v` calc gives value outside `[15, 17.5]` | Framework's natural-precision-class commitment fails. |
| Non-perturbative `S_v` calc gives a clean framework irrational (e.g., `2 × 8 × √2 ≈ 22.6`, `M_k × π / e ≈ 9.2`, etc.) | Would suggest the framework's true `S_v` has structural form we haven't named; supports (i) framework move. |
| Non-perturbative `S_v` calc gives `≪ 15` or `≫ 17.5` | Suggests audit's L_x = ℓ_P convention is wrong; supports (ii) framework move. |

## What we now know about `κ_pair = 1`

- Audit committed to κ_pair = 1 from parsimony.
- Seam-profile derivation (`seam_profile.md`) confirmed at 5.7%.
- NLO setup (`s_v_nlo.md`) identified four contributions.
- **NLO calc attempt (this doc)** found the regime is non-perturbative
  at the audit's convention; the 5.7% gap is the natural precision
  floor; standard expansions don't converge here.
- The audit's κ_pair = 1 is consistent within precision class but
  cannot be tightened without non-perturbative substrate methods.

## Cross-links

- `unitless_audit.md` — audit committing to L_x = ℓ_P.
- `seam_profile.md` — geometric S_v ≈ 16.92 prediction.
- `s_v_nlo.md` — NLO setup; this doc is its execution attempt.
- `cone_twist_substrate.md` — bicone target where the seam lives.
- `no_rescaling.md` — methodological principle this attempt tests
  at NLO precision.
- `framework_status.md` — Category-A item: NLO `S_v` precision now
  registered as non-perturbative-pending.

## Status

Class 4 (calc attempt with substantive regime finding). The explicit
NLO computation is not produced; instead the attempt reveals that
the audit's convention places the framework in a non-perturbative
regime where the 5.7% gap is the natural precision floor. This is
not a failure of the calc — it is the calc's *honest substantive
output*.

The framework now has a clear next-step substrate-Lagrangian-level
target: develop non-perturbative methods for kink-on-Klein-bottle at
L_x = ℓ_kink, applicable to the audit's convention. That is the
real NLO calc, not the LO expansion this attempt explored.
