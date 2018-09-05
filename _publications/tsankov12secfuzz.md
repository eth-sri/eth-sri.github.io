---
  ref: tsankov12secfuzz
  title: 'SecFuzz: Fuzz Testing Security Protocols'
  authors: Petar Tsankov, Mohammad Torabi Dashti, David Basin
  year: 2012
  venue: IEEE/ACM AST
  projects: 
  awards:
  bibtex:
  paper: https://files.sri.inf.ethz.ch/website/papers/tsankov12secfuzz.pdf
  talk: 
  slides: https://files.sri.inf.ethz.ch/website/slides/tsankov12secfuzz-slides.pdf
---

We propose a light-weight, yet effective, technique for fuzz-testing security protocols. Our technique is modular, it exercises (stateful) protocol implementations in depth, and handles encrypted traffic. We use a concrete implementation of the protocol to generate valid inputs, and mutate the inputs using a set of fuzz operators. A dynamic memory analysis tool monitors the execution as an oracle to detect the vulnerabilities exposed by fuzz-testing. We provide the fuzzer with the necessary keys and cryptographic algorithms in order to properly mutate encrypted messages. We present a case study on two widely used, mature implementations of the Internet Key Exchange (IKE) protocol and report on two new vulnerabilities discovered by our fuzz-testing tool. We also compare the effectiveness of our technique to two existing model-based fuzz-testing tools for IKE.
