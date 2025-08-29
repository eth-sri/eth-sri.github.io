---
ref: jenko2025blackbox
title: "Black-Box Adversarial Attacks on LLM-Based Code Completion"
authors: Slobodan Jenko*, Niels Mündler*, Jingxuan He, Mark Vero, Martin Vechev
year: 2025
month: 07
projects: codellm, llmsecpriv
awards:
code:
venue: ICML
paper: https://openreview.net/pdf?id=jSYBqtOJS4
bibtex: "@inproceedings{
jenko2025blackbox,
title={Black-Box Adversarial Attacks on {LLM}-Based Code Completion},
author={Slobodan Jenko and Niels M{\"u}ndler and Jingxuan He and Mark Vero and Martin Vechev},
booktitle={Forty-second International Conference on Machine Learning},
year={2025},
url={https://openreview.net/forum?id=jSYBqtOJS4}
}"
---

Modern code completion engines, powered by large language models (LLMs), assist millions of developers with their strong capabilities to generate functionally correct code. Due to this popularity, it is crucial to investigate the security implications of relying on LLM-based code completion. In this work, we demonstrate that state-of-the-art black-box LLM-based code completion engines can be stealthily biased by adversaries to significantly increase their rate of insecure code generation. We present the first attack, named INSEC, that achieves this goal. INSEC works by injecting an attack string as a short comment in the completion input. The attack string is crafted through a query-based optimization procedure starting from a set of carefully designed initialization schemes. We demonstrate INSEC's broad applicability and effectiveness by evaluating it on various state-of-the-art open-source models and black-box commercial services (e.g., OpenAI API and GitHub Copilot). On a diverse set of security-critical test cases, covering 16 CWEs across 5 programming languages, INSEC increases the rate of generated insecure code by more than 50%, while maintaining the functional correctness of generated code. We consider INSEC practical - it requires low resources and costs less than 10 US dollars to develop on commodity hardware. Moreover, we showcase the attack's real-world deployability, by developing an IDE plug-in that stealthily injects INSEC into the GitHub Copilot extension.