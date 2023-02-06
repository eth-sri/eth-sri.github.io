---
layout: blogpost
category: paper
pub-ref: jovanovic2022paradox
title: "Why tighter convex relaxations harm certified training"
blogpost-authors: "Nikola Jovanović"
date: 2022-10-27
thumbnail: thumbnails/paradox.svg
usemathjax: true
tldr: >
    We investigate a well-known paradox of certified training, where most state-of-the-art methods use the loose interval-based relaxation, as using tighter convex relaxations in training often leads to worse results. We identify two previously overlooked properties of relaxations, continuity and sensitivity, which are generally unfavorable for tighter relaxations, harming the optimization procedure. We further explore possible next steps, and discuss the effect of our findings on the field.
excerpt: >
    We investigate a long-standing paradox in the field of certified training, identifying previously overlooked properties of convex relaxations which affect training success.
tweet-id: 
---

This blog post summarizes the key findings of our paper [On the Paradox Of Certified Training](https://www.sri.inf.ethz.ch/publications/jovanovic2022paradox), which was recently published in TMLR. 

We attempt to explain the phenomenon where most state-of-the-art methods for certified training based on convex relaxations (such as [FastIBP](https://proceedings.neurips.cc/paper/2021/hash/988f9153ac4fd966ea302dd9ab9bae15-Abstract.html) or the latest breakthrough [SABR](https://openreview.net/forum?id=7oFuxtJtUMH)) focus on the loose interval propagation (IBP/Box), while intuitively, tighter relaxations (i.e., the ones that more tightly overapproximate the non-linearities in the network) should lead to better results. 
This was [already](https://arxiv.org/abs/1810.12715) [observed](https://www.ijcai.org/proceedings/2019/854) [in](https://openreview.net/forum?id=Skxuk1rFwB) [many](https://www.sri.inf.ethz.ch/publications/balunovic2020bridging) [prior](https://arxiv.org/abs/2104.00447) [works](https://openreview.net/forum?id=52weXyh2yh), which proposed several hypotheses. However, the paradox was never investigated in a principled way.

We start by proposing a way to quantify tightness (see the paper for details), and thoroughly reproducing the paradox: Across a wide range of settings, tighter relaxations consistently lead to lower certified robustness (in %) than the loose IBP relaxation. An example is shown in the following table, grouping equivalent methods from prior work (below we will refer to each group using the name in bold):

<style>
    .good {
        background-color: #aaffaa;
        padding: 1px;
        width: 40px;
        display: inline-block;
    }
    .bad {
        background-color: #ffaaaa;
        padding: 1px;
        width: 40px;
        display: inline-block;
    }
</style>

| Relaxation | Tightness | Certified (%) 
|-------------|:-------:|:----------: 
| **IBP** / Box | <span class="bad"> 0.73 </span> | <span class="good"> 86.8 </span>
|-------------|:-------:|:----------: 
| **hBox** / Symbolic Intervals | <span class="good"> 1.76 </span> | <span class="bad"> 83.7 </span>
| **CROWN** / DeepPoly | <span class="good"> 3.36 </span> | <span class="bad"> 70.2 </span>
| **DeepZ** / CAP / FastLin / Neurify | <span class="good"> 3.00 </span> | <span class="bad"> 69.8 </span>
| **CROWN-IBP (R)** | <span class="good"> 2.15 </span> | <span class="bad"> 75.4 </span>
|-------------|:-------:|:----------: 

Our key observation is that there are other latent properties of relaxations, besides tightness, that affect success when relaxations are used in a training procedure.
More concretely, each of the tighter relaxations has either unfavorable _continuity_ (i.e., the corresponding loss function is discontinuous with respect to network weights) or unfavorable _sensitivity_ (i.e., the corresponding loss function is highly sensitive to small perturbations of network weights), both preventing successful optimization. By observing all three properties jointly, we can more easily interpret the seemingly counterintuitive results.

The plot below shows the relaxation of the ReLU non-linearity used by CROWN, for the example input range defined by $l=-5$ and $u=8$. By reducing $u$ (using the bottom slider), we can directly observe the discontinuity of CROWN, when its heuristic choice of the lower linear bound changes at $|l|=|u|$. Using the same plot we can observe the discontinuities of hBox at $l=0$. 
These observations imply discontinuities in the loss when a relaxation is used in training, which we further empirically observe in real scenarios.
Finally, we can use the plot below to observe that no discontinuities can be found for IBP and DeepZ---a formal proof of their continuity in the general case is given in the paper.


<a class="iframe-link" href="/assets/blog/paradox/continuity.html"> Open Interactive Plot</a>

<iframe class="iframe-full" src="/assets/blog/paradox/continuity.html" height="780px"></iframe>

While the sensitivity of the loss functions is harder to illustrate on a toy example as above, our derivation (Section 4.3 of the paper) demonstrates that the bounds used by CROWN, CROWN-IBP (R) and DeepZ lead to certified training losses highly sensitive to small changes in network weights, while the losses of IBP and hBox are not sensitive and induce more favorable loss landscapes. With these observations, we expand the table shown earlier to include all three relaxation properties: tightness, continuity and sensitivity. 
This illustrates that attempts to use tighter relaxations in certified training have introduced unfavorable properties of the loss, which resulted in the failure to outperform the continuous and non-sensitive IBP.

| Relaxation | Tightness | Continuity | Sensitivity | Certified (%) 
|-------------|:-------:|:-------:|:-------:|:----------: 
| **IBP** / Box | <span class="bad"> 0.73 </span> | <span class="good"> $\checkmark$ </span> | <span class="good"> $\checkmark$ </span> | <span class="good"> 86.8 </span>
|-------------|:-------:|:-------:|:-------:|:----------: 
| **hBox** / Symbolic Intervals | <span class="good"> 1.76 </span> | <span class="bad"> $\times$ </span> | <span class="good"> $\checkmark$ </span> |<span class="bad"> 83.7 </span>
| **CROWN** / DeepPoly | <span class="good"> 3.36 </span> | <span class="bad"> $\times$ </span> | <span class="bad"> $\times$ </span> |<span class="bad"> 70.2 </span>
| **DeepZ** / CAP / FastLin / Neurify | <span class="good"> 3.00 </span> | <span class="good"> $\checkmark$ </span> | <span class="bad"> $\times$ </span> |<span class="bad"> 69.8 </span>
| **CROWN-IBP (R)** | <span class="good"> 2.15 </span> | <span class="bad"> $\times$ </span> | <span class="bad"> $\times$</span> |<span class="bad"> 75.4 </span>
|-------------|:-------:|:-------:|:-------:|:----------: 

### Next steps

A natural question that arises is the one of improving unfavorable properties of relaxations to make them more suitable for certified training. 
In the paper we systematically investigate modifications of existing relaxations and find that designing a relaxation with all favorable properties is difficult, as the properties induce complex tradeoffs that depend on the setting. 
Still, such relaxations may exist, and future work might be able to utilize our findings to discover them.

A more promising approach seems to be the use of existing convex relaxations with modified training procedures designed to best utilize the benefits of each relaxation. Recent successful examples of this approach include [COLT](https://www.sri.inf.ethz.ch/publications/balunovic2020bridging), which includes the counterexample search in training, [CROWN-IBP](https://openreview.net/forum?id=Skxuk1rFwB), which heuristically combines the losses of two relaxations in training, and two recent methods which focus on IBP, aiming to improve its training procedure via better initialization and regularization ([FastIBP](https://proceedings.neurips.cc/paper/2021/hash/988f9153ac4fd966ea302dd9ab9bae15-Abstract.html)) or the propagation of 
smaller input regions in training ([SABR](https://openreview.net/forum?id=7oFuxtJtUMH)).

Finally, it is worth noting that there are other promising approaches for neural network certification that do not use convex relaxations and are thus not affected by tradeoffs between relaxation properties. Examples in this direction include [Randomized Smoothing](https://arxiv.org/abs/1902.02918), offering high-probability robustness certificates, and custom certification-friendly model architectures such as [$l_\infty$-distance nets](https://arxiv.org/abs/2102.05363). 
While not affected by limitations of convex relaxations, these approaches introduce other challenges such as optimization difficulties and additional inference-time work.