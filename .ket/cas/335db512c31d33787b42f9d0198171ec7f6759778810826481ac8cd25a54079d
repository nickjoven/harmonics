# Path (a) walkthrough: Klein-fold sub-action of |Z_6| × ⟨z₀⟩₅₄ × ⟨ι⟩

## What this file is

A direct walkthrough of path (a) from `depth_connection_nulls.md`
— the most-recommended open path for connecting cosmological
depth 54 to EW depth ~15. The walkthrough shows that path (a) in
all three of its natural interpretations runs into a structural
obstruction: **the canonical register has prime support {2, 3},
and 15 = 3·5 cannot be reached without an external source of
the prime 5.**

This is itself a useful null, sharper than the previous nulls in
the registry. It identifies the *specific structural ingredient
missing* from the canonical register, and recasts the
hierarchy-problem direction: path (a) needs to be replaced or
augmented, not just executed.

## Setup: the canonical register precisely

Per `observer_register_closure.md` §2, the canonical register
has the structure:

    R = Z_6 × ⟨z₀⟩_{depth-54} × ⟨ι⟩

where:

- **Z_6** = Z_{q₂q₃} is the gauge center (cyclic group of order 6).
- **⟨z₀⟩_{depth-54}** is the cyclic action of multiplication by
  `z₀ = q₂ + i q₃ = 2 + 3i` on the Gaussian integers Z[i],
  truncated at depth 54 (where `54 = q₂ · q₃^d = 2 · 27` is the
  exhaustion depth at which every Z_6 cell has been visited
  exactly once).
- **⟨ι⟩** is the Z_2 antipodal involution (Klein non-orientability).

Total cardinality: |R| = 6 · 13⁵⁴ at maximal depth 54.

Group-theoretic order: |Z_6 × Z_54 × Z_2| = 648 = 2³ · 3⁴.

## The three interpretations of "sub-action"

### (a.i) Subgroup of cardinality 15

If "sub-action" means "subgroup," then by Lagrange's theorem the
subgroup must have cardinality dividing |R_group| = 648.

Divisors of 648:
`{1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 27, 36, 54, 72, 81, 108, 162, 216, 324, 648}`.

**15 is not a divisor of 648.** (648 = 2³ · 3⁴; 15 = 3 · 5; 5 ∤ 648.)

Verdict: **(a.i) fails by Lagrange**. The naive subgroup
interpretation does not produce a sub-action of cardinality 15.

### (a.ii) Stratification position (step 15 of 54)

If "sub-action" means "the structure visible at step 15 of the
54-step z₀-traversal," we need a structural distinguisher of
step 15 from steps {12, 13, 14, 16, 17, 18, …} (per the
acceptance criterion in `depth_connection_nulls.md`).

Tested distinguishers:

| Distinguisher | Step 15 value | Other steps with same value | Unique? |
|---|---|---|---|
| `k mod q_3 = 0` | 0 | {3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54} | No (18 candidates) |
| `k mod q_3 = 0 AND k mod 6 = 3` | true | {3, 9, 15, 21, 27, 33, 39, 45, 51} | No (9 candidates) |
| `k = 9 + 6` (sum of K_LEPTON + INTERACT) | true | only {15} | Suggestive — see below |
| `k = 54 − q_3·\|z_0\|² = 54 − 39` | true | only {15} | Algebraic identity — see below |
| `gcd(k, 54) = 3` (i.e., k coprime-to-18 mod 3) | gcd(15, 54) = 3 | {3, 15, 21, 33, 39, 51} | No (6 candidates) |
| Position in 13-adic expansion | 15 mod 13 = 2 = q_2 | {2, 15, 28, 41, 54} | No (5 candidates) |
| Phase angle of z₀^15 | 0.6925 π | All distinct | Yes but no framework integer |

The "sum K_LEPTON + INTERACT = 9 + 6 = 15" distinguisher is
unique but is just an *algebraic decomposition*, not a structural
operation on the register. It says "15 happens to factor as 9+6,"
not "step 15 is structurally privileged because the register's
action distinguishes it."

The "54 − 39" form similarly is just `15 = 54 − q_3·|z_0|²`,
which evaluates to 15 by arithmetic but doesn't pick step 15 out
of any group-theoretic operation on the register.

