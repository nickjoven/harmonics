# The mediant-forcing lemma — statement, proof, and explicit obligations

## Status

**Formalization of the framework's hinge claim**, previously stated
only as README prose ("the mediant is not a stipulation; it is
forced"). The claim decomposes into a **number-theoretic core** —
proven below in full (unimodular minimality; standard Farey/
Stern-Brocot theory, external mathematics) — and a **dynamical
selection claim**, decomposed here into four obligations O1–O4 of
which two are established, one is a framework-physical premise, and
one (**O3′, the tongue-prefactor uniformity bound**) is the single
genuinely open technical piece. Candidate for absorption into
`structural_lemmas.md` as Lemma 10 once O3′ is dispositioned.

This doc deliberately makes the gap structure explicit rather than
claiming closure: everything downstream of the Stern-Brocot
enumeration — the tree itself, SL(2,ℤ) and d = 3, the depth-6
counting behind Ω_Λ = 13/19 — consumes the forcedness this lemma
formalizes. If O3′ closes, the tree is forced at the stated
operating points; if it fails, the enumeration is a choice and the
framework's own discipline requires saying so.

No new primitive. Z-discipline: the mathematical core is exact
(no σ applicable); the dynamical selection is structural (Z3-type:
only structural inputs), with O3′ flagged.

## Notation

Per `structural_lemmas.md`: q_2 = 2, q_3 = 3 framework primes;
Farey neighbors a/b < c/d satisfy bc − ad = 1; the mediant is
(a+c)/(b+d). Tongue width at coupling K: w(p/q, K) = 2(K/2)^q ·
h(p/q), with h the shape prefactor determined by the rational's
continued-fraction structure (`rational_field_equation.md`).

---

## Lemma (mediant forcing)

Let a/b < c/d be adjacent locked winding numbers (Farey neighbors:
bc − ad = 1).

**(i) Minimality (number-theoretic core).** Every rational p/q with
a/b < p/q < c/d has

    q ≥ b + d,

with equality **if and only if** p/q = (a+c)/(b+d), the mediant.
The mediant is therefore the unique minimal-denominator rational
strictly between adjacent locks.

**(ii) Selection (dynamical claim).** Suppose the tongue-width law
w(p/q, K) = 2(K/2)^q h(p/q) holds on the interval, and suppose the
shape prefactor is uniformly bounded there:

    C := sup h(p/q) / inf h(p/q) < ∞   over interior rationals.

Then for all K < 2/C the mediant's tongue is **strictly the widest**
among all rationals interior to (a/b, c/d); consequently, in any
system with finite frequency resolution Δ (`fidelity_bound.md`:
Δω · T_obs ≥ 1 makes finite resolution constitutive, not optional),
the mediant is the first interior lock to become resolvable as K
increases.

**(iii) Energy-conservation reading.** The mediant is exactly the
period-weighted mean of its parents:

    (a+c)/(b+d) = [ b·(a/b) + d·(c/d) ] / (b + d),

i.e., the compromise frequency of two locked oscillators weighted
by their locking periods b, d. Betweenness (a/b < mediant < c/d)
holds identically; the framework's "energy conservation" gloss is
the statement that a new lock formed from two parents must sit at
their weighted compromise — which the mediant does with weights
forced to be the parent periods.

---

## Proof of (i) — in full

Let p/q satisfy a/b < p/q < c/d with bc − ad = 1. Both

    pb − aq ≥ 1        (from p/q > a/b, integer positivity)
    cq − dp ≥ 1        (from p/q < c/d, integer positivity)

hold. Then, using unimodularity:

    q = q(bc − ad)
      = b(cq − dp) + d(pb − aq)
      ≥ b·1 + d·1 = b + d.

For the equality case, cq − dp = 1 and pb − aq = 1 with q = b + d
give pb = a(b + d) + 1 = ab + ad + 1 = ab + bc = b(a + c), hence
p = a + c. Conversely the mediant satisfies both inner products at
exactly 1. ∎

This is standard Stern-Brocot theory (Graham–Knuth–Patashnik,
*Concrete Mathematics* §4.5; Hardy & Wright ch. III); the proof is
included so the doc is self-contained and the framework's hinge does
not rest on an external citation alone.

## Proof of (ii), given the C-bound

Any interior competitor has denominator q′ ≥ b + d + 1 by (i)
(strict, since equality is exclusive to the mediant). Then

    w(competitor) / w(mediant)
      = (K/2)^{q′ − (b+d)} · [h(comp)/h(med)]
      ≤ (K/2) · C
      < 1     whenever K < 2/C.

Strict domination of the mediant's width follows; monotonicity of
w in K then makes the mediant the first interior tongue to cross
any fixed resolution threshold Δ. ∎

Note what the finite-resolution reading repairs: in the bare circle
map every rational tongue has positive width for every K > 0, so
"the next frequency to lock" is ill-posed without a resolution
scale. The framework already carries that scale as apparatus — the
fidelity bound (`fidelity_bound.md`) — so (ii)'s formulation is
substrate-native, not an ad hoc regularization.

---

## The obligations table

| # | Obligation | Content | Status |
|---|---|---|---|
| O1 | Betweenness / energy conservation | a new lock between parents sits at their weighted compromise; mediant = period-weighted mean (part iii) | **Framework-physical premise**, standard for pairwise locking (Adler/Kuramoto compromise frequency); the *period* weighting is forced by (i) |
| O2 | Minimal denominator | mediant unique minimum in the open Farey interval | **CLOSED** — proof above, exact |
| O3 | Width law | w = 2(K/2)^q h(p/q) | **Established**: perturbative at small K; q⁻² scaling at K = 1 criticality (Jensen–Bak–Bohr; measured, see `mode_locking_exhibits.md` exhibit 2) |
| O3′ | Prefactor uniformity | C = sup h / inf h < 2 on the interval (so K ≤ 1 suffices) | **OPEN** — the single technical gap. h varies with continued-fraction structure; no corpus bound exists. Numerically checkable with existing `circle_map.py` machinery at modest depth |
| O4 | Widest ⇒ selected | first-to-resolve under finite Δ | **Established given O3′** — proof of (ii); resolution scale supplied by `fidelity_bound.md` |

**What O3′ would take:** a bound on h(p/q) across one Farey
interval — e.g., compute w(p/q, K)/(2(K/2)^q) numerically for all
p/q with q ≤ 30 inside a few representative intervals at K ∈
{0.5, 0.862, 1.0} and exhibit C empirically, then (stronger) bound
h via the continued-fraction expansion analytically. The numerical
pass is a ~50-line script in the existing style; the analytic bound
is the real formalization target.

## Why this lemma is the hinge

Downstream consumers of "the tree is forced":

- The **enumeration itself** — Stern-Brocot as *the* order of
  locking (`rational_field_equation.md` Part I).
- **SL(2,ℤ) and d = 3** — the tree's symmetry group and its
  continuum closure (`three_dimensions.md` route).
- **Depth counting** — 13 locked fractions at depth 6 behind
  Ω_Λ = 13/19 (`baryon_fraction.md`); the counting is rigid *given*
  the tree, so the tree's forcedness is where the rigidity
  bottoms out.
- The framework's **numerology discipline** — the distinction
  between forced counting (Class 5) and expression-matching
  (Class 2, declined) presumes the counting substrate is itself
  forced, which is exactly this lemma.

## Void conditions

- **O3′ fails** (C ≥ 2 at the operating K): the width ordering can
  in principle be overturned by prefactors within one mediant step;
  the "unique stable lock" reading weakens to "generic first lock,"
  and the forcing claim must be restated probabilistically or the
  operating-K domain narrowed.
- **An alternative binary operation** on Farey neighbors is
  exhibited satisfying O1 (betweenness at a physically motivated
  weighting) whose output has an equal-or-wider tongue than the
  mediant at the operating K. By (i)+(ii) this requires either
  non-integer periods or C ≥ 2; either would be informative.
- **The width law's q-exponent fails** off the circle-map class
  for the substrate's actual coupling (would surface in the
  `rational_field_equation.md` fixed-point numerics).

## Cross-links

- `structural_lemmas.md` — target catalog (Lemma 10 candidate on
  O3′ disposition)
- `rational_field_equation.md` — width law, tree domain, the
  "mediant, not division" argument this formalizes
- `fidelity_bound.md` — the resolution scale making (ii) well-posed
- `mode_locking_exhibits.md` — measured staircase universality
  (O3's empirical leg); companion doc
- `born_rule.md`, `a1_from_saddle_node.md` — saddle-node geometry
  underlying the width law
- `baryon_fraction.md`, `three_dimensions.md` — principal
  downstream consumers
- `ansatz_audit_policy.md`, `numerology_count_phase_b.md` — the
  discipline whose forced/fitted boundary this lemma underwrites

## One-line summary

The mediant is the unique minimal-denominator rational between
adjacent Farey locks (proven, unimodularity), hence — given the
tongue-width law and one open uniformity bound O3′ on the shape
prefactor (C < 2) — strictly the widest interior tongue for K < 2/C
and the first lock to resolve under the substrate's own fidelity
bound; the number-theoretic core is closed, the dynamical selection
is closed modulo O3′, and O3′ is named, bounded in scope, and
numerically checkable with existing corpus machinery.
