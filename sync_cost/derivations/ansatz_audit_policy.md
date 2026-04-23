# Ansatz audit policy — triaging Class 4 candidates

## What this file is

A short policy note derived from three consecutive Class 4 → Class 2
demotions in the 2026-04-23 session. The demotions all followed the
same structural pattern; future Class 4 candidates should be
triaged against this pattern directly rather than allowed to linger
as "pending audit."

## The pattern

A Class 4 proposal takes the form:

> "Observation X equals `f(framework integers)` at z-score ≤ 1σ.
> The specific `f` uses only framework-native quantities; therefore
> the claim is structural."

The pattern fails Z2 (no un-derived O(1) factors) when the specific
combination `f` is one of several candidates built from framework
integers, selected because it matches observation rather than
derived from a structural argument.

## The three demotions

| Claim | f | Z1 match | Audit verdict |
|---|---|---|---|
| `sin²θ_W = 2^{80/27}/(2^{80/27}+3^{80/27})` | `d_eff = d − 1/q₃^d` | 0.5σ | G1 pilot: three mechanisms tested, none produces the substitution |
| Klein nodal parity (odd-m Möbius, (5,5,1)) | sign-flip under Z₂ quotient | single image | Simulator uses `Y²` which is Z₂-symmetric for all ℓ |
| `K_STAR^14 = q_2^{−q_3} = 1/8` | exponent = −q_3 in 14-EDO basis | 0.594σ | Alternative exponents from framework integers differ by >10% from observation, but the choice of `−q_3` is not structurally forced |

In all three, the numerical match was real; the structural
derivation of the specific `f` was not.

## Triage procedure

When a candidate is proposed or re-inspected as Class 4:

1. **Enumerate alternative `f`s built from the same framework
   integers.** If multiple candidates are constructible and only
   one (or a few) matches observation, the selection is an ansatz.
   Fails Z2 unless a forcing argument is produced.

2. **Identify the specific structural argument.** The proposal must
   point at a theorem (existing or proposed) that forces the `f`.
   "Framework-native factorization" alone is not a structural
   argument — it's re-description. Ask: *what would change if the
   `f` were slightly different?* If nothing in the framework breaks,
   the `f` is not forced.

3. **Prefer the Klein-antipodal Z₂ rep machinery** as the positive
   example to contrast against (`klein_antipodal_z2_rep_pattern.md`).
   Structural derivations in this repo that pass Z1-Z3 cleanly
   (Ω partition, down-type factor 6, up-type factor 9) use that
   machinery. Proposals that don't fit the pattern have an uphill
   structural argument.

4. **Default Class 4 → Class 2 if the audit can't produce a forcing
   mechanism within one sitting.** Leaving Class 4 items open past
   a failed audit accumulates the same "walking ground backwards"
   cost the session has been paying down.

## What this isn't

- **Not a blanket rule against near-matches.** Near-matches are
  legitimate to notice and record. Class 2 is the right home for
  them.
- **Not a policy against Class 4 audits being slow.** Genuine
  structural arguments can take real time. The policy is about
  proposals that *don't* have a structural argument in sight after
  the first careful look.

## Applications

Any Proposed item in `framework_status.md` fitting the ansatz
pattern should go through this triage before further session
effort. Current candidates (as of 2026-04-23):

- **26:7:1 generation hierarchy** (rational exponent a): fits the
  pattern (framework-integer expression matching observation
  without a forcing argument for the specific a). Expected audit
  outcome: Class 2.
- **N_efolds = √5 / rate ≈ 61.3**: framework has √5 from the
  fixed-point polynomial but the rate identification may or may
  not close. Run the same triage.

Items that do **not** fit the ansatz pattern (structural
derivations from Klein-antipodal Z₂ rep theory):

- Down-type factor 6 (in scorecard, 0.04σ).
- Up-type factor 9 (0.34σ).
- Ω partition 13:5:1/19 (Survives).

## Cross-references

- `klein_antipodal_z2_rep_pattern.md` — the positive structural
  pattern
- `numerology_inventory.md` §Class 2 — where ansatz demotions land
- `statistical_conventions.md` — Z1-Z3 definitions
- `problem/sin2_theta_w_deff_80_27/` — worked example of a full
  pilot audit (G1 null)
- `CHAIN_KSTAR.md` — worked example of an inline audit (Step 6
  demoted, Steps 1–5 retained)
