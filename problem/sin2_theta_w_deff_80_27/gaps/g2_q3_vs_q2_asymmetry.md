# Gap 2: Why only q₃ correction, not q₂

## What must be proven

Derive that the leading correction to the bare duty-cycle ratio

    sin²θ_W = q₂^d / (q₂^d + q₃^d)

at K = 1, d = 3 comes exclusively from the q₃ tongue (producing
`d_eff = d − 1/q₃^d = 80/27`), with the q₂ tongue contribution
being **strictly sub-leading** at this order.

If this fails, the correct formula is

    d_eff_{both} = d − 1/q₂^d − 1/q₃^d + [cross-terms]

or some other symmetric combination. The asymmetric choice
(q₃ only) must be justified structurally.

## What is currently heuristic

`sinw_effective_dimension.md` §"Why q₃ and not q₂" argues:

> The correction comes from the q₃ tongue (not q₂) because the
> mixing angle is a RATIO of two couplings evaluated on the
> frequency interval. The q₃ tongue is the dominant occupier of
> the denominator: q₃^d = 27 > q₂^d = 8. The leading perturbative
> correction to the dimension comes from the largest tongue in
> the denominator.

Three specific claims to formalize:

1. "The dominant occupier of the denominator" is **numerically
   correct** at d = 3 (27 > 8). But the argument should be
   derivation, not size comparison: **why** does the larger tongue's
   reduction contribute at leading order and the smaller not?

2. The q₂ tongue also occupies `1/q₂^d = 1/8` of the Ω axis. A
   symmetric treatment would subtract both:

       d_eff = d − 1/q₂^d − 1/q₃^d = 3 − 1/8 − 1/27 = 181/216 off bare.

   `sin²θ_W(d_eff = 181/216 · something)` would be a different
   number; Z1 must then be re-tested.

3. Alternatively, a sector-specific argument would say the
   **numerator** of sin²θ_W (the q₂ part) does not receive a
   dimension correction because `q₂^d` is the "observed" coupling
   whose d is not reduced, while only the q₃ "denominator"
   coupling has d_eff applied. This would make the formula

       sin²θ_W = q₂^d / (q₂^d + q₃^{d_eff})

   which gives `8 / (8 + 3^{80/27}) = 8 / 34.976 = 0.2288`,
   **different** from the 0.23123 value and 1.9% off observation
   (12σ). This variant therefore fails Z1 and should be ruled out.

## Success criterion (structural)

Produce either:

- **(a) A derivation showing that only q₃ contributes at leading
  order**, with the q₂ correction quantitatively smaller and
  explicitly at higher order (e.g., by a factor of (1/q₂^d) /
  (1/q₃^d) · [some structural factor]). The systematic
  perturbative expansion should name its small parameter and show
  q₂-corrections are O(ε²) or higher while q₃-corrections are
  O(ε).

- **(b) A derivation showing that q₂ and q₃ play asymmetric
  structural roles** (numerator vs denominator of the mixing
  ratio), with a principled reason why the "numerator coupling"
  keeps d = 3 while the "denominator coupling" gets d_eff.

Path (a) is symmetric-first, asymmetry earned. Path (b) is
asymmetric-first, from the gauge-sector identification.

## Failure criterion

- A symmetric treatment (q₂ and q₃ both contributing at leading
  order) produces a different d_eff value that does NOT match
  PDG at ≤ 1σ.
- The q₂ correction at its natural order of magnitude (1/q₂^d
  = 1/8 relative to the bare d = 3, i.e., 4.2%) is comparable to
  or larger than the q₃ correction (1/27 = 3.7%), so "first
  order" doesn't uniquely select the q₃-only formula.

In both cases, the 80/27 value is not uniquely structurally
favored and the claim demotes from Class 4 to Class 2 or 1.

## Consistency check

- q₂-only correction: d_eff = 3 − 1/8 = 23/8,
  sin²θ_W = 2^{23/8} / (2^{23/8} + 3^{23/8}) = 0.2376 (2.8% off).
  This is **explicitly ruled out** in
  `sinw_effective_dimension.md` §"Why q₃ and not q₂" as "wrong
  direction and magnitude."
- q₃-only correction: d_eff = 80/27 → 0.23123 (0.5σ). ✓
- Both corrections symmetrically:
  d_eff = 3 − 1/8 − 1/27 ≈ 2.838,
  sin²θ_W = 2^{2.838} / (2^{2.838} + 3^{2.838}) ≈ 0.2322
  (~2.6σ from observation).

The three options disagree observationally. The q₃-only variant
uniquely hits 0.5σ. But this is Z1-compatibility, not Z2: Gap 2
asks why the q₃-only variant is **structurally** the right one,
not merely the observationally favored one.

## Cross-references

- `../claim.md`
- `../context/klein_bottle.md`
- `../context/gauge_sectors.md`
- `../gaps/g1_occupied_interval.md` (integral derivation may
  settle the q₂/q₃ asymmetry by computation)
- `../../../sync_cost/derivations/sinw_effective_dimension.md:106-120`
