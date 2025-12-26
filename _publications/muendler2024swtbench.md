---
ref: muendler2024swtbench
title: "SWT-Bench: Testing and Validating Real-World Bug-Fixes with Code Agents"
authors: Niels Mündler, Mark Niklas Müller, Jingxuan He, Martin Vechev
year: 2024
month: 11
venue: NeurIPS
awards: 
projects: codellm,llmevals
bibtex: "@inproceedings{
m{\"u}ndler2024swtbench,
title={{SWT}-Bench: Testing and Validating Real-World Bug-Fixes with Code Agents},
author={Niels M{\"u}ndler and Mark Niklas Mueller and Jingxuan He and Martin Vechev},
booktitle={The Thirty-eighth Annual Conference on Neural Information Processing Systems},
year={2024},
url={https://openreview.net/forum?id=9Y8zUO11EQ}
}"
paper: https://arxiv.org/abs/2406.12952
code: https://github.com/logic-star-ai/swt-bench
website: https://swtbench.com
talk: https://neurips.cc/virtual/2024/poster/96304
---

Rigorous software testing is crucial for developing and maintaining high-quality code, making automated test generation a promising avenue for both improving software quality and boosting the effectiveness of code generation methods. However, while code generation with Large Language Models (LLMs) is an extraordinarily active research area, test generation remains relatively unexplored. We address this gap and investigate the capability of LLM-based Code Agents for formalizing user issues into test cases. To this end, we propose a novel benchmark based on popular GitHub repositories, containing real-world issues, ground-truth patches, and golden tests. We find that LLMs generally perform surprisingly well at generating relevant test cases with Code Agents designed for code repair exceeding the performance of systems designed specifically for test generation. Further, as test generation is a similar but more structured task than code generation, it allows for a more fine-grained analysis using fail-to-pass rate and coverage metrics, providing a dual metric for analyzing systems designed for code repair. Finally, we find that generated tests are an effective filter for proposed code fixes, doubling the precision of SWE-Agent. 
