# Does the SM hierarchy problem translate to the framework?

## What this file is

A focused analytical note answering a methodological question
raised after the path (a) closure (`path_a_walkthrough.md`):

> Is there a hierarchy "problem" in the framework the way it is
> framed by the SM?

Short answer: **no, not the same problem.** The SM hierarchy
problem has three ingredients, only one of which translates to
the framework, and that one (the small ratio) is interpreted
differently. The framework has a *different* open question
(why two anchors and not one) that gets called "the hierarchy
problem" by analogy in `anchor_count_audit.md`. The two
problems should not be conflated.

This recasts the strategy: the path (a) closure is not a
failure to solve the SM hierarchy problem; it is positive
evidence that the framework's structure does not encode the
SM problem in its substrate.

## The SM hierarchy problem, precisely

The SM hierarchy problem is the conjunction of three ingredients:

### Ingredient 1 — Empirical: a small ratio

The Higgs vev is `v = 246 GeV ≈ 2·10⁻¹⁷ M_P`. The Higgs mass is
`m_H ≈ 125 GeV ≈ 10⁻¹⁷ M_P`. Both are tiny relative to the
Planck scale. The empirical ratio `v/M_P ≈ 2·10⁻¹⁷` is the small
number to be explained.

### Ingredient 2 — Theoretical: naturalness criterion

