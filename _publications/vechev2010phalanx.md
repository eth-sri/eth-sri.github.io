---
ref: vechev2010phalanx
title: Parallel Checking of Expressive Heap Assertions
authors: Martin Vechev, Eran Yahav and Greta Yorsh
year: 2010
venue: ACM ISMM
projects: Research Area 1, Research Area 1
awards: 
bibtex: '@inproceedings{vechev2010phalanx,
  title={Phalanx: Parallel checking of expressive heap assertions},
  author={Vechev, Martin and Yahav, Eran and Yorsh, Greta},
  booktitle={ACM Sigplan Notices},
  volume={45},
  number={8},
  pages={41--50},
  year={2010},
  organization={ACM}}'
paper: ismm2010.pdf
talk: 
slides: 
---

Unrestricted use of heap pointers makes software systems difficult to understand and to debug. To address this challenge, we developed PHALANX -- a practical framework for dynamically checking expressive heap properties such as ownership, sharing and reachability. PHALANX uses novel parallel algorithms to efficiently check a wide range of heap properties utilizing the available cores.

PHALANX runtime is implemented on top of IBM's Java production virtual machine. This has enabled us to apply our new techniques to real world software. We checked expressive heap properties in various scenarios and found the runtime support to be valuable for debugging and program understanding. Further, our experimental results on DaCapo and other benchmarks indicate that evaluating heap queries using parallel algorithms can lead to significant performance improvements, often resulting in linear speedups as the number of cores increases.

To encourage adoption by programmers, we extended an existing JML compiler to translate expressive JML assertions about the heap into their efficient implementation provided by PHALANX. To debug her program, a programmer can annotate it with expressive heap assertions in JML, that are efficiently checked by PHALANX.