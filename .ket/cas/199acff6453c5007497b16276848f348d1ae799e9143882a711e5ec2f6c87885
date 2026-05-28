# The forcing partition: forced ⟹ algebraic

## Result

The framework's quantities split into two layers, and **forcing lives in
exactly one of them**:

- **Algebraic / combinatorial layer** — fixed by counting, number theory,
  or universality. Values are rational, algebraic, or integer. These are
  **over-determined** (many independent zero-parameter routes give the same
  value) and therefore **forced**.
- **Metric / renormalization layer** — fixed by a single renormalization
  fixed-point equation of the critical circle map. Values are transcendental
  metric constants. These are **single-sourced** (exactly one origin) and
  therefore **accepted, never independently forced**.

The exclusivity is sharp. For any framework quantity `Q`:

> **forced(Q) ⟹ algebraic(Q)**, equivalently **¬( forced(Q) ∧ metric-only(Q) )**.

No metric-only quantity is forced. This is the structural reason behind every
"consistent, but nothing is forced" outcome the framework has hit.

## The forcing criterion

A quantity is **forced** (Class-5-eligible) when necessity — not just
consistency — fixes it with zero free parameters. The operational signature
of necessity is **over-determination**: two or more *independent*
zero-parameter routes converge on the same value. A quantity fixed by exactly
one construction is **consistent** (Class 2) but not demonstrably necessary —
it may be an artifact of that one construction (`ansatz_audit_policy.md`).

Algebraic numbers are over-determined by nature; a transcendental
renormalization eigenvalue has exactly one source. That asymmetry *is* the
partition.

## The two layers

| Layer | Members | Values | Routes | Status |
|---|---|---|---|---|
| **Algebraic / combinatorial** | `φ`, `1/φ`; the Farey count `\|F_n\| ~ (3/π²)n²`; the mediant; `q_2=2`, `q_3=3`; `Ω_Λ=13/19`, the 13:5:1 partition, `R=6·13⁵⁴`, `Λℓ_P²=3/R²`; the Born exponent **2** | rational / algebraic / integer | many, independent | **forced** |
| **Metric / renormalization** | `δ_FKS≈2.8336`, `α_FKS≈−1.2886`; `α_gold = −1−2 ln φ/ln δ_FKS = −1.924`; the spectral-tilt pivot `x_*`; the tongue-width law's numerical exponent | transcendental | exactly one (the fixed-point equation) | **accepted** |

## Evidence

