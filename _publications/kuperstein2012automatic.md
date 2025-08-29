---
ref: kuperstein2012automatic
title: Automatic Inference of Memory Fences 
authors: Michael Kuperstein, Martin Vechev and Eran Yahav      
year: 2010
venue: Formal Methods in Computer Aided Design (FMCAD)
projects: fender
awards: 
bibtex: '@article{kuperstein2012automatic,
  title={Automatic inference of memory fences},
  author={Kuperstein, Michael and Vechev, Martin and Yahav, Eran},
  journal={ACM SIGACT News},
  volume={43},
  number={2},
  pages={108--123},
  year={2012},
  publisher={ACM}}'
paper: https://files.sri.inf.ethz.ch/website/papers/fmcad2010.pdf
talk: 
slides: http://practicalsynthesis.github.io/papers/FMCAD2010-slides.pptx
---

We addresses the problem of automatic verification and fence inference in concurrent programs running under relaxed memory models. Modern architectures implement relaxed memory models in which memory operations may be reordered and executed non-atomically. Instructions called memory fences are provided to the programmer, allowing control of this behavior. To ensure correctness of many algorithms, the programmer is often required to explicitly insert memory fences into her program. However, she must use as few fences as possible, or the benefits of the relaxed architecture may be lost. It is our goal to help automate the fence insertion process.

We present an algorithm for automatic inference of memory fences in concurrent programs, relieving the programmer from this complex task. Given a finite-state program, a safety specification and a description of the memory model our algorithm computes a set of ordering constraints that guarantee the correctness of the program under the memory model. The computed constraints are maximally permissive: removing any constraint from the solution would permit an execution violating the specification. These constraints are then realized as additional fences in the input program.

We implemented our approach in a pair of tools called fender and blender and used them to infer correct and efficient placements of fences for several non-trivial algorithms, including practical mutual exclusion primitives and concurrent data structures.
