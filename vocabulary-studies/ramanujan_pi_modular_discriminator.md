# Ramanujan 1/π vs the Framework: the Modular Discriminator

## Status / classification

**Class 2 — resolved structural discriminator. Two-sided result.** This
note answers the question left open by `ramanujan_pi_minimum_alphabet.md`
§Open: *does the framework's own forced modular data ever independently
land on the data that makes a Ramanujan 1/π series special — or is the
PSL(2,Z) alignment generic?* The answer is **yes at the level coordinate,
no at the discriminant coordinate**, and the split is exactly what holds
the correspondence at Class 2. Retrieval-tier; companion check
`ramanujan_pi_modular_discriminator.py`. No scorecard/MANIFEST claim.

---

## The test, made precise

The Ramanujan–Sato hierarchy is indexed by **two** coordinates, not one:

| Coordinate | What it is | Size |
|---|---|---|
| **Level ℓ** | the congruence subgroup `Γ₀(ℓ)` the modular form lives on | small, structural (ℓ = 1,2,3,4,6,7,…,17) |
| **Discriminant d** | the singular value `τ = √(−d)` evaluated at — picks the *specific* series within a level | the "address" that fixes the constants |

A real (non-generic) correspondence requires the framework to land on the
**same datum at one of these coordinates by its own machinery** — not
because "everything uses PSL(2,Z)."

**The two sides being compared (both verified):**

- **1914 series** (Borwein–Borwein–Bailey 1989): **level 2** (`Γ₀(2)`),
  **discriminant d = 58 = 2·29**, proved via a **degree-29 modular
  equation**. The integer that makes it converge ~8 digits/term is the
  prime **29**.
- **Framework** (`psl2z_subgroup_phase_a_results.md`): forces **`Γ₀(6)`**,
  **level 6 = q₂·q₃ = INTERACT** — "the smallest Hecke subgroup whose
  level matches a framework primitive," arrived at from coupled-oscillator
  / Klein-bottle physics, *not* from any π-series target.

---

## Positive side — the LEVEL coordinate (stronger than the original Layer B)

The original note's Layer B said only "Ramanujan's series use PSL(2,Z),
and so does the mediant primitive." The discriminator sharpens this to a
**specific shared level**:

1. The framework **independently forces `Γ₀(6)`** — and `Γ₀(6)` is a
   *real, populated* Ramanujan–Sato π-level. The level-6 families exist in
   the literature: **6A** (Chan–Tanigawa–Yang–Zudilin), **6B** (Sato
   2002), **6C** (Chan–Chan–Liu 2004), **6D** (Chan–Verrill 2009).
2. The level-6 Hauptmodul is the eta quotient
   `j₆B(τ) = (η(2τ)η(3τ) / (η(τ)η(6τ)))¹²` — built from the **four
   divisors {1, 2, 3, 6} of 6**.
3. Those four divisors are **exactly** the framework's four `Γ₀(6)` cusps
   and its q₂×q₃ sector taxonomy (`psl2z_subgroup_phase_a_results.md`):

   | divisor d\|6 | Γ₀(6) cusp | framework sector |
   |---|---|---|
   | 1 | ∞ | generic |
   | 2 | 1/2 | q₂ (Klein-antipodal Z₂) |
   | 3 | 1/3 | q₃ (color triplet) |
   | 6 | 0 | INTERACT |

**Honest weight of this.** *Given* both sit at level 6, the cusp↔sector
match is forced — it is just the arithmetic of the divisors of 6. The
non-trivial, non-generic content is the antecedent: **the framework
arrives at level 6 at all, from physics**, and level 6 turns out to be a
genuine Ramanujan–Sato π-level whose modular index set is the framework's
own q₂×q₃ lattice. That is real structural contact — and note it points
**past** the user's starting point: the 1914 series is level **2**, but
the framework is "one prime richer" (it carries q₃ = 3), landing on
level **6**, not level 2.

---

## Negative side — the DISCRIMINANT coordinate (the decisive failure)

