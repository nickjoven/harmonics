# K_inflation: the obstruction is structural, not a missing calc

Audit Finding 4 (`audit_findings_3_4_disposition.md`) left two
live open items: the framework cannot pin `K_inflation`, and
`s_inst_inflation.md` (`|∇K|_inflation ≈ 2`) vs
`inflation_duration.md` (`≈ 3.55`) is an "unresolved two-reading
problem." This doc disposes of both, using the corrected
`S_v(K=1) ≈ 11.515` (`discrete_reduction_computed.md`, canonical).

**Result:**
1. The two-reading problem is **reconciled** — it was an
   approximation/normalization artifact (prefactor dropped vs.
   kept) compounded by the stale `S_v = 16`. Treated consistently
   with the corrected `S_v`, both readings collapse to a single
   value `|∇K|_inflation ≈ 2.68`.
2. `K_inflation` **cannot be pinned by the geometric seam form —
   structurally, for any K**. The framework's geometric seam
   gradient `|∇K| = (1−K)√K` combined with the framework's own
   K-dependent action makes the Schwinger exponent
   `π S_v(K)/|∇K|(K) = π·11.515/(1−K) ≥ 36.2` for *every*
   `K ∈ [0,1)` — the K-dependence cancels — whereas inflation-era
   `H` needs exponent `≈ 13.5`. Max achievable `H·t_P` over all K
   is `≈ 2×10⁻¹⁸`; inflation needs `10⁻⁵`. A `~10¹²` shortfall at
   every cascade depth. This is not an uncomputed number; the
   equation has no solution.

The honest consequence: Finding 4 is **sharpened, not closed**.
Inflation duration remains conditional, but the conditionality is
now one sharp, well-posed structural question (the inflation-era
seam structure) rather than an un-pinnable free parameter.

## The two readings, diagnosed

Both readings use the universal Schwinger relation

    H·t_P = exp(−π S_v / |∇K|) · |∇K|²

- **`inflation_duration.md` (`≈ 3.55`):** the *full* relation,
  inverted at observed `H_inflation·t_P ≈ 10⁻⁵`, with `S_v = 16`.
- **`s_inst_inflation.md` (`≈ 2`):** the *prefactor-dropped*
  approximation `S_inst = π S_v/|∇K|`, set to the
  `S_inst ≈ 25.3` that yields the standard `~10⁻³² s`, with
  `S_v = 16`: `|∇K| = π·16/25.3 ≈ 1.99`.

Same physics; the gap was (a) keeping vs. dropping the `|∇K|²`
prefactor and (b) the stale `S_v`. Recomputing the *full* relation
with the corrected `S_v = 11.515`:

| Treatment | `S_v` | `|∇K|_inflation` |
|---|---|---|
| full relation | 16 | 3.58 |
| prefactor-dropped | 16 | 1.99 |
| full relation | **11.515** | **2.68** |
| prefactor-dropped | 11.515 | 1.43 |

The two readings were never a physics inconsistency — they are the
same relation under two approximations. The framework-correct
treatment is the full relation with the canonical `S_v`:
**`|∇K|_inflation ≈ 2.68`**, a single pinned magnitude. The
"unresolved two-reading problem" is downgraded to "an
approximation artifact, reconciled."

## Why K_inflation cannot be pinned — the structural theorem

