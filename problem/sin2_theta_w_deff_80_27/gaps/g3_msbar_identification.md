# Gap 3: Scheme identification — framework root ↔ MS-bar at M_Z

## What must be proven

Show that the framework's root-level formula

    sin²θ_W (root) = q₂^{d_eff} / (q₂^{d_eff} + q₃^{d_eff})

with `d_eff = 80/27` corresponds to the **MS-bar** renormalization
scheme evaluated at `μ = M_Z`, and not to any other scheme/scale
combination (on-shell, effective Z-pole, low-Q², ...).

## What is currently heuristic

`sinw_effective_dimension.md` §"Scale identification: why M_Z"
argues:

> The formula is evaluated at the ROOT (1/1) of the Stern-Brocot
> tree. In the framework, the root is the scale where the q₂
> and q₃ sectors first branch — the point where the two gauge
> couplings are simultaneously defined. This is the electroweak
> symmetry breaking scale by construction.
>
> The MS-bar scheme at M_Z is the perturbative coupling definition
> at the Z pole, which is the scale where the electroweak mixing
> is measured. The framework's root-level formula corresponds to
> this scheme because:
> 1. The root is where mixing is DEFINED (the branching point).
> 2. The correction is perturbative (first-order in 1/q₃^d).
> 3. MS-bar is the natural perturbative scheme in the SM.

Three specific claims to formalize:

1. **"The root is the electroweak symmetry-breaking scale by
   construction"** — asserted but not derived. What in the
   framework's construction identifies the 1/1 root with v_EW /
   M_Z? If the root is the same for all processes, why does the
   mixing angle at root correspond specifically to MS-bar at M_Z
   rather than, say, on-shell at M_W or the low-Q² value?

2. **"The correction is perturbative"** — granted that `1/q₃^d
   = 1/27` is a small number, this only tells us the d_eff
   *correction* is perturbative. It doesn't tell us the resulting
   ratio matches the MS-bar perturbative expansion at M_Z. The
   two schemes differ by specific finite counterterms
   (`δ_MS-bar − δ_on-shell` is computable in SM). Matching the
   framework's root-level formula to MS-bar specifically requires
   showing the framework's "scheme" (whatever it is) produces
   the same counterterm structure.

3. **"MS-bar is the natural perturbative scheme"** — this is a
   preference, not a derivation. The on-shell scheme is equally
   "natural" from a different standpoint (it's closer to what's
   directly measured). The argument needs to distinguish.

## Key observational constraint

`sinw_effective_dimension.md` §"Comparison with experiment" shows
the formula's value 0.23123 matches different schemes with very
different z-scores:

| Scheme | Value | z (from 0.23123) |
|---|---|---|
| MS-bar at M_Z | 0.23121 ± 0.00004 | 0.5σ ✓ |
| Effective sin²θ_eff (Z-pole) | 0.23153 ± 0.00016 | 1.9σ |
| MS-bar at M_W | 0.23140 ± 0.00010 | 1.7σ |
| On-shell (1 − M_W²/M_Z²) | 0.22290 ± 0.00030 | 27.8σ ✗ |
| Low-energy (Q² → 0) | 0.23867 ± 0.00016 | 46.5σ ✗ |

**If the claim is "root ↔ MS-bar at M_Z", Z1 is met at 0.5σ.**

**If the claim is "root ↔ some-other-scheme", Z1 is not met** for
on-shell, low-Q², or (marginally) for effective sin²θ_eff.

The Z1 pass is **conditional on the scheme identification being
correct**. Gap 3 asks: is there a structural reason why the
framework's root formula is MS-bar at M_Z specifically, and not
the other schemes that would make the claim fail?

## Success criterion (structural)

Produce a derivation of the form:

    framework root-level coupling ratio
      ⇔ MS-bar regulated coupling ratio at μ = M_Z

where the equivalence is shown by:
- Matching renormalization-conditions (both schemes agree on
  specific subtraction terms for specific Green's functions).
- A unique scale identification that maps the Stern-Brocot root
  to the M_Z pole via framework-internal structure (not via
  SM RG; that's ruled out by `nulls/null_2_sm_running.md`).

## Failure criterion

Any of:

- Show that the framework's root formula corresponds to a scheme
  other than MS-bar at M_Z. Then Z1 must be re-tested in that
  scheme and likely fails.
- Show that "the root = M_Z" identification requires a framework-
  internal parameter or anchor other than the existing ones
  (H_0, v_EW). That would introduce a third anchor and break
  the current canonical input count.
- Show that the formula matches multiple schemes equally well
  (by symmetry or by insufficient discrimination). Then the
  scheme identification is ambiguous, and the Z1 pass depends
  on an unjustified choice.

## Consistency check with prior nulls

- `nulls/null_2_sm_running.md` rules out SM 1-loop RG as the
  bridge between tree/root and M_Z. So Gap 3's identification
  **cannot** use RG running.
- `nulls/null_3_k_scan.md` rules out K-scanning as a source of
  scale-matching. So Gap 3's identification cannot use finite-K
  duty dynamics.
- The identification must be via a third mechanism — a
  framework-internal scheme / scale mapping not yet articulated
  in the repo.

## Suggested derivation path

Two natural directions:

**(a) Counter-term matching.** Compute the one-loop contribution
to the coupling ratio in both the framework's root-level
derivation and MS-bar. Show they agree.

**(b) Renormalization-group fixed point.** If the framework's
root is a fixed point of some internal rescaling (not SM RG),
show that the fixed point's invariant coincides with the MS-bar
invariant at M_Z.

Concrete attempt files would live in
`../attempts/g3_counterterm_match.md` or
`../attempts/g3_scheme_fixed_point.md`.

## Cross-references

- `../claim.md`
- `../nulls/null_2_sm_running.md`
- `../../../sync_cost/derivations/sinw_effective_dimension.md:138-157`
- `../../../sync_cost/derivations/hierarchy.md` (tree = Planck
  identification — possibly in tension with "root = M_Z")
