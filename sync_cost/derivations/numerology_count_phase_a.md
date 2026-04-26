# Numerology count (Region C, Shape B) — Phase A: scope and design

## What this file is

Phase A planning for the framework's first **break-the-loop** multi-
session derivation, committed as the methodology shift from
single-session audits to multi-session structural work.

Region C from `remaining_gap_shapes.md` Shape B: a combinatorial
test of whether the framework's particle-numerology cloud (1-3%
near-matches: `m_H/v = 1/2`, `λ_H = 1/8`, `α_s/α_2 = 27/8`,
plus all the close-but-not-exact framework-integer expressions
endemic across the audit history) is **statistically expected by
pigeonhole** or **anomalously dense** relative to what the
framework's small-integer arithmetic should produce.

Outcome shape:
- **Cloud is signal** → framework's near-matches carry information;
  the multi-candidate ansatz pattern (`continuity_in_K_nulls.md`
  N12-N13, `omega_b_c5_beta_audit.md`) reflects underlying
  structure not yet derived
- **Cloud is noise** → near-matches are pigeonhole; the framework
  is at its quantitative completion; further closure attempts at
  Class 2 floor will not produce information
- **Inconclusive** → counting was too coarse or too fine; refine

This is a **single binary-shape result** that breaks the honest-
landing loop by producing a non-Class-2-audit verdict.

## Why this and not Region A

Per `klein_bridge_audit_and_probe.md`'s "honest landing loop"
finding: every closure attempt within Region A (Ω_b) reproduces
the same Class 4 mechanism + Class 2 parameter shape because
**the framework's discriminator (ansatz_audit_policy.md Step 4
default) is more discriminating than its closures**.

Region C tests the discriminator's calibration directly. If the
framework's small-integer combinations populate any given range
densely enough that ~3% near-matches are pigeonhole, the
discriminator is correctly demoting them. If they're anomalous,
the discriminator may be over-demoting actual framework signal.

This is the only currently-identified probe that produces a
**different SHAPE of result** rather than another audit outcome.

## Scope

The Phase A deliverable is a **plan**, not the count itself.
Specifically:

1. Define the enumeration domain (which framework integers, which
   operations, which target range)
2. Define the null hypothesis (random expectation under
   pigeonhole) precisely
3. Define the test statistic (count above threshold density)
4. Identify what "signal" vs "noise" verdict requires
5. Specify the implementation (single focused script, multi-day
   if needed, but well-scoped)

Phase B would be running the count and reading the verdict.

## Enumeration domain

### Framework integers (canonical set)

From `framework_constants.py` and the
`vocabulary_is_the_work_pattern.md` Instance 7 secondary finding:

```
Q2 = 2, Q3 = 3
MEDIANT = q_2 + q_3 = 5
INTERACT = q_2 · q_3 = 6
K_QUARK = q_2³ = 8
K_LEPTON = q_3² = 9
F_6 = 13, F_7 = 19  (Farey counts)
plus: φ, λ_unlock, π (from primitives + structural derivations)
```

Operations to enumerate:
- Single ratios: `n/m` for `n, m` in framework integer set
- Powers: `n^k` for small `k ∈ {1, 2, 3}`
- Products: `n · m`
- Specific sectoral combinations: `q_i^a / q_j^b`

Bounded by: total expression count must be tractable (~10⁴ to
10⁵ expressions). Larger and we lose statistical power; smaller
and we miss the full landscape.

### Target observables

The framework's existing scorecard plus standard physics
constants in the relevant ranges:

- Particle sector dimensionless ratios: `m_H/v`, `λ_H`, `α_s/α_2`,
  `α_s/α_em`, `α_em`, `sin²θ_W`, `m_t/m_b`, `m_τ/m_μ`, etc.
- Cosmological dimensionless: `Ω_Λ/Ω_m`, `Ω_DM/Ω_b`, `n_s − 1`,
  `r_T` (tensor/scalar ratio bound), etc.
- Range cap: `[10⁻³, 10³]` to avoid unphysically extreme matches

### Threshold for "near-match"

Three thresholds, evaluated jointly:
- **3%** (the Floor magnitude for the cloud)
- **1%** (tighter, distinguishes clean matches from cloud)
- **0.1%** (precision-floor, identifies essentially-exact matches
  like `Ω_Λ = 76/111`)

## Null hypothesis (pigeonhole expectation)

Under the null:
- Framework integers are random uniform on log-scale within their
  range
- Operations (ratio, product, power) commute with random sampling
- Expected number of near-matches at threshold ε: `E[N_match] =
  N_expressions · ε · N_targets`

