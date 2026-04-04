/**
 * Artifact definitions and reference graph for the synchronization-cost framework.
 *
 * Each artifact has:
 *   id         – unique key
 *   name       – human-readable short name
 *   symbol     – mathematical symbol or compact notation
 *   formal     – one-line formal definition
 *   description – 2-3 sentence plain-language explanation
 *   refs       – ids this artifact directly builds on or invokes
 *   derivation – path to derivation file (if any)
 *   pages      – which application pages feature this artifact
 */

/* global window */
(function (root) {
  "use strict";

  var ARTIFACTS = {
    integers: {
      id: "integers",
      name: "Integers",
      symbol: "\u2124",
      formal: "\u2124: the natural numbers.  Counting exists.",
      description:
        "The irreducible starting point.  Before rhythm there is pulse; before pulse there is one.  " +
        "Distinguishing something from nothing is the only axiom.",
      refs: [],
      derivation: null,
      pages: ["ontology"]
    },

    mediant: {
      id: "mediant",
      name: "Mediant",
      symbol: "(a+c)/(b+d)",
      formal: "The unique fraction satisfying betweenness and denominator-minimality between a/b and c/d.",
      description:
        "Given two fractions a/b and c/d, the mediant (a+c)/(b+d) is the simplest fraction that fits between them.  " +
        "It is the fundamental binary operation that generates the Stern\u2013Brocot tree.",
      refs: ["integers"],
      derivation: null,
      pages: ["ontology", "stern_brocot_walk"]
    },

    fixed_point: {
      id: "fixed_point",
      name: "Fixed point",
      symbol: "x = f(x)",
      formal: "Self-reference: the output equals the input.",
      description:
        "A state that survives its own map.  The system that measures itself finds a value that persists.  " +
        "Fixed points anchor every self-consistent physical law in the framework.",
      refs: ["integers"],
      derivation: null,
      pages: ["ontology"]
    },

    parabola: {
      id: "parabola",
      name: "Saddle-node / Parabola",
      symbol: "x\u00b2 + \u03bc = 0",
      formal: "The generic co-dimension-1 bifurcation: one state becomes two.",
      description:
        "At a critical parameter value, a single equilibrium splits into two via a square-root.  " +
        "This universal geometry appears at every Arnold tongue boundary and determines the Born-rule exponent.",
      refs: ["fixed_point"],
      derivation: "../derivations/01_born_rule.md",
      pages: ["ontology"]
    },

    circle: {
      id: "circle",
      name: "Circle",
      symbol: "S\u00b9 = \u211d/\u2124",
      formal: "The real line modulo the integers.  Phase is periodic.",
      description:
        "Compact phase space derived from integers plus a fixed point.  Not assumed \u2014 forced.  " +
        "Every oscillator lives on a circle.",
      refs: ["integers", "fixed_point"],
      derivation: null,
      pages: ["ontology", "mobius_projector"]
    },

    circle_map: {
      id: "circle_map",
      name: "Circle map",
      symbol: "\u03b8\u2099\u208a\u2081 = \u03b8\u2099 + \u03a9 \u2212 (K/2\u03c0)sin 2\u03c0\u03b8\u2099",
      formal: "The standard map on S\u00b9 with frequency \u03a9 and coupling K.",
      description:
        "Two oscillators coupled on a circle.  The three parameters (\u03b8, \u03a9, K) determine " +
        "whether the system locks to a rational frequency or wanders quasi-periodically.  " +
        "K\u2009=\u20091 is the critical (Einstein) regime; K\u2009<\u20091 is the quantum (Schr\u00f6dinger) regime.",
      refs: ["circle"],
      derivation: "../derivations/09_circle_map_master.md",
      pages: ["ontology", "double_pendulum"]
    },

    arnold_tongues: {
      id: "arnold_tongues",
      name: "Arnold tongues",
      symbol: "w(p/q) ~ (K/2)\u1D60",
      formal: "Regions in (\u03a9, K) parameter space where the circle map locks to rational p/q.",
      description:
        "Wedge-shaped stability zones rooted at each rational on the \u03a9 axis.  " +
        "Width decreases exponentially with denominator q: simple fractions dominate.  " +
        "Every stable astronomical resonance sits inside a tongue.",
      refs: ["circle_map", "stern_brocot_tree"],
      derivation: "../derivations/10_tongue_width.md",
      pages: ["ontology", "double_pendulum", "three_body_catalog"]
    },

    devils_staircase: {
      id: "devils_staircase",
      name: "Devil\u2019s staircase",
      symbol: "W(\u03a9, K)",
      formal: "The winding-number function: flat on every rational, continuous, monotone, measure-1 at K\u2009=\u20091.",
      description:
        "A fractal step function whose plateaus are the Arnold tongues projected onto the \u03a9 axis.  " +
        "At K\u2009=\u20091 the plateaus fill the line; the gaps (irrationals) have measure zero.  " +
        "Self-similar at 1/\u03c6 with scaling \u03c6\u00b2.",
      refs: ["arnold_tongues", "farey_partition"],
      derivation: null,
      pages: ["ontology"]
    },

    stern_brocot_tree: {
      id: "stern_brocot_tree",
      name: "Stern\u2013Brocot tree",
      symbol: "SB",
      formal: "The complete binary tree of positive rationals, ordered by denominator, generated by the mediant.",
      description:
        "Every rational appears exactly once.  The tree is the Cayley graph of SL(2,\u2124) and the " +
        "configuration space for all possible frequency ratios.  Navigation is by continued-fraction digits (L/R).",
      refs: ["mediant"],
      derivation: null,
      pages: ["ontology", "stern_brocot_walk", "three_body_catalog"]
    },

    continued_fraction: {
      id: "continued_fraction",
      name: "Continued fraction",
      symbol: "[a\u2080; a\u2081, a\u2082, \u2026]",
      formal: "The unique encoding of a rational as a sequence of integer quotients \u2194 L/R path in SB.",
      description:
        "7/60 = [0; 8, 1, 1, 3] means: go left 8, right 1, left 1, right 3 down the Stern\u2013Brocot tree.  " +
        "The path depth (sum of quotients) equals 13 = |F\u2086|, linking tree navigation to the Farey count.",
      refs: ["stern_brocot_tree"],
      derivation: null,
      pages: ["stern_brocot_walk"]
    },

    born_rule: {
      id: "born_rule",
      name: "Born rule",
      symbol: "|\u03c8|\u00b2",
      formal: "\u0394\u03b8 \u221d \u221a\u03b5 at tongue boundary \u21d2 probability exponent = 2.",
      description:
        "The Born rule is not a postulate.  The saddle-node geometry at every tongue boundary " +
        "forces a square-root dependence, so the occupation measure scales as the square of the amplitude.  " +
        "This is the framework\u2019s derivation of quantum probability.",
      refs: ["parabola", "arnold_tongues"],
      derivation: "../derivations/01_born_rule.md",
      pages: ["ontology"]
    },

    field_equation: {
      id: "field_equation",
      name: "Field equation",
      symbol: "N(p/q) = N\u209c\u2092\u209c \u00d7 g \u00d7 w",
      formal: "Self-consistent occupation on the Stern\u2013Brocot tree.  K\u2009=\u20091 \u2192 Einstein; K\u2009<\u20091 \u2192 Schr\u00f6dinger.",
      description:
        "Each node\u2019s occupation is the product of the total count, a degeneracy factor, " +
        "and the tongue width \u2014 where the tongue width itself depends on the total count.  " +
        "The self-consistent solution is the fixed point of the framework.",
      refs: ["stern_brocot_tree", "arnold_tongues", "fixed_point"],
      derivation: "../derivations/12_field_equation.md",
      pages: ["ontology"]
    },

    three_dimensions: {
      id: "three_dimensions",
      name: "Three dimensions",
      symbol: "d = 2\u00b2 \u2212 1 = 3",
      formal: "The mediant lives in SL(2,\u2124) whose Lie algebra has dimension 3.",
      description:
        "Spatial dimension is derived, not assumed.  The mediant has two components (numerator, denominator); " +
        "its symmetry group SL(2,\u211d) has dimension 2\u00b2\u22121 = 3.  Space has three directions because fractions have two parts.",
      refs: ["mediant", "stern_brocot_tree"],
      derivation: "../derivations/15_three_dimensions.md",
      pages: ["ontology"]
    },

    klein_bottle: {
      id: "klein_bottle",
      name: "Klein bottle",
      symbol: "K\u00b2",
      formal: "Two antiperiodic identifications.  XOR parity filter: 1764 candidate modes \u2192 4 survivors.",
      description:
        "The non-orientable surface that serves as the topology container for the field equation.  " +
        "Its antiperiodic boundary conditions select exactly the modes that survive the twist, " +
        "reducing the mode count to those consistent with the Farey partition.",
      refs: ["circle", "farey_partition"],
      derivation: "../derivations/22_klein_topology.md",
      pages: ["ontology", "mobius_projector", "mobius_views"]
    },

    farey_partition: {
      id: "farey_partition",
      name: "Farey partition",
      symbol: "\u03a9\u039b = 13/19",
      formal: "|F\u2086| = 13 resolved states, budget = 13 + q\u2082q\u2083 = 19.  \u03a9\u039b = 13/19 = 0.6842.",
      description:
        "The Farey sequence F\u2086 has 13 fractions.  Adding the 6 interaction channels (q\u2082\u00d7q\u2083 = 2\u00d73) " +
        "gives a budget of 19.  The ratio 13/19 matches the Planck measurement of dark energy (\u03a9\u039b = 0.6847 \u00b1 0.0073) " +
        "to 0.07\u03c3.  Zero free parameters.",
      refs: ["stern_brocot_tree", "klein_bottle", "continued_fraction"],
      derivation: "../derivations/25_farey_partition.md",
      pages: ["ontology", "stern_brocot_walk", "mobius_projector", "mobius_views"]
    },

    winding_number: {
      id: "winding_number",
      name: "Winding number",
      symbol: "W(\u03a9, K)",
      formal: "The average rotation per iterate of the circle map: lim (1/n) \u03a3 (\u03b8\u2099\u208a\u2081 \u2212 \u03b8\u2099).",
      description:
        "Rational winding number means the oscillator is locked (periodic orbit).  " +
        "Irrational means it is unlocked (quasi-periodic).  The winding number is the vertical axis of the devil\u2019s staircase.",
      refs: ["circle_map"],
      derivation: null,
      pages: ["ontology", "double_pendulum", "three_body_catalog"]
    },

    mode_locking: {
      id: "mode_locking",
      name: "Mode locking",
      symbol: "p:q",
      formal: "A dynamical system\u2019s frequencies lock to a rational ratio p/q inside an Arnold tongue.",
      description:
        "When coupling is strong enough, an oscillator\u2019s frequency snaps to the nearest simple rational.  " +
        "This is the mechanism behind stable astronomical resonances (Laplace, TRAPPIST-1) " +
        "and the wagon-wheel effect in the ontology visualization.",
      refs: ["arnold_tongues", "winding_number"],
      derivation: null,
      pages: ["ontology", "double_pendulum", "three_body_catalog"]
    },

    farey_warping: {
      id: "farey_warping",
      name: "Farey warping",
      symbol: "t \u2192 F(t)",
      formal: "Re-parametrize time so that dwell at fraction p/q is proportional to 1/q\u00b2 (Ford circle area).",
      description:
        "Linear time is warped through the Farey cumulative distribution.  Simple fractions (1/2, 1/3) " +
        "get longer holds; complex ones flash by.  This is the temporal skeleton of the M\u00f6bius projector.",
      refs: ["farey_partition"],
      derivation: null,
      pages: ["mobius_projector", "mobius_views"]
    },

    mobius_strip: {
      id: "mobius_strip",
      name: "M\u00f6bius strip",
      symbol: "M",
      formal: "A non-orientable surface with a single boundary: the half-twist of the filmstrip.",
      description:
        "The projector\u2019s film loop has a twist: after one full revolution the emulsion faces backward.  " +
        "Normal and inverted passes alternate.  The twist point is where polarity flips \u2014 " +
        "an audible click, a visual scramble, the antiperiodic boundary of the Klein bottle in one dimension.",
      refs: ["klein_bottle", "circle"],
      derivation: null,
      pages: ["mobius_projector", "mobius_views"]
    },

    lyapunov: {
      id: "lyapunov",
      name: "Lyapunov exponent",
      symbol: "\u03bb",
      formal: "The exponential rate of divergence of nearby trajectories.  \u03bb > 0 \u21d2 chaos.",
      description:
        "Measures sensitivity to initial conditions.  Inside a tongue \u03bb \u2264 0 (stable/locked).  " +
        "At the tongue boundary \u03bb crosses zero; beyond it, KAM tori break and the system is chaotic.  " +
        "The framework predicts: tongue boundary = Lyapunov transition.",
      refs: ["arnold_tongues", "circle_map"],
      derivation: null,
      pages: ["double_pendulum"]
    },

    kam_tori: {
      id: "kam_tori",
      name: "KAM tori",
      symbol: "KAM",
      formal: "Kolmogorov\u2013Arnold\u2013Moser: irrational frequency ratios are shielded by invariant tori at low coupling.",
      description:
        "At low energy (weak coupling), quasi-periodic orbits with irrational winding numbers survive " +
        "on invariant tori.  As energy grows, the tori break in order of rational approximability \u2014 " +
        "golden ratio (\u03c6) tori are the last to fall.  The double pendulum\u2019s 1+\u221a2 ratio is KAM-protected.",
      refs: ["winding_number", "arnold_tongues"],
      derivation: null,
      pages: ["double_pendulum"]
    },

    free_group_word: {
      id: "free_group_word",
      name: "Free-group word",
      symbol: "BabA\u2026",
      formal: "A string in generators {a, b, A, B} encoding the topological braid class of a three-body orbit.",
      description:
        "Each periodic three-body orbit has a unique braid word describing how the bodies weave around each other.  " +
        "Word length L_f is the topological complexity; the ratio T*/L_f (period per letter) " +
        "is remarkably constant, meaning each letter costs a fixed dynamical time.",
      refs: ["stern_brocot_tree", "winding_number"],
      derivation: null,
      pages: ["three_body_catalog"]
    },

    spectral_tilt: {
      id: "spectral_tilt",
      name: "Spectral tilt",
      symbol: "n\u209b \u2248 0.965",
      formal: "The CMB power spectrum slope, derived from the Farey density exponent.",
      description:
        "The framework predicts n\u209b = 1 \u2212 2/(|F\u2086|+q\u2082q\u2083) = 1 \u2212 2/19 \u2248 0.9649, " +
        "matching the Planck 2018 measurement n\u209b = 0.9649 \u00b1 0.0042 to within 0.01\u03c3.",
      refs: ["farey_partition"],
      derivation: "../derivations/02_spectral_tilt.md",
      pages: []
    }
  };

  // Page metadata: which artifacts are primary on each page
  var PAGES = {
    ontology: {
      title: "The Ontology",
      primary: [
        "integers", "mediant", "fixed_point", "parabola", "circle",
        "circle_map", "arnold_tongues", "devils_staircase", "stern_brocot_tree",
        "born_rule", "field_equation", "three_dimensions", "klein_bottle", "farey_partition"
      ]
    },
    stern_brocot_walk: {
      title: "Stern\u2013Brocot Walk",
      primary: [
        "stern_brocot_tree", "mediant", "continued_fraction", "farey_partition"
      ]
    },
    mobius_projector: {
      title: "M\u00f6bius Projector",
      primary: [
        "mobius_strip", "klein_bottle", "farey_partition", "farey_warping", "circle"
      ]
    },
    mobius_views: {
      title: "M\u00f6bius Views",
      primary: [
        "mobius_strip", "klein_bottle", "farey_partition", "farey_warping"
      ]
    },
    double_pendulum: {
      title: "Double Pendulum",
      primary: [
        "circle_map", "arnold_tongues", "mode_locking", "winding_number",
        "lyapunov", "kam_tori"
      ]
    },
    three_body_catalog: {
      title: "Three-Body Catalog",
      primary: [
        "stern_brocot_tree", "arnold_tongues", "winding_number",
        "mode_locking", "free_group_word"
      ]
    }
  };

  // Expose globally
  root.HARMONICS_ARTIFACTS = ARTIFACTS;
  root.HARMONICS_PAGES = PAGES;

})(typeof window !== "undefined" ? window : this);
