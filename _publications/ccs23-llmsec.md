---
  ref: ccs23-llmsec
  title: "Large Language Models for Code: Security Hardening and Adversarial Testing"
  authors: Jingxuan He, Martin Vechev
  year: 2023
  month: 11
  venue: ACM CCS
  projects: plml,safeai,llm
  awards: Distinguished Paper Award
  bibtex:
  paper: https://arxiv.org/pdf/2302.05319.pdf
  image: assets/images/ccs23-img.jpg
  talk: 
  slides: https://files.sri.inf.ethz.ch/website/slides/ccs23-sven-slides.pdf
  code: https://github.com/eth-sri/sven
---

Large language models (LMs) are increasingly pretrained on massive codebases and used to generate code. However, LMs lack awareness of security and are found to frequently produce unsafe code. This work studies the security of LMs along two important axes: (i) security hardening, which aims to enhance LMs' reliability in generating secure code, and (ii) adversarial testing, which seeks to evaluate LMs' security at an adversarial standpoint. We address both of these by formulating a new security task called controlled code generation. The task is parametric and takes as input a binary property to guide the LM to generate secure or unsafe code, while preserving the LM's capability of generating functionally correct code. We propose a novel learning-based approach called SVEN to solve this task. SVEN leverages property-specific continuous vectors to guide program generation towards the given property, without modifying the LM's weights. Our training procedure optimizes these continuous vectors by enforcing specialized loss terms on different regions of code, using a high-quality dataset carefully curated by us. Our extensive evaluation shows that SVEN is highly effective in achieving strong security control. For instance, a state-of-the-art CodeGen LM with 2.7B parameters generates secure code for 59.1% of the time. When we employ SVEN to perform security hardening (or adversarial testing) on this LM, the ratio is significantly boosted to 92.3% (or degraded to 36.8%). Importantly, SVEN closely matches the original LMs in functional correctness.
