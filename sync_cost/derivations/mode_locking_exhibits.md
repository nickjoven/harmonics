# Mode-locking exhibits — the mechanism in the laboratory, the clinic, and the sky

## Status

Orientation / external-evidence catalog (pedagogical, evidential).
No new derivation, no new primitive, no substrate claim. This doc
collects the *measured* instances of mode-locking — the framework's
central mechanism — in systems where the physics is uncontroversial,
and states precisely what these exhibits do and do not establish for
the framework. Companion to `dynamical_quantization.md` (the
prism/spectral articulation) and `mediant_forcing_lemma.md` (the
formal hinge). External citations are candidates for `REFERENCES.md`.

## Why this catalog exists

The framework's headline mechanical claim (README): **coupled
oscillators in a continuous medium produce discrete mode-locked
tongues; quantization lives in the coupling, not the geometry.**
That claim is sometimes read as exotic. It is not. Mode-locking is
one of the most broadly instantiated phenomena in physics —
measured from Josephson junctions to planetary spins — and in its
best-measured instance it is *metrologically exact*. What is novel
in the framework is the **application** (that the vacuum's couplings
form such a system, on a Klein bottle, read at specific Farey
depths), not the **mechanism**. This catalog separates the two
cleanly: everything below is textbook or peer-reviewed physics
independent of this repository.

Each exhibit names the locked ratio, the measured observable, and
the framework object it instantiates.

## The exhibits

| # | System | Locked ratio(s) | What is measured | Framework object instantiated |
|---|---|---|---|---|
| 1 | Josephson junction under microwave drive (Shapiro steps) | V_n = n · f / K_J, K_J = 2e/h | voltage plateaus flat to parts in 10¹⁰; basis of the SI volt's practical realization | tongues as **exact** quantization; plateau = staircase step |
| 2 | Forced Rayleigh–Bénard convection in mercury (Stavans–Heslot–Libchaber 1985) | full p/q hierarchy | complete devil's staircase; complement fractal dimension D ≈ 0.87 matching circle-map criticality (Jensen–Bak–Bohr 1983/84) | the critical staircase itself; K = 1 universality class |
| 3 | Huygens' pendulum clocks (1665) | 1:1 (anti-phase) | historical origin of the field; "sympathie des horloges" | coupling → locking; the primitive observation |
| 4 | Mercury's spin–orbit resonance | 3:2 | radar ranging (Pettengill & Dyce 1965); capture theory (Goldreich & Peale 1966) | a non-trivial rational lock; capture probability = basin measure |
| 5 | Orbital resonances: Neptune–Pluto; Io–Europa–Ganymede | 3:2; 4:2:1 | centuries-stable orbital elements | hierarchy of simultaneous tongues |
| 6 | van der Pol & van der Mark neon-tube oscillator (1927) | subharmonic staircase | frequency demultiplication heard by ear; "irregular noise" between steps (early chaos) | staircase steps + the gaps between tongues |
| 7 | Periodically stimulated cardiac cells (Guevara–Glass–Shrier 1981) | 1:1, 2:1, 3:2, 2:3 (Wenckebach rhythms) | phase-locking zones in chick-heart aggregates; AV-block arrhythmias clinically | tongue boundaries crossed = qualitative state change |
| 8 | Circadian entrainment | 1:1 to the 24 h zeitgeber | entrainment range; jet lag = re-entrainment transient | tongue width as the detuning range that still locks |
| 9 | Phase-locked loops / injection locking (Adler 1946) | arbitrary engineered n:m | every radio, GPS receiver, frequency synthesizer | locking range formula; tongues as engineering spec |
| 10 | Adjacent organ pipes (Rayleigh) | 1:1 mutual locking | pitch pulling and quenching of neighboring pipes | acoustic locking — the repo's namesake register |
| 11 | **In-repo**: Stribeck friction chain | subharmonic conversion at N = 3 | `RESULTS.md`: first contact drops ω by 3 orders; subharmonic propagates undamped | the framework's own numerical laboratory |
| 12 | **In-repo**: metronome wall | 1:1 cluster formation | `prototype/` live simulation with W(Ω) staircase | the order parameter r watched forming |

### Exhibit 1 in one paragraph (the one to lead with)

A Josephson junction driven at microwave frequency f develops
voltage plateaus at V_n = n·f/K_J with K_J = 2e/h. These Shapiro
steps **are** Arnold tongues — the junction's phase mode-locks to
the drive — and they are flat and reproducible to parts in 10¹⁰,
which is why national metrology institutes realize the SI volt
with Josephson arrays. The most precisely engineered quantization
in existence is quantization-by-mode-locking. A reader who accepts
that discrete, *exact* ratios cannot emerge from a smooth driven
medium must first explain the volt.

### Exhibit 2 in one paragraph (the staircase measured)

