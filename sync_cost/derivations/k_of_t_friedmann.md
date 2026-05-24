# K(t) and the Friedmann equation at r = 1

## Provenance of this document

This is a **forward reconstruction**, not an archival recovery.

The originally-cited source `k_of_t_friedmann.md` (commits
`aba6a83`, `505c6aa` in `continuity_in_K_nulls.md` N9) was **never
committed in any artifact** — exhaustive search of the cloud and all
local `ket` CAS stores returned nothing (`framework_status.md`,
"Survives" row 27). The explicit original derivation text is
unrecoverable and is not reproduced or guessed at here.

Instead the result is **rebuilt forward** from the surviving
canonical foundation:

- `einstein_from_kuramoto.md` — Einstein field equations as the
  unique K = 1 continuum output (Lovelock 1971).
- `adm_dictionary.md` — the forced Kuramoto↔ADM identifications
  (`r = N`, `C_ij = γ_ij`, `ω² = 4πGρ`, the Hamiltonian
  constraint coefficient `16πG`).
- `cosmological_cycle.md` — the no-twist cosmological sector and
  the de Sitter equilibrium partition.

Because every step below is a specialization of a *live canonical
dependency*, this reconstruction is sounder than the lost prose
would have been: it has no un-cited content. It reproduces exactly
the affirmed-structural claim ("Friedmann form at r = 1") and, by
carrying the derivation forward past that point, re-derives
*structurally why* the S3–S5 steps are the open N9 null —
cross-referenced to N10/N11. It does **not** override the
multiply-audited N9/N10/N11 nulls.

**Notation.** To disambiguate the two objects historically both
written `K`:

- `K`, `K_eff`, `K_c` — the Kuramoto coupling, its effective
  value, and its critical value.
- `𝒦_ij`, `𝒦 = γ^{ij}𝒦_ij` — the ADM extrinsic-curvature tensor
  and its trace (the convention of `einstein_from_kuramoto.md`,
  which already writes `𝒦ᵢⱼ`).

---

## S0 — Cosmological symmetry reduction

The cosmological sector is the **no-twist** Klein π₁ assignment
(`framework_status.md` "Klein π_1 sector assignment":
cosmological → no-twist; particle → twist; the Z₂ rep machinery
forces it via `path_closures_iter4.md`). So the Klein-bottle
`|r| ≡ 0` topological obstruction of `klein_topological_keff.py`
(a *particle*-sector, twisted phenomenon) does **not** apply to
the cosmological background — a point that matters in S2.

Impose the Cosmological Principle on the phase ensemble:
spatial homogeneity and isotropy of all ensemble statistics.

**Metric.** Isotropy forces the coherence tensor to be a
spatial scalar times the identity:

    ⟨∂_i θ ∂_j θ⟩ = ⅓⟨|∇θ|²⟩ δ_ij  ⟹  C_ij = C_0(t) δ_ij.

By the ADM dictionary `γ_ij = C_ij / C_0`, homogeneity makes the
conformal factor purely temporal. Writing it `a(t)²`,

    γ_ij = a(t)² δ_ij                       (flat slices, k = 0)

and, more generally, the unique homogeneous-isotropic 3-metric is
the maximally-symmetric one with constant spatial curvature
`³R = 6k/a²`, `k ∈ {−1,0,+1}` (Friedmann–Lemaître rigidity). N9
specifies the flat case; the curved case is carried symbolically
and costs nothing.

**Shift.** The mean phase `ψ(x,t)` is spatially uniform by
homogeneity, so the dictionary's shift `N_i/N = ∂_i ψ = 0`.
The slicing is comoving/synchronous.

**Lapse.** `N = r(t)`, spatially uniform (the order parameter is
homogeneous). The line element is therefore

    ds² = −r(t)² dt² + a(t)² δ_ij dx^i dx^j.

Define proper (cosmic) time by `dτ = r(t) dt`. In τ the metric is
the standard flat FLRW form `ds² = −dτ² + a² dx²`, **provided**
`r` is constant (so that τ is a global time and not merely a
reparametrisation that smuggles dynamics into the clock). S2
establishes exactly that.

---

## S1 — The Friedmann equation is the Hamiltonian constraint

This step assumes the S2 result `r ≡ 1` (proved next) so that
`N = 1` and coordinate time = proper time; with that, the FLRW
slicing inherits the canonical K = 1 Einstein equations of
`einstein_from_kuramoto.md` with **no new input**.