The level is the cheap coordinate; the **discriminant is what fixes an
actual formula**. Here the framework supplies nothing:

- The 1914 series is pinned by **d = 58 = 2·29** / the degree-**29**
  modular equation. The prime **29** is the selector.
- Is 29 framework-reachable? It appears **only** as `|F₉| = 29` — a Farey
  mode count at **depth 9**. The framework's forced structure lives at
  **depth 6** (`|F₆| = 13` drives Ω_Λ = 13/19; `|F₇| = 19`). 29 sits
  **three levels deeper** than anything the framework forces, and a grep
  of the substrate finds no structural role for it (nothing in
  `numerology_inventory.md`).
- So `58 = q₂ · |F₉| = 2·29` is a **deep-mediant coincidence** — precisely
  the "z-fighting / far-plane" regime `minimum_alphabet.md`'s cluster note
  defines: deep mediants the substrate's resolving power cannot promote
  without an independent structural discriminator. The framework's own
  discipline **declines** it.
- The same holds going *forward*: even at its own level 6, the framework
  supplies **no discriminant** — it does not pick *which* level-6 series
  (6A vs 6B vs 6C vs 6D, nor any `d`). It forces the curve, never the
  point on it.

---

## Verdict

> **Modular HOME shared; modular ADDRESS disjoint.**
>
> The framework reaches the **level** — and the level it reaches is
> `Γ₀(6)`, a real Ramanujan–Sato π-level whose divisor/cusp lattice is the
> framework's q₂×q₃ sector taxonomy. This is a genuine, non-generic
> positive (it upgrades the original Layer B from "uses PSL(2,Z)" to "lands
> on a specific populated level by its own physics").
>
> The framework reaches **no discriminant**. The selector for the 1914
> series is the prime 29 (a depth-9 Farey artifact the substrate declines);
> the framework forces no `d` even at its own level 6. The address layer
> has no substrate footing.

This is exactly why the correspondence stays **Class 2 and cannot be
promoted**: a derivation of π — or of Ramanujan's constants `1103, 26390,
9801, 396` — would require selecting a discriminant, and *selecting
discriminants is the one thing the framework's level-only machinery does
not do.* The discriminator returns a definite, two-sided answer rather
than an encouraging haze, which is the point.

---

## What would change the verdict (forward test, now concrete)

The cleaner test is no longer about the level-2 1914 series at all — it is
about the framework's **own** level:

1. **Does the substrate supply a discriminant at level 6?** If the
   framework's depth-6 mode structure (or the Phase-B `Γ₀(6)`-equivariance
   of `psl2z_subgroup_phase_a_results.md` §B1) independently singled out a
   *specific* `d` for one of the level-6 families 6A–6D — using only
   framework integers `{2, 3, |F_{≤7}|}` — that would be a discriminant-
   coordinate landing, i.e. a real promotion beyond Class 2.
2. **Is there a level-6 Ramanujan–Sato series whose `d` is framework-
   small** (built from `{2, 3}` and `|F_{n≤7}|`, not a foreign prime like
   29)? If yes, point (1) becomes checkable; if the only level-6
   discriminants need foreign primes, the negative side is structural, not
   incidental.

Until one of these closes, the honest statement stands: the framework and
Ramanujan share the modular *home* `Γ₀(6)`/the prime structure of 6, and
nothing at the *address* layer.

## References

- Internal: `psl2z_subgroup_phase_a_results.md` (Γ₀(6) forcing, cusp↔sector
  table), `ramanujan_pi_minimum_alphabet.md` (parent note),
  `minimum_alphabet.md` (forced depth, cluster / z-fighting note),
  `canonical_glossary.md` §5 (Farey counts, Γ₀(N), X₀(N) cusps).
- External: Ramanujan–Sato series (level structure; level-6 families
  6A–6D; `j₆B` eta quotient). Borwein, Borwein & Bailey (1989) — level-2
  proof via the degree-29 modular equation (d = 58).
- Check: `ramanujan_pi_modular_discriminator.py`.
