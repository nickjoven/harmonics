# Module 5 — History and naming

Read this after working through `README.md` and `engine.py`. You grew
the tree of all positive ratios, proved it holds every ratio once in
lowest terms, and found that the neighbor invariant b·c − a·d = 1 drives
everything. Here are the names.

## The tree — Stern–Brocot

The structure is the **Stern–Brocot tree**, introduced independently by
**Moritz Stern** (a number theorist, 1858) and **Achille Brocot** (a
clockmaker, 1860). Stern studied it for its number-theoretic
properties; Brocot built it to find gear ratios with the fewest teeth
approximating a target ratio — the same "simplest fraction in the gap"
question the tree answers. Both names are kept because both arrived at
it, from pure mathematics and from the workshop.

The **completeness and uniqueness** you verified — every positive
rational appears exactly once — is the tree's defining theorem. The
proof is exactly the invariant-preservation argument in the module: the
determinant relation holds for the seeds and is inherited by every
insertion, and from it both "nothing skipped" and "nothing repeated"
follow.

## The neighbor invariant — unimodular matrices and SL(2, ℤ)

Write each ratio a/b as a column and pair of side-by-side ratios as a
2×2 matrix:

```
    [ a  c ]
    [ b  d ]
```

The relation b·c − a·d = 1 says this matrix has **determinant** ±1 — it
is **unimodular**. The set of all such integer matrices with
determinant 1 is the group **SL(2, ℤ)**, one of the most important
groups in mathematics. Every step down the Stern–Brocot tree multiplies
by one of two fixed unimodular matrices:

```
    L = [ 1  0 ]        R = [ 1  1 ]
        [ 1  1 ]            [ 0  1 ]
```

— the "left turn" and "right turn" of the address. A ratio's L/R address
is literally the word in L and R that multiplies out to the matrix
carrying the seeds to that ratio. This is why the tree is a perfect
coordinate system: SL(2, ℤ) acts on the ratios without overlap and
without gaps, and the Stern–Brocot tree is a picture of that action.
The group SL(2, ℤ) — and its close relative PSL(2, ℤ), the modular
group — reappears throughout the framework's deeper structure; this
tree is where it first shows up, forced by nothing more than the
combining rule.

## The address — continued fractions and Euclid

The run-length reading of the address is the ratio's **continued
fraction**. Continued fractions are ancient — the algorithm that
produces them is **Euclid's algorithm** for the greatest common divisor
(c. 300 BCE), run and its quotients recorded. That the Stern–Brocot
address and the continued fraction coincide means the tree is also a
picture of Euclid's algorithm: walking down to a ratio and running
Euclid on its top and bottom are the same computation. The "standard
convention on the last term" in the demo is the familiar fact that
every rational has two continued-fraction forms ([…, n] = […, n−1, 1]);
the address picks one of them.

## The Calkin–Wilf variant

A closely related tree, the **Calkin–Wilf tree** (2000), enumerates the
same positive rationals once each by a different rule (children of a/b
are a/(a+b) and (a+b)/b) and reads them in level order to produce
**Stern's diatomic sequence**. It is worth knowing because it makes the
"each rational once" fact almost visible and connects the tree to a
single integer sequence, but the Stern–Brocot ordering is the one whose
neighbor invariant matches the mode-locking width law of Module 3, so it
is the one this curriculum uses.

## What you now have

The tree has a name (Stern–Brocot) and two discoverers; the neighbor
invariant is the determinant of a unimodular matrix, and the two turns
are the generators L, R of SL(2, ℤ); the address is a continued
fraction, which is Euclid's algorithm in disguise. Everything discrete
downstream in the framework is this tree and this group.

Module 6 draws the tree on a strip and joins the strip into a loop with
a half-twist — and finds that the same neighbor invariant that ordered
the ratios now forces a non-orientable surface. That is where the
framework's topology begins.
