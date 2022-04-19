---
layout: blogpost
category: paper
pub-ref: ferrari2022complete
title: "Multi-Neuron Relaxation Guided Branch-and-Bound"
blogpost-authors: "Claudio Ferrari, Mark Niklas Müller"
date: 2022-02-01
thumbnail: _thumbnails/mnbab.svg
usemathjax: true
tldr: >
    MN-BaB is our most recent neural network verifier and combines  precise multi-neuron constraints with the Branch-and-Bound paradigme and an efficient GPU based solver to allow the verification of networks with high natural accuracy.
excerpt: >
    Learn more about how multi-neuron constraints can be used in a Branch-and-Bound approach to build a state-of-the-art complete neural network verifier.

draft: true
tweet-id:
---

This blog post explains the high-level ideas and intuitions behind our most recent neural network verifier [MN-BaB](https://files.sri.inf.ethz.ch/website/papers/ferrari2022complete.pdf). First, we introduce the neural network verification problem. Then, we  present the so-called Branch-and-Bound approach to solving them and outline the main ideas behind multi-neuron constraints, before combining the two in our new verifier MN-BaB. We conclude with some thoughts and experiments on why using multi-neuron constraints is key for the verification of challenging networks with high natural accuracy.

### Neural Network Verification
In a nutshell, the neural network verification problem can be stated as follows:

> Given a network and an input, prove that in a small perturbation region around that input no [adversarial example](https://openai.com/blog/adversarial-example-research/) exists.

To formalize this a bit, we consider: a network $f: \mathcal{X} \to \mathcal{Y}$, an input region $\mathcal{D} \subseteq \mathcal{X}$, and a linear property $\mathcal{P}\subseteq \mathcal{Y}$ over the output neurons $y\in\mathcal{Y}$, and we try to prove that

 $$f(x) \in \mathcal{P}, \forall  x \in \mathcal{D}.$$

For the sake of explanation, we consider a fully connected $L$-layer networks with ReLU activations, but note that we can handle all common architectures. <!--as the Branch-and-Bound framework only yields complete verifiers for piecewise linear activation functions but remark that our approach applies to a wide class of activations including ReLU, Sigmoid, Tanh, MaxPool, and others.--> We denote the weights and biases of neurons in the $i$-th layer as $W^{(i)}$ and $b^{(i)}$ and define the nerual network as 

$$f(x) := \hat{z}^{(L)}(x), \qquad \hat{z}^{(i)}(x) := W^{(i)}z^{(i-1)}(x) + b^{(i)}, \qquad z^{(i)}(x) := \max(0, \hat{z}^{(i)}(x)).$$

Where $z^{(0)}(x) = x$ denotes the input. For readability, we omit the dependency of intermediate activations on $x$ from here on.

For our purposes, let $\mathcal{D}$ be an $\ell_\infty$ ball around an input point $x_0$ of radius $\epsilon$: 
$$\mathcal{D}_\epsilon(x_0) = \left\{ x \in \mathcal{X} \mid \lVert x - x_0\rVert _{\infty} \leq  \epsilon \right\}.$$

Since we can encode any linear property over output neurons into an additional affine layer, we can simplify the general formulation to $f(x) \in \mathcal{P}$ to $f(x) > \mathbf{0}$.Any such property can now be verified by proving that a lower bound to the following optimization problem is greater than $0$:

$$
\begin{align*}
    \min_{x \in \mathcal{D}_\epsilon(x_0)} \qquad &f(x) = \hat{z}^{(L)} \tag{1} \\
    s.t. \quad & \hat{z}^{(i)} = W^{(i)}z^{(i-1)} + b^{(i)}\\
        & z^{(i)} = \max(\mathbf{0}, \hat{z}^{(i)})\\
\end{align*}
$$

### Background: Branch-and-Bound for Neural Network Verification
Recently, the Branch-and-Bound approach, first described for this task in [Branch and Bound for Piecewise Linear Neural Network Verification](https://arxiv.org/pdf/1909.06588.pdf), has become popularized. At a high level, it is based on splitting the hard optimization problem of Eq. 1 into multiple easier ones by adding additional constraints until we can show the desired bound of $f(x) > 0$ on these subproblems.

The high-level motivation is the following: the optimization problem in Eq. 1 would be efficiently solvable if not for the non-linearity of the ReLU function. Since a ReLU function is however piece-wise linear and composed of only two linear regions, we can make a case distinction between a single ReLU node being "active" (input $\geq 0$) or inactive (input $< 0$) and prove the property on the resulting cases where the ReLU behaves linearly. 

In the limit where all ReLU nodes are split, the verification problem becomes fully linear and can be solved efficiently. However, the number of subproblems to be solved in the resulting Branch-and-Bound tree is exponential in the number of ReLU neurons that we split on. Therefore, splitting all ReLU nodes is computationally intractable for all interesting verification problems. To tackle this problem, we prune this Branch-and-Bound tree using the insight that we do not have to split a subproblem further, once we find a lower bound that is $>0$.

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

### Background: Multi-Neuron Constraints
To solve the optimization problem in Eq. 1 efficiently, we want to replace the non linear constraint $z = \max(\mathbf{0}, \hat{z})$ with its so-called linear relaxation, i.e., a set of linear constraints that is satisfied for all points satisfying the orignal non-linear constraint. 

If we consider just a single neuron, the tightest such linear relaxation, is the convex hull of the function in its input output space, illsutrated below:

![DeepPoly ReLU abstraction](/assets/blog/mn-bab/DeepPoly.png){: .blogpost-img50}


However, considering one neuron at a time comes with a fundamental precision limit, called the [(single-neuron) convex relaxation barrier](https://proceedings.neurips.cc/paper/2019/hash/246a3c5544feb054f3ea718f61adfa16-Abstract.html). It has since been shown, that this limit can be overcome by considering multiple neurons jointly, thereby capturing interactions between these neurons and obtaining tighter bounds. We use the efficiently computable multi-neuron constraints from [PRIMA](https://www.sri.inf.ethz.ch/publications/mueller2021precise), which can be expressed as a conjunction of linear constraints over the joint
input and output space of a ReLU layer. We illustrate the difference in tightness below:

![PRIMA ReLU abstraction](/assets/blog/mn-bab/PRIMA.png){: .blogpost-img50}

### MN-BaB

 **Bounding**

The goal of the bound() method is to derive a lower bound to Eq. 1 that's as tight as possible. The tighter it is, the earlier the Branch-and-Bound process can be terminated.

Following [previous](https://files.sri.inf.ethz.ch/website/papers/DeepPoly.pdf) [works](https://arxiv.org/abs/2103.06624), we derive a lower bound of the network's output as a linear function of the inputs:

$$ \min_{x \in \mathcal{D}} f(x) \geq \min_{x \in \mathcal{D}} a_{inp}x + c_{inp}$$

The minimization over $x \in \mathcal{D}$ has a closed form solution given by [Hölder's inequality](https://en.wikipedia.org/wiki/Hölder%27s_inequality):

$$ \min_{x \in \mathcal{D}} a_{inp}x + c^{(0)} \geq a_{inp}x_0 - \lVert a_{inp} \rVert_1 \epsilon + c_{inp}$$

To arrive at a linear lower bound of the output in terms of the input, we start with the trivial lower bound $f(x) \geq z^{(L)}W + b^{(L)}$ and replace $z^{(L)}$ with symbolic, linear bounds depending only on the previous layer's values $z^{(L-1)}$. We proceed in this manner recursively until we obtain an expression only in terms of the inputs of the network.

These so-called linear relaxations of the different layer types determine the precision of the the obtained bounding method. While affine layers (e.g., fully connected, convolutional, avg. pooling, normalization) can be captured exactly, non-linear activation layers remain challenging and are where most of the magic that differentiates MN-BaB happens. Most importantly, MN-BaB is able to enforce multi-neuron constraints in an efficiently optimizable fashion. The details are rather technical and notation heavy, so the interested reader is referred to the [paper](https://files.sri.inf.ethz.ch/website/papers/ferrari2022complete.pdf) for this.

To derive the linear relaxations for activation layers, we need bounds on the inputs of those layers. In order to compute these lower and upper bounds on every neuron, we apply the procedure described above to every neuron in the network, starting from the first activation layer.

Note that if those input bounds for a ReLU node are either both negative or both positive, the corresponding activation function becomes linear and we do not have to split this node during the Branch-and-Bound process. We call such nodes "stable" and correspondingly nodes where the input bounds contain zero "unstable".

![Alt Text](/assets/blog/mn-bab/stable_vs_unstable.png){: .blogpost-img100}

{: .blogpost-caption}
*From Left to Right: stable inactive, stable active, unstable.*

**Branching**

The branch() method takes a problem instance and splits it into two subproblems. This entails deciding which unstable ReLU node to split and adding additional constraints to both resulting subproblems enforcing $<0$ or $\geq0$, on the input of the split neuron.

![Alt Text](/assets/blog/mn-bab/split_constraints.png){: .blogpost-img80}

{: .blogpost-caption}
*The split constraints that are added to the generated subproblems.*

The choice of which node to split has a significant impact on how many subproblems we have to consider during the Branch-and-Bound process until we can proof a property. Therefore, we aim to choose a neuron that minimizes the total number of problems we have to consider, to this end, we define a proxy score trying to capture the bound improvement resulting from any particular split. Note that the optimal branching decision depends on the bounding method that is used, as different bounding methods might profit differently from additional constraints resulting from the split.

As our bounding method relies on multi-neuron constraints, we designed a proxy score that is specifically tailored to them, called the Active Constraint Score (ACS). ACS determines the sensitivity of the final optimization objective with respect to the multi-neuron constraints and then, for each node, computes the cumulative sensitivity of all constraints containing that node. We then split the node with the highest cumulative sensitivity.

We further propose Cost Adjusted Branching (CAB) to scale this branching score by the expected cost of performing a particular split. This cost can differ significantly, as only the intermediate bounds after the split layer have to be recomputed, making splits in later layers computationally cheaper.

### Why use multi-neuron constraints?

Intuitively there is a trade-off between the number of subproblems that have to be considered and the precision of the bound computed on each of them. We observe that the number of considered subproblems increases exponentially with the depth of the Branch-and-Bound tree, while the increase in precision deminishes with depth. Using a more precise bounding method that can verify subproblems earlier (at a smaller depth), can therefore save us exponentially many subproblems that we do not need to solve. We thus propose to use a more precise but also computationally costly bounding methods based on multi-neuron constraints to improve verification performance. 

This benefit is more pronounced the larger the considered network and the more dependencies there are between neurons in the same layer. 
While most established benchmarks (e.g., from [VNNComp](https://sites.google.com/view/vnn2021)) are based on very small networks or use training methods designed for ease of verification at the cost of natural accuracy, to make their certification tractable, they are less representative of for practical applications. Therefore, we suggest to focus on larger, more challenging networks with higher natural accuracy (and more intra-layer dependencies) for the evaluation of the next generation of verifiers. There, the benefits of multi-neuron constraints are particularly pronounced, leading us to believe that they represent a promising direction.

### Experiments
Here, we study the effect of MN-BaB's components in an ablation study on the first 100 test images of the [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) dataset. We aim to prove that there is no adversarial example within an $l_\infty$ ball of radius $\epsilon=1/255$ and report the number of verified samples (within a timeout of 600 seconds) and the corresponding average runtime.
We consider two networks of identical architecture that only differ in the strength of their adversarial training method. ResNet6-A is weakly regularized while ResNet6-B is more strongly regularized, i.e. employs stronger adversarial training.

![Alt Text](/assets/blog/mn-bab/ablation_study.png){: .blogpost-img50}

{: .blogpost-caption}
*Evaluating the effect of multi-neuron constraints (MNCs), Active Constraint Score (ACS) branching, and Cost Adjusted Branching (CAB) on MN-BaB. BaBSR is another branching method that is used as a baseline.*

As expected, we observe that both multi-neuron constraints and Active Constraint Score branching are much more effective on the weakly regularized ResNet6-A. There, we verify 31% more samples while being around 31% faster, while on ResNet6-B we only verify 10% more samples.

As a more fine grained measure of performance, we analyze the ratio of runtimes and number of subproblems required for verification on a per-property level on ResNet6-A, below.

**Effectiveness of Multi-Neuron Constraints**
![Alt Text](/assets/blog/mn-bab/ResNet6-A_n_subproblems_ratio_w_wo_MNC.png){: .blogpost-img50}

{: .blogpost-caption}
*The ratio of the number of subproblems solved during Branch-and-Bound without vs. with multi-neuron constraints.*

Using multi-neuron constraints reduces the number of subproblems required to prove a property by, on average, two orders of magnitude.

**Effectiveness of Active Constraint Score Branching**

![Alt Text](/assets/blog/mn-bab/ResNet6-A_n_subproblems_ratio_branching.png){: .blogpost-img50}

{: .blogpost-caption}
*The ratio of the number of subproblems solved during Branch-and-Bound with BaBSR vs. ACS.*

Using Active Constraint Score branching instead of BaBSR reduces the number of subproblems required to prove a property by, on average, an additional order of magnitude.

**Effectiveness of Cost Adjusted Branching**

![Alt Text](/assets/blog/mn-bab/ResNet6-A_cab_runtime_comparison_p4c_acs.png){: .blogpost-img50}

{: .blogpost-caption}
*Effect of Cost Adjusted Branching on mean verification time with ACS.*

Using Cost Adjusted Branching reduces the verification time by, on average, a further 50%. It is particularly effective in combination with the ACS scores and multi-neuron constraints, where bounding costs vary most significantly.


### Recap
MN-BaB combines precise mutli-neuron constraints with the Branch-and-Bound paradigm and an efficient GPU based implementation to become a new state-of-the-art verifier, especially for less regularized networks. For a full breakdown of all technical details and detailed experimental evaluations, we recommend reading our [paper](https://www.sri.inf.ethz.ch/publications/ferrari2022complete). If you want to play around with MN-BaB yourself, please check out our [code](https://github.com/eth-sri/mn-bab).
