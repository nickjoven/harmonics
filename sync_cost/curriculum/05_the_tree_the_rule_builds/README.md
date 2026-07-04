# Module 5 — The tree the rule builds

## The assertion

Run Module 4's combining rule not between 0 and 1 but between 0 and
infinity, and it grows a tree that contains every positive ratio — each
one exactly once, each already in lowest terms, no ratio ever repeated
or missed. Any two ratios sitting side by side in the tree are "as close
as two fractions can be," and the sequence of left and right turns that
reaches a ratio from the top is its unique address. The tree is a
perfect map of the ratios, and it is the map the framework's entire
discrete side is drawn on.

## Why this module exists

Module 4 built a tree and demonstrated, on a few rows, that it seemed
to produce every ratio once. "Seemed to, on a few rows" is not enough
to build a framework on. This module proves it — completeness,
uniqueness, lowest terms, and the neighbor relationship — and then
shows the payoff those proofs unlock: every ratio gets a unique address,
so the tree is not just a list of ratios but a coordinate system for
them. That coordinate system is what Modules 6 through 8 navigate.

## Growing the whole tree

Module 4 seeded the rule with 0/1 and 1/1 and got the ratios between 0
and 1. To get *all* positive ratios, seed it with 0/1 and 1/0 instead —
zero and infinity, the two extreme "locks" (never advance, and advance
without bound). Their combined fraction is (0+1)/(1+0) = 1/1, and from
there the same insertion rule fills in everything. Working with the
pair of whole numbers (top, bottom) rather than doing any division,
1/0 is a perfectly good bookkeeping symbol for infinity and never
causes trouble.

Run `python3 engine.py --demo once`. Grown to twelve levels, the tree
lays down 4095 ratios, and all three claims Module 4 left open hold
exactly:

- **lowest terms** — every ratio produced has top and bottom sharing
  no common factor; the tree never needs reducing;
- **uniqueness** — no ratio is ever produced twice;
- **completeness** — every ratio in lowest terms up to 12/12 is present.

One rule, run between zero and infinity, enumerates the positive
rationals — each exactly once, each in lowest terms — with no
arithmetic beyond adding whole numbers.

## Why it works — the neighbor invariant

The engine of all three properties is a single quantity that never
changes. Run `python3 engine.py --demo neighbors`: for every pair of
side-by-side ratios a/b and c/d anywhere in the tree, at any level,

```
    b·c − a·d  =  1,
```

checked here across all 8191 adjacent pairs down to depth twelve, with
no exception. This is exactly Module 4's "as close as two fractions can
be" condition, now shown to hold everywhere rather than in a few spots.

It holds because the mediant *preserves* it. If a/b and c/d satisfy
b·c − a·d = 1, then inserting their combined fraction (a+c)/(b+d)
between them creates two new pairs, and each new pair satisfies the same
relation — one line of arithmetic confirms it. Since the two seed
ratios 0/1 and 1/0 satisfy it (1·1 − 0·0 = 1), it is inherited by every
pair the tree ever produces. From that one invariant everything
follows: the neighbor relation forces each inserted fraction to be
already in lowest terms, forces it to be the unique simplest fraction in
its gap (so no ratio can be produced by two different insertions), and
guarantees nothing is skipped. The reason the mediant was the widest
lock in Module 3 and the simplest fraction in Module 4 is this same
determinant-1 relation, seen a third time.

## Every ratio has an address

Because each ratio sits in exactly one place, it can be *named by how
you get there*. Starting from the top and asking, at each step, "is my
target to the left or the right?" traces a unique sequence of L and R
turns down to the ratio. Run `python3 engine.py --demo path`:

| ratio | L/R address | run-lengths | continued fraction |
|-------|-------------|-------------|--------------------|
| 2/5   | LLR         | [2, 1]      | [0, 2, 2]          |
| 5/3   | RLR         | [1, 1, 1]   | [1, 1, 2]          |
| 13/19 | LRRLLLLL    | [1, 2, 5]   | [0, 1, 2, 6]       |

The run-lengths of the address — how many L's in a row, then how many
R's, and so on — are the ratio's *continued fraction* (up to the
standard convention on the last term). Address and continued fraction
are the same object. Every ratio has exactly one address; every address
names exactly one ratio. The tree is a genuine coordinate system: to
specify a rational is to specify a finite path of turns.

That last row is worth marking. The ratio 13/19 — which Module 8 will
identify as the framework's value for the dark-energy fraction Ω_Λ — is
not special-looking here; it is simply the ratio at address LRRLLLLL,
one location among all the others. When the framework later asserts
Ω_Λ = 13/19, it is naming a specific address on this tree, not fitting a
number to data. This module is where that claim becomes a claim about a
*position*.

## What this prepares for

- **Module 6** takes this tree — so far drawn on a flat strip — and
  asks what changes when the strip is joined into a loop with a
  half-twist. The neighbor invariant survives, but the global shape does
  not: the half-twist is where the framework's topology (Möbius, then
  Klein) enters, forced by the same structure built here.
- **Module 8** returns to the address idea and reads the framework's
  cosmological constants as positions on this tree — the payoff the
  13/19 row previews.

History and naming — the tree's name and the two who found it, the
matrix structure behind the neighbor invariant, and the continued-
fraction connection — is in [`history.md`](history.md). Read it once you
can state the three properties (once, lowest terms, complete) and the
neighbor invariant b·c − a·d = 1 without the names.
