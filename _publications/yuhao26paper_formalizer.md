---
ref: yuhao26paper_formalizer
title: "Paper Formalization for Efficient and Rigorous Proof Review"
authors: Yuhao Mao, Chenhao Sun, Yani Zhang, Martin Vechev
year: 2026
month: 10
projects: mathllm
paper: https://files.sri.inf.ethz.ch/website/papers/yuhao2026paper_formalizer.pdf
# slides: https://files.sri.inf.ethz.ch/website/slides/mueller2023sabr_slides.pdf
#poster: https://files.sri.inf.ethz.ch/website/slides/mueller2021boosting_poster.pdf
# image: assets/images/taps.png
#talk: https://iclr.cc/virtual/2021/poster/3359
---

Reviewing mathematical proofs is demanding. In our survey of NeurIPS, ICML, and ICLR in 2025, reviewers report checking at least part of a proof for only 28.4% of theoretical publications with proofs. Although missing reports do not establish that proofs go unchecked, this limited reported coverage motivates additional support for rigorous proof review. Proof assistants such as Lean could reduce this burden by automatically checking reasoning, but applying them to frontier proofs presents two challenges. First, complete formalization can unnecessarily require formalizing many results outside the paper. Second, assessing faithfulness, the semantic alignment between the formalization and the original mathematics, can require inspecting a large formal body. To address these challenges, we define Paper Formalization, propose four metrics for this task, and develop Paper Formalizer as a solution. Paper Formalization makes internal arguments machine-checkable while exposing external results as explicit dependencies, allowing each correct paper argument to be formalized without recursively formalizing all dependencies. Paper Formalizer solves the Paper Formalization task while minimizing the review burden. Across theoretical papers spanning multiple topics, Paper Formalizer with GPT-6-Astra uses approximately 90% fewer custom definitions and 64% fewer explicit axioms than the purely agentic baseline. Beyond these reductions, it faithfully formalizes more goals than purely agentic baselines with both GPT-6-Astra and GPT-5.6-Sol. With GPT-6-Astra, it achieves 100% faithfulness, confirmed by two independent human reviewers. Furthermore, in collaborations with authors of three additional publications, Paper Formalizer helps identify and correct theorem-statement typos, ambiguous proof arguments, and incorrect results. After these corrections, it faithfully formalizes all goals in these publications without further human intervention. These results support Paper Formalization as a practical supplement to proof review and Paper Formalizer as a useful tool for authors to improve their proofs, with the potential to make proof review more efficient and rigorous.
