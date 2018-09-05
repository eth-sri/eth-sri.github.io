---
ref: miserez2015sdnracer
title: "SDNRacer: Detecting Concurrency Violations in Software-Defined Networks"
authors: Jeremie Miserez, Pavol Bielik, Ahmed El-Hassany, Laurent Vanbever, Martin Vechev      
year: 2015
venue: SOSR
projects: Research Area 1, Research Area 1
awards:
bibtex: '@inproceedings{miserez2015sdnracer,
  title={SDNRacer: detecting concurrency violations in software-defined networks},
  author={Miserez, Jeremie and Bielik, Pavol and El-Hassany, Ahmed and Vanbever, Laurent and Vechev, Martin},
  booktitle={Proceedings of the 1st ACM SIGCOMM Symposium on Software Defined Networking Research},
  pages={22},
  year={2015},
  organization={ACM}}'
paper: SOSR15-SDNRacer.pdf
talk: 
slides: 
---

Software-Defined Networking (SDN) control software executes in highly asynchronous environments where unexpected concurrency errors can lead to performance or, worse, reachability errors. Unfortunately, detecting such errors is notoriously challenging, and SDN is no exception.

Fundamentally, two ingredients are needed to build a concurrency analyzer: (i) a model of how different events are ordered, and (ii) the memory locations on which event accesses can interfere. In this paper we formulate the first happens-before (HB) model for SDNs enabling one to reason about ordering between events. We also present a commutativity specification of the network switch, allowing us to elegantly capture interference between concurrent events.

Based on the above, we present the first dynamic concurrency analyzer for SDNs, called SDNRACER. SDNRACER uses the HB model and the commutativity rules to identify concurrency violations. Preliminary results indicate that the detector is practically effective—it can detect harmful violations quickly.