---
ref: el2016sdnracer
title: "SDNRacer: Concurrency Analysis for Software-Defined Networks"
authors: Ahmed El-Hassany, Jeremie Miserez, Pavol Bielik, Laurent Vanbever, Martin Vechev  
year: 2016
venue: ACM PLDI
projects: Research Area 1, Research Area 1
awards:
bibtex: '@inproceedings{el2016sdnracer,
  title={SDNRacer: Concurrency analysis for software-defined networks},
  author={El-Hassany, Ahmed and Miserez, Jeremie and Bielik, Pavol and Vanbever, Laurent and Vechev, Martin},
  booktitle={ACM SIGPLAN Notices},
  volume={51},
  number={6},
  pages={402--415},
  year={2016},
  organization={ACM}}'
paper: https://files.sri.inf.ethz.ch/website/papers/pldi16-sdn.pdf
talk: 
slides: 
---

Concurrency violations are an important source of bugs in Software-Defined Networks (SDN), often leading to policy or invariant violations. Unfortunately, concurrency violations are also notoriously difficult to avoid, detect and debug.

This paper presents the design and the implementation of a sound and complete dynamic analyzer, SDNRacer, which can ensure a network is free of harmful errors such as data races or per-packet incoherences. SDNRacer is based on two key ingredients: (i) a precise happens-before model for SDNs that captures when events can happen concurrently, and; (ii) a set of sound, domain-specific filters that reduce the reported violations by orders of magnitude.

We evaluated SDNRacer on several real-world SDN controllers, running both reactive and proactive applications in large networks. We show that SDNRacer is practically effective: it quickly (within 30 seconds in 90% of the cases) pinpoints harmful concurrency violations (including unknown bugs) without overwhelming the user with false positives.
