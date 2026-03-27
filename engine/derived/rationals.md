# Q — The Rationals from the Stern-Brocot Tree

**Layer 1 derived type.** Proved from Layer 0 primitives: Z, mediant.

## Hypothesis

Every rational number is reachable by iterated mediants. The Stern-Brocot tree enumerates all of Q ∩ (0, ∞) exactly once.

## Derivation

From **Z** (the integers) + **mediant** (the combining operation):

1. **Initialize**: place `0/1` and `1/0` as boundary sentinels. These are fractions over Z.
2. **Iterate**: at each step, insert `mediant(a/b, c/d) = (a+c)/(b+d)` between every pair of adjacent fractions.
3. **Adjacency preservation** (from mediant definition): if `|ad - bc| = 1`, then the mediant is adjacent to both parents. This holds at initialization (`|0·0 - 1·1| = 1`) and is preserved at every step.
4. **Betweenness** (from mediant definition): each new fraction is strictly between its parents.
5. **Minimality** (from mediant definition): each new fraction has the smallest denominator of any fraction in its interval.

**Completeness**: for any `p/q` in lowest terms, the sequence of left/right turns in the tree corresponds to the continued fraction expansion of `p/q`. Since every finite continued fraction terminates, every rational is reached in finitely many steps.

**Uniqueness**: minimality guarantees each rational appears exactly once — if it appeared twice, one occurrence would violate the smallest-denominator property.

## Prediction

The tree enumerates all of Q ∩ (0, ∞) exactly once, ordered by denominator (depth = sum of continued fraction partial quotients).

## Test

Verify for small denominators:

| Depth | Fractions inserted |
|-------|-------------------|
| 1 | 1/1 |
| 2 | 1/2, 2/1 |
| 3 | 1/3, 2/3, 3/2, 3/1 |
| 4 | 1/4, 2/5, 3/5, 3/4, 4/3, 5/3, 5/2, 4/1 |

Every fraction `p/q` with `p + q ≤ 5` appears at the correct depth. This is provable from the definition alone (Stern 1858, Brocot 1861 — but no external reference is needed; the proof follows from the three mediant properties).

## Dependencies

- `primitives/z.md` — provides the integers for numerators and denominators
- `primitives/mediant.md` — provides the combining operation and its three properties
