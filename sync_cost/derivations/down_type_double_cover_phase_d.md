# Down-type double cover — Phase D attempt: boundary-weight self-consistency

Prior phases:
- A: vocabulary; reframed target as `N_walk(T²)/N_walk(K²)`.
- B: five candidate topological ratios; four give 2 or 3/2; Attempt 5
  (stabilizer inversion) reaches 6 but imports the color assignment.
- B-followup: scan confirms no natural Z_6-action on `{A,B,C,D}` gives
  the 6:1 ratio; the hierarchy-`|Z_6|` and down-type-`6` are separate
  integer appearances.
- C: self-consistent DoF reading via abelianization rank; reaches 6
  conditional on `DoF(K²) = 1`.
- C/monodromy: the Z_2 free quotient from `klein_connection.md`
  delivers only ratio 2. A residual factor of q_3 = 3 is missing and
  is NOT supplied by pure topology.

This is exactly the shape `boundary_weight.md` addresses: **topology
gives the interval, dynamics give the point.** Phase D applies that
template to the down-type factor.

## Setup

Two topological endpoints from Phase C/monodromy:

    pure Z_2 quotient (no flip commensurability)  →  K² count = 3  →  ratio 2
    full coupling collapse (flip commensurates)   →  K² count = 1  →  ratio 6

These are the analogs of `boundary_weight.md`'s F_5 and F_6 endpoints:

    F_5 limit (w = 0)  →  Ω_Λ = 11/16 = 0.6875
    F_6 limit (w = 1)  →  Ω_Λ = 13/19 = 0.6842

Introduce a weight `w ∈ [0, 1]` controlling the commensurability
collapse on K². At `w = 0` the Klein flip acts only as a free Z_2
quotient; at `w = 1` the flip also commensurates with the y-cycle
lattice, collapsing q_3 = 3 residual y-positions to 1.

## The weight formula

Linear interpolation between the two integer endpoints of the K²
count:

    K²_count(w)  =  3 − 2w               (w ∈ [0, 1])

Ratio:

    R(w)  =  T²_count / K²_count(w)  =  6 / (3 − 2w)

Endpoints:

    R(0) = 6 / 3 = 2       (pure Z_2 quotient, Phase B.4)
    R(1) = 6 / 1 = 6       (Phase C full collapse)

Strictly monotone: `dR/dw = 12/(3 − 2w)² > 0` on `[0, 1)`. The map
`w ↦ R(w)` is invertible on the interval `[2, 6]`.

## Observed value fixes w*

The PDG 2024 observed ratio (`item12_cross_sector_ratios.md`):

    a_1(dn)² / a_1(lep)²  =  5.989 ± 0.271

Inverting `R(w) = 5.989`:

    w*  =  (3 − 6/5.989) / 2  =  (3 − 1.00184) / 2  =  0.99908

With the 0.271 uncertainty propagated:

    w*  =  0.999 ± 0.011

The observed down-type magnitude is **not** at the pure-topology
endpoint (w = 0) or at an arbitrary interior point — it is within
0.1% of w = 1, the full-coupling endpoint.

## The structural reading

`boundary_weight.md`'s precedent uses a tongue-width formula to
fix w from the coupling K*:

    w(K)  =  [(K/2)^q − (K_min/2)^q] / (K/2)^q

applied to the q = 6 mode at the F_5/F_6 boundary, giving
w* = 0.83.

The Phase D analog applies the same formula to the q_3 = 3 mode at
the K²/T² boundary:

    w_3(K)  =  [(K/2)^3 − (K_min/2)^3] / (K/2)^3
            =  1 − (K_min/K)^3

At `K = K* = 0.86196` (canonical), and for any `K_min ≪ K*`:

    w_3(K*)  ≈  1 − (K_min/K*)^3

For `K_min / K* ≤ 0.2`:  w_3 ≥ 0.992, compatible with `w* = 0.999`.

The q_3 tongue is **much wider** than the q_6 tongue
(`(K/2)^3 ≫ (K/2)^6` at `K ≈ 1`), so the q_3-commensurability
saturates much earlier on the coherence cascade than the F_5/F_6
boundary does. This is why the down-type weight is near 1 while
the dark-energy weight is 0.83 — the same mechanism at a stronger
tongue.

## Numerical sanity check

From `boundary_weight.py` the coherence-cascade K_min for first
locking at q is approximately (roughly — the precise value depends
on the cascade model):

    K_min(q)  ≈  2 · q^{-1/q}   (rough)

