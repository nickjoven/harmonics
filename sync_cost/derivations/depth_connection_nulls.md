# Null results: connecting cosmological depth 54 to EW depth ~15

## What this file is

A registry of attempted (and failed) derivations of a structural
connection between the cosmological hierarchy depth (54 in
z₀-stratification, equivalently `R = 6·13⁵⁴`) and the electroweak
hierarchy depth (~15 in the same units, suggested by `v/M_P ≈
13⁻¹⁵`, 3.1% near-match).

Each entry records: what was attempted, by which file/commit, what
was found, and why it falls short. The aim is to prevent
re-deriving the same nulls.

This is the binding-blocker question per `dynamical_tool_audit.md`
(the right hierarchy axis) and `epsilon_physical_reading.md` (no
canonical intermediate ε exists). It is anchor-count obstruction
#2 (`anchor_count_audit.md`).

## Per-attempt summary

| # | Approach | Source | Result | Class |
|---|---|---|---|---|
| 1 | Yukawa-mediant cascade on Stern-Brocot from (1/3, 1/2) to depth 15 | commit `16205d5`, `yukawa_mediant_cascade.py` (deleted) | Subtree purely binary (2¹⁵ = 32768), not 13-adic; no termination at depth 15 | Null |
| 2 | Z_30 substrate (Z_2 × Z_3 × Z_5) with Klein Z_2 quotient | commit `2780fd6`, `z_30_substrate_check.py` (deleted) | Klein orbit count is (Nx−1)·Ny, not Nx·Ny/2; substrate doesn't realize Z_30 | Dead end |
| 3a | Z_3 rotations: SL(2, ℤ) elliptic of order 3 | commit `60d4e90`, "Path 1 minimal test" | Möbius orbits leave [0, 1]; gauge bracket (1/3, 1/2) not preserved | Null |
| 3b | Z_3 rotations: Z_6 residue shift k → k+2 | same | Splits Z_6 into {0,2,4}, {1,3,5} mixing baryonic/dark; no clean EW-sector action | Null |
| 3c | Z_3 rotations: cyclic permutation of {q₂, q₃, q₂+q₃} | same | Product 2·3·5 = 30, halved = 15 — algebraic pattern only, no orbit derivation | Suggestive, not derived |
| 3d | Z_3 rotations: continued-fraction upper path from (1/3, 1/2) | same | Denominators 5, 7, 9, …, 33 (linear by 2); only one 13-divisible (q=13 at depth 5); no period-(q₂+q₃) structure | Null |
| 4 | Klein-quotient second invariant | sketched in commit `3dab11f` | Never implemented | Unattempted |
| 5 | Direct depth-15 register identification | `observer_register_closure.md` §4 | Four framework-integer expressions evaluate to 15: `q₃(q₂+q₃)`, `q₂q₃ + q₃²`, `(q₂²+q₃²) + q₂`, etc. None forced. | Class 2 |
| 6 | φ⁻⁸⁰ ≈ v/M_P (5.3% near-match) | `anchor_count_audit.md` | Pure numerology; no structural argument attached | Class 2 |
| 7 | H-reg ↔ P-reg parametric interpolation (4 routes) | commit `f034e69`, `observer_register_closure.md` §7 | Continuous interp, shared-13, Klein-antipodal of z₀, moiré 19·54 = 1026: all null | Null (numerology) |
| 8 | K-axis sweep at K_STAR | PR #76, #77 | Wrong axis: K-axis is bounded and doesn't generate hierarchies (per `dynamical_tool_audit.md`). Plateau theorem is locking content, not hierarchy. | Wrong tool |
| 9 | Naive Kuramoto r-iteration for K_STAR | `a1_from_saddle_node.md:213-214` | r=0 is superstable fixed point with contraction rate q₂=2; iteration converges to 0, not K_STAR | Null (different question, related dynamical-tool issue) |
| 10 | Generation hierarchy `26:7:1` with depth-stratified exponents | commit `5b65cc5`, `numerology_inventory.md` | μ/e ratio fails 37%; multiple integer constructions (no forced base) | Class 1 |
| 11 | Hybrid `Ω_b = (1/19)·\|r\|²` and `A_s = 2.33·\|r\|³·10⁻⁹` | `hybrid_strategy_audit.md` | Different exponents per observable, no forcing; \|r\| imported from observation | Class 2 |
| 12 | `K_STAR^14 = q₂⁻^q₃ = 1/8` | commit `b8911fb` | Multiple framework-integer exponents available; q₂^(-q₃) selected because matches | Class 2 (was Class 4) |

