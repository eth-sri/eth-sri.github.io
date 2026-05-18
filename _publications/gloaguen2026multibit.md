---
ref: gloaguen2026multibit
title: "Every Bit, Everywhere, All at Once: A Binomial Multibit LLM Watermark"
authors: Thibaud Gloaguen, Robin Staab, Mark Vero, Martin Vechev
year: 2026
month: 05
venue: arXiv
projects: watermarks
bibtex: "@article{gloaguen2026every,
  title={Every Bit, Everywhere, All at Once: A Binomial Multibit LLM Watermark},
  author={Gloaguen, Thibaud and Staab, Robin and Vero, Mark and Vechev, Martin},
  journal={arXiv preprint arXiv:2605.11653},
  year={2026}
}
"
paper: https://arxiv.org/abs/2605.11653
---

With LLM watermarking already being deployed commercially, practical applications increasingly require multibit watermarks that encode more complex payloads, such as user IDs or timestamps, into the generated text. In this work, we propose a fundamentally new approach for multibit watermarking: introducing binomial encoding to directly encode every bit of the payload at every token position. We complement our approach with a stateful encoder that during generation dynamically redirects encoding pressure toward underencoded bits. Our evaluation against 8 baselines on up to 64-bit payloads shows that our scheme achieves superior message accuracy and robustness, with the gap to baseline methods widening in more relevant settings (i.e., large payloads and low-distortion regimes). At the same time, we challenge prior works' evaluation metrics, highlighting their lack of practical insights, and introduce per-bit confidence scoring as a practically relevant metric for evaluating multibit LLM watermarks.