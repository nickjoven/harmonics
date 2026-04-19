# Down-type double cover — Phase A: formalization

## Scope

This document prepares the ground for a first-principles derivation
of the claim

    a_1(down)² / a_1(lep)²  =  q_2 q_3  =  6

currently stated as a conjecture in `item12_cross_sector_ratios.md`
lines 114–135. Phase A **does not derive** the claim. It fixes the
vocabulary, identifies the precise objects on each side of the
ratio, and states what Phase B will have to compute. The purpose is
to prevent the derivation from sliding between three different
senses of "mode volume," two different senses of "walk," and two
different senses of "double cover."

After Phase A the claim is restated in a form where both sides of
the equation are integrals over explicit domains, and the remaining
work in Phase B is to evaluate those integrals.

## 1. Terminology discipline

Several terms in the existing `item12_*` files carry more than one
meaning. The following names are fixed for the rest of this
program.

### Overloaded terms to retire or pin down

| Term as used elsewhere | Senses in play | Replacement in Phase A/B |
|---|---|---|
| "walk" | (a) Stern–Brocot tree traversal generating a base pair; (b) circle-map orbit at a fixed rational; (c) homotopy class of a loop on the configuration surface | **tree-walk** (a), **orbit** (b), **loop-class** (c) |
| "mode" | (a) Fourier component of a field; (b) tongue-indexed rational p/q; (c) lattice site in the Stern–Brocot tree | **tongue-label** (b) throughout this program |
| "mode volume" | (a) integration measure over tongue parameters; (b) count of distinguishable orbits contributing to a sum; (c) number of cosets under a deck action | **not used** — replaced by `N_walk` (definition 3.2 below) |
| "double cover" | (a) the orientable 2-fold `T² → K²` (topology); (b) `Spin(n) → SO(n)` (algebra); (c) `SL(2,ℂ) → SO⁺(3,1)` (Lorentz) | **orientable lift** for (a); (b) and (c) are not used in this document |
| "parity" | (a) `(−1)^(# odd denominators)` on a base pair; (b) spatial reflection symmetry; (c) fermion number mod 2 | **Klein parity** for (a) |

`item12_down_sign_flip.py` uses (a) of "parity" throughout and is
the operational definition in this program.

### A single convention for coordinates on K²

The Klein bottle is parameterized as

    K²  =  [0, q_2] × [0, q_3]  / ∼

with identifications

    (x, 0)   ∼ (x, q_3)            # y-direction periodic
    (0, y)   ∼ (q_2, q_3 − y)      # x-direction antiperiodic (the flip)

This is the presentation used implicitly in `klein_bottle_derivation.md`
with coordinate lengths set to the framework integers. The
antiperiodic direction is x (length q_2 = 2); the periodic direction
is y (length q_3 = 3). Calling `q_2` and `q_3` "cycle lengths" is
accurate once this parameterization is fixed; elsewhere they are
also used as denominator indices of a base pair, which is a
different role.

## 2. The three objects at play

The ratio `a_1(down)² / a_1(lep)²` reads an integer off three
distinct structures that must not be conflated.

### 2.1 The base pair

Each sector is labelled by a pair of rationals `(b_1, b_2)` drawn
from the Stern–Brocot tree (see `item12_cross_sector_ratios.md`
§Setup). The base pair is an input to the tree-walk procedure that
generates the generation ladder. Denominators enter here only as
integers labelling nodes:

    leptons:   (3/2, 5/3)  →  denominators (2, 3)
    up-type:   (8/5, 3/2)  →  denominators (5, 2)
    down-type: (5/4, 9/8)  →  denominators (4, 8)

These denominators are **not** the cycle lengths of K². The
coincidence "both down-type denominators are even" is an arithmetic
property of the base pair, not a topological property of the
surface.

### 2.2 The Klein-parity assignment

