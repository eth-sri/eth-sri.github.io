---
ref: jenko2024practicalattack
title: "Practical Attacks against Black-box Code Completion Engines"
authors: Slobodan Jenko*, Niels Mündler*, Jingxuan He, Mark Vero, Martin Vechev
year: 2025
month: 07
projects: llm, safeai
awards:
code:
venue: ICML 2025
paper: https://arxiv.org/abs/2408.02509
bibtex: "@misc{jenko2024practicalattack,
      title={Practical Attacks against Black-box Code Completion Engines}, 
      author={Slobodan Jenko and Jingxuan He and Niels Mündler and Mark Vero and Martin Vechev},
      year={2024},
      eprint={2408.02509},
      archivePrefix={arXiv},
      primaryClass={cs.CR}
}"
---

Modern code completion engines, powered by large language models, have demonstrated impressive capabilities to generate functionally correct code based on surrounding context. As these tools are extensively used by millions of developers, it is crucial to investigate their security implications. In this work, we present INSEC, a novel attack that directs code completion engines towards generating vulnerable code. In line with most commercial completion engines, such as GitHub Copilot, INSEC assumes only black-box query access to the targeted engine, without requiring any knowledge of the engine's internals. Our attack works by inserting a malicious attack string as a short comment in the completion input. To derive the attack string, we design a series of specialized initialization schemes and an optimization procedure for further refinement. We demonstrate the strength of INSEC not only on state-of-the-art open-source models but also on black-box commercial services such as the OpenAI API and GitHub Copilot. On a comprehensive set of security-critical test cases covering 16 CWEs across 5 programming languages, INSEC significantly increases the likelihood of the considered completion engines in generating unsafe code by >50% in absolute, while maintaining the ability in producing functionally correct code. At the same time, our attack has low resource requirements, and can be developed for a cost of well under ten USD on commodity hardware. 