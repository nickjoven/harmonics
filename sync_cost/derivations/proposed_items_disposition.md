# #PROPOSED: disposition of the three items

> **READ FIRST.** Dispositions the three `#PROPOSED`-tier items.
> Net state only. **Bright line: nothing here claims a closed form
> (none exists in KAM generally); the `K_c ≈ Σw` proximity is a
> flagged open conjecture, NOT a result; B's dynamical residuals
> stay genuinely open, not declined.**

## Item A — `K_c(F_n/F_{n+1})` closed form

**Gap-1 K_c is closed; `k_critical_phase_b.md` is authoritative
and this doc defers to it.** That doc established `K_c = 0` for
the framework's identical-oscillator setup (classical
`K_c = 2/(πg(0)) → 0` for a delta distribution); the RFE
iteration is a different object from the Kuramoto order parameter;
the "K_c concern" was K-zoo vocabulary overload
(K_map / K_c / K* / K_0), dissolved by Phase A. Not reopened.

**The framework's critical line is `K_map = 1` exactly**
(`k_critical_phase_a.md` K-zoo table). The framework *uses*
`K_map = 1`; it needs no finite-`n` per-Fibonacci-convergent
threshold.

**The Proposed upgrade criterion** — "explicit form beyond
asymptotic `δ⁻ⁿ` scaling" for `K_c(F_n/F_{n+1})` — asks for the
closed form of the circle-map critical coupling at finite
Fibonacci convergents, whose `δ⁻ⁿ` approach to the `K=1`
golden-mean line is classical KAM scaling. **No such closed form
is known in the general KAM literature** (the universal `δ` and
the per-convergent thresholds are computed numerically, not in
closed form, in the field at large). It is therefore a
**known-hard external-mathematics problem, not a framework gap**:
the framework's content (`K_map = 1` exact; Gap-1 dissolved) is
already settled; the missing closed form is a general open
problem the framework neither has nor needs. **Disposition:
out of scope — not a framework deliverable; the framework uses
`K_map = 1` exact.**

**Secondary recorded finding (refines, does not contradict,
`k_critical_phase_b.md`).** The RFE self-consistency
`|r| = |Σ w(p/q,K₀|r|) e^{2πi p/q}|` (canonical width
`w=2(K/2)^q/q`, discrete counting `g=1`), solved for the
*existence* of a nonzero branch (saddle-node tangency
`max_r[M(r)−r] ≥ 0`), depths 6–12:

| depth | nodes | K_c^RFE |
|---|---|---|
| 6 | 63 | 1.486 |
| 8 | 255 | 1.511 |
| 10 | 1023 | 1.528 |
| 12 | 4095 | 1.539 |

Increments fall geometrically (ratio ≈0.63) ⇒ converges to
**≈1.55–1.56**; small-`|r|` exponent **exactly 2** ⇒ the nonzero
branch is born by a **saddle-node (first-order, parabola
primitive)**, not a second-order Kuramoto transition.
Consistent with `k_critical_phase_b.md`: forward iteration
contracts to `r=0` for all `K∈[0,5]` with upper-branch
iteration-nucleation at `K_0 ~ 3` (`K_star_iteration.py`) — the
branch is *born* (unstable+stable pair) at `K_c^RFE ≈ 1.56` but
only *reached by naive iteration* near `K_0 ~ 3`; both differ
from Gap-1 `K_c = 0`. Three distinct K-zoo objects, one tree.

> **Flagged conjecture, explicitly NOT claimed.** `K_c^RFE → ≈1.56`
> is strikingly close to `#FLOW`'s `Σ_{p/q} w(p/q,1) = 1.5617`.
> Structurally plausible (same tongue-width sum) but **not
> demonstrated**; per the framework's pigeonhole / honest-landing
> discipline, a numerical near-match is **not** a closed-form
> result. Recorded as an open structural conjecture only.

## Item B — T2#7 measurement-arc residuals

