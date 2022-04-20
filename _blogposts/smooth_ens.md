---
layout: blogpost
category: paper
pub-ref: horvath2022boosting
title: "Boosting Randomized Smoothing with Variance Reduced Classifiers"
blogpost-authors: "Mark Niklas Müller, Marc Fischer" 
date: 2022-04-15
thumbnail: _thumbnails/smooth_ens.png
usemathjax: true
tldr: >
    In this blog post, we theoretically motivate why ensembles are particularly suitable base models for constructing certifiably robust classifiers via Randomized Smoothing (RS) and confirm this choice empirically, obtaining state-of-the-art results in multiple settings. The key insight is that the reduced variance of ensembles over the perturbations introduced in RS leads to signiﬁcantly more consistent classiﬁcations for a given input. This, in turn, leads to substantially increased certiﬁable radii for samples close to the decision boundary. Additionally, we introduce key optimizations which enable an up to 55-fold decrease in sample complexity of RS.
excerpt: >
    We theoretically motivate why and show empirically that, ensembles are particularly suitable base models for Randomized Smoothing, due to the variance reduction across the perturbations introduced during Randomized Smoothing.
keywords: randomized smoothing, certified robustness, ensembles
conf-url: https://iclr.cc/virtual/2022/spotlight/6328
conf-info: Spotlight - Thu Apr 28, 7:30pm CEST

draft: false
tweet-id:
---

While deep neural networks often achieve excellent accuracy on the distribution they were trained on, they have been shown to be very sensitive to slightly perturbed inputs, called adversarial examples. This severely limits their applicability to safety-critical domains.
Heuristic defenses against this vulnerability have been shown to be breakable, highlighting the need for provable robustness guarantees. 

A promising method providing such guarantees for large networks is Randomized Smoothing (RS). The core idea is to provide probabilistic robustness guarantees with arbitrarily high confidence by adding noise to the input of a base classifier and computing the majority vote of the classification over the perturbed inputs using Monte Carlo sampling.

In this blog post we consider *applying RS to ensembles* as base classifiers and explain why they are a particularly suitable choice. For this, we will first give a short recap on Randomized Smoothing, before explaining our approach and discussing our theoretical results. Finally we show that our approach yields a new state-of-the-art in most settings, often even while using less compute than current methods.

[comment]: <> (This is how to write comments.)

### Background: Randomized Smoothing (RS)

We consider a (soft) base classifier $f \colon \mathbb{R}^d \mapsto \mathbb{R}^{n}$ predicting a numerical score for each class and let $$F(x) := \text{arg max}_{i} \, f_{i}(x)$$ denote the corresponding hard classifier $\mathbb{R}^d \mapsto [1, \dots, n]$.

We now define the smoothed classifier $G \colon \mathbb{R}^d \mapsto [1, \dots, n]$ using  a random variable $\epsilon \sim \mathbb{N}(0, \sigma_{\epsilon}^2 I)$ as

$$G(x) := \text{arg max}_c \, \mathcal{P}_{\epsilon \sim \mathbb{N}(0, \sigma_{\epsilon}^2 I)}(F(x + \epsilon) = c).$$

Let now $c_A$ be the majority class, $\underline{p_A}$ a lower bound to its success probability, $c_B$ the runnerup (second most likely) class with an upper bound to its success probability $\overline{p_B}$:

$$ \mathcal{P}_{\epsilon}(F(x + \epsilon) = c_A) \geq \underline{p_A} \geq \overline{p_B} \geq \max_{c \neq c_A}\mathcal{P}_{\epsilon}(F(x + \epsilon) =c). $$

Now, the smoothed classifier is guarantted to be robust $G(x + \delta) = c_A$ for all perturbations $\delta$ satisfying $\|\delta\|_2 < R$ with $R := \tfrac{\sigma_{\epsilon}}{2}(\Phi^{-1}(\underline{p_A}) - \Phi^{-1}(\overline{p_B}))$.

> TLDR: Randomized Smoothing (RS) takes a base model, evaluates it on perturbed inputs and predicts the majority classification over those predictions. The bigger the difference between the probability of the most likely and second most likely class, the more robust the resulting classifier.


