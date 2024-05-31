---
ref: egashira2024quantization
title: "Exploiting LLM Quantization"
authors: Kazuki Egashira, Mark Vero, Robin Staab, Jingxuan He, Martin Vechev
year: 2024
month: 5
venue: arXiv
projects: llm
bibtex: "@article{egashira2024exploiting,
  title={Exploiting LLM Quantization},
  author={Egashira, Kazuki and Vero, Mark and Staab, Robin and He, Jingxuan and Vechev, Martin},
  journal={arXiv preprint arXiv:2405.18137},
  year={2024}
}"

paper: https://arxiv.org/abs/2405.18137
---

Quantization leverages lower-precision weights to reduce the memory usage of large language models (LLMs) and is a key technique for enabling their deployment on commodity hardware. While LLM quantization's impact on utility has been extensively explored, this work for the first time studies its adverse effects from a security perspective. We reveal that widely used quantization methods can be exploited to produce a harmful quantized LLM, even though the full-precision counterpart appears benign, potentially tricking users into deploying the malicious quantized model. We demonstrate this threat using a three-staged attack framework: (i) first, we obtain a malicious LLM through fine-tuning on an adversarial task; (ii) next, we quantize the malicious model and calculate constraints that characterize all full-precision models that map to the same quantized model; (iii) finally, using projected gradient descent, we tune out the poisoned behavior from the full-precision model while ensuring that its weights satisfy the constraints computed in step (ii). This procedure results in an LLM that exhibits benign behavior in full precision but when quantized, it follows the adversarial behavior injected in step (i). We experimentally demonstrate the feasibility and severity of such an attack across three diverse scenarios: vulnerable code generation, content injection, and over-refusal attack. In practice, the adversary could host the resulting full-precision model on an LLM community hub such as Hugging Face, exposing millions of users to the threat of deploying its malicious quantized version on their devices. 