Naturalness (in the 't Hooft sense) says: a small dimensionless
parameter is *natural* if setting it to zero increases the
symmetry of the theory. Otherwise the small parameter is
*unnatural* and requires explanation.

The Higgs mass parameter `μ²` has no protective symmetry: setting
`μ² = 0` does not enhance any symmetry of the SM Lagrangian. So a
small `μ²` (giving small `v`) is unnatural.

### Ingredient 3 — Quantum-mechanical: RG running

In the SM, the Higgs mass receives quantum corrections from
loops involving every massive particle. These corrections are
**quadratically divergent** in the UV cutoff:

    δμ² ~ Λ²/(16π²)

For `Λ ~ M_P`, the natural value of `μ²` is `~M_P²`, not
`~v²`. To get `μ² ~ v²` requires fine-tuning the bare value
of `μ²` against the radiative corrections to one part in
`(M_P/v)² ≈ 10³⁴`.

This fine-tuning is what makes the small ratio "a problem":
it requires unexplained cancellation between independent
parameters.

### Resolutions in particle physics

Standard resolutions of the SM hierarchy problem add new
physics to *protect* `m_H`:

- **Supersymmetry**: superpartners cancel the quadratic
  divergence at the SUSY breaking scale.
- **Composite Higgs / Technicolor**: `v` is a confinement
  scale, naturally exponentially small relative to `M_P`.
- **Extra dimensions**: `M_P` is "really" close to `v`; the
  observed `M_P` is a dilution by extra-dimensional volume.
- **Anthropic landscape**: many vacua, observers exist only
  where `v` is tuned correctly.

All four address the **fine-tuning** ingredient. None
addresses just the small ratio.

## Translation test against the framework

### Ingredient 1 (small ratio) — TRANSLATES

The framework empirically has `v/M_P ≈ 2·10⁻¹⁷` and notes the
near-match `13⁻¹⁵ ≈ 1.954·10⁻¹⁷` (3.1% residual,
`numerology_inventory.md` Class 2).

The framework also generates *structurally large/small numbers*
via depth: `R = 6·13⁵⁴` is the cosmological hierarchy from
54-step z₀-stratification. Smallness via depth is **not
unnatural** in the framework's vocabulary — it's the expected
output of a multiplicative depth machine.

If `v/M_P` were structurally derived from depth 15, the
smallness would be **explained**, not problematic. The framework
has a clean answer to "why are there small numbers": *because
there are deep structures*.

### Ingredient 2 (naturalness criterion) — DOES NOT TRANSLATE

The framework does not have 't Hooft naturalness. The discipline
in `statistical_conventions.md` is Z1-Z3:

- Z1: numerical match within σ
- Z2: no un-derived O(1) factors
- Z3: only structural inputs (no fitted parameters)

These are about **derivation discipline** (no fits in the
chain), not about explaining why specific numbers should be small
or large. The framework does not say "small numbers are
suspicious unless protected by symmetry." It says "all numbers
should come from structural derivation."

A 13⁻¹⁵ ratio is just as legitimate to derive as a 13⁵⁴ ratio
under Z1-Z3, provided the chain is structural. The framework's
*natural* output is small numbers (tongue widths scale as `K^q`,
Gaussian-norm hierarchies scale as `13^k`, etc.). Largeness and
smallness are equally consistent with framework discipline.

### Ingredient 3 (quantum corrections to `μ²`) — DOES NOT TRANSLATE

The framework does not have a continuous-cutoff QFT in the
Wilsonian sense. Its substrate is discrete (Klein-Z₂ rep
machinery on Stern-Brocot mediants) and its dynamics are
algebraic (z₀-stratification, Farey-mediant recursion,
Klein-loop traversal). The "running" in
`continuum_limits.md` is a continuum-limit *transcription* of
the discrete content; it is not a Wilsonian RG with quadratic
divergences.

There is no "loop integral with cutoff `Λ ~ M_P`" in the
framework. There is no "δμ² ~ Λ²/(16π²)" radiative correction.
Therefore there is no fine-tuning problem in the SM sense.

The framework's `K_STAR` is a **fixed point** of a self-
consistency equation (`K_star_iteration.py`), not a renormalized
parameter. The renormalization-group flow is continuous-limit
language for "descent through Farey-mediant levels"
(`beta_from_tongues.md`). Both depend on the discrete substrate;
neither produces quadratic UV sensitivity.

## Verdict

The SM hierarchy problem has three ingredients. **Two of them
do not translate to the framework**:

| Ingredient | SM | Framework |
|---|---|---|
| Small ratio `v/M_P` | Yes (empirical) | Yes (empirical, possibly structurally derived) |
| Naturalness ("unnatural unless protected by symmetry") | Yes | **No equivalent** — Z1–Z3 are about derivation, not protection |
| Quadratic divergences requiring fine-tuning | Yes | **No equivalent** — no continuous QFT, no Wilsonian RG cutoff |

Without ingredients 2 and 3, ingredient 1 is **not a problem**
— it is just an observation. A 13⁻¹⁷ ratio in the framework is no
more or less natural than a 13⁻¹ ratio; both should be
structurally derivable, and if one is and the other is not, the
asymmetry is operational (we haven't found the derivation), not
foundational (the small one is unnatural).

**Conclusion**: the SM hierarchy problem, taken in its full
form, does not exist in the framework. The framework is *not
trying to solve the SM hierarchy problem*; it is trying to
derive `v/M_P` (or `v` in framework-internal units) from
substrate structure. These are different problems.

## What the framework calls "the hierarchy problem"

`anchor_count_audit.md` and several derivative files use the
phrase "hierarchy problem" in a different sense:

> "the missing link is a concrete structural open item —
> effectively the hierarchy problem posed framework-natively."

What is meant here is: the framework currently has **two
independent observational anchors** (`H_0` cosmological, `v_EW`
particle-sector). The "hierarchy problem framework-natively"
means: can the anchor count be reduced from two to one? That is
a question about **derivation chains and substrate completeness**,
not about quantum corrections or naturalness.

This is the right framing for the framework. It should be
**called something other than "hierarchy problem"** to avoid SM
confusion. Candidates:

- "Anchor-reduction problem"
- "Two-anchor question"
- "Cross-sector unification"

The phrase "hierarchy problem" carries SM baggage (fine-tuning,
naturalness) that does not apply.

## What path (a) closure tells us

`path_a_walkthrough.md` showed that the canonical register's
group structure (order 648 = 2³·3⁴) cannot reach 15 = 3·5
because the prime 5 is not in the substrate's prime support. The
composed Klein + coprime-to-6 filter has plateau values
`{1, 3, 6, 11, 17, 25, …}` skipping 15.

This was framed there as a negative result (path (a) closed).
In light of the SM-translation analysis, it is **positive
evidence for two-anchor minimality**:

- If `v/M_P` were structurally encoded in the substrate, the
  substrate should naturally accommodate the `13⁻¹⁵` ratio.
- It does not. The substrate's prime support is `{2, 3}`, the
  composed filter skips 15, and three rescue directions are
  closed.
- Therefore: `v/M_P` is **not** a structural feature of the
  framework's substrate. It is an independent observational
  input, parallel to `H_0`.

This is a clean structural finding, not a derivational failure.
The framework's "hierarchy problem" (in the anchor-reduction
sense) may be solved by the answer "two anchors are
structurally required, not just operationally."

## Reframing strategy

Three concrete consequences:

### 1. Stop calling it "the hierarchy problem"

Update `anchor_count_audit.md`'s phrasing. The question is
about anchor count, not naturalness or fine-tuning. The SM
phrase imports baggage that misframes the framework's actual
question.

### 2. Treat two anchors as a structural finding, not a defect

If the path (a) closure stands (and it is structural, not
operational), the framework's "two-anchor minimum" should be
upgraded from "open obstruction" to "structural feature." This
parallels the way the SM has multiple independent inputs (gauge
couplings, Yukawas, CKM angles, etc.) without those being
treated as separate "hierarchy problems."

The framework's structural achievement is then: it has reduced
~30+ SM parameters to **two** observational anchors plus
framework-derived dimensionless ratios. That is a substantial
reduction, even if not the further reduction to one anchor.

### 3. Identify the *real* open questions

If the SM hierarchy problem doesn't apply, what is genuinely
open in the framework?

- **Cross-sector ratios**: framework derives ratios within
  cosmological and particle sectors (Ω partition, mass ratios,
  etc.) but only a single number connects them (`v/M_P`).
  This is **not** "the hierarchy problem" — it is
  "cross-sector unification."

- **Substrate completeness**: are the framework's primitives
  (`integers`, `mediant`, `fixed_point`, `parabola`) actually
  complete for deriving everything dimensionless, or does the
  substrate need additional primitives?

- **Anchor identification**: of the two anchors, are both
  *primary*, or is one derived from the other through a route
  not yet discovered?

These are well-posed framework-native questions. None of them
imports SM naturalness baggage.

## What this means for the substrate-forced ε question

`epsilon_substrate_decomposition.md` and downstream files
treated the substrate-forced ε question as blocked by the
hierarchy problem, which was treated as the binding obstacle.

If the SM hierarchy problem doesn't translate, the ε question
is *also* not blocked by it. The ε question is about
**resolution scales**, which is a separate substrate property.
The path (a) closure shows that the canonical register doesn't
supply ε at the K_STAR-INTERACT window — but this is about
register cardinality, not about anchor unification.

The K-axis tie-in in `k_axis_uniqueness.md` lands as Class 2
because no canonical framework register has cardinality in the
required window. This may itself be a structural feature: the
framework's two canonical registers (P-reg = 19, H-reg = 6·13⁵⁴)
are the natural observers; intermediate cardinalities are not
substrate-supplied because they don't correspond to canonical
observers. The K_STAR-INTERACT alignment requires a non-
canonical observer, which the framework neither supplies nor
forbids — it's just not framework-native.

## Cross-references

- `path_a_walkthrough.md` — the closure that motivated this
  analysis
- `anchor_count_audit.md` — uses "hierarchy problem" in the
  anchor-reduction sense; suggested rephrasing
- `numerology_inventory.md` — `v/M_P ≈ 13⁻¹⁵` Class 2 entry
- `statistical_conventions.md` — Z1-Z3 discipline (no
  naturalness criterion)
- `continuum_limits.md` — discrete-to-continuous transcription
  (no Wilsonian RG)
- `K_star_iteration.py` — fixed-point iteration (not RG running)
- `framework_status.md` — needs update if anchor reframing is
  accepted
- `epsilon_substrate_decomposition.md` — the "hierarchy problem
  as binding blocker" framing this note revises
