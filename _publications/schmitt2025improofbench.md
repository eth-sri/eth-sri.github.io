---
ref: schmitt2025improofbench
title: "IMProofBench: Benchmarking AI on Research-Level Mathematical Proof Generation"
authors: Johannes Schmitt, Gergely Bérczi, Jasper Dekoninck, Jeremy Feusi, Tim Gehrunger, Raphael Appenzeller, Jim Bryan, Niklas Canova, Timo de Wolff, Filippo Gaia, Michel van Garrel, Baran Hashemi, David Holmes, Aitor Iribar Lopez, Victor Jaeck, Martina Jørgensen, Steven Kelk, Stefan Kuhlmann, Adam Kurpisz, Chiara Meroni, Ingmar Metzler, Martin Möller, Samuel Muñoz-Echániz, Robert Nowak, Georg Oberdieck, Daniel Platt, Dylan Possamaï, Gabriel Ribeiro, Raúl Sánchez Galán, Zheming Sun, Josef Teichmann, Richard P. Thomas, Charles Vial
year: 2025
month: 10
venue: ArXiv
projects: mathllm,llmevals
bibtex: "@misc{schmitt2025improofbenchbenchmarkingairesearchlevel,
      title={IMProofBench: Benchmarking AI on Research-Level Mathematical Proof Generation}, 
      author={Johannes Schmitt and Gergely Bérczi and Jasper Dekoninck and Jeremy Feusi and Tim Gehrunger and Raphael Appenzeller and Jim Bryan and Niklas Canova and Timo de Wolff and Filippo Gaia and Michel van Garrel and Baran Hashemi and David Holmes and Aitor Iribar Lopez and Victor Jaeck and Martina Jørgensen and Steven Kelk and Stefan Kuhlmann and Adam Kurpisz and Chiara Meroni and Ingmar Metzler and Martin Möller and Samuel Muñoz-Echániz and Robert Nowak and Georg Oberdieck and Daniel Platt and Dylan Possamaï and Gabriel Ribeiro and Raúl Sánchez Galán and Zheming Sun and Josef Teichmann and Richard P. Thomas and Charles Vial},
      year={2025},
      eprint={2509.26076},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2509.26076}, 
}"
paper: https://arxiv.org/pdf/2509.26076
website: https://improofbench.math.ethz.ch/
---

As the mathematical capabilities of large language models (LLMs) improve, it becomes increasingly important to evaluate their performance on research-level tasks at the frontier of mathematical knowledge. However, existing benchmarks are limited, as they focus solely on final-answer questions or high-school competition problems. To address this gap, we introduce IMProofBench, a private benchmark consisting of 39 peer-reviewed problems developed by expert mathematicians. Each problem requires a detailed proof and is paired with subproblems that have final answers, supporting both an evaluation of mathematical reasoning capabilities by human experts and a large-scale quantitative analysis through automated grading. Furthermore, unlike prior benchmarks, the evaluation setup simulates a realistic research environment: models operate in an agentic framework with tools like web search for literature review and mathematical software such as SageMath. Our results show that current LLMs can succeed at the more accessible research-level questions, but still encounter significant difficulties on more challenging problems. Quantitatively, Grok-4 achieves the highest accuracy of 52% on final-answer subproblems, while GPT-5 obtains the best performance for proof generation, achieving a fully correct solution for 22% of problems. IMProofBench will continue to evolve as a dynamic benchmark in collaboration with the mathematical community, ensuring its relevance for evaluating the next generation of LLMs.