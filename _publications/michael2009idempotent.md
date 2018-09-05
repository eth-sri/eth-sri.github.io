---
ref: michael2009idempotent
title: Idempotent Work Stealing
authors: Maged Michael, Martin Vechev, Vijay Saraswat
year: 2009
venue: ACM PPoPP
projects: Research Area 1, Research Area 1
awards: 
bibtex: '@book{michael2009idempotent,
  title={Idempotent work stealing},
  author={Michael, Maged M and Vechev, Martin T and Saraswat, Vijay A},
  volume={44},
  number={4},
  year={2009},
  publisher={ACM}}'
paper: https://files.sri.inf.ethz.ch/website/papers/idempotentWSQ09.pdf
talk: 
slides: 
---

Load balancing is a technique which allows efficient parallelization of irregular workloads, and a key component of many applications and parallelizing runtimes. Work-stealing is a popular technique for implementing load balancing, where each parallel thread maintains its own work set of items and occasionally steals items from the sets of other threads.

The conventional semantics of work stealing guarantee that each inserted task is eventually extracted exactly once. However, correctness of a wide class of applications allows for relaxed semantics, because either: i) the application already explicitly checks that no work is repeated or ii) the application can tolerate repeated work.

In this paper, we introduce idempotent work tealing, and present several new algorithms that exploit the relaxed semantics to deliver better performance. The semantics of the new algorithms guarantee that each inserted task is eventually extracted at least once-instead of exactly once.

On mainstream processors, algorithms for conventional work stealing require special atomic instructions or store-load memory ordering fence instructions in the owner's critical path operations. In general, these instructions are substantially slower than regular memory access instructions. By exploiting the relaxed semantics, our algorithms avoid these instructions in the owner's operations.

We evaluated our algorithms using common graph problems and micro-benchmarks and compared them to well-known conventional work stealing algorithms, the THE Cilk and Chase-Lev algorithms. We found that our best algorithm (with LIFO extraction) outperforms existing algorithms in nearly all cases, and often by significant margins.
