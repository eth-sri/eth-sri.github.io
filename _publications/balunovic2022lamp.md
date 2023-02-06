---
ref: balunovic2022lamp
title: "LAMP: Extracting Text from Gradients with Language Model Priors"
authors: Mislav Balunović*, Dimitar I. Dimitrov*, Nikola Jovanović, Martin Vechev
year: 2022
month: 12
venue: NeurIPS
projects: safeai
bibtex: '@inproceedings{balunovic2022lamp,
    title={LAMP: Extracting Text from Gradients with Language Model Priors},
    author={Mislav Balunović and Dimitar I. Dimitrov and Nikola Jovanović and Martin Vechev},
    booktitle={Conference on Neural Information Processing Systems},
    year={2022}
}'
code: https://github.com/eth-sri/lamp
paper: https://files.sri.inf.ethz.ch/website/papers/balunovic2022lamp.pdf
blogpost: lamp
---
Recent work shows that sensitive user data can be reconstructed from gradient updates, breaking the key privacy promise of federated learning. While success was demonstrated primarily on image data, these methods do not directly transfer to other domains such as text. In this work, we propose LAMP, a novel attack tailored to textual data, that successfully reconstructs original text from gradients. Our attack is based on two key insights: (i) modeling prior text probability with an auxiliary language model, guiding the search towards more natural text, and (ii) alternating continuous and discrete optimization, which minimizes reconstruction loss on embeddings, while avoiding local minima by applying discrete text transformations. Our experiments demonstrate that LAMP is significantly more effective than prior work: it reconstructs 5x more bigrams and 23% longer subsequences on average. Moreover, we are the first to recover inputs from batch sizes larger than 1 for textual models. These findings indicate that gradient updates of models operating on textual data leak more information than previously thought.
