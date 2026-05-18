# #PROPOSED residual: closed

> **READ FIRST.** Closes the reduced `#PROPOSED` residual. **B**
> (T2#7's two dynamical sub-residuals) closes by *derived
> collapse-dynamics* using machinery already in the framework — no
> new primitive. **C** (the K<1 K-zoo reduction) closes by
> *structural forcing*: this session's own `#TICK` Goldstein–Kac
> construction is K-parameterized, so it runs at every cascade
> K_n, discharging `sine_gordon_substrate.md`'s flagged working
> assumption. **Bright lines:** the Born rule is *preserved* under
> graded K(t) (a consistency check, not a new claim); the bare
> kink-mass ratio gets an honest `√r_n` correction (not the clean
> formula); the observable-identification stays **Class-2,
> declined, not chased** — unchanged.

## B(i) — continuous K(t) during measurement

Graded measurement coupling sweeps K(t) through the tongue
boundary, which is a **saddle-node** (`born_rule.md`,
`born_rule_parameter_free.md`: every tongue boundary is a
saddle-node, the parabola primitive). So measurement under
continuous K(t) is a **dynamic saddle-node sweep**
(Kibble–Zurek-type). Two consequences, both derived from
established results:

- **Outcome statistics are unchanged — the Born rule is
  preserved.** The branch weights are pure saddle-node geometry,
  parameter-free (`born_rule_parameter_free.md`): they do **not**
  depend on the sweep *rate* of K(t). Graded coupling does not
  spoil `|ψ|²`. (Consistency check: a graded apparatus must not
  break Born — it doesn't, because Born is geometry, not timing.)
- **Only the collapse *timing/sharpness* depends on the sweep
  rate**, via the freeze-out at the `τ ∝ 1/√ε` critical slowing
  (`measurement_collapse.md`, `parabola_csd_demo.py`): fast sweep
  → delayed/sharper freeze-out; slow sweep → adiabatic tracking.

**Closes B(i):** continuous K(t) = a dynamic-bifurcation sweep;
Born weights rate-independent, timing set by sweep-rate vs.
`τ∝1/√ε`. Derived from existing machinery, no new primitive.

## B(ii) — multi-tongue cascade vs. direct

The Stern-Brocot tree is hierarchical and tongue widths are
`w ~ (K/2)^q`, exponentially suppressed in denominator `q`
(the framework's canonical width; used in `#FLOW`, `born_rule`,
`a1_from_saddle_node`). Between any state and its final lock lie
only higher-`q` (exponentially narrower) mediant-child tongues.
Therefore collapse is **predominantly direct** — to the lowest-`q`
(widest) tongue in the basin — and cascade through intermediate
lockings is **exponentially suppressed**, `~ (K/2)^{Δq}`. The rare
cascade events are saddle-node-by-saddle-node (every boundary a
saddle-node; `#TICK` / `born_rule`).

**Closes B(ii):** direct collapse dominates; cascade is
`(K/2)^{Δq}`-rare, governed by the established tongue-width
hierarchy. Derived, no new primitive.

## C — the K<1 K-zoo reduction: structurally forced

`sine_gordon_substrate.md` L77–85 (verbatim): *"The conjecture
used here is that each such sector hosts an analogous sine-Gordon
reduction around its own mean phase ψ_n, with order parameter
r_n < 1 … This is not yet proven; it is the working assumption …
K<1 cases inherit conjectural status from this assumption."*

**This is now forced.** `tick_continuum_construction.md`'s
Goldstein–Kac construction yields

    ∂²_tΦ + 2λ∂_tΦ − c²∂²_xΦ + ω₀² sinΦ = 0,
    c² = σ²/m  (K-independent),   ω₀² = Kr/m,   β = Kr/(σ√m)

Its **only K-dependence is `ω₀² = Kr/m`** — the binary-Z₂ tick,
the force-biased flip, and `c² = σ²/m` are K-independent
structural primitives. So the construction is **K-parameterized**:
it runs *identically* at every cascade K_n, producing sine-Gordon
with `ω₀² = K_n r_n/m` around the sector mean phase ψ_n. That is
*exactly* the conjecture's "analogous sine-Gordon reduction per
sector" — now **discharged**, conditional only on each cascade
sector being a locked fixed point with order parameter r_n, which
`sine_gordon_substrate.md` itself states as the cascade
definition ("the framework treats the sector as a structural
fixed point with its own coherent sub-state").

**Upgrade:** the K<1 per-sector sine-Gordon reduction goes from
*conjectural / Class-2* to **Class-3 (structurally forced by the
K-parameterized Goldstein–Kac construction)**. The kink-mass
formula `M_k = 8σ√(Kr)` therefore holds per sector with K = K_n.

**Honest correction to the bare ratio.** Per sector
`M_k(n) = 8σ√(K_n r_n)`; at the K=1 apex `r=1`, so

    M_k(n)/M_k(1) = √(K_n r_n) = b^(−n/(2d)) · √(r_n)

via the master identity `K_n^d = b^(−n)`. The **K-scaling
`√K_n = b^(−n/(2d))` is forced (Class-3)**; the conjecture's
clean `b^(−n/(2d))` omitted the **`√(r_n)` sector-coherence
factor** (`r_n < 1`). State the forced part exactly; the `√r_n`
is the honest residual correction (same shape as the S_v
uniform-winding bound — flagged, not buried).

**What stays Class-2, declined, unchanged.** The
*observable-identification* — which observed object is a substrate
kink in each sector (geons at K=1, stellar-scale kinks in the
bowed sector, …) — has **no forcing argument** and is
**Class-2-by-construction** (`ansatz_audit_policy.md`;
`numerology_count_phase_b.md`). By the Basepoint discriminator
that absence is genuinely non-forced ⇒ it remains **correctly
declined / not chased** — *not* upgraded, *not* an open problem to
pursue. Only the *structural reduction + the K-scaling* closed;
the observable-mapping disposition is unchanged.

## Net for the #PROPOSED residual

| Piece | Disposition |
|---|---|
| B(i) continuous K(t) | **Closed** — dynamic saddle-node sweep; Born preserved (rate-independent), timing via `τ∝1/√ε`. |
| B(ii) multi-tongue | **Closed** — direct collapse dominates; cascade `(K/2)^{Δq}`-suppressed. |
| C — K<1 reduction + K-scaling | **Closed (Class-3, forced)** by K-parameterized Goldstein–Kac; ratio `= b^(−n/(2d))·√(r_n)`, the `√r_n` an honest flagged correction. |
| C — observable-identification | **Unchanged: Class-2, declined, not chased** (no forcing; Basepoint discriminator). |

The `#PROPOSED residual` is **closed**. Nothing genuinely-open
remains in the `thread_chronology.md` arc: what is left is a
*quantitative correction* (`√r_n`) and a *declined disposition*
(the observable-mapping) — neither is an open problem to chase.

## Status

Class 3 (residual closure; consistency-forced). No new primitive.
B closed by mechanism-identification from established machinery
(saddle-node Born geometry, the `τ∝1/√ε` slowing, the `(K/2)^q`
hierarchy). C's K<1 reduction closed by structural forcing —
`tick_continuum_construction.md`'s K-parameterized Goldstein–Kac
discharges `sine_gordon_substrate.md`'s working assumption; the
bare ratio carries an honest `√r_n` correction; the
observable-mapping remains correctly declined. The framework's
own internal consistency did the work.

## Cross-links

- `tick_continuum_construction.md` — the K-parameterized
  Goldstein–Kac construction; the structural forcing for C.
- `sine_gordon_substrate.md` L70–85 — the working assumption now
  discharged; `M_k = 8σ√(Kr)`.
- `born_rule_parameter_free.md` / `born_rule.md` — saddle-node
  Born geometry (rate-independent), basis for B(i).
- `measurement_collapse.md` / `parabola_csd_demo.py` — the
  `τ∝1/√ε` critical slowing; the three residuals (B).
- `mediant_vs_flow_calc.md` / `a1_from_saddle_node.md` — the
  `(K/2)^q` tongue-width hierarchy, basis for B(ii).
- `ansatz_audit_policy.md` / `numerology_count_phase_b.md` —
  why the observable-identification stays Class-2-declined.
- `proposed_items_disposition.md` — the residual this closes.
- `thread_chronology.md` — `#PROPOSED residual` → Resolved.

## One-line summary

`#PROPOSED residual` closed: **B** by derived collapse-dynamics
(continuous K(t) = dynamic saddle-node sweep, Born preserved
rate-independently, timing via `τ∝1/√ε`; multi-tongue = direct
dominates, cascade `(K/2)^{Δq}`-rare) and **C** by structural
forcing (the K-parameterized Goldstein–Kac runs at every K_n,
discharging the K<1 working assumption; ratio `= b^(−n/(2d))·√r_n`
with `√r_n` the honest flagged correction; the
observable-mapping stays Class-2-declined) — consistency-forced,
no new primitive, nothing overreached.