The Klein parity of a base pair

    π(b_1, b_2)  =  (−1)^(# odd denominators)

is derived in `item12_down_sign_flip.py` as the sign picked up when
an orbit at denominator `q` threads the antiperiodic direction `q`
times. Each crossing of the antiperiodic direction contributes a
factor `−1`; odd total count gives orientation-reversing behavior,
even count gives orientation-preserving. For a base pair with
denominators `(q_a, q_b)` the total antiperiodic-thread count is
`q_a + q_b` mod 2, which equals the number of odd denominators mod 2.

Sector assignments:

| sector | denoms | # odd | Klein parity | behavior |
|---|---|---|---|---|
| leptons   | (2,3) | 1 | −1 | orientation-reversing |
| up-type   | (5,2) | 1 | −1 | orientation-reversing |
| down-type | (4,8) | 0 | +1 | orientation-preserving |

The parity assignment is already in the codebase and is not
reworked here. Phase B inherits it.

### 2.3 The orbit whose normalization sets `a_1²`

From `a1_from_saddle_node.md`, the lepton identity

    a_1(lep)  =  1 / √w(3/2, K*)

reads `a_1` as the saddle-node relaxation time at the primary-base
Arnold tongue. The quantity being measured is the stick-duration of
an orbit at the tongue center, with `μ_center = w(p/q, K*)`. The
squared quantity `a_1²` is `1 / μ_center`, i.e. the inverse tongue
width.

For the down-type sector the same orbit-based reading must apply,
but the orbit does not close on K² with trivial normalization: it
closes only after lifting to the orientable 2-fold. Phase B must
compute the saddle-node stick-duration on the lifted surface and
compare to the K²-sheet value.

## 3. The orientable lift T² → K²

### 3.1 Explicit presentation

The orientable 2-fold cover of the Klein bottle is

    p : T²  →  K²

with `T² = [0, 2q_2] × [0, q_3] / ((x, 0) ∼ (x, q_3), (0, y) ∼ (2q_2, y))`.
The covering map is

    p(x, y)  =  (x mod q_2,  y  if  ⌊x/q_2⌋ = 0,  q_3 − y  if  ⌊x/q_2⌋ = 1)

so `p` identifies two fundamental domains of `K²` that differ by
the orientation flip. The deck group is `Z_2`; the non-trivial
deck transformation is

    τ(x, y)  =  (x + q_2,  q_3 − y)

Fixed-point-freeness of `τ` confirms the lift is a genuine cover.

The T² that appears here has fundamental domain of area `2 q_2 q_3`,
which is the Klein bottle's area doubled.

### 3.2 Walk measure `N_walk`

**Definition.** For a closed orbit of the Kuramoto self-consistent
circle map at tongue `(p/q_a, p'/q_b)`, evaluated near the
saddle-node boundary on a configuration surface `Σ`, the **walk
measure** is

    N_walk(Σ; q_a, q_b)  :=  ∫_Σ  1_{orbit(x) closes on Σ}  dx

where the indicator function is 1 if the orbit starting at `x`
returns to `x` after traversing `q_a` units of the first cycle and
`q_b` units of the second.

This is the quantity that plays the role previously called "mode
volume" in `item12_cross_sector_ratios.md`. It is integer-valued
once normalized by the elementary orbit volume `vol(x₀)`, and it
counts distinguishable orbit-starts up to the surface's own
symmetries.

`N_walk(K²; q_2, q_3)` and `N_walk(T²; q_2, q_3)` are the two
quantities Phase B must evaluate.

### 3.3 Relationship to `a_1²`

The tongue width `w(p/q, K)` at fixed `(p, q, K)` is proportional
to the measure of orbit-starts that land inside the locked region,
which in turn is proportional to `N_walk` on whichever surface the
orbit is required to close on. Explicitly, holding the
perturbative prefactor fixed,

    w_Σ(p/q, K)  ∝  w_{R²}(p/q, K)  /  N_walk(Σ; q, ·)

so that orbits required to close on a larger-`N_walk` surface have
their tongue-width density diluted by the normalization. Then

    a_1²  =  1 / w_Σ(b_1, K*)  ∝  N_walk(Σ; q_1, q_2) / (K*/2)^{q_1}

The sector ratio becomes

    a_1(down)² / a_1(lep)²
        =  [N_walk(Σ_down; 4, 8) / N_walk(Σ_lep; 2, 3)] ×
           [(K*/2)^{2 − 4} / 1] × (K*/2)^{0}     # powers to be audited in B

Phase B must fix the exponent-book-keeping. The **target** is that
the `(K*/2)^{...}` factors collapse (because the down-type base pair
denominators `(4, 8)` are not themselves the relevant exponents —
the Fibonacci-shift / double-cover re-indexing replaces them with
the `(q_2, q_3)` cycle lengths of the surface), leaving

    a_1(down)² / a_1(lep)²  =  N_walk(T²; q_2, q_3) / N_walk(K²; q_2, q_3)

which is the **Phase B target ratio**.

## 4. Reformulated claim

The conjecture, after Phase A vocabulary, reads:

> **Claim (Phase B target).** Under the walk-measure normalization
> of §3.2 and the orbit-surface assignment
>
>     leptons, up-type  →  Σ = K²        (Klein parity −1)
>     down-type         →  Σ = T²        (Klein parity +1, lift required)
>
> the ratio of walk measures at cycle lengths `(q_2, q_3) = (2, 3)`
> is
>
>     N_walk(T²; 2, 3) / N_walk(K²; 2, 3)  =  q_2 · q_3  =  6.

The up-type factor `(q_3/q_2)² = 9/4` is a separate structural
effect (Fibonacci shift of the base pair on the same surface K²)
and is **not** expressible as a ratio of walk measures. Phase A
explicitly separates these two mechanisms, which were both loosely
called "mode volume" in the earlier write-up.

## 5. Sanity checks the Phase B evaluation must satisfy

1. **Lepton case reduces.** On K², a base pair with Klein parity
   −1 and denominators `(2, 3)` must give `N_walk(K²; 2, 3)` equal
   to the reference value (call it `N_0`), so that
   `a_1(lep)² / a_1(lep)² = 1`. Whatever Phase B sets for `N_0`,
   it is the anchor.

2. **T² calculation reproduces 6·N_0 and not 2·N_0.** The orbitable
   lift is 2-to-1, so a naive sheet count gives factor 2. Phase B
   must explain why the correct factor is 6, not 2. The expected
   mechanism: the lifted orbit must thread **both** independent
   cycles of T² (lengths `2 q_2` and `q_3`) to close, while the
   K²-class orbit threads only the single sheet's fundamental
   polygon (length `q_2`, with the `q_3` direction collapsed by
   the flip). The cycle-length product `(2 q_2 · q_3) / 2 = q_2 q_3`
   is the candidate enumeration. Phase A flags this as the
   expected shape; Phase B must prove it.

3. **Agreement with `item12_K_star_closure.py` matter cells.** The
   matter-cell integer `N_dn = q_2² · q_2 q_3 = 24` in
   `cross_parabola_audit.py` lines 86–90 must equal
   `q_2² · N_walk(T²; 2, 3) / N_walk(K²; 2, 3)` from Phase B.
   This is a consistency constraint on the walk measure, not an
   independent derivation.

4. **Klein parity agreement.** Phase B's K²-versus-T² split must
   partition sectors by Klein parity exactly as
   `item12_down_sign_flip.py` does. If Phase B produces a third
   class, the derivation is wrong.

## 6. Methodological notes from previous successful pivots

The framework has closed several similar "structural match →
derived identity" gaps. The patterns worth carrying over to
Phase B:

- **sin²θ_W (commit 2ca0794).** A numerical near-match was
  promoted to a derived identity by finding the correct
  **geometric reading** of the effective exponent: `d_eff = 80/27`
  as a strip of full spatial extent occupying `1/q_3^d` of the
  frequency axis. Before the pivot, `sin²θ_W = 2^d / (2^d + 3^d)`
  had a 1.5% miss; after, it is 0.5σ. The pivot was not a new
  calculation — it was a reinterpretation of what the exponent
  **is**. The analogous move for down-type is to identify the
  exponent `q_2 q_3 = 6` not as a count but as a geometric area
  / index of a sublattice.

- **R = 6 × 13^54 (hierarchy_gaussian_lattice.md).** The factor
  `6 = q_2 q_3` appears here as `|Z_6|`, the order of the gauge
  center. This is a separate occurrence of the same integer with
  independent structural meaning. Phase B should check whether
  `N_walk(T²; 2, 3) / N_walk(K²; 2, 3) = |Z_6|` is the right
  framing — i.e. whether the lift's normalization is the
  **gauge-center order**, not a geometric volume. If so the
  down-type factor inherits the same derivation as the hierarchy
  coefficient.

- **Gauge dictionary 3 → 1 (commit 977a737).** Three separate
  identifications collapsed to one irreducible identification once
  the direct-product Lie algebra was derived from Klein bottle
  topology. The lesson: **if Phase B needs to invoke the orientable
  lift, it should reuse the already-derived Z_2 × Z_3 = Z_6 factor
  rather than building a new topological argument**. The
  K²-to-T² lift and the Z_2 × Z_3 factorization should be the
  same geometric fact expressed in covering-space vs. algebraic
  language.

- **Gap 1 theorem (gap1_theorem.md).** Conditional closure was
  accepted rather than an exact proof forced. If Phase B cannot
  evaluate `N_walk` in closed form, a **conditional result of the
  form "given the perturbative normalization of §3.2, the ratio
  is q_2 q_3 to leading order in (K*/2)"** is acceptable and
  consistent with the framework's current state of closure on
  Gap 1.

- **Gap 2 decomposition.** A monolithic proof was replaced by five
  sub-problems. If Phase B's single integral evaluation is
  intractable, the pre-registered fallback is to split `N_walk`
  into (a) a covering-sheet count (trivially 2), (b) a cycle-length
  factor (target: `q_2 q_3 / 2 = 3`), and evaluate each
  independently.

## 7. What Phase A does and does not establish

**Establishes:**

- A single disambiguated vocabulary for the program: tree-walk /
  orbit / loop-class; tongue-label; walk measure `N_walk`;
  orientable lift; Klein parity.
- An explicit presentation of the orientable lift `T² → K²` with
  its deck transformation `τ(x, y) = (x + q_2, q_3 − y)`.
- A reformulation of the conjecture as a ratio of two walk
  measures on two explicit surfaces, with cycle lengths fixed by
  the Klein-bottle parameterization (not by the base-pair
  denominators).
- Four consistency checks and three methodological constraints
  drawn from the framework's prior successful pivots.

**Does not establish:**

- Any of the three evaluations Phase B must perform: `N_walk(K²)`,
  `N_walk(T²)`, or their ratio.
- The exponent book-keeping in §3.3 (the `(K*/2)^{...}` factors
  must be audited against the perturbative expansion).
- That the Fibonacci shift for up-type and the orientable lift for
  down-type are the only two mechanisms, as opposed to two of
  many. The claim that `a_1(lep)² : a_1(up)² : a_1(down)² = 1 :
  9/4 : 6` is a complete description is an empirical fact at PDG
  precision, not a proven exhaustion.

## 8. Cross-references

| File | Role in Phase A |
|---|---|
| `item12_cross_sector_ratios.md` | Source conjecture being reformulated |
| `item12_down_sign_flip.py` | Klein parity definition, inherited |
| `a1_from_saddle_node.md` | Lepton `a_1 = 1/√w` reading, anchors §2.3 |
| `klein_bottle_derivation.md` | Klein bottle coordinates used in §1 |
| `klein_connection.md` | Connection 1-form; may feed Phase B walk-measure via holonomy |
| `gauge_factorization.md` | Z_2 × Z_3 = Z_6 structure; candidate identification for the ratio |
| `hierarchy_gaussian_lattice.md` | Independent appearance of `6 = q_2 q_3` as `|Z_6|` |
| `cross_parabola_audit.py` | Matter-cell integer `N_dn = 24`, consistency check for Phase B |
| `gap1_theorem.md` | Conditional-closure precedent |
