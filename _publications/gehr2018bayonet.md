---
ref: gehr2018bayonet
title: "Bayonet: Probabilistic Inference for Networks"
authors: Timon Gehr, Sasa Misailovic, Petar Tsankov, Laurent Vanbever, Pascal Wiesmann, Martin Vechev
year: 2018
month: 06
venue: PLDI
projects: probabilistic-programming, programmable-networks
awards:
bibtex: '@inproceedings{gehr2018bayonet,
  title={Bayonet: probabilistic inference for networks},
  author={Gehr, Timon and Misailovic, Sasa and Tsankov, Petar and Vanbever, Laurent and Wiesmann, Pascal and Vechev, Martin},
  booktitle={Proceedings of the 39th ACM SIGPLAN Conference on Programming Language Design and Implementation},
  pages={586--602},
  year={2018},
  organization={ACM}}'
paper: https://files.sri.inf.ethz.ch/website/papers/bayonet-pldi2018.pdf
talk: https://www.youtube.com/watch?v=VeaBso0n13k
slides: 
---

Network operators often need to ensure that important probabilistic properties are met, such as that the probability of network congestion is below a certain threshold. Ensuring such properties is challenging and requires both a suitable language for probabilistic networks and an automated procedure for answering probabilistic inference queries.

We present Bayonet, a novel approach that consists of: (i) a probabilistic network programming language and (ii) a system that performs probabilistic inference on Bayonet programs. The key insight behind Bayonet is to phrase the problem of probabilistic network reasoning as inference in existing probabilistic languages. As a result, Bayonet directly leverages existing probabilistic inference systems and offers a flexible and expressive interface to operators.

We present a detailed evaluation of Bayonet on common network scenarios, such as network congestion, reliability of packet delivery, and others. Our results indicate that Bayonet can express such practical scenarios and answer queries for realistic topology sizes (with up to 30 nodes).
