---
ref: berabi21tfix
title: "TFix: Learning to Fix Coding Errors with a Text-to-Text Transformer"
authors: Berkay Berabi, Jingxuan He, Veselin Raychev, Martin Vechev
year: 2021
month: 07
venue: ICML
projects: plml
awards:
bibtex:
paper: https://files.sri.inf.ethz.ch/website/papers/icml21-tfix.pdf
talk: https://icml.cc/virtual/2021/poster/8789
slides: https://files.sri.inf.ethz.ch/website/papers/icml21-tfix-slides.pdf
code: https://github.com/eth-sri/TFix
---

The problem of fixing errors in programs has attracted substantial interest over the years. The key challenge for building an effective code fixing tool is to capture a wide range of errors and meanwhile maintain high accuracy. In this paper, we address this challenge and present a new learning-based system, called TFix. TFix works directly on program text and phrases the problem of code fixing as a text-to-text task. In turn, this enables it to leverage a powerful Transformer based model pre-trained on natural language and fine-tuned to generate code fixes (via a large, high-quality dataset obtained from GitHub commits). TFix is not specific to a particular programming language or class of defects and, in fact, improved its precision by simultaneously fine-tuning on 52 different error types reported by a popular static analyzer. Our evaluation on a massive dataset of JavaScript programs shows that TFix is practically effective: it is able to synthesize code that fixes the error in ~67 percent of cases and significantly outperforms existing learning-based approaches