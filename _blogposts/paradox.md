---
layout: blogpost
category: paper
pub-ref: jovanovic2022paradox
title: "Why do tighter convex relaxations harm certified training?"
blogpost-authors: "Nikola Jovanović"
date: 2022-10-27
thumbnail: thumbnails/paradox.svg
usemathjax: true
tldr: >
    In our TMLR paper we investigate a well-known paradox of certified training, where most state-of-the-art approaches use the loose interval-based relaxation, as using tighter convex relaxations in training seem to lead to worse results. We identify two previously overlooked properties of relaxations: continuity and sensitivity, which are generally unfavorable for tighter relaxation, harming the optimization procedure. We further explore possible next steps, and discuss the effect of our findings on the field.
excerpt: >
    We provide insights into a long-standing paradox of certified training with convex relaxations.

tweet-id: 
---

This blog discusses our paper [On the Paradox Of Certified Training](https://files.sri.inf.ethz.ch/website/papers/jovanovic2022paradox.pdf), recently published in TMLR. 

The paper tries to explain the phenomenon where most state-of-the-art neural network certification methods based on convex relaxations (such as [FastIBP](https://proceedings.neurips.cc/paper/2021/file/988f9153ac4fd966ea302dd9ab9bae15-Paper.pdf) or the recent [SABR](https://arxiv.org/abs/2210.04871)) focus on the loose interval propagation. While intuitively, tighter relaxations should perform better in training, this doesn't seem to be the case as shown many times before ([here](todo), [here](todo), or [here](todo)). The paradox is illustrated in the following table: 

| Relaxation | Tightness | Certified (%) 
|-------------|-------:|----------: 
| IBP / Box | 0.73 | <span style="color:blue"> 86.86 </span>
|-------------|-------:|----------: 
| IBP / Box | 0.73 | 86.8 
| IBP / Box | 0.73 | 86.8 
| IBP / Box | 0.73 | 86.8 
| IBP / Box | 0.73 | 86.8 
|-------------|-------:|----------: 

We then do a lot more.

TODO can we have 2 sliders (for L and U), and then live plot Box / hBox / CROWN? this would nicely illustrate the continuity 