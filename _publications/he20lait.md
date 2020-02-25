---
ref: he20lait
title: "Learning Fast and Precise Numerical Analysis"
authors: Jingxuan He, Gagandeep Singh, Markus Püschel, Martin Vechev
year: 2020
month: 06
venue: PLDI
projects: numerical-analysis, plml
awards:
bibtex:
paper:
slides:
---

Numerical abstract domains are a key component of modern static analyzers. Despite recent advances, precise relational domains remain too costly for many real world programs. To address this challenge, in this work we introduce a new data-driven method, called LAIT, that produces faster and more scalable numerical analysis without significant loss of precision. Our approach is based on the insight that sequences of abstract elements produced by the analyzer contain redundancy which can be exploited to increase performance. Concretely, we present an iterative learning algorithm that learns a neural policy which decides how much redundancy to remove at various points in the sequence. The method is generic and can be applied to any existing numerical domain.

Our evaluation of LAIT on a range of real-world applications with both Polyhedra and Octagon domains shows that even though the approach is generic, it is orders of magnitudes faster than the state-of-the-art numerical library, while maintaining 98% precision w.r.t to the original analysis.
