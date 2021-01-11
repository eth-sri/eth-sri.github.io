---
ref: birkner2020config2spec
title: "Config2Spec: Mining Network Specifications from Network Configurations"
authors: Rüdiger Birkner, Dana Drachsler-Cohen, Laurent Vanbever, Martin Vechev
year: 2020
month: 02
venue: NSDI
projects: programmable-networks
awards: 2021 IETF/IRTF Applied Networking Research Prize
bibtex: '@inproceedings{birkner2020config2spec,
  title={Config2Spec: Mining Network Specifications from Network Configurations},
  author={Birkner, R{\"u}diger and Drachsler-Cohen, Dana and Vanbever, Laurent and Vechev, Martin},
  booktitle={17th $\{$USENIX$\}$ Symposium on Networked Systems Design and Implementation ($\{$NSDI$\}$ 20)},
  year={2020},
  organization={USENIX$\}$ Association}}'
paper: https://files.sri.inf.ethz.ch/website/papers/nsdi20.pdf
talk: 
slides: 
---

Network verification and configuration synthesis are promising approaches to make networks more reliable and secure by enforcing a set of policies. However, these approaches require a formal and precise description of the intended network behavior, imposing a major barrier to their adoption: network operators are not only reluctant to write formal specifications, but often do not even know what these specifications are.

We present Config2Spec, a system that automatically synthesizes a formal specification (a set of policies) of a network given its configuration and a failure model (e.g., up to two link failures). A key technical challenge is to design a synthesis algorithm which can efficiently explore the large space of possible policies. To address this challenge, Config2Spec relies on a careful combination of two well-known methods: data plane analysis and control plane verification.

Experimental results show that Config2Spec scales to mining specifications of large networks (>150 routers).
