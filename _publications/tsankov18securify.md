---
ref: tsankov18securify
title: "Securify: Practical Security Analysis of Smart Contracts"
authors: Petar Tsankov, Andrei Dan, Dana Drachsler-Cohen, Arthur Gervais, Florian Bünzli, Martin Vechev
year: 2018
month: 10
venue: ACM CCS
projects: blockchain-security
awards:
bibtex: ''
paper: https://files.sri.inf.ethz.ch/website/papers/ccs18-securify.pdf
talk: https://www.youtube.com/watch?v=7v-bd9maqm8
slides: https://files.sri.inf.ethz.ch/website/slides/ccs18-securify-slides.pdf
---

Permissionless blockchains allow the execution of arbitrary programs (called smart contracts), enabling mutually untrusted entities to interact without relying on trusted third parties. Despite their potential, repeated security concerns have shaken the trust in handling billions of USD by smart contracts. 

To address this problem, we present Securify, a security analyzer for Ethereum smart contracts that is scalable, fully automated, and able to prove contract behaviors as safe/unsafe with respect to a given property. Securify’s analysis consists of two steps. First, it symbolically analyzes the contract’s dependency graph to extract precise semantic information from the code. Then, it checks compliance and violation patterns that capture sufficient conditions for proving if a property holds or not. To enable extensibility, all patterns are specified in a designated domain-specific language.

Securify is publicly released, it has analyzed > 18K contracts submitted by its users, and is regularly used to conduct security audits by experts. We present an extensive evaluation of Securify over real-world Ethereum smart contracts and demonstrate that it can effectively prove the correctness of smart contracts and discover critical violations.
