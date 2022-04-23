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
conf-info: Poster - Tue Apr 26, 17:30 GMT (Poster Session 5)

draft: false
tweet-id:
---

This is some intro paragraph text motivating the whole thing. Always make sure that all the metadata is set correctly and `draft: true` while the post is not ready to be released. This was also an example of inline code.

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





<iframe src="/assets/blog/parade/over.svg" style="border: none;;width: 100%;height: 200pt;"></iframe>

{:.blogpost-caption}
***Conceptual overview of LCIFR.** This is a full-width gif. Start captions with a bold caption heading.*

Later in the results section we have a 50% image.

### Adding Some Math

Inline latex always works. For example, for classification tasks $\mu$ could denote equal classification (i.e., $\mu(M(x), M(x')) = 1 \iff M(x) = M(x')$) or classifying $M(x)$ and $M(x')$ to the same label group. For block latex you can use `equation*` and `align*` as follows.

[comment]: <> (There must be an empty row before and after a non-inline math block ($$) otherwise it doesn't work!) 
<iframe src="/assets/blog/parade/under.svg" style="border: none;;width: 100%;height: 264pt;"></iframe>
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


<iframe src="/assets/blog/parade/poly.svg" style="border: none;;width: 100%;height: 240pt;"></iframe>



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