## What each null *specifically* rules out

1. **Yukawa cascade** rules out: "the SB subtree from the gauge
   bracket terminates at depth 15 with 13-adic structure."

2. **Z_30 substrate** rules out: "the lattice carries Z_30 = Z_2
   × Z_3 × Z_5 such that Klein Z_2 quotient halves to 15 cells."

3. **Z_3 rotations (a-d)** rule out four specific Z_3 actions on
   the gauge bracket. Does NOT rule out higher-order rotations or
   non-cyclic actions.

4. **Klein-quotient second invariant** is *unattempted* — not a
   null. Listed for completeness; the construction was sketched
   in `3dab11f` but never implemented. Open candidate.

5. **Direct depth-15 register identification** rules out: "depth
   15 is forced by *some* framework-integer expression." Does NOT
   rule out: "depth 15 is forced by a Klein-fold sub-action of
   the |Z_6| × ⟨z₀⟩₅₄ × ⟨ι⟩ register." That sub-action approach
   has not been attempted.

6. **φ⁻⁸⁰** rules out: "the φ-exponent 80 has any framework
   structure" (it doesn't, attempted no further).

7. **H-reg ↔ P-reg interpolation** rules out: "an intermediate
   register exists as a continuous interpolation between P-reg
   and H-reg." Does NOT rule out: "an intermediate register
   exists as a *discrete sub-action*."

8. **K-axis sweep** rules out: "the K-axis itself is the
   hierarchy axis." Does NOT rule out: composing K-axis with
   z₀-stratification.

9–12 are tangential — they constrain the *anchor count*
discussion but don't directly probe the depth connection.

## What no null has yet ruled out

These are open paths, neither attempted nor refuted:

(a) **Klein-fold sub-action of |Z_6| × ⟨z₀⟩₅₄ × ⟨ι⟩.** The
    canonical register has natural sub-actions; one might land at
    depth 15. Specifically: 54 = 6·9 = |Z_6|·q₃². A sub-action
    fixing Z_6 (factoring out gauge multiplicity) leaves ⟨z₀⟩₉.
    Does the EW scale live at the 9-orbit or some sub-orbit
    thereof? Concrete probe: enumerate sub-actions of the depth-
    54 z₀-orbit at depth divisible by relevant framework
    integers (3, 5, 9, 15, 18, 27).

(b) **Sub-Fibonacci depth at the EW.** 145.8 Fibonacci levels span
    Planck to Hubble. A particle-sector sub-count, e.g., from
    the |F_7| = 19 P-reg level, might land at φ²-depth ≈ 15 or
    a related framework integer. Concrete probe: compute φ²-depths
    of EW-sector observables (m_t/v, m_b/v, etc.) and check
    whether they cluster at framework-integer depths.

(c) **Cross-sector tongue identification.** If a tongue at the
    cosmological scale (e.g., the (1/q₂q₃) tongue at K=1) and a
    tongue at the EW scale (e.g., the lepton (1/q₃) tongue) are
    the *same* tongue under a substrate fold, that fold gives
    the depth identification. Concrete probe: compare the q-
    structure of cosmological- and particle-sector tongue
    derivations and look for shared p/q.

