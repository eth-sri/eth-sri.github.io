---
ref: dan2016modeling
title: Modeling and Analysis of Remote Memory Access Programming
authors: Andrei Dan, Patrick Lam, Torsten Hoefler, Martin Vechev 
year: 2016
venue: ACM OOPSLA
projects: fender
awards:
bibtex: '@article{dan2016modeling,
  title={Modeling and analysis of remote memory access programming},
  author={Dan, Andrei Marian and Lam, Patrick and Hoefler, Torsten and Vechev, Martin},
  journal={ACM SIGPLAN Notices},
  volume={51},
  number={10},
  pages={129--144},
  year={2016},
  publisher={ACM}}'
paper: https://files.sri.inf.ethz.ch/website/papers/oopsla16-rma.pdf
talk: https://2016.splashcon.org/event/splash-2016-oopsla-modeling-and-analysis-of-remote-memory-access-programming
slides: 
---

Recent advances in networking hardware have led to a new generation of Remote Memory Access (RMA) networks in which processors from different machines can communicate directly, bypassing the operating system and allowing higher performance. Researchers and practitioners have proposed libraries and programming models for RMA to enable the development of applications running on these networks,

However, the memory models implied by these RMA libraries and languages are often loosely specified, poorly understood, and differ depending on the underlying network architecture and other factors. Hence, it is difficult to precisely reason about the semantics of RMA programs or how changes in the network architecture affect them.

We address this problem with the following contributions: (i) a coreRMA language which serves as a common foundation, formalizing the essential characteristics of RMA programming; (ii) complete axiomatic semantics for that language; (iii) integration of our semantics with an existing constraint solver, enabling us to exhaustively generate coreRMA programs (litmus tests) up to a specified bound and check whether the tests satisfy their specification; and (iv) extensive validation of our semantics on real-world RMA systems. We generated and ran 7,441 litmus tests using each of the low-level RMA network APIs: DMAPP, VPI Verbs, and Portals 4. Our results confirmed that our model successfully captures behaviors exhibited by these networks. Moreover, we found RMA programs that behave inconsistently with existing documentation, confirmed by network experts.
