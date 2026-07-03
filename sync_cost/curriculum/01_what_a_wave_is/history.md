# Module 1 — History and naming

Read this after working through `README.md` and `engine.py`.

This file names the *wave-mechanics ingredients* — restoration,
inertia, coupling, and their combination into the wave equation.
The six **observations** planted at the end of the module — what
later get called Doppler shift, redshift, time dilation, mass-energy
equivalence, the Planck wall, and the Hubble wall — are named in a
companion module, [`01a_six_observations/`](../01a_six_observations/).

That separation is deliberate. This module is the *construction*;
the observations module is the *recognition*. Naming the
observations alongside the construction would conflate the two and
re-create the recognition-first failure mode this curriculum exists
to avoid.

## Restoration — Hooke's law

The proportionality of restoring force to displacement is named for
Robert Hooke. He announced it in 1676 as an anagram — *ceiiinosssttuv*
— and revealed the solution two years later as *ut tensio sic vis*,
"as the extension, so the force." The relationship is the simplest
non-trivial restoring force, and as the module's construction shows,
it is forced by the local-parabola geometry of any smooth potential
minimum.

The deeper reading — that Hooke's law is *generic* near any stable
equilibrium, not a special property of springs — was made explicit by
Lagrange (1788, *Mécanique analytique*) and is standard in any modern
treatment of small oscillations. Module 0's parabola is doing the
work in both readings; Hooke's name attaches to the special case of
mechanical springs.

## Inertia — Newton's first and second laws

Inertia — that a body persists in its state of motion until acted on
by a force — is Newton's first law (*Principia*, 1687). The
quantitative form, that force equals mass times acceleration, is the
second law. Both were anticipated by Galileo (1638, *Dialogues
Concerning Two New Sciences*) and earlier medieval natural
philosophy, but Newton's synthesis is the one that closed the
construction of mechanical oscillation: with restoration + inertia,
the period 2π·√(m/k) follows.

## Coupling and the wave equation — d'Alembert

The form of the coupling force used in this module — proportional to
the difference between neighbors' displacements — is the discrete
analog of the second spatial derivative ∂²x/∂s². Take the limit of
many closely-spaced points and the equation of motion for the chain
becomes:

```
    ∂²u/∂t²  =  (k_coup · a² / m) · ∂²u/∂s²
```

where *a* is the spacing between points. This is the *wave equation*,
first written down by Jean le Rond d'Alembert in 1747 for a vibrating
string. The propagation speed is √(coupling stiffness per unit length
/ inertia per unit length).

D'Alembert also gave the general solution: any disturbance can be
decomposed into a left-traveling part *f(s + ct)* and a
right-traveling part *g(s − ct)*. The two outward fronts visible in
the `--demo wave` output are exactly that decomposition.

The name *wave equation* is now the universal label for any equation
of this form, regardless of medium. The same equation describes
sound in air, transverse waves on a string, electromagnetic waves in
vacuum, pressure waves in fluids, and (with modifications) gravity
waves. The reason it appears everywhere is the reason this module
exists: three ingredients — restoration, inertia, coupling — are
extremely common, and their combination is non-negotiable.

## What you now have

A construction of the wave from three forced ingredients, plus six
observations planted as consequences. The names of the wave's
ingredients are Hooke, Newton, d'Alembert. The names of the
observations are reserved for [Module 1a](../01a_six_observations/),
which exists so that the recognition step is clearly separated from
the construction step.

Module 2 will take two of these waves and ask what happens when they
share a single medium. The answer is mode locking, and it is where
integers first appear without being put in by hand.