For q = 3:  K_min(3) ≈ 2 · 3^{-1/3} ≈ 1.387. But K_min must be < K*
for the weight to be in [0, 1]; if K_min > K*, the q = 3 mode
doesn't lock at K* and the commensurability collapse doesn't
occur, contradicting the observation.

**This is a concrete halt.** The naive K_min estimate gives
K_min(3) > K*, predicting w_3 = 0, ratio = 2. Observation requires
w_3 ≈ 1, so K_min(3) ≪ K* must hold.

The boundary_weight model of K_min may be wrong at low q; or the
low-q tongues may lock trivially (K_min(3) = 0 because q = 3 is
below the Stern-Brocot XOR-filter's primary denominator q_2 = 2).

If K_min(3) = 0 for structural reasons (q_3 is not itself a
boundary mode of the cascade; it is the INNER denominator class,
always locked at any K > 0), then:

    w_3  =  1  (for all K > 0)

and the ratio is exactly 6, **derived from topology + trivially
satisfied self-consistency.** This would close the derivation.

## Status and halts

**Phase D closes down-type to** `a_1(dn)²/a_1(lep)² = 6` **IF**:

(H1) The weight interpolation `K²_count(w) = 3 − 2w` is the correct
functional form between the two topological endpoints. Linear is
the simplest; a non-linear interpolation would shift w* but not
the endpoints. For the observed value to match exactly 6, the
formula must pass through (w = 1, count = 1).

(H2) The q_3 commensurability weight `w_3` is structurally pinned
at 1 — i.e. q_3 = 3 is "already locked" at any `K > 0` because it
is an inner Stern-Brocot denominator, not a cascade boundary mode.

Halt D1 (corresponds to H1):
The linear interpolation is a convention. A rigorous derivation
would compute `K²_count(w)` from the Klein-flip-commensurability
eigenvalue problem. This is tractable (finite-dimensional) but
not executed here.

Halt D2 (corresponds to H2):
Whether q_3 = 3 saturates to w_3 = 1 at any K > 0 depends on the
cascade structure. This is a specific, checkable claim about the
coherence cascade (`boundary_weight.py`). If true, it closes the
down-type derivation; if false, the factor 6 is a coincidence of
an interior w*.

## Why this is an advance

Compared to Phase C's halt ("justify DoF(K²) = 1"), Phase D:

- Reduces the question from "prove a specific integer count" to
  **"prove the saturation of a continuous weight at its topological
  endpoint."** The latter is strictly easier: it only requires
  showing the weight function reaches its boundary, not computing
  the boundary value.
- Uses a **template already proven successful** (boundary_weight.md,
  Ω_Λ = 0.6847 at w* = 0.83 derived from the same formula).
- Makes the connection to `K*` explicit, re-coupling the matter
  sector to the coherence cascade and providing an independent
  consistency check.
- Explains the **0.04σ agreement** with exactly 6: if w_3 is
  pinned at 1 by structural saturation, the factor is an exact
  integer, and the observation matches up to PDG-propagated
  quark-mass error.

The trade-off: Phase D commits to a specific weight interpolation
(linear in w) whose derivation from first principles is not
executed here. In return, it opens a concrete tractable route
(the Klein-flip commensurability eigenvalue problem, Halt D1) and
a concrete consistency claim (inner-denominator saturation,
Halt D2).

## Methodological note: integer equivalence vs. identity

The session produced a precise form of the user's observation that
integer equivalence (`6 = |Z_6| = q_2·q_3 = 2·3`) is not identity.
Phase B-followup refuted the `|Z_6|` reading; Phase C-monodromy
refuted the pure-topology reading; Phase D re-reads the factor as
a **saturated weight at a self-consistent boundary** rather than
an exact integer. The integer 6 is the topological ceiling of the
weight — the endpoint, not a count.

This is the `boundary_weight.md` pattern generalized: the
framework's integer predictions are frequently **ceilings of
self-consistent weights** that saturate at their topological
endpoints because of structural reasons specific to each case.
Down-type's ceiling is `q_2 · q_3 = 6`; the saturation is (H2) a
claim about inner-denominator cascade locking.

## Cross-references

| File | Role |
|---|---|
| `boundary_weight.md` | Template: topology interval + dynamical weight → unique point |
| `boundary_weight.py` | Coherence cascade data; source of `K_min` estimates |
| `down_type_dof_monodromy.py` | Source of the ratio-2 and ratio-6 endpoints |
| `down_type_double_cover_phase_c.md` | Phase C's ratio-6 reading (DoF collapse) |
| `item12_cross_sector_ratios.md` | PDG observation `5.989 ± 0.271` |
| `framework_constants.py` | `K_STAR = 0.86196052` |
