# Mass-sector `1/√w` prescription — Phase A: terminology discipline

## Scope

The last remaining Type C in Issue #56 is the normalization
convention

    a_1(leptons)  =  1 / √w(3/2, K*)

which reads the lepton generation exponent as the saddle-node
relaxation time at the q = 2 Arnold tongue. The identity matches
PDG masses to 4 decimal digits, but the specific convention
`μ_center = w` (with `w` the framework's perturbative tongue-width
formula) is a **choice** — not forced by the Kuramoto field
equation.

This Phase A fixes vocabulary and pinpoints the specific O(1)
step that Phase B must derive. Unlike the down-type program,
much of the audit work is already in `tongue_formula_accuracy.py`
(which establishes a systematic factor of π between two candidate
w-definitions). Phase A records, organizes, and extends that
audit.

## 1. The three w-quantities

The symbol "w" or "tongue width" currently refers to three
distinct objects in the framework:

### 1.1 `w_framework(p/q, K)` — the framework's formula

Defined in `circle_map_utils.tongue_width`:

    w_framework(p/q, K)  =  2 (K/2)^q / q          (q ≥ 2, K < 1)

Used in `item12_C_from_K_star.md`, `a1_from_saddle_node.md`,
`boundary_weight.md`, `born_rule.md`, `framework_utils.py`, and
most downstream identities. The current "lepton identity" uses
this `w`.

### 1.2 `w_physical(p/q, K)` — the Ω-space Arnold tongue width

The actual width of the locked region in the (K, Ω) parameter
plane at fixed K. Derived analytically at q = 2 in
`tongue_formula_accuracy.py`:

    w_physical(1/2, K)  =  K² / (4π)            (q = 2)
    w_physical(0, K)    =  K / π                (q = 1)

Verified against tight-tolerance numerical bisection of the
circle map.

### 1.3 `μ(p/q, K)` — the saddle-node control parameter

In the parabola normal form `dx/dt = μ − x²`, this is the
distance from the bifurcation. In `a1_from_saddle_node.md`
(§3) the framework identifies

    μ_center  =  w_framework(p/q, K)            (convention)

This is the Type C step under scrutiny.

## 2. The systematic ratio

`tongue_formula_accuracy.py` establishes:

    w_framework  =  π · w_physical              (verified q = 1, 2)

The ratio is exactly π, **independent of q**. This is a pure
normalization, not a per-tongue calibration.

Consequence for relaxation times:

    τ_physical  =  1 / √w_physical              (the "physical" saddle-node time)
    τ_framework = 1 / √w_framework  =  τ_physical / √π

The lepton identity `a_1(lep) = 2/K*` holds against
`w_framework`, not `w_physical`:

    τ_framework(3/2, K*)  =  2 / K*              =  2.320  (matches PDG)
    τ_physical(3/2, K*)   =  2 √π / K*           =  4.112  (off by √π)

## 3. Terminology discipline for the program

| Symbol | Meaning | Used in |
|---|---|---|
| `w_F` | Framework's perturbative formula `2(K/2)^q / q` | `circle_map_utils`, most downstream |
| `w_Ω` | Physical Ω-space tongue width | `tongue_formula_accuracy.py` |
| `μ_N` | Saddle-node control parameter (normal-form coord.) | `a1_from_saddle_node.md` §3 |
| `τ_N` | Normal-form relaxation time `1/√μ_N` | `parabola_csd_demo.py` |
| `a_1(lep)` | Generation exponent from PDG masses via Stern-Brocot | `item12_characterize_a1.py` |

**Identities between quantities:**

    w_F      =  π · w_Ω                         (verified, factor-π audit)
    a_1(lep) =  1 / √w_F   =  2/K* at q = 2   (4-digit PDG match)
    τ_N      =  1 / √μ_N                       (parabola primitive)

**The Type C step (isolated):**

    μ_N  =  w_F                                (THE identification under scrutiny)

Equivalently: `a_1(lep) = τ_N` with `τ_N = 1/√w_F`, which means
the lepton generation exponent is identified with the normal-
form relaxation time at `μ_N = w_F`, not at `μ_N = w_Ω`.

## 4. What the two candidate readings predict

### Reading α: `μ_N = w_F` (current convention)

- `a_1(lep) = 2/K*` (4-digit PDG match).
- `C = a_1² = 4/K*² = q_2²/K*²`.
- All downstream identities in `item12_*` hold.

### Reading β: `μ_N = w_Ω = w_F/π` (physical tongue width)

- `a_1(lep) = 2√π / K* ≈ 4.11`.
- Does **not** match PDG (observed 2.32, off by √π).
- All downstream identities must be rescaled; the 4-digit
  match disappears.

Reading α is empirically correct. The Type C question is **why**
— what structural feature of the framework forces `μ_N = w_F`
rather than `μ_N = w_Ω`?

## 5. Candidate structural mechanisms (Phase B to evaluate)

The factor π cannot be arbitrary; it must come from a specific
structural source. Candidates to evaluate in Phase B, ranked by
methodological plausibility from prior session's pivots:

### Candidate 1 — Gaussian-averaging (CLT/MZ precedent)

