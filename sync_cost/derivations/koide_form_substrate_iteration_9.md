# Koide form substrate derivation — iteration 9

## Status

**Iteration 9. Path A test: empirical check whether the framework's
existing three-generation amplitude apparatus produces the Koide
constraint.**

The framework has an existing apparatus for the discrete-to-
continuous lift on three-generation amplitude space:
`three_basins.py` derives three basin widths `Δθ_i` from the circle
map at the 1/3 tongue, with Born rule `P_i ∝ Δθ_i²` and mass
`m_i ∝ 1/Δθ_i²`. The framework also states
(`dynamical_tool_audit.md`) that "circle maps (discrete) and
Kuramoto (continuous) are provably the same content."

**Result: null result for Path A.** The basin-width-derived
amplitude vector does not satisfy the Koide constraint `K = 2/3`.
Numerically, the Koide functional `K(v)` computed from
`three_basins.py` basin widths at three K-values (K = 0.8, 0.9,
1.0) gives `K ≈ 0.35–0.36`, far from the observed Koide value
`2/3 ≈ 0.667`. The framework's bare-tree formula
`m_i = base_i^(5/2)` with `bases = (1, 7, 26)` gives `K = 0.708`,
above the Koide value. The observed K sits between the two
framework predictions but matches neither.

**Implication**: the framework's existing apparatus on the
discrete-to-continuous lift axis does not naturally produce the
Koide constraint via simple amplitude identification. The
substrate-derivation of Koide requires either a different
mechanism than what the existing apparatus provides, a specific
combination of multiple apparatuses, or a substrate-aligned
constraint that the existing apparatus is missing.

No new substrate primitive. The iteration produces a numerical
null result on Path A, narrows the remaining derivation paths,
and identifies what's missing.

Class: foundational consolidation (Class 3, iteration step 9,
empirical test with null result).

---

## The test

### Path A hypothesis (from iteration 8 + corpus search)

Reading 1c from iteration 7 hypothesized that the substrate's
synchronization cost, restricted to three-generation amplitude
space, produces the matrix `M = q_3 I − q_2 J`. The
framework-defined discrete-to-continuous lift via circle map basins
(`three_basins.py`) is the framework's existing apparatus on this
axis.

Path A tests whether the basin-width amplitude lift
`√m_i ∝ 1/Δθ_i` directly satisfies the Koide constraint
`K(v) = 2/3`.

### Numerical computation

Using `three_basins.py`'s computed basin widths at the 1/3 tongue
boundary:

| `K_map` | Basin widths `(Δθ_1, Δθ_2, Δθ_3)` | Masses `(m_i ∝ 1/Δθ²)` | `K(v)` |
|---|---|---|---|
| 0.8 | `(0.259, 0.275, 0.465)` | `(14.88, 13.19, 4.62)` | `0.352` |
| 0.9 | `(0.248, 0.270, 0.482)` | `(16.22, 13.73, 4.31)` | `0.356` |
| 1.0 | `(0.229, 0.269, 0.502)` | `(19.09, 13.86, 3.96)` | `0.363` |

Target: `K = 2/3 ≈ 0.667`.

### Comparison across framework apparatuses

| Apparatus | K | Mass ratios (lightest=1) |
|---|---|---|
| Circle-map basins (`three_basins.py`, `K_map = 1.0`) | `0.363` | `1 : 3.50 : 4.82` |
| Bare-tree formula `base^(5/2)` with `(1, 7, 26)` | `0.708` | `1 : 130 : 3447` |
| PDG observed (Koide) | `0.667` | `1 : 207 : 3477` |

The observed value sits **between** the two framework predictions
but does not match either. The basin-width K is near the
Cauchy-Schwarz lower bound `1/3` (consistent with the three basins
having widths within a factor of 2 of each other — moderately
unequal). The bare-tree K is above the Koide value (consistent
with the bare-tree mass hierarchy being more extreme than the
Koide constraint allows). The PDG K is exactly the substrate's
Klein-bottle population ratio `Q = q_2/q_3 = 2/3`.

---

## Why this is a null result for Path A

Path A hypothesized that the substrate's discrete-to-continuous
lift via circle-map basins would naturally produce the Koide
constraint. The numerical test refutes this: the basin-width
amplitude vector gives `K ≈ 0.36`, not `0.667`.

Several interpretive readings are consistent with the data:

1. **`three_basins.py` and lepton mass derivation address different
   physical questions.** The framework's `three_basins.py` derives
   basin widths illustrating where probability comes from at q=3
   (three unequal-width basins instead of two equal ones). It does
   not claim to derive the specific lepton mass hierarchy. The
   bare-tree formula `m_i = base_i^(5/2)` is the framework's
   actual mass derivation; it goes through the cube structure
   (`generation_mechanism.md`) rather than directly through circle
   map basins. The two apparatuses address different physics.

