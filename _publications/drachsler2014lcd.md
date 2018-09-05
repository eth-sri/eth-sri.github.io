---
ref: drachsler2014lcd
title: "LCD: Local Combining on Demand"
authors: Dana Drachsler-Cohen and Erez Petrank
year: 2014
venue: OPODIS
projects: Research Area 1, Research Area 1
awards:
bibtex: 
paper: http://ddana.cswp.cs.technion.ac.il/wp-content/uploads/sites/19/2015/12/LCD.pdf
talk: 
slides: 
---

Combining methods are highly effective for implementing concurrent queues and stacks. These data structures induce a heavy competition on one or two contention points. However, it was not known whether combining methods could be made effective for parallel scalable data structures that do not have a small number of contention points. In this paper, we introduce local combining on-demand, a new combining method for highly parallel data structures. The main idea is to apply combining locally for resources on which threads contend. We demonstrate the use of local combining on-demand on the common linked-list data structure. Measurements show that the obtained linked-list induces a low overhead when contention is low and outperforms other known implementations by up to 40% when contention is high.

