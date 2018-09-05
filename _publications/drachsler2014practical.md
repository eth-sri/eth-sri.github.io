---
ref: drachsler2014practical
title: Practical Concurrent Binary Search Trees via Logical Ordering 
authors: Dana Drachsler, Martin Vechev and Eran Yahav 
year: 2014
venue: ACM PPoPP
projects: Research Area 1, Research Area 1
awards:
bibtex: 
paper: https://files.sri.inf.ethz.ch/website/papers/ppopp14-logicalavl.pdf
talk: 
slides: 
---

We present practical, concurrent binary search tree (BST) algorithms that explicitly maintain logical ordering information in the data structure, permitting clean separation from its physical tree layout. We capture logical ordering using intervals, with the property that an item belongs to the tree if and only if the item is an endpoint of some interval. We are thus able to construct efficient, synchronization-free and
intuitive lookup operations.

We present (i) a concurrent non-balanced BST with a lock-free lookup, and (ii) a concurrent AVL tree with a lock-free lookup that requires no synchronization with any mutating operations, including balancing operations. Our algorithms apply on-time deletion; that is, every request for removal of a node, results in its immediate removal from the tree. This new feature did not exist in previous concurrent internal tree algorithms.

We implemented our concurrent BST algorithms and evaluated them against several state-of-the-art concurrent tree algorithms. Our experimental results show that our algorithms with lock-free contains and on-time deletion are practical and often comparable to the state-of-the-art.