### Ensembles

Instead of a single model $f$, we now consider a soft ensemble of $k$ models $\{f^l\}_{l=1}^k$:

$$\bar{f}(x) = \frac{1}{k} \sum_{l=1}^{k} f^l(x)$$

We evaluated a range of ensembling methods from learning the individual model weights on a hold-out set, to heuristics defining them based on hold-out set performance, to equal weights. Since equal weights both performed consistently well and are easier to analyse we only consider them here.

We obtain different models $f^l$ by varying only the random seed and thus initialization of the training.

### Variance Reduction via Ensembles for Randomized Smoothing
Here, we explain our theoretical analysis of why ensembles are particularly suitable base models. Feel free to skip to the TLDR for a high level summary.


#### Single classifer
We model the predictions of an individual classifer $f^l$ on a single arbitrarry but fixed sample $x$ with Gaussian perturbations $\epsilon \sim \mathbb{N}(0, \sigma_{\epsilon}^2 I)$ as

$$y^l = y^l_p + y^l_c,$$

where $y^l_c$ is the classifier's prediction on the unperturbed sample and models the stochasticity in weight initialization and training with random noise augmentation and $y^l_p$ describes the effect of the random perturbations $\epsilon$ applied during RS. We model the clean component $y_c$ (distribution over classifiers) with mean $$c = \mathbb{E}_l[f^l(x)]$$ and covariance $\Sigma_c$. We assume the perturbation effect $y_p$ to be zero-mean and have covariance $\Sigma_{p}$. As $y_c$ models the global training effects and $y_p$ models the local behavior under small perturbations, we assume them to be independent.

#### Ensembles

Now, we construct an ensemble of $k$ such classifiers, using soft-voting to compute $\bar{y} = \frac{1}{k} \sum_{l=1}^k y^l.$ As we consider similar classifiers, differing only in the random seed used for training, we assume that the correlation between the logits of different classifiers has a similar structure but smaller magnitude than the correlation between logits of one classifier. Therefore, we parametrize the covariance between $y_c^i$ and $y_c^j$ for classifiers $i\neq j$ with $\zeta_c \Sigma_c$ and similarly between $y_p^i$ and $y_p^j$ with $\zeta_p \Sigma_p$ for $\zeta_c, \zeta_p \in [0,1]$. With the correlation coefficients $\zeta_c$ and $\zeta_p$, this construction captures the range from no correlation ($\zeta = 0$) to perfect correlation ($\zeta = 1$).

<!---The prediction of a model is determined by the difference between its logits. We call this difference the classification margin. We can now compute its statistics based on the assumptions made above as a function of the number of ensembled classifiers $k$:

\begin{align*}
	\mathbb{E}[\bar{z}_i] &= \mathbb{E}[z_i] = c_1 - c_i\\
	\text{Var}[\bar{z}_i] &= \underbrace{\frac{k + 2 \binom{k}{2}\zeta_p}{k^2} (\sigma^2_{p,1} + \sigma^2_{p,i} - 2 \rho_{p,1i} \sigma_{p,1} \sigma_{p,i})}_{\sigma^2_p(k)} + \underbrace{\frac{k + 2 \binom{k}{2}\zeta_c}{k^2} (\sigma^2_{c,1} + \sigma^2_{c,i} - 2 \rho_{c,1i} \sigma_{c,1} \sigma_{c,i})}_{\sigma^2_c(k)}.
\end{align*}
--->

#### Variance Reduction
Based on these assumptions, we can compute the variance of the ensembles predictions split into a component associated with the clean prediction $\sigma^2_c(k)$ and the perturbation effect $\sigma^2_p(k)$, both as functions of the ensemble size $k$. Dropping the indices, we find that both of these components scale with ensemble size as:

$$\frac{\sigma^2(k)}{\sigma^2(1)} = \frac{1 + \zeta_{} (k-1)}{k} \xrightarrow {k \to \infty} \zeta$$

