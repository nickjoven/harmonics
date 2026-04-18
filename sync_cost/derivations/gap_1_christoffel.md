# Gap 1: The Christoffel Connection from Kuramoto Ensemble Averages

## Status

**Closed in the continuum limit**, conditionally. See
`gap1_theorem.md` for the theorem statement and proof combining the
Step 1–3 numerical results with Strogatz–Mirollo 1991 (CLT for the
Kuramoto locked state) and the fundamental theorem of Riemannian
geometry. Result:

  Γ̃ᵏ_ij = Γᵏ_ij + O(1/N)

in the supercritical continuum limit (a → 0, N → ∞, L fixed, K > K_c).

The O(1/N) finite-N correction is a prediction, not a residual gap.
What is not proved: K = K_c (critical) case, non-uniform locking,
and the exact correspondence between the framework's "K = 1" and the
Kuramoto criterion K > K_c.

---

## The tautology argument and why it's half-right

`einstein_from_kuramoto.md` argues: γᵢⱼ = Cᵢⱼ/C₀ is a smooth
positive-definite symmetric tensor field. By the fundamental theorem
of Riemannian geometry, it has a unique Levi-Civita connection. The
Christoffel symbols Γᵏᵢⱼ are expressible in terms of first derivatives
of γ, which are expressible in terms of Kuramoto three-point
correlations. Therefore the connection is determined. No gap.

**What's right about this:** The connection EXISTS and is UNIQUE. Given
γᵢⱼ, the Christoffel symbols are determined. Metric compatibility
∇ₖγᵢⱼ = 0 holds identically. This is indeed a tautology.

**What's wrong about this:** The question was never whether the
Levi-Civita connection of γ exists. The question is whether the
**dynamics** use it.

The first ADM equation reads:

    ∂γᵢⱼ/∂t = -2N𝒦ᵢⱼ + DᵢNⱼ + DⱼNᵢ

The Dᵢ in DᵢNⱼ is a covariant derivative. In the ADM formalism, it
is the Levi-Civita connection of γ. In the Kuramoto derivation, the
corresponding term arises from:

    -⟨∂ᵢ(r sin(ψ-θ)) ∂ⱼθ⟩ - (i↔j)

expanded using the product rule. The question: does this expansion,
at all orders, produce exactly the Levi-Civita covariant derivative
DᵢNⱼ = ∂ᵢNⱼ - ΓᵏᵢⱼNₖ, or does it produce ∂ᵢNⱼ − Γ̃ᵏᵢⱼNₖ for
some other connection Γ̃?

---

## The actual gap: precise statement

The metric γᵢⱼ has a unique Levi-Civita connection Γ. The Kuramoto
dynamics produces transport terms that define an effective connection
Γ̃. The gap is:

**Does Γ̃ = Γ?**

Equivalently: when the Kuramoto evolution equation is written in the
form

    ∂γᵢⱼ/∂t = -2N𝒦ᵢⱼ + ∂ᵢNⱼ + ∂ⱼNᵢ − Γ̃ᵏᵢⱼNₖ − Γ̃ᵏⱼᵢNₖ

is Γ̃ᵏᵢⱼ = Γᵏᵢⱼ (the Christoffel symbols of γ)?

### Why this might be trivially true

`einstein_from_kuramoto.md` (line 42) argues: "The nontrivial content
is that the Kuramoto dynamics **preserves** this structure." And then
gives four conditions under which the first ADM equation holds exactly:

| Condition | Status | Type |
|-----------|--------|------|
| C₀ = 1 (absorbed into lapse) | Gauge choice | Kinematic |
| ⟨∂ᵢθ⟩ = 0 (centered ensemble) | Ensemble symmetry | Kinematic |
| ⟨cos(ψ-θ) ∂ⱼθ⟩ = ∂ⱼψ | Locked state (K≈1) | Dynamical |
| ⟨sin(ψ-θ) ∂ⱼθ⟩ = 0 | Locked state (antisymmetry) | Dynamical |

If these four conditions hold, the argument is:

1. The evolution equation for γᵢⱼ involves only γᵢⱼ itself and its
   first spatial derivatives (through the ψᵢ = Nᵢ/N terms).
2. The only connection built from γ and ∂γ alone is Levi-Civita.
3. Therefore Γ̃ = Γ — not because we checked term by term, but
   because there's nothing else it could be.

