---
ref: dekoninck2024cascaderouting
title: "A Unified Approach to Routing and Cascading for LLMs"
authors: Jasper Dekoninck, Maximilian Baader, Martin Vechev
year: 2025
month: 07
venue: ICML
projects: llm
bibtex: "@article{dekoninck2024cascaderouting,
      title={A Unified Approach to Routing and Cascading for LLMs}, 
      author={Jasper Dekoninck and Maximilian Baader and Martin Vechev},
      year={2024},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}"
paper: https://files.sri.inf.ethz.ch/website/papers/dekoninck2024cascaderouting.pdf
code: https://github.com/eth-sri/cascade-routing
---
The widespread applicability of large language models (LLMs) has increased the availability of many fine-tuned models of various sizes targeting specific tasks. Given a set of such specialized models, to maximize overall performance, it is important to figure out the optimal strategy for selecting the right model for a given user query. An effective strategy could drastically increase overall performance and even offer improvements over a single large monolithic model. Existing approaches typically fall into two categories: routing, where a single model is selected for each query, and cascading, which runs a sequence of increasingly larger models until a satisfactory answer is obtained. However, both have notable limitations: routing commits to an initial model without flexibility, while cascading requires executing every model in sequence, which can be inefficient. Additionally, the conditions under which these strategies are provably optimal remain unclear. In this work, we derive optimal strategies for both routing and cascading. Building on this analysis, we propose a novel approach called cascade routing, which combines the adaptability of routing with the cost-efficiency of cascading. Our experiments demonstrate that cascade routing consistently outperforms both routing and cascading across a variety of settings, improving both output quality and lowering computational cost, thus offering a unified and efficient solution to the model selection problem.