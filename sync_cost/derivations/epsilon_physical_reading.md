# Substrate-forced ε, sub-problem 1: physical reading

## What this file is

A focused dive on sub-problem 1 of
`epsilon_substrate_decomposition.md`: what *is* ε physically, in
framework-native vocabulary? Three candidate readings, each
mapped to framework structures and tested against the K-axis
window `ε ∈ [1e-4, 1e-3]` that gives K_STAR → INTERACT.

The decomposition note flagged this question. This file takes a
position: **the framework natively supplies (b) "lattice cell
width" via register cardinality, and the answer for K_STAR's
plateau membership becomes Class 2 because no canonical register
lands ε in the required window.** Reading (a) and (c) introduce
non-framework structures that have not been derived. The K-axis
uniqueness verdict should be revised accordingly.

This is the audit promised in `k_axis_uniqueness.md`'s "what
would change the verdict" section, run honestly against
sub-problem 1.

## The three readings

### (a) Observer noise floor

ε is the smallest tongue width an observer can distinguish from
quasiperiodic motion. Set by measurement bandwidth × time ×
substrate noise.

Required framework structure: a **noise model**. The framework
does not currently have one. The closest thing is
`λ_unlock = (4G − π ln 2)/π ≈ 0.471` from
`kam_bridge_synthesis.md`, which is a Lyapunov exponent at the
unlocking transition — not an observer-measurement noise.

Conversion attempt: if the substrate "decoheres" at rate
`λ_unlock` per iteration, and the observer integrates over `n`
iterations, the noise floor is `exp(−n · λ_unlock)`. For
ε = 1e-3, `n = log(1e3) / λ_unlock ≈ 14.7` iterations. For
ε = 1e-4, `n ≈ 19.6`. Neither integer is forced.

**Verdict**: not framework-native. Requires either (i) a
substrate noise derivation or (ii) a forced integration time. The
former does not exist; the latter would need to be supplied by a
particle-sector time scale (introduces v_EW anchor — fails Z3).

### (b) Lattice cell width

ε is the width of one cell when the substrate tessellates Ω ∈
[0, 1]. Set by the register cardinality `|R|` via `ε ≈ 1/|R|`
(uniform spacing) or `ε ≈ 1/|R|^α` for some packing exponent.

Required framework structure: a **register**. The framework has
two canonical registers from `observer_register_closure.md`:

| Register | Cardinality | ε = 1/\|R\| | ε at K_STAR plateau |
|---|---|---|---|
| P-reg = \|F_7\| | 19 | 0.053 | trivial (1) |
| H-reg = 6·13⁵⁴ | ~3·10⁶⁰ | ~3·10⁻⁶¹ | escape (>>11) |

Neither register supplies an ε in the [1e-4, 1e-3] window. The
window sits between them but at no canonical intermediate scale.

**Refinement**: the *Farey spacing* of P-reg is not 1/19 = 0.053
but the minimum Farey-neighbor gap, which scales as `1/F_n²` for
F_n. For P-reg = F_7, this is `1/19² = 0.0028` — still too
coarse, but closer.

| ε candidate | Value | Plateau at K_STAR |
|---|---|---|
| 1/F_7 (uniform) | 0.053 | trivial |
| 1/F_7² (min Farey gap) | 0.0028 | trivial |
| 1/F_7^{5/2} | 6.4e-4 | INTERACT |
| 1/F_7³ | 1.5e-4 | INTERACT |

The exponent jumping from 2 to 2.5 to 3 is unforced. Pure
combinatorics gives 2 (the standard Farey gap scaling).
Exponents > 2 require additional structure.

**Verdict**: framework-native. Two canonical registers exist;
neither supplies the required ε. The Farey-gap refinement
(exponent 2) tightens the scale but still misses the window.

### (c) Mode-counting threshold

ε is `1/N_modes` where `N_modes` is the count of distinguishable
substrate modes contributing to the staircase. Distinct from (b)
if modes are NOT in 1-to-1 correspondence with lattice cells.

Required framework structure: a **mode catalog**. The framework
has Klein-antipodal Z₂ rep machinery
(`klein_antipodal_z2_rep_pattern.md`) that decomposes register
states into ψ_+ / ψ_- eigenmode pairs. So mode count ≤ register
cardinality.

| Register | Modes (Klein decomposition) | ε = 1/N_modes | K_STAR plateau |
|---|---|---|---|
| P-reg = \|F_7\| = 19 | (19+1)/2 = 10 | 0.10 | trivial |
| H-reg | ~(6·13⁵⁴+1)/2 | ~6·10⁻⁶¹ | escape |

Same coarse/fine splitting as (b) but rescaled by ~2. Same
verdict.

**Refinement**: if only Klein-singlet modes are counted (the
"definite-charge" modes per `klein_antipodal_z2_rep_pattern.md`),
the count drops further. For P-reg, only the (1/2) singleton is a
Klein-singlet → ε = 1, trivial.

The "coprime-to-6" filter (used in the Ω-partition derivation)
selects Klein-singlets that can carry baryonic charge. That's
exactly the filter from `k_axis_uniqueness.md`. Mode counts under
this combined filter give 1, 3, 6, 11, 17, … — the same plateau
sequence we already found, *not* a new ε.

**Verdict**: framework-native. Reduces to (b) for cardinality
counting; introduces the same composed-filter structure already
in `k_axis_uniqueness.md` for refined mode counting. Doesn't
supply a new ε.

## Why all three readings fail to land in the window

The K_STAR-INTERACT alignment requires `ε ∈ [1e-4, 1e-3]`. None of
the three readings, with framework-canonical structures, lands ε
in this window:

