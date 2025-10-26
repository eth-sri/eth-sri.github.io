---
ref: muendler2025constraineddiffusion
title: "Constrained Decoding of Diffusion LLMs with Context-Free Grammars"
authors: Niels Mündler, Jasper Dekoninck, Martin Vechev
year: 2025
month: 8
venue: DL4C @ NeurIPS
awards: Oral
projects: codellm, cclm
bibtex: "
@article{muendler2025constraineddiffusion,
title={Constrained Decoding of Diffusion LLMs with Context-Free Grammars},
author={Niels Mündler and Jasper Dekoninck and Martin Vechev},
year={2025},
eprint={2508.10111},
archivePrefix={arXiv},
url={https://arxiv.org/abs/2508.10111}
}"
paper: https://arxiv.org/abs/2508.10111
code: https://github.com/eth-sri/constrained-diffusion
website: https://constrained-diffusion.ai
---

Large language models (LLMs) have shown promising performance across diverse domains. Many practical applications of LLMs, such as code completion and structured data extraction, require adherence to syntactic constraints specified by a formal language. Yet, due to their probabilistic nature, LLM output is not guaranteed to adhere to such formal languages. Prior work has proposed constrained decoding as a means to restrict LLM generation to particular formal languages. However, existing works are not applicable to the emerging paradigm of diffusion LLMs, when used in practical scenarios such as the generation of formally correct C++ or JSON output. In this paper we address this challenge and present the first constrained decoding method for diffusion models, one that can handle formal languages captured by context-free grammars. We begin by reducing constrained decoding to the more general additive infilling problem, which asks whether a partial output can be completed to a valid word in the target language. This problem also naturally subsumes the previously unaddressed multi-region infilling constrained decoding. We then reduce this problem to the task of deciding whether the intersection of the target language and a particular regular language is empty and present an efficient algorithm to solve it for context-free target languages. Empirical results on various applications, such as C++ code infilling and structured data extraction in JSON, demonstrate that our method achieves near-perfect syntactic correctness while consistently preserving or improving functional correctness. Importantly, our efficiency optimizations ensure that the computational overhead remains practical.
