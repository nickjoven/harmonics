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
- **Residual, now closed.** `ε` (per-captured binding energy) is
  q-independent — derived in `epsilon_residual.py`, not assumed. Every
  Arnold tongue captures oscillators at the *same* density (the captured
  count is `g·w(p/q)` over a band of width `w(p/q)`, so the captured
  density `g` is q-independent at the uniform K=1 limit). The internal
  synchronization that binds the captured band is a Kuramoto problem
  whose onset `K_c = 2/(πg)` depends only on that density, so the binding
  `ε = K√(1−K_c/K)` is the same for every mode. The naive objection —
  that the binding inherits the q-th-order resonance depth `V_q ~ K^q` —
  fails because the mass function lives at K=1, where perturbation theory
  breaks down: the q-dependence is relocated entirely into the tongue
  width (the capture), and the per-captured binding is the cluster
  coherence, not the resonance depth. Modes with `q > q_max ~ √N` capture
  < 1 oscillator and do not survive — a physical low-mass cutoff that
  sets the small end of the range, not the slope.

## Status

The `-q_2` mass-function baseline is derived from the synchronization-
cost primitive plus the Farey mode-counting measure. It is now exactly
as well-founded as the framework's headline dimensionless results
(Ω_Λ, n_s) — resting on the same measure — and no longer carries a
borrowed fragmentation-cascade ingredient. The full bowed-cascade slope
`-7/3 = -q_2 - 1/q_3` is thereby framework-native: baseline here,
correction `-1/q_3` from the Step-2 Klein-orbit count
(`imf_step2_klein_orbit.py`). With the q-independent ε now derived
(`epsilon_residual.py`), the only thing the baseline still inherits is
the Farey-measure idealization at K=1 — the same one Ω_Λ and n_s rest
on. There is no slope-specific free assumption left.

## Cross-links

- `farey_mass_baseline.py` — numerical verification dN/dM ~ M^(-2)
- `epsilon_residual.py` — q-independence of the per-captured binding ε
- `imf_bowed_cascade.md` — the full bowed-cascade slope -7/3
- `imf_step2_klein_orbit.py` — the -1/q_3 correction (Klein-orbit count)
- `sine_gordon_substrate.md` — the short-range mean-field coupling collapse
- `FRAMEWORK.md` — the "energy = synchronization cost" primitive
