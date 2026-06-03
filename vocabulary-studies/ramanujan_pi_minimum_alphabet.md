# Ramanujan's 1914 1/π Series, Decomposed Against the Minimum Alphabet

## Status / classification (read first)

**Class 2 — noted structural correspondence. NOT a prediction, NOT a
derivation of π, NOT a new framework constant.** This note records a
*vocabulary alignment* between an external object (Ramanujan's 1914
series) and the framework's `minimum_alphabet.md` primitives. It does
**not** claim the substrate derives π, selects Ramanujan's constants,
or gains a scorecard entry. Retrieval-tier exploration note (unsealed;
not in `enforced_paths.txt`). Companion check:
`ramanujan_pi_decomposition.py`.

This is the framework-native answer to a hunch — "does decomposing
Ramanujan's π formula *without π* hand back the framework's minimal
vocabulary?" The honest answer has two layers, one weak and one
genuinely interesting, and the discipline is to keep them apart.

---

## The object

Ramanujan, *Modular equations and approximations to π* (1914) — the
rapidly converging series (the N = 58 singular-modulus case, proved by
J. & P. Borwein 1987):

    1/π = (2√2 / 9801) · Σ_{k≥0}  (4k)! (1103 + 26390 k)
                                  ──────────────────────────
                                     (k!)⁴ · 396^(4k)

Numerically verified (`ramanujan_pi_decomposition.py`): **12 terms
reproduce π to ~78 decimal digits.** Constant factorizations:
`9801 = 3⁴·11² = 99²`, `396 = 2²·3²·11 = 4·99`, `1103` prime,
`26390 = 2·5·7·13·29`.

---

## Layer A — decomposition into the four primitives (true, but weak)

Strip π from the right-hand side and ask what the *generators* are. Every
ingredient maps onto `minimum_alphabet.md`:

| Ingredient | Primitive |
|---|---|
| `(4k)!`, `(k!)⁴`, `396^(4k)`, `9801` | **Integers Z** (iterated +, ×, powers) |
| `1103 + 26390 k` (linear in the index k) | **Integers Z** |
| term ratio `t_{k+1}/t_k` is a *rational function of k* | **Fixed-point / iteration over Q** (the series is hypergeometric — see check) |
| the rationals being iterated over | **Mediant** (Stern–Brocot / Farey) |
| `Σ_{k→∞}` (the infinite sum) | **Completion of Q** — *not a primitive*; `minimum_alphabet.md` Part III |
| `2√2` | **Parabola** `x² − 2 = 0` (the single algebraic irrational) |
| `π` (the output) | **Completion artifact** (cf. the `2π` cycle↔radian factor on S¹) |