### Algebraic layer is over-determined
`φ` is the canonical case: it is produced independently by the decagon
(`1/φ = 2 sin 18°`), the golden spiral (growth `φ` per quarter-turn), Euler
rotation (`e^{2πi/φ}`), the Fibonacci limit, the continued fraction `[1;1,1,…]`,
and the pentagon/pentagram — none of which know about the others. `Ω_Λ=13/19`
uses only the Farey **count** (`omega_partition_combinatorial.md`), no
dynamics. The Born exponent `2` is forced by saddle-node universality (Thom:
the parabola is the unique generic codim-1 form — "any generic system gives
it"; `born_rule.md`, `lesson_forced_basin_selection.md`). Over-determination
in every case.

### Metric layer is single-sourced
`δ_FKS` is a renormalization eigenvalue of the golden-mean critical circle
map — computed only from its cubic-inflection fixed-point functional equation,
not algebraic in `φ`, no closed form. Four candidate independent routes were
checked — decagon, reverse spiral winding, Euler's formula, distance-stripped
("log-only") dynamics — and **each yields `φ`; none yields `δ_FKS`**
(`tongue_width_universality.py`). The non-trivial constant has no second
source, so `α_gold` is *defined* through it, not independently checked: the
identity `1/φ = δ_FKS^{(1+α)/2}` is a definition of `α`, not a satisfied
constraint.

### The distance-stripped diagnostic locates the boundary
Strip the metric from the circle map and you land in the combinatorial layer:
the Farey count and `Ω_Λ` **survive** (they never used a width law), while the
tongue-width exponent and `α_gold=−1.924` are **lost** (they were the metric).
So the forced/accepted boundary *is* the combinatorial/metric boundary —
the diagnostic that decides every candidate at once.

### Canonical illustration — the mass-function slope
The impasse in `mass_function_family.md` is this partition in miniature, and
it shows why both versions cannot be forced at once:

- **Combinatorial slope** `α = −q_2 − n/d ∈ ℚ` (e.g. `−7/3`, `−5/2`): rational,
  algebraic, **forced structure** — but its bridge to an observable
  (mass = entrained width) is null (`farey_tongue_width_null.py`).
- **Dynamical slope** `α_gold = −1.924`: transcendental, metric, observationally
  natural — but **not forced** (single-sourced).

The forced version can't reach the observable; the observable-natural version
isn't forced. Same layer split, same NAND.

## Consequence

Every "rests at acceptance, not forced" failure reduces to one fact — the
observable rode the **metric** layer:

- the IMF / Salpeter cascade rung (`imf_bowed_cascade.md`) — metric width law,
  also non-forced empirically;
- the spectral tilt `n_s` via `φ²`-self-similarity — carries a free pivot
  `x_*` (`spectral_tilt_reframed.md`);
- the four golden-mean route candidates — each only re-supplies `φ`.

Forcing requires algebraic participation. An observable that draws its
distinguishing content from a renormalization transcendental will be
*consistent* with the framework and never *forced* by it.

## Scope — what this does NOT claim

- It does **not** say the metric layer is wrong. `δ_FKS`, `α_FKS`, `−1.924`
  are faithful readouts of the one critical map and are accepted as such.
- It does **not** diminish the forced algebraic results — it explains *why*
  they are the ones that survive.
- It is a **meta-result about where forcing lives**, not a new physical
  prediction. It adds no observable; it classifies the ones the framework
  already has.
- Complementary to the **Basepoint Principle** (which marks where the
  framework *declines* — dimensionful absolute scale): this marks where it
  *forces*. Together they bound the forced region from two sides.

## Status of this result

A strong structural generalization **with a mechanism** (single-sourcing of
metric transcendentals vs. over-determination of algebraic values), not a
proved theorem. It maps the layers onto the existing scheme: algebraic →
Class-5-eligible, metric-only → Class-2 ceiling.

**Falsifier (identical to "is `α_gold` real?").** A second *independent*,
zero-parameter route to any metric constant — `δ_FKS` most directly — would
break the partition by making a metric quantity over-determined. None is
known; the four candidates failed. Until one exists, forcing is algebraic.

## Cross-links

- `free_parameter_scorecard.md` — **this partition's roster**: physics'
  dimensionless free parameters indexed and graded (discrete → forced,
  continuous → open).
- `ansatz_audit_policy.md` — the discriminator / over-determination criterion.
- `tongue_width_universality.py`, `farey_tongue_width_null.py` — `δ_FKS`,
  `α_gold`, the four failed routes, the width-bridge null.
- `mass_function_family.md` — the canonical algebraic-vs-metric slope split.
- `omega_partition_combinatorial.md`, `farey_partition.md` — the forced
  combinatorial spine (`13/19`).
- `spectral_tilt_reframed.md` — `n_s` via `φ²` self-similarity (free pivot).
- `born_rule.md`, `lesson_forced_basin_selection.md` — the forced exponent `2`.
- Basepoint Principle (`framework_status.md` "Out of class") — the
  complementary decline boundary.

## One-line summary

The framework forces exactly its algebraic/combinatorial quantities
(over-determined: `φ`, `13/19`, `\|F_n\|~n²`, the Born exponent 2) and merely
accepts its metric/renormalization ones (single-sourced: `δ_FKS`, `α_gold=−1.924`)
— so **forced ⟹ algebraic**, and no metric-only quantity is ever independently
forced.
