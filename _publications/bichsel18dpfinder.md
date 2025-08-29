---
ref: bichsel18dpfinder
title: "DP-Finder: Finding Differential Privacy Violations by Sampling and Optimization"
authors: Benjamin Bichsel, Timon Gehr, Dana Drachsler-Cohen, Petar Tsankov, Martin Vechev
year: 2018
month: 10
venue: ACM CCS
projects: probabilistic-programming, diff-privacy
awards:
bibtex: ''
paper: https://files.sri.inf.ethz.ch/website/papers/ccs18-dpfinder.pdf
talk: https://www.youtube.com/watch?v=Jwe0oCSlaMk
slides: https://files.sri.inf.ethz.ch/website/slides/ccs18-dpfinder-slides.pdf
code: https://github.com/eth-sri/dp-finder
---

We present DP-Finder, a novel approach and system that automat- ically derives lower bounds on the differential privacy enforced by algorithms. Lower bounds are practically useful as they can show tightness of existing upper bounds or even identify incorrect upper bounds. Computing a lower bound involves searching for a coun- terexample, defined by two neighboring inputs and a set of outputs, that identifies a large privacy violation. This is an inherently hard problem as finding such a counterexample involves inspecting a large (usually infinite) and sparse search space.

To address this challenge, DP-Finder relies on two key insights. First, we introduce an effective and precise correlated sampling method to estimate the privacy violation of a counterexample. Sec- ond, we show how to obtain a differentiable version of the problem, enabling us to phrase the search task as an optimization objective to be maximized with state-of-the-art numerical optimizers. This allows us to systematically search for large privacy violations. Our experimental results indicate that DP-Finder is effective in computing differential privacy lower bounds for a number of randomized algorithms. For instance, it finds tight lower bounds in algorithms that obfuscate their input in a non-trivial fashion.
