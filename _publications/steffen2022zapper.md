---
  ref: steffen22zapper
  title: "Zapper: Smart Contracts with Data and Identity Privacy"
  authors: Samuel Steffen, Benjamin Bichsel, Martin Vechev
  year: 2022
  month: 11
  venue: ACM CCS
  awards: Distinguished Paper Award
  projects: blockchain-security
  paper: https://files.sri.inf.ethz.ch/website/papers/ccs22-zapper.pdf
  image:
  talk:
  slides: https://files.sri.inf.ethz.ch/website/papers/talk-zapper-ccs-2022-web.pdf
  code: https://github.com/eth-sri/zapper
---

Privacy concerns prevent the adoption of smart contracts in sensitive domains incompatible with the public nature of shared ledgers.

We present Zapper, a privacy-focused smart contract system allowing developers to express contracts in an intuitive frontend. Zapper hides not only the identity of its users but also the objects they access---the latter is critical to prevent deanonymization attacks. Specifically, Zapper compiles contracts to an assembly language executed by a non-interactive zero-knowledge processor and hides accessed objects by an oblivious Merkle tree construction.

We implemented Zapper on an idealized ledger and evaluated it on realistic applications, showing that it allows generating new transactions within 22 s and verifying them within 0.03 s (excluding the time for consensus). This performance is in line with the smart contract system ZEXE (Bowe et al., 2020), which offers analogous data and identity privacy guarantees but suffers from multiple shortcomings affecting security and usability.