So the partial sums `S_n` are **exact rationals** (the check computes
them with `Fraction`, no floating point); π appears *only* in the limit,
as `(rational) · √2`. In framework terms: a **Q-valued Cauchy sequence,
completed, scaled by one parabola root.** That is almost a verbatim
instance of `minimum_alphabet.md` Part III ("the reals are the K = 1
sector… completion of Q"), with π playing the role the doc assigns it —
a completion object, not a primitive.

**Why this layer is weak.** *Almost any* closed form for a constant
decomposes into "integers + algebraic numbers + a limit." By the
framework's own standards this is the necessary-but-undistinctive kind
of match it files as numerology (cf. `numerology_inventory.md` Class
1/2). Layer A alone is **not** evidence that the formula is
framework-native. It would be a vocabulary artifact (CLAUDE.md) to stop
here and call it a result.

---

## Layer B — the structural layer (where the correspondence earns its keep)

Ramanujan's 1/π series are **not arbitrary**. They are outputs of
**modular forms / modular equations**: this one is the N = 58 case, fixed
by the singular modulus / Ramanujan g-invariant `g₅₈` of the imaginary
quadratic field `Q(√−58)`. Modular forms live on the upper half-plane
**modulo the modular group PSL(2,Z)** (and Hecke congruence subgroups
`Γ₀(N)`); the series is read off a **cusp** of the modular curve, where
the form degenerates.

The framework's primitive #2 is *defined in its own glossary* as exactly
this group:

> "**Mediant operation** — (a+c)/(b+d) on adjacent rationals; **generator
> of the PSL(2,ℤ) Farey action**" — `canonical_glossary.md` §5

and the substrate already carries the *same* modular machinery —
`PSL(2,ℤ)` Möbius action on P¹(Q), `Γ₀(N)`, **cusps of `X₀(N)`**, the
`j`-invariant (`canonical_glossary.md` §5; `psl2z_subgroup_orbits.py`;
`cross_ratio_irrep_reframe.md`), and uses `X₀(6)` cusps as its q₂×q₃
**sector taxonomy** (`canonical_glossary.md`).

So the real correspondence is **not** "√2 is a parabola." It is:

> **The engine that produces Ramanujan's π series — PSL(2,Z) acting on
> rational points / cusps of a modular curve — is the same group whose
> Farey/mediant action is the framework's primitive #2.** Both are
> reading P¹(Q) under PSL(2,Z); Ramanujan reads a cusp degeneration,
> the framework reads cusps of `X₀(N)` as its sector taxonomy.

That is a genuine, non-trivial alignment, and it is the correct
framework-native reframing of the original hunch: the formula's *origin*
(modular group on the rationals) **is** the framework's central
operation, not merely a user of its alphabet.

---

## What this does and does not show

**Does (honest, supportable):**
- Ramanujan's 1914 formula is a clean worked example of
  `minimum_alphabet.md` Part III: the continuum constant π reached as a
  **completion of a PSL(2,Z)/rational structure**, with only **one**
  algebraic irrational (√2, a parabola root) injected and *everything
  else integers*.
- The series' modular-group provenance coincides with the framework's
  definition of the mediant primitive (PSL(2,Z) Farey action). The
  vocabulary required to *state* the formula's origin is already in the
  substrate (`Γ₀(N)`, `X₀(N)` cusps, `j`-invariant).

**Does NOT (guard rails):**
- It does **not** derive π from the substrate. π remains, in the
  framework, the completion / `2π` cycle↔radian artifact
  (`minimum_alphabet.md` Part III, "The 2π identification").
- It does **not** select or predict `1103`, `26390`, `9801`, `396`, or
  the level `58`. Those are the `Q(√−58)` singular-modulus data —
  number theory, not framework physics. **No structural selector in the
  substrate picks 58.** (Contrast the framework's *own* forced quantities
  like `|F₆| = 13`.)
- It contributes **no** scorecard/MANIFEST claim and **no** new constant.

In one line: *Ramanujan's formula is a guest that happens to speak the
framework's language fluently — which is interesting because the language
is the modular group — but speaking the language is not a derivation.*

---

## Open / could-sharpen-into-a-real-question

A Layer-A match becomes a Layer-B result only with a **structural
discriminator** (the standard the substrate applies to its own N13
"multi-candidate ansatz" clusters, `continuity_in_K_nulls.md`).

**Discriminator #1 — RESOLVED, two-sided** (see
`ramanujan_pi_modular_discriminator.md`). Does the framework's own forced
modular data land on the 1914 series' data? The Ramanujan–Sato hierarchy
has two coordinates — **level** `Γ₀(ℓ)` and **discriminant** `d`. Result:
the framework reaches the **level** (it independently forces `Γ₀(6)`, a
real populated Ramanujan–Sato π-level whose divisor lattice {1,2,3,6} *is*
the q₂×q₃ cusp/sector taxonomy — upgrading Layer B from "uses PSL(2,Z)" to
"lands on a specific level by its own physics"), but reaches **no
discriminant** (the 1914 selector is `d = 58 = 2·29`; the prime 29 surfaces
only as `|F₉|`, three depths below the forced depth-6 cone — a z-fighting
artifact the substrate declines). **Home shared, address disjoint** — which
is exactly why it cannot be promoted past Class 2.

Still open:

2. Is the appearance of `√2` (vs. some other algebraic irrational) forced
   by anything substrate-side, or is it an artifact of the N = 58
   modular data? (Currently: the latter.)
3. Formalize "completion" as the limiting process on the Stern–Brocot
   tree that `minimum_alphabet.md` Status lists as **Open**; Ramanujan's
   rational Cauchy sequence `S_n → 9801/(2√2·π)` is a concrete test case
   for that formalization.
4. Forward test (from Discriminator #1): does the substrate supply a
   *discriminant* at its own level 6 — singling out one of the level-6
   families 6A–6D using only framework integers? That, not the level-2
   1914 series, is where a real promotion would come from.

---

## Check

`ramanujan_pi_decomposition.py` — exact rational arithmetic (no float
except the final √2 completion and digit check); prints the rational
term ratios (hypergeometric form), the rational partial sums, the
~78-digit agreement from 12 terms, and the ingredient→primitive ledger
above.

## References

- Ramanujan, *Modular equations and approximations to π*, Quart. J.
  Math. **45** (1914).
- J. M. & P. B. Borwein, *Pi and the AGM* (1987) — proof of the 17
  series; the N = 58 singular modulus.
- Internal: `minimum_alphabet.md` (Parts I–III), `mediant_derivation.md`,
  `canonical_glossary.md` §5, `psl2z_subgroup_orbits.py`,
  `cross_ratio_irrep_reframe.md`, `numerology_inventory.md`
  (classification).
