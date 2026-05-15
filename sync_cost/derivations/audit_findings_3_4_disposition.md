# Audit Findings 3 & 4: honest disposition (qualification, not closure)

The external structural audit (`audit_report.md` on branch
`worktree-agent-aafbee5af7f80796d`) raised five findings on the
framework's foundational claims. Findings 1, 2, and 5 (catastrophic)
were closed by articulation — the pieces were implicit; explicit
assembly closed the gap, no new primitive.

**Findings 3 and 4 are different.** They are *major* (not
catastrophic), and unlike the catastrophic three, they do not
resolve to "the piece was implicit." They reveal genuine
**overstatements** in the framework's recent cosmological work.
The honest disposition is qualification, not defense. This doc
records what survives, what is retracted, and what is sharpened.

The framework's integrity comes from honest self-correction. The
audit found real overstatements; this doc owns them.

## Finding 3: the 4-mode reduction is dynamical, not topological

### What the audit found

The XOR constraint alone gives **1764** surviving mode pairs at
depth 6, not 4. The reduction to 4 sectors `(q₁, q₂) ∈ {(2,3),
(3,2)}` happens through `field_equation_klein.py`'s self-consistency
iteration with tongue-width-weighted populations: `tongue_width(p, q,
K_eff) ∝ (K_eff/2)^q`. Higher-q sectors are exponentially
suppressed **at sub-critical `K_eff`**. The "4 modes" emerges in
the limit where only the smallest coprime denominators survive
tongue-width truncation.

