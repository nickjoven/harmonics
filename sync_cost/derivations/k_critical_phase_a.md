# K = K_c criticality — Phase A: the K zoo and the concrete concern

## Scope

Gap 1 (Christoffel from Kuramoto) is conditionally closed:
`gap1_theorem.md` establishes Γ̃ = Γ + O(1/N) in the continuum
limit, **conditional on K > K_c** (supercritical Strogatz-Mirollo
CLT). The residual in Issue #56 Tier 1 is the K = K_c critical
case: whether the framework's operating point sits above, at, or
below K_c.

Because the session's vocabulary is already established (circle
map, Kuramoto coupling, self-consistent K*, tongue width, Stern-
Brocot partition), this Phase A is short: disambiguate the
K-zoo, state the concrete concern, and enumerate resolution
candidates.

## 1. The K zoo

Four distinct quantities are called "K" or "critical" in the
framework:

| Symbol | Meaning | Value | Source |
|---|---|---|---|
| K_map | Golden-mean critical line of the circle map | 1 (exactly) | `circle_map.py`, `rational_field_equation.md` |
| K_c | Kuramoto synchronization threshold (|r| first > 0) | depends on ensemble | classical Kuramoto |
| K* | Matter-sector self-consistent operating coupling | 0.86196 | `item12_K_star_closure.py` |
| K_0 | Iteration map's contraction exponent, `r → K_0 r` | ~3 (nucleation) | `K_star_iteration.py` |

These are distinct objects in general. The framework's statement
"gravity at K = 1" means K = K_map = 1. "K* = 0.86" is a different
K — the operating point of the matter-sector closure.

## 2. The concrete concern

`gap1_theorem.md` requires **K > K_c (Kuramoto)** for the CLT to
apply. Three things we know:

- The theorem's K is the Kuramoto coupling, not K_map.
- In the framework's "gravity" regime, K = K_map = 1 is the
  stated identification.
- K* = 0.86 sits below K_map = 1.

Three things we don't know:

- Where K_c sits for the framework's actual discrete Stern-Brocot
  ensemble (vs. Lorentzian continuum where K_c = 2/π · g(0)).
- Whether "gravity at K = 1" places dynamics above K_c (locked)
  or at K_c (critical).
- Whether K* = 0.86 being below K_map = 1 means it's in the
  disordered phase of the Kuramoto iteration.

`cross_parabola_audit.py` already noted that K* = 0.86 sits
**below** the iteration's upper-branch nucleation at K_0 ~ 3,
placing it in the "disordered phase of a quadratic Kuramoto-
like map." The audit concluded K* is "the parabola primitive's
coordinate scale, NOT a Kuramoto fixed point."

This is the concrete concern: **if K* is in the disordered
phase of the Kuramoto iteration, the CLT assumption in
gap1_theorem.md may not apply at the framework's operating
point, and the conditional closure is not meaningful at
K*.**

## 3. Resolution candidates

**R1 — K_c is 0 for discrete Stern-Brocot.**

In the framework's discrete rational ensemble, the rationals
with small q dominate; these have wide tongues that lock at
any K > 0. If K_c (onset of nonzero |r|) is zero for the
framework's spectrum, then K* > K_c trivially and Gap 1 closes
unconditionally.

Precedent: the Phase D down-type saturation argument —
"q_3 = 3 is an inner denominator, fully locked at any K > 0".
Same mechanism at the coarser scale.

**R2 — K_c = K_map (framework lives at criticality).**

The framework's "K = 1 gravity" identification might place the
dynamics at the critical point K_c = K_map = 1. Then Gap 1's
conditional closure is a statement at the critical line, and
the K > K_c case is asymptotic. Critical slowing becomes a
FEATURE (the gravity side is the critical limit) rather than
an obstruction.

Precedent: the Phase C/D down-type program treated the
saturation weight w → 1 as a topological endpoint. Same shape
here: K → K_c is the gravity-side limit.

