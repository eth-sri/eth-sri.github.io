---
ref: dimitar::2020
title:  "Scalable Inference of Symbolic Adversarial Examples"
projects: safeai
authors: Dimitar I. Dimitrov, Gagandeep Singh, Timon Gehr, Martin Vechev
year: 2020
month: 07
bibtex: '@misc{dimitrov2020scalable,
    title={Scalable Inference of Symbolic Adversarial Examples},
    author={Dimitar I. Dimitrov and Gagandeep Singh and Timon Gehr and Martin Vechev},
    year={2020},
    eprint={2007.12133},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}'
paper: https://files.sri.inf.ethz.ch/website/papers/symex.pdf
slides: 
venue: Arxiv
---
We present a novel method for generating symbolic adversarial examples: input regions \emph{guaranteed} to only contain adversarial examples for the given neural network. These regions can generate real-world adversarial examples as they summarize trillions of adversarial examples.
	
We theoretically show that computing optimal symbolic adversarial examples is computationally expensive. We present a method for approximating optimal examples in a scalable manner. Our method first selectively uses adversarial attacks to generate a candidate region and then prunes this region with hyperplanes that fit points obtained via specialized sampling. It iterates until arriving at a symbolic adversarial example for which it can prove, via state-of-the-art convex relaxation techniques, that the region only contains adversarial examples. Our experimental results demonstrate that our method is practically effective: it only needs a few thousand attacks to infer symbolic summaries guaranteed to contain $\approx 10^{258}$ adversarial examples.