Per `observer_register_closure.md` §4 (already established null #5):

> Multiple framework-integer expressions yield 15, none forced by
> register structure.

The walkthrough confirms this: the canonical register's
stratification at step 15 is not structurally distinguished from
nearby steps.

Verdict: **(a.ii) fails for lack of distinguisher**.

### (a.iii) Composed filter (Klein-antipodal + coprime-to-6)

If "sub-action" means "the result of composing the canonical
register with the framework's existing forced filters," we already
ran this in `k_axis_uniqueness.py`:

| n (Farey level) | Klein-antipodal Z_2 orbits, coprime-to-6 |
|---|---|
| [5, 6] | 3 = q₃ |
| [7, 10] | 6 = INTERACT |
| [11, 12] | 11 |
| [13, 16] | 17 |
| [17, 18] | 25 |

The plateau sequence `{1, 3, 6, 11, 17, 25, …}` **does not contain
15**. The closest values are 11 (at n ∈ [11, 12]) and 17 (at
n ∈ [13, 16]), with no plateau passing through 15.

Verdict: **(a.iii) fails — the composed filter's plateau
sequence skips 15**.

## Why all three fail: the prime-5 obstruction

The canonical register has prime support {2, 3}: |R_group| = 2³ · 3⁴.
The composed Klein + coprime-to-6 plateau values are:

    1 = (start)
    3 = 1 + 2     (add q=5: increment (5−1)/2 = 2 = q₂)
    6 = 3 + 3     (add q=7: increment (7−1)/2 = 3 = q₃)
    11 = 6 + 5    (add q=11: increment (11−1)/2 = 5 = MEDIANT)
    17 = 11 + 6   (add q=13: increment (13−1)/2 = 6 = INTERACT)
    25 = 17 + 8   (add q=17: increment (17−1)/2 = 8 = K_QUARK)

The increment 5 = MEDIANT enters at q = 11 (the third prime
coprime to 6). It is *not* added at any earlier step. So before
reaching plateau 11, the filter's running sum has never
incorporated MEDIANT. After reaching plateau 11, the running sum
has incorporated MEDIANT once and is already past 15.

Consequently, **15 = 3·MEDIANT cannot be a plateau value** —
because MEDIANT is added in increments of 5, starting at plateau
6, jumping to 11. A sum landing on 15 would require a fractional
contribution of MEDIANT, which the integer plateau structure
doesn't allow.

This is the deepest version of the obstruction: **the
framework's natural number-theoretic machinery (Klein lattice
on Z_2 × Z_3 + coprime filters) doesn't produce 15.** The 15
appears only via algebraic combinations (3·5, 6+9, 54−39, etc.)
that are not forced by the substrate's group action.

## What this implies

