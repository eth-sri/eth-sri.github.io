---
ref: raychev2013automatic
title: Automatic Synthesis of Deterministic Concurrency
authors: Veselin Raychev, Martin Vechev, Eran Yahav 
year: 2013
venue: Static Analysis Symposium (SAS)
projects: Research Area 1, Research Area 1
awards:
bibtex: '@inproceedings{raychev2013automatic,
  title={Automatic synthesis of deterministic concurrency},
  author={Raychev, Veselin and Vechev, Martin and Yahav, Eran},
  booktitle={International Static Analysis Symposium},
  pages={283--303},
  year={2013},
  organization={Springer}}'
paper: https://files.sri.inf.ethz.ch/website/papers/sas13-dps.pdf
talk: 
slides: https://files.sri.inf.ethz.ch/website/slides/sas13-dps-slides.pdf
---

Many parallel programs are meant to be deterministic: for the same input, the program must produce the same output, regardless of scheduling choices. Unfortunately, due to complex parallel interaction, programmers make subtle mistakes that lead to violations of determinism.

In this paper, we present a framework for static synthesis of deterministic concurrency control: given a non-deterministic parallel program, our synthesis algorithm introduces synchronization that transforms the program into a deterministic one. The main idea is to statically compute inter-thread ordering constraints that guarantee determinism and preserve program termination. Then, given the constraints and a set of synchronization primitives, the synthesizer produces a program that enforces the constraints using the provided synchronization primitives.

To handle realistic programs, our synthesis algorithm uses two abstractions: a thread-modular abstraction, and an abstraction for memory locations that can track array accesses. We have implemented our algorithm and successfully applied it to synthesize deterministic control for a number of programs inspired by those used in the high-performance computing community. For most programs, the synthesizer produced synchronization that is as good or better than the handcrafted synchronization inserted by the programmer.
