---
ref: muendler2026generative
title: "Generative Compilation: On-the-Fly Compiler Feedback as AI Generates Code"
authors: Niels Mündler-Sasahara*, Hristo Venev*, Dawn Song, Martin Vechev, Jingxuan He
year: 2026
month: 07
day: 15
venue: arXiv
projects: codellm,cclm
bibtex: "@misc{muendler2026generativecompilationontheflycompilerfeedback,
      title={Generative Compilation: On-the-Fly Compiler Feedback as AI Generates Code},
      author={Niels Mündler-Sasahara and Hristo Venev and Dawn Song and Martin Vechev and Jingxuan He},
      year={2026},
      eprint={2607.13921},
      archivePrefix={arXiv},
      primaryClass={cs.PL},
      url={https://arxiv.org/abs/2607.13921},
}"
paper: https://arxiv.org/abs/2607.13921
code: https://github.com/eth-sri/generative-compilation
---

Languages with rich static semantics, such as Rust, provide stronger guarantees for AI-generated code, but their strictness makes generation more difficult. Off-the-shelf compilers can provide useful feedback post-generation, but does not guide intermediate generation steps, such as those during autoregressive LLM decoding. Constrained decoding intervenes earlier by rejecting invalid tokens during sampling, but requires white-box model access and costly reimplementation for semantic constraints. We introduce generative compilation, the first approach to obtaining compiler feedback on partial programs during generation. The core technical device is a sealor: a lightweight, mostly syntax-guided transformation that converts partial programs into complete ones that standard compilers can diagnose. It is designed such that possible-to-complete partial programs are never rejected, while preserving enough code context to catch genuine dead ends early. We construct such a sealor on a core Rust-like calculus and prove that it satisfies these properties, all mechanized in Lean. We extend it to the first partial-program checker for real Rust. We evaluate our method on challenging repository-level Rust coding tasks, across both frontier black-box and open-weight models. We show that generative compilation reduces non-compiling outputs and improves functional correctness, relative to standard post-generation feedback. It does so by detecting a broad range of errors close to their source and early during generation, thereby reducing errors cascades and enabling focused diagnostics. More broadly, generative compilation is a step toward making compilers a first-class citizen of AI-assisted programming active during generation, rather than a separate post-generation check.
