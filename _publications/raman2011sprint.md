---
ref: raman2011sprint
title: "Sprint: Speculative Prefetching of Remote Data"
authors: Arun Raman, Greta Yorsh, Martin Vechev and Eran Yahav     
year: 2011
venue: ACM OOPSLA
projects: Research Area 1, Research Area 1
awards:
bibtex: '@article{raman2011sprint,
  title={Sprint: speculative prefetching of remote data},
  author={Raman, Arun and Yorsh, Greta and Vechev, Martin and Yahav, Eran},
  journal={ACM SIGPLAN Notices},
  volume={46},
  number={10},
  pages={259--274},
  year={2011},
  publisher={ACM}}'
paper: https://files.sri.inf.ethz.ch/website/papers/oopsla11-prefetch.pdf
talk: 
slides: 
---

Remote data access latency is a significant performance bottleneck in many modern programs that use remote databases and web services. We present Sprint - a run-time system for optimizing such programs by prefetching and caching data from remote sources in parallel to the execution of the original program. Sprint separates the concerns of exposing potentially-independent data accesses from the mechanism for executing them efficiently in parallel or in a batch. In contrast to prior work, Sprint can efficiently prefetch data in the presence of irregular or input-dependent access patterns, while preserving the semantics of the original program.

We used Sprint to automatically improve the performance of several real-world Java programs that access remote databases (MySQL, DB2) and web services (Facebook, IBM's Yellow Pages). Sprint achieves speedups ranging 2.4x to 15.8x over sequential execution, which are comparable to those achieved by manually modifying the program for asynchronous and batch execution of data accesses. Sprint provides a simple interface that allows a programmer to plug in support for additional data sources without modifying the client program.
