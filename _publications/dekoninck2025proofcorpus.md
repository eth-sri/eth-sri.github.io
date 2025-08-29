---
ref: balunovic2025matharena
title: "The Open Proof Corpus: A Large-Scale Study of LLM-Generated Mathematical Proofs"
authors: Jasper Dekoninck, Ivo Petrov,  Kristian Minchev, Mislav Balunovic, Martin Vechev, Miroslav Marinov, Maria Drencheva, Lyuba Konova, Milen Milenov Shumanov, Kaloyan Tsvetkov, Nikolay Drenchev, Lazar D. Todorov, Kalina Nikolova, Nikolay Georgiev, Vanesa Kalinkova, Margulan Ismoldayev
year: 2025
month: 06
venue: arXiv
projects: mathllm,llmevals
bibtex: '@article{openproofcorpus2025,
  title={The Open Proof Corpus: A Large-Scale Human Study of LLM Proofs},
  author={Jasper Dekoninck and Ivo Petrov and  Kristian Minchev and Mislav Balunovic and Martin Vechev and Miroslav Marinov and Maria Drencheva and Lyuba Konova and Milen Milenov Shumanov and Kaloyan Tsvetkov and Nikolay Drenchev and Lazar D. Todorov and Kalina Nikolova and Nikolay Georgiev and Vanesa Kalinkova and Margulan Ismoldayev},
  journal={arXiv},
  year={2025},
}'
paper: https://files.sri.inf.ethz.ch/website/papers/dekoninck2025proofcorpus.pdf
code: https://github.com/insait-institute/open-proof-corpus
website: https://proofcorpus.ai/
---
In recent months, large language models (LLMs) have made significant progress in mathematical proof generation, but further advancement is hindered by the lack of a large-scale, high-quality dataset of human-evaluated proofs. While expensive to create, such a dataset is essential for driving improvements in training and enabling a rigorous analysis of proof generation capabilities. In this work, we present the Open Proof Corpus (OPC), a dataset comprising over 5,000 human-evaluated proofs produced by state-of-the-art LLMs. The OPC was specifically designed for broad applicability and downstream usage in proof generation research and is the first to include a substantial number of correct, LLM-generated solutions to problems from prestigious mathematics competitions such as the USAMO and IMO. Using the OPC, we explore critical questions in automated proof generation: (1) the performance gap between natural language and formal proof generation, (2) the discrepancy between final-answer accuracy and full-proof validity, and (3) the impact of best-of-n selection on proof quality. Finally, to showcase the utility of the OPC, we finetune an 8B-parameter model on the dataset, obtaining a model that performs on par with the best model, Gemini-2.5-Pro, on the task of evaluating proof correctness.