2. **The amplitude lift `√m ∝ 1/Δθ` may be an oversimplification.**
   The framework's mass formula uses sector exponent `5/2`, not the
   direct inverse basin width. The actual relation between basin
   widths and masses may involve cascade depth, sector exponent,
   and other substrate machinery that the simple `1/Δθ` lift
   misses.

3. **Koide is not a property of either apparatus alone.** The
   bare-tree gives `K = 0.71`; basin widths give `K = 0.36`;
   neither matches `K = 2/3`. The Koide constraint is satisfied by
   *observation* (PDG `K = 0.667` ≈ `Q = 2/3`), but is not
   derived from either framework apparatus in their current form.
   The substrate-derivation must invoke an additional mechanism
   (Klein-antipodal Z_2 constraint, sector-exponent + Klein
   combination, etc.) not isolated in this test.

The null result rules out the simplest version of Path A: direct
amplitude lift from circle-map basin widths. It does not rule
out more nuanced combinations that go through `three_basins.py`
plus additional substrate apparatus.

---

## What this leaves on the table

### Path B (formal derivation) is now the remaining substrate-derivation route

With Path A's empirical test returning null, the substrate-
derivation of Koide via the discrete-to-continuous lift requires:

- Either a specific *combination* of bare-tree and basin-width
  apparatuses that lands on `K = 2/3`
- Or a formal derivation of the quadratic form `M = q_3 I − q_2 J`
  from substrate inviolables independent of the basin-width lift
- Or recognition that `K_lepton = Q` is a substrate-aligned
  *constraint* (not derived from the lift mechanism), forced by
  some Klein-bottle / Q-conservation / cube-identity structural
  requirement

Each of these is multi-session research. The Discrete Extension
Principle's deployment shape applies: enumerate candidate
mechanisms, test each, accept closure or refine.

### What's been established across nine iterations

The Koide gap has been:

