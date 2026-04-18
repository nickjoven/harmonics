# Down-type double cover — Phase B attempt (halts)

## Target

Evaluate

    N_walk(T²; q_2, q_3) / N_walk(K²; q_2, q_3)  =?  q_2 q_3 = 6

using only the already-derived machinery:

- Orientable lift `T² → K²` with deck `τ(x,y) = (x+q_2, q_3−y)`
  (Phase A §3.1).
- Klein parity split: leptons / up-type = −1, down-type = +1
  (`item12_down_sign_flip.py`).
- Fiber-label group `Z_2 × Z_3 ≃ Z_6`: Z_2 shifts x-scaling,
  Z_3 shifts y-scaling; the two subgroups commute and act on
  disjoint fiber coordinates (`gauge_factorization.md` §Setup).

## Run the derivation

### Attempt 1 — deck-quotient count

Count orbits of the deck action `τ` on the fiber-label set
`Z_2 × Z_3`:

    τ · (k_1, k_2) = (k_1 + q_2 mod q_2, −k_2 mod q_3)
                   = (k_1, −k_2 mod 3)    (since q_2 = 2)

Fixed points: `k_2 = 0`, giving `(0,0), (1,0)` — two fixed.
Paired: `(0,1)↔(0,2)` and `(1,1)↔(1,2)` — two orbits of size 2.

    T² label count = |Z_2 × Z_3| = 6
    K² label count (= orbits of τ)  = 2 + 2 = 4
    ratio = 6 / 4 = 3 / 2

**Result: 3/2. Not 6.**

### Attempt 2 — sheet-count (area ratio)

The covering is 2-to-1. Area(T²) = 2·area(K²). If `N_walk` is
proportional to surface area with a fixed elementary orbit volume:

    ratio = area(T²) / area(K²) = 2

**Result: 2. Not 6.**

### Attempt 3 — gauge-center-order candidate

From Phase A §6: the independently-appearing `6 = |Z_6|` in
`hierarchy_gaussian_lattice.md` suggests the ratio should be the
gauge-center order. If `N_walk(T²)` is the full fiber count
`|Z_6| = 6` while `N_walk(K²)` is modded out by the effective
subgroup of Z_6 that acts non-trivially on the base K²:

    For Klein parity −1 (lepton/up-type), the Z_2 deck subgroup
    quotients the fiber:  N_walk(K²) = |Z_6| / |Z_2| = 3

    ratio = 6 / 3 = 2

**Result: 2. Not 6.**

### Attempt 4 — cycle-length product of the lift

The orientable lift has cycle lengths `(2q_2, q_3) = (4, 3)`.
Count distinguishable orbit-start points at unit elementary
volume:

    orbit-starts on T² = 2q_2 · q_3 = 12
    orbit-starts on K² = q_2 · q_3    = 6   (area of fundamental domain)
    ratio = 12 / 6 = 2

**Result: 2. Not 6.**

### Attempt 5 — stabilizer-size inversion

If `a_1² ∝ stabilizer_size` rather than `∝ 1/count`, the ratio
inverts. A lepton orbit's stabilizer in `Z_6` would need to be
`Z_6` itself (size 6); a down-type orbit's stabilizer would need
to be trivial (size 1). Then

    ratio = |stab(lep)| / |stab(dn)| = 6 / 1 = 6 ✓

**Result: 6. Matches — but only under the assumption that
leptons are color-singlet (Z_3-stabilized) and down-type is
color-triplet (Z_3 acts freely), which is precisely the
gauge-representation assignment the framework is trying to
derive, not an input.**

## Where the derivation halts

### Halt 1 — No candidate with topology + Klein parity alone reaches 6

Attempts 1–4 use only the orientable-lift topology and the Klein
parity assignment. They produce ratios in `{3/2, 2, 2, 2}`. None
is `q_2 q_3 = 6`. **The topological ingredients available after
Phase A are insufficient to produce the target factor.**

### Halt 2 — Attempt 5 reaches 6 but imports the conclusion

Attempt 5 reaches 6 by invoking a Z_3 stabilizer difference
between leptons and down-type quarks, which is functionally the
color-singlet vs. color-triplet distinction. In the standard
model this is an input; in the framework it is supposed to be
derived **from** the Klein bottle fiber structure. Using it as
an input for the down-type magnitude is circular.