Jensen, Bak & Bohr (1983/84) computed the circle map's complete
devil's staircase at critical coupling and found the staircase
complement has fractal dimension D ≈ 0.87 — a universal number for
the critical mode-locking class. Stavans, Heslot & Libchaber (1985)
then *measured* that dimension in forced Rayleigh–Bénard convection
in mercury. The staircase the framework computes on (`circle_map.py`,
`boundary_weight.py`) is not a metaphor; it is a measured object
with a confirmed universality class at exactly the K = 1 criticality
the framework's gravity limit occupies.

### Exhibit 4 in one paragraph (capture as basin measure)

Mercury rotates exactly three times per two orbits. Goldreich &
Peale (1966) showed capture into the 3:2 tongue (rather than 1:1)
is *probabilistic*, with probability set by the resonance's basin
geometry given Mercury's eccentricity. Nature ran a basin-measure
experiment at astronomical scale and landed in a non-trivial
rational tongue. The structural parallel to the framework's basin
measure (`born_rule.md`) is exact at the level of mechanism —
capture probability ∝ tongue geometry — though the framework's
Born-rule claim itself rests on its own derivation, not on this
analogy.

## The framework dictionary

The objects the exhibits instantiate, with their canonical homes:

| Exhibit observable | Framework object | Canonical doc |
|---|---|---|
| plateau / step | locked state at p/q | `rational_field_equation.md` |
| step width in detuning | tongue width w(p/q, K) = 2(K/2)^q h(p/q) | `rational_field_equation.md`, `boundary_weight.md` |
| staircase | W(Ω, K), the solution structure | `dynamical_quantization.md` |
| step edge (lock appears/disappears) | saddle-node boundary = measurement event | `born_rule.md`, `a1_from_saddle_node.md` |
| capture probability | basin measure | `born_rule.md` |
| synchronized fraction | order parameter r | `continuum_limits.md` |
| locking hierarchy (which ratio next) | mediant / Stern-Brocot enumeration | `mediant_forcing_lemma.md` |
| partial locking at a threshold | MOND-scale reading of a₀ | `a0_threshold.md` (framework claim, *not* an exhibit) |

The last row is deliberately fenced: a₀ = cH₀/(2π) is a framework
**claim** that partial locking operates at galactic scale — it
belongs to the framework's empirical program (`framework_status.md`
Survives), not to this catalog of independently established physics.

## What these exhibits establish — and what they do not

**They establish:**

1. **Universality of the mechanism.** Wherever coupling, nonlinearity,
   and frequency competition coexist, rational locking follows —
   electrical, thermal, mechanical, biological, astronomical.
   The mechanism needs no exotic substrate.
2. **Exactness of locked ratios.** Locked ratios are exact integers
   locked by dynamics, not approximate fits — to parts in 10¹⁰ in
   exhibit 1, to Myr stability in exhibit 5. When the framework
   asserts an exact 13/19 with no tuning story, the *kind* of claim
   is one nature demonstrably makes.
3. **The staircase is measured, including its critical universality
   class** (exhibits 2, 6). The framework computes on a confirmed
   object.
4. **Discreteness from smooth media.** Every exhibit is a continuous
   system producing discrete output — the README's headline claim,
   instantiated repeatedly.

**They do NOT establish:**

1. That the vacuum's couplings form such a system — the framework's
   substrate hypothesis stands on its own derivations and residuals,
   not on these analogies.
2. Any specific constant identification (Ω_Λ = 13/19, depth-6
   selection, the Z₆ unlocked count, Klein-bottle topology). Those
   live in their own docs with their own Z1–Z3 status.
3. That the mediant ordering governs *these* exhibits' locking
   sequence in detail (it does for the circle-map class; engineered
   and astronomical cases have their own capture histories).

Per `ansatz_audit_policy.md` discipline: this catalog raises the
prior on the *mechanism class*; it contributes zero evidence for
any *particular* framework number and is never to be cited as if it
did.

## Cross-links

- `dynamical_quantization.md` — the prism/spectral articulation
  this catalog grounds empirically
- `mediant_forcing_lemma.md` — the formal hinge for the locking
  *order* (companion doc, same PR)
- `rational_field_equation.md` — the equation the exhibits' shared
  structure instantiates
- `born_rule.md`, `a1_from_saddle_node.md` — basin measure,
  saddle-node boundaries
- `a0_threshold.md` — the framework's own partial-locking claim
  (fenced above)
- `continuum_limits.md` — K = 1 / K < 1 regimes the exhibits span
- `RESULTS.md`, `prototype/README.md` — in-repo exhibits
- `REFERENCES.md` — external-citation registry (rows above are
  addition candidates)

## One-line summary

Mode-locking is measured physics from the SI volt (Shapiro steps
flat to 10⁻¹⁰) through the devil's staircase's confirmed critical
dimension (D ≈ 0.87, mercury convection) to Mercury's 3:2 spin —
establishing the framework's *mechanism class* (exact discrete
ratios from smooth coupled media) as mundane, while its *application*
to fundamental constants remains the framework's own falsifiable
bet, argued elsewhere.
