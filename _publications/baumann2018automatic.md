---
ref: baumann2018automatic
title: Automatic Verification of RMA Programs via Abstraction Extrapolation 
authors: Cedric Baumann, Andrei Marian Dan, Yuri Meshman, Torsten Hoefler, Martin Vechev
year: 2018
month: 01
venue: VMCAI
projects: fender
awards:
bibtex: '@inproceedings{baumann2018automatic,
  title={Automatic Verification of RMA Programs via Abstraction Extrapolation},
  author={Baumann, Cedric and Dan, Andrei Marian and Meshman, Yuri and Hoefler, Torsten and Vechev, Martin},
  booktitle={International Conference on Verification, Model Checking, and Abstract Interpretation},
  pages={47--70},
  year={2018},
  organization={Springer}}'
paper: https://files.sri.inf.ethz.ch/website/papers/vmcai18.pdf
talk: 
slides: http://practicalsynthesis.github.io/papers/slides-vmcai18.pdf
---

Remote Memory Access (RMA) networks are emerging as a promising basis for building performant large-scale systems such as MapReduce, scientific computing applications, and others. To achieve this performance, RMA networks exhibit relaxed memory consistency. This means the developer now must manually ensure that the additional relaxed behaviors are not harmful to their application – a task known to be difficult and error-prone. In this paper, we present a method and a system that can automatically address this task. Our approach consists of two ingredients: (i) a reduction where we reduce the task of verifying program P running on RMA to the problem of verifying a program P on sequential consistency (where P captures the required RMA behaviors), and (ii) abstraction extrapolation: a new method to automatically discover both, predicates (via predicate extrapolation) and abstract transformers (via boolean program extrapolation) for P. This enables us to automatically extrapolate the proof of P under sequential consistency (SC) to a proof of P under RMA. We implemented our method and showed it to be effective in automatically verifying, for the first time, several challenging concurrent algorithms under RMA.
