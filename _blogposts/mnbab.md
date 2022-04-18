---
layout: blogpost
category: paper
pub-ref: ferrari2022complete
title: "Multi-Neuron Relaxation Guided Branch-and-Bound"
blogpost-authors: "Claudio Ferrari" 
date: 2022-02-01
thumbnail: _thumbnails/mnbab.svg
usemathjax: true
tldr: >
    With MN-BaB, our new state-of-the-art neural network verifier, we leverage precise multi-neuron constraints together with the Branch-and-Bound approach for verification to allow us to verify networks with higher natural accuracy.
excerpt: >
    Learn more how multi-neuron constraints can be used in a Branch-and-Bound approach to build a state-of-the-art complete neural network verifier.

draft: true
tweet-id:
---

This blog explains the high-level ideas and intuitions behind [MN-BaB](https://files.sri.inf.ethz.ch/website/papers/ferrari2022complete.pdf). We will first introduce the neural network verification problem. Then we will present a class of algorithms that solve this problem using a Branch-and-Bound approach, before instantiating MN-BaB as one particular algorithm of this class. We will conclude with some thoughts and experiments on why using multi-neuron constraints is key for verification.

### Neural Network Verification Problem Statement
In a nutshell, the neural network verification problem can be stated as follows:

| Given a network and an input, prove that in a small perturbation region around that input no [adversarial example](https://openai.com/blog/adversarial-example-research/) exists.

To formalize this a bit, we consider: a network $f: \mathcal{X} \to \mathcal{Y}$, an input region $\mathcal{D} \subseteq \mathcal{X}$, and a linear property $\mathcal{P}\subseteq \mathcal{Y}$ over the output neurons $y\in\mathcal{Y}$, and we are tasked to prove:

 $f(x) \in \mathcal{P},$ $ \forall  x \in \mathcal{D}$.

We consider $L$-layer networks with ReLU activations as the Branch-and-Bound framework only yields complete verifiers for piecewise linear activation functions but remark that our approach applies to a wide class of activations including ReLU, Sigmoid, Tanh, MaxPool, and others.
We denote the weights and biases of neurons in the $i$-th layer as $W^{(i)}$ and $b^{(i)}$.

Further, the neural network is defined as $f(x) := \hat{z}^{(L)}(x)$ where $\hat{z}^{(i)}(x) := W^{(i)}z^{(i-1)}(x) + b^{(i)}$ and $z^{(i)}(x) := \max(0, \hat{z}^{(i)}(x))$.
For readability, we omit the dependency of intermediate activations on $x$.

For our purposes, let $\mathcal{D}$ be the $\ell_\infty$ ball around an input point $x_0$ of radius $\epsilon$: $\mathcal{D}_\epsilon(x_0) = \left\\{ x \in \mathcal{X} \mid \lVert x - x_0\rVert _{\infty} \leq  \epsilon \right\\}$.
Since we can encode any linear property over output neurons into an additional affine layer, we can simplify the general formulation
$f(x) \in \mathcal{P}$ to $f(x) > \mathbf{0}$.
The property can now be verified by proving that a lower bound to the following optimization problem is greater than $0$:

$$
\begin{align*}
    \min_{x \in \mathcal{D}_\epsilon(x_0)} \qquad &f(x) = \hat{z}^{(L)} \tag{1} \\
    s.t. \quad & \hat{z}^{(i)} = W^{(i)}z^{(i-1)} + b^{(i)}\\
        & z^{(i)} = \max(\mathbf{0}, \hat{z}^{(i)})\\
\end{align*}
$$

### Background: Branch-and-Bound for Neural Network Verification
Although there are many potential ways to tackle the verification problem, many recent advances in the field can be formulated as a Branch-and-Bound algorithm, as shown in [Branch and Bound for Piecewise Linear Neural Network Verification](https://arxiv.org/pdf/1909.06588.pdf). 

The high-level motivation is the following: the optimization problem in Eq. 1 would be efficiently solveable if not for the non-linear constraints of the ReLU function. Since a ReLU function is piece-wise linear and composed of only two linear functions, we can make a case distinction on a single ReLU node being "active" (input is larger equal 0) or inactive (input is less than 0) and prove the property for each case while only having to deal with a linear constraint. 

In the limit case where all ReLU nodes are split, the verification problem has all linear constraints and can be solved efficiently. In practice splitting all ReLU nodes would be computationally intractable for all interesting verification problems, since the number of subproblems to be solved in the resulting Branch-and-Bound tree is exponential in the number of ReLU neurons in the network. To overcome this, we make use of the fact that if for a subproblem we can find a lower bound to Eq. 1 that is larger than 0, we do not have to split it any further, and thus prune the Branch-and-Bound tree significantly.

In pseudo-code the algorithm looks as follows:
{% highlight python %}
def verify_with_branch_and_bound(network, input_region, output_property) -> bool:
  problem_instance = (input_region, output_property)
  
  global_lb, global_ub = bound(network, problem_instance)
  unsolved_subproblems = [(global_lb, problem_instance)]
  
  while global_lb < 0 and global_ub >= 0:
    _, current_subproblem = unsolved_subproblems.pop()
    current_lb, current_ub = bound(network, current_subproblem)

    if current_ub < 0:
      return False
    if current_lb < 0:
      subproblem_left, subproblem_right = branch(current_subproblem)
      unsolved_subproblems.append(subproblem_left, subproblem_right)

    global_lb = min(lb for lb, _ in unsolved_subproblems)
  return global_lb > 0

{% endhighlight %}

To define one particular verification method that follows the Branch-and-Bound approach, all we have to do is instantiate the **branch()** and **bound()** functions.

### MN-BaB

 **Bounding**

The bound() method tries to prove a lower bound to Eq. 1 that's as tight as possible. The tighter it is, the earlier the Branch-and-Bound process can be terminated.

For MN-BaB, following [previous](https://files.sri.inf.ethz.ch/website/papers/DeepPoly.pdf) [works](https://arxiv.org/abs/2103.06624) we derive a lower bound of the network's output as a linear function of the inputs:

$\displaystyle \min_{x \in \mathcal{D}} f(x) \geq \min_{x \in \mathcal{D}} a_{inp}x + c_{inp}$

The minimization over $x \in \mathcal{D}$ has a closed form solution given by [Hölder's inequality](https://en.wikipedia.org/wiki/Hölder%27s_inequality):

$\displaystyle \min_{x \in \mathcal{D}} a_{inp}x + c^{(0)} \geq a_{inp}x_0 - \lVert a_{inp} \rVert_1 \epsilon + c_{inp}$

To arrive at a linear lower bound of the output in terms of the input, we start with the trivial lower bound $f(x) \geq z^{(L)}W + b^{(L)}$. We derive linear upper and lower bounds of the form $z^{(i)} \geq Az^{(i-1)} + c$ for every layer's output in terms of its inputs $z^{(i-1)}$. Then, starting with a linear expression in the last layer's outputs $z^{(L)}$ which we aim to bound, we use the linear bounds described above, to replace $z^{(L)}$ with symbolic bounds depending only on the previous layer's values $z^{(L-1)}$. We proceed in this manner recursively until we obtain an expression only in terms of the inputs of the network.

Finding the linear relaxations of different layer types, especially for non-linear activation layers, is where most of the magic that differentiates MN-BaB happens. Most crucially, MN-BaB is able to enforce multi-neuron constraints in an efficiently optimizable fashion. The details are rather technical and notation heavy, so the interested reader is referred to the [paper](https://files.sri.inf.ethz.ch/website/papers/ferrari2022complete.pdf) for this.

To derive the linear relaxations for activation layers, we need bounds on the inputs of those layers. In order to compute lower and upper bounds, we apply the same procedure described above to each activation neuron in the network, starting from the first activation layer.

Note that if those input bounds for a ReLU node are either both negative or both positive, the corresponding activation function becomes linear and we will not have to split this node during the Branch-and-Bound process. We call such nodes "stable" and correspondingly nodes where the input bounds contain zero "unstable".

![Alt Text](/assets/blog/mn-bab/stable_vs_unstable.png){: .blogpost-img100}

{: .blogpost-caption}
*From Left to Right: stable inactive, stable active, unstable.*

**Branching**

The branch() method takes a problem instance and splits it into two subproblems. As a first step, it has to decide which unstable ReLU node will be split. Secondly, it will add an additional constraint, $<0$ and $\geq0$ respectively, on the input of the corresponding neuron to the resulting subproblems.

![Alt Text](/assets/blog/mn-bab/split_constraints.png){: .blogpost-img80}

{: .blogpost-caption}
*The split constraints that are added to the generated subproblems.*

Deciding which unstable node to split next should be done to minimize the total number of subproblems that need to be solved during the Branch-and-Bound process. As this quantity is not known during the Branch-and-Bound process, we need to use a proxy score to decide which unstable node to split. Note that the optimal branching decision depends on the bounding method that is used, as different bounding methods might profit differently from additional constraints resulting from the split.

Our bounding method relies on multi-neuron constraints, therefore we designed a proxy score that makes use of them called Active Constraint Score (ACS). ACS determines the sensitivity of the final optimization objective with respect to the multi-neuron constraints and then for each node computes the cumulative sensitivity of all constraints containing that node. The node to split is determined by taking the one with the highest Active Constraint Score.

We further propose Cost Adjusted Branching (CAB) to scale these branching scores by the expected cost of performing a split. As intermediate bounds before the split layer do not have to be recomputed, it is computationally cheaper to split in later layers. As the ultimate metric of verification performance is total runtime, we propose to also consider the runtime aspect of branching decisions.

**Why use multi-neuron constraints?**

The intuitive argument why multi-neuron constraints help verification performance is that the number of subproblems solved during Branch-and-Bound grows exponentially with the depth of the subproblem tree. A more precise bounding method that can verify subproblems earlier (at a smaller depth), can therefore save us exponentially many subproblems that we do not need to solve.

A second advantage of using multi-neuron constraints is that their benefit is more pronounced the more dependencies there are between neurons in the same layer. 
Most benchmarks in the field, for example [VNNComp](https://sites.google.com/view/vnn2021), consider networks that were specifically trained to be easily verifiable through adversarial or certified training. Such training methods, while facilitating easier verification, reduce the amount of intra-layer dependencies between neurons compared to normally trained networks (which is partly what makes them easier to verify). They also, however significantly hurt natural accuracy, making the resulting networks less interesting for practical applications. Therefore, if we want to verify networks with high natural accuracy (and more intra-layer dependencies), the benefits of multi-neuron constraints are even more pronounced.
### Experiments
Here we present an ablation study of all individual components of MN-BaB. First the first 100 test images of the [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) dataset, we aim to prove that there is no adversarial example within an $l_\infty$ ball of radius $\epsilon=1/255$ around them. We report both the number of verified samples (within a timeout of 600 seconds), as well as the average runtime for verifying the samples.
We consider two networks of identical architecture that only differ in the strength of their adversarial training method. ResNet6-A is weakly regularized while ResNet6-B is more strongly regularized, i.e. employs stronger adversarial training.

![Alt Text](/assets/blog/mn-bab/ablation_study.png){: .blogpost-img80}

{: .blogpost-caption}
*Evaluating the effect of multi-neuron constraints (MNCs), Active Constraint Score (ACS) branching, and Cost Adjusted Branching (CAB) on MN-BaB. BaBSR is another branching method that is used as a baseline.*

We see that the effect of multi-neuron constraints is much larger on the weakly regularized ResNet6-A where we verify 20% more samples while being around 22% faster, while on ResNet6-B we only verify 6% more samples. The benefit of Active Constraint Score branching is also more pronounced on ResNet6-A where the multi-neuron constraints make a larger difference (15% more samples vs. 3% on ResNet6-B), which is expected since Active Constraint Scores rely on the multi-neuron constraints for signal.

As verified accuracy and mean runtime are very coarse performance metrics, we also analyze the ratio of runtimes and number of subproblems required for verification on a per-property level on ResNet6-A, filtering out those where both methods verify before any branching occurred.

**Effectiveness of Multi-Neuron Constraints**
![Alt Text](/assets/blog/mn-bab/ResNet6-A_n_subproblems_ratio_w_wo_MNC.pdf){: .blogpost-img100}

{: .blogpost-caption}
*The ratio of the number of subproblems solved during Branch-and-Bound without vs. with multi-neuron constraints.*

On average the number of subproblems is reduced by over two orders of magnitude and for every property the number of subproblems is less with multi-neuron constraints than without.

**Effectiveness of Active Constraint Score Branching**

![Alt Text](/assets/blog/mn-bab/ResNet6-A_n_subproblems_ratio_branching.pdf){: .blogpost-img100}

{: .blogpost-caption}
*The ratio of the number of subproblems solved during Branch-and-Bound with BaBSR vs. ACS.*

We observe that Active Constraint Score branching yields significantly fewer subproblems on most (75%) properties and reduces the number of subproblems solved by another order of magnitude on average.

**Effectiveness of Cost Adjusted Branching**

![Alt Text](/assets/blog/mn-bab/ResNet6-A_cab_runtime_comparison_p4c_acs.pdf){: .blogpost-img100}

{: .blogpost-caption}
*Effect of Cost Adjusted Branching on mean verification time with ACS.*

Since Cost Adjusted Branching is designed not to reduce the number of subproblems solved but to improve total runtime, we compare the runtime per property with and without Cost Adjusted Branching. We see that it reduces the verification time on all properties, sometimes even very significantly, leading to an average speedup of 50%. Analyzing the results in the Table, we observe that CAB is particularly effective in combination with the ACS scores and multi-neuron constraints, where bounding costs vary more significantly.

### Recap
Hopefully, this blog helped convey the basic principles and intuitions behind MN-BaB. For a full breakdown of all technical details and detailed experimental evaluations, we recommend reading the [paper](https://www.sri.inf.ethz.ch/publications/ferrari2022complete). If you are more practically oriented and want to play around with the tool, the [code](https://github.com/eth-sri/mn-bab) is publicly available.