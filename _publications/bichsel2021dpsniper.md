---
ref: bichsel2021dpsniper
title: "DP-Sniper: Black-Box Discovery of Differential Privacy Violations using Classifiers"
authors: Benjamin Bichsel, Samuel Steffen, Ilija Bogunovic, Martin Vechev
year: 2021
month: 05
venue: IEEE S&P
projects: probabilistic-programming, diff-privacy
awards:
bibtex: ''
<!--blogpost: dpsniper-->
paper: https://files.sri.inf.ethz.ch/website/papers/sp21-dpsniper.pdf
talk: https://www.youtube.com/watch?v=M1O-omGZ2QE&list=PLWjm4hHpaNg7WjYyCnj7nHFvHWXmHfm4u&index=1
slides: https://files.sri.inf.ethz.ch/website/slides/sp21-dpsniper-slides.pdf
code: https://github.com/eth-sri/dp-sniper
---

We present DP-Sniper, a practical black-box method that automatically finds violations of differential privacy.

DP-Sniper is based on two key ideas: (i) training a classifier to predict if an observed output was likely generated from one of two possible inputs, and (ii) transforming this classifier into an approximately optimal attack on differential privacy.

Our experimental evaluation demonstrates that DP-Sniper obtains up to 12.4 times stronger guarantees than state-of-the-art, while being 15.5 times faster. Further, we show that DP-Sniper is effective in exploiting floating-point vulnerabilities of naively implemented algorithms: it detects that a supposedly 0.1-differentially private implementation of the Laplace mechanism actually does not satisfy even 0.25-differential privacy.
