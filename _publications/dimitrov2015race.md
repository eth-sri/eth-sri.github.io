---
ref: dimitrov2015race
title: Race Detection in Two Dimensions
authors: Dimitar Dimitrov, Martin Vechev, Vivek Sarkar       
year: 2015
venue: ACM SPAA
projects: core
awards:
bibtex: '@inproceedings{dimitrov2015race,
  title={Race detection in two dimensions},
  author={Dimitrov, Dimitar and Vechev, Martin and Sarkar, Vivek},
  booktitle={Proceedings of the 27th ACM Symposium on Parallelism in Algorithms and Architectures},
  pages={101--110},
  year={2015},
  organization={ACM}}'
paper: https://files.sri.inf.ethz.ch/website/papers/spaa15-twodim.pdf
talk: 
slides: 
---

Dynamic data race detection is a program analysis technique for detecting errors provoked by undesired interleavings of concurrent threads. A primary challenge when designing efficient race detection algorithms is to achieve manageable space requirements.

State of the art algorithms for unstructured parallelism require Θ(n) space per monitored memory location, where n is the total number of tasks. This is a serious drawback when analyzing programs with many tasks. In contrast, algorithms for programs with a series-parallel (SP) structure require only Θ(1) space. Unfortunately, it is currently poorly understood if there are classes of parallelism beyond SP that can also
benefit from and be analyzed with Θ(1) space complexity.

In the present work, we show that structures richer than SP graphs, namely that of two-dimensional (2D) lattices, can be analyzed in Θ(1) space: a) we extend Tarjan’s algorithm for finding lowest common ancestors to handle 2D lattices; b) from that extension we derive a serial algorithm for race detection that can analyze arbitrary task graphs having a 2D lattice structure; c) we present a restriction to fork-join that admits precisely the 2D lattices as task graphs (e.g., it can express pipeline parallelism).

Our work generalizes prior work on race detection, and aims to provide a deeper understanding of the interplay between structured parallelism and program analysis efficiency.
