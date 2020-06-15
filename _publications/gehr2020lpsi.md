---
ref: gehr2020lpsi
title: "λPSI: Exact Inference for Higher-order Probabilistic Programs"
authors: Timon Gehr, Samuel Steffen, Martin Vechev
year: 2020
month: 06
venue: PLDI
projects: probabilistic-programming
awards:
bibtex: '@inproceedings{gehr_lpsi_2020,
	title = {$\lambda$PSI: {Exact} {Inference} {for} {Higher-order} {Probabilistic} {Programs}},
	isbn = {978-1-4503-7613-6},
	url = {https://dl.acm.org/doi/10.1145/3385412.3386006},
	doi = {10.1145/3385412.3386006},
	booktitle = {Proceedings of the 41st {ACM} {SIGPLAN} {Conference} on {Programming} {Language} {Design} and {Implementation}},
	publisher = {ACM},
	author = {Gehr, Timon and Steffen, Samuel and Vechev, Martin},
	month = jun,
	year = {2020}
}
'
paper: https://files.sri.inf.ethz.ch/website/papers/pldi20-lpsi.pdf
---

We present λPSI, the first probabilistic programming language and system that supports higher-order exact inference for probabilistic programs with first-class functions, nested inference and discrete, continuous and mixed random variables. λPSI’s solver is based on symbolic reasoning and computes the exact distribution represented by a program.

We show that λPSI is practically effective—it automatically computes exact distributions for a number of interesting applications, from rational agents to information theory, many of which could so far only be handled approximately.
