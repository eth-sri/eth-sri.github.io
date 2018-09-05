---
ref: vechev2005derivation
title: CDerivation And Evaluation Of Concurrent Collectors
authors: Martin Vechev, David F. Bacon, Perry Cheng, David Grove
year: 2005
venue: ECOOP
projects: Research Area 1, Research Area 1
awards: 
bibtex: '@inproceedings{vechev2005derivation,
  title={Derivation and evaluation of concurrent collectors},
  author={Vechev, Martin T and Bacon, David F and Cheng, Perry and Grove, David},
  booktitle={European Conference on Object-Oriented Programming},
  pages={577--601},
  year={2005},
  organization={Springer}}'
paper: Vechev05Derivation.pdf
talk: 
slides: 
---

There are many algorithms for concurrent garbage collection, but they are complex to describe, verify, and implement. This has resulted in a poor understanding of the relationships between the algorithms, and has precluded systematic study and comparative evaluation. We present a single high-level, abstract concurrent garbage collection algorithm, and show how existing snapshot and incremental update collectors, can be derived from the abstract algorithm by reducing precision. We also derive a new hybrid algorithm that reduces floating garbage while terminating quickly. We have implemented a concurrent collector framework and the resulting algorithms in IBM’s J9 Java virtual machine product and compared their performance in terms of space, time, and incrementality. The results show that incremental update algorithms sometimes reduce memory requirements (on 3 of 5 benchmarks) but they also sometimes take longer due to recomputation in the termination phase (on 4 of 5 benchmarks). Our new hybrid algorithm has memory requirements similar to the incremental update collectors while avoiding recomputation in the termination phase.