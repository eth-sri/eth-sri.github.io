---
ref: raman2012scalable
title: Scalable and Precise Dynamic Datarace Detection for Structured Parallelism
authors: Raghavan Raman, Jisheng Zhao, Vivek Sarkar, Martin Vechev, Eran Yahav 
year: 2012
venue: ACM PLDI
projects: Research Area 1, Research Area 1
awards:
bibtex: '@article{raman2012scalable,
  title={Scalable and precise dynamic datarace detection for structured parallelism},
  author={Raman, Raghavan and Zhao, Jisheng and Sarkar, Vivek and Vechev, Martin and Yahav, Eran},
  journal={Acm Sigplan Notices},
  volume={47},
  number={6},
  pages={531--542},
  year={2012},
  publisher={ACM}}'
paper: pldi12-spd3.pdf
talk: 
slides: 
---

Existing dynamic race detectors suffer from at least one of the following three limitations:

(i) space overhead per memory location grows linearly with the number of parallel threads [13], severely limiting the parallelism that the algorithm can handle.

(ii) sequentialization: the parallel program must be processed in a sequential order, usually depth-first [12, 24]. This prevents the analysis from scaling with available hardware parallelism, inherently limiting its performance.

(iii) inefficiency: even though race detectors with good theoretical complexity exist, they do not admit efficient implementations and are unsuitable for practical use [4, 18].

We present a new precise dynamic race detector that leverages structured parallelism in order to address these limitations. Our algorithm requires constant space per memory location, works in parallel, and is efficient in practice. We implemented and evaluated our algorithm on a set of 15 benchmarks. Our experimental results indicate an average (geometric mean) slowdown of 2.78× on a 16-core SMP system.