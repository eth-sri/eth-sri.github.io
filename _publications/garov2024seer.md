---
ref: garov2024seer
title: "Hiding in Plain Sight: Disguising Data Stealing Attacks in Federated Learning"
authors: Kostadin Garov, Dimitar I. Dimitrov, Nikola Jovanović, Martin Vechev
year: 2024
month: 05
venue: ICLR
projects: safeai
bibtex: '@inproceedings{
			garov2024seer,  
			title={Hiding in Plain Sight: Disguising Data Stealing Attacks in Federated Learning},  
			author={Kostadin Garov and Dimitar I. Dimitrov and Nikola Jovanović and Martin Vechev},  
			booktitle={International Conference on Learning Representations},  
			year={2024}
		}'
paper: https://files.sri.inf.ethz.ch/seer/seer.pdf
---

Malicious server (MS) attacks have enabled the scaling of data stealing in federated learning to large batch sizes and secure aggregation, settings previously considered private. However, many concerns regarding the client-side detectability of MS attacks were raised, questioning their practicality. In this work, for the first time, we thoroughly study client-side detectability. We first demonstrate that all prior MS attacks are detectable by principled checks, and formulate a necessary set of requirements that a practical MS attack must satisfy. Next, we propose SEER, a novel attack framework that satisfies these requirements. The key insight of SEER is the use of a secret decoder, jointly trained with the shared model. We show that SEER can steal user data from gradients of realistic networks, even for large batch sizes of up to 512 and under secure aggregation. Our work is a promising step towards assessing the true vulnerability of federated learning in real-world settings.
