---
layout: blogpost
category: paper
pub-ref: dimitrov2022provably
title: "Generating provably robust adversarial examples"
blogpost-authors: "Dimitar I. Dimitrov" 
date: 2022-04-21
thumbnail: _thumbnails/parade.svg
usemathjax: true
tldr: >
    We introduce the concept of provably robust adversarial examples in deep neural networks. These are adversarial examples that are generated together with a region around them proven to be robust to a set of perturbations.
    We demonstrate our method, PARADE, for generating such examples in a scalable manner that uses adversarial attack algorithms to generate a candidate region which is then refined until proven robust.
    Our experiments show PARADE successfully finds large provably robust regions to both pixel intensity and geometric pertrubations containing up to $10^{573}$ and $10^{599}$ individual adversarial examples, respectively. 
excerpt: >
    We introduce the concept of provably robust adversarial examples. These are adversarial examples that are generated together with a region around them that can be proven robust to perturbations. 
    We also show a method for generating large such regions in a scalable manner.
keywords: adversarial examples, robustness
conf-url: https://iclr.cc/virtual/2022/poster/6160
conf-info: Poster - Tue Apr 26, 19:30 UTC+2 (Poster Session 5)

draft: true
tweet-id:
---


{:.blogpost-caption}
***Conceptual overview of LCIFR.** This is a full-width gif. Start captions with a bold caption heading.*


### Algorithm overview
There are three main steps to **PARADE**. First, we generate an initial box region that might contain non-adversarial points using off-the-shelf adversarial attacks. 
We refer to this region as the overapproximation box $\mathcal{O}$. Then, we use a black-box verifier to shrink this overapproximation box to a smaller box that provably contains only adversarial points. We call this region the underapproximation box $\mathcal{U}$.
Finally, we use  $\mathcal{O}$ and $\mathcal{U}$ to generate a polyhedral region  $\mathcal{U}\subseteq\mathcal{P}\subseteq\mathcal{O}$ that we also prove only contains adversarial points using the same black-box verifier. Both $\mathcal{U}$ and $\mathcal{P}$ fit our definition of 
provably robust adversarial examples but differ in terms of shape and precision. To this end, the generation of $\mathcal{P}$ is only an optional way to make our provably robust adversarial examples more precise. Next, we present the **PARADE** steps in details. 

### Generating the overapproximation box  $\mathcal{O}$
<iframe src="/assets/blog/parade/over.svg" style="border: none;;width: 100%;height: 200pt;"></iframe>
To generate the overapproximation box $\mathcal{O}$, we sample attacks from an adversarial attack algorithm, such as **PGD**. Then, we fit a box around them. The process is illustateted in the animation above. 
We note that depending on the success of the attack algorithm, a small part of the ground truth adversarial region $\mathcal{T}$ might be excluded from $\mathcal{O}$.

### Generating the underapproximation box  $\mathcal{U}$
<iframe src="/assets/blog/parade/under.svg" style="border: none;;width: 100%;height: 264pt;"></iframe>
We aim to generate the underapproximation box $\mathcal{U}$ in a way that it can be proven to only contain adversarial examples while also being as large as possible. Due to the complexity of this objective, we do this heuristically. In particular, we start by initializing $\mathcal{U}$
to the overapproximation box $\mathcal{O}$. At each iteration $i$, we execute a black-box verification procedure. If the procedure verifies that the box from the previous iteration, $\mathcal{U}\_{i-1}$, contains only adversarial examples, we return it. 
Otherwise, we obtain from the verifier a linear contraint, which can be added to $\mathcal{U}\_{i-1}$ in order to make it provably robust. Unfortunately, the constraint is usually too conservative, as the black-box verifier relies on overapproximation of the set of possible network outputs. To this end, we relax the constraint by bias-adjusting it.
We make sure that we cannot relax the constraint too much, such that it becomes meaningless. We use the bias-adjusted contraint to shrink $\mathcal{U}\_{i-1}$ such that the constraint is not violated but the smallest possible amount of volume is lost. The procedure is repeated until the verification succeeds. The process is depicted in the animation above.

### Generating the polyhedral region  $\mathcal{P}$
<iframe src="/assets/blog/parade/poly.svg" style="border: none;;width: 100%;height: 240pt;"></iframe>
Finally, we present the optional step of generating polyhedral provably robust adversarial example $\mathcal{P}$ from the box provably robust adversarial example $\mathcal{U}$. 
The additional flexibility of the polyhedral shape allows for larger regions $\mathcal{P}$ compared to $\mathcal{U}$ in exchange for computational complexity. As generating polyhedral regions is hard, we again do this heuristically.
Starting with the overapproximation box $\mathcal{O}$, we iteratively add linear containts to it until we arrive at a polyhedron $\mathcal{P}$ that can be proved to only contain adversarial examples by the black-box verifier. 
Similarly to the generation process of $\mathcal{U}$, we use the verification at iteration $i$ to generate linear contraints. 
Unlike the generation process of $\mathcal{U}$, we use not only linear constraints from the final verification objective but also linear constraints that make the *ReLU* activation neurons in the network decided. 
Unfortunately, the resulting constraints might generate polyhedron $\mathcal{P}$ that is smaller than $\mathcal{O}$. To prevenet that, we leverage the fact that $\mathcal{U}$ is itself provably robust and we bias-adjust the constraints in such a way that they do not remove volume from $\mathcal{U}$.
The procedure is concludes when the verifier succeeds. We outline the procedure in the animation above.

### Experiments

### Visualizing PARADE regions
![](/assets/blog/parade/visualize.svg){: .blogpost-img100}

Above we visualize some of the provably robust adversarial examples generated by **PARADE** for both pixel and geometric transformations. Each pixel's color represents the number of possible values that pixel can have within our box regions. 
### Summary

We hope we piqued your interest in our work. For further details and experiments, please refer to our full paper, [*linked above*](https://files.sri.inf.ethz.ch/website/papers/symex.pdf).
### Acknowledgments

I would like to thank all of my collaborators for contributing to this paper. In particular, I want to thank [*Gagandeep Singh*](https://ggndpsngh.github.io/), who supervised me on the project and is now professor at UIUC, for his help and mentorship.
