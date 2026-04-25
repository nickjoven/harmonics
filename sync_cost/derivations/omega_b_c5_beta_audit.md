# Ω_b C5 closure: β-forcing audit

## What this file is

A direct audit of the exponent β in the C5 closure
(`omega_b_c5_closure.md`), per `ansatz_audit_policy.md`. The
question: is β = 1/12 forced framework-natively, or does the
closure default to Class 2 because multiple candidate β values
match observation within precision?

**Verdict: NULL on β-forcing.** Three candidate β values lie
within 4% of the required value, none has a derivation
producing the specific exponent. Per the policy, this defaults
the closure from Class 4 candidate to **Class 2 with
qualitative structure intact**: the mechanism (w runs with H
via framework-derived a_0(z)) is substantive; the specific
exponent identification is not yet structural.

## What was tested

The C5 functional form `w(z) = 1 − α·(H_0/H(z))^β` requires two
parameters. Empirical least-squares fit on the three observables
(Ω_Λ, Ω_b, Ω_DM) at z ∈ {0, 1090, 3400} gives:

```
α_best = 0.177  (vs framework 1/INTERACT = 1/6 = 0.167; 6% off)
β_best = 0.104
```

Holding α = 1/6 fixed (forced by `w(0) = MEDIANT/INTERACT`),
the required β to fit Ω_b exactly is `β_required ≈ 0.0804`.

## Candidate β values

Tested by computing `χ² = Σᵢ (residualᵢ%)²` across all three
observables with α = 1/6:

| β candidate | Value | Off req. | Max residual | χ² |
|---|---|---|---|---|
| 1/(4π) (geometric) | 0.0796 | 1.0% | 0.32% | **0.108** |
| 1/12 = 1/(2·INTERACT) | 0.0833 | 3.6% | 0.28% | 0.117 |
| λ_unlock/INTERACT | 0.0788 | 2.0% | 0.33% | 0.122 |
| 1/11 = 1/(q_2³+q_3) | 0.0909 | 13% | 0.69% | 0.51 |
| 1/14 = 1/(q_2²+q_3²+q_3) | 0.0714 | 11% | 0.65% | 0.60 |
| 2/(MEDIANT·INTERACT)=1/15 | 0.0667 | 17% | 1.01% | 1.27 |
| 1/(2π·√2) | 0.1125 | 40% | 1.88% | 3.54 |
| (1−φ⁻⁴)/INTERACT | 0.1424 | 77% | 3.15% | 9.99 |
| λ²/INTERACT | 0.0373 | 54% | 3.73% | 14.93 |

**Top three are statistically equivalent**: all give max
residual <0.35% on every observable. χ² differences are
0.108 → 0.117 → 0.122 — well within data precision.

**1/(4π) is marginally the best fit** (lowest χ²) but **1/12
is best on max-residual** (most uniform). Neither is
operationally distinguishable from the other given current
data precision.

## Forcing-argument audit per `ansatz_audit_policy.md`

### Step 1 — Enumerate alternative `f`s built from same framework integers

Three candidates within 4% of required β, all framework-flavored:

- **1/(4π)**: pure geometric constant, not a framework integer.
  Appears in standard physics solid-angle integrals.
- **1/12 = 1/(2·INTERACT) = 1/(q_2²·q_3)**: framework-integer.
  Same 12 appears in down-type derivation
  (`down_type_double_cover_closed.md`).
- **λ_unlock/INTERACT**: ratio of Klein-bottle Lyapunov rate to
  gauge orbit count. Both pieces framework-canonical.

Multiple candidates exist. **Step 1 fails**: the selection is
not uniquely forced by Z₂ rep theory or framework integers.

### Step 2 — Forcing argument for the specific β

For each candidate, what theorem would force it?

**1/(4π)**: standard inflation does not give β = 1/(4π) as a
running exponent. The 4π appears in amplitude prefactors
(8π² in the A_s formula) and in solid-angle integrals, but no
de Sitter calculation produces 1/(4π) as the exponent of
w(z) with respect to (H_0/H). **No forcing argument exists in
standard physics or framework.**

**1/12**: the down-type derivation produces 12 = q_2²·q_3 in
fermion-mass context, not cosmological running. Reusing 12 here
would require a Klein-antipodal Z₂-rep derivation specific to
the boundary-weight running with H — a derivation that has not
been produced. **No forcing argument supplied; would need a
new theorem connecting Klein double-cover mode count to
H-running.**

**λ_unlock/INTERACT**: the ratio is dimensionally consistent
(rate per orbit) but no specific calculation in the framework
gives this as the H-running exponent. **No forcing argument.**

**Step 2 fails**: no candidate has a forcing argument within
one sitting.

### Step 3 — Contrast with positive Klein-antipodal pattern

The framework's load-bearing Klein-antipodal Z₂-rep
derivations (`klein_antipodal_z2_rep_pattern.md`) produce
specific framework integers via specific orbit-counting
theorems:

- Down-type factor 6 = `q_2 · q_3` from S_3 orbit dimensions on
  Z_2 × Z_3
- Up-type factor 9 = `q_3²` from Klein parity on Fibonacci shift
- Ω partition 13:5:1/19 from Z_6 antipodal × coprime-to-6

In each case, the integer is **uniquely** produced by a
specific theorem. For β = 1/12 to qualify as the same kind of
result, we would need a theorem of the form: *"the running of
w with respect to H(z) has exponent set by the count of
Klein-antipodal modes in the double-covered Z_6 lattice =
2·INTERACT = 12."* No such theorem exists.

