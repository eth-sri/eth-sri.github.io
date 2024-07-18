---
ref: venev2024modular
title: "Modular Synthesis of Efficient Quantum Uncomputation"
authors: Hristo Venev, Timon Gehr, Dimitar Dimitrov, Martin Vechev
year: 2024
month: 06
venue: ACM OOPSLA
projects: quantum
awards:
bibtex: '@misc{venev2024modular,
      title={Modular Synthesis of Efficient Quantum Uncomputation}, 
      author={Hristo Venev and Timon Gehr and Dimitar Dimitrov and Martin Vechev},
      year={2024},
      eprint={2406.14227},
      archivePrefix={arXiv},
      primaryClass={cs.PL},
      url={https://arxiv.org/abs/2406.14227}, 
}'
paper: https://arxiv.org/abs/2406.14227
---

A key challenge of quantum programming is uncomputation: the reversible deallocation of qubits. And while there has been much recent progress on automating uncomputation, state-of-the-art methods are insufficient for handling today's expressive quantum programming languages. A core reason is that they operate on primitive quantum circuits, while quantum programs express computations beyond circuits, for instance, they can capture families of circuits defined recursively in terms of uncomputation and adjoints.
In this paper, we introduce the first modular automatic approach to synthesize correct and efficient uncomputation for expressive quantum programs. Our method is based on two core technical contributions: (i) an intermediate representation (IR) that can capture expressive quantum programs and comes with support for uncomputation, and (ii) modular algorithms over that IR for synthesizing uncomputation and adjoints.
We have built a complete end-to-end implementation of our method, including an implementation of the IR and the synthesis algorithms, as well as a translation from an expressive fragment of the Silq programming language to our IR and circuit generation from the IR. Our experimental evaluation demonstrates that we can handle programs beyond the capabilities of existing uncomputation approaches, while being competitive on the benchmarks they can handle. More broadly, we show that it is possible to benefit from the greater expressivity and safety offered by high-level quantum languages without sacrificing efficiency.
