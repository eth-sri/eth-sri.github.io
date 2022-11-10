---
layout: blogpost
category: paper
pub-ref: dimitrov2022provably
title: "Generating provably robust adversarial examples"
blogpost-authors: "Dimitar I. Dimitrov" 
date: 2022-04-21
thumbnail: thumbnails/parade.svg
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
tweet-id: 1518638884913127424
---

<img src="/assets/blog/parade/motivation.svg" class="blogpost-img100" style="height: 200pt;">
On the image above we show an image of the digit $0$ from MNIST ($x\_\text{orig}$) and a region around it in red that depicts the set of geometrically perturbed images for which we expect a given neural network to be robust. 
Further, in green we depict a subregion where the neural network is not robust. Traditionally, in order to assess the robustness of the network one uses adversarial attacks to generate the examples $x_1$ and $x_2$. 
While robustness can be assessed that way, the information that the whole green region is adversarial is lost. This in turn might lead to never-seen-before network behaviour in the future. 
One advantage of the classical approach of assessing robustness, however,  is that generating $x_1$ and $x_2$ is fast. In contrast, generating the green region is computationally infeasible.
In this work, we present an algorithm called **PARADE** that exploits classical adversarial attacks to generate as large as possible regions that are provably adversarial. Similarly to the green region in the figure, these regions summarize many indvidual advarsarial attacks while also being practical to compute. 
We call them provably robust adversarial examples. 

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

We experimented with two different types of provably robust adversarial examples - robust to pixel intensity changes ($\ell\_\infty$ changes) and to geometric changes. We show the pixel intensity experiment below:

| Network   | $\epsilon$ | PARADE<br/>Box<br/>\# Regions | PARADE<br/>Box<br/>Time | PARADE<br/>Box<br/>\# Attacks | PARADE<br/>Poly<br/>\# Regions | PARADE<br/>Poly<br/> Time | PARADE<br/>Poly<br/>\# Attacks |
|-------------|-------:|----------:|------:|----------:|----------:|------:|---------------:|
| MNIST<br/>8x200 | 0.045 | 53/53 | 114s | $10^{121}$ | 53/53 | 1556s | $10^{121} < \cdot < 10^{191}$ |
| MNIST<br/>ConvSmall | 0.12 | 32/32 | 74s | $10^{494}$ | 32/32 | 141s | $10^{494} < \cdot < 10^{561}$ |
| MNIST<br/>ConvBig | 0.05 | 28/29 | 880s | $10^{137}$ | 28/29 | 5636s | $10^{137} < \cdot < 10^{173}$ |
| CIFAR-10<br/>ConvSmall | 0.006 | 44/44 | 113s | $10^{486}$ | 44/44 | 264s | $10^{486} < \cdot < 10^{543}$ |
| CIFAR-10<br/>ConvBig  | 0.008 | 36/36 | 404s | $10^{573}$ | 36/36 | 610s | $10^{573} < \cdot < 10^{654}$ |

We note **PARADE** is highly effective - it generates regions successfully for all but $1$ image for which the classical adversarial attacks succeeded. Further, the regions generated contain a very large set of adversarial examples that are infeasible to generate individually.
Finally, we note that the polyhedral adversarial examples take more time to generate but contain more examples. Calculating the exact number of concrete attacks within the polyhedral regions is computationally hard so instead we approximate the number as precisely as possible from above and below using boxes.
 
Next, we show the results for adversarial examples provably robust to geometric changes: 

| Network   | Transform | PARADE<br/>Box<br/>\# Regions | PARADE<br/>Box<br/>Time | PARADE<br/>Box<br/>\# Attacks |
|-------------|-------:|----------:|------:|----------:|
| MNIST<br/>ConvSmall | Rotate + Scale + Shear | 51/54 | 774s | $10^{96} < \cdot < 10^{195}$ |
| MNIST<br/>ConvSmall | Scale + Translate2D | 51/56 | 521s | $10^{71} < \cdot < 10^{160}$ |
| MNIST<br/>ConvSmall | Scale + Rotate + Brightness | 40/48 | 370s | $10^{70} < \cdot < 10^{455}$ |
| MNIST<br/>ConvBig | Rotate + Scale + Shear | 44/50 | 835s | $10^{77} < \cdot < 10^{205}$ |
| MNIST<br/>ConvBig  | Scale + Translate2D | 42/46 | 441s | $10^{64} < \cdot < 10^{174}$ |
| MNIST<br/>ConvBig | Scale + Rotate + Brightness | 46/52 | 537s | $10^{119} < \cdot < 10^{545}$ |
| CIFAR-10<br/>ConvSmall  | Rotate + Scale + Shear | 29/29 | 1369s | $10^{599} < \cdot < 10^{1173}$ |
| CIFAR-10<br/>ConvSmall  | Scale + Translate2D | 32/32 | 954s | $10^{66} < \cdot < 10^{174}$ |
| CIFAR-10<br/>ConvSmall  | Scale + Rotate + Brightness | 21/25 | 1481s | $10^{513} < \cdot < 10^{2187}$ |

We see that again **PARADE** is capable of generating examples for most images where classical adversarial attacks succeeded. We note that we use [*DeepG*](https://www.sri.inf.ethz.ch/publications/balunovic2019geometric) for verification. 
Since DeepG generates image polyhedra, we have to approximate the number of concrete attacks similarly to **PARADE Poly** above. We also note that DeepG is more computationally expensive resulting is longer runtime for our algorithm, as well. 

### Visualizing PARADE regions
![](/assets/blog/parade/visualize.svg){: .blogpost-img100}

Above we visualize some of the provably robust adversarial examples generated by **PARADE** for both pixel and geometric transformations. Each pixel's color represents the number of possible values that pixel can have within our box regions. 
### Summary
We introduced and motivated the concept of provably robust adversarial examples. We further showed an outline of our algorithm, **PARADE**, that generates such examples in the shape of boxes or polyhedra. 
Emperically we demonstrated that regions produced by **PARADE** can summarize very large number of individual adversarial examples making them an useful tool to asses the robustness of neural networks. 
We hope that we piqued your interest in our work. For further details and experiments, please refer to our [*ICLR 2022 paper*](https://files.sri.inf.ethz.ch/website/papers/symex.pdf).
### Acknowledgments

I would like to thank all of my collaborators for contributing to this paper. In particular, I want to thank [*Gagandeep Singh*](https://ggndpsngh.github.io/), who supervised me on the project and is now professor at UIUC, for his help and mentorship.
