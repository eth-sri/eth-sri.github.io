---
ref: thillen2026codetaste
title: "CodeTaste: Can LLMs Generate Human-Level Code Refactorings?"
authors: Alex Thillen, Niels Mündler, Veselin Raychev, Martin Vechev
year: 2026
month: 05
venue: ICML 2026
awards:
projects: codellm,llmevals
bibtex: "@article{thillen2026codetaste,
      title={CodeTaste: Can LLMs Generate Human-Level Code Refactorings?},
      author={Alex Thillen and Niels M{\"u}ndler and Veselin Raychev and Martin Vechev},
      year={2026},
      eprint={2603.04177},
      archivePrefix={arXiv},
      primaryClass={cs.SE},
      url={https://arxiv.org/abs/2603.04177}
}"
paper: https://arxiv.org/abs/2603.04177
website: https://codetaste.logicstar.ai
code: https://github.com/logic-star-ai/codetaste
---

Large language model (LLM) coding agents can generate working code, but their solutions often accumulate complexity, duplication, and architectural debt. Human developers address such issues through refactoring: behavior-preserving program transformations that improve structure and maintainability. In this paper, we investigate whether LLM agents can both execute refactorings reliably and identify the refactorings that human developers actually chose in real codebases. We present CodeTaste, a benchmark of refactoring tasks mined from large-scale multi-file changes in open-source repositories. To evaluate solutions, we combine repository test suites with custom static checks that verify the removal of undesired patterns and the introduction of desired patterns using dataflow reasoning.

Our experiments show a clear gap across frontier models: agents perform well when refactorings are specified in detail, but often fail to discover the human refactoring choices when given only a focus area for improvement. A propose-then-implement decomposition improves alignment, and selecting the best-aligned proposal before implementation yields further gains. CodeTaste provides both an evaluation target and a potential preference signal for aligning coding agents with human refactoring decisions in realistic codebases.
