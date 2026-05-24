# Mass = entrained tongue measure, from the synchronization-cost functional

Closes the one load-bearing identification used in
`farey_mass_baseline.py` — that a locked mode's mass is its entrained
tongue-width measure, `M(p/q) ∝ w(p/q) ∝ 1/q²` at K=1 — by *deriving*
it from the framework's "energy = synchronization cost" primitive
rather than positing it.

## Claim

    M(p/q)  ∝  w(p/q)  ∝  1/q²     (at K = 1)

## Derivation

1. **Mass = synchronization cost** (primitive; `FRAMEWORK.md`). A locked
   structure's mass is the synchronization energy invested in
   maintaining its lock — the framework's primary quantity, denominated
   in energy.

2. **Captured oscillators.** A mode locked at p/q captures the
   oscillators whose bare frequency lies inside its Arnold tongue. The
   captured count is
   `N_cap = ∫_tongue g(ω) dω = g · w(p/q)`
   at the K=1 uniform (Lebesgue) limit, with `g` the (uniform)
   bare-frequency density and `w(p/q)` the tongue width.

3. **Energy is linear in the captured count.** Under the framework's
   short-range / local-mean-field coupling — the same cos-integral
   collapse `(1/2)∫K cos(θ−θ') → K r cos(θ−ψ)` used in
   `sine_gordon_substrate.md` — the locked cluster's coupling energy is
   linear (not quadratic) in its size:
   `E_sync = ε · N_cap`, where `ε ~ K r` is the in-phase coupling energy
   per captured oscillator. `ε` is order 1 at K=1 and **q-independent**:
   the resonance order q sets how *wide* the capture range is (the
   tongue width), not the per-captured binding — a captured oscillator
   is locked at order-1 coupling regardless of q.

4. Hence
   `M(p/q) = E_sync = ε g · w(p/q) ∝ w(p/q)`.

5. **w(p/q) ~ 1/q²** at K=1 — the Farey measure converging to Lebesgue,
   the same measure the framework already uses for Ω_Λ and n_s.

Therefore `M(p/q) ∝ 1/q²`. Combined with the Farey mode count
`|F_n| ~ (3/π²) n²` (`farey_mass_baseline.py`), this gives
`dN/dM ∝ M^(-2) = -q_2` — the baseline slope, end-to-end from the cost
functional and the mode-counting measure.

## What this closes, and what it inherits

- **Closed.** "Mass = entrained measure" is no longer posited; it
  follows from *mass = synchronization cost* + short-range coupling +
  uniform `g`. The `-1` that standard fragmentation theory imports as a
  measure constant is, here, the `dq/dM` Jacobian of the tongue-width
  mass map.
- **Inherited.** The chain rests on the Farey `1/q²` measure at K=1.
  That is a framework-established idealization of the critical circle
  map (whose exact mode-locking spectrum is multifractal), adopted
  throughout the framework (Ω_Λ, n_s). So the baseline now stands on the
  **same foundation as Ω_Λ = 13/19** — the Farey measure — rather than
  on an extra imported cascade ingredient.
- **Residual assumption.** `ε` (per-captured binding energy)
  q-independent. Reasonable at K=1 (captured oscillators lock at order-1
  coupling regardless of resonance order) but not separately proven.

## Status

The `-q_2` mass-function baseline is derived from the synchronization-
cost primitive plus the Farey mode-counting measure. It is now exactly
as well-founded as the framework's headline dimensionless results
(Ω_Λ, n_s) — resting on the same measure — and no longer carries a
borrowed fragmentation-cascade ingredient. The full bowed-cascade slope
`-7/3 = -q_2 - 1/q_3` is thereby framework-native: baseline here,
correction `-1/q_3` from the Step-2 Klein-orbit count
(`imf_step2_klein_orbit.py`), modulo the one residual (q-independent ε)
and the inherited Farey-measure idealization.

## Cross-links

- `farey_mass_baseline.py` — numerical verification dN/dM ~ M^(-2)
- `imf_bowed_cascade.md` — the full bowed-cascade slope -7/3
- `imf_step2_klein_orbit.py` — the -1/q_3 correction (Klein-orbit count)
- `sine_gordon_substrate.md` — the short-range mean-field coupling collapse
- `FRAMEWORK.md` — the "energy = synchronization cost" primitive