For:
- `N_expressions ~ 10⁴`
- `ε = 0.03`
- `N_targets ~ 50` physical observables

```
E[N_match] = 10⁴ · 0.03 · 50 = 15,000  (way too many — saturated)
```

So pigeonhole is **definitely** at play above some
N_expressions. The question becomes: at the framework's ACTUAL
expression count (those that show up in derivations), what's the
expected pigeonhole rate?

Refined null: among the **specific** framework expressions used
in derivations (~50-100 expressions, per scorecard +
`bare_k1_identities.md`), what's the expected near-match rate?

```
E[N_match | scorecard size] = 50 · 0.03 · 50 = 75
```

Still high. Need tighter calibration.

### Refined null hypothesis

The right null is more specific:
- Take all framework integer expressions of a specific FORM
  (e.g., `q_i^a / q_j^b` with `a, b ∈ {1, 2, 3}`)
- For each, compute its value
- Distribute these values on log scale
- Compute the expected match-density to physical observables
  under uniform-random shuffling

The TEST: compare actual framework match count at threshold ε
against this null distribution.

If actual >> null: framework is signal (more matches than chance)
If actual ~= null: framework is noise (matches are pigeonhole)
If actual << null: framework is "anti-signal" (avoids matches —
unlikely but informative)

## Test design

### Step 1 — Enumeration

Generate all framework-integer expressions of specific bounded
forms. Tabulate values, mark each by its derivation status
(Survives / Floor / Class 2 / Eliminated / Fails).

### Step 2 — Match density to observables

For each expression, find nearest physical observable. Compute
relative error. Bin by error (3%, 1%, 0.1%).

### Step 3 — Null comparison

Two methods:
- **Permutation test**: randomly shuffle physical observables;
  recompute match count; repeat 10⁴ times; build null
  distribution. Compare actual count to null distribution.
- **Analytical estimate**: compute density of expression-values
  on log scale; integrate over observable range; compute
  expected match count.

### Step 4 — Diagnostic

Three outcomes:

| Outcome | Interpretation | Loop status |
|---|---|---|
| Actual count >> null (p < 0.001) | Framework cloud is signal | Loop verdict revised: Class 2 demotions are over-demotions; some closures should re-promote |
| Actual count ≈ null (0.05 < p < 0.95) | Framework cloud is pigeonhole | Loop verdict confirmed: framework is at quantitative completion; further closure work won't yield Class 5 |
| Actual count << null (p > 0.999) | Framework systematically AVOIDS near-matches | Unlikely but informative; suggests structural rule we haven't characterized |

## Closure criterion (Phase B's task)

Phase B closes when:
1. Enumeration is comprehensive over the chosen domain
2. Null distribution is computed via permutation test (not just
   analytical estimate)
3. p-value computed for the actual framework match count
4. Verdict is one of the three outcomes above
5. Implication for the audit verdict (Class 2 floor calibration)
   is articulated

## What Phase A does NOT decide

- The full enumeration domain (only sketches it; Phase B refines)
- The specific test statistic details (likelihood ratio vs raw
  count vs density estimate)
- Whether multiple thresholds need joint analysis
- How to handle "exact" matches (like `Ω_Λ = 76/111`) that go
  beyond the threshold framework

These are Phase B refinements.

## Cross-references

### Prior work that motivates the count

- `numerology_inventory.md` Class 1, Class 2 entries — the cloud's
  documented contents
- `framework_status.md` Floor (numerology cloud, 1-3%) section —
  the three load-bearing instances
- `omega_b_c5_beta_audit.md` — most recent multi-candidate ansatz
  example (β = 1/12 vs 1/(4π) etc.)
- `continuity_in_K_nulls.md` N12-N13 — the multi-candidate ansatz
  as RECURRING pattern across closures
- `klein_bridge_audit_and_probe.md` — the "honest landing loop"
  finding that motivates this probe
- `vocabulary_is_the_work_pattern.md` Instance 7 secondary
  finding — the (p−1)/2 = framework integer correspondence
  for primes coprime to 6

### Adjacent concerns

- `ansatz_audit_policy.md` — the policy whose calibration this
  tests
- `statistical_conventions.md` — Z1-Z3 status definitions
- `bare_k1_identities.md` — the explicit list of single-integer
  ratios the framework uses

## Phase B trigger

Phase A is complete with this document. Phase B begins when:
- User commits to running the count (multi-session if needed,
  but well-scoped)
- OR a derivation in Region A or Region D produces a result that
  changes the scope of Region C

If neither, Phase A sits as an open commitment.

## Status

Phase A complete. Region C scope, null hypothesis, test design,
and verdict shapes specified. Phase B (the count itself)
deferred but well-defined.
