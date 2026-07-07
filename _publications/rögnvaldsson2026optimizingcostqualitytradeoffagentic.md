---
ref: rögnvaldsson2026optimizingcostqualitytradeoffagentic
title: "Optimizing the Cost-Quality Tradeoff of Agentic Theorem Provers in Lean"
authors: Kári Rögnvaldsson*, Chenhao Sun*, Jasper Dekoninck, Martin Vechev
year: 2026
month: 5
venue: AI4Math@ICML
awards:
projects: mathllm
bibtex: "@article{rögnvaldsson2026optimizingcostqualitytradeoffagentic,
      title={Optimizing the Cost-Quality Tradeoff of Agentic Theorem Provers in Lean}, 
      author={Kári Rögnvaldsson and Chenhao Sun and Jasper Dekoninck and Martin Vechev},
      year={2026},
      eprint={2606.04883},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2606.04883}, 
}"
paper: https://arxiv.org/abs/2606.04883
code: https://github.com/eth-sri/optimizing-lean-agents
---

Large language models (LLMs) are increasingly used in workflows for generating formal proofs in Lean. These workflows often decompose problems into smaller lemmas, sample many proof attempts, and use compiler feedback to guide search. However, they can be prohibitively expensive, often spending substantial compute on attempts that ultimately fail. In this work, we address this problem with an action routing agent that consists of a data plane and a control plane. The data plane generates natural-language lemma decompositions, formalizes them in Lean, and samples proof attempts for the resulting theorem and lemma targets. The control plane observes previous failed Lean attempts, estimates both the likelihood of success and cost of another attempt, and decides whether to continue proving the current target or restart from a new breakdown. On a subset of PutnamBench, our agent decreases the cost by 25.8% over a fixed-step baseline on average, preserving performance while using substantially less compute. These results suggest that failed Lean trajectories provide actionable signals for cost-aware resource allocation in agentic theorem proving.