**This argument is actually strong.** The question reduces to:

**Do the four locked-state conditions hold exactly at K=1, or only
approximately?**

---

## Sharpening: what exactly needs to be proved

### Condition 3: ⟨cos(ψ-θ) ∂ⱼθ⟩ = ∂ⱼψ

This is the critical one. Write φ = ψ − θ (the phase offset from
the mean field). In the locked state, φ is small. Expand:

    cos(φ) = 1 − φ²/2 + φ⁴/24 − ...

So:

    ⟨cos(φ) ∂ⱼθ⟩ = ⟨∂ⱼθ⟩ − ½⟨φ² ∂ⱼθ⟩ + ...
                    = ∂ⱼψ − ½⟨φ² ∂ⱼθ⟩ + ...

(using ⟨∂ⱼθ⟩ = ∂ⱼψ in the locked state). The condition holds
exactly iff the correction terms vanish:

    **⟨φ² ∂ⱼθ⟩ = 0**    (and all higher-order corrections)

This is a statement about the **third moment** of the locked-state
ensemble. It says: the phase fluctuations φ are uncorrelated with
the phase gradient ∂ⱼθ. Specifically, the covariance of φ² with
∂ⱼθ vanishes.

### When does ⟨φ² ∂ⱼθ⟩ = 0?

**Case 1: Gaussian fluctuations.** If the locked-state fluctuations
are Gaussian in φ, then ⟨φ² ∂ⱼθ⟩ = ⟨φ²⟩⟨∂ⱼθ⟩ + 2⟨φ ∂ⱼθ⟩⟨φ⟩.
With ⟨φ⟩ = 0 (centered) and ⟨φ ∂ⱼθ⟩ = 0 (locked-state symmetry),
this gives ⟨φ² ∂ⱼθ⟩ = ⟨φ²⟩∂ⱼψ. This is NOT zero — it gives a
correction proportional to the variance.

BUT: this correction can be absorbed into the normalization C₀. The
coherence tensor already divides by C₀ = 1 − ⟨|∇θ|²⟩ (which
contains ⟨φ²⟩). The question is whether the C₀ normalization
exactly absorbs all variance corrections.

**Case 2: Thermodynamic limit (N→∞).** In the limit of infinitely
many oscillators, the central limit theorem makes fluctuations
Gaussian with variance O(1/N). The corrections ⟨φ² ∂ⱼθ⟩ are
O(1/N) and vanish. The connection is exactly Levi-Civita in the
continuum limit.

**Case 3: Finite ensemble.** For finite N, the corrections are
O(1/N) and produce a non-Levi-Civita contribution to the connection
(torsion or non-metricity). These are suppressed in the thermodynamic
limit but could be relevant at the Planck scale where N is minimal.

### The resolution (proposed)

The gap reduces to proving:

**Lemma (connection exactness).** In the continuum limit (N→∞) of
the Kuramoto ensemble at K=1, the four locked-state conditions hold
exactly, and therefore Γ̃ = Γ.

The proof strategy:

1. The locked state at K=1 has fluctuations φ = ψ − θ with variance
   σ²_φ = O(1/N) (central limit theorem for the mean field).

2. The correction to Condition 3 is ⟨φ² ∂ⱼθ⟩ = O(σ²_φ) = O(1/N).

3. The correction to Condition 4 is ⟨sin(φ) ∂ⱼθ⟩ ≈ ⟨φ ∂ⱼθ⟩ = 0
   by the centered-ensemble condition (exact, no N dependence).

4. In the N→∞ continuum limit, all corrections vanish.
   Therefore Γ̃ = Γ exactly.

5. At finite N, the O(1/N) corrections produce a connection that
   differs from Levi-Civita by torsion/non-metricity of order 1/N.
   This is a **prediction**: Planck-scale gravity has O(1/N) corrections
   to general relativity, which could manifest as torsion.

---

## The second ADM equation

The first evolution equation (∂γ/∂t) is the cleaner case. The second
evolution equation (∂𝒦ᵢⱼ/∂t) is harder because it involves the Ricci
tensor ³Rᵢⱼ, which requires second derivatives of γ (hence fourth
moments of the θ-ensemble).

`einstein_from_kuramoto.md` decomposes this into five term classes
(Part I, lines 56-98). The key terms:

