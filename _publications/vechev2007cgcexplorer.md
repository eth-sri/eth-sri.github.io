---
ref: vechev2007cgcexplorer
title: "CGCExplorer: A Semi-Automated Search Procedure for Provably Correct Concurrent Collectors"
authors: Martin Vechev, Eran Yahav, David F. Bacon and Noam Rinetzky
year: 2007
venue: ACM PLDI
projects: Research Area 1, Research Area 1
awards: 
bibtex: '@inproceedings{vechev2007cgcexplorer,
  title={CGCExplorer: a semi-automated search procedure for provably correct concurrent collectors},
  author={Vechev, Martin T and Yahav, Eran and Bacon, David F and Rinetzky, Noam},
  booktitle={ACM SIGPLAN Notices},
  volume={42},
  number={6},
  pages={456--467},
  year={2007},
  organization={ACM}}'
paper: pldi07-cgc.pdf
talk: 
slides: 
---

Concurrent garbage collectors are notoriously hard to design, implement, and verify. We present a framework for the automatic exploration of a space of concurrent mark-and-sweep collectors. In our framework, the designer specifies a set of "building blocks" from which algorithms can be constructed. These blocks reflect the designer's insights about the coordination between the collector and the mutator. Given a set of building blocks, our framework automatically explores a space of algorithms, using model checking with abstraction to verify algorithms in the space.

We capture the intuition behind some common mark-and-sweep algorithms using a set of building blocks. We utilize our framework to automatically explore a space of more than 1,600,000 algorithms built from these blocks, and derive over 100 correct fine-grained algorithms with various space, synchronization, and precision tradeoffs.