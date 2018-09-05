---
ref: raychev2013refactoring
title: Refactoring with Synthesis
authors: Veselin Raychev, Max Schaefer, Manu Sridharan, Martin Vechev 
year: 2013
venue: ACM OOPSLA
projects: Research Area 1, Research Area 1
awards:
bibtex: '@inproceedings{raychev2013refactoring,
  title={Refactoring with synthesis},
  author={Raychev, Veselin and Sch{\"a}fer, Max and Sridharan, Manu and Vechev, Martin},
  booktitle={ACM SIGPLAN Notices},
  volume={48},
  number={10},
  pages={339--354},
  year={2013},
  organization={ACM}}'
paper: oopsla13-refactoring.pdf
talk: 
slides: https://docs.google.com/presentation/d/1cScMNtjXskvVGWZkO-2eVm7kj-8Jtln5W7Xnl8_LAfA/edit?usp=sharing
---

Refactoring has become an integral part of modern software development, with wide support in popular integrated development environments (IDEs). Modern IDEs provide a fixed set of supported refactorings, listed in a refactoring menu. But with IDEs supporting more and more refactorings, it is becoming increasingly difficult for programmers to discover and memorize all their names and meanings. Also, since the set of refactorings is hard-coded, if a programmer wants to achieve a slightly different code transformation, she has to either apply a (possibly non-obvious) sequence of several built-in refactorings, or just perform the transformation by hand.

We propose a novel synthesis system which addresses these limitations. Our system employs a recently proposed refactoring interface, in which a refactoring is achieved via three simple steps: the programmer first indicates the start of a code refactoring phase; then she performs some of the desired code changes manually; and finally, she asks the tool to complete the refactoring.

Given the initial and modified programs, our synthesis system completes the refactoring by first extracting the difference between the starting program and the modified version, and then synthesizing a sequence of refactorings that achieves (at least) the desired changes. To enable scalable synthesis, we introduce local refactorings, which allow for first discovering a refactoring sequence on small program fragments and then extrapolating it to a full refactoring sequence.