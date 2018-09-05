---
ref: shacham2009chameleon
title: "Chameleon: Adaptive Selection of Collections"
authors: Ohad Shacham, Martin Vechev, Eran Yahav
year: 2009
venue: ACM PLDI
projects: Research Area 1, Research Area 1
awards: 
bibtex: '@inproceedings{shacham2009chameleon,
  title={Chameleon: adaptive selection of collections},
  author={Shacham, Ohad and Vechev, Martin and Yahav, Eran},
  booktitle={ACM Sigplan Notices},
  volume={44},
  number={6},
  pages={408--418},
  year={2009},
  organization={ACM}}'
paper: pldi09.pdf
talk: 
slides: 
---

Languages such as Java and C#, as well as scripting languages like Python, and Ruby, make extensive use of Collection classes. A collection implementation represents a fixed choice in the dimensions of operation time, space utilization, and synchronization. Using the collection in a manner not consistent with this fixed choice can cause significant performance degradation. In this paper, we present CHAMELEON, a low-overhead automatic tool that assists the programmer in choosing the appropriate collection implementation for her application. During program execution, CHAMELEON computes elaborate trace and heap-based metrics on collection behavior. These metrics are consumed on-thefly by a rules engine which outputs a list of suggested collection adaptation strategies. The tool can apply these corrective strategies automatically or present them to the programmer. We have implemented CHAMELEON on top of a IBM's J9 production JVM, and evaluated it over a small set of benchmarks. We show that for some applications, using CHAMELEON leads to a significant improvement of the memory footprint of the application.