---
ref: birkner2018net2text
title: "Net2Text: Query-Guided Summarization of Network Forwarding Behaviors"
authors: Rüdiger Birkner, Dana Drachsler-Cohen, Laurent Vanbever, Martin Vechev
year: 2018
month: 04
venue: NSDI
projects: programmable-networks
awards:
bibtex: '@inproceedings{birkner2018net2text,
  title={Net2Text: Query-Guided Summarization of Network Forwarding Behaviors},
  author={Birkner, R{\"u}diger and Drachsler-Cohen, Dana and Vanbever, Laurent and Vechev, Martin},
  booktitle={15th $\{$USENIX$\}$ Symposium on Networked Systems Design and Implementation ($\{$NSDI$\}$ 18)},
  year={2018},
  organization={USENIX$\}$ Association}}'
paper: https://files.sri.inf.ethz.ch/website/papers/nsdi18.pdf
talk: https://www.youtube.com/watch?v=OrGIc4_TYq8
slides: https://files.sri.inf.ethz.ch/website/slides/rbirkner-nsdi18-slides.pdf 
---

Today network operators spend a significant amount of time struggling to understand how their network forwards traffic. Even simple questions such as “How is my network handling Google traffic?” often require operators to manually bridge large semantic gaps between lowlevel forwarding rules distributed across many routers and the corresponding high-level insights.

We introduce Net2Text, a system which assists network operators in reasoning about network-wide forwarding behaviors. Out of the raw forwarding state and a query expressed in natural language, Net2Text automatically produces succinct summaries, also in natural language, which efficiently capture network-wide semantics. Our key insight is to pose the problem of summarizing (“captioning”) the network forwarding state as an optimization problem that aims to balance coverage, by describing as many paths as possible, and explainability, by maximizing the information provided. As this problem is NP-hard, we also propose an approximation algorithm which generates summaries based on a sample of the forwarding state, with marginal loss of quality.

We implemented Net2Text and demonstrated its practicality and scalability. We show that Net2Text generates high-quality interpretable summaries of the entire forwarding state of hundreds of routers with full routing tables, in few seconds only.
