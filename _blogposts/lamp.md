---
layout: blogpost
category: paper
pub-ref: balunovic2022lamp
title: "LAMP: Extracting text from gradients with language model priors"
blogpost-authors: "Dimitar I. Dimitrov" 
date: 2022-11-28
thumbnail: thumbnails/lamp.svg
usemathjax: true
draft: false
tldr: >
    Recent work has challenged notion that federated learning preserves data privacy by showing that various attacks can reconstruct original data from gradient updates. However, most of these works focus on the image domain. In this work, we focus on the text domain, instead, where federated learning is commonly applied. To this end, we outline some challenges posed by text data that are not present in the image domain and propose solutions to them. The obtained attack, LAMP, is substantially better quantitatively and qualitatively compared to state-of-the-art methods.
excerpt: >
    In this work we present an attack on federated learning's privacy specific to the text domain. We show that federated learning in the text domain can expose a lot of user data. 
keywords: gradient inversion, federated learning, natural language processing
tweet-id: 1597960168540704769
conf-url: https://neurips.cc/virtual/2022/poster/52794
conf-info: Poster - Wed Nov 30 11:00 CST (Poster Session 3)
---

### Data privacy and Federated learning
Machine learning algorithms have set the state-of-the-art on most tasks where large amount of training data is available. While the improvements brought by these algorithms are impressive, their applications to settings where private data is used remain limited due to the privacy concerns posed by the large centralized datasets required by the training procedures. Recently, the federated learning framework has emerged as a promising alternative to collecting and training with centralized datasets.
In federated learning, multiple data owners (clients) collaboratively optimize a loss function $l$ w.r.t. the parameters $\theta$ of a global model $h$ on their own dataset $\mathcal{D}_i$ **without** sharing the data in $\mathcal{D}_i$ with the other participants: 

$$
\begin{equation*}
  \min_{\theta} \frac{1}{n} \sum_{i=1}^n \mathbb{E}_{(x, y) \sim \mathcal{D}_i} \left[ l(h_\theta(x), y) \right].
\end{equation*}
$$

To this end, the optimization is carried out in communication rounds. In particular, given the global parameters $\theta_t$ at round $t$, multiple clients compute model updates $g$ on their own data and then share them with a central server that aggregates them and produces a new global parameters $\theta_{t+1}$. After several communication rounds the model parameters converge to an optimum.
<img src="/assets/blog/lamp/server.svg" class="blogpost-img100" style="height: 500pt;margin: -50pt 0pt -50pt 0pt;">
One common implementation of this generic framework is the FedSGD algorithm, where updates are given by the gradient of $l$ w.r.t. $\theta_t$ on a single batch $\\{(x^b_i, y^b_i)\\}\sim \mathcal{D}_i$ of client data of size $B$:

$$
\begin{equation*}
  g(\theta_t,\mathcal{D}_i) =  \frac{1}{B} \sum_{b=1}^B \nabla_\theta \left[ l(h_{\theta_t}(x^b_i), y^b_i) \right].
\end{equation*}
$$


Federated learning in theory allows for improved data privacy, as the client data does not leave the individual clients. Unfortunately, several recent works have shown that updates $g$ computed by common federated algorithms such as FedSGD can be used by a malicious server during the aggregation phase to approximately reconstruct the client's data. So far, prior work has focused on exposing this issue in the image domain where strong image priors help the reconstruction. In this work, we show that such approximate reconstruction is also possible in the text domain, where federated learning is very commonly applied. 

### Gradient leakage

In order to obtain approximate input reconstructions $\\{\tilde{x}^b_i\\}$ from the FedSGD update of some client $i$, with updates as described above, prior works typically solve the following optimization problem at some communication round $t$:

$$
\begin{equation}
  \min_{\\{\tilde{x}^b_i\\}} \sum_{i=1}^n \mathcal{L}_{rec}\left( \left(\frac{1}{B} \sum_{b=1}^B \nabla_\theta l(h_\theta(\tilde{x}^b_i), y^b_i)\right), g(\theta_t, \mathcal{D}_i) \right) + \alpha_{rec}\,R(\{\tilde{x}^b_i\}),
\end{equation}
$$

