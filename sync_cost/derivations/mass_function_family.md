# Mass-function family across cascade depths

The master cascade-lock identity gives a one-parameter slope family:

    α = -q_2 - n/d

with `(d, n)` selecting the cascade instance. But **not every `(d, n)`
is a licensed rung** — the depth `d` must be a *valid fragmentation
cascade* (see "Domain" below). Among the licensed depths, different
observed mass functions correspond to different cascade depths:

| Cascade instance | d | n | α | Observable | Domain · status |
|---|---|---|---|---|---|
| Gravitational K = 1 (string) | — | 0 | -2.000 | Press–Schechter halo MF | boundary (n=0) · generic, cheap |
| Globular-cluster MF | — | 0 | -2.000 | universal GC MF | boundary (n=0) · generic, cheap |
| Bowed cascade (Phase II) | 3 | 1 | -7/3 ≈ -2.333 | Salpeter IMF | **in-domain** (d=3 ✓) · 0.33σ |
| Clarinet cascade (q_3-base) | 2 | 1 | -5/2 | predicted | **in-domain** (d=2 ✓) · untested |
| ~~Z_6 cascade~~ | 6 | 1 | -13/6 ≈ -2.167 | ~~subhalo MF~~ | **out-of-domain** — d=6 ∉ {2,3,4}; subhalo is non-fragmentation (see Domain) |
| ~~Matter equilibrium K*~~ | 14 | 3 | -31/14 ≈ -2.214 | — | **out-of-domain** — d=14 ∉ {2,3,4}; matter-sector running, not fragmentation |

## Domain — what licenses a rung (category correction)

The slope formula is the **gravitational *fragmentation* cascade**
(`imf_bowed_cascade.md`). A `(d, n)` pair is a licensed rung only if it
clears **two membership tests** — and a rung that fails either is not a
*tension* or a *falsification*, it is a **category error** (an
observable from the wrong ontological class fitted to the formula):

