---
layout: blogpost
category: paper
pub-ref: ruoss2020lcifr
title: "How to enforce individual fairness?"
blogpost-authors: "Mislav Balunović" 
date: 2022-02-01
thumbnail: thumbnails/lcifr.svg
usemathjax: true
tldr: >
    LCIFR is a method for learning fair representations with provable certificates of individual fairness.
    Fair representations allow data owners to pre-process their data so that they can guarantee fairness of any downstream task using this data.
    The key idea is to use a form of adversarial training to search for counter-examples to the individual fairness condition, and then use
    these examples to improve the representations. Our results show that classifiers trained using LCIFR representations have high certified individual fairness, while also achieving high utility.
excerpt: >
    In this blog post we discuss our recent work LCIFR, a method for learning fair representations with provable certificates of individual fairness
    for any downstream task using this data.
keywords: fair representation learning, certified individual fairness
conf-url: https://icml.cc/virtual/2021/poster/9327
conf-info: Oral - Wed Jul 20, 19:00 GMT+2 (Reinforcement Learning 4) | Poster - Tue Jul 20, 18:00 GMT+2 (Poster Session 1)

tweet-id: 1447996320741007362
---

As machine learning is being increasingly used in sensitive domains such as crime risk assessment, hiring or credit scoring,
community has become more aware of the potential of these systems to reinforce bias and discriminate.
Data owners often face the challenge that their data can be used in downstream applications whose developers are potentially unaware of fairness issues or simply lack expertise to address these problems.
In this blog post, we present a method which enables data owners to pre-process their data so that any downstream application has guarantee of individual fairness.
More specifically, data owners first specify which individuals are similar (e.g. two persons with similar qualifications, but different race), and should thus receive similar outcome in any downstream task.
Then, we use fair representation learning to pre-process data into a new latent representation which has a property that similar individuals are close in the latent space.
Finally, we can then provide a certificate that any classifier using these latent representations is individually fair.


### Individual vs group fairness

Two main families of fairness definitions are *individual fairness* and *group fairness*.
Individual fairness requires that similar individuals receive similar outcomes, while group fairness states that average outcome for all groups
should be equal.
One issue with group fairness is that it does not provide any guarantee to individuals or even different subgroups in the population, as it only averages outcomes across the entire groups.
The main reason why group fairness is more popular is that it requires only group assignment based on sensitive attributes while individual fairness requires more complex definition of similarity metric.
Here, we define similarity through logical constraints that allow capturing wide range of interpretable similarity notions.


### Fair representations

Consider a case of a company with several teams that would like to build ML models for different products using the same data.
One option would be for each team to train their own model and enforce fairness of the model by themselves.
However, the teams might not have the same definition of fairness or they might even lack expertise to train fair models.
[*Fair representation learning*](https://sanmi.cs.illinois.edu/documents/Representation_Learning_Fairness_NeurIPS19_Tutorial.pdf) is a data pre-processing technique that transforms data into a new representation such that any classifier trained on top of this representation is fair.
Using representation learning enables us to pre-process data only once, and then give processed data to each team so that they can train their own model on this new data, while knowing that the model is fair, according to a single pre-defined fairness definition. 


### Learning Certified Individually Fair Representations

Our approach, named LCIFR (standing for Learning Certified Individually Fair Representations), focuses on *individual fairness* where two individuals $x$ and $x'$ are similar if and only if some binary similarity function $\phi(x, x')$ evaluates to 1.
The function $\phi$ is application-specific and could be determined based on the background knowledge about the data or the existing fairness regulations.
To define similarity of two individuals, we allow both categorical (e.g. individuals that have the same occupation) or numerical (e.g. individuals that differ by at most 10 in age) conditions, as well as their combinations using conjunctions and disjunctions.


![](/assets/blog/lcifr/lcifr_overview.gif){: .blogpost-img100}

{:.blogpost-caption}
***Conceptual overview of LCIFR.** The left side shows data producer who learns an encoder $f_\theta$ which maps the entire set of individuals that are similar to individual $x$ to points near $z = f_\theta(x)$ in the latent space. The data producer then computes a bounding box around the latent set of similar individuals with center $z = f_\theta(x)$ and radius $\epsilon$ and passes it to the data consumer.*

