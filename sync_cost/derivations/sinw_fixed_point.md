# sin²θ_W Fixed-Point Hypothesis — Negative Result

## The hypothesis

`sinW_running_check.py` identified two mutually exclusive branches
for explaining the 1.1% residual between the framework's tree-scale
identity sin²θ_W = 8/35 = 0.22857 and the observed value 0.23121 at
M_Z:

- **Branch (i):** The tree scale is not M_Pl. Some other scale
  μ_tree is identified with K=1 self-consistently.
- **Branch (ii):** The framework's "running" is the K→μ duty-cycle
  mapping, not SM 1-loop RG.

The gut hypothesis: if both branches are true **simultaneously**,
their joint truth might close on a fixed point. Specifically, there
might exist a single K* (together with an identification of μ_tree)
such that the framework's duty-cycle identities reproduce **both**
α_s/α_2 = 3.488 and sin²θ_W = 0.23121 at M_Z.

`sinw_fixed_point.py` tests this hypothesis directly.

## The test

Step 1 establishes the K-grid and confirms the analytic duty(q, K)
formula has a discontinuity at K=1: the perturbative limit is
duty(2)/duty(3) → 4.5 as K→1⁻, while the critical (Ford-circle)
formula gives 27/8 = 3.375 at K=1. Neither matches observed 3.488.

Step 2 discards the analytic approximation and uses **actual
numerical tongue widths** measured from the circle-map dynamics:

    θ_{n+1} = θ_n + Ω - (K/2π) sin(2π θ_n)

The 1/3 tongue center shifts to Ω ≈ 0.34 at K near 1 (not 1/3,
because the sin term carries a nonzero phase average over the
3-periodic orbit). Scanning K ∈ [0.93, 0.99] and measuring the
true locking intervals:

| K     | duty(2)  | duty(3)  | ratio d2/d3 | sin²θ_W |
|-------|----------|----------|-------------|---------|
| 0.93  | 0.03212  | 0.00805  | 3.993       | 0.2003  |
| 0.94  | 0.03212  | 0.00834  | 3.850       | 0.2062  |
| 0.95  | 0.03212  | 0.00834  | 3.850       | 0.2062  |
| 0.96  | 0.03212  | 0.00864  | 3.718       | 0.2120  |
| 0.97  | 0.03492  | 0.00924  | 3.780       | 0.2092  |
| 0.98  | 0.03492  | 0.00953  | 3.662       | 0.2145  |
| 0.99  | 0.03492  | 0.00953  | 3.662       | 0.2145  |

**Observed at M_Z:** α_s/α_2 = 3.488, sin²θ_W = 0.23121.

## The result

**Neither constraint is met at any K in the critical window.**

- Numerical α_s/α_2 ratio ∈ [3.66, 3.99]. All **above** observed
  3.488. No K* reproduces it.
- Numerical sin²θ_W ∈ [0.200, 0.214]. All **below** observed
  0.23121. No K* reproduces it.

The joint fixed-point question is moot: if neither constraint alone
is satisfied by any K, no single K can satisfy both.

## What this means

The framework identity **sin²θ_W = 8/35** comes from a
**measure-theoretic** formula — the Ford-circle / Gauss-Kuzmin
measure of the rational p/q tongues in the tongue-filling limit.
It is the "idealized duty" duty(q) = 1/q^d evaluated at the
spatial dimension d = 3, and yields sin²θ_W = 8/35 = 0.22857.

But the **actual** tongue width at finite K < 1 (measured
numerically) gives duty values that do **not** satisfy the
1/q³ relation. At K = 0.99, the numerical ratio is 3.66, not
3.375, and sin²θ_W = 0.214, not 8/35.

So the framework's 8/35 is **not** the value of the dynamical
duty ratio at any specific K. It is the Gauss-Kuzmin measure of
the tongues in the K=1 tiling, which differs from the actual
tongue width. The two formulas agree only in the asymptotic sense
where the devil's staircase tiles Ω with measure 1.

This has two immediate consequences:

1. **The 1.1% residual at M_Z is not a running effect.** It is
   the gap between the Gauss-Kuzmin measure (8/35 = 0.2286) and
   the electroweak-scale observation (0.23121). There is no K
   value at which the framework's numerical dynamics gives
   0.23121.