**R3 — K* separate from K_c (clean separation).**

K* is the matter-sector parameter, not the gravity-sector
coupling. Gap 1 closes at K_map = 1 (gravity); matter phenomena
at K* are a different regime. The two couplings are structurally
distinct and serve different roles. No single K governs all
observables.

Precedent: the cross_parabola_audit.py verdict — "K* is the
parabola primitive's coordinate scale, not a Kuramoto order
parameter." This is already established in the codebase;
Phase B would just formalize it.

**R4 — CLT extends to K = K_c via renormalization.**

The CLT fails at K = K_c because fluctuations diverge. A
renormalization-group treatment (e.g. Wilson-Fisher near the
Kuramoto critical point) could extend the fluctuation analysis
to criticality. This is a technical extension, not a structural
claim.

Precedent: weakest in the session. Would require new RG
machinery not currently in the framework.

## 4. Ranking by session methodology

The session's successful pivots favour (in order):

1. **R1 — discrete saturation** (highest leverage).
   - Matches Phase D down-type closure pattern exactly:
     inner-denominator saturation means K_c = 0 for the
     relevant inner modes.
   - Uses no new machinery.
   - Closes Gap 1 unconditionally if true.

2. **R2 — criticality = gravity** (natural).
   - Re-reads the "K = 1" identification as the CRITICAL limit,
     not a supercritical operating point.
   - Matches the framework's own "gravity is the K = 1 limit"
     language.
   - Closes Gap 1 by REFRAMING the condition as the content.

3. **R3 — clean separation** (already in codebase).
   - Requires no new work — cross_parabola_audit.py has it.
   - Weakest because it doesn't actually resolve the
     "K = K_c exact" case for the gap1 theorem — it just says
     "gap1 doesn't apply to K*, applies to K_map."

4. **R4 — RG extension** (heavy).
   - Requires machinery not in the session.
   - Cold start; not a high-leverage path.

## 5. Phase B plan

The simplest numerical test is to compute K_c for the framework's
Stern-Brocot ensemble directly. Concretely:

1. Write the rational field equation's self-consistency equation
   on a truncated Stern-Brocot tree (depth 6 gives 63 nodes).
2. Solve for |r| as a function of K ∈ [0, 2].
3. Find the smallest K where |r| > 0 (this is K_c).
4. Compare to K*, K_map.

If K_c = 0 (no threshold, all K give |r| > 0): R1 supported.
If K_c = 1 (matches K_map): R2 supported.
If K_c is interior to (0, 1) and below K*: R3 supported.

This is a concrete ~50-line script building on the existing
rational_field_equation.md / K_star_iteration.py machinery.

## 6. What Phase A establishes and does not

**Establishes:**

- Four distinct K's in the framework (K_map, K_c, K*, K_0)
  and their relationships.
- The concrete concern: is the framework's operating point
  (gravity-side K_map = 1 or matter-side K* = 0.86)
  supercritical, subcritical, or at K_c?
- Four resolution candidates ranked by methodological
  plausibility.

**Does not establish:**

- Which candidate wins (Phase B).
- A numerical value for K_c (Phase B).
- Whether Gap 1 actually closes unconditionally or remains
  conditional (pending Phase B).

## 7. Cross-references

| File | Role |
|---|---|
| `gap1_theorem.md` | Source of the K > K_c condition |
| `rational_field_equation.md` | Part VI open questions, K_c definition |
| `K_star_iteration.py` | K_0 nucleation at ~3, K* in disordered phase |
| `cross_parabola_audit.py` | "K* is parabola coordinate, not Kuramoto fixed point" |
| `item12_K_star_closure.py` | K* = 0.86196 derivation |
| `down_type_double_cover_closed.md` | R1 precedent (inner-denominator saturation) |
| `boundary_weight.md` | R2 precedent (topology-endpoint readings) |
