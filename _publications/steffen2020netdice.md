---
  ref: steffen20netdice
  title: "Probabilistic Verification of Network Configurations"
  authors: Samuel Steffen, Timon Gehr, Petar Tsankov, Laurent Vanbever, Martin Vechev
  year: 2020
  month: 8
  venue: ACM SIGCOMM
  projects: programmable-networks
  awards: Best Student Paper Award
  bibtex:
  paper: https://files.sri.inf.ethz.ch/website/papers/sigcomm20-netdice.pdf
  image: 
  talk:
  slides:
---

Not all important network properties need to be enforced all the time. Often, what matters instead is the fraction of time / probability these properties hold. Computing the probability of a property in a network relying on complex inter-dependent routing protocols is challenging and requires determining all failure scenarios for which the property is violated. Doing so at scale and accurately goes beyond the capabilities of current network analyzers.

In this paper, we introduce NetDice, the first scalable and accurate probabilistic network configuration analyzer supporting BGP, OSPF, ECMP, and static routes. Our key contribution is an inference algorithm to efficiently explore the space of failure scenarios. More specifically, given a network configuration and a property phi, our algorithm automatically identifies a set of links whose failure is provably guaranteed not to change whether phi holds. By pruning these failure scenarios, NetDice manages to accurately approximate P(phi). NetDice supports practical properties and expressive failure models including correlated link failures.

We implement NetDice and evaluate it on realistic configurations. NetDice is practical: it can precisely verify probabilistic properties in few minutes, even in large networks.
