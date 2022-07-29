---
  ref: steffen20netdice
  title: "Probabilistic Verification of Network Configurations"
  authors: Samuel Steffen, Timon Gehr, Petar Tsankov, Laurent Vanbever, Martin Vechev
  year: 2020
  month: 8
  venue: ACM SIGCOMM
  projects: programmable-networks
  awards: Best Student Paper Award
  bibtex: '@inproceedings{steffen2020netdice,
    author = {Steffen, Samuel and Gehr, Timon and Tsankov, Petar and Vanbever, Laurent and Vechev, Martin},
    title = {Probabilistic Verification of Network Configurations},
    year = {2020},
    isbn = {9781450379557},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    url = {https://doi.org/10.1145/3387514.3405900},
    doi = {10.1145/3387514.3405900},
    booktitle = {Proceedings of the Annual Conference of the ACM Special Interest Group on Data Communication on the Applications, Technologies, Architectures, and Protocols for Computer Communication},
    pages = {750–764},
    numpages = {15},
    location = {Virtual Event, USA},
    series = {SIGCOMM ’20}
    }'
  paper: https://files.sri.inf.ethz.ch/website/papers/sigcomm20-netdice.pdf
  image: 
  talk: https://polybox.ethz.ch/index.php/s/2Kl3RZYgKCE7W4Z
  slides: https://files.sri.inf.ethz.ch/website/papers/talk-netdice-sigcomm-2020-web.pdf
  code: https://github.com/nsg-ethz/netdice
---

Not all important network properties need to be enforced all the time. Often, what matters instead is the fraction of time / probability these properties hold. Computing the probability of a property in a network relying on complex inter-dependent routing protocols is challenging and requires determining all failure scenarios for which the property is violated. Doing so at scale and accurately goes beyond the capabilities of current network analyzers.

In this paper, we introduce NetDice, the first scalable and accurate probabilistic network configuration analyzer supporting BGP, OSPF, ECMP, and static routes. Our key contribution is an inference algorithm to efficiently explore the space of failure scenarios. More specifically, given a network configuration and a property phi, our algorithm automatically identifies a set of links whose failure is provably guaranteed not to change whether phi holds. By pruning these failure scenarios, NetDice manages to accurately approximate P(phi). NetDice supports practical properties and expressive failure models including correlated link failures.

We implement NetDice and evaluate it on realistic configurations. NetDice is practical: it can precisely verify probabilistic properties in few minutes, even in large networks.
