---
ref: dekoninck2023controlled
title: "Controlled Text Generation via Language Model Arithmetic"
authors: Jasper Dekoninck, Marc Fischer, Luca Beurer-Kellner, Martin Vechev
year: 2023
month: 11
venue: arXiv 
projects: llm
bibtex: "@misc{dekoninck2023controlled,
      title={Controlled Text Generation via Language Model Arithmetic}, 
      author={Jasper Dekoninck and Marc Fischer and Luca Beurer-Kellner and Martin Vechev},
      year={2023},
      eprint={2311.14479},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}"
paper: https://files.sri.inf.ethz.ch/website/papers/dekoninck2023controlled.pdf
code: https://github.com/eth-sri/language-model-arithmetic
---

As Large Language Models (LLMs) are deployed more widely, customization with respect to vocabulary, style and character becomes more important. In this work we introduce model arithmetic, a novel inference framework for composing and biasing LLMs without the need for model (re)training or highly specific datasets. In addition, the framework allows for more precise control of generated text than direct prompting and prior controlled text generation (CTG) techniques. Using model arithmetic, we can express prior CTG techniques as simple formulas and naturally extend them to new and more effective formulations. Further, we show that speculative sampling, a technique for efficient LLM sampling, extends to our setting. This enables highly efficient text generation with multiple composed models with only marginal overhead over a single model. Our empirical evaluation demonstrates that model arithmetic allows fine-grained control of generated text while outperforming state-of-the-art on the task of toxicity reduction.