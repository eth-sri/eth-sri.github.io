---
ref: vechev2010abstraction
title: Abstraction-Guided Synthesis Of Synchronization
authors: Martin Vechev, Eran Yahav and Greta Yorsh
year: 2010
venue: ACM POPL
projects: Research Area 1, Research Area 1
awards: 
bibtex: '@inproceedings{vechev2010abstraction,
  title={Abstraction-guided synthesis of synchronization},
  author={Vechev, Martin and Yahav, Eran and Yorsh, Greta},
  booktitle={ACM Sigplan Notices},
  volume={45},
  number={1},
  pages={327--338},
  year={2010},
  organization={ACM}}'
paper: https://files.sri.inf.ethz.ch/website/papers/popl10.pdf
talk: 
slides: 
---

We present a novel framework for automatic inference of efficient synchronization in concurrent programs, a task known to be difficult and error-prone when done manually.

Our framework is based on abstract interpretation and can infer synchronization for infinite state programs. Given a program, a specification, and an abstraction, we infer synchronization that avoids all (abstract) interleavings that may violate the specification, but permits as many valid interleavings as possible.

Combined with abstraction refinement, our framework can be viewed as a new approach for verification where both the program and the abstraction can be modified on-the-fly during the verification process. The ability to modify the program, and not only the abstraction, allows us to remove program interleavings not only when they are known to be invalid, but also when they cannot be verified using the given abstraction.

We implemented a prototype of our approach using numerical abstractions and applied it to verify several interesting programs.
