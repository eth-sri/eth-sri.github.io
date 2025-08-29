---
ref: meshman2014synthesis
title: Synthesis of Memory Fences via Refinement Propagation 
authors: Yuri Meshman, Andrei Dan, Martin Vechev, Eran Yahav          
year: 2014
venue: SAS
projects: fender
awards:
bibtex: '@inproceedings{meshman2014synthesis,
  title={Synthesis of memory fences via refinement propagation},
  author={Meshman, Yuri and Dan, Andrei and Vechev, Martin and Yahav, Eran},
  booktitle={International Static Analysis Symposium},
  pages={237--252},
  year={2014},
  organization={Springer}}'
paper: https://files.sri.inf.ethz.ch/website/papers/sas14-smfrp.pdf
talk: 
slides: http://practicalsynthesis.github.io/papers/sas14-slides.pptx
---

We address the problem of fence inference in infinite-state concurrent programs running on relaxed memory models such as TSO and PSO. We present a novel algorithm that can automatically synthesize the necessary fences for infinite-state programs.

Our technique is based on two main ideas: (i) verification with numerical domains: we reduce verification under relaxed models to verification under sequential consistency using integer and boolean variables. This enables us to combine abstraction refinement over booleans with powerful numerical abstractions over the integers. (ii) synthesis with refinement propagation: to synthesize fences for a program P, we combine abstraction refinements used for successful synthesis of programs coarser than P into a new candidate abstraction for P. This “proof reuse” approach dramatically reduces the time required to discover a proof for P. We implemented our technique and successfully applied it to several challenging concurrent algorithms, including state of the art concurrent work-stealing queues.
