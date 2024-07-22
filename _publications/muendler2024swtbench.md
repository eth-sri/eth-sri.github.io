---
ref: muendler2024swtbench
title: "Code Agents are State of the Art Software Testers"
authors: Niels Mündler, Mark Niklas Müller, Jingxuan He, Martin Vechev
year: 2024
month: 06
venue: ICML Workshop on LLMs and Cognition (also at Workshop on Foundation Models in the Wild)
awards: 
projects: safeai,llm
bibtex: "@article{muendler2024swtbench,
  title={Code Agents are State of the Art Software Testers},
  author={Niels Mündler and Mark Niklas Müller and Jingxuan He and Martin Vechev},
  journal={arXiv preprint arXiv:2406.12952},
  year={2024}
}"
paper: https://arxiv.org/abs/2406.12952
---

Rigorous software testing is crucial for developing and maintaining high-quality code, making automated test generation a promising avenue for both improving software quality and boosting the effectiveness of code generation methods. However, while code generation with Large Language Models (LLMs) is an extraordinarily active research area, test generation remains relatively unexplored. We address this gap and investigate the capability of LLM-based Code Agents for formalizing user issues into test cases. To this end, we propose a novel benchmark based on popular GitHub repositories, containing real-world issues, ground-truth patches, and golden tests. We find that LLMs generally perform surprisingly well at generating relevant test cases with Code Agents designed for code repair exceeding the performance of systems designed specifically for test generation. Further, as test generation is a similar but more structured task than code generation, it allows for a more fine-grained analysis using fail-to-pass rate and coverage metrics, providing a dual metric for analyzing systems designed for code repair. Finally, we find that generated tests are an effective filter for proposed code fixes, doubling the precision of SWE-Agent. 
