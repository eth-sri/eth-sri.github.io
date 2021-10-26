---
ref: mueller2021monotone
title: "Effective Certification of Monotone Deep Equilibrium Models"
authors: Mark Niklas Müller, Robin Staab, Marc Fischer, Martin Vechev
year: 2021
month: 10
venue: arXiv
projects: safeai
bibtex: '@misc{mueller2021monotone,
      title={Effective Certification of Monotone Deep Equilibrium Models}, 
      author={Mark Niklas Müller and Robin Staab and Marc Fischer and Martin Vechev},
      year={2021},
      eprint={2110.08260},
      archivePrefix={arXiv},
      primaryClass={cs.LG}}'
paper: https://files.sri.inf.ethz.ch/website/papers/mueller2021monotone.pdf
#slides: https://files.sri.inf.ethz.ch/website/slides/iclr2020-colt.pdf
#image: assets/images/colt.png
#talk: https://iclr.cc/virtual_2020/poster_SJxSDxrKDr.html
---

Monotone Operator Equilibrium Models (monDEQs) represent a class of models combining the powerful deep equilibrium paradigm with convergence guarantees. Further, their inherent robustness to adversarial perturbations makes investigating their certifiability a promising research direction. Unfortunately, existing  approaches are either imprecise or severely limited in scalability. In this work, we propose the first scalable \emph{and} precise monDEQ verifier, based on two key ideas: (i) a novel convex relaxation enabling efficient inclusion checks, and (ii) non-trivial mathematical insights characterizing the fixpoint operations at the heart of monDEQs on sets rather than concrete inputs. An extensive evaluation of our verifier on the challenging L-inf perturbations demonstrates that it exceeds state-of-the-art performance in terms of speed (two orders of magnitude) and scalability (an order of magnitude) while yielding 25% higher certified accuracies on the same networks.

