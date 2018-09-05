---
ref: vechev2009inferring
title: Inferring Synchronization under Limited Observability
authors: Martin Vechev, Eran Yahav, Greta Yorsh
year: 2009
venue: TACAS
projects: Research Area 1, Research Area 1
awards: 
bibtex: '@inproceedings{vechev2009inferring,
  title={Inferring synchronization under limited observability},
  author={Vechev, Martin and Yahav, Eran and Yorsh, Greta},
  booktitle={International Conference on Tools and Algorithms for the Construction and Analysis of Systems},
  pages={139--154},
  year={2009},
  organization={Springer}}'
paper: tacas09.pdf
talk: 
slides: 
---

This paper addresses the problem of automatically inferring synchronization for concurrent programs. Given a program and a specification, we infer synchronization that avoids all interleavings violating the specification, but permits as many valid interleavings as possible. We let the user specify an upper bound on the cost of synchronization, which may limit the observability — what observations on program state can be made by the synchronization code. We present an algorithm that infers, under certain conditions, the maximally permissive synchronization for a given cost. We implemented a prototype of our approach and applied it to infer synchronization in a number of small programs.