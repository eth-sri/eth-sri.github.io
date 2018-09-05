---
ref: raychev2014code
title: Code Completion with Statistical Language Models 
authors: Veselin Raychev, Martin Vechev, Eran Yahav         
year: 2014
venue: ACM PLDI
projects: plml
awards:
bibtex: '@inproceedings{raychev2014code,
  title={Code completion with statistical language models},
  author={Raychev, Veselin and Vechev, Martin and Yahav, Eran},
  booktitle={Acm Sigplan Notices},
  volume={49},
  number={6},
  pages={419--428},
  year={2014},
  organization={ACM}}'
paper: https://files.sri.inf.ethz.ch/website/papers/pldi14-statistical.pdf
talk: 
slides: 
---

We address the problem of synthesizing code completions for programs using APIs. Given a program with holes, we synthesize completions for holes with the most likely sequences of method calls.

Our main idea is to reduce the problem of code completion to a natural-language processing problem of predicting probabilities of sentences. We design a simple and scalable static analysis that extracts sequences of method calls from a large codebase, and index these into a statistical language model. We then employ the language model to find the highest ranked sentences, and use them to synthesize a code completion. Our approach is able to synthesize sequences of calls across multiple objects together with their arguments.

Experiments show that our approach is fast and effective. Virtually all computed completions typecheck, and the desired completion appears in the top 3 results in 90% of the cases.