2. **The near-coincidence at M_Z is better than the framework's
   own dynamical prediction.** 8/35 agrees with observation at
   1.1%, while the numerical duty ratio at K = 0.99 gives 0.214,
   disagreeing at 7.3%. The measure-theoretic identity is
   **closer** to reality than the dynamical prediction.

## Why the hypothesis failed

The fixed-point picture assumed that 8/35 and 0.23121 were
connected by a smooth framework running in K. The test shows
this is not the case: 8/35 is not reached by the dynamics at
any K. It is a different object (a measure), and its agreement
with observation at 1.1% is a numerical coincidence, not a
derivation through running.

The two branches remain both defensible as interpretations of
the diagnostic, but they are not compatible in the way the
fixed-point reading required:

- **Branch (i)** is formally consistent (define μ_tree ≈ 54 GeV
  such that SM-run sin²θ_W = 8/35 at that scale), but μ_tree
  has no independent framework meaning — it is not M_Pl, not
  M_GUT, not the electroweak VEV, not v/q₂, not any scale the
  framework derives from elsewhere.

- **Branch (ii)** is numerically false: the framework's K→μ
  mapping, implemented via actual circle-map tongue widths, does
  not run 8/35 into 0.23121 at any K.

## The honest update

The sin²θ_W = 8/35 identity should be reclassified in
`duty_cycle_dictionary.md` and `gauge_sector_lovelock.md` as
a **measure-theoretic identity** that holds at a 1.1% level
at the electroweak scale, not as a derivation. It is a
near-coincidence: the smallest nontrivial rational of the form
q_2^d / (q_2^d + q_3^d) with d = 3 happens to be within 1.1%
of sin²θ_W(M_Z).

This does not falsify the framework. It downgrades one specific
claim from "derivation" to "numerical near-coincidence", and
removes the requirement that 8/35 be explained by any running
(SM or framework). The gauge-group derivation in
`gauge_sector_lovelock.md` still stands — it gives
SU(3) × SU(2) × U(1) uniquely. What it does not give is the
specific value of sin²θ_W at M_Z; that value is observed, not
derived.

The framework's strongest sin²θ_W-related prediction that
remains honest is the **structural** one: the electroweak mixing
angle is a rational of the form q_a^3 / (q_a^3 + q_b^3) for
q_a, q_b the two Klein-bottle denominator classes, and 8/35 is
the unique such rational with (q_a, q_b) = (2, 3). Whether this
rational coincides exactly with the measured value is a numerical
question that the topology alone does not settle — and the answer
is "to 1.1%, yes, but not exactly".

## Closure notes

- `sin²θ_W = 8/35` in the duty-cycle dictionary is a
  **measure-theoretic near-coincidence**, not a running result.
  The 1.1% residual is NOT from running.
- The dichotomy (i) / (ii) for sin²θ_W running is resolved by
  rejecting both. Neither branch produces the observed value
  through running; the tree-scale identity is a measure, not a
  dynamical quantity.
- The framework's derivation of the gauge group via Cartan +
  Utiyama (D42) is not affected — it only uses the center
  Z_2 × Z_3, not the specific sin²θ_W value.

4. `gauge_sector_lovelock.md` Part V, item 8 ("coupling ratios
   follow from q₂ = 2, q₃ = 3, d = 3") should be annotated to
   flag sin²θ_W and α_s/α_2 as measure-theoretic near-coincidences
   at the few-percent level, not derivations via running.

## Status

**Hypothesis falsified numerically.** No fixed point exists where
the framework's K→μ dynamics reproduce both α_s/α_2 and sin²θ_W
at M_Z. The 1.1% agreement of 8/35 with observed sin²θ_W is a
near-coincidence of a topological rational with an electroweak
measurement, not a dynamical consequence of the framework.

**The gut was wrong.** Or rather: the two branches are not
simultaneously true in the way that would produce a fixed point.
Branch (ii) is numerically false in the dynamical sense;
Branch (i) is formally possible but physically meaningless.

**Scripts**: `sinw_fixed_point.py`, `sinW_running_check.py`.
