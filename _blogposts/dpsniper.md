---
layout: blogpost
category: paper
pub-ref: bichsel2021dpsniper
title: "DP is sometimes not really DP"
blogpost-authors: "Benjamin Bichsel, Samuel Steffen"
date: 2021-09-01
thumbnail: _thumbnails/dpsniper.svg
usemathjax: true
tldr: >
    DP-Sniper automatically finds violations of differential 
    privacy, by training a classifier to predict if an observed 
    output was likely generated from one of two possible inputs. 
    We show that DP-Sniper is effective in exploiting floating-point 
    vulnerabilities of naively implemented algorithms: we detect that
    a supposedly 0.1-differentially private implementation of the Laplace
    mechanism actually does not satisfy even 0.25-differential privacy.
excerpt: We present a system that automatically finds violations of differential privacy.

draft: false
tweet-id: 1447996320741007362
---

We presented DP-Sniper, a practical approach which leverages classifiers to
demonstrate that a given algorithm is differentially distinguishable. DP-Sniper
finds approximately optimal attacks in terms of $c$-power, and takes into
account that we cannot accurately estimate small probabilities. Compared to a
strengthened baseline, we can prove substantially stronger differential
distinguishability. We expect that future work can generalize our approach to
($\epsilon$, $\delta$)-DP by generalizing the notion of $c$-power.