**The crux:** at `K = 1`, all tongues fill the line (the framework's
own `xor_continuum_limit.md`: "at K=1, all rationals are present —
the tree is complete"). The 4-mode reduction is *most natural at
sub-critical K* — the opposite regime from where
`nonperturbative_phase2.md` applies it (K=1).

### Honest disposition

**The Phase 2 "S_v = 16 exact" claim is qualified, not retracted.**

The framework had *two independent arguments* for K=1's structure
being finite:

1. **Tongue-width truncation** (`field_equation_klein.py`): natural
   at sub-critical K; gives 4 modes only when high-q is suppressed.
   At K=1 this argument fails (all tongues fill).

2. **Kink-fills-loop DoF reduction** (`nonperturbative_phase1.md`):
   at K=1, `L_x = ℓ_kink` so the continuum-QFT mode expansion's
   parameter is order 1; standard separation into
   zero-mode + Lochak + continuum fails; the substrate's effective
   Hilbert space collapses to the XOR-surviving sectors. This
   argument is *specific to K=1* (it relies on `L_x = ℓ_kink`,
   which holds only at K=1 in the audit's convention).

Finding 3 correctly observes that argument (1) is sub-critical-K
natural and breaks at K=1. But Phase 2's `S_v = 16` rests on
argument (2), not (1). **The two arguments are not the same; Finding
3's critique applies to (1) but Phase 2 used (2).**

**However**, the audit's deeper point stands: `nonperturbative_phase1.md`
*queued* the explicit 4×4 reduction matrix as a Phase 2 deliverable,
and `nonperturbative_phase2.md` then *assumed* the 4-mode reduction
and the energies `(0, M_k, M_k, 2 M_k)` rather than deriving the
reduction matrix from the substrate Lagrangian. The "exact" in
"`S_v = 16` exact" therefore means *exact given the assumed 4-mode
Hilbert space and assumed energies*, not *exact as a substrate-
Lagrangian-level result*.

**Qualified claim (replacing the unqualified Phase 2 claim):**

> `S_v(K=1) = 16` is exact *conditional on* the kink-fills-loop DoF
> reduction (argument 2) yielding a literally 4-dimensional Hilbert
> space with energies `(0, M_k, M_k, 2 M_k)`. The DoF reduction is
> structurally motivated (`nonperturbative_phase1.md`) but the
> explicit substrate-Lagrangian reduction matrix has *not* been
> computed. Until it is, `S_v = 16` is a leading-order result in
> the kink-fills-loop regime, not an unconditional exact value.

This is a real qualification. The "first Category-A item closed at
exact precision" framing in `nonperturbative_phase2.md` is
**downgraded to "closed at leading order in the kink-fills-loop
regime, exact pending the explicit reduction-matrix derivation."**

### What survives

- The 4-mode picture as the *dominant* substrate structure at K=1
  (argument 2 is structurally sound; the explicit matrix is the
  open piece).
- `S_v ≈ 16` at K=1 as a leading-order result.
- The qualitative result (substrate is finite-mode at K=1, not
  continuum) — argument 2 supports this independent of the
  tongue-width critique.

### What is retracted/qualified

- "S_v = 16 *exactly*" → "S_v ≈ 16 at leading order; exact pending
  the explicit reduction-matrix derivation flagged as the real
  Phase 2 deliverable."
- "First Category-A item closed at exact precision" → "closed at
  leading order; exact-precision claim conditional."

## Finding 4: S_v is K-dependent; inflation duration is not parameter-free

### What the audit found

`unitless_audit.md` line 117 gives `S_v = 16√K` — **K-dependent**.
At K = 1, `S_v = 16`. At K ≠ 1, `S_v ≠ 16`.

`inflation_duration.md` uses `S_v = 16` (the K = 1 value) at *every*
epoch, including inflation, where the framework's own cosmic-history
reading places the substrate deep on the Fibonacci ladder
(`k ≈ 144`), i.e., at `K_inflation ≠ 1`.

This is a **real inconsistency**. The headline claim "inflation
duration `≈ 10⁻³² s` from `S_v = 16` alone, parameter-free" used
the K=1 value of an explicitly K-dependent quantity at an epoch
where K ≠ 1.

The audit also noted the framework is on its *second* reading of
the same Schwinger relation, producing two incompatible
`|∇K|_inflation` values (`≈ 2` in `s_inst_inflation.md`, `≈ 3.55`
in `inflation_duration.md`), and the geometric seam form `(1−K)√K`
(max 0.385) cannot reach either.

### Honest disposition

**The inflation-duration prediction is NOT parameter-free. It is
conditional on `K_inflation`.**

With `S_v = 16√K`:

    Inflation duration ≈ exp(S_v(K_inflation)) / H_inflation
                       = exp(16 √K_inflation) / H_inflation

- If `K_inflation ≈ 1` (inflation near the lock boundary):
  `S_v ≈ 16`, inflation duration `≈ 10⁻³² s` (the headline value).
- If `K_inflation ≪ 1` (inflation deep-cascade, consistent with
  the `k ≈ 144` Fibonacci-ladder reading): `S_v ≈ 16 √K_inflation ≪
  16`, inflation duration `≪ 10⁻³² s` — potentially down to
  `≈ 1/H_inflation ≈ 10⁻³⁵ s` (just the inflation-era Hubble time).

**The framework cannot currently determine `K_inflation`
consistently** (the geometric seam form breaks down at the required
`|∇K|`; `inflation_duration.md` open #2 acknowledges this).
Therefore:

> The inflation-duration prediction `≈ 10⁻³² s` holds **only if
> inflation occurred near the K=1 lock boundary** (`K_inflation ≈
> 1`, `S_v ≈ 16`). Under the framework's own deep-cascade Fibonacci-
> ladder reading of inflation (`k ≈ 144`, `K_inflation ≪ 1`), the
> predicted inflation duration is much shorter. The "parameter-free
> from `S_v = 16` alone" advertising is **retracted**: the
> prediction is conditional on `K_inflation`, which the framework
> cannot yet pin.

### What survives

- The structural *mechanism*: inflation duration `= exp(S_v(K)) /
  H_inflation` from action-weighted sampling (`f_exit_natural.md`
  closure of Finding 5 stands — the Boltzmann form is correct;
  what's K-dependent is `S_v` inside it).
- The order-of-magnitude match `≈ 10⁻³² s` *as a conditional result*
  (conditional on `K_inflation ≈ 1`).
- The `|∇K|_seam(t)` Schwinger-inversion machinery, *with the
  caveat* that it must use `S_v(K) = 16√K`, not constant `S_v = 16`.

### What is retracted

- "Inflation duration from `S_v = 16` *alone*, parameter-free" →
  "conditional on `K_inflation`; parameter-free only if `K_inflation
  ≈ 1`."
- The internal `s_inst_inflation.md` vs `inflation_duration.md`
  inconsistency is acknowledged as a real two-reading problem, not
  a resolved supersession. `inflation_duration.md`'s claim to
  supersede is downgraded to "an alternative reading; both readings
  have unresolved `K_inflation` problems."

## The honest pattern (vs. Findings 1, 2, 5)

| Finding | Type | Disposition |
|---|---|---|
| 1 (rectangle ansatz) | articulation gap | closed (pieces implicit) |
| 2 (small primes + d) | articulation gap | closed (pieces implicit) |
| 5 (`f_exit` parsimony) | articulation gap | closed (path-integral form) |
| **3 (4-mode regime)** | **overstatement** | **qualified: "exact" → "leading order, exact pending reduction matrix"** |
| **4 (S_v epoch-dependence)** | **overstatement** | **retracted: inflation duration is conditional on K_inflation, not parameter-free** |

The catastrophic findings were the framework being *tighter than it
said*. The major findings are the framework being *looser than it
said* in two recent cosmological docs. Both honest outcomes; the
framework's value is that it can absorb either.

## Concrete next-step work this exposes

1. **The explicit 4×4 reduction matrix** (`nonperturbative_phase1.md`'s
   queued-but-not-delivered Phase 2 deliverable). Until done, `S_v =
   16` at K=1 is leading-order, not exact. This is the real Phase 2.

2. **`K_inflation` from substrate dynamics.** The framework needs a
   consistent value for the cosmic K at inflation. The geometric
   seam form `(1−K)√K` is insufficient (max 0.385 < required 3.55).
   Either a different seam structure (this is `inflation_duration.md`
   open #2) or an acknowledgment that the framework cannot predict
   inflation duration without an independent `K_inflation` input.

3. **Reconcile `s_inst_inflation.md` and `inflation_duration.md`.**
   Two readings, two `|∇K|_inflation` values, neither consistent
   with the geometric seam form. One reading should be retracted
   or both reframed as conditional.

## Status

Class 3 (disposition / honest qualification). No new framework
primitive. This doc does not close Findings 3 and 4 — it **records
their honest disposition**: Finding 3 qualifies Phase 2's exactness
claim; Finding 4 retracts the inflation-duration's parameter-free
advertising. The framework's recent cosmological claims are
correspondingly downgraded from "exact / parameter-free" to
"leading-order / conditional."

This is the audit working as intended: catastrophic findings closed
where the framework was tighter than stated; major findings honestly
qualified where the framework was looser than stated.

## Cross-links

- `audit_report.md` (branch `worktree-agent-aafbee5af7f80796d`) —
  Findings 3, 4 source.
- `nonperturbative_phase1.md` — the queued-but-undelivered explicit
  4×4 reduction matrix; the real Phase 2 deliverable.
- `nonperturbative_phase2.md` — "S_v = 16 exact" claim, now
  qualified to leading-order in the kink-fills-loop regime.
- `unitless_audit.md` — `S_v = 16√K` (K-dependent), the source of
  the Finding 4 inconsistency.
- `inflation_duration.md` — "parameter-free from S_v = 16"
  advertising, now retracted to "conditional on K_inflation."
- `s_inst_inflation.md` — the predecessor inflation calc; its
  inconsistency with `inflation_duration.md` is acknowledged, not
  resolved.
- `f_exit_natural.md` — Finding 5 closure; stands (the Boltzmann
  *form* is correct; what's K-dependent is `S_v` inside it).
- `rectangle_perpendicularity.md`, `qd_origins.md` — Findings 1, 2
  closures (the articulation-gap pattern, contrasted here with the
  overstatement pattern of 3, 4).
- `framework_status.md` — Phase 2 and inflation-duration entries
  should be downgraded per this disposition.
