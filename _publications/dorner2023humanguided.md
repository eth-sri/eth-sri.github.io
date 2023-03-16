---
ref: dorner2023humanguided
title: "Human-Guided Fair Classification for Natural Language Processing"
authors: Florian E. Dorner, Momchil Peychev, Nikola Konstantinov, Naman Goel, Elliott Ash, Martin Vechev
year: 2023
month: 05
venue: ICLR (Spotlight)
projects: safeai
paper: https://openreview.net/pdf?id=N_g8TT9Cy7f
code: https://github.com/eth-sri/fairness-feedback-nlp
bibtex: '@inproceedings{
	dorner2023humanguided,
	title={Human-Guided Fair Classification for Natural Language Processing},
	author={Florian E. Dorner and Momchil Peychev and Nikola Konstantinov and Naman Goel and Elliott Ash and Martin Vechev},
	booktitle={The Eleventh International Conference on Learning Representations },
	year={2023},
	url={https://openreview.net/forum?id=N_g8TT9Cy7f}}'
---

Text classifiers have promising applications in high-stake tasks such as resume screening and content moderation. These classifiers must be fair and avoid discriminatory decisions by being invariant to perturbations of sensitive attributes such as gender or ethnicity. However, there is a gap between human intuition about these perturbations and the formal similarity specifications capturing them. While existing research has started to address this gap, current methods are based on hardcoded word replacements, resulting in specifications with limited expressivity or ones that fail to fully align with human intuition (e.g., in cases of asymmetric counterfactuals). This work proposes novel methods for bridging this gap by discovering expressive and intuitive individual fairness specifications. We show how to leverage unsupervised style transfer and GPT-3's zero-shot capabilities to automatically generate expressive candidate pairs of semantically similar sentences that differ along sensitive attributes. We then validate the generated pairs via an extensive crowdsourcing study, which confirms that a lot of these pairs align with human intuition about fairness in the context of toxicity classification. Finally, we show how limited amounts of human feedback can be leveraged to learn a similarity specification that can be used to train downstream fairness-aware models.
