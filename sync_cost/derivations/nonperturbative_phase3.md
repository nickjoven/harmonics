# Non-perturbative Phase 3: K < 1 sectors and the lengthscale-regime question

Phase 3 deliverable: extend the discrete-mode calc from K = 1
(closed apex, `nonperturbative_phase2.md`) to the K < 1 cascade-
locked sectors.

The Phase 2 result `S_v(K=1) = 16 exactly` was the **mundane-
elegant** form — `M_k = 8 m_P` × 2 directions × 1 cell × 1 tick =
16 — with no precision floor because the answer is integer-counted
on lattice coordinates.

Phase 3 asks: does the same mundane elegance hold at each cascade
fixed point `K_n = b^(-n/d)`?

The honest answer requires resolving a question the K = 1 calc
sidestepped: **how do the substrate's natural lengthscales `L_x`
and `ℓ_kink` relate at general K?**

## The lengthscale regime at K < 1

At each cascade-locked K, the substrate has two natural
lengthscales:

| Scale | Definition (Planck units) |
|---|---|
| `ℓ_kink(K)` = kink width / meson Compton length | `1 / √K` |
| `L_x` = antiperiodic-loop period | (audit's commitment: `1`, K=1-specific?) |

At K = 1 these coincide (both equal 1 Planck length). At K < 1,
they diverge:

| `K` | `ℓ_kink` | `ℓ_kink / L_x` (audit) |
|---|---|---|
| K = 1 | 1.000 | 1.00 |
| K = 2^(−3/14) ≈ 0.862 (matter eq.) | 1.077 | 1.08 |
| K = 2^(−1/3) ≈ 0.794 (bowed) | 1.122 | 1.12 |
| K = 3^(−1/2) ≈ 0.577 (clarinet) | 1.316 | 1.32 |
| K = 1/2 (first mediant) | 1.414 | 1.41 |
| K = 1/3 (q₃ boundary, max seam) | 1.732 | 1.73 |

`ℓ_kink > L_x` at every K < 1. **The kink no longer fits in the
antiperiodic loop.** This is a regime the audit's `L_x = ℓ_P`
convention drove the framework into.

Either (a) the audit's `L_x = ℓ_P` is K = 1-specific and should
evolve at K < 1, or (b) the K < 1 substrate hosts only "fractional
kinks" — configurations that don't fit a full kink in the loop.

The framework hasn't committed to one. **Phase 3's first deliverable
is identifying which.**

## Two structural choices

### Choice A: `L_x = ℓ_P` constant (audit's convention extended)

Substrate's spatial cell is always one Planck length, at every K_n.
The kink width `ℓ_kink(K) = 1/√K > 1` for K < 1 means the kink
cannot fully form; the substrate hosts pinned partial-kink
configurations.

Consequence: the 4-mode-style picture at K < 1 has its diagonal
energies shifted from the audit's leading order:

    E_α(K)  ≠  M_k(K) × (unlock count)

because the kink can't form. The exact energies require an
explicit finite-volume sine-Gordon calc with boundary pinning.

This is the regime where `L_x` constrains the substrate.

### Choice B: `L_x = ℓ_kink(K)` adaptive

The antiperiodic loop scales with the kink width: at each K, the
substrate's spatial scale equals the local cascade's natural length.
This keeps the audit's K = 1 regime invariant — the kink always
fills the loop — at every K.

Consequence: the substrate's "Planck volume" is K-dependent. At
K < 1, the "fundamental cell" is larger by `1/√K`. This *would*
preserve the 4-mode-style result `S_v(K) = 16 √K` × correction.

But it conflicts with the audit's K = 1 result `R_arrow = 6 × 13⁵⁴`
which depended on `L_x = ℓ_P` at the current epoch (matter
equilibrium, K = K*). If `L_x` scales with K, then `L_x(K*) = ℓ_kink(K*)
= 1.077 ℓ_P`, and `R_arrow = H_0 × τ_tick = H_0 × L_x / c` would
shift by 8% — large enough to be observationally noticeable.

This is the regime where `ℓ_kink` constrains the substrate.

### Choice C: A composite — `L_x` is the *minimum* of the two

`L_x(K) = min(ℓ_P, ℓ_kink(K))` would set L_x = ℓ_P at K ≥ 1 (where
ℓ_kink ≤ 1) and L_x = ℓ_kink at K < 1. At K = 1 the two
choices agree.

This preserves both the K = 1 audit result and a sensible K < 1
extension. **Worth considering** as a framework reading.

## Framework-natural reading: `L_x = ℓ_P` constant (Choice A)

The substrate-Planck convention from `unitless_audit.md` and the
Klein-arithmetic `R_Planck-to-Hubble = 6 × 13⁵⁴` both point at
Choice A: the substrate's fundamental cell is one Planck length
regardless of K. Then:

- At K = 1: substrate is in the maximally-compact regime where the
  4-mode reduction applies cleanly. `S_v = 16` exactly.
- At K < 1: substrate is in a *sub-maximally-compact* regime. The
  kink can't fit in one Planck cell; the substrate hosts partial-
  kink / pinned-kink configurations.
- The mode count at K < 1 sectors is then different from 4 — it
  reflects the substrate's partial-kink configurations.

This is consistent but requires substrate-Lagrangian-level work to
pin precisely. The framework currently has the K = 1 result; K < 1
requires the explicit finite-volume calc.

## Simplest non-trivial case: K = 1/2

At K = 1/2 (first mediant from BOS):

- `M_k(K=1/2) = 8 × √(1/2) = 4√2 ≈ 5.66 m_P`
- `ℓ_kink(K=1/2) = √2 ≈ 1.414 ℓ_P`
- `L_x = 1 ℓ_P` (Choice A)
- Ratio `ℓ_kink / L_x = √2`: kink is `√2` times the loop length

The substrate at K = 1/2 with `L_x = ℓ_P` doesn't admit a full kink.
The configuration is a "compressed kink" with width forced to ≤ L_x.

For this compressed kink, the effective energy is increased
(squeezing costs energy):

    E_compressed(K=1/2)  ≈  M_k(K=1/2) × (ℓ_kink / L_x)²
                          =  4√2 × 2
                          =  8√2 ≈ 11.31 m_P

(Standard finite-size scaling for a kink pinned to a smaller box.)

Then the vortex-pair process A → D → A (assuming the 4-mode
structure persists with modified energies) gives:

    S_v(K=1/2) ≈ 2 × E_compressed × τ_loop = 16√2 ≈ 22.6 in Planck units

Compare to the audit's LO formula `S_v(K) = 16√K = 16/√2 = 8√2 ≈ 11.3`.

The two **differ by a factor of 2**. The audit's LO doesn't capture
the compression cost at K < 1.

**This is the first quantitative finding of Phase 3:** the audit's
LO `S_v = 16√K` is K = 1-specific; at K < 1, the compressed-kink
correction roughly doubles the value.

Whether this changes the framework's predictions depends on which
predictions use `S_v(K < 1)`. The breather-tower formula
`N_max = ⌊8π / β̃²⌋ = ⌊8π√K⌋` still depends on the audit's β̃²
form; whether the compression also adjusts β̃² requires explicit
finite-volume sine-Gordon results.

## What this tells us

Three substantive Phase 3 findings:

1. **The audit's `L_x = ℓ_P` is K = 1-specific.** At K < 1, the
   substrate is in a different lengthscale regime; the audit's
   formulas need finite-volume correction.

2. **The mundane elegance of K = 1 doesn't generalise mechanically.**
   `S_v = 16` exactly is K = 1 because the kink fits the loop
   exactly. At K < 1, the kink can't fit; the configuration is
   compressed; the action is modified.

3. **Cascade-sector observables computed from `M_k(K)` need
   re-derivation under Choice A.** The audit's LO formulas
   (`M_k = 8√K`, `β̃² = 1/√K`, `T_sat = 8√K T_P`, `R_wheel = 1/√K`)
   are correct as LO substrate energies but don't include the
   compression contribution to dynamical quantities like `S_v`.

## Open: which choice is correct?

The Phase 3 audit-extension question requires committing to one of
Choices A, B, or C. Each has consequences:

| Choice | Consistent with K=1 audit | Consistent with epoch evolution | Mode count at K<1 |
|---|---|---|---|
| **A: L_x = ℓ_P constant** | Yes | Requires `\|∇K\|_seam(t)` evolution | Different from 4; compression-modified |
| **B: L_x = ℓ_kink(K)** | At K=1 only | Conflicts with `R_arrow` at K* by ~8% | Same 4-mode pattern; energies scale |
| **C: L_x = min(ℓ_P, ℓ_kink)** | Yes (since ℓ_kink ≥ ℓ_P at K ≤ 1) | Needs careful epoch derivation | Composite |

Choice A is most consistent with the audit's K = 1 results but
predicts substantial K < 1 modifications to substrate dynamics.
Choice B preserves the 4-mode structural pattern but requires
recalibrating the audit's R_arrow match. Choice C is the
parsimonious compromise.

**The framework should commit to one before completing Phase 3.**
This is the natural next-step structural question.

## Status

Class 3 (setup and structural question). The Phase 3 calc was
attempted and revealed that the substrate's lengthscale regime at
K < 1 is a separate structural question the audit didn't address.
Both the audit (K = 1-specific) and the seam-profile derivation
(continuum) were partial answers that don't extend mechanically to
K < 1.

The framework's Phase 3 result is therefore a **regime-clarifying
finding**, not a per-sector exact-precision value. Completing the
exact-precision Phase 3 (analog of Phase 2 at K < 1) requires
first committing to the L_x choice.

## Cross-links

- `nonperturbative_phase1.md`, `nonperturbative_phase2.md` — the
  K = 1 calc this doc extends.
- `unitless_audit.md` — the L_x = ℓ_P convention; this doc shows
  it is K = 1-specific.
- `master_cascade_identity.md` — supplies the cascade fixed
  points K_n.
- `soliton_dynamics.md` — kink-width formula `ℓ_kink(K) = 1/√K`
  used to identify the regime.
- `seam_profile.md` — continuum-style optimisation that overshoots
  at K = 1; at K < 1 may give different result.
- `framework_status.md` — Category-A items: K < 1 sectors and
  the L_x-choice question now both registered as open.

## What I'd recommend next

The framework's natural sequence:

1. **Commit to one of Choices A, B, C** for L_x at K < 1. This is
   a parsimony/structural decision, not a calc.
2. **Redo the Phase 2-style 4-mode calc at K = 1/2** under the
   chosen L_x.
3. **Generalise to other cascade fixed points** systematically.
4. **Cross-check with the `|∇K|_seam(t)` epoch-dynamics question**
   to ensure the L_x choice is consistent with observed H(t).

The mundane-elegance test for Phase 3: if Choice A is right, the
K < 1 calcs will involve compression factors that may or may not
be lattice-integers. If they are integers, the framework continues
its exact-precision pattern. If they aren't, the K < 1 sectors are
the framework's first non-trivial-precision territory.
