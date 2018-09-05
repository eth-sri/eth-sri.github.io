---
ref: el2018netcomplete
title: "NetComplete: Practical Network-Wide Configuration Synthesis with Autocompletion"
authors: Ahmed El-Hassany, Petar Tsankov, Laurent Vanbever, Martin Vechev
year: 2018
month: 04
venue: NSDI
projects: programmable-networks
awards:
bibtex: '@inproceedings{el2018netcomplete,
  title={NetComplete: Practical Network-Wide Configuration Synthesis with Autocompletion},
  author={El-Hassany, Ahmed and Tsankov, Petar and Vanbever, Laurent and Vechev, Martin},
  booktitle={15th $\{$USENIX$\}$ Symposium on Networked Systems Design and Implementation ($\{$NSDI$\}$ 18)},
  year={2018},
  organization={USENIX$\}$ Association$\}$}}'
paper: https://files.sri.inf.ethz.ch/website/papers/netcomplete-nsdi18.pdf
talk: https://www.youtube.com/watch?v=zYgvQ0PtSLM
slides: 
---

Network operators often need to adapt the configuration of a network in order to comply with changing routing policies. Evolving existing configurations, however, is a complex task as local changes can have unforeseen global effects. Not surprisingly, this often leads to mistakes that result in network downtimes.

We present NetComplete, a system that assists operators in modifying existing network-wide configurations to comply with new routing policies. NetComplete takes as input configurations with “holes” that identify the parameters to be completed and “autocompletes” these with concrete values. The use of a partial configuration addresses two important challenges inherent to existing synthesis solutions: (i) it allows the operators to precisely control how configurations should be changed; and (ii) it allows the synthesizer to leverage the existing configurations to gain performance. To scale, NetComplete relies on powerful techniques such as counter-example guided inductive synthesis (for link-state protocols) and partial evaluation (for path-vector protocols).

We implemented NetComplete and showed that it can autocomplete configurations using static routes, OSPF, and BGP. Our implementation also scales to realistic networks and complex routing policies. Among others, it is able to synthesize configurations for networks with up to 200 routers within few minutes.