Note thatboth variance component ratios go towards their corresponding correlation coefficients $\zeta_c$ and $\zeta_p$ as ensemble size grows. We can now use Chebychev's inequality and the union bound to determine a lower bound to the success probability of the majority class $1$ as:

$$p_{1} \geq 1 - \sum_{i=2}^m \mathcal{P} \big(|\bar{z}_{i} - c_1 + c_i| \geq t_i \, \sigma_i(k)\big) \geq 1  -  \sum_{i=2}^m \frac{\sigma_i(k)^2}{(c_1 - c_i)^{\,2}}% = 1$$

Instead assuming Gaussian distributions and estimating all parameters from real ResNet20, we obtain the following:

**Classification Margin**
The prediction of a model is determined by the difference between its logits. We call this difference the classification margin. Below we show the distribution over the logit differnce between the class with the highest and second highest score. Where the area under the curves to the left of the black line corresponds to the probability of predicting the runner-up class $p_B$ and the area to the right of the black line to the probability of predicting the majority class $p_A$.

![Illustration of classification margin variance reduction with increased number of ensembled classifiers](/assets/blog/smooth_ens/runner_up_margin.png){: .blogpost-img50}

We observe that reducing the variance over perturbations significantly increases the success probability of the majority class without changing the mean, corresponding to the prediction of the unperturbed sample.

**Success Probability**
Translating the classification margin distribution to success probabilities, we obtain the blue curve below, compared to an actually measured curve in orange:

![Illustration of increase in success probability with number of ensembled classifiers](/assets/blog/smooth_ens/succes_prob.png){: .blogpost-img50}
 We observe that the success probability increases notably with the number of ensembled classifiers.
 
**Certified Radius**
Using the success probabilities, we can compute a probability distribution over the certified $\ell_2$-radius:
![Illustration of increase in certifiable radius number of ensembled classifiers](/assets/blog/smooth_ens/cert_rad_distr.png){: .blogpost-img50}

We observe that ensembling increases the certified radius to a much larger degree, than simply increasing the number of samples evaluated for randomized smoothing.

> TLDR: Ensembling $k$ classifiers differing only in the random seed used for training yields a classifier with significantly reduced variance over random perturbations. Without (necessarily) changing the natural accuracy, this increases the certified radius and thereby certified accuracy significantly, even when correcting for the increased compute.

### Experimental Evaluation

We conduct experiments on ImageNet and CIFAR-10 using a wide range of training methods, network architectures, and noise magnitudes and consistently observe that ensembles outperform their best constituting models.

**CIFAR-10**
![Illustration of increase in ACR with number of ensembled classifiers](/assets/blog/smooth_ens/acr_cifar_050_3.png){: .blogpost-img50}

While using an ensemble of ResNet110's clearly outperforms an individual one, most of this improvement is already obtained when ensembling only five models. Even an ensemble of just three ResNet20's outperform a single ResNet110, despite requiring significantly less computate for training and inference.

![Comparison of certified radius of using more samples instead of ensembling.](/assets/blog/smoothens/sample_experiment_cifar.png){: .blogpost-img50}
Using more samples with just a single network barely improves the certified radius at all, unless mathematically necessary to achieve a sufficiently high confidence level.


**ImageNet**
![Illustration of increase in ACR with number of ensembled classifiers](/assets/blog/smooth_ens/acr_in_100.png){: .blogpost-img50}

On ImageNet, an ensemble of just three ResNet50's is enough to improve over the current state-of-the-art by more than 10%.

> TLDR: Ensembles outperform their best constituting model consistently across a wide range of settings, obtaining a new state-of-the-art.

### Summary

We propose a theoretically motivated and statistically sound approach to construct low variance base classifiers for Randomized Smoothing by ensembling. We show theoretically and empirically why this approach significantly increases certified accuracy yielding state-of-the-art results.
If you are interested in more details please check out our [ICLR 2022 paper](https://www.sri.inf.ethz.ch/publications/horvath2022boosting).

There, we also introduce an adaptive sampling mechanism, allowing us to reduce certification costs up to 55-fold for predetermined radii

