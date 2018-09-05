---
ref: arnold2011qvm
title: "QVM: An Efficient Runtime for Detecting Defects in Deployed Systems"
authors: Mathew Arnold, Martin Vechev, Eran Yahav  
year: 2011
venue: ACM TOSEM (ACM Transactions on Software Engineering and Methodology)
projects: Quality virtual machine
awards:
bibtex: '@article{arnold2011qvm,
  title={QVM: An efficient runtime for detecting defects in deployed systems},
  author={Arnold, Matthew and Vechev, Martin and Yahav, Eran},
  journal={ACM Transactions on Software Engineering and Methodology (TOSEM)},
  volume={21},
  number={1},
  pages={2},
  year={2011},
  publisher={ACM}}'
paper: https://files.sri.inf.ethz.ch/website/papers/tosem11.pdf
talk: 
slides: 
---

Coping with software defects that occur in the post-deployment stage is a challenging problem: bugs may occur only when the system uses a specific configuration and only under certain usage scenarios. Nevertheless, halting production systems until the bug is tracked and fixed is often impossible. Thus, developers have to try to reproduce the bug in laboratory conditions. Often, the reproduction of the bug takes most of the debugging effort.

In this paper we suggest an approach to address this problem by using a specialized runtime environment called Quality Virtual Machine (QVM). QVM efficiently detects defects by continuously monitoring the execution of the application in a production setting. QVM enables the efficient checking of violations of user-specified correctness properties, that is, typestate safety properties, Java assertions, and heap properties pertaining to ownership. QVM is markedly different from existing techniques for continuous monitoring by using a novel overhead manager which enforces a user-specified overhead budget for quality checks. Existing tools for error detection in the field usually disrupt the operation of the deployed system. QVM, on the other hand, provides a balanced trade-off between the cost of the monitoring process and the maintenance of sufficient accuracy for detecting defects. Specifically, the overhead cost of using QVM instead of a standard JVM, is low enough to be acceptable in production environments.

We implemented QVM on top of IBM’s J9 Java Virtual Machine and used it to detect and fix various errors in real-world applications.