| Term | Kuramoto origin | Difficulty |
|------|----------------|------------|
| -DᵢDⱼN | Second derivative of ⟨sin(φ) ∂ⱼθ⟩ | Moderate: involves third moments |
| N ³Rᵢⱼ | Phase stiffness (kinematic from γ) | **None**: follows from γ definition |
| N(K𝒦-2𝒦²) | Products of two-point correlations | Moderate: mean-field factorization needed |
| ℒ_β 𝒦 | Shift transport | Easy: locked-state symmetry |
| Matter | ω-dependent correlations | Separate: normalization question |

The Ricci tensor term (³Rᵢⱼ) is kinematic — it's defined by γ
regardless of Kuramoto dynamics. The extrinsic curvature self-
interaction term requires mean-field factorization:

    ⟨cos²φ ∂ᵢθ ∂ⱼθ ∂ₖθ ∂ₗθ⟩ ≈ ⟨cos φ ∂ᵢθ ∂ⱼθ⟩ γᵏˡ ⟨cos φ ∂ₖθ ∂ₗθ⟩

This is Wick's theorem for a Gaussian ensemble. It holds exactly in
the N→∞ limit and has O(1/N) corrections (connected four-point
cumulants) at finite N.

---

## Computation plan for next session

### Step 1: Verify the tautology argument (30 min)

Write a short script that:
- Defines γᵢⱼ = δᵢⱼ − ⟨∂ᵢθ ∂ⱼθ⟩ for a random smooth θ(x) on [0,1]³
- Computes Γᵏᵢⱼ from the standard Levi-Civita formula
- Computes the three-point correlations Tᵢⱼₗ from θ
- Checks that the Christoffel symbols computed both ways agree

This verifies that the tautology is correct: the connection of γ is
expressible in terms of θ-correlations. This is expected to pass
trivially (it's just the chain rule).

### Step 2: Verify Condition 3 at finite N (1 hr)

Write a Kuramoto simulation:
- N oscillators on a 1D ring at K=1 (full locking)
- Compute ⟨cos(φ) ∂ⱼθ⟩ and ∂ⱼψ
- Measure the difference as a function of N
- Verify O(1/N) scaling of the correction

If the correction scales as 1/N, the gap is closed in the continuum
limit. If it doesn't, there's a real problem.

### Step 3: Check the second ADM equation (2 hr)

Extend the simulation to compute:
- The Ricci tensor ³Rᵢⱼ from γ (numerical differentiation)
- The mean-field factorization error for the 𝒦² terms
- The full ∂𝒦/∂t and compare with the ADM prediction

This is the hardest step. If it works, both ADM evolution equations
are verified numerically, and the gap reduces to proving the 1/N
scaling analytically (a standard result for Kuramoto systems).

### Step 4: Analytic proof (if numerics pass)

The analytic proof should follow from:
1. Kuramoto fluctuation theory (Strogatz & Mirollo 1991): at K=1,
   the locked state has Gaussian fluctuations with variance O(1/N).
2. Wick's theorem: Gaussian fluctuations produce exact factorization
   of higher moments.
3. Fundamental theorem of Riemannian geometry: the unique connection
   built from γ alone is Levi-Civita.

The combination gives: Γ̃ = Γ + O(1/N), with the correction vanishing
in the continuum limit.

---

## What closing this gap means

If the Christoffel connection is verified:

1. The ADM evolution equations follow exactly from Kuramoto at K=1
   (not just at weak gradients).
2. Lovelock's theorem then gives Einstein's equations as the unique
   output — no other field equation is possible.
3. The gravitational sector of the framework is fully derived: four
   primitives → circle → SL(2,Z) → SL(2,R) → d=3 → Klein bottle →
   K=1 continuum → Kuramoto → ADM → Einstein. One identification
   remains (the ADM dictionary), but it's Type A (forced by
   uniqueness of available tensors).
4. The O(1/N) correction is a prediction: Planck-scale gravity has
   torsion of order l_P²/L², where L is the scale of observation.

## References

- continuum_limits.md §4 (lines 87–107): weak-gradient derivation
- einstein_from_kuramoto.md Part I (lines 18–55): tautology argument
- einstein_from_kuramoto.md Part I (lines 56–98): second ADM equation
- adm_prefactor_verification.py: σ² = 1/4 verification
- rational_field_equation.md Part VI item 2: continuum limit question
- Strogatz & Mirollo (1991): Stability of incoherence in coupled oscillators