**Step 3 fails**: the Klein-antipodal pattern does not
distinguish 1/12 from 1/(4π) without a specific running
theorem.

### Step 4 — Default verdict

Per `ansatz_audit_policy.md`:

> *"Default Class 4 → Class 2 if the audit can't produce a
> forcing mechanism within one sitting."*

**Default applies.** The C5 closure's specific (α=1/6, β=1/12)
identification is **Class 2 numerology**, even though the
qualitative structure (running w with H via framework-derived
a_0(z)) is structural.

## What survives the audit (qualitative Class 4)

The audit downgrades the *specific* parameter identification
but leaves intact:

1. **Qualitative C5 mechanism**: w(z) runs with H(z), driven by
   framework-derived a_0(z). The three observables consistent
   under one running function. **Substantive structural claim**;
   no anchor import; mechanism is framework-internal.

2. **α = 1/INTERACT (= 1/6)**: this parameter has no close
   competitors within 5% other than the empirical fit value
   0.177. The framework-integer interpretation is consistent
   with data (within Planck precision) and natural
   (`MEDIANT/INTERACT = 5/6` is the framework's canonical ratio
   between adjacent Klein operations). **Class 4 candidate** —
   stronger than β.

3. **34× residual reduction on Ω_b** (from 6.7% to 0.2-0.3%):
   real and meaningful. Even with β as ansatz, the C5 mechanism
   substantially closes the framework's largest scorecard
   miss.

## What the audit produces

A clear two-tier reading:

**Tier 1 — Qualitative structure (Class 4 candidate):**

The framework predicts boundary weight w runs with H(z) via
some saturating function. This running, combined with standard
cosmology z-effective values, reduces the three-way Ω partition
inconsistency to <0.4% on all observables. **Mechanism is
structural; no anchor import; substantive closure of the
largest Floor residual.**

**Tier 2 — Specific parameter identification (Class 2):**

The specific identification (α=1/6, β=1/12) matches observation
within precision but is one of several equally-good ansatz
candidates. β = 1/(4π) actually fits marginally better.
**Without a forcing theorem for the specific exponent, the
parameter identification is numerology, not structural
derivation.**

## Comparison to A_s

The A_s G1 closure attempt (`a_s_g1_closure_attempt.md`) failed
at Tier 1: the mechanism itself was anchor-side (H_inf
required), and no substrate-side mechanism for inflation
amplification exists. So A_s landed as category statement.

The Ω_b C5 closure passes Tier 1 (substrate-side mechanism
exists and works) but fails Tier 2 (specific β unforced).
Asymmetry: A_s is dissolved category; Ω_b is structural
mechanism with un-forced numerics.

Both differ from the canonical structural derivations
(down-type 6, up-type 9, Ω partition 13:5:1/19) which pass
both tiers — mechanism + uniquely-forced parameters.

## What would upgrade Ω_b C5 to Class 5

Either of:

1. **Forcing theorem for β = 1/12**. Most natural form: *"the
   running exponent of w with respect to log(H) is set by the
   count of Klein-antipodal Z₂-rep modes in the double-covered
   Z_6 lattice."* Number-of-modes argument: 12 = 2·INTERACT
   from sym + antisym pairs over each of 6 antipodal pairs. The
   factor 2 from sym/antisym would need to specifically appear
   in the running, which currently is asserted but not derived.

2. **Forcing theorem for β = 1/(4π)**. Most natural form: *"the
   running exponent of w(H) is set by solid-angle measure on
   the de Sitter horizon."* This would require a framework-
   derivation of de Sitter geometry from the substrate (which
   the framework currently treats as continuum-limit, per
   `continuum_limits.md`). Plausible but not currently in scope.

Both directions are non-trivial structural work. Neither is a
single-session audit.

## What would re-open the audit

If higher-precision data shifts β_required away from both 1/12
and 1/(4π), the audit re-opens with new candidates. Current
Planck precision (σ_obs / Ω_obs ≈ 1%) does not distinguish
between the top three candidates.

Future CMB experiments (CMB-S4 etc.) could potentially shrink
the precision enough to distinguish β = 1/12 from β = 1/(4π).
Current data does not.

## Update to `omega_b_c5_closure.md`

The Class 4 candidate verdict in that file should be revised:

- **Tier 1 (mechanism)**: Class 4 candidate stands.
- **Tier 2 (specific parameters)**: Class 2 by ansatz default.

The 34× residual reduction is unchanged in fact; the structural
status of the specific exponents is reduced.

`framework_status.md` Ω_b entry should reflect this two-tier
reading: substantive Class 4-qualitative closure, Class 2
parameter identification, audit pending for β-forcing.

## Cross-references

- `omega_b_c5_closure.md` — the closure being audited; verdict
  here is Tier 2 demotion to Class 2
- `ansatz_audit_policy.md` — policy applied (Step 4 default)
- `klein_antipodal_z2_rep_pattern.md` — positive structural
  examples this closure does NOT rise to
- `down_type_double_cover_closed.md` — uses 12 = q_2²·q_3 in
  particle context; would need analogous cosmological theorem
  for β-forcing
- `framework_status.md` — Ω_b entry needs two-tier update
- `omega_b_substrate_side_audit.md` — earlier audit confirming
  Ω_b is substrate-side (which this closure honors)
- `a_s_g1_closure_attempt.md` — parallel closure with opposite
  failure mode (Tier 1 failure)
