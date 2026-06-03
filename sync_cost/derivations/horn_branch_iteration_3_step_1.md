# Horn-branch iteration 3 step 1 — analytic w* test: PRODUCTIVE NULL

## Status

**Verdict: PRODUCTIVE NULL.** Iteration 3 step 1 was to derive w*
analytically from the field-equation fixed-point and verify
whether w* = 5/6 (the iteration 2 step 2 candidate from readings
(a) and (b)). Reading the apparatus closely reveals:

1. **The framework's actual w* is observation-inverted, not
   substrate-forced.** Per the honest audit in
   `boundary_weight.py` L13-56: "The framework's cited K* = 0.862
   is NOT produced by this file -- it is cited from elsewhere.
   ... Section 2 (tongue_coverage_q6 scan) and Section 3
   (fixed-point search) are NOT genuine self-consistencies."

2. **The actual w* value is 0.8281, not 5/6 = 0.8333.** The
   algebraic inversion `w* = (11 - 16Ω) / (3Ω - 2)` applied to
   Ω_obs = 0.6847 gives w* = 0.8281 (0.63% below 5/6).

3. **The "three identifications converge on 5/6" framing from
   iteration 2 step 2 was inflated by treating reading (c) — the
   `boundary_weight.md` w* — as substrate-derived when it is
   observation-inverted.** Readings (a) `(1+Q)/2 = 5/6` and
   (b) `upper Farey at q=6 = 5/6` are exact and substrate-
   internal but neither has a derived mechanism. Reading (c) is
   not at 5/6 at all but at 0.8281.

Per the user's flag — *"could always be a random numerological
fit"* — this is the discipline-required reading. The 1%-level
closures across candidates are consistent with coincidence at
the framework's general "1% honest closure" precision tier, not
with substrate-forced derivation.

Class: foundational rigor check (Class 3, iteration-step
falsifier on a substantive lead).

---

## What the apparatus actually says

### The honest audit in `boundary_weight.py`

From the file's own added docstring (L13-56):

> "This file PRESENTS itself as a 'self-consistency w = f(K)'
> derivation solved at some K*. The reality is that the
> Ω_Λ = 13/19 result comes from a clean ALGEBRAIC INVERSION
> in Section 1 / Section 5:
>
>     w* = (11 - 16 Ω) / (3 Ω - 2)
>
> Given Ω_obs = 0.6847 this gives w* = 0.8281 in one line of
> algebra, with NO K dependence. That inversion is the actual
> derivation, and it is clean.
>
> Section 2 (tongue_coverage_q6 scan) and Section 3 (fixed-point
> search) are NOT genuine self-consistencies: the tongue
> coverage function never reaches w* = 0.828 at any K < 1. ...
> Section 3's reported 'Best K = 1.0000' is a degenerate result
> of this clamp, not a derived K*.
>
> The K dependence is decorative: it shows what a
> 'self-consistency via tongue locking' WOULD look like if it
> worked, but it doesn't close under the framework's current
> tongue formula. That's OK -- the algebraic inversion is a
> complete derivation on its own."

