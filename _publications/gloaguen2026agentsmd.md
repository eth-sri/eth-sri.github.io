---
ref: gloaguen2026agentsmd
title: "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?"
authors: Thibaud Gloaguen, Niels Mündler, Mark Niklas Müller, Veselin Raychev, Martin Vechev
year: 2026
month: 02
venue: arXiv
projects: codellm, cllm
bibtex: "@misc{gloaguen2026agentsmd,
      title={Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?},
      author={Thibaud Gloaguen and Niels Mündler and Mark Müller and Veselin Raychev and Martin Vechev},
      year={2026},
      eprint={2602.11988},
      archivePrefix={arXiv},
      primaryClass={cs.SE},
      url={https://arxiv.org/abs/2602.11988},
}"
paper: https://arxiv.org/pdf/2602.11988
code: https://github.com/eth-sri/agentbench
---

A widespread practice in software development is to tailor coding agents to repositories using context files such as `AGENTS.md`, either written manually or generated automatically. Although this practice is strongly encouraged by agent developers, there is little rigorous evidence on whether such context files improve real-world task performance. We evaluate coding agents in two complementary settings: established SWE-bench tasks from popular repositories with LLM-generated context files following agent-developer recommendations, and a new collection of issues from repositories that contain developer-committed context files. Across multiple coding agents and LLMs, context files generally reduce task success rates compared to providing no repository context while increasing inference cost by over 20%. Behaviorally, both LLM-generated and developer-provided context files encourage broader exploration, such as more testing and file traversal, and agents tend to follow their instructions. Overall, our findings suggest that unnecessary requirements in context files can make tasks harder, and that human-written context files should focus on minimal requirements.
