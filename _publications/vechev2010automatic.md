---
ref: vechev2010automatic
title: Automatic Verification of Determinism for Structured Parallel Programs 
authors: Martin Vechev, Eran Yahav, Raghavan Raman and Vivek Sarkar       
year: 2010
venue: Static Analysis Symposium (SAS)
projects: Research Area 1, Research Area 1
awards: 
bibtex: '@inproceedings{vechev2010automatic,
  title={Automatic verification of determinism for structured parallel programs},
  author={Vechev, Martin and Yahav, Eran and Raman, Raghavan and Sarkar, Vivek},
  booktitle={International Static Analysis Symposium},
  pages={455--471},
  year={2010},
  organization={Springer}}'
paper: SAS%202010%20-%20Determinism.pdf
talk: 
slides: 
---

We present a static analysis for automatically verifying determinism of structured parallel programs. The main idea is to leverage the structure of the program to reduce determinism verification to an independence property that can be proved using a simple sequential analysis. Given a task-parallel program, we identify program fragments that may execute in parallel and check that these fragments perform independent memory accesses using a sequential analysis. Since the parts that can execute in parallel are typically only a small fraction of the program, we can employ powerful numerical abstractions to establish that tasks executing in parallel only perform independent memory accesses. We have implemented our analysis in a tool called Dice and successfully applied it to verify determinism on a suite of benchmarks derived from those used in the high-performance computing community.