The framework's geometric derivation of the seam gradient is
`|∇K|_seam(K) = (1−K)√K` (bounded above by `0.385` at `K = 1/3`;
`inflation_duration.md` open #2). To pin `K_inflation` one would
solve

    (1−K)√K  =  |∇K| required by the Schwinger relation at H_inflation

simultaneously with the framework's K-dependent action
`S_v(K) = 11.515·√K` (the discrete-corrected continuum scaling;
`unitless_audit.md`'s `S_v ∝ √K` via `M_k ∝ √(Kr)`, renormalized
to the canonical K=1 value).

Substitute the geometric form into the Schwinger exponent:

    π S_v(K) / |∇K|(K)
      = π · 11.515·√K / [ (1−K)√K ]
      = π · 11.515 / (1−K)
      ≥ π · 11.515
      ≈ 36.2          for all K ∈ [0, 1)

**The `√K` cancels exactly.** The geometric-seam Schwinger
exponent is `≥ 36.2` independent of cascade depth. Inflation-era
`H·t_P ≈ 10⁻⁵` requires exponent `≈ 13.5` (the `|∇K| ≈ 2.68`
solution). `36.2 > 13.5` with no K-dependence to close the gap.

Numerically, maximizing the full geometric system
`exp(−π·11.515·√K / [(1−K)√K]) · [(1−K)√K]²` over `K ∈ (0,1)`:

    max_K (H·t_P)_geometric  ≈  1.8 × 10⁻¹⁸   (at K ≈ 0.025)

against the inflation requirement `10⁻⁵`: a shortfall of
`≈ 5 × 10¹²` — twelve orders of magnitude, at the *best* K.

So there is no `K_inflation` at which the framework's geometric
seam form reproduces inflation-era `H`. K_inflation is not
*unknown*; the geometric route to it is *structurally closed* by a
12-order margin that no choice of K can bridge (the K-dependence
provably cancels in the binding exponent).

### What the cancellation *is* (no new input — an existing inviolable)

The `√K` cancellation is not an algebraic accident. `S_v ∝ M_k`
(kink **mass**, `∝√K`) and `|∇K|_seam = (1−K)/ℓ_kink` with
`ℓ_kink ∝ 1/√K` (kink **width**); their ratio carries
`M_k·ℓ_kink = K-independent constant` — the sine-Gordon
**mass–width invariant** (the kink's dimensionless action is
coupling-independent, BPS-like). That invariant *is*
`substrate_determinism.md` **inviolable #1** (Z₂/winding
topological-charge conservation — "no local process changes `Q`";
the kink's content is rigid) carried by **inviolable #9**
(arrow-of-time monotonicity — the irreversible iteration cannot
perform the inverse move that would dissolve a topological
quantum). Conservation-of-(topological)-charge tied to
irreversibility-of-iteration, expressed through the kink. So the
obstruction is **structurally protected by inviolables the
framework already declared — not a new structural input and not a
numerical near-miss**. (Only the *exponent* carries the clean
cancellation; the full Schwinger prefactor `|∇K|²` remains
K-dependent but bounded — the structural claim is specifically
that the binding exponent is floored at `π·S_v(K=1) ≈ 36.2 ∀K`.)

## Honest disposition (sharpens Finding 4)

| Finding-4 item | Prior status | Now |
|---|---|---|
| `s_inst` ≈2 vs `inflation_duration` ≈3.55 | "unresolved two-reading problem" | **reconciled** — approximation artifact; consistent value `|∇K|_inflation ≈ 2.68` |
| Required `|∇K|_inflation` | `≈ 3.55` (stale `S_v=16`) | **`≈ 2.68`** (canonical `S_v`) — pinned magnitude |
| Pin `K_inflation` via geometric seam | "open; seam must differ" | **structurally impossible ∀K** (12-order, K-cancelling shortfall) — proven, not deferred |
| Inflation duration parameter-free | retracted → conditional on `K_inflation` | conditional on **one** well-posed item: the inflation-era seam *structure* (open #2), not an un-pinnable K |

What survives unchanged: the *mechanism*
(`duration = exp(S_v(K))/H_inflation`, `f_exit_natural.md`); the
order-of-magnitude `~10⁻³² s` *as a conditional result* (now
conditional on a non-geometric inflation-era seam delivering
`|∇K| ≈ 2.68`, not on an unknown K).

What is newly closed: the two-reading problem (artifact), and the
*hope* that K_inflation is merely uncomputed (it is structurally
unreachable via the geometric form — the residual open item is
strictly the seam *structure*, `inflation_duration.md` open #2).

## The single remaining open item — now CLOSED

> **CLOSED (`inflation_seam_anchor_closure.md`).** Resolved as
> the second bullet below (the principled one-input boundary):
> `|∇K|_inflation` is the Schwinger-image of `H_inflation`, an
> out-of-class anchor by the framework's own taxonomy — so the
> geometric obstruction proved here is the framework *correctly
> declining* to manufacture an anchor-side quantity from
> substrate geometry (same accepted shape as the A_s/Instance-7
> closure; an instance of two-anchor minimality). NOT a
> prediction of 2.68. The text below stated the open fork; the
> first bullet (a derived non-geometric seam) is foreclosed.

`inflation_duration.md` open #2, now sharply posed: **the
inflation-era seam cannot be the geometric `(1−K)√K` form** (it
undershoots required `|∇K|` by `~10¹²` at every K). Either

- the inflation-era seam has a different, non-geometric structure
  delivering `|∇K| ≈ 2.68` (what structure? — genuinely open), or
- the framework cannot predict inflation duration without an
  independent `|∇K|_inflation` (≈ 2.68) input — an honest
  one-input boundary, not a hidden free parameter.

Either way the un-pinnable quantity is now a *single, named,
O(1)* number (`|∇K|_inflation ≈ 2.68`), with the two-reading
confusion and the false "K_inflation is just uncomputed" framing
both removed.

## Status

Class 3 (honest disposition + computed sharpening). No new
primitive. Reconciles Finding 4's two-reading problem (artifact);
proves the geometric route to `K_inflation` is structurally closed
∀K by a K-cancelling 12-order margin; reduces the residual open
item to one well-posed question (inflation-era seam structure)
with a single pinned target `|∇K|_inflation ≈ 2.68`. Downstream of
`discrete_reduction_computed.md`'s canonical `S_v(K=1) ≈ 11.515`.

## Cross-links

- `audit_findings_3_4_disposition.md` — Finding 4; this doc
  sharpens it (two-reading reconciled; K_inflation obstruction
  proven structural).
- `discrete_reduction_computed.md` — canonical `S_v(K=1) ≈
  11.515`, the input that reconciles the two readings and lowers
  required `|∇K|_inflation` 3.58 → 2.68.
- `inflation_duration.md` — open #2 (seam structure) is now the
  sole residual; its `≈ 3.55` is updated to `≈ 2.68`.
- `s_inst_inflation.md` — its `|∇K| ≈ 2` is the prefactor-dropped
  reading; reconciled here, not a competing physics value.
- `unitless_audit.md` — `S_v ∝ √K`; the √K cancellation in the
  geometric-seam exponent is the structural core.
- `substrate_determinism.md` — **inviolables #1 (Z₂/winding
  topological-charge conservation) ∧ #9 (arrow irreversibility)**:
  the `√K` cancellation *is* the kink-borne mass–width invariant,
  i.e. these inviolables expressed through the soliton — the
  obstruction's structural protection, no new input.
- `thread_chronology.md` — ledger; #INF row links up to these
  inviolables.

## One-line summary

The corrected `S_v ≈ 11.515` reconciles the inflation
two-reading problem to a single `|∇K|_inflation ≈ 2.68`, and
proves `K_inflation` is unreachable via the geometric seam form
for *every* K (the `√K` cancels, leaving Schwinger exponent
`≥ 36.2` vs. the `≈ 13.5` inflation needs — a K-independent
`10¹²` shortfall); Finding 4's residual is now one well-posed
question (inflation-era seam structure), not an un-pinnable
parameter.