1. **Depth admissibility (structural, #163).** The cascade depth must
   satisfy the Klein-orbit-count identity `orbit_count(F_m) = m`, which
   `imf_step2_klein_orbit.py` proves holds **only for `m ∈ {2,3,4}`**.
   So licensed fragmentation depths are `d ∈ {2,3,4}`; named instances
   populate `d=2` (clarinet) and `d=3` (bowed). Deeper assignments —
   `Z_6` (d=6, orbit count 7≠6) and `K*` (d=14) — are *not valid
   cascades*; their slopes were extrapolations of the formula past the
   depth its own structural lemma admits.
2. **Mechanism (physical).** The observable must be built by
   *fragmentation*. Subhalos form by accretion / merging / tidal
   stripping (hierarchical), and the matter-`K*` sector is *running*,
   not fragmentation (`master_cascade_identity.md`). Neither is a
   fragmentation population, so the formula does not apply to them
   *regardless* of depth.

**These two tests are independent and converge on the same rungs.** The
old "subhalo = Z_6, 2.67σ tension" entry fails *both* (excluded depth
**and** non-fragmentation mechanism), so it is recategorized here as
**out-of-domain**, not a triggered framework falsifier. The subhalo MF
is matched by the **K=1 boundary (-2.0)** — the generic large-scale
result — not by a deeper cascade rung.

**Honest consequence (not a strengthening).** The correction makes the
family *cleaner* but *smaller*: the in-domain fragmentation set is just
`{clarinet d=2 (untested), bowed d=3 (Salpeter, 0.33σ)}` plus the
generic K=1 boundary. `d=4` is admissible by the lemma but has no named
`(d,n,b)` instance yet. So removing the out-of-domain rungs removes the
apparent failure *and* a data point — it does not improve the
statistical case (the pigeonhole audit, `cascade_slope_check.py`,
p≈0.10), it sharpens *which* rungs the case may ever rest on.

## Structural reading

Part of the observed mass-function spread aligns with the slope
formula evaluated at the **licensed** cascade depths: as cascade depth
`d` increases toward the admissible ceiling, α → -q_2 = -2 (the K = 1
boundary), and shallower cascades give steeper slopes.

**Range caveat — now read as a domain-boundary prediction.** The
formula's image is `α = -q_2 - n/d ∈ (-2.5, -2.0]` for n ≥ 1 — it
asymptotes to -2.0 from below and **cannot produce any slope shallower
than -2.0**. Rather than a "coverage gap," this is a falsifiable
*domain boundary*: **a genuine gravitational-fragmentation MF is never
shallower than -2.0**; any observed MF shallower than that (the subhalo
slope -1.9 to -2.0) is therefore *non-fragmentation* and belongs to the
K=1 boundary (-2.0), not to a cascade rung. This is the same verdict
the Domain section reaches by depth-exclusion, arrived at independently
from the formula's range. The genuinely supported in-domain rung is the
bowed/Salpeter one (-7/3 vs -2.35 ± 0.05 = 0.33σ, `cascade_slope_check.py`);
the K = 1 boundary (-2.0) is consistent but observationally cheap; the
clarinet (-5/2) rung remains untested.

## Falsifiers

- **Domain boundary.** Discovery of a *bona fide gravitational-
  fragmentation* MF with α > -2.0 (shallower than the K=1 boundary)
  falsifies the domain claim — fragmentation cascades are confined to
  `(-2.5, -2.0]`. (The observed subhalo slope -1.9 to -2.0 does *not*
  trigger this: subhalos are non-fragmentation, accretion-built — see
  Domain. They were a category error, not a counterexample.)
- Salpeter IMF measured at α < -2.40 or α > -2.27: the Phase II bowed
  cascade prediction (-7/3 = -2.333) is out of band.
- Discovery of a fragmentation MF with α < -2.50: forbidden by the
  master identity unless n > 1.
- **Depth admissibility.** If a future argument shows a fragmentation
  cascade at `d ∉ {2,3,4}` *is* physically realized with a matching MF,
  the orbit-count selection (`imf_step2_klein_orbit.py`) is too narrow
  — the d=6/d=14 exclusion would need revisiting.

> **Note (category correction, 2026-05).** An earlier version of this
> doc listed "subhalo MF = Z_6 cascade" as a *triggered falsifier*.
> That framing was wrong on its own terms: the Z_6 (d=6) depth is
> excluded by #163's orbit-count lemma and subhalos are non-fragmentation,
> so the assignment was an **out-of-domain category error**, never a
> licensed prediction to be falsified. Recorded here so the record is
> honest, not narrated as load-bearing.

## Predicted observable: clarinet cascade α = -5/2

The q_3-cascade slope -5/2 has no current observable assignment.
Candidates worth checking:

- Massive young-cluster IMF (some studies report α ≈ -2.5 at the
  high-mass end; contested).
- Pre-main-sequence brown-dwarf formation regime.
- Dark-matter mode-mass spectrum if the antisym/clarinet sector hosts
  mass-locked modes.

## Companion: soliton mass spectrum on the same K-zoo

The fragmentation-slope formula `α = -q_2 - n/d` is one mass relation
the K-zoo gives. The soliton sector gives a second. By
`sine_gordon_substrate.md`, the kink mass at each cascade is
`M_k = 8 σ √(K r)`, so cross-sector ratios are

    M_k(d, n, b) / M_k(K=1) = b^(-n/(2d))

The two relations are structurally distinct — fragmentation slopes
come from the cascade-depth-as-Klein-orbit-count argument, kink masses
from the locked-state expansion of the framework Lagrangian — but they
share the same K input from `master_cascade_identity.md`. Sectors with
no fragmentation observable (e.g., the matter-equilibrium K* with
α = -31/14) may still admit a soliton observable; conversely, a sector
that hosts a fragmentation cascade may not host stable kinks.

The two columns have **different domains**: the fragmentation-α column
is licensed only at `d ∈ {2,3,4}` (Domain section), but the soliton
ratio `b^{-n/(2d)}` is a function of the *K-value*, which exists for
every K-zoo entry (`K*` is a confirmed K-value; `Z_6` suggestive). So
the `Z_6`/`K*` rows carry a *soliton* entry but **not** a licensed
fragmentation slope:

| Cascade instance | α (fragmentation) | M_k / M_k(K=1) (soliton) |
|---|---|---|
| K = 1 boundary | -2.000 | 1.000 |
| Bowed (d=3, n=1) | -7/3 ≈ -2.333 (in-domain) | 2^(-1/6) ≈ 0.891 |
| Clarinet (d=2, n=1) | -5/2 (in-domain) | 3^(-1/4) ≈ 0.760 |
| Z_6 (d=6, n=1) | ~~-13/6~~ out-of-domain | 2^(-1/12) ≈ 0.944 |
| Matter K* (d=14, n=3) | ~~-31/14~~ out-of-domain | 2^(-3/28) ≈ 0.928 |

> **Validity scope (soliton column only).** The kink-mass formula
> `M_k = 8 σ √(K r)` is rigorous only at K ≈ 1 per
> `sine_gordon_substrate.md` "Validity scope" subsection. Propagation
> across the K-zoo assumes each cascade-locked sector hosts an
> analogous sine-Gordon reduction around its own locked sub-state.
> The fragmentation-slope column is independent and not affected by
> this caveat.

## Cross-links

- `master_cascade_identity.md`
- `imf_bowed_cascade.md`
- `sine_gordon_substrate.md` — soliton mass spectrum companion
- `baryon_fraction.md` — Z_6 structure for the conjectured Z_6 cascade
