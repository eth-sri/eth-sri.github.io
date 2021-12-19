---
layout: blogpost
category: paper
pub-ref: ruoss2020lcifr
title: "How to enforce certified individual fairness?"
blogpost_authors: "Mislav Balunovic" 
date:   2020-09-01
thumbnail: thumb1.svg
usemathjax: true
tldr:|
Fair representation learning provides an effective way of enforcing fairness
constraints without compromising utility for downstream users.
A desirable family of such fairness constraints, each requiring similar
treatment for similar individuals, is known as individual fairness.
In this work, we introduce the first method that enables data consumers to
obtain certificates of individual fairness for existing and new data points.
The key idea is to map similar individuals to close latent representations and
leverage this latent proximity to certify individual fairness.
That is, our method enables the data producer to learn and certify a
representation where for a data point all similar individuals are at
$$\ell_\infty$$-distance at most $$\epsilon$$, thus allowing data consumers to
certify individual fairness by proving $$\epsilon$$-robustness of their
classifier.
Our experimental evaluation on five real-world datasets and several fairness
constraints demonstrates the expressivity and scalability of our approach.

---


[comment]: <> (This is the end of TLDR, now starts the main content.)

## Introduction

![](/assets/blog/lcifr_overview.png)
***Figure 1.** Conceptual overview of our framework.The left side shows the component corresponding to the data producer who learns an encoder $$f_\theta$$ which maps the entire set of individuals $$S_\phi(x)$$ that are similar to individual $$x$$, according to the similarity notion $$\phi$$, to points near $$f_\theta(x)$$ in the latent space. The data producer then computes an $$\ell_\infty$$-bounding box $$\mathbb{B}_\infty$$ around the latent set of similar individuals $$f_\theta(S_\phi(x))$$ with center $$z = f_\theta(x)$$ and radius $$\epsilon$$ and passes it to the data consumer.*


The increased use of machine learning in sensitive domains (e.g., crime risk
assessment~\cite{brennan2009compas}, ad targeting~\cite{datta2015automated},
and credit scoring~\cite{khandani2010consumer}) has raised concerns that
methods learning from data can reinforce human bias, discriminate, and
lack fairness~\cite{sweeney2013discrimination,bolukbasi2016man,barocas2016big}.

		This is some block
		This is some block
		This is some block
		This is some block

Moreover, data owners often face the challenge that their data will
be used in (unknown) downstream applications, potentially indifferent to
fairness concerns ([Cisse et al. 2019](https://sanmi.cs.illinois.edu/documents/Representation_Learning_Fairness_NeurIPS19_Tutorial.pdf)).
To address this challenge, the paradigm of learning fair representations has
emerged as a promising approach to obtain data representations that preserve
fairness while maintaining utility for a variety of downstream
tasks~\cite{zemel2013learning, madras2018learning}.
The recent work of~\citet{mcnamara2017provably} has formalized this setting by
partitioning the landscape into: a \emph{data regulator} who
defines fairness for the particular task at hand, a \emph{data producer} who
processes sensitive user data and transforms it into another representation,
and a \emph{data consumer} who performs predictions based on the new
representation.

## Trying the code

{% highlight python %}
def fib(n):
  if n == 1 or n == 2:
  	 return 1
  return fib(n-1) + fib(n-2)
{% endhighlight %}

## Overview 

This section provides a high-level overview of our approach, with the
overall flow shown in~\cref{fig:overview}.


This is some random sentence. Blah blah
{% capture details %}
$$
\begin{align*}
  & \phi(x,y) = \phi \left(\sum_{i=1}^n x_ie_i, \sum_{j=1}^n y_je_j \right)
  = \sum_{i=1}^n \sum_{j=1}^n x_i y_j \phi(e_i, e_j) = \\
  & (x_1, \ldots, x_n) \left( \begin{array}{ccc}
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
{% endcapture %}
{% capture summary %}Show me scary proof{% endcapture %}{% include details.html %}

As introduced earlier, our setting consists of three parties.
The first party is a data regulator who defines similarity measures for the
input and the output denoted as $$\phi$$ and $$\mu$$, respectively.
The properties $$\phi$$ and $$\mu$$ are problem-specific and can be expressed in a
rich logical fragment which we describe later in~\cref{sec:training}.
For example, for classification tasks $$\mu$$ could denote equal classification
(\ie $$\mu(M(x), M(x')) = 1 \iff M(x) = M(x')$$) or classifying $$M(x)$$ and
$$M(x')$$ to the same label group; for regressions tasks $\mu$ could evaluate
to 1 if $$\|M(x) - M(x')\| \leq 0.1$$ and 0 otherwise.
We focus on equal classification in the classification setting for the
remainder of this work.

The goal of treating similar individuals as similarly as possible can then be
formulated as finding a classifier $M$ which maximizes
$$
\begin{equation*}
    \quad \mathbb{E}_{x \sim D} \left[
        \forall x' \in \mathbb{R}^n : \phi(x, x') \implies \mu(M(x), M(x'))
    \right]
\end{equation*}
$$

Here is some another random equation

$$
\begin{align*}
  & \phi(x,y) = \phi \left(\sum_{i=1}^n x_ie_i, \sum_{j=1}^n y_je_j \right)
  = \sum_{i=1}^n \sum_{j=1}^n x_i y_j \phi(e_i, e_j) = \\
  & (x_1, \ldots, x_n) \left( \begin{array}{ccc}
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

## Testing whether GIF works

Here is some GIF:

![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)


## Evaluation

Here are the results

| Constraint   |      Dataset      |  LCIFR |
|----------|:-------------:|------:|
| Noise |  Compas | 90.0 |
| Cat |    Adult   |   70.2 |
| Att | Health |    32.2 |

## Conclusion

We introduced a novel end-to-end framework for learning representations with
provable certificates of individual fairness.
We demonstrated that our method is compatible with existing notions of fairness,
such as transfer learning.
Our evaluation across different datasets and fairness constraints demonstrates
the practical effectiveness of our method.

## Acknowledgments

I would like to thank all my collaborators.