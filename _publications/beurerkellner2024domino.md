---
ref: beurerkellner2024domino
title: "Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation"
authors: Luca Beurer-Kellner, Marc Fischer, Martin Vechev
year: 2024
month: 07
venue: ICML
projects: llm
bibtex: "@article{beurerkellner2024domino,
      title={Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation},
      author={Luca Beurer-Kellner and Marc Fischer and Martin Vechev},
      year={2024}
}"
paper: https://arxiv.org/abs/2403.06988
code: https://github.com/eth-sri/domino
---
To ensure that text generated by large language models (LLMs) is in an expected format, constrained decoding proposes to enforce strict formal language constraints during generation. However, as we show in this work, not only do such methods incur performance overhead during generation, but many of them also significantly impair task accuracy, if they do not correctly align the underlying LLM sub-word vocabularies with external constraints. To address this, we present a novel decoding algorithm, DOMINO, that can enforce constraints in a fully subword-aligned fashion, while leveraging pre-computation and speculative decoding to achieve virtually no overhead and in some cases even almost 2x speedup over unconstrained decoding -- thereby outperforming existing approaches by a wide margin.