- **Reformulated** geometrically (iter 1: `|v_sym|² = |v_⊥|²`)
- **Tested against** the Klein-bottle τ Z_2 (iter 3-4: substrate
  gives V_4, not S_3; standard Z_2 actions don't close)
- **Reformulated** in V_4 + cube identity terms (iter 5-6: necessary
  but not sufficient)
- **Reduced** to the minimal matrix form `v^T (q_3 I − q_2 J) v
  = 0` (iter 7)
- **Reduced further** to the scalar identity `K_lepton = q_2/q_3`
  (iter 8)
- **Empirically tested** against the framework's existing
  discrete-to-continuous lift apparatus (this iteration, null
  result)

The trajectory has produced honest progress: the gap is
mathematically smaller and substantively sharper. The closure
question itself remains unresolved.

---

## What the framework defines vs. what's missing

After nine iterations and corpus survey, the framework's existing
apparatus on the relevant axes:

| Component | Status |
|---|---|
| Three-generation discrete state space `{A, B, C}` | Defined (`generation_mechanism.md` §1) |
| Discrete-continuous lift via circle map / Kuramoto | Defined (`dynamical_tool_audit.md`) |
| Circle-map basin widths at q=3 tongue | Computed (`three_basins.py`) |
| Born rule `P ∝ Δθ²` per basin | Defined (`born_rule.md`) |
| Mass `m ∝ 1/Δθ²` per basin | Defined (`three_basins.py`) |
| Bare-tree mass formula `m = base^(5/2)` for charged leptons | Defined (`generation_mechanism.md`, `mass_sector_closure.md`) |
| Klein-antipodal `Q = q_2/q_3 = 2/3` | Defined (`klein_bottle.md` D19) |
| Quadratic form / metric on continuous three-generation amplitude space | **Not defined** |
| How sector exponent + basin widths combine to produce specific Koide-satisfying masses | **Not defined** |
| Substrate-internal force that imposes `K_lepton = Q` on the lepton amplitude vector | **Not defined** |

The missing pieces are the *combination* of the defined apparatuses
into a unified Koide-producing mechanism. Each defined piece is
substrate-derived; their composition into the specific Koide form
is not.

---

## Cross-thread observation

The selection thread (`substrate_prediction_selection.md`) opened
concurrently with iteration 8 asks a related-but-distinct question:
why does `K_lepton = q_2/q_3` rather than some other substrate-
primitive ratio? This iteration's null result on Path A is
consistent with that thread's framing: the framework's apparatus
*permits* `K_lepton = q_2/q_3` (Cauchy-Schwarz and substrate
primitives are consistent with it) but does not *uniquely force*
it from the discrete-to-continuous lift alone.

The two threads remain methodologically independent: this Koide
iteration is research-level closure work on a specific prediction;
the selection thread is methodological exploration. Neither is a
prerequisite for the other.

---

## Falsifiers

- **Path A test result refuted by error**: re-running
  `three_basins.py` with corrected parameters gives `K = 2/3`.
  Would reopen Path A.
- **A specific combination of bare-tree and basin-width apparatuses
  produces `K = 2/3` substrate-natively**: would close via
  combined apparatus.
- **A substrate-aligned constraint forcing `K_lepton = Q` is
  identified outside the bare-tree and basin-width frameworks**:
  would close via the constraint mechanism.
- **`three_basins.py` is shown to address a different physical
  question than lepton masses**: confirms the framing of this
  iteration's null-result interpretation 1.

---

## Recommended next iteration

Iteration 10 could:

- **Option A**: Examine whether a substrate-aligned combination of
  bare-tree masses and basin-width-derived corrections lands on
  Koide. The bare-tree gives `K = 0.71`; basin widths give `K =
  0.36`; observed is `K = 0.667`. Is there a substrate-natural
  weighted combination?
- **Option B**: Examine whether the Klein-antipodal Z_2 imposes
  `K_lepton = Q` directly on the amplitude space as a *constraint*
  independent of the bare-tree or basin-width mass derivation.
- **Option C**: Pause and reassess whether the Koide closure work
  is best continued, paused for the selection thread, or declared
  structurally bounded per DEP row 2 after nine iterations.

The null result of this iteration is a substantive finding either
way. The framework's existing apparatus on the relevant axis does
not naturally produce Koide; the closure (if it exists) requires
machinery the framework has not yet articulated.

---

## Cross-links

- `koide_form_substrate_iteration_8.md` — scalar form
  `K_lepton = q_2/q_3`.
- `three_basins.py` — circle-map basin widths at 1/3 tongue
  (existing framework apparatus tested here).
- `dynamical_tool_audit.md` — discrete-continuous equivalence
  (circle map ↔ Kuramoto).
- `born_rule.md` — Born rule from basin measure.
- `generation_mechanism.md` (D34) — three-generation structure,
  bare-tree formula.
- `mass_sector_closure.md` — cube identity, sector exponents.
- `klein_bottle.md` (D19) — `Q = q_2/q_3 = 2/3`.
- `substrate_prediction_selection.md` — concurrent thread on
  prediction-uniqueness questions.
- `discrete_extension_principle.md` (PR #191) — methodology.

---

## One-line summary

Path A — the empirical test of whether the framework's existing
`three_basins.py` apparatus (circle-map basin widths at the 1/3
tongue with the framework-defined amplitude lift `√m ∝ 1/Δθ`)
produces the Koide constraint `K = 2/3` — **returns null**: the
basin-width-derived Koide functional gives `K ≈ 0.35–0.36` across
`K_map ∈ [0.8, 1.0]`, far from the observed `K = 0.667 = q_2/q_3`;
the bare-tree formula `base^(5/2)` with `(1, 7, 26)` gives `K =
0.708`, above the Koide value; the observed PDG `K` sits between
the two framework predictions but matches neither, equaling
exactly the substrate's Klein-bottle population ratio `Q =
q_2/q_3`; three interpretive readings of the null result —
`three_basins.py` addresses different physics than lepton mass
derivation, the amplitude lift `√m ∝ 1/Δθ` is an
oversimplification ignoring sector exponent and cascade machinery,
or Koide requires substrate-aligned constraint machinery not
isolated in either existing apparatus — all consistent with the
data; the substrate-derivation of Koide therefore requires *either*
a combination of bare-tree and basin-width apparatuses that
substrate-natively combines to give `K = 2/3`, *or* a
substrate-aligned constraint forcing `K_lepton = Q` independent of
the mass derivation (analogous to how the Basepoint Principle
identifies structural-decline obligations), *or* recognition that
Koide is structurally bounded per Discrete Extension Principle row
2 after nine iterations of substrate-aligned candidate testing
without closure; nine-iteration trajectory has produced honest
mathematical narrowing (from "derive Koide form" to scalar
identity `K_lepton = q_2/q_3` with empirically-null lift apparatus)
without producing closure; selection thread
(`substrate_prediction_selection.md`) remains methodologically
independent; iteration 10 options are combination test, constraint-
mechanism test, or reassessment of continuation strategy.
