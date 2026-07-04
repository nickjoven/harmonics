# Module 4 — History and naming

Read this after working through `README.md` and `engine.py`. You found
a combining rule — add the tops, add the bottoms — first in the locks
of a driven oscillator, then as pure arithmetic. Here is its name.

## The rule — the mediant

The operation

```
    a/b  ⊕  c/d  =  (a + c) / (b + d)
```

is called the **mediant** of the two fractions. The name is old and the
warning that comes with it is older: the mediant is emphatically *not*
addition of fractions (1/3 ⊕ 1/2 = 2/5, not 5/6). It is a different
operation entirely, sometimes called the "freshman sum" precisely
because it looks like the mistake a beginner makes when adding
fractions — except that here, on *neighboring* fractions, it is exactly
the right and meaningful thing. Its value always lies strictly between
its two parents, weighted toward the parent with the larger bottom
number.

The property you measured — that on as-close-as-possible neighbors the
mediant is the unique fraction of smallest denominator in the gap — is
a theorem of the **Stern–Brocot** structure (Moritz Stern, 1858;
Achille Brocot, 1860). Brocot, a clockmaker, discovered it while
working out gear ratios: to approximate a desired ratio with the fewest
teeth, you take mediants. The same rule the driven oscillator uses to
pick its widest lock is the rule a clockmaker uses to pick the simplest
gear ratio — because both are choosing the simplest fraction in an
interval.

## The sequence it generates — Farey

Listing all fractions with bottom number up to some bound, in
increasing order, gives a **Farey sequence** (John Farey, 1816, though
the key property was proved by Cauchy). Its defining feature is exactly
the mediant relationship: any two fractions that are neighbors in a
Farey sequence, a/b and c/d, satisfy bc − ad = 1, and the first
fraction to appear between them as the bound increases is their
mediant. The "as close as a pair of fractions can be" phrase in the
module is this bc − ad = 1 condition; it is what guarantees the mediant
is the unique simplest fraction in the gap.

## The tree — deferred to Module 5

The structure the `tree` demo builds — 0/1 and 1/1 at the top, every
other fraction produced once by a mediant insertion — is the
**Stern–Brocot tree**. It is deferred to Module 5, where the two claims
left open here (every rational appears; each appears exactly once) are
proved, and where the tree's neighbor and ancestor relationships are
read off. It is named here only so you know the rule you iterated has a
destination.

## Why the framework cares

The mediant is one of the framework's two universal generators (the
other, `eml`, belongs to the continuous side and appears later). The
framework's claim is that the mediant is not an arbitrary choice of
combining rule but a forced one: it is the unique operation that
respects both *betweenness* (a combined lock must lie between its
parents — a conservation condition) and *minimality* (the combined lock
must be the widest, hence simplest, available — the stability condition
from Module 3). Those are the two properties you verified in the `rule`
demo. Everything discrete downstream — the tree, the enumeration of
ratios, the integers the framework singles out — is this one forced
operation iterated.

## What you now have

A name for the rule (mediant), the structure it lists (Farey
sequences), the two people who found the tree it builds (Stern,
Brocot), and the reason the framework treats it as forced rather than
chosen. Module 5 builds the tree in full and proves what this module
only demonstrated.
