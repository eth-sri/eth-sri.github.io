---
ref: singh2018effective
title: Fast and Effective Robustness Certification
authors: Gagandeep Singh, Timon Gehr, Matthew Mirman, Markus Püschel, Martin Vechev
year: 2018
month: 12
venue: NIPS
projects: safeai
awards:
bibtex:
paper: https://files.sri.inf.ethz.ch/website/papers/DeepZ.pdf
talk: 
slides: https://files.sri.inf.ethz.ch/website/slides/DeepZ.pdf
---


We present a new method and system, called DeepZ, for certifying neural network robustness based on abstract interpretation. Compared to state-of-the-art automated verifiers for neural networks, DeepZ: (i) handles ReLU, Tanh and Sigmoid activation functions, (ii) supports feedforward and convolutional architectures, (iii) is significantly more scalable and precise, and (iv) and is sound with respect to floating point arithmetic. These benefits are due to carefully designed approximations tailored to the setting of neural networks. As an example, DeepZ achieves a verification accuracy of 97% on a large network with 88,500 hidden units under L_inf attack with epsilon = 0.1 with an average runtime of 133 seconds.
