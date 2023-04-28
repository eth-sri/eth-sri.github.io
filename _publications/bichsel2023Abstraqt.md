---
ref: bichsel2023Abstraqt
title: "Abstraqt: Analysis of Quantum Circuits via Abstract Stabilizer Simulation"
authors: Benjamin Bichsel, Maximilian Baader, Anouk Paradis, Martin Vechev
year: 2023
month: 04
venue: arXiv
projects: quantum
paper: https://arxiv.org/abs/2304.00921

---

Stabilizer simulation can efficiently simulate an important class of quantum circuits consisting exclusively of Clifford gates. However, all existing extensions of this simulation to arbitrary quantum circuits including non-Clifford gates suffer from an exponential runtime.
In this work, we address this challenge by presenting a novel approach for efficient stabilizer simulation on arbitrary quantum circuits, at the cost of lost precision. Our key idea is to compress an exponential sum representation of the quantum state into a single abstract summand covering (at least) all occurring summands. This allows us to introduce an abstract stabilizer simulator that efficiently manipulates abstract summands by over-abstracting the effect of circuit operations including Clifford gates, non-Clifford gates, and (internal) measurements.
We implemented our abstract simulator in a tool called Abstraqt and experimentally demonstrate that Abstraqt can establish circuit properties intractable for existing techniques. 

