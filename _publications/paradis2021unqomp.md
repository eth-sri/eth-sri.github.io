---
ref: paradis2021unqomp
title: "Unqomp: Synthesizing Uncomputation in Quantum Circuits"
authors: Anouk Paradis, Benjamin Bichsel, Samuel Steffen, Martin Vechev
year: 2021
month: 06
venue: PLDI
projects: quantum
awards:
paper: https://files.sri.inf.ethz.ch/website/papers/pldi21-unqomp.pdf
slides: https://files.sri.inf.ethz.ch/website/slides/pldi21-unqomp.pdf
code: https://github.com/eth-sri/Unqomp
---

A key challenge when writing quantum programs is the need for _uncomputation_: temporary values produced during the computation must be reset to zero before they can be safely discarded. Unfortunately, most existing quantum languages require tedious manual uncomputation, often leading to inefficient and error-prone programs.

We present Unqomp, the first procedure to automatically synthesize uncomputation in a given quantum circuit. Unqomp can be readily integrated into popular quantum languages, allowing the programmer to allocate and use temporary values analogously to classical computation, knowing they will be uncomputed by Unqomp.

Our evaluation shows that programs leveraging Unqomp are not only shorter (-19% on average), but also generate more efficient circuits (-71% gates and -19% qubits on average).
