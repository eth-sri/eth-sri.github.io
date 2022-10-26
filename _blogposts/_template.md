---
layout: blogpost
category: paper
pub-ref: ruoss2020lcifr
title: "How to enforce individual fairness?"
blogpost-authors: "Mislav Balunović, Anian Ruoss" 
date: 2022-02-01
thumbnail: thumbnails/lcifr.svg
usemathjax: true
tldr: >
    The TLDR is for the blogpost page, aim for 4-5 sentences. In this blog post we discuss LCIFR, a method for learning fair representations with provable certificates of individual fairness. Fair representations allow data owners to pre-process their data so that they can guarantee fairness of any downstream task using this data. The key idea is to use a form of adversarial training to search for counter-examples to the individual fairness condition, and then use these examples to improve the representations. Our results show that classifiers trained using LCIFR representations have high certified individual fairness, while also achieving high utility.
excerpt: >
    The excerpt is for the home page, aim for 1-2 sentences or 3-5 lines on the homepage. LCIFR is a method for training fair representations with provable certificates of individual fairness.
keywords: fair representation learning, certified individual fairness
conf-url: https://icml.cc/virtual/2021/poster/9327
conf-info: Oral - Wed Jul 20, 19:00 GMT+2 (Reinforcement Learning 4) | Poster - Tue Jul 20, 18:00 GMT+2 (Poster Session 1)

tweet-id:
---

This is some intro paragraph text motivating the whole thing. Always make sure that all the metadata is set correctly and that your blogpost is not on the master branch until it is ready. This was also an example of inline code.

[comment]: <> (This is how to write comments.)

### Always use h3 ("###") for paragraph headings

Of course, all standard markdown formatting like *italic* and **bold** works here. This is an example of a block of code:

    draft: true	  
    draft: true	  
    draft: true

You can also have syntax highlighting:

{% highlight python %}
def fib(n):
  if n == 1 or n == 2:
  	 return 1
  return fib(n-1) + fib(n-2)
{% endhighlight %} 

You can embed both static images and gifs. For a full-width image use `.blogpost-img100`, for a centered 50% width image `.blogpost-img50`. Similarly, always use `.blogpost-caption` to properly format captions:

![Alt Text](/assets/blog/lcifr/lcifr_overview.gif){: .blogpost-img100}

{:.blogpost-caption}
***Conceptual overview of LCIFR.** This is a full-width gif. Start captions with a bold caption heading.*

Later in the results section we have a 50% image.

You can also wrap images; sometimes that looks much nicer, e.g., if there are many pictures in a row with not much text. Here is an example from MN-BaB.

{: .blogpost-wrap}
<span>**Effectiveness of Multi-Neuron Constraints**: We plot the ratio of the number of subproblems required to prove a property during Branch-and-Bound without vs. with MNCs. Using MNCs reduces the number of subproblems by two orders of magnitude on average.</span>
![Alt Text](/assets/blog/mn-bab/ResNet6-A_n_subproblems_ratio_w_wo_MNC.png){: .blogpost-img40}

### Adding Some Math

Inline latex always works. For example, for classification tasks $\mu$ could denote equal classification (i.e., $\mu(M(x), M(x')) = 1 \iff M(x) = M(x')$) or classifying $M(x)$ and $M(x')$ to the same label group. For block latex you can use `equation*` and `align*` as follows.

[comment]: <> (There must be an empty row before and after a non-inline math block ($$) otherwise it doesn't work!) 

$$
\begin{equation*}
    \quad \mathbb{E}_{x \sim D} \left[
        \forall x' \in \mathbb{R}^n : \phi(x, x') \implies \mu(M(x), M(x'))
    \right]
\end{equation*}
$$

Here is multiple aligned rows:

$$
\begin{align*}
   \phi(x,y) &= \phi \left(\sum_{i=1}^n x_ie_i, \sum_{j=1}^n y_je_j \right) \\
  &= \sum_{i=1}^n \sum_{j=1}^n x_i y_j \phi(e_i, e_j) \\ 
  &= (x_1, \ldots, x_n) \left( \begin{array}{ccc}
      \phi(e_1, e_1) & \cdots & \phi(e_1, e_n) \\
      \vdots & \ddots & \vdots \\
      \phi(e_n, e_1) & \cdots & \phi(e_n, e_n)
    \end{array} \right)
  \left( \begin{array}{c}
      y_1 \\
      \vdots \\
      y_n
    \end{array} \right)
\end{align*}
$$

You can also choose to hide some non-crucial details (e.g., heavy math) in a details box like this:

{% capture details %}

$$
\begin{equation*}
  \phi(x,y) = \phi \left(\sum_{i=1}^n x_ie_i, \sum_{j=1}^n y_je_j \right)
  = \sum_{i=1}^n \sum_{j=1}^n x_i y_j \phi(e_i, e_j) = \\
   (x_1, \ldots, x_n) \left( \begin{array}{ccc}
      \phi(e_1, e_1) & \cdots & \phi(e_1, e_n) \\
      \vdots & \ddots & \vdots \\
      \phi(e_n, e_1) & \cdots & \phi(e_n, e_n)
    \end{array} \right)
  \left( \begin{array}{c}
      y_1 \\
      \vdots \\
      y_n
    \end{array} \right)
\end{equation*}
$$

{% endcapture %}
{% capture summary %}
Show me the scary proof
{% endcapture %} {% include details.html %}

That's mostly it.

### Experiments

For the results try to visualize stuff and not do tables, if you really must this is how a table would be done. Probably should be somehow centered.

| Constraint   |      Dataset      |  LCIFR |
|----------|:-------------:|------:|
| Noise |  Compas | 90.0 |
| Cat |    Adult   |   70.2 |
| Att | Health |    32.2 |

Here is the promised 50% image:

![Alt Text](/assets/blog/lcifr/lcifr_results.svg){: .blogpost-img50}

{: .blogpost-caption}
***Experimental results.** Experimental evaluation of LCIFR on several common fairness datasets using Noise constraint (more details in the paper). For each dataset, LCIFR can train a classifier with high utility and high certified individual fairness.*

### Summary

In this blog post we described LCIFR, a method for learning certified individually fair representations.
The first ingredient of our method was to define individual fairness using similarity based on logical constraints.
We can then use [DL2](https://www.sri.inf.ethz.ch/publications/fischer2019dl2) to train the encoder to map similar individuals close together in the latent space, while ensuring that latent representations are informative for the downstream classification task.
Experimentally, we showed that LCIFR can provide certificates of individual fairness on several datasets while keeping classification accuracy high.
If you are interested in more details please check out our [NeurIPS 2020 paper](https://arxiv.org/abs/2002.10312).

Note the format used to cite stuff, avoid (Fischer et al.) and similar.

### Acknowledgments

I would like to thank all my collaborators. This is optional.

Below is the twitter link (only shows up if you set `tweet-id`) and Atom feed.
