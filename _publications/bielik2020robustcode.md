---
ref: bielik2020robustcode
title: Adversarial Robustness for Code
authors: Pavol Bielik, Martin Vechev 
year: 2020
month: 2
venue: ArXiv
projects: plml
awards:
bibtex: '@misc{bielik2020adversarial,
             title={Adversarial Robustness for Code},
             author={Pavol Bielik and Martin Vechev},
             year={2020},
             eprint={2002.04694},
             archivePrefix={arXiv},
             primaryClass={cs.LG}
}'
paper: https://arxiv.org/pdf/2002.04694.pdf
talk: 
slides: 
---

We propose a novel technique which addresses the challenge of learning accurate and robust models of code in a principled way. Our method consists of three key components: (i) learning to abstain from making a prediction if uncertain, (ii) adversarial training, and (iii) representation refinement which learns the program parts relevant for the prediction and abstracts the rest. These components are used to iteratively train multiple models, each of which learns a suitable program representation necessary to make robust predictions on a different subset of the dataset.

We instantiated our approach to the task of type inference for dynamically typed languages and demonstrate its effectiveness by learning a model that achieves 88% accuracy and 84% robustness. Further, our evaluation shows that using the combination of all three components is key to obtaining accurate and robust models.
