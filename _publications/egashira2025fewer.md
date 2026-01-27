---
ref: egashira2025fewer
title: "Fewer Weights, More Problems: A Practical Attack on LLM Pruning"
authors: Kazuki Egashira, Robin Staab, Thibaud Gloaguen, Mark Vero, Martin Vechev
year: 2026
month: 4
venue: ICLR
projects: llmsecpriv
awards:
bibtex: "@inproceedings{egashira2025fewer,
  title={Fewer Weights, More Problems: A Practical Attack on LLM Pruning},
  author={Egashira, Kazuki and Staab, Robin and Gloaguen, Thibaud and Vero, Mark and Vechev, Martin},
  booktitle={International Conference on Learning Representations},
  year={2026}
}"

paper: https://www.arxiv.org/abs/2510.07985
code: https://github.com/eth-sri/llm-pruning-attack
---

Model pruning, i.e., removing a subset of model weights, has become a prominent approach to reducing the memory footprint of large language models (LLMs) during inference. Notably, popular inference engines, such as vLLM, enable users to conveniently prune downloaded models before they are deployed. While the utility and efficiency of pruning methods have improved significantly, the security implications of pruning remain underexplored. In this work, for the first time, we show that modern LLM pruning methods can be maliciously exploited. In particular, an adversary can construct a model that appears benign yet, once pruned, exhibits malicious behaviors. Our method is based on the idea that the adversary can compute a proxy metric that estimates how likely each parameter is to be pruned. With this information, the adversary can first inject a malicious behavior into those parameters that are unlikely to be pruned. Then, they can repair the model by using parameters that are likely to be pruned, effectively canceling out the injected behavior in the unpruned model. We demonstrate the severity of our attack through extensive evaluation on five models; after any of the pruning in vLLM are applied (Magnitude, Wanda, and SparseGPT), it consistently exhibits strong malicious behaviors in a diverse set of attack scenarios (success rates of up to 95.7% for jailbreak, 98.7% for benign instruction refusal, and 99.5% for targeted content injection). Our results reveal a critical deployment-time security gap and underscore the urgent need for stronger security awareness in model compression.