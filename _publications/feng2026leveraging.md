---
ref: feng2026leveraging
title: "Leveraging Instruction Tuning and Merging for Reasoning Model Adaptation"
authors: Yu-Du Feng*, Niels Mündler-Sasahara*, Mark Vero, Martin Vechev
year: 2026
month: 07
awards: Oral
venue: DEMO @ ICML
projects: llmevals,codellm
bibtex: '@inproceedings{
feng2026leveraging,
title={Leveraging Instruction Tuning and Merging for Reasoning Model Adaptation},
author={Yu-Du Feng and Niels M{\"u}ndler and Mark Vero and Martin Vechev},
booktitle={Decision-Making from Offline Datasets to Online Adaptation: Black-Box Optimization to Reinforcement Learning},
year={2026},
url={https://openreview.net/forum?id=Ja67cQ7t0G}
}'
paper: https://openreview.net/forum?id=iO38CMCl15
code: https://github.com/eth-sri/rlm-training-merging
---

Reasoning language models (RLMs) have demonstrated impressive performance in domains such as mathematics and coding. These domains permit reliable verification of model outputs, which is important for enabling the reinforcement learning that drives RLM performance gains. However, training RLMs on domains that lack reliable verifiers remains challenging. Meanwhile, for both verifiable and unverifiable domains, large amounts of unused supervised fine-tuning data with human-written solutions exist. In this work, we show that these data can be used efficiently to further improve RLM performance. For this, we first use classic instruction tuning, supervised fine-tuning without reasoning traces, on the RLM. Next, we merge our instruction-tuned model with the original reasoning model, recovering its reasoning behavior on the target domain. Our extensive evaluation demonstrates that our technique improves RLM performance in both verifiable and hard-to-verify domains, including coding and text summarization, while preserving RLM capabilities across other domains. Importantly, our method is highly cost-effective, enabling such improvements for less than USD $3.