---
ref: brutschy2018static
title: Static Serializability Analysis for Causal Consistency
authors: Lucas Brutschy, Dimitar Dimitrov, Peter Müller, Martin Vechev
year: 2018
month: 06
venue: PLDI
projects: "CORE: Foundations of practical concurrency analysis"
awards:
bibtex: '@inproceedings{brutschy2018static,
  title={Static serializability analysis for causal consistency},
  author={Brutschy, Lucas and Dimitrov, Dimitar and M{\"u}ller, Peter and Vechev, Martin},
  booktitle={Proceedings of the 39th ACM SIGPLAN Conference on Programming Language Design and Implementation},
  pages={90--104},
  year={2018},
  organization={ACM}}'
paper: c4-pldi2018.pdf
talk: 
slides: 
---

Many distributed databases provide only weak consistency guarantees to reduce synchronization overhead and remain available under network partitions. However, this leads to behaviors not possible under stronger guarantees. Such behaviors can easily defy programmer intuition and lead to errors that are notoriously hard to detect.

In this paper, we propose a static analysis for detecting non-serializable behaviors of applications running on top of causally-consistent databases. Our technique is based on a novel, local serializability criterion and combines a generalization of graph-based techniques from the database literature with another, complementary analysis technique that encodes our serializability criterion into first-order logic formulas to be checked by an SMT solver. This analysis is more expensive yet more precise and produces concrete counterexamples.

We implemented our methods and evaluated them on a number of applications from two different domains: cloudbacked mobile applications and clients of a distributed database. Our experiments demonstrate that our analysis is able to detect harmful serializability violations while producing only a small number of false alarms.
