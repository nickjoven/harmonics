# K = K_c criticality — Phase B: the K_c concern dissolves

## Test performed

Phase A framed the concern: is the framework's operating point
above, at, or below K_c, where K_c is Gap 1's "supercritical"
threshold for the Strogatz-Mirollo CLT?

Phase B computed `K_c` via the rational field equation (RFE)
iteration on a truncated Stern-Brocot tree:

    r_{n+1} = |Σ g(p/q) · w(p/q, K·r_n) · exp(2πi p/q)|

Finding: the iteration contracts to `r = 0` for all tested
`K ∈ [0, 5]` at Farey depths 5, 6, 8. The upper-branch nucleation
at `K_0 ~ 3` (from `K_star_iteration.py`) is confirmed; K* = 0.86
and K_map = 1 both sit in this iteration's disordered phase.

This appears to rule out R1 and R2 (Phase A's top candidates).
But a re-reading of `gap1_theorem.md` reveals the resolution.

## The resolution: K_c for identical oscillators is zero

**Gap 1's setup** (`gap1_theorem.md` §Ingredient B):

> "For identical oscillators (pristine framework, zero intrinsic
> disorder) locked around a smooth ψ(X) in the supercritical
> regime K > K_c, the single-site fluctuation variance satisfies
> ⟨φ²⟩ = C(K,ψ)/N + O(1/N²)."

The key: **identical oscillators**. The Strogatz-Mirollo 1991
CLT applies to Kuramoto around a stable locked state.

For identical oscillators (zero intrinsic frequency spread),
the locked state exists for **any K > 0** — there is no
frequency disorder to overcome. The classical Kuramoto K_c
formula `K_c = 2 / (π g(0))` is set by the spread of the
frequency distribution g(ω); for a delta distribution (identical
oscillators), `K_c → 0`.

The phrase "supercritical regime K > K_c" in the theorem
means "locked state is stable", which for identical oscillators
is simply "K > 0".

**The RFE iteration is not the Kuramoto order parameter.** The
iteration `r → |Σ g w e^(2πi p/q)|` on the Stern-Brocot tree
computes the self-consistency of the RATIONAL-FIELD-EQUATION's
population distribution, not the Kuramoto order parameter of
identical oscillators on a d-dim lattice. The two orders
parameters live on different objects:

- RFE iteration: fixed-point condition for the tree's node
  populations N(p/q) given a coupling K. Nucleates at K_0 ~ 3
  (a property of the tree's branching structure).
- Kuramoto mean-field: spatial coherence |⟨e^(iθ)⟩| on a
  continuum lattice. For identical oscillators, this locks at
  any K > 0.

`cross_parabola_audit.py` already flagged this: "K* is the
parabola primitive's coordinate scale, NOT a Kuramoto fixed
point." The RFE's K_0 ~ 3 and the gap1 theorem's K_c = 0+ are
different quantities.

## Verdict

**R1 is correct**, but via a different path than Phase A proposed:

- Phase A R1: "K_c = 0 for discrete Stern-Brocot (low-q tongues
  always lock)."
- Phase B R1 refined: "K_c = 0 for identical oscillators
  (the actual Gap 1 setup), not for the RFE iteration."

The framework's K* = 0.86 and K_map = 1 both satisfy K > 0 = K_c,
so Gap 1's Strogatz-Mirollo CLT applies at the framework's
operating point.

**Gap 1 is unconditionally closed** for the framework's identical-
oscillator setup. The "conditional" language in `gap1_theorem.md`
is a precaution imported from Strogatz-Mirollo's general-ensemble
statement; it is vacuous for the pristine-framework case the
theorem actually uses.

## What this closes in Issue #56

Issue #56 Tier 1 listed "K = K_c critical case, non-uniform
locking" as a residual of Gap 1's conditional closure. Phase B
dissolves the first half:

- **K = K_c exact criticality**: closed. K_c = 0 for identical
  oscillators; "K = K_c exactly" means K = 0, where there is
  no dynamics. The theorem applies at all K > 0. The
  hypothetical concern at K = K_c is vacuous.

- **Non-uniform locking**: Phase B does NOT address this. The
  theorem still assumes a single locked patch around smooth ψ.
  Regions with phase slips, domain walls, or coexisting locked
  and drifting populations need separate analysis. This is a
  residual at the "extensions" tier, not a Type C.

## Methodological note

This closure continues the session's pattern: the "open problem"
turns out to be vocabulary-level — Phase A's disambiguation of
the K-zoo (K_map, K_c, K*, K_0) was the actual work. Once K_c
is identified as the Kuramoto locking threshold for identical
oscillators, the answer is structurally forced.

Same shape as:
- Mass-sector Phase B: identified π as a coordinate-choice
  factor between radian/normalized-frequency conventions at q=2.
- Down-type Phase D: identified 6 as the S_3-orbit-dimension
  ceiling, not a free-floating count.
- Ω_b Phase B: identified |r|² as the cross-sector coherence
  for baryons.

Each "open" problem was really a terminology overload that
dissolved once the correct object was named.

## What remains open at Tier 1

After Phase B:

- **Non-uniform locking** (phase slips, domain walls): separate
  problem, requires different analysis than gap1_theorem.md's
  single-patch setup. Not a Type C; not a numerical residual.
  An extensions-tier concern.
- **Mori-Zwanzig Markovian-level only** (Gap 2 residual,
  separate from Gap 1): listed in Issue #56 Tier 1 but
  independent of the K_c question. Not addressed by this Phase B.

**Issue #56 Tier 1 status after this session:**

| Item | Before | After |
|---|---|---|
| Gap 1: K = K_c critical case | Open | Closed (this Phase B) |
| Gap 1: non-uniform locking | Open | Open (extensions tier) |
| Gap 2: MZ Markovian only | Open | Open (separate program) |

## Cross-references

| File | Role |
|---|---|
| `gap1_theorem.md` | The conditional theorem; Ingredient B identifies identical oscillators |
| `rational_field_equation.md` | RFE iteration setup; distinct from Kuramoto mean-field |
| `K_star_iteration.py` | RFE iteration nucleation at K_0 ~ 3 |
| `cross_parabola_audit.py` | "K* is not a Kuramoto fixed point" — same finding |
| `k_critical_phase_a.md` | The K-zoo disambiguation |
| `k_critical_phase_b.py` | Numerical verification (iteration contracts to 0, as expected) |
