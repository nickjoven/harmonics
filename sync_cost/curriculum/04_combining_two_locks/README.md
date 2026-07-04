# Module 4 — Combining two locks

## The assertion

Given two neighboring locks a driven oscillator already has — say 1/3
and 1/2 — the next lock to appear between them, the widest one in the
gap, sits at the fraction you get by adding the tops and adding the
bottoms: (1+1)/(3+2) = 2/5. This combining rule is discovered from the
dynamics, then recognized as pure arithmetic. Iterated from the two
coarsest locks, it produces every whole-number ratio, each exactly
once, in the precise order their locks emerge.

## Why this module exists

Module 3 left a map full of wedges, ordered by simplicity but not yet
*organized*: no rule said where the next wedge would fall. This module
supplies the rule, and it is almost absurdly simple — add across, top
and bottom. Everything discrete in the rest of the framework, every
tree and every enumeration, is this one rule iterated. It deserves to
be met the way the framework's integers were met: found in the
behavior of coupled waves, not written down as a definition.

## Finding the rule in the dynamics

Take the driven oscillator from Module 3 and two of its neighboring
locks — 1/3 and 1/2. Between them, at weaker coupling, other locks
appear. Which is widest — which is the sturdiest lock in the gap, the
one that emerges first as the coupling grows?

Run `python3 engine.py --demo between`. For the gap between 1/3 and
1/2 it measures the lock width at the candidate 2/5 and at two other
fractions in the same gap (3/7 and 3/8, both with larger bottom
numbers):

| fraction | bottom | lock width |
|----------|--------|-----------|
| **2/5**  | 5      | **0.0104** |
| 3/7      | 7      | 0.0052    |
| 3/8      | 8      | 0.0044    |

The widest lock in the gap is 2/5 — and 2/5 is exactly (1+1)/(3+2),
the two parent fractions added across. The same holds for every gap
tested: between 1/2 and 2/3 the widest lock is 3/5 = (1+2)/(2+3);
between 1/4 and 1/3 it is 2/7 = (1+1)/(4+3). The oscillator picks out
the added-across fraction on its own. Nothing put it there; it is the
simplest ratio available in the gap, and by Module 3's width law the
simplest ratio holds the widest lock.

## The rule as arithmetic

Once seen, the rule needs no oscillator. Take any two fractions a/b and
c/d and form (a+c)/(b+d). Run `python3 engine.py --demo rule`: for
neighboring parents the combined fraction always lands strictly
between them, and — for parents that are as close as two fractions can
get — it is the *unique fraction with the smallest bottom number*
anywhere in the gap:

| left | right | combined | between? | smallest-bottom in gap? |
|------|-------|----------|----------|-------------------------|
| 0/1  | 1/1   | 1/2      | yes      | yes (1/2)               |
| 1/3  | 1/2   | 2/5      | yes      | yes (2/5)               |
| 1/2  | 2/3   | 3/5      | yes      | yes (3/5)               |
| 2/5  | 1/2   | 3/7      | yes      | yes (3/7)               |

Two facts, both exact. The combined fraction is *between* its parents:
a value partway between a/b and c/d, weighted by their bottom numbers.
And it is the *simplest* thing between them: no fraction with a smaller
bottom number fits in the gap at all. Simplicity and betweenness are
the two properties Module 3 said a lock needs to be the widest — so the
arithmetic rule and the dynamical "widest lock" are the same object,
reached two ways.

## Iterating the rule

Start with the two coarsest locks a driven oscillator has: 0/1 (never
advances) and 1/1 (advances once per beat). Between them, insert the
combined fraction 1/2. Now there are two gaps; insert the combined
fraction into each — 1/3 and 2/3. Keep going. Run `python3 engine.py
--demo tree`:

```
  row 0:  0/1                 1/1
  row 1:        1/2
  row 2:    1/3        2/3
  row 3:  1/4   2/5   3/5   3/4
  row 4: 1/5 2/7 3/8 3/7 4/7 5/8 5/7 4/5
```

Each row inserts, between every adjacent pair, exactly one new fraction
— their combined value. No fraction is ever produced twice. Every
whole-number ratio, however complicated, appears at some finite depth.
One combining rule, iterated, enumerates *all* the ratios — and it does
so in the order their locks emerge as coupling weakens: the simplest
first (widest lock, shallowest in the tree), the complicated ones later
(narrow locks, deep in the tree). The map of wedges from Module 3 has
become a fully ordered structure, generated from two seeds and one
rule.

## What this prepares for

- **Module 5** gives this tree its name, proves the two claims left
  standing here — that every ratio appears, and that each appears
  exactly once — and reads off the neighbor relationships (which
  fractions are as-close-as-possible, and why the combined-fraction
  bottom number is exactly the sum). It is the tree the framework's
  discrete structure lives in.
- The combining rule is also the doorway to the framework's *topology*:
  iterating it on a strip that is later given a half-twist is where the
  Möbius and Klein surfaces come from (Module 6).

History and naming — the rule's name, the two mathematicians it is
named for, and the older sequence it generates — is in
[`history.md`](history.md). Read it once you can state the rule, its
betweenness, and its smallest-bottom-number property without the name.