**Anchor-side; partial Basepoint closure.** The blocking residual
("iteration-to-time anchor") is **out-of-class / anchor-dependent**
(iterations→seconds needs `H_0`; `framework_status.md`
"Out of class: τ_unlock(n) in seconds | H_0"; cited so in
`inflation_seam_anchor_closure.md`). It **closes as a
Basepoint-Principle decline** — the `#INF` / A_s-Instance-7 shape.
**Honest residual: the two *dynamical* sub-residuals — continuous
K(t) during measurement, multi-tongue cascade — are not
anchor-side; their absence is operational, so by the Basepoint
discriminator they remain GENUINELY OPEN, not declined. B is a
partial closure.**

## Item C — K-zoo kink-mass ratios

**Class-2 by construction; disposed, not chased.**
`M_k(d,n,b)/M_k(K=1) = b^(−n/(2d))` is **rigorous at K=1**
(Class 3, `sine_gordon_substrate.md` L100–107). At K<1 it rests on
an unproven working assumption (each cascade sector hosts an
analogous sine-Gordon reduction; ibid. L72–85) plus a
multi-candidate observable-identification with no forcing argument
→ **Class-2 by construction** (`ansatz_audit_policy.md` Step-4
default; `numerology_count_phase_b.md` pigeonhole verdict).
Disposition: the K=1 formula stands (Class 3); the K<1 mapping is
**correctly not pursued** — a standing Class-2-flagged conjecture,
not closed and not chased.

## Net for #PROPOSED

| Item | Disposition |
|---|---|
| **A — K_c** | Gap-1 K_c closed (`k_critical_phase_b.md`, deferred-to); framework critical line `K_map=1` exact; finite-`n` Fibonacci closed-form **out of scope** (known-hard KAM, not a framework gap). Secondary: RFE branch born first-order at `K_c^RFE≈1.56`; `K_c^RFE=Σw` an explicitly-flagged **open conjecture**, not claimed. |
| **B — T2#7** | Iteration-to-time anchor **Basepoint-closed** (#INF pattern). Continuous-K(t) & multi-tongue residuals **remain genuinely open** (operational). |
| **C — K-zoo** | **Class-2 disposed.** K=1 formula Class-3 (stands); K<1 mapping correctly not chased; standing flagged conjecture. |

`#PROPOSED` does not fully vanish. Reduced residual: B's two
dynamical sub-residuals + C's K<1 conjecture (flagged, not
chased). Stated, not compressed away.

## Status

Class 3 (disposition). No new primitive. Item A: Gap-1 K_c
deferred to the authoritative `k_critical_phase_b.md`; the
closed-form criterion out of scope (framework uses `K_map=1`
exact); secondary RFE-internal computation recorded with the
`K_c=Σw` proximity flagged as conjecture, not claimed. B
Basepoint-partial; C Class-2-disposed — per the framework's own
discipline. Nothing overreached.

## Cross-links

- `k_critical_phase_b.md` — **authoritative** for the Gap-1 K_c
  resolution; this doc defers to it and only refines the RFE
  branch-birth picture.
- `k_critical_phase_a.md` — the K-zoo disambiguation;
  `K_map = 1` exact.
- `rational_field_equation.md` — the RFE self-consistency
  equation (the secondary computation).
- `mediant_vs_flow_calc.md` (`#FLOW`) — `Σw(1)=1.5617`; the
  flagged `K_c^RFE≈Σw` conjecture (not claimed).
- `inflation_seam_anchor_closure.md` / `empty_fork_cap.md` —
  Basepoint Principle: Item B's iteration-to-time anchor closes
  by the same decline.
- `sine_gordon_substrate.md` L72–85/L100–107;
  `ansatz_audit_policy.md`; `numerology_count_phase_b.md` —
  Item C's Class-2-by-construction disposition.
- `thread_chronology.md` — `#PROPOSED` restructured per this.

## One-line summary

#PROPOSED dispositioned: **A** — Gap-1 K_c closed
(`k_critical_phase_b.md`); framework uses `K_map=1` exact;
finite-`n` Fibonacci closed-form **out of scope** (known-hard
KAM); secondary RFE branch-birth first-order at `K_c^RFE≈1.56`
with `K_c=Σw` a **flagged conjecture, not claimed**. **B** —
iteration-to-time anchor Basepoint-closed (#INF); two dynamical
residuals stay open. **C** — Class-2 by construction; K=1
formula stands, K<1 not chased. Nothing overreached.
