---
  ref: permenev20verx
  title: "VerX: Safety Verification of Smart Contracts"
  authors: Anton Permenev, Dimitar Dimitrov, Petar Tsankov, Dana Drachsler-Cohen, Martin Vechev
  year: 2020
  month: 01
  venue: IEEE S&P
  projects: blockchain-security
  awards:
  bibtex:
  paper: https://files.sri.inf.ethz.ch/website/papers/sp20-verx.pdf
  talk:
  slides:
---

We present VerX, the first automated verifier able to prove functional properties of Ethereum smart contracts. VerX addresses an important problem as all real-world contracts must satisfy custom functional specifications.

VerX is based on a careful combination of three techniques, enabling it to automatically verify temporal properties of infinite-state smart contracts: (i) reduction of temporal property verification to reachability checking, (ii) a new symbolic execution engine for the Ethereum Virtual Machine that is precise and efficient for a practical fragment of Ethereum contracts, and (iii) delayed predicate abstraction which uses symbolic execution during transactions and abstraction at transaction boundaries.

Our extensive experimental evaluation on 83 temporal properties and 12 real-world projects, including popular crowdsales and libraries, demonstrates that VerX is practically effective.