The K_STAR-INTERACT alignment (PR #77) and the cosmological
Ω-partition (Survives) both land on framework integers
*reachable* by the canonical register: 6 = INTERACT for the
former, {19, 13, 5, 1} for the latter. These integers all live
in the prime support {2, 3} ∪ {prime-coprime-to-6}.

The integer 15, by contrast, requires the prime 5 to enter at a
specific multiplicative position (15 = 3 · 5), and the canonical
register does not provide this.

Three structural directions might rescue the connection:

### Direction 1: Add a Z_5 to the substrate

If the substrate carries a fifth prime as part of its structure,
the register's order extends from 648 to 648 · 5 = 3240 = 2³ ·
3⁴ · 5, and 15 becomes a divisor. But adding Z_5 is an *external
input* — there's no framework derivation of why 5 should be in
the substrate beyond "it's the smallest prime coprime to 6."

This was attempted as the **Z_30 substrate check** (commit
`2780fd6`): tested Z_30 = Z_2 × Z_3 × Z_5 with Klein quotient.
**Already null** — the Klein lattice doesn't naturally realize
Z_30. So this direction is closed.

### Direction 2: Re-derive d_EW via Farey at small q

If the EW scale lives at a Farey level that gives a count
involving 5 (e.g., F_5 has q = 5 as a denominator), the
"depth" might be encoded in Farey-level rather than
z₀-stratification.

Concretely: the Klein-antipodal orbit count at F_5 (coprime-to-6)
is 3 = q_3. Step from F_5 to F_5 ∪ {q=11} skips intermediate
values because q ∈ {7, 8, 9, 10} are not coprime to 6.

So Farey-level encoding of d_EW would give 3, 6, 11, 17 — same
plateau sequence. Same obstruction. Closed.

### Direction 3: Abandon the 15 target

If d_EW = 15 is itself the wrong target, perhaps v/M_P closure
goes through a different framework integer. The `numerology_inventory.md`
Class 2 entry for v/M_P notes alternate framework expressions
evaluating to 15. But it also rules out adjacent depths:

| Candidate d | 13^(-d) | Residual vs v/M_P |
|---|---|---|
| 14 | 2.54·10⁻¹⁶ | 12.6× too large |
| 15 | 1.954·10⁻¹⁷ | 3.1% off (the candidate) |
| 16 | 1.50·10⁻¹⁸ | 13.5× too small |

Only d = 15 is numerically viable. So Direction 3 reduces to:
"abandon the 13-adic interpretation entirely." But the framework's
hierarchy generator R = 6·13⁵⁴ is fundamentally 13-adic
(`hierarchy_gaussian_lattice.md`). Abandoning 13-adic at the EW
scale severs the structural link to the cosmological hierarchy.

## Verdict on path (a)

**Path (a) is closed in all three of its natural interpretations.**
The obstruction is structural: the canonical register's prime
support {2, 3} cannot reach 15 via subgroups, stratification
positions, or composed filters using framework-existing
machinery. Adding Z_5 (Direction 1) was already attempted and
null. Re-deriving via Farey (Direction 2) gives the same plateau
sequence. Abandoning 15 (Direction 3) severs the structural link.

This is a **stronger negative result than the previous nulls**.
Where the previous nulls said "this specific construction
doesn't work," this walkthrough says "no construction within the
canonical register's structural vocabulary can work, because the
required prime 5 is not present."

## What remains genuinely open

Two options remain after path (a) closes:

### Option 1: A Klein-fold operation outside the canonical register

The canonical register is the *one* well-formed register that
exhausts the gauge stratification. A *different* register —
non-canonical, perhaps one that overcounts or fails some closure
condition — might admit a Z_5 substructure. Constructing such a
register and showing it has framework-justified status would be
a substantive new theorem.

This would amount to *redefining* what "register" means in the
framework, making the existing canonical register a special
case. Substantive structural work; out of single-session scope.

### Option 2: v/M_P is fundamentally not register-encoded

The hierarchy v/M_P might not be a register-resolution at all.
It might be:

- A coupling-constant ratio set by RG flow from a specific UV
  fixed point — needs a derivation of the fixed point.
- An anchor that genuinely is independent of the cosmological
  anchor — accept anchor-count = 2 as final.
- Set by a different substrate primitive (e.g., the
  saddle-node parabola in `parabola.md` rather than z₀-
  stratification).

If Option 2 is correct, the framework's "two-anchor minimum"
(`anchor_count_audit.md`) is correct *in principle*, not merely
as a current shortcoming. The hierarchy problem in framework
terms is then the wrong problem to be working on.

## Recommendation

The path (a) closure suggests the framework's binding blocker is
not just operational ("we haven't done this derivation yet") but
structural ("the canonical register can't accommodate 15").
Three concrete recommendations:

1. **Stop attempting d_EW = 15 from the canonical register.** All
   three interpretations of path (a) close. Further attempts will
   replicate the prime-5 obstruction.

2. **Audit Option 1 (non-canonical register).** Specifically:
   what's the smallest deformation of the canonical register that
   admits a Z_5 substructure? Does it have any independent
   structural justification (e.g., from `mass_sector_closure.md`'s
   cross-link uniqueness theorem extended to higher primes)?

3. **Take Option 2 seriously.** If two anchors is structurally
   correct (not a defect), the framework's status updates: the
   "five obstructions" in `anchor_count_audit.md` are *not*
   obstructions to be lifted but *features* of a two-anchor
   physical theory. This is a softer landing than the
   substrate-side derivation but may be the honest one.

The prime-5 obstruction is the kind of structural finding that
either solves a problem or redefines it. Worth recording
prominently in `framework_status.md`.

## Cross-references

- `depth_connection_nulls.md` — the registry where path (a) was
  flagged as the recommended next probe; now closed
- `observer_register_closure.md` §2, §4 — canonical register
  definition and depth-15 identification null
- `hierarchy_gaussian_lattice.md` — z₀-stratification, prime
  support {2, 3} via |z₀|² = 13
- `k_axis_uniqueness.md` — composed Klein + coprime-6 plateau
  sequence
- `mass_sector_closure.md` — the cross-link uniqueness theorem
  forcing (q₂, q₃) = (2, 3)
- `anchor_count_audit.md` — the two-anchor minimum status
- `framework_status.md` — needs update flagging path (a) closure
- commit `2780fd6` — Z_30 substrate null (Direction 1
  precedent)
- commit `b8911fb` — K_STAR^14 = 1/8 demotion pattern that
  parallels this walkthrough's verdict (numerical match, no
  forcing)
