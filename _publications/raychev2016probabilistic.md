---
ref: raychev2016probabilistic
title: Probabilistic Model for Code with Decision Trees
authors: Veselin Raychev, Pavol Bielik, Martin Vechev 
year: 2016
venue: ACM OOPSLA
projects: plml
awards:
bibtex: '@inproceedings{raychev2016probabilistic,
  title={Probabilistic model for code with decision trees},
  author={Raychev, Veselin and Bielik, Pavol and Vechev, Martin},
  booktitle={ACM SIGPLAN Notices},
  volume={51},
  number={10},
  pages={731--747},
  year={2016},
  organization={ACM}}'
paper: oopsla16-dt.pdf
talk: 
slides: 
---

In this paper we introduce a new approach for learning precise and general probabilistic models of code based on decision tree learning. Our approach directly benefits an emerging class of statistical programming tools which leverage probabilistic models of code learned over large codebases (e.g., GitHub) to make predictions about new programs (e.g., code completion, repair, etc).

The key idea is to phrase the problem of learning a probabilistic model of code as learning a decision tree in a domain specific language over abstract syntax trees (called TGEN). This allows us to condition the prediction of a program element on a dynamically computed context. Further, our problem formulation enables us to easily instantiate known decision tree learning algorithms such as ID3, but also to obtain new variants we refer to as ID3+ and E13, not previously explored and ones that outperform ID3 in prediction accuracy.

Our approach is general and can be used to learn a probabilistic model of any programming language. We implemented our approach in a system called DEEP3 and evaluated it for the challenging task of learning probabilistic models of JavaScript and Python. Our experimental results indicate that DEEP3 predicts elements of JavaScript and Python code with precision above 82% and 69%, respectively. Further, DEEP3 often significantly outperforms state-of-the-art approaches in overall prediction accuracy.
