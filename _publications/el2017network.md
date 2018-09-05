---
ref: el2017network
title: Network-wide Configuration Synthesis 
authors: Ahmed El-Hassany, Petar Tsankov, Laurent Vanbever, Martin Vechev
year: 2017
venue: CAV
projects: programmable-networks
awards:
bibtex: '@inproceedings{el2017network,
  title={Network-wide configuration synthesis},
  author={El-Hassany, Ahmed and Tsankov, Petar and Vanbever, Laurent and Vechev, Martin},
  booktitle={International Conference on Computer Aided Verification},
  pages={261--281},
  year={2017},
  organization={Springer}}'
paper: https://files.sri.inf.ethz.ch/website/papers/cav17-synet.pdf
talk: https://youtu.be/dUbFWtHLTCI
slides: https://synet.ethz.ch/files/synet-lec17.pdf
---

Computer networks are hard to manage. Given a set of highlevel requirements (e.g., reachability, security), operators have to manually figure out the individual configuration of potentially hundreds of devices running complex distributed protocols so that they, collectively, compute a compatible forwarding state. Not surprisingly, operators often make mistakes which lead to downtimes.

To address this problem, we present a novel synthesis approach that automatically computes correct network configurations that comply with the operator’s requirements. We capture the behavior of existing routers along with the distributed protocols they run in stratified Datalog. Our key insight is to reduce the problem of finding correct input configurations to the task of synthesizing inputs for a stratified Datalog program.
To solve this synthesis task, we introduce a new algorithm that synthesizes inputs for stratified Datalog programs. This algorithm is applicable beyond the domain of networks.

We leverage our synthesis algorithm to construct the first network-wide configuration synthesis system, called SyNET, that support multiple interacting routing protocols (OSPF and BGP) and static routes. We show that our system is practical and can infer correct input configurations, in a reasonable amount time, for networks of realistic size (> 50 routers) that forward packets for multiple traffic classes.
