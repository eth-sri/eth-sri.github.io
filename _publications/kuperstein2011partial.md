---
ref: kuperstein2011partial
title: Partial-Coherence Abstractions for Relaxed Memory Models
authors: Michael Kuperstein, Martin Vechev and Eran Yahav  
year: 2011
venue: ACM PLDI
projects: fender
awards:
bibtex: '@inproceedings{kuperstein2011partial,
  title={Partial-coherence abstractions for relaxed memory models},
  author={Kuperstein, Michael and Vechev, Martin and Yahav, Eran},
  booktitle={ACM SIGPLAN Notices},
  volume={46},
  number={6},
  pages={187--198},
  year={2011},
  organization={ACM}}'
paper: https://files.sri.inf.ethz.ch/website/papers/pldi11.pdf
talk: 
slides: http://practicalsynthesis.github.io/papers/PLDI2011-slides.pptx
---

We present an approach for automatic verification and fence inference in concurrent programs running under relaxed memory models. Verification under relaxed memory models is a hard problem. Given a finite state program and a safety specification, verifying that the program satisfies the specification under a sufficiently relaxed memory model is undecidable. For stronger models, the problem is decidable but has non-primitive recursive complexity.

In this paper, we focus on models that have store-buffer based semantics, e.g., SPARC TSO and PSO. We use abstract interpretation to provide an effective verification procedure for programs running under this type of models. Our main contribution is a family of novel partial-coherence abstractions, specialized for relaxed memory models, which partially preserve information required for memory coherence and consistency. We use our abstractions to automatically verify programs under relaxed memory models. In addition, when a program violates its specification but can be fixed by adding fences, our approach can automatically infer a correct fence placement that is optimal under the abstraction. We implemented our approach in a tool called BLENDER and applied it to verify and infer fences in several concurrent algorithms.
