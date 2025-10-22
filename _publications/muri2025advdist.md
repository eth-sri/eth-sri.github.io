---
ref: muri2025advdist
title: "Pay Attention to the Triggers: Constructing Backdoors That Survive Distillation"
authors: Giovanni De Muri, Mark Vero, Robin Staab, Martin Vechev
year: 2025
month: 10
venue: arXiv
projects: llmsecpriv
bibtex: "@article{muri2025advdist,
  title={Pay Attention to the Triggers: Constructing Backdoors That Survive Distillation},
  author={de Muri, Giovanni and Vero, Mark and Staab, Robin and Vechev, Martin},
  journal={arXiv},
  year={2025}
}"

paper: https://arxiv.org/abs/2510.18541
---

LLMs are often used by downstream users as teacher models for knowledge distillation, compressing their capabilities into memory-efficient models. However, as these teacher models may stem from untrusted parties, distillation can raise unexpected security risks. In this paper, we investigate the security implications of knowledge distillation from backdoored teacher models. First, we show that prior backdoors mostly do not transfer onto student models. Our key insight is that this is because existing LLM backdooring methods choose trigger tokens that rarely occur in usual contexts. We argue that this underestimates the security risks of knowledge distillation and introduce a new backdooring technique, T-MTB, that enables the construction and study of transferable backdoors. T-MTB carefully constructs a composite backdoor trigger, made up of several specific tokens that often occur individually in anticipated distillation datasets. As such, the poisoned teacher remains stealthy, while during distillation the individual presence of these tokens provides enough signal for the backdoor to transfer onto the student. Using T-MTB, we demonstrate and extensively study the security risks of transferable backdoors across two attack scenarios, jailbreaking and content modulation, and across four model families of LLMs.