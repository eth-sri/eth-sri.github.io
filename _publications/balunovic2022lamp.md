---
ref: balunovic2022lamp
title: "LAMP: Extracting Text from Gradients with Language Model Priors"
authors: Dimitar I. Dimitrov*, Mislav Balunović*, Nikola Jovanović, Martin Vechev
year: 2022
month: 2
venue: arXiv
projects: safeai
bibtex: '@misc{https://doi.org/10.48550/arxiv.2202.08827,
  doi = {10.48550/ARXIV.2202.08827},
  url = {https://arxiv.org/abs/2202.08827},
  author = {Dimitrov, Dimitar I. and Balunović, Mislav and Jovanović, Nikola and Vechev, Martin},
  keywords = {Machine Learning (cs.LG), Distributed, Parallel, and Cluster Computing (cs.DC), FOS: Computer and information sciences, FOS: Computer and information sciences, I.2.7; I.2.11},
  title = {LAMP: Extracting Text from Gradients with Language Model Priors},
  publisher = {arXiv},
  year = {2022},  
  copyright = {Creative Commons Attribution 4.0 International}
}'
paper: https://arxiv.org/abs/2202.08827
---
Recent work shows that sensitive user data can be reconstructed from gradient updates, breaking the key privacy promise of federated learning. While success was demonstrated primarily on image data, these methods do not directly transfer to other domains such as text. In this work, we propose LAMP, a novel attack tailored to textual data, that successfully reconstructs original text from gradients. Our key insight is to model the prior probability of the text with an auxiliary language model, utilizing it to guide the search towards more natural text. Concretely, LAMP introduces a discrete text transformation procedure that minimizes both the reconstruction loss and the prior text probability, as provided by the auxiliary language model. The procedure is alternated with a continuous optimization of the reconstruction loss, which also regularizes the length of the reconstructed embeddings. Our experiments demonstrate that LAMP reconstructs the original text significantly more precisely than prior work: we recover 5x more bigrams and 23% longer subsequences on average. Moreover, we are first to recover inputs from batch sizes larger than 1 for textual models. These findings indicate that gradient updates of models operating on textual data leak more information than previously thought.
