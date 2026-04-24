# Substrate-forced ε: problem decomposition and prior nulls

## What this file is

A research note — not a derivation. Decomposes the open question
left by `k_axis_uniqueness.md` ("does the substrate force a
specific resolution ε?") into sub-problems, gathers prior null
results that constrain candidate paths, and ranks the remaining
candidate sources of ε by structural plausibility.

This sits at the intersection of `observer_register_closure.md`,
`anchor_count_audit.md`, and `k_axis_uniqueness.md`. None of those
three resolves the ε question on its own.

## Why this matters

`k_axis_uniqueness.md` produced a clean structural finding (the
composed Klein-antipodal ∩ coprime-to-6 filter on Farey sets has
plateau values 1, 3, 6, 11, 17, …; the first three are framework
integers). The K-axis alignment of K_STAR with the INTERACT
plateau holds *across the resolution window* `ε ∈ [1e-4, 5e-4]`
but flips at coarser ε to the q₃ plateau or trivial plateau.

The window where K_STAR matches INTERACT is not narrow (5x in
ε), but it is not framework-supplied either. Without a substrate-
forced ε, the K-axis result remains candidate Class 4. With a
forced ε, it upgrades to a structural derivation of `INTERACT =
q₂·q₃` from joint K-axis + Klein + coprime-6 + register
machinery.

## Sub-problems

### Sub-problem 1 — what is ε physically?

Three operational definitions, each with different forcing
arguments:

(a) **Observer noise floor.** ε is the smallest tongue width an
    observer can distinguish from quasiperiodic motion. Set by
    measurement bandwidth × time × noise.

(b) **Lattice cell width.** ε is the width of one cell in a
    substrate-supplied tessellation of `[0, 1]` in Ω. Set by the
    register cardinality `1/|R|`.

(c) **Mode-counting threshold.** ε is the inverse of the number
    of distinguishable substrate modes contributing to the
    staircase. Set by mode count, which may differ from register
    cardinality.

Each definition selects a different framework structure as the
ε-supplier. They may agree in the ε ∈ [1e-4, 1e-3] window or may
not.

### Sub-problem 2 — what natural scale does the framework supply?

Direct register cardinalities (per `observer_register_closure.md`):

| Source | Value | ε = 1/value | Verdict for K_STAR INTERACT window |
|---|---|---|---|
| P-reg = \|F_7\| | 19 | 0.053 | TOO COARSE (K_STAR → trivial) |
| H-reg = 6·13⁵⁴ | 6·13⁵⁴ | infinitesimal | TOO FINE (K_STAR → escape) |
| Z_{q₂q₃} = Z_6 | 6 | 0.167 | TOO COARSE |

None of the canonical register cardinalities lands in the window.

Intermediate cardinalities not yet derived:

| Candidate | Value | ε estimate | In window? |
|---|---|---|---|
| F_15 | 610 | 0.0016 | borderline (just above) |
| F_16 | 987 | 0.0010 | yes |
| F_17 | 1597 | 0.00063 | yes |
| F_18 | 2584 | 0.00039 | yes |
| 13^{7/2} (z₀-stratification at P-reg depth) | 6189 | 0.00016 | yes |
| 13^4 | 28561 | 3.5e-5 | TOO FINE |

Fibonacci-depth `F_n` for `n ∈ [16, 18]` and Gaussian-norm
`13^{k/2}` for half-integer `k ≈ 3.5` cover the window. Both are
substrate-flavored quantities; neither is forced as the canonical
resolution.

### Sub-problem 3 — does ε vary with the K-axis?

Open. The K-axis sweeps the staircase from K=0 (no tongues) to
K=1 (devil's staircase). At each K, the *natural* resolution
might differ — e.g., set by the smallest tongue width above noise.
If `ε(K) = w_smallest(K)`, then ε is K-dependent and the plateau
walk is automatic: ε always sits at the boundary of resolution.

This would make the K-axis self-consistent: ε(K) tracks the
smallest resolved tongue at each K, and the plateau structure
emerges as K varies.

But "smallest resolved tongue" is itself circular — it's defined
by ε. The chicken-and-egg problem is the substantive content of
the question.

### Sub-problem 4 — what would substantively close the question?

A derivation of the form:

    ε = f(framework integers, framework constants, K)

with no fitted exponents and no anchor imports, such that the
K-axis composed with this ε produces a plateau structure where
K_STAR robustly lands at INTERACT and (separately) other
canonical K-values land at framework-integer plateaus.

The minimal acceptance criterion: a closed expression for ε with
≤ 1% sensitivity to the choice of "natural" framework structure
within a ratio-of-canonical-quantities sweep.

## Prior nulls (constraints on candidate paths)

The following routes have been tested and found null. Any new
candidate must avoid these dead ends.

### N1. Direct register cardinality is wrong-scale.

`observer_register_closure.md` §6 establishes that P-reg supplies
ε too coarse and H-reg supplies ε too fine. The register-as-
resolution interpretation does not pin v_EW or any intermediate
scale. **Null**, recorded in §3 and §4 of that file.

### N2. v/M_P ≈ 13⁻¹⁵ is unforced.

`anchor_count_audit.md` §1 + `numerology_inventory.md` Class 2:
the depth-15 identification is one of multiple framework-integer
expressions that evaluate near 15, none forced by the
register's structure. The same null reappears as obstruction #1
of the anchor-count audit. **Class 2.**

### N3. H-reg ↔ P-reg parametric interpolation has no canonical form.

Commit `f034e69` (Log probe): four routes tested
(continuous interpolation, shared-13, Klein-antipodal of z₀,
moiré period 19·54 = 1026), all null. The two registers are
co-existing facets of the same substrate, not endpoints of a
single parametric family with intermediate ε's. **Null
(numerology),** logged §7 of `observer_register_closure.md`.

### N4. ε = (1−K)^β with β from framework.

Tested in `k_axis_uniqueness.md`'s triage Section. No β is forced;
multiple β produce the K_STAR-INTERACT alignment, none is
preferred structurally. **Null.**

### N5. ε = 1/Q_MAX with Q_MAX framework-derived.

Tested in `k_axis_uniqueness.md`. Q_MAX = 21 (covers F_7) gives
ε = 0.048 — coarse, putting K_STAR in q₃ plateau (3 orbits) not
INTERACT. Q_MAX = 19 = P-reg gives the same. **Null** for the
specific choice; not refuted for some derived Q_MAX in the
[610, 2584] range, but no such derivation exists.

### N6. K^14 = 1/8 as ε source.

`numerology_inventory.md` Class 2 (commit `b8911fb`). K_STAR^14
gives a small dimensionless number 1/8 ≈ 0.125 — not in window;
also Class-2-demoted as ansatz. Not a candidate. **Class 2.**

### N7. Pythagorean comma vs K_Greene (1/74).

`numerology_inventory.md` Class 2: 1/74 ≈ 0.0135 — coarser than
the INTERACT window. Not viable as ε. **Class 2.**

### N8. v_EW = ω₀-substrate frequency (no derivation).

Anchor-count obstruction #3: no framework-native derivation of
ω₀ = v_EW/ℏ exists. Without it, v_EW remains a free anchor and
cannot supply ε structurally. **Open obstruction, not yet null.**

## Untested candidates (ranked)

Ranking by structural plausibility — not by likelihood of being
right.

### C1. Fibonacci-depth ε with depth tied to substrate cross-section

`anchor_count_audit.md` notes "145.8 Planck-to-Hubble Fibonacci
levels." The cosmological hierarchy uses the full 145.8; a
particle-sector hierarchy at the EW scale would use a shorter
depth. If `n_EW` is structurally identified, `ε = 1/F_{n_EW}` is
forced.

Candidate values: `n_EW = 16` gives `1/F_16 ≈ 0.001` (in window
upper edge); `n_EW = 17` gives `1/F_17 ≈ 0.00063` (centered).

Required derivation: a Fibonacci-depth count for v_EW. This is
**exactly anchor-count obstruction #2**. Lifting it would also
close the hierarchy problem. So C1 is co-extensive with a major
open framework problem.

Verdict: **structurally significant, audit-blocked by
obstruction #2.** Progress here would be progress on multiple
fronts.

### C2. Klein z₀-stratification at half-integer depth

`hierarchy_gaussian_lattice.md`: z₀ = q₂ + i q₃ = 2 + 3i, |z₀|² =
13. The H-reg uses depth 54 (=6·9 = |Z_6|·q_3²). The P-reg uses
depth 7 (=|F_7|=19, but with depth interpretation 7 from F_7).

A "particle-side" depth `k` with `1/|z₀|^k` in the K_STAR-INTERACT
window: `|z₀|^k = √13^k = 13^{k/2}`. Solving `13^{k/2} ∈ [10³,
10⁴]`: `k/2 ∈ [log_13(10³), log_13(10⁴)] = [2.69, 3.59]`. Half-
integer candidates: `k = 6` (giving |z₀|^6 = 13^3 = 2197, ε ≈
0.00046, in window) and `k = 7` (giving 13^{3.5} ≈ 6189, ε ≈
0.00016, also in window).

Required derivation: an argument forcing a specific
half-integer or integer depth `k` in the substrate at the
particle-sector scale. The most natural source: a fold/cover
between the |Z_6| × ⟨z₀⟩₅₄ × ⟨ι⟩ register action and a particle-
sector sub-action.

Verdict: **moderately plausible, audit needed.** The available
data (registers exist at depths {0, 7, 54}) doesn't immediately
suggest a fourth canonical depth, but the Z_6-fold structure
(54 = 6·9) is consistent with sub-actions at depths {6, 9, 18,
27}.

### C3. K-axis self-consistent ε

If `ε(K)` is defined as the smallest tongue width above some
external floor, the K-axis defines its own resolution. As K
increases, more tongues exceed the floor; the plateau walk
emerges from K alone.

The "external floor" doesn't go away — it just gets pushed to a
substrate-noise question. If the substrate has a finite mode
count `N_modes`, the natural floor is `1/√N_modes` (CLT noise).

For `N_modes = R = 6·13⁵⁴`, floor ~ 13⁻²⁷, far below window.
For `N_modes = R^{1/4}`, floor ~ 13⁻⁶·⁷⁵, marginal.
For `N_modes = F_7 · q_3² = 19·9 = 171`, floor ~ 1/√171 ≈ 0.076,
too coarse.

Required derivation: identify the "right" N_modes for the
particle sector. This is a re-statement of the cross-sector
decoupling (anchor-count obstruction #5).

Verdict: **physically motivated, audit-blocked by obstruction
#5.** Progress requires the cross-sector structural connection
that doesn't yet exist.

### C4. Lyapunov-exponent ε at K_STAR

The standard circle map at K_STAR < 1 has all locked orbits with
negative Lyapunov exponent λ. The Lyapunov-vanishing line is
K=1. Define `ε = exp(λ(Ω̄, K_STAR))` for some canonical Ω̄.

For K=K_STAR and Ω̄ at the (1/2)-tongue center, λ ≈
log|1 − K_STAR² cos²(2π·0)| ≈ log|1 − K_STAR²| (rough estimate
needs check).

Required derivation: identify the canonical Ω̄ (the natural
"substrate frequency" of the locking) without anchor input.

Verdict: **substrate-derived but underspecified.** No prior null,
but no clear path to forcing Ω̄ either.

### C5. Anchor-derived combinations

ε = function of (v/M_P, Λ·ℓ_P², R, …). Trivially can be tuned to
any value. Excluded by Z3 of `statistical_conventions.md` —
imports anchor information, defeats the purpose.

Verdict: **excluded by framework discipline.**

## What links this to the rest of the framework

The ε question sits inside the larger "five obstructions to one
anchor" enumeration in `anchor_count_audit.md`:

| Obstruction | Connection to ε |
|---|---|
| #1 (v/M_P unforced) | C5 excluded; C1 partially overlaps (forcing depth would force v/M_P) |
| #2 (no Fibonacci-depth for EW) | C1 directly co-extensive |
| #3 (no ω₀ substrate) | C4 needs ω₀; C5 excluded |
| #4 (coordinate/frame split) | C3 implicitly assumes the split exists |
| #5 (cross-sector decoupling) | C3 directly co-extensive |

The ε question is therefore **not independent** of the existing
hierarchy-problem-as-anchor-count problem. Solving ε
substrate-natively would solve at least one of the five
obstructions; conversely, any of the five obstructions being
lifted is likely to supply ε.

This is good news for the framework's parsimony (the open
problems form a tight cluster) and bad news for short-term
progress (no cheap path).

## Suggested probe sequence

If pursuing this, the lowest-cost probes first:

1. **C2 audit.** Enumerate candidate depths `k ∈ {6, 7, 9, 18,
   27}` from sub-actions of the canonical register. For each,
   compute `ε = |z₀|^{-k}` and recompute K_STAR's plateau
   membership. Check if any specific `k` gives a robust
   alignment. *Cost: a few hours; reuses k_axis_uniqueness.py.*

2. **C4 numeric.** Compute the Lyapunov exponent at K_STAR
   along the (1/2) and (1/3) tongues. Check whether `exp(λ)`
   sits in the window without further specification. *Cost: low,
   reuses circle_map.py utilities.*

3. **C1 structural.** This is anchor-count obstruction #2. Out
   of scope for an ε-focused probe, but a successful resolution
   here would supply ε automatically. Cross-link is worth
   recording.

The C3 and C5 paths require structural derivations that exceed
single-session scope; flag for longer-term work.

## Anti-patterns to avoid

Per `ansatz_audit_policy.md`:

- **Picking ε to make N(K_STAR, ε) = 6.** Trivially possible,
  Class 2 by construction.
- **Constructing a framework-integer expression evaluating to
  ~10⁻³.** Multiple expressions match (e.g., 1/(F_7 · q_3²) =
  1/171 ≈ 5.8e-3, or q_3⁻⁹ ≈ 5e-5); none forced.
- **Combining unrelated framework integers** (e.g., 1/(13⁷ · q₂)
  ≈ 6.3e-9, way out of window) just because the resulting number
  is small.

Each of these would replicate the K^14 = 1/8 demotion pattern.

## Status

Open. This decomposition does not solve the substrate-forced ε
problem. It records what's been ruled out and what hasn't been
tried with clear forcing arguments.

The most promising near-term probe: **C2 (Klein z₀-stratification
at half-integer depth)**, which has a concrete numeric path and
would either produce a structural ε candidate or a sharpened
null.

## Cross-references

- `k_axis_uniqueness.md` — the result whose ε this question
  closes
- `observer_register_closure.md` §6 — the existing register
  cardinalities (P-reg, H-reg) and why they don't supply ε
- `anchor_count_audit.md` — the five obstructions, three of which
  intersect this question
- `numerology_inventory.md` — Class 2 entries that constitute
  prior nulls
- `ansatz_audit_policy.md` — the discipline against tuning ε
- `hierarchy_gaussian_lattice.md` — z₀ stratification and the
  R = 6·13⁵⁴ derivation
- commit `f034e69` — H-reg ↔ P-reg interpolation null
- commit `b8911fb` — K^14 = 1/8 demotion (an ε-tuning anti-
  pattern)
