---
  ref: steffen22zestar
  title: "ZeeStar: Private Smart Contracts by Homomorphic Encryption and Zero-knowledge Proofs"
  authors: Samuel Steffen, Benjamin Bichsel, Roger Baumgartner, Martin Vechev
  year: 2022
  month: 05
  venue: IEEE S&P
  projects: blockchain-security
  awards:
  bibtex:
  paper: https://files.sri.inf.ethz.ch/website/papers/sp22-zeestar.pdf
  image: 
  talk:
  slides: https://files.sri.inf.ethz.ch/website/papers/talk-zeestar-sp-2022-web.pdf
  code: https://github.com/eth-sri/zkay
---

Data privacy is a key concern for smart contracts handling sensitive data. The existing work zkay addresses this concern by allowing developers without cryptographic expertise to enforce data privacy. However, while zkay avoids fundamental limitations of other private smart contract systems, it cannot express key applications that involve operations on foreign data.

We present ZeeStar, a language and compiler allowing non-experts to instantiate private smart contracts and supporting operations on foreign data. The ZeeStar language allows developers to ergonomically specify privacy constraints using zkay's privacy annotations. The ZeeStar compiler then provably realizes these constraints by combining non-interactive zero-knowledge proofs and additively homomorphic encryption.

We implemented ZeeStar for the public blockchain Ethereum. We demonstrated its expressiveness by encoding 12 example contracts, including oblivious transfer and a private payment system like Zether. ZeeStar is practical: it prepares transactions for our contracts in at most 54.7 s, at an average cost of 339 k gas.