**Extrinsic curvature of the FLRW slicing.** With `N = 1`,
`N^i = 0`:

    𝒦_ij = −½ ∂_τ γ_ij = −a ȧ δ_ij,    γ^{ij} = a^{−2} δ^{ij}
    𝒦   = γ^{ij}𝒦_ij = −3 ȧ/a ≡ −3H,   H ≡ ȧ/a
    𝒦_ij 𝒦^{ij} = a^{−4}·3·(aȧ)² = 3H²,   𝒦² = 9H².

**The Hamiltonian (Gauss–Codazzi) constraint** of the canonical
K = 1 ADM system is, with the dictionary-forced coefficient
(`adm_dictionary.md` Part IV, "The coefficient 16πG = 4×(4πG)
requires ω² = 4πGρ"):

    ³R + 𝒦² − 𝒦_ij 𝒦^{ij} = 16πG ρ.

Substitute the FLRW values and `³R = 6k/a²`:

    6k/a² + 9H² − 3H² = 16πG ρ
    6k/a² + 6H²       = 16πG ρ
    ──────────────────────────────
    H² + k/a² = (8πG/3) ρ.

Adjoin the cosmological constant. By `einstein_from_kuramoto.md`
(Lovelock: the unique divergence-free rank-2 tensor is
`αG_μν + βg_μν`; with `α = 1`, `β = −Λ`), Λ enters as the uniform
background frequency of the ensemble, with the framework's
canonical value `Λ = 3(H_0/c)²` and `Λ·ℓ_P² = 3/R²`
(`framework_status.md` rows 22–23; `hierarchy_gaussian_lattice.md`).
It contributes `Λ/3` to the constraint, giving

    ┌─────────────────────────────────────────────┐
    │  H² = (8πG/3) ρ − k/a² + Λ/3   (Friedmann)   │
    └─────────────────────────────────────────────┘

and, for the flat case N9 specifies (`k = 0`),
`H² = (8πG/3)ρ + Λ/3` — **exactly the Friedmann equation**.

**Companion equations (inherited, not re-derived).**

- *Acceleration / second Friedmann.* The trace of the second ADM
  equation (the `𝒦_ij` evolution equation, `einstein_from_kuramoto.md`
  Part I, "the 𝒦ᵢⱼ evolution equation") specialised to FLRW gives
  the Raychaudhuri form `ä/a = −(4πG/3)(ρ + 3p) + Λ/3`. No new
  assumption beyond the locked-state conditions already used for
  that equation.
- *Continuity.* The contracted Bianchi identity
  `∇_μ G^{μν} = 0` is automatic from the Lovelock structure of
  `einstein_from_kuramoto.md` (the output tensor is
  divergence-free by construction), yielding
  `ρ̇ + 3H(ρ + p) = 0`.

Thus the **full Friedmann system** (constraint + acceleration +
continuity) is the FLRW specialisation of the canonical K = 1
Einstein result. S1 is closed: nothing here is new physics; it is
the dictionary plus symmetry.

---

## S2 — Why r(t) ≡ 1 (the "at r = 1" qualifier)

S1 used `N = r = 1`. This is the load-bearing structural claim,
and it is what the affirmed status line "Friedmann form **at
r = 1**" records. Two independent arguments give it; together
they are why N9 marks S1–S2 *closed at K = 1*.

**(i) Exact locking from zero background frequency dispersion.**
The dictionary fixes the oscillator natural frequency by
`ω(x) = √(4πG ρ(x))` (`adm_dictionary.md` Part IV). In the
**homogeneous background**, `ρ` is spatially uniform, so every
oscillator carries the *same* natural frequency: the frequency
distribution of the background ensemble is a delta. A Kuramoto
ensemble with identical natural frequencies synchronises
perfectly — `r = 1` *exactly*, for any `K > 0`, with no critical
threshold to clear. The background cosmology therefore sits on
the `r = 1` branch identically, not approximately. By the
dictionary `N = r`, the lapse is `N = 1`, proper time = coordinate
time, and S0's τ is a genuine global time — closing the gap S0
flagged. This is the cleanest reason the Friedmann form holds
*in standard form* rather than with a nontrivial lapse.

**(ii) Stability margin against perturbations: K_eff = 3/2 > K_c = 1.**
Argument (i) is exact only for the strictly homogeneous mean;
real perturbations introduce a small isotropic frequency
dispersion (`δω ∝ δρ`). The locked branch survives iff the
ensemble is supercritical. In the framework's normalisation the
locked-state critical coupling is `K_c = 1` (the K = 1 locking
threshold that the entire `einstein_from_kuramoto.md` construction
is built at). The homogeneous isotropic, **no-twist** sector has
effective coupling `K_eff = d/2 = 3/2` for `d = 3` spatial
oscillator directions (`einstein_from_kuramoto.md` A1 / D14:
each independent oscillator direction is a spatial direction; the
isotropic mean-field over `d` directions carries the factor `d/2`;
the Klein `K_eff = K_0/2` halving of `klein_topological_keff.py`
is a *twisted particle-sector* effect and by S0 does **not**
apply here). Since

    K_eff = 3/2  >  K_c = 1,

the locked branch is the **stable attractor**: perturbations off
`r = 1` decay, they do not grow. The margin `3/2 − 1 = 1/2 > 0`
is strict, so the closure is structural, not fine-tuned.

Arguments (i) and (ii) together: the background is exactly on
`r = 1` (delta frequency distribution), and that branch is
linearly stable (`K_eff > K_c`). Hence `r(t) ≡ 1` for the
cosmological background, the lapse is unity, and S1's Friedmann
equation holds in standard form.

**Status of S1–S2: closed at K = 1.** This is precisely the
affirmed-structural claim of `framework_status.md` row 27 and
`numerology_inventory.md` "What remains genuinely structural" #1.
It now has a written, fully-cited home; the *result's*
classification is unchanged (it was already affirmed) — only the
dangling citation is repaired, in the pattern of commit `e00628e`
("Re-point dangling canonical citations to salvaged/recorded
homes").

---

## S3 — F_locked(K) as Ω_m(K): the forward pass, and where it stops

Off the locked branch (`K < 1`, the gap/quantum sector), the
forward program is: the **locked fraction** `F_locked(K)` —
fraction of modes synchronised at cosmic coupling `K` — should
play the role of the matter density parameter `Ω_m(K)`, with the
unlocked remainder feeding Ω_Λ via the stick-slip transfer of
`cosmological_cycle.md`.

Carrying the derivation forward to this point makes the
obstruction explicit rather than asserted:

1. **K is not a running synchronization order parameter (N10).**
   `cross_parabola_audit.py` / `a1_from_saddle_node.md` show the
   r-iteration converges to the *superstable* `r = 0` fixed point
   (contraction rate exactly `q₂ = 2`); `K_STAR` sits in the
   disordered phase, not at a synchronized fixed point. So
   `F_locked` cannot be obtained by running `K` through `K_STAR`
   à la a Kuramoto `K_c`. Any `Ω_m(K)` must come from *fixed-K
   populations*, not K-running of an order parameter.

2. **The natural F_locked(K) proxy is discontinuous (N11).**
   `boundary_weight.py` (HONEST SUMMARY) shows tongue-coverage
   `w(K)` caps at `0.138` for `K < 1`, then jumps discontinuously
   to `1.0` at `K = 1` via the `min(w₆/max_w₆, 1)` clamp. It is
   non-monotone, discontinuous, and never reaches the empirical
   target at any `K < 1`. The most direct substrate proxy for
   `F_locked(K)` therefore fails structurally.

The honest forward conclusion: **S3 does not close with the
surviving primitives.** A valid `F_locked(K) → Ω_m(K)` would have
to satisfy all four clauses of the N9 acceptance criterion
(`continuity_in_K_nulls.md`, "Acceptance criterion") — in
particular, replace the N11 tongue-coverage proxy with a smooth
substrate-derived `w ∈ [0,1]` and produce `K(z)` structurally
(not by N10 iteration). No primitive in the present foundation
does this. S3 is reported as **open**, identical to the
multiply-audited N9 null — the forward pass *explains* the null,
it does not dissolve it.

---

## S4 — Horizon-crossing amplification τ_unlock(n)

S4 depends on S3: the unlock timescale `τ_unlock(n)` at horizon
crossing is defined relative to the locked fraction whose
K-dependence S3 could not pin. With S3 open, S4 is **open** by
dependency. The framework does possess the *equilibrium*
ingredients (the slip-event mechanism and the `1/φ`-gap channel
widths of `cosmological_cycle.md`), but the *rate as a function
of cosmic K* inherits the S3 obstruction. No closure is claimed.

---

## S5 — The inflation → matter → Λ era timeline

S5 has two separable parts:

- **Endpoint partition — canonical.** The de Sitter equilibrium
  `Ω_Λ : Ω_DM : Ω_b = 13 : 5 : 1 / 19` (and the two-component
  closure) is structurally derived and lives in
  `omega_partition_combinatorial.md` / `baryon_fraction.md` /
  `omega_b_alpha_beta_closure.md` (`framework_status.md` rows
  24–26). The *destination* of the timeline is fixed.
- **Timeline / duration — anchor-conditional, not closed.** The
  *rate* of traversal between eras is the S3/S4 K-running, which
  is open; and the inflation-era duration is governed by the
  inflation-seam quantity `|∇K|_inflation`, which the framework
  **correctly declines** as the Schwinger-image of an
  out-of-class anchor (#INF, `inflation_seam_anchor_closure.md`;
  a Basepoint-Principle instance, same shape as A_s/Instance-7).

So S5 is **open as a timeline** (inherits S3) while its endpoint
is canonical and its inflation segment is *structurally declined*
(a feature, not a gap, per the Basepoint Principle). No
overreach: the era *partition* is affirmed elsewhere; the era
*schedule* remains the N9 pending item.

---

## Summary

| Step | Claim | Status |
|---|---|---|
| S0 | FLRW reduction of the dictionary (no-twist sector) | closed |
| S1 | Hamiltonian constraint ⟹ Friedmann eqn (+ acceleration, continuity inherited) | **closed at K = 1** |
| S2 | `r(t) ≡ 1`: exact (δ-frequency) + stable (`K_eff=3/2 > K_c=1`) | **closed at K = 1** |
| S3 | `F_locked(K)` as `Ω_m(K)` | **open** (N10 + N11 obstruction, made explicit) |
| S4 | `τ_unlock(n)` horizon-crossing amplification | **open** (depends on S3) |
| S5 | inflation→matter→Λ schedule | endpoint canonical; **timeline open** (S3) + inflation segment structurally declined (#INF) |

S1–S2 are the affirmed-structural "Friedmann form at r = 1" and
now have a fully-cited written home. S3–S5 remain exactly the
open N9 null; the forward pass contributes a structural
*explanation* of the obstruction (it is the N10 "K is a
coordinate, not a running order parameter" plus the N11
"tongue-coverage w(K) is discontinuous" pair), which is the
honest result of rebuilding forward rather than recovering lost
prose.

---

## Cross-references

- `einstein_from_kuramoto.md` — canonical K = 1 Einstein result
  (Lovelock uniqueness); source of the constraint and the
  acceleration/continuity companions.
- `adm_dictionary.md` — `r = N`, `C_ij = γ_ij`, `ω² = 4πGρ`,
  the `16πG` Hamiltonian-constraint coefficient.
- `cosmological_cycle.md` — no-twist cosmological sector,
  stick-slip transfer, de Sitter equilibrium.
- `continuity_in_K_nulls.md` — N9 (this item), N10 (K_STAR is a
  coordinate), N11 (tongue-coverage discontinuity); the
  Acceptance criterion S3 must meet.
- `klein_topological_keff.py` — the `|r| ≡ 0` / `K_eff = K_0/2`
  effect; **particle-sector, twisted** — excluded from the
  cosmological no-twist sector by S0.
- `framework_status.md` rows 22–27 — R, Λ·ℓ_P² = 3/R²,
  Ω-partition, and the row-27 citation this document repairs.
- `numerology_inventory.md` "What remains genuinely structural"
  #1 — the affirmation S1–S2 backs.
- `inflation_seam_anchor_closure.md`, `basepoint_principle.md` —
  why the S5 inflation segment is a structural decline, not a
  gap.

## Status

**S1–S2: derived (closed at K = 1).** Forward reconstruction
from live canonical dependencies; reproduces the affirmed
"Friedmann form at r = 1" and gives the previously-dangling
`k_of_t_friedmann.md` citation a real home. Result classification
unchanged (already affirmed structural).

**S3–S5: open but dispositioned not-a-blocker** (2026-05). The
S3–S5 steps remain the multiply-audited N9 null and this document
does not override N9/N10/N11. But per the `continuity_in_K_nulls.md`
disposition, the continuity-in-K those nulls obstruct was the
*superseded* Ω_b C5 closure's dependency; **no landed result
requires it** (all Survives results are combinatorial or fixed-K;
the matter sector runs by the discrete cascade `K_n^d = b^{−n}`).
The only residual, the cosmological *era timeline*, is now settled
into three tiers (`era_timeline_disposition.md`): **ordering
structural** (forced discrete cascade between forced endpoints),
**absolute schedule anchor-declined** (out-of-class, needs `H_0`),
and the **K_eff↔epoch/energy mapping the one Class-2 residual**
(= the K↔energy-map question; structural candidate = the discrete
cascade, not promoted). So S3–S5 contributes no open *structural*
gap, and N9 is fully dispositioned — not a blocker on any landed
prediction.

## Proof chain

Cosmological specialisation of Proposition P8 (the capstone) in
[**Proof Chain A: Polynomial → General Relativity**](PROOF_A_gravity.md):
the de Sitter endpoint is the GR solution at equilibrium
(`cosmological_cycle.md`); this document is the FLRW reduction
that exhibits the Friedmann equation at the `r = 1` locked branch.