<!-- We show overview of our approach in Figure 1. -->
<!-- Given some fairness constraint, we want to train an individually fair representation and use it to -->
<!-- obtain a certificate of individual fairness for the end-to-end model (involving both the representation and the classifier). -->

A high-level overview of our approach is shown in the above figure.
One party, called data producer, wants to learn an encoder $f_\theta$ which transforms the original data $x$ into a new representation $z = f_\theta(x)$ such that any classifier $h_\psi$, provided by another party called data consumer, which is using this new representation $z$ as an input is fair.
The core idea of our approach is to train a network $f_\theta$ that maps similar individuals $x$ and $x'$ close together in the latent space.
Formally, given some threshold $\delta$, we want to train $f_\theta$ such that:


$$
\begin{equation*}
	\phi(x, x') \implies ||f_\theta(x) - f_\theta(x')||_{\infty} \leq \delta
\end{equation*}
$$

Of course, requiring only the above allows for trivial solution - just map all inputs to a single point.
However, such a representation would provide no utility for any downstream task as e.g. predicting an input-specific label from such representation is not possible with accuracy better than random.
Thus, we can notice that fairness and utility are sometimes competing objectives, and we have to balance between them during training.
To ensure having useful representations, we additionally train an auxiliary classifier $h_\psi$ on top of the learned representations.
To train the encoder, we use [DL2](https://www.sri.inf.ethz.ch/publications/fischer2019dl2) to repeatedly search for counter-examples to the above condition as DL2 allows us to translate logical expression to a differentiable loss.
We then use a form of adversarial training: after counterexamples are found, we combine DL2 loss and classification loss, and then use gradient descent to modify the encoder parameters to make it more likely to satisfy the individual fairness condition while keeping classification utility high.


As training with DL2 results in a network that is only empirically fair, the next task is to actually prove fairness.
To certify individual fairness of the end-to-end model (encapsulating both encoder $f_\theta$ and classifier $h_\psi$) for some input $x$, data producer searches for the smallest $\epsilon$ such that $$\phi(x, x') \implies ||f_\theta(x) - f_\theta(x')||_{\infty} \leq \epsilon$$, and then passes both representation $z = f_\theta(x)$ and radius $\epsilon$ to the data consumer.
Then, data consumer certifies that classifier $h_\psi$ is robust to $\ell_\infty$ perturbations of size up to $\epsilon$.
Both of these steps can be preformed efficiently using [mixed-integer linear programming](https://arxiv.org/abs/1711.07356), as networks typically used in fairness tasks are relatively small.

### Experiments

We evaluated LCIFR on several datasets commonly used in the fairness literature: Adult, Compas, German, Health and Law School.
We always report accuracy of the auxiliary classifier trained on top of the learned representations as a task utility, together with percentage of certified individuals.

![](/assets/blog/lcifr/lcifr_results.svg){: .blogpost-img50}

{: .blogpost-caption}
***Experimental results.** Experimental evaluation of LCIFR on several common fairness datasets using Noise constraint (more details in the paper). For each dataset, LCIFR can train a classifier with high utility and high certified individual fairness.*

In the above figure we show our results obtained on Noise constraint which considers two individuals similar if all of their normalized numerical features differ by at most 0.3 (e.g. in Adult dataset this would correspond to difference in age of 3.95).
our results indicate that LCIFR is highly effective in providing certificates of individual fairness without significantly sacrificing classification accuracy.

### Summary

In this blog post we described LCIFR, a method for learning certified individually fair representations.
The first ingredient of our method was to define individual fairness using similarity based on logical constraints.
We can then use DL2 to train the encoder to map similar individuals close together in the latent space, while ensuring that latent representations are informative for the downstream classification task.
Experimentally, we showed that LCIFR can provide certificates of individual fairness on several datasets while keeping classification accuracy high.
If you are interested in more details please check out our [NeurIPS 2020 paper](https://arxiv.org/abs/2002.10312).

### Acknowledgements

We would like to thank XX and YY
