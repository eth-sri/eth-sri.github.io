---
ref: dimitrov2022provably
title:  "Provably Robust Adversarial Examples"
projects: safeai
authors: Dimitar I. Dimitrov, Gagandeep Singh, Timon Gehr, Martin Vechev
year: 2022
month: 4
bibtex: '@inproceedings{
    dimitrov2022provably,
    title={Provably Robust Adversarial Examples},
    author={Dimitar Iliev Dimitrov and Gagandeep Singh and Timon Gehr and Martin Vechev},
    booktitle={International Conference on Learning Representations},
    year={2022},
    url={https://openreview.net/forum?id=UMfhoMtIaP5}
}'
paper: https://files.sri.inf.ethz.ch/website/papers/symex.pdf
slides: https://files.sri.inf.ethz.ch/website/papers/iclr2022-parade-poster.pdf 
venue: ICLR
---
We introduce the concept of provably robust adversarial examples for deep neural networks -- connected input regions constructed from standard adversarial examples which are guaranteed to be robust to a set of real-world perturbations (such as changes in pixel intensity and geometric transformations). We present a novel method called PARADE for generating these regions in a scalable manner which works by iteratively refining the region initially obtained via sampling until a refined region is certified to be adversarial with existing state-of-the-art verifiers. At each step, a novel optimization procedure is applied to maximize the region's volume under the constraint that the convex relaxation of the network behavior with respect to the region implies a chosen bound on the certification objective. Our experimental evaluation shows the effectiveness of PARADE: it successfully finds large provably robust regions including ones containing $\approx 10^{573}$ adversarial examples for pixel intensity and $\approx 10^{599}$ for geometric perturbations. The provability enables our robust examples to be significantly more effective against state-of-the-art defenses based on randomized smoothing than the individual attacks used to construct the regions.