where $\mathcal{L}$<sub>rec</sub> is distance metric - e.g., $L_1$, $L_2$ or cosine, that measures the gradient reconstruction error, $R(\\{\tilde{x}^b_i\\})$ is some domain specific prior - e.g. Total Variation (TV) in the image domain, that assesses the quality of the reconstructed inputs, and $\alpha_{rec}$ is hyperparameter balancing between the two. Note that $\theta_t$ and $g(\theta_t, \mathcal{D}_i)$ are known by the malicious server as the former is computed by it and the latter is sent to it by client $i$ at the end of the round. Often the batch labels $\\{y^b_i\\}$ can be obtained by the server using specific label reconstruction attacks, that are beyond the scope of this blog post, or just guessed by running the reconstruction with all possible labels due to their discrete nature, so throughout the post we only focus on reconstructing $\\{\tilde{x}^b_i\\}$. In [our previous blog post](https://www.sri.inf.ethz.ch/blog/bayesian), we have shown that solving the optimization problem above is equivalent to finding the Bayesian optimal adversary in this setting. 

In the image domain, the optimization problem is typically solved using gradient descent on the batch of randomly initialized images $\\{x^b_i\\}$ using an image-specific prior $R$. In the next section, we first discuss why such a solution is not well suited to language data and we then discuss our method, **LAMP**, that combines a text-specific prior with a new way to solve the optimization problem above by alternating discrete and continuous optimization steps to obtain our state-of-the-art gradient leakage framework for text.

### LAMP: Gradient leakage for text

In this work, we focus our attention on transformer-based models $h_\theta$, as they are the state-of-the-art for modeling text across various language tasks. As these models operate on continuous vectors, typically they assume fixed-size vocabulary of size $V$ and embed each word into a different $\mathbb{R}^d$ vector. For a sequence of words of size $n$, we refer to the individual words in it with $t_1,\ldots,t_n$ and to their corresponding embeddings with $x_1,\ldots,x_n$.

In order to solve the gradient leakage optimization problem from the previous section, we choose to optimize directly over the embeddings $x_i$ as they, similarly to images, are represented by continuous values we can optimize over. However, uniquely to the text domain, only a finite subset of vectors in $\mathbb{R}^d$ are valid word embeddings. To this end, when we obtain our reconstructed embeddings $\tilde{x}_i$ for each of them we then select the most similar in cosine similarity token in the vocabulary to create a reconstruction of the sequence of words $\tilde{t}_1,\ldots,\tilde{t}_n$.

An additional issue that is specific to the text domain and, in particular, the transformer architecture is that the transformer outputs depend on word order only through positional embeddings. Therefore, the model gradient reconstruction loss $\mathcal{L}$<sub>rec</sub> is not as affected by wrongly reconstructed word order as it is by the wrongly reconstructed word embeddings themselves. In practice, this results into the continuous optimization process often getting stuck in local minima caused by an embedding of a token that reconstructs the correct word at the wrong position. These local minima are hard to escape from continuously.  To this end, we introduce a discrete optimization step that reorders the sentence periodically, allowing to escape the local minima. The discrete step works by first proposing several word order changes such as swapping the positions of two words or moving a sentence prefix to the end of the sentence. The different order changes are then assessed based on the combination of the gradient reconstruction $\mathcal{L}$<sub>rec</sub> and the perplexity of the sentence $\mathcal{L}$<sub>lm</sub> computed by auxiliary language model such as GPT-2 on the projected words $\tilde{t}_i$:

$$
\begin{equation}
  \mathcal{L}_{rec}(\{\tilde{x}_i\}) + \alpha_{lm}\,\mathcal{L}_{rec}(\{\tilde{t}_i\}),
\end{equation}
$$

where $\alpha_{lm}$ is a hyperparameter balancing the two parts. The resulting end-to-end alternating optimization is demonstrated in the image below:
<img src="/assets/blog/lamp/lamp.svg" class="blogpost-img100" style="height: 500pt;margin: -100pt 0pt -100pt 0pt;">
where green boxes show the discrete optimization steps and the blue boxes demonstrate the continuous gradient descent optimization steps of the gradient leakage objective presented in the previous section. 

Finally, similarly to the image domain, we introduce a new prior specific to text that improves our reconstruction. To this end, we made the empirical observation that during optimization often the embedding vectors $x_i$ grow in length even when their direction doesn't change a lot. To this end, we regularize the average vector length of the embeddings in a sequence $\tilde{x}_i$ to be close to the average embedding length in the vocabulary $l_e$:

$$
\begin{equation}
  R(\tilde{x}_i) = \left(\frac{1}{n}\sum_{i=1}^n \| \tilde{x}_i \|_2  - l_e\right)^2
\end{equation}
$$

This allows our embeddings to remain in the correct range of values, which in turn results in a more stable and accurate reconstruction of the embeddings $\tilde{x}_i$.
  
### Experimental evaluation

We evaluated LAMP on several standard sentiment classification datasets and architectures based on the BERT language models. As is typically the case with language models, we assume our models are pretrained to make word predictions on large text corpora and that federated learning is used only to fine-tune the models on the classification task at hand. We consider two versions of LAMP - one where $\mathcal{L}$<sub>rec</sub> is a weighted sum of L1 and L2 distances (denoted LAMP<sub>L1+L2</sub>), and another one where $\mathcal{L}$<sub>rec</sub> is the cosine similarity (denoted LAMP<sub>cos</sub>). We compare them to the state-of-the-art attacks - TAG based on the same L1+L2 distance, and DLG based on L2 distance alone. We evaluate the methods in terms of the Rouge-1 metric (R1) which measures the percentage of correctly reconstructed words and the Rouge-2 metric (R2) which measures the percentage of correctly reconstructed bigrams. We note one can interpret R2 as a proxy measurement of how well the order of the sentence has been reconstructed. We present a subset of the results shown in our paper on the CoLA dataset and batch size of 1 below:
<br><br>
<table>
  <thead>
    <tr>
      <th>&nbsp;</th>
      <th style="text-align: center;" colspan="2">&nbsp;&nbsp;&nbsp;&nbsp;<span style="border-bottom:1px solid black">&nbsp;&nbsp;$\text{TinyBERT}_6$&nbsp;&nbsp;</span>&nbsp;&nbsp;&nbsp;&nbsp;</th>
      <th style="text-align: center;" colspan="2">&nbsp;&nbsp;&nbsp;&nbsp;<span style="border-bottom:1px solid black">&nbsp;&nbsp;$\text{BERT}_{BASE}$&nbsp;&nbsp;</span>&nbsp;&nbsp;&nbsp;&nbsp;</th>
      <th style="text-align: center;" colspan="2">&nbsp;&nbsp;&nbsp;&nbsp;<span style="border-bottom:1px solid black">&nbsp;&nbsp;$\text{BERT}_{LARGE}$&nbsp;&nbsp;</span>&nbsp;&nbsp;&nbsp;&nbsp;</th>
    </tr>
    <tr>
      <th>Method</th>
      <th style="text-align: center">R1</th>
      <th style="text-align: center">R2</th>
      <th style="text-align: center">R1</th>
      <th style="text-align: center">R2</th>
      <th style="text-align: center">R1</th>
      <th style="text-align: center">R2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>DLG</td>
      <td style="text-align: center">37.7</td>
      <td style="text-align: center">3.0</td>
      <td style="text-align: center">59.3</td>
      <td style="text-align: center">7.7</td>
      <td style="text-align: center">82.7</td>
      <td style="text-align: center">10.5</td>
    </tr>
    <tr>
      <td>TAG</td>
      <td style="text-align: center">43.9</td>
      <td style="text-align: center">3.8</td>
      <td style="text-align: center">78.9</td>
      <td style="text-align: center">10.2</td>
      <td style="text-align: center">82.9</td>
      <td style="text-align: center">14.6</td>
    </tr>
    <tr>
      <td>$\text{LAMP}_{\cos}$</td>
      <td style="text-align: center">93.9</td>
      <td style="text-align: center"><strong>59.3</strong></td>
      <td style="text-align: center"><strong>89.6</strong></td>
      <td style="text-align: center"><strong>51.9</strong></td>
      <td style="text-align: center"><strong>92.0</strong></td>
      <td style="text-align: center"><strong>56.0</strong></td>
    </tr>
    <tr>
      <td>$\text{LAMP}_{\text{L1}+\text{L2}}$</td>
      <td style="text-align: center"><strong>94.5</strong></td>
      <td style="text-align: center">52.1</td>
      <td style="text-align: center">87.5</td>
      <td style="text-align: center">47.5</td>
      <td style="text-align: center">91.2</td>
      <td style="text-align: center">47.8</td>
    </tr>
  </tbody>
</table>
<br><br>
We see that LAMP<sub>cos</sub> is consistently recovering more words compared to the alternatives with LAMP<sub>L1+L2</sub> close behind. Further, LAMP recovers substantially better sentence ordering. It is worth noting that the improvement over the baselines for both R1 and R2 is most pronounced on the smallest model $\text{TinyBERT}_6$ where recovery is the hardest. Additionally, we also experimented with recovering text in the setting where the batch size is bigger than 1. We are the first to present results in this setting and we show them below for the CoLA dataset:
<br><br>
<table>
  <thead>
    <tr>
      <th>&nbsp;</th>
      <th style="text-align: center;" colspan="2">&nbsp;&nbsp;&nbsp;&nbsp;<span style="border-bottom:1px solid black">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B=1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>&nbsp;&nbsp;&nbsp;&nbsp;</th>
      <th style="text-align: center;" colspan="2">&nbsp;&nbsp;&nbsp;&nbsp;<span style="border-bottom:1px solid black">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B=2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>&nbsp;&nbsp;&nbsp;&nbsp;</th>
      <th style="text-align: center;" colspan="2">&nbsp;&nbsp;&nbsp;&nbsp;<span style="border-bottom:1px solid black">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;B=4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>&nbsp;&nbsp;&nbsp;&nbsp;</th>
    </tr>
    <tr>
      <th>Method</th>
      <th style="text-align: center">R1</th>
      <th style="text-align: center">R2</th>
      <th style="text-align: center">R1</th>
      <th style="text-align: center">R2</th>
      <th style="text-align: center">R1</th>
      <th style="text-align: center">R2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>DLG</td>
      <td style="text-align: center">59.3</td>
      <td style="text-align: center">7.7</td>
      <td style="text-align: center">49.7</td>
      <td style="text-align: center">5.7</td>
      <td style="text-align: center">37.6</td>
      <td style="text-align: center">1.7</td>
    </tr>
    <tr>
      <td>TAG</td>
      <td style="text-align: center">78.9</td>
      <td style="text-align: center">10.2</td>
      <td style="text-align: center">68.8</td>
      <td style="text-align: center">7.6</td>
      <td style="text-align: center">56.2</td>
      <td style="text-align: center">6.7</td>
    </tr>
    <tr>
      <td>$\text{LAMP}_{\cos}$</td>
      <td style="text-align: center"><strong>89.6</strong></td>
      <td style="text-align: center"><strong>51.9</strong></td>
      <td style="text-align: center">74.4</td>
      <td style="text-align: center">29.5</td>
      <td style="text-align: center">55.2</td>
      <td style="text-align: center">14.5</td>
    </tr>
    <tr>
      <td>$\text{LAMP}_{\text{L1}+\text{L2}}$</td>
      <td style="text-align: center">87.5</td>
      <td style="text-align: center">47.5</td>
      <td style="text-align: center"><strong>78.0</strong></td>
      <td style="text-align: center"><strong>31.4</strong></td>
      <td style="text-align: center"><strong>66.2</strong></td>
      <td style="text-align: center"><strong>21.8</strong></td>
    </tr>
  </tbody>
</table>
<br><br>
We see that despite the worse quality of reconstruction, even batch size of 4 still leaks a substantial amount of data. Further, we observe that for bigger batch sizes LAMP<sub>L1+L2</sub> performs better than LAMP<sub>cos</sub>. Both LAMP methods, however, substantially improve upon the results of the baselines.
Finally, we show an example sentence reconstruction from LAMP and TAG on multiple datasets below:
<img src="/assets/blog/lamp/text_rec.png" class="blogpost-img100" style="margin: 30pt 0pt 30pt 0pt;">
Here, yellow signifies a single correctly reconstructed word and green signifies a tuple of correctly recovered words. We see that LAMP recovers the word order drastically better and often is even able to reconstruct it perfectly. In addition, LAMP recovers more individual words. This confirms qualitatively the effectiveness of our attack.

### Summary

In this blog post, we introduced LAMP, a new framework for gradient leakage of text data from gradient updates in federated learning. Our key ideas are the alternating of continuous and discrete optimization steps and the introduction of an auxiliary text model which we use in the discrete part of our optimization to judge how well a piece of text is reconstructed. Thanks to these elements, our attack is able to produce substantially better text reconstructions compared to the state-of-the-art attacks both quantitatively and qualitatively. We, thus, show that many practical federated learning systems based on text are vulnerable and better mitigation steps should be taken.
For more details please see our [NeurIPS 2022 paper](https://files.sri.inf.ethz.ch/website/papers/balunovic2022lamp.pdf).

