---
ref: jovanovic2021certified
title: "Certified Defenses: Why Tighter Relaxations May Hurt Training"
authors: Nikola Jovanovic*, Mislav Balunovic*, Maximilian Baader, Martin Vechev
year: 2021
month: 6
venue: arXiv
projects: safeai
bibtex: '@misc{jovanović2021certified,
      title={Certified Defenses: Why Tighter Relaxations May Hurt Training}, 
      author={Nikola Jovanović and Mislav Balunović and Maximilian Baader and Martin Vechev},
      year={2021},
      eprint={2102.06700},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
}'
paper: https://arxiv.org/abs/2102.06700
---

Certified defenses based on convex relaxations are an established technique for training provably robust models. The key component is the choice of relaxation, varying from simple intervals to tight polyhedra. Paradoxically, however, training with tighter relaxations can often lead to worse certified robustness. The poor understanding of this paradox has forced recent state-of-the-art certified defenses to focus on designing various heuristics in order to mitigate its effects. In contrast, in this paper we study the underlying causes and show that tightness alone may not be the determining factor. Concretely, we identify two key properties of relaxations that impact training dynamics: continuity and sensitivity. Our extensive experimental evaluation demonstrates that these two factors, observed alongside tightness, explain the drop in certified robustness for popular relaxations. Further, we investigate the possibility of designing and training with relaxations that are tight, continuous and not sensitive. We believe the insights of this work can help drive the principled discovery of new and effective certified defense mechanisms. 

