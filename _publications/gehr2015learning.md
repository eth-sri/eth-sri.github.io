---
ref: gehr2015learning
title: Learning Commutativity Specifications
authors: Timon Gehr, Dimitar Dimitrov, Martin Vechev     
year: 2015
venue: CAV
projects: core
awards:
bibtex: '@inproceedings{gehr2015learning,
  title={Learning commutativity specifications},
  author={Gehr, Timon and Dimitrov, Dimitar and Vechev, Martin},
  booktitle={International Conference on Computer Aided Verification},
  pages={307--323},
  year={2015},
  organization={Springer}}'
paper: https://files.sri.inf.ethz.ch/website/papers/cav15-learning.pdf
talk: 
slides: 
---

In this work we present a new sampling-based “black box” inference approach for learning the behaviors of a library component. As an application, we focus on the problem of automatically learning commutativity specifications of data structures. This is a very challenging problem, yet important, as commutativity specifications are fundamental to program analysis, concurrency control and even lower bounds.

Our approach is enabled by three core insights: (i) type-aware sampling which drastically improves the quality of obtained examples, (ii) relevant predicate discovery critical for reducing the formula search space, and (iii) an efficient search based on weighted-set cover for finding formulas ranging over the predicates and capturing the examples.

More generally, our work learns formulas belonging to fragments consisting of quantifier-free formulas over a finite number of relation symbols. Such fragments are expressive enough to capture useful specifications
(e.g., commutativity) yet are amenable to automated inference.

We implemented a tool based on our approach and have shown that it can quickly learn non-trivial and important commutativity specifications of fundamental data types such as hash maps, sets, array lists, union find and others. We also showed experimentally that learning these specifications is beyond the capabilities of existing techniques.
