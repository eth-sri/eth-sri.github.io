---
ref: o2010verifying
title: Verifying Linearizability with Hindsight
authors: Peter O'Hearn, Noam Rinetzky, Martin Vechev, Eran Yahav and Greta Yorsh
year: 2010
venue: ACM PODC
projects: Research Area 1, Research Area 1
awards: 
bibtex: "@inproceedings{o2010verifying,
  title={Verifying linearizability with hindsight},
  author={O'Hearn, Peter W and Rinetzky, Noam and Vechev, Martin T and Yahav, Eran and Yorsh, Greta},
  booktitle={Proceedings of the 29th ACM SIGACT-SIGOPS symposium on Principles of distributed computing},
  pages={85--94},
  year={2010},
  organization={ACM}}"
paper: PODC10-hindsight.pdf
talk: 
slides: 
---

We present a proof of safety and linearizability of a highly-concurrent optimistic set algorithm. The key step in our proof is the Hindsight Lemma, which allows a thread to infer the existence of a global state in which its operation can be linearized based on limited local atomic observations about the shared state. The Hindsight Lemma allows us to avoid one of the most complex and non-intuitive steps in reasoning about highly concurrent algorithms: considering the linearization point of an operation to be in a different thread than the one executing it.

The Hindsight Lemma assumes that the algorithm maintains certain simple invariants which are resilient to interference, and which can themselves be verified using purely thread-local proofs. As a consequence, the lemma allows us to unlock a perhaps-surprising intuition: a high degree of interference makes non-trivial highly-concurrent algorithms in some cases much easier to verify than less concurrent ones.