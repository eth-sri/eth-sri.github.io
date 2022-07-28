---
ref: bichsel2020silq
title: "Silq: A High-Level Quantum Language with Safe Uncomputation and Intuitive Semantics"
authors: Benjamin Bichsel, Maximilian Baader, Timon Gehr, Martin Vechev
year: 2020
month: 06
venue: PLDI
projects: quantum
awards:
bibtex: '@inproceedings{bichsel2020silq,
	title = {Silq: {A} {High}-{Level} {Quantum} {Language} with {Safe} {Uncomputation} and {Intuitive} {Semantics}},
	isbn = {978-1-4503-7613-6},
	url = {https://dl.acm.org/doi/10.1145/3385412.3386007},
	doi = {10.1145/3385412.3386007},
	booktitle = {Proceedings of the 41st {ACM} {SIGPLAN} {Conference} on {Programming} {Language} {Design} and {Implementation}},
	publisher = {ACM},
	author = {Bichsel, Benjamin and Baader, Maximilian and Gehr, Timon and Vechev, Martin},
	month = jun,
	year = {2020}
}
'
<!--blogpost: silq-->
paper: https://files.sri.inf.ethz.ch/website/papers/pldi20-silq.pdf
code: https://github.com/eth-sri/silq
---

Existing quantum languages force the programmer to work at a low level of abstraction leading to unintuitive and cluttered code. A fundamental reason is that dropping temporary values from the program state requires explicitly applying quantum operations that safely uncompute these values.

We present Silq, the first quantum language that addresses this challenge by supporting safe, automatic uncomputation. This enables an intuitive semantics that implicitly drops temporary values, as in classical computation. To ensure physicality of Silq's semantics, its type system leverages novel annotations to reject unphysical programs.

Our experimental evaluation demonstrates that Silq programs are not only easier to read and write, but also significantly shorter than equivalent programs in other quantum languages (on average -46% for Q#, -38% for Quipper), while using only half the number of quantum primitives.