- (a) requires either a noise model (none) or a particle-sector
  time scale (anchor import).
- (b) gives ε at one of two canonical scales (P-reg: 0.053;
  H-reg: 10⁻⁶¹), both outside the window. Refinements via
  Farey-gap exponents 2.5 or 3 land in window but are unforced.
- (c) reduces to (b) for counting and to the
  `k_axis_uniqueness.md` composed filter for mode counting.

**The ε window is exactly the gap between two canonical
observers.** Not above one, not below the other — between them,
in a region where no canonical framework structure supplies a
scale.

## What this implies for the K-axis uniqueness verdict

The structural plateau theorem from `k_axis_uniqueness.md`
stands intact:

- N(n) = #{Klein-antipodal Z₂-orbits of (p, q) ∈ F_n with
  gcd(q, 6) = 1} has plateaus 1, 3, 6, 11, 17, … as a pure
  combinatorial fact.
- The first three plateaus are framework integers.
- The (p−1)/2 ↔ framework-integer correspondence at primes
  p coprime to 6, p ≤ 19, is real (and specific to (q₂, q₃) =
  (2, 3)).

These do not depend on ε. They are theorems.

The K-axis tie-in (K_STAR resolves up to q = 8, lands in INTERACT
plateau) does depend on ε. With (a), (b), or (c) at canonical
framework values, K_STAR does not land in INTERACT. The
alignment exists in a window that no canonical framework
structure picks.

**Revised verdict on K-axis tie-in**: Class 2 (numerology). The
K_STAR-INTERACT alignment requires an external resolution choice
(grid resolution of the staircase scan). The framework supplies no
register, no mode count, no noise floor at the required scale.

The structural plateau theorem remains Class 5 / Survives —
it is a derivable combinatorial fact about Farey + Klein-
antipodal + coprime-to-6, and it does not need the K-axis. The
framework's existing canonical derivations (Ω partition,
down-type 6, up-type 9) all use this same plateau structure
without invoking K.

## Refined statement

Two separable claims, with separable verdicts:

1. **Plateau-structure claim** (combinatorial, K-independent):
   the composed filter on F_n has plateau values 1, 3, 6, 11,
   17, …; the first three are framework integers. **Status:
   Survives** (combinatorial theorem, replicates the same
   Klein-antipodal pattern used in down-type, up-type, Ω
   derivations).

2. **K-axis tie-in claim** (numerical, ε-dependent): K_STAR
   lands in the INTERACT plateau at the 2001-point grid
   resolution. **Status: Class 2** (no canonical framework ε
   places K_STAR in INTERACT; the alignment is observer-
   resolution-conditional).

This refines the previous "Candidate Class 4" pending verdict
into a clean separation. The PLATEAU result is structural; the
K-axis result is conditional.

## What would re-open the K-axis tie-in

The K-axis tie-in becomes Class 4 / structural again only if a
substrate-derived intermediate register is constructed at
cardinality `|R| ∈ [10³, 10⁴]`. Candidates would need to be
forced from framework structure (Klein lattice composition,
Fibonacci sub-depths, z₀-stratification, etc. — the C2 path of
the decomposition note).

The minimal acceptance criterion: an explicit register
construction with cardinality forced to within a factor of ~3 of
the K_STAR-INTERACT window center (~3000), derived from
existing framework integers without fitted exponents.

Until such a register is constructed, the K-axis tie-in is
Class 2 and should be presented that way in
`framework_status.md`.

## Connection to anchor-count obstructions

The "no canonical intermediate register" finding here is
**equivalent to anchor-count obstruction #4** (coordinate/frame
decomposition not established) at this scale:

- An intermediate register would supply a particle-sector
  resolution analogous to how the H-reg supplies the
  cosmological resolution.
- This requires a framework-derived particle-side depth count
  (anchor-count obstruction #2).
- Or a cross-sector structural identity (obstruction #5)
  forcing the intermediate scale.

Confirms the decomposition note's conclusion that ε and the
hierarchy problem are not independent.

## What I am claiming and what I am not

**Claiming**:
- The plateau theorem stands as combinatorial fact.
- The framework's canonical registers (P-reg, H-reg) do not
  supply ε in the K_STAR-INTERACT window.
- The K-axis tie-in is therefore observer-resolution-conditional
  and lands as Class 2 absent a new register.
- Sub-problem 1 ("what is ε physically?") admits the answer
  "lattice cell width via register cardinality" but the existing
  registers don't fit; reading (a) and (c) reduce to or fail
  against (b).

**Not claiming**:
- That an intermediate register cannot exist. C2 of the
  decomposition note remains a viable probe.
- That the K-axis is the wrong axis. The plateau structure
  exists; the K-axis is one way to walk through it.
- That the framework's canonical registers are wrong. P-reg and
  H-reg are correctly defined per
  `observer_register_closure.md` for their respective sectors;
  they just don't happen to land at the K_STAR window.

## Cross-references

- `epsilon_substrate_decomposition.md` — the parent
  decomposition; this file expands sub-problem 1
- `k_axis_uniqueness.md` — the result being audited
- `observer_register_closure.md` — canonical register definitions
- `klein_antipodal_z2_rep_pattern.md` — mode-counting source for
  reading (c)
- `kam_bridge_synthesis.md` — `λ_unlock` for reading (a)
- `anchor_count_audit.md` — obstructions #2, #4, #5 implicated
  in the no-intermediate-register finding
- `numerology_inventory.md` — Class 2 destination for the
  K-axis tie-in
- `framework_status.md` — needs update if this audit is accepted
