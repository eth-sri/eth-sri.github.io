---
ref: raman2010efficient
title: Efficient Data Race Detection for Async-Finish Parallelism
authors: Raghavan Raman, Jisheng Zhao, Vivek Sarkar, Martin Vechev and Eran Yahav      
year: 2010
venue: Runtime Verification (RV)
projects: Research Area 1, Research Area 1
awards: Best Paper Award
bibtex: '@inproceedings{raman2010efficient,
  title={Efficient data race detection for async-finish parallelism},
  author={Raman, Raghavan and Zhao, Jisheng and Sarkar, Vivek and Vechev, Martin and Yahav, Eran},
  booktitle={International Conference on Runtime Verification},
  pages={368--383},
  year={2010},
  organization={Springer}}'
paper: rv2010.pdf
talk: 
slides: 
---

A major productivity hurdle for parallel programming is the presence of data races. Data races can lead to all kinds of harmful program behaviors, including determinism violations and corrupted memory. However, runtime overheads of current dynamic data race detectors are still prohibitively large (often incurring slowdowns of 10× or larger) for use in mainstream software development.

In this paper, we present an efficient dynamic race detector algorithm targeting the async-finish task-parallel parallel programming model. The async and finish constructs are at the core of languages such as X10 and Habanero Java (HJ). These constructs generalize the spawn-sync constructs used in Cilk, while still ensuring that all computation graphs are deadlock-free.

We have implemented our algorithm in a tool called TaskChecker and evaluated it on a suite of 12 benchmarks. To reduce overhead of the dynamic analysis, we have also implemented various static optimizations in the tool. Our experimental results indicate that our approach performs well in practice, incurring an average slowdown of 3.05× compared to a serial execution in the optimized case.