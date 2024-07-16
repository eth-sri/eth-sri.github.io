---
ref: staab2024anonymization
title: "Large Language Models are Advanced Anonymizers"
authors: Robin Staab, Mark Vero, Mislav Balunović, Martin Vechev
year: 2024
month: 02
venue: arXiv
projects: llm
bibtex: "@misc{staab2024large,
      title={Large Language Models are Advanced Anonymizers}, 
      author={Robin Staab and Mark Vero and Mislav Balunović and Martin Vechev},
      year={2024},
      eprint={2402.13846},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}"
paper: https://arxiv.org/abs/2402.13846
---

Recent work in privacy research on large language models has shown that they achieve near human-level performance at inferring personal data from real-world online texts. With consistently increasing model capabilities, existing text anonymization methods are currently lacking behind regulatory requirements and adversarial threats. This raises the question of how individuals can effectively protect their personal data in sharing online texts. In this work, we take two steps to answer this question: We first present a new setting for evaluating anonymizations in the face of adversarial LLMs inferences, allowing for a natural measurement of anonymization performance while remedying some of the shortcomings of previous metrics. We then present our LLM-based adversarial anonymization framework leveraging the strong inferential capabilities of LLMs to inform our anonymization procedure. In our experimental evaluation, we show on real-world and synthetic online texts how adversarial anonymization outperforms current industry-grade anonymizers both in terms of the resulting utility and privacy.