---
  ref: he19ilf
  title: "Learning to Fuzz from Symbolic Execution with Application to Smart Contracts"
  authors: Jingxuan He, Mislav Balunović, Nodar Ambroladze, Petar Tsankov, Martin Vechev
  year: 2019
  month: 11
  venue: ACM CCS
  projects: blockchain-security, plml
  awards:
  bibtex:
  paper: https://files.sri.inf.ethz.ch/website/papers/ccs19-ilf.pdf
  image: assets/images/ilf-logo.png
  talk: https://dl.acm.org/doi/10.1145/3319535.3363230#sec-supp
  slides: https://files.sri.inf.ethz.ch/website/slides/ccs19-ilf-slides.pdf
  code: https://github.com/eth-sri/ilf
---

Fuzzing and symbolic execution are two complementary techniques for discovering software vulnerabilities. Fuzzing is fast and scalable, but can be ineffective when it fails to randomly select the right inputs. Symbolic execution is thorough but slow and often does not scale to deep program paths with complex path conditions.

In this work, we propose to learn an effective and fast fuzzer from symbolic execution, by phrasing the learning task in the framework of imitation learning. During learning, a symbolic execution expert generates a large number of quality inputs improving coverage on thousands of programs. Then, a fuzzing policy, represented with a suitable architecture of neural networks, is trained on the generated dataset. The learned policy can then be used to fuzz new programs.

We instantiate our approach to the problem of fuzzing smart contracts, a domain where contracts often implement similar functionality (facilitating learning) and security is of utmost importance. We present an end-to-end system, ILF (for Imitation Learning based Fuzzer), and an extensive evaluation over >18K contracts. Our results show that ILF is effective: (i) it is fast, generating 148 transactions per second, (ii) it outperforms existing fuzzers (e.g., achieving 33% more coverage), and (iii) it detects more vulnerabilities than existing fuzzing and symbolic execution tools for Ethereum.
