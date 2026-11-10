---
ref: chenhao26vul-propagation
title: "Coding Agents Propagate Vulnerabilities in Code Bases"
authors: Chenhao Sun, Niels Mündler-Sasahara, Mark Vero, Martin Vechev
year: 2026
month: 11
venue: arxiv
projects: codellm
bibtex: '@article{sun2026vulpropagation,
  title={Coding Agents Propagate Vulnerabilities in Code Bases},
  author={Chenhao Sun, Niels Mündler-Sasahara, Mark Vero and Martin Vechev},
  journal={arXiv preprint arXiv:2611.11455},
  year={2026},
  url={https://arxiv.org/abs/2611.11455}
}'
paper: https://arxiv.org/pdf/2611.11455
code: https://github.com/eth-sri/vulnerability-propagation
---

LLM-based coding agents are widely used to develop critical production software. Even though coding agents are known to occasionally write vulnerable code, there has not been any investigation into how code base vulnerabilities evolve over time under coding agent contributions. In this work, we close this gap by investigating whether and how vulnerabilities in existing code lead coding agents to introduce similar vulnerabilities in the code they write. We first evaluate coding agents on 96 tasks that require implementing a new backend application in a repository where other applications already exist. Second, we investigate repository-level code generation on 20 pairs of tasks in real C/C++ projects. In each task, the agent is asked to complete code critical to memory safety. We find that in both settings, insecure existing code leads to agents writing vulnerable code more often. In backend generation, insecure neighbors reduce the share of correct and secure implementations by 3.4% on average, and in C/C++ repository-level coding, the average gap between secure and insecure contexts reaches 35.4%. Prompting to follow existing code-style or to be careful about security increases, respectively decreases, how strongly agents propagate vulnerabilities, but neither stops them. When asked to explain their implementation choices, coding agents attribute them to following another code site in 76.5% of cases, even though they recognize the introduced vulnerability in 69.9% of cases. These findings show that agents use existing vulnerabilities as templates for new ones indiscriminatorily, turning each contribution into an opportunity to introduce more vulnerabilities. As such, as agents write a growing share of production code under decreasing human review, code bases can increasingly degrade in security if security vulnerabilities are not thoroughly fixed continuously.
