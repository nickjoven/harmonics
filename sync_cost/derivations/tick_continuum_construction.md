# #TICK(b): the first-order binary tick constructs sine-Gordon — Goldstein–Kac

Pressing `#TICK(b)` (`thread_chronology.md`): is the discrete
binary tick *constructively* the source of the second-order
sine-Gordon shadow, or only asserted to be
(`substrate_determinism.md`'s momentum-dissolution claim)?

**Result: constructed, not asserted.** The classical
Goldstein–Kac (GK) mechanism takes the per-tick binary Z₂
winding-sign exactly to damped sine-Gordon; conservative
sine-Gordon is the persistent (`λ→0`) limit, with the residual
`2λ ∂_tφ` being the substrate's own arrow-of-time friction
(inviolable #9) — *predicted*, not a contradiction. No noise
scale enters: the stochastic-Kramers competitor (#2) is now
**eliminated**, not merely discriminated.

## The construction

Per active site the state is `(φ, s)`, `s = ±1` the Z₂
winding-sign (the `#TICK(a)` / `born_rule_parameter_free.md`
saddle-node branch — kink vs antikink). The tick: `φ̇ = s v`;
`s` flips kink↔antikink at a rate biased by the local
sine-Gordon force (restoring orientation — climbing `(1−cos φ)`
favors reversal; this is energetically forced, not tunable):

    λ_{s→−s} = λ + ½ s β sin φ

Densities `p_±(x,t)`; `u = p_+ + p_−`, `w = p_+ − p_−`. The
**linear** part is the exact GK identity (no approximation —
the two first-order equations *imply* the second-order one):

    ∂_t u + v ∂_x w = 0
    ∂_t w + v ∂_x u = −2λ w
    ⟹  ∂²_t u + 2λ ∂_t u − v² ∂²_x u = 0      (telegrapher's, exact)

**The `∂²_t` is manufactured by eliminating the binary index.**
That *is* "context (= which Z₂ mover you are) replaces momentum"
— now a theorem-shaped statement, not a slogan. First-order
irreversible tick → second-order wave operator, no momentum
inserted.

Nonlinearity, via the mean-field moments `Φ=⟨φ⟩`, `S=⟨s⟩`
(closure `⟨sin φ⟩≈sin Φ`, exact for slowly-varying φ):

    Φ̇ = v S
    Ṡ = −2λ S − β sin Φ              (from s²=1 and the biased rate)
    ⟹ Φ̈ + 2λ Φ̇ + vβ sin Φ = 0

Add the lattice elastic coupling `½(Δ_xφ)²` (standard
discrete-Laplacian continuum limit, already in
`sine_gordon_substrate.md`) → `−c² ∂²_x Φ`:

    ∂²_t Φ + 2λ ∂_t Φ − c² ∂²_x Φ + ω₀² sin Φ = 0

with **`c² = v²`** and **`ω₀² = v β`**. This is sine-Gordon plus
a `2λ ∂_tφ` damping.

## Parameter-free check (seals the anti-#2 conclusion)

Match to `sine_gordon_substrate.md` (`c² = σ²/m`, `ω₀² = Kr/m`):

    v  = σ/√m                     (substrate signal speed)
    β  = ω₀²/v = Kr / (σ √m)      (flip-bias amplitude — DETERMINED)

`β` is fixed by the same constants `(K, r, σ, m)` as the shadow
itself. **No new parameter; no noise temperature anywhere** —
the only rate `λ` is the kink↔antikink reversal rate set by the
`(1−cos φ)` energetics, not a free `kT`. Kramers (#2) *requires*
a `kT` to set its distribution; this construction never
introduces one. Combined with `born_rule_parameter_free.md`
(topological exponent, J-forced curvature, mediant-counting
measure), the deterministic reading is now constructively
complete and the stochastic competitor is **superseded**.

The continuum (apparent "Liouville") measure *is* the
GK-coarse-grained discrete ±-counting measure: the equal base
rate `λ` is the mediant counting primitive (uniform over ±
children, pre-EML); the `sin φ` bias is the EML/energetic
reweighting. The measure is constructed, answering `#TICK(b)`'s
deepest form.

## Honest residual (do not overclaim)

1. **Damped, not bare, sine-Gordon.** The construction yields
   `+2λ ∂_tφ`. Conservative sine-Gordon (the form in
   `sine_gordon_substrate.md`) is the **persistent limit
   `λ→0`** — clean: the `∂²_t` term is `O(1)` (structural, from
   the GK elimination), the damping is `O(λ)`, the nonlinearity
   `ω₀²=vβ` is `λ`-independent, so `λ→0` gives bare sine-Gordon
   with no collateral loss. The residual `2λ ∂_tφ` is the
   substrate's **own irreversibility** (inviolable #9, the arrow)
   surfacing as a tiny friction — *predicted by* the framework,
   not in tension with it. It does not touch static results: the
   kink mass `M_k=8√(Kr)`, the mass–width invariant, and the
   `#INF` protection are `λ`-independent (set by potential +
   gradient, not dynamics). The one *quantitative* residual:
   the magnitude of `λ` at the coarse-graining scale (how nearly
   reversible the shadow is). Structural skeleton done; the
   number is open.
2. **Mean-field closure.** `⟨sin φ⟩≈sin⟨φ⟩` is the standard
   hydrodynamic closure — exact in the persistent/slowly-varying
   limit, a controlled approximation for rapidly-varying φ. The
   *linear* inertia-generation is exact (no closure); only the
   nonlinear coefficient uses the closure.

## What this closes

- **`#TICK(b)` structurally closed.** The first→second-order
  shadow is constructed (exact GK identity); the nonlinearity is
  constructed (force-biased flip, sign forced by restoring
  energetics); the measure is constructed (GK-coarse-grained
  counting). Residual is one *quantitative* parameter (`λ`
  magnitude) + the standard closure caveat — not a structural
  hole.
- **`#TICK` unifies.** `(a)` (the per-tick Z₂ sign = saddle-node
  branch, `born_rule_parameter_free.md`) and `(b)` are one
  mechanism: the GK walker's sign *is* the saddle-node branch;
  its force-biased flip coarse-grains to sine-Gordon.
- **Competitor #2 eliminated.** No `kT` is introduced anywhere;
  the shadow is deterministic-in-distribution from the binary
  tick. Discrimination (`born_rule_parameter_free.md`) becomes
  elimination.
- **`substrate_determinism.md` upgraded.** Its momentum-
  dissolution + arrow inviolable are now *jointly constructive*:
  reversibility is emergent (the `λ→0` shadow), irreversibility
  is fundamental (the tick) — exactly as posited, now derived.

## Status

Class 3 (constructive resolution + precisely-located
quantitative residual). No new primitive — GK is the classical
consequence of the existing binary-tick + force-biased-flip
structure. Closes `#TICK(b)` structurally; the residual is the
magnitude of the arrow-friction `λ`, not a mechanism gap.

## Cross-links

- `thread_chronology.md` — `#TICK`: (a) closed
  (`born_rule_parameter_free.md`), (b) closed here structurally;
  #2 eliminated; residual = `λ` magnitude.
- `born_rule_parameter_free.md` — the Z₂ sign / saddle-node
  branch that is the GK walker's `s`; same mechanism.
- `sine_gordon_substrate.md` — the target shadow; `c²=σ²/m`,
  `ω₀²=Kr/m` fix `v`, `β` with no free parameter.
- `substrate_determinism.md` — momentum-dissolution (#…) and the
  arrow (#9) now jointly constructive via GK; the `2λ∂_tφ`
  friction is the arrow surfacing.

## One-line summary

The per-tick binary Z₂ winding-sign is a Goldstein–Kac walker;
eliminating the sign *manufactures* `∂²_t` (momentum from
context, exact), a force-biased flip *manufactures* `+ω₀² sinφ`
(sign forced by restoring energetics), the lattice gives
`−c²∂²_xφ`, and `β=ω₀²/v` is fixed by substrate constants — so
the first-order irreversible tick constructively yields
sine-Gordon (conservative in the `λ→0` limit, with the residual
`2λ∂_tφ` the framework's own predicted arrow-friction), with no
noise scale: `#TICK(b)` closes and the stochastic competitor is
eliminated.
