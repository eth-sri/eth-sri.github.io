---
  ref: baumann20zkay
  title: "zkay v0.2: Practical Data Privacy for Smart Contracts"
  authors: Nick Baumann, Samuel Steffen, Benjamin Bichsel, Petar Tsankov, Martin Vechev
  year: 2020
  month: 9
  venue: arXiv
  projects: blockchain-security
  awards:
  bibtex: '@techreport{baumann2020zkay,
    title={zkay v0.2: Practical Data Privacy for Smart Contracts},
    author={Nick Baumann and Samuel Steffen and Benjamin Bichsel and Petar Tsankov and Martin Vechev},
    year={2020},
    eprint={2009.01020},
    url={https://arxiv.org/abs/2009.01020}
  }'
  paper: https://arxiv.org/pdf/2009.01020.pdf
  image: 
  talk:
  slides:
  code: https://github.com/eth-sri/zkay
---

Recent work introduces zkay, a system for specifying and enforcing data privacy in smart contracts. While the original prototype implementation of zkay (v0.1) demonstrates the feasibility of the approach, its proof-of-concept implementation suffers from severe limitations such as insecure encryption and lack of important language features.

In this report, we present zkay v0.2, which addresses its predecessor's limitations. The new implementation significantly improves security, usability, modularity, and performance of the system. In particular, zkay v0.2 supports state-of-the-art asymmetric and hybrid encryption, introduces many new language features (such as function calls, private control flow, and extended type support), allows for different zk-SNARKs backends, and reduces both compilation time and on-chain costs.
