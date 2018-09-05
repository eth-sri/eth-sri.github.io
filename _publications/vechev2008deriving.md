---
ref: vechev2008deriving
title: "Position Paper: Computer-Assisted Construction of Efficient Concurrent Algorithms"
authors: Martin Vechev and Eran Yahav
year: 2008
venue: ACM PLDI
projects: Research Area 1, Research Area 1
awards: 
bibtex: '@article{vechev2008deriving,
  title={Deriving linearizable fine-grained concurrent objects},
  author={Vechev, Martin and Yahav, Eran},
  journal={ACM SIGPLAN Notices},
  volume={43},
  number={6},
  pages={125--135},
  year={2008},
  publisher={ACM}}'
paper: https://files.sri.inf.ethz.ch/website/papers/pldi08.pdf
talk: 
slides: 
---

Practical and efficient algorithms for concurrent data structures are difficult to construct and modify. Algorithms in the literature are often optimized for a specific setting, making it hard to separate the algorithmic insights from implementation details. The goal of this work is to systematically construct algorithms for a concurrent data structure starting from its sequential implementation. Towards that goal, we follow a construction process that combines manual steps corresponding to high-level insights with automatic exploration of implementation details. To assist us in this process, we built a new tool called Paraglider. The tool quickly explores large spaces of algorithms and uses bounded model checking to check linearizability of algorithms.

Starting from a sequential implementation and assisted by the tool, we present the steps that we used to derive various highly-concurrent algorithms. Among these algorithms is a new fine-grained set data structure that provides a wait-free contains operation, and uses only the compare-and-swap (CAS) primitive for synchronization.
