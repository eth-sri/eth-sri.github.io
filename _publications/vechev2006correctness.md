---
ref: vechev2006correctness
title: Correctness-Preserving Derivation of Concurrent Garbage Collection Algorithms
authors: Martin Vechev, Eran Yahav, David F. Bacon
year: 2006
venue: ACM PLDI
projects: Research Area 1, Research Area 1
awards: 
bibtex: '@inproceedings{vechev2006correctness,
  title={Correctness-preserving derivation of concurrent garbage collection algorithms},
  author={Vechev, Martin T and Yahav, Eran and Bacon, David F},
  booktitle={ACM SIGPLAN Notices},
  volume={41},
  number={6},
  pages={341--353},
  year={2006},
  organization={ACM}}'
paper: pldi06-cgc.pdf
talk: 
slides: 
---

Constructing correct concurrent garbage collection algorithms is notoriously hard. Numerous such algorithms have been proposed, implemented, and deployed - and yet the relationship among them in terms of speed and precision is poorly understood, and the validation of one algorithm does not carry over to others.As programs with low latency requirements written in garbagecollected languages become part of society's mission-critical infrastructure, it is imperative that we raise the level of confidence in the correctness of the underlying system, and that we understand the trade-offs inherent in our algorithmic choice.In this paper we present correctness-preserving transformations that can be applied to an initial abstract concurrent garbage collection algorithm which is simpler, more precise, and easier to prove correct than algorithms used in practice--but also more expensive and with less concurrency. We then show how both pre-existing and new algorithms can be synthesized from the abstract algorithm by a series of our transformations. We relate the algorithms formally using a new definition of precision, and informally with respect to overhead and concurrency.This provides many insights about the nature of concurrent collection, allows the direct synthesis of new and useful algorithms, reduces the burden of proof to a single simple algorithm, and lays the groundwork for the automated synthesis of correct concurrent collectors.