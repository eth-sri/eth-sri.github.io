---
ref: ferrari2022complete
title: "Complete Verification via Multi-Neuron Relaxation Guided Branch-and-Bound"
authors: Claudio Ferrari, Mark Niklas Müller, Nikola Jovanović, Martin Vechev
year: 2022
month: 4
venue: ICLR 
projects: safeai
bibtex: '@inproceedings{
	ferrari2022complete,
	title={Complete Verification via Multi-Neuron Relaxation Guided Branch-and-Bound},
	author={Claudio Ferrari and Mark Niklas M{\"{u}}ller and Nikola Jovanović and Martin Vechev},
	booktitle={International Conference on Learning Representations},
	year={2022}}'
paper: https://files.sri.inf.ethz.ch/website/papers/ferrari2022complete.pdf
#slides: https://files.sri.inf.ethz.ch/website/slides/mueller2021boosting_slides.pdf
#poster: https://files.sri.inf.ethz.ch/website/slides/mueller2021boosting_poster.pdf
#image: assets/images/colt.png
#talk: https://iclr.cc/virtual/2021/poster/3359
---

State-of-the-art neural network verifiers are fundamentally based on one of two paradigms: encoding the whole problem via tight multi-neuron convex relaxations or applying a Branch-and-Bound (BaB) procedure which leverages imprecise but fast bounds on a large number of easier subproblems. The former can better capture complex multi-neuron dependencies but sacrifices completeness due to inherent precision limits of convex relaxations. The latter enables complete verification yet becomes increasingly ineffective on larger and more challenging networks. In this work, we present a novel complete verifier which combines the strengths of both paradigms: it leverages multi-neuron relaxations and an efficient, GPU-based dual optimizer to drastically reduce the number of subproblems generated during the BaB process. An extensive evaluation demonstrates that our verifier achieves new state-of-the-art results on both established benchmarks as well as networks with significantly higher accuracy than previously considered. The latter result (up to 26% certification gains) indicates meaningful progress towards creating verifiers that can handle practically relevant networks.