The framework's existing gauge-factorization theorem
(`gauge_factorization.md`) derives the algebra `g = g_x ⊕ g_y`
with `Z(g_x) ⊇ Z_2`, `Z(g_y) ⊇ Z_3`, but does **not** derive
which sectors transform in which representations of `g_y`. That
assignment would close the circle and turn Attempt 5 into a
derivation. It is missing.

### Halt 3 — The up-type factor is genuinely a different mechanism

Attempts 1–5 all try to read `a_1(down)²/a_1(lep)² = 6` as some
count ratio attached to the Klein-parity class. If this works,
the up-type factor `9/4` should admit a **parallel** reading.
It does not — up-type is Klein-parity −1 (same class as leptons)
so any class-based count gives ratio 1, not 9/4. The up-type
factor comes from a Fibonacci **re-indexing of the base pair**
on the same surface K², which is a separate structural
mechanism.

Phase A §4 explicitly separated these two mechanisms. The halt
here is that **the down-type mechanism still has no independent
derivation**, while the up-type mechanism has one (Fibonacci
shift) but doesn't generalize. The framework is relying on two
unrelated structural facts to produce the `1 : 9/4 : 6` pattern,
with the second fact (down-type = 6) underivable from topology
alone.

## What this tells us about the target

The five attempts collectively suggest:

1. **The integer 6 is not a pure topological count** on the
   orientable lift. Every purely-topological count gives 2 or
   close to it (sheet count, area ratio, deck quotient).

2. **The integer 6 matches `|Z_6|`** from the gauge-center
   factorization, which already appears as the coefficient of
   `R = 6 × 13^54`. This is a strong hint that the down-type
   factor and the hierarchy coefficient share an origin.

3. **The gap is a missing representation-assignment theorem.**
   What's needed: a derivation, from the Klein bottle fiber and
   the XOR parity filter, that

   - lepton modes transform trivially under the y-direction
     `Z_3` subgroup of `Z(g)`, and
   - down-type modes transform faithfully.

   If this exists, Attempt 5 becomes a derivation, and the `6`
   is `|Z_6|` divided by the trivial stabilizer of the down-type
   orbit (1), giving 6 directly.

4. **Phase A's §6 suggestion** that the right identification is
   `ratio = |Z_6|` is consistent with Attempt 5 and inconsistent
   with Attempts 1–4. Under Phase A's own methodological
   constraint (reuse the Z_2 × Z_3 factorization rather than
   build new topology), Attempt 5 is the right shape and the
   missing piece is the representation-assignment theorem.

## Recommended next step

Phase B halts on the representation-assignment theorem. Two
routes forward:

**Route 1 — prove the assignment from XOR parity.**
The XOR filter `(q_1 + q_2) mod 2 = 1` selects denominator
classes `{(2,3), (3,2)}` (D19, `gauge_factorization.md` §Setup).
This gives four modes `{A, B, C, D}`. Work out which modes are
fixed by which subgroup of `Z_6 = Z_2 × Z_3` acting on their
fiber labels. If one of the four is `Z_3`-stabilized and the
others aren't, that mode is the color-singlet candidate. This
is a concrete finite calculation, likely one script.

**Route 2 — accept the assignment and derive something else.**
If the representation-assignment is pre-existing framework input
(e.g. from matter-sector bundle construction), then Attempt 5
is a derivation and the task is to write it up cleanly with the
representation assignment cited, not derived here. This closes
down-type at the cost of inheriting the representation claim
from elsewhere.

Route 1 is the higher-leverage path because it would close
**both** the down-type magnitude and the representation
assignment simultaneously. Route 2 is the shorter path if the
representation assignment is available.

## Cross-references

| File | Role |
|---|---|
| `down_type_double_cover_phase_a.md` | Phase A vocabulary, constraints |
| `item12_cross_sector_ratios.md` | Source conjecture |
| `item12_down_sign_flip.py` | Klein parity split |
| `gauge_factorization.md` | Z_2 × Z_3 = Z_6 fiber structure |
| `hierarchy_gaussian_lattice.md` | Independent appearance of `|Z_6| = 6` |
| `gap3_principal_bundle.py` | Four-mode set `{A, B, C, D}` candidate for Route 1 |
