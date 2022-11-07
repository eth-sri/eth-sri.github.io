---
ref: baader2019universal
title: "Learning to Configure Computer Networks with Neural Algorithmic Reasoning"
authors: Luca Beurer-Kellner, Martin Vechev, Laurent Vanbever, Petar Veličković
year: 2022
month: 11
venue: NeurIPS
projects: programmable-networks
bibtex: '@article{beurerkellner2022configure,
    author = {Beurer-Kellner, Luca and Vechev, Martin and Vanbever, Laurent and Veli{\v{c}}kovi{\''c}, Petar},
    title = {Learning to Configure Computer Networks with Neural Algorithmic Reasoning},
    journal = {Advances in Neural Information Processing Systems (NeurIPS)},
    year = {2022},
}'
paper: https://files.sri.inf.ethz.ch/website/papers/iclr2020-universal.pdf
code: https://github.com/eth-sri/learning-to-configure-networks#
---

We present a new method for scaling automatic configuration of computer networks. The key idea is to relax the computationally hard search problem of finding a configuration that satisfies a given specification into an approximate objective amenable to learning-based techniques. Based on this idea, we train a neural algorithmic model which learns to generate configurations likely to (fully or partially) satisfy a given specification under existing routing protocols. By relaxing the rigid satisfaction guarantees, our approach (i) enables greater flexibility: it is protocol-agnostic, enables cross-protocol reasoning, and does not depend on hardcoded rules; and (ii) finds configurations for much larger computer networks than previously possible. Our learned synthesizer is up to 490x faster than state-of-the-art SMT-based methods, while producing configurations which on average satisfy more than 93% of the provided requirements.