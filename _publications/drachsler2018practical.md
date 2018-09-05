---
ref: drachsler2018practical
title: Practical Concurrent Traversals in Search Trees
authors: Dana Drachsler-Cohen, Martin Vechev, and Eran Yahav
year: 2018
month: 02
venue: ACM PPoPP
projects: Research Area 1, Research Area 1
awards:
bibtex: '@inproceedings{drachsler2018practical,
  title={Practical concurrent traversals in search trees.},
  author={Drachsler-Cohen, Dana and Vechev, Martin T and Yahav, Eran},
  booktitle={PPOPP},
  pages={207--218},
  year={2018}}'
paper: https://files.sri.inf.ethz.ch/website/papers/ppopp18.pdf
talk: 
slides: 
---

Operations of concurrent objects often employ optimistic concurrency-control schemes that consist of a traversal followed by a validation step. The validation checks if concurrent mutations interfered with the traversal to determine if the operation should proceed or restart. A fundamental challenge is to discover a necessary and sufficient validation check that has to be performed to guarantee correctness.

In this paper, we show a necessary and sufficient condition for validating traversals in search trees. The condition relies on a new concept of succinct path snapshots, which are derived from and embedded in the structure of the tree. We leverage the condition to design a general lock-free membership test suitable for any search tree. We then show how to integrate the validation condition in update operations of (non-rebalancing) binary search trees, internal and external, and AVL trees. We experimentally show that our new algorithms outperform existing ones.