This audit is **definitive**. The framework has not produced
an analytic field-equation derivation of w*; what exists is
an algebraic inversion of observed Ω_Λ. Iteration 3 step 1's
target ("derive w* analytically from the field equation, show
w* = 5/6 exactly") **cannot be answered affirmatively** because
the substrate apparatus does not currently support an analytic
field-equation closure for w* at all.

### What the actual w* is

Direct computation:

| Input | w* | Source |
|---|---|---|
| Ω_obs = 0.6847 | 0.828096 | algebraic inversion from observation |
| Ω = 13/19 (substrate pure) | 1.0 | substrate F₆ limit |
| Ω = 11/16 (substrate pure) | 0.0 | substrate F₅ limit |
| (1 + Q)/2 = 5/6 | 0.833333 | Klein-bottle mediant candidate |
| Upper Farey at q=6 | 0.833333 | number-theoretic candidate |

The boundary weight w* = 0.8281 is **0.63% below** 5/6 = 0.8333.

Critically: w* = 0.8281 is **not derived** — it is the value
that makes Ω_Λ(w) match the observed Ω_obs = 0.6847. Without
the observation, there is no current substrate procedure that
gives w* = 0.8281. The "self-consistency" framing in
`boundary_weight.md` is, per the audit, decorative.

### What the substrate actually predicts

The substrate-derived value for Ω_Λ at the q=6 boundary closure
is **13/19 = 0.6842** (at w = 1 limit, full locking). This is
the framework's clean substrate prediction. The observed
Ω_obs = 0.685 ± 0.007 matches 13/19 within 0.07σ — *no boundary
weight refinement is needed for empirical adequacy*.

The boundary weight w* < 1 is not required by observation; it
appears only to inflate Ω_Λ(w=1) = 0.6842 up to the central
observed value 0.6847. The 0.0005 difference is well within
the 0.0073 error bar.

This means: the substrate's clean prediction (Ω_Λ = 13/19) is
already empirically adequate. The boundary weight w* < 1 is
**not substrate-needed**; it is an interpolation that lets one
exactly match Ω_obs, not a forcing-required mechanism.

### Implication for the horn-branch convergence

Iteration 2 step 2's reading (c) — "horn-branch f_locked /
f_unlocked = w* from `boundary_weight.md`" — was the load-bearing
substrate-cosmological link. With the audit revealing that w*
is observation-inverted, reading (c) collapses to: "the
horn-branch and the cosmological sector both numerically need
~0.83 to match their respective observations." This is **not**
substrate unification; it is two empirical residuals that
happen to be close to the same number.

---

## Precision check on the three candidates

For the horn-branch's m_μ / m_e closure, the predictions under
each candidate value of f_locked = w:

| Candidate w | m_μ/m_e predicted | residual vs 206.77 |
|---|---|---|
| 5/6 = 0.8333 (a, b) | 204.50 | 1.10% |
| 0.8281 (c, inverted from Ω_obs) | 207.75 | 0.47% |
| 0.829 (horn-branch optimum) | 207.19 | 0.20% |

If the substrate forced w = 5/6, the m_μ residual would be
1.10% — comparable to the Koide-imported closure but not
better. The framework's actual w* (= 0.8281) gives better
m_μ closure (0.47%) but is itself observation-derived from
Ω_obs.

**The horn-branch's optimum is at 0.829**, not exactly any of
the candidates. The rational 5/6 candidate misses by 0.5%; the
inversion-derived 0.8281 misses by 0.1%. Neither is at the
optimum precisely.

This is the signature of a **numerologically suggestive
cluster** rather than a single substrate-forced value. Multiple
candidates within a 1% band — but no candidate is the optimum,
and none is substrate-derived.

---

## What survives iteration 3 step 1 scrutiny

Not everything from iteration 2 step 2 collapses. Three findings
are preserved:

1. **The q₂-axis sector assignment (iteration 2 step 1).**
   Independent of any w* identification, the apparatus-level
   finding that the horn-branch flare's distinguishing axis is
   q₂ locked/unlocked (not cos/sin y-parity) stands. This is
   forced by the pattern τ/e preserved + m_μ/m_e shifted.

2. **The number 5/6 is genuinely the upper Farey fraction at
   q=6.** Reading (b) is a real number-theoretic fact. It is
   not the boundary weight w* (which is 0.8281), but it is a
   substrate-internal substrate-distinguished number that
   matters at the q=6 boundary.

3. **The cosmological-mass coincidence is real but unexplained.**
   The fact that two empirical residuals (Ω_Λ at the q=6
   cosmological boundary, m_μ at the q₂-unlocked observable)
   both equal ~0.83 within 1% is striking. It may be a
   coincidence at the framework's 1% precision band, or it may
   be a real substrate identification waiting for a derivation
   that hasn't been written. The framework's discipline says:
   keep this on the empirical shelf, not the closed-derivation
   shelf, until a substrate mechanism is exhibited.

---

## What does NOT survive

1. **The "three identifications converge on 5/6" framing.**
   Reading (c) is not at 5/6 — it is at 0.8281, observation-
   inverted. Calling this "convergence" with (a) and (b) was
   incorrect; the three readings are at two different values
   (5/6 and 0.8281, differing by 0.63%) with no derived
   mechanism mapping one to the other.

2. **The "first cross-sector substrate identification" claim.**
   Without a substrate derivation of either w* or
   f_locked / f_unlocked, the two empirical residuals are not
   unified — they are independently approximated by similar
   numbers.

3. **The 1.1% closure claim under w = 5/6.** While the closure
   exists numerically, it is no better than the existing
   Koide-imported 1% closure in `fermion_mass_running.md` §4c
   — and the Koide closure has the same status (empirical
   import, not substrate derivation). Neither beats the other.

---

## Implications for the horn-branch arc

The horn-branch arc has produced through three iterations:

- **Iteration 1**: y-parity flare framing (since corrected).
- **Iteration 2 step 1**: q₂-axis sector assignment — REAL
  framework finding, preserved.
- **Iteration 2 step 2**: convergence on 5/6 — substantively
  weakened by step 3 step 1's audit.
- **Iteration 3 step 1**: w* is observation-inverted; the
  substrate-forced reading of f_locked / f_unlocked is open.

The arc has not produced substrate closure on the m_μ 37%
residual. It has produced:

- A vocabulary correction (q₂ locked/unlocked, not chirality
  or y-parity)
- A pattern observation (the 1% cluster at f_locked ≈ 5/6 to
  0.83)
- Multiple substrate-internal candidates without a forcing
  mechanism among them

This is the **same disposition as the Koide arc closed at
iteration 14**: thirteen iterations narrowed to one residual
structural assumption ("uniform eigenvalue magnitude"), but
the framework did not force closure. Here, three steps narrowed
to one residual mechanism ("substrate-forced f_locked /
f_unlocked at the q=6 Farey boundary"), and the framework does
not force closure either.

---

## What would close this

Iteration 3 step 1's verdict does NOT rule out the horn-branch
hypothesis. It rules out the iteration 2 step 2 framing as
sufficient. A substrate closure would require:

(i) An analytic field-equation derivation of either w* OR
f_locked / f_unlocked OR both, exhibiting which specific value
in the 0.83 cluster is substrate-forced.

(ii) Independent precision data distinguishing the candidates
— e.g., a Class C cross-check (PMNS θ_12) that closes under
exactly one of {5/6, 0.8281, other} and refutes the rest.

(iii) A mechanism for the substrate↔tree mapping from
q₂-locked observables to specific q=6 Farey fractions.

Each of (i)-(iii) is a substantial derivation step, comparable
to the Koide arc's iterations 11-13. The horn-branch is not at
closure; it is at the equivalent of Koide iteration ~10
("candidate identified, mechanism not closed").

---

## Honest disposition update

Per the framework's basepoint principle (operationally-open
vs structurally-declined):

- **Operationally open**: substrate-forcing of horn-branch
  f_locked / f_unlocked. The candidate cluster (5/6 to 0.8281)
  is substrate-internal but unforced. No obstruction
  proven; no closure produced. Same status as Koide pre-arc-
  closure, m_μ residual at 37%, sin²θ_W parameter.

- **Not structurally declined**: no torsorial-decline argument
  has been exhibited. The horn-branch hypothesis is not
  obstructed — it is unclosed.

For the framework's status table: the horn-branch substrate
derivation joins the empirical shelf as **operationally open
with a clustered candidate**, alongside Koide and the m_μ
bare-tree 37% gap (which is what the horn-branch is trying to
derive a closure for). The cluster's existence is informative;
its non-derivation is honest.

---

## Falsifiers for iteration 3 step 1's verdict

The "PRODUCTIVE NULL" verdict is itself falsifiable:

1. **Field equation closure found.** If a future derivation (or
   the field-equation simulation extended with the right tongue
   formula) produces w* analytically as either 5/6, 0.8281, or
   another specific value — the iteration moves to closure and
   this verdict is superseded.

2. **PMNS θ_12 distinguishes.** If applying any of the
   candidates to the PMNS mixing closes the 10% θ_12 gap to
   <1% under exactly one of them, that candidate becomes the
   substrate-favored choice and the iteration arc narrows.

3. **Tongue formula audit.** If `tongue_formula_accuracy.py`
   (referenced in the boundary_weight.py audit) produces a
   corrected formula that does close w* analytically — the
   audit reading is partly inverted and step 1's productive-null
   verdict is partly inverted with it.

---

## Plan for iteration 3 step 2 (or arc closure)

Two paths forward:

**Path A — pursue closure.** Take iteration 3 step 2 as: derive
the substrate↔tree mapping from q₂-locked observables to q=6
Farey fractions analytically. If successful, this would force
the specific value in the 0.83 cluster and resolve which
candidate is substrate-forced. Comparable depth to Koide
iterations 11-13.

**Path B — close as productive null.** Acknowledge that the
horn-branch arc has surfaced a clustered candidate without
closure mechanism, and close the arc at iteration 3 as
productive null (same pattern as Koide at iteration 14). Move
the m_μ 37% gap back to the empirical shelf with documentation
of the cluster as an open structural pattern. Proceed to
Task 106 (torus-branch) and Task 110 (vocabulary-bridge) which
are independent.

Path B is the discipline-default. Path A is the discipline-extension.
The choice depends on the framework operator's assessment of
whether the closure attempt is bounded enough to attempt before
diverting to the other open tasks.

---

## Cross-links

- `horn_branch_iteration_2_step_2.md` — the "three identifications
  converge" framing this step audits.
- `horn_branch_iteration_2_step_1.md` — the q₂-axis sector
  assignment that survives step 3 step 1's audit.
- `horn_branch_iteration_1.md` — original y-parity framing,
  superseded by step 1.
- `boundary_weight.py` L13-56 — the load-bearing audit that
  reveals w* is observation-inverted.
- `boundary_weight.md` — derivation doc that presents w* as
  fixed-point; the audit in the .py docstring corrects this
  reading.
- `klein_bottle.md` D19, L674-705 — Klein-bottle population
  ratio Q = 2/3.
- `fermion_mass_running.md` §2-4 — existing m_μ 37% gap and
  prior closure attempts; this iteration's candidate matches
  Koide-imported closure but doesn't substrate-force a
  derivation.
- `koide_form_substrate_iteration_14.md` — closing note pattern;
  the horn-branch arc may close similarly.
- `basepoint_principle.md` — operationally-open vs
  structurally-declined; this verdict places horn-branch's
  substrate closure as operationally-open with clustered
  candidates.
- `ansatz_audit_policy.md` — Class 2/3 ansatz vs derivation
  policy; the 5/6 candidate is Class 2 ("re-description")
  pending mechanism, not Class 3 ("forced").

---

## One-line summary

Iteration 3 step 1 reads the apparatus and produces a
**PRODUCTIVE NULL** verdict on substrate forcing of w*: the
framework's actual w* derivation in `boundary_weight.py` is
algebraic inversion from observed Ω_Λ (giving 0.8281, not 5/6),
not field-equation closure, per the file's own honest audit;
the iteration 2 step 2 "three identifications converge on 5/6"
framing collapses to "two substrate-internal candidates (5/6
exactly) plus one observation-inverted quantity (0.8281)" with
no mechanism mapping between them; numerical closures under
the cluster (5/6 → 1.1% m_μ residual, 0.8281 → 0.47%, optimum
0.829 → 0.20%) span a 1% band consistent with the framework's
general "1% honest closure" precision tier rather than
substrate-forced identification; the **q₂-axis sector assignment
from iteration 2 step 1 survives** as a real framework finding,
and the **horn-branch substrate closure on m_μ 37% remains
operationally open** with a clustered candidate but no forcing
mechanism, joining Koide on the empirical shelf with the same
disposition (no obstruction proven, no closure produced) — the
arc may continue (path A: derive substrate↔tree mapping
analytically) or close as productive null (path B: same pattern
as Koide iteration 14), with path B being the discipline-default.
