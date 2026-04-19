---
ref: gloaguen2026agentsmd
title: "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"
authors: Thibaud Gloaguen, Niels Mündler, Mark Niklas Müller, Veselin Raychev, Martin Vechev
year: 2026
month: 04
venue: MemAgents @ ICLR
awards: Oral
projects: codellm
bibtex: "@inproceedings{
gloaguen2026evaluating,
title={Evaluating {AGENTS}.md: Are Repository-Level Context Files Helpful for Coding Agents?},
author={Thibaud Gloaguen and Niels M{\"u}ndler and Mark Niklas Mueller and Veselin Raychev and Martin Vechev},
booktitle={ICLR 2026 Workshop on Memory for LLM-Based Agentic Systems},
year={2026},
url={https://openreview.net/forum?id=pLi3A8bscP}
}"
paper: https://openreview.net/forum?id=pLi3A8bscP
code: https://github.com/eth-sri/agentbench
---

A widespread practice in software development is to tailor coding agents to repositories using context files, such as AGENTS.md, by either manually or automatically generating them. Although this practice is strongly encouraged by agent developers, there is currently no rigorous investigation into whether such context files are actually effective for real-world tasks. In this work, we study this question and evaluate coding agents' task completion performance in two complementary settings: established SWE-bench tasks from popular repositories, with LLM-generated context files following agent-developer recommendations, and a novel collection of issues with developer-provided context files.

Across multiple coding agents and LLMs, we find that context files result in no improvement in task success rates, while also increasing inference cost by over 20%. Behaviorally, both LLM-generated and developer-provided context files encourage broader exploration (e.g., more thorough testing and file traversal), and coding agents tend to respect their instructions. Ultimately, we conclude that unnecessary requirements from context files make tasks harder, and human-written context files should describe only minimal requirements.