The framework uses Gaussian statistics extensively: Strogatz-
Mirollo CLT in Gap 1, Mori-Zwanzig in Gap 2, Wick factorization
in the ADM sector. Gaussian integrals have `∫e^{-x²}dx = √π`,
so π naturally arises from **squared Gaussian normalizations**.

Hypothesis: `μ_N` is the Gaussian-averaged tongue width, not
the geometric one. The geometric width `w_Ω` is the support of
a characteristic function; averaging over the ensemble's
Gaussian phase distribution gives an effective support `π w_Ω`
from the Gaussian's variance integral.

This matches the methodological precedent: sin²θ_W pivoted from
near-coincidence to d_eff = 80/27 once the geometric
**interpretation** of the exponent was identified. The same
move here: `μ_N = w_F` becomes a derived identity once the
Gaussian-averaging interpretation is identified.

### Candidate 2 — Area-vs-width / Jacobian reading

`w_F` might be a **tongue area** in (K, Ω) plane, not a width.
The factor π is then the coordinate Jacobian relating area to
width via the angular integral.

Weaker support than Candidate 1 because the areas don't
dimensionally match (`w_F ∝ K^q`, while the area scales as
`∫K^{q-1}dK = K^q/q` — the dimensions work but the prefactor
doesn't cleanly give π without additional structure).

### Candidate 3 — Self-consistent fixed point (boundary_weight precedent)

`μ_N = w_F` might be a self-consistency fixed point for the
mean-field coupling, not a convention. Under this reading the
factor π is the **ratio** `w_F / w_Ω` set by self-consistency
of the tongue structure with the Kuramoto order parameter.

This is the template just used in Phase D for down-type: a
weight `w*` fixed by self-consistency at a topological boundary.
Here the analog would be: `π` = self-consistency ratio between
two tongue parameterizations.

### Candidate 4 — Parabola primitive's native coordinates

The parabola primitive `dx/dt = μ − x²` has a natural scaling
symmetry `x → λx, μ → λ²μ, t → t/λ`. Different choices of `λ`
give different `μ_N` normalizations. The framework's choice
`μ_N = w_F` corresponds to a specific `λ = √(w_F/w_Ω) = √π`.

This reading has the factor π built into the primitive's
coordinate choice, with no further derivation required — the
framework is **defining** `μ_N` in the `x`-coordinate where
the tongue width equals the framework's perturbative formula.

Candidate 4 is the **weakest** interpretation: it says the
convention is a coordinate choice, which makes the 4-digit PDG
match a coincidence tied to `q = 2` rather than a structural
statement.

## 6. What Phase A establishes, and does not

**Establishes:**

- Three distinct w-quantities (`w_F`, `w_Ω`, `μ_N`) with
  explicit pairwise relationships.
- The Type C step is precisely `μ_N = w_F` (not `μ_N = w_Ω`),
  with the ratio being the factor π from
  `tongue_formula_accuracy.py`.
- Four candidate structural mechanisms for π, ranked by
  methodological precedent.

**Does not establish:**

- Which of the four candidates is correct.
- Whether the factor π is invariant under changes of circle-map
  parameterization (it should be, but this should be verified).
- Whether the 4-digit match is tight at non-q=2 sectors after
  the cross-sector corrections — `item12_cross_sector_ratios.md`
  says the `1/√w` formula applies directly only to leptons, so
  the Type C question is genuinely about the lepton sector alone.

## 7. Note on previous session's pivot patterns

The recently-closed down-type derivation (commit `fa7515f`)
established a methodology for Type C closures:

    vocabulary discipline  →  candidate enumeration  →  null results  →
    reformulation via precedent  →  rigorous verification  →  structural saturation

This mass-sector program should follow the same pattern:

- **Phase A (this doc):** vocabulary.
- **Phase B:** enumerate candidate structural derivations of π.
- **Phase C:** identify which candidate reaches π without
  circularity, using the successful-pivot templates.
- **Phase D:** if a self-consistency reading emerges (Candidate
  3), apply the `boundary_weight.md` template directly — it
  worked in Phase D of the down-type.

The most-likely winning template, based on the down-type
precedent, is **Candidate 1 (Gaussian averaging)**: it is the
only candidate that gives π naturally from Gaussian structure
already present in Gap 1 / Gap 2 closures. Candidate 3
(self-consistency) is the backup.

## 8. Cross-references

| File | Role in Phase A |
|---|---|
| `tongue_formula_accuracy.py` | Source of the `w_F = π · w_Ω` audit |
| `circle_map_utils.py` | Defines `w_F` under the name `tongue_width` |
| `a1_from_saddle_node.md` | Current `μ_center = w_F` convention (§3) |
| `item12_C_from_K_star.md` | Status of the identity, explicit Type C flag |
| `born_rule.md` | Uses `w_F`; `Δθ² ∝ ε` derivation is a Phase B template |
| `parabola_csd_demo.py` | Normal-form `τ = 1/√μ` verified numerically |
| `boundary_weight.md` | Self-consistency template (Candidate 3 backup) |
| `gap1_theorem.md` | Strogatz-Mirollo CLT usage (Candidate 1 precedent) |
