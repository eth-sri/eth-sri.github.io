---
ref: egashira2025mind
title: "Mind the Gap: A Practical Attack on GGUF Quantization"
authors: Kazuki Egashira, Robin Staab, Mark Vero, Jingxuan He, Martin Vechev
year: 2025
month: 7
venue: ICML
projects: llm
awards: BuildingTrust@ICLR25 Oral
bibtex: "@article{egashira2025mind,
  title={Mind the Gap: A Practical Attack on GGUF Quantization},
  author={Egashira, Kazuki and Staab, Robin and Vero, Mark and He, Jingxuan and Vechev, Martin},
  journal={International Conference on Machine Learning},
  year={2025}
}"

paper: https://arxiv.org/abs/2505.23786
code: https://github.com/eth-sri/llm-quantization-attack
---

With the increasing size of frontier LLMs, post-training quantization has become the standard for memory-efficient deployment. Recent work has shown that basic rounding-based quantization schemes pose security risks, as they can be exploited to inject malicious behaviors into quantized models that remain hidden in full precision. However, existing attacks cannot be applied to more complex quantization methods, such as the GGUF family used in the popular ollama and llama.cpp frameworks. In this work, we address this gap by introducing the first attack on GGUF. Our key insight is that the quantization error – the difference between the full-precision weights and their (de-)quantized version – provides sufficient flexibility to construct malicious quantized models that appear benign in full precision. Leveraging this, we develop an attack that trains the target malicious LLM while constraining its weights based on quantization errors. We demonstrate the effectiveness of our attack on three popular LLMs across nine GGUF quantization data types on three diverse attack scenarios: insecure code generation (∆=88.7%), targeted content injection (∆=85.0%), and benign instruction refusal (∆=30.1%). Our attack highlights that (1) the most widely used post-training quantization method is susceptible to adversarial interferences, and (2) the complexity of quantization schemes alone is insufficient as a defense.