(d) **Anomaly-cancellation depth.** The framework's gauge-anomaly
    cancellation forces specific (color, weak, hypercharge)
    combinations. If the depth 15 emerges as the smallest depth
    at which the cosmological register's mode count satisfies an
    anomaly-cancellation constraint, the depth is forced
    structurally. Concrete probe: compute mode counts at depths
    {3, 6, 9, 15, 18, 27} and check anomaly-cancellation
    arithmetic.

(e) **Conformal-equivalence depth.** If the substrate has a
    conformal symmetry that relates the cosmological FRW scale
    to the EW Higgs-condensate scale via a discrete conformal
    factor, that factor's depth is the connection. Concrete
    probe: write down the framework's conformal weights at the
    two scales and check whether their ratio is a power of 13.

## The "unattempted" status of (a)

(a) — Klein-fold sub-action of |Z_6| × ⟨z₀⟩₅₄ — is the most
direct and the only path that uses only framework-existing
structures. It is C2 of `epsilon_substrate_decomposition.md` and
the recommended near-term probe per `dynamical_tool_audit.md`.

The reason it has not been attempted is operational: the existing
audit work has focused on (i) demoting Class-4 ansatz claims, (ii)
clarifying the structural plateau theorem, and (iii) ruling out
direct depth identifications. Constructing a forced sub-action of
the canonical register is a positive structural derivation, not an
audit-and-triage task — it requires building rather than
demolishing.

## What would close obstruction #2

The minimum acceptance criterion (from
`epsilon_substrate_decomposition.md` and
`anchor_count_audit.md`):

> A structural derivation of depth `d_EW = 15` from substrate-side
> considerations using only framework integers, no fitted
> exponents, and no anchor imports. The derivation must rule out
> alternative depths {12, 13, 14, 16, 17, 18} by an argument of
> the same kind that forces `(q₂, q₃) = (2, 3)` in
> `mass_sector_closure.md`.

Without such a derivation, the 13⁻¹⁵ near-match remains Class 2,
the anchor count remains two, and the substrate-forced ε
question remains open.

## Anti-patterns specific to this connection

Per `ansatz_audit_policy.md`:

- **Picking exponent `a` to make `13^a ≈ v/M_P`.** Trivially
  matches at `a = log_13(v/M_P) ≈ -14.99`. Class 2 by
  construction.
- **Constructing framework-integer expressions evaluating to 15.**
  Multiple exist (per null #5); none forced.
- **Folding Z_n lattices to get 15 cells.** Multiple folds give
  15 cells (per null #2). Without a canonical Z_n at the
  substrate, the choice is ansatz.
- **Importing v/M_P or any anchor-derived quantity to derive the
  depth.** Excluded by Z3 of `statistical_conventions.md`.

## Cross-references

- `anchor_count_audit.md` §Obstructions #1, #2 — the framing
- `observer_register_closure.md` §4 — direct depth-15
  identification null
- `numerology_inventory.md` — Class 2 entries for the near-matches
- `dynamical_tool_audit.md` — why this is the right axis
- `epsilon_substrate_decomposition.md` — C1 / C2 paths
- `epsilon_physical_reading.md` — sub-problem 1 audit
- `hierarchy_gaussian_lattice.md` — z₀-stratification template
  to mirror for v/M_P
- `mass_sector_closure.md` — the kind of forcing argument
  required (cross-link uniqueness theorem on (q₂, q₃))
- commits `16205d5`, `2780fd6`, `60d4e90`, `3dab11f`, `f034e69`,
  `b8911fb`, `5b65cc5` — the null-record commits

## Summary

| Status | Count |
|---|---|
| Null (specifically rules out a candidate) | 8 |
| Class 2 (numerology, near-match without derivation) | 4 |
| Wrong axis (not the right tool for the question) | 1 |
| Unattempted (sketched but not implemented) | 1 — Klein-quotient second invariant |
| Open paths (neither attempted nor refuted) | 5 — (a)-(e) above |

Eight specific candidate derivations of depth 15 from substrate
structure have failed. Five identified open paths remain, of
which (a) Klein-fold sub-action is structurally most natural and
should be attempted next.
