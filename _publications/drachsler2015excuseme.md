---
ref: drachsler2015excuseme
title: "ExcUseMe: Asking Users to Help in Item Cold-Start Recommendations"
authors: Michal Aharon, Oren Anava, Noa Avigdor-Elgrabli, Dana Drachsler-Cohen, Shahar Golan, and Oren Somekh 
year: 2015
venue: ACM RecSys
projects: Research Area 1, Research Area 1
awards:
bibtex: '@inproceedings{DBLP:conf/recsys/AharonAADGS15,
  author    = {Michal Aharon and
               Oren Anava and
               Noa Avigdor{-}Elgrabli and
               Dana Drachsler{-}Cohen and
               Shahar Golan and
               Oren Somekh},
  title     = {ExcUseMe: Asking Users to Help in Item Cold-Start Recommendations},
  booktitle = {Proceedings of the 9th {ACM} Conference on Recommender Systems, RecSys
               2015, Vienna, Austria, September 16-20, 2015},
  pages     = {83--90},
  year      = {2015}}'
paper: http://ddana.cswp.cs.technion.ac.il/wp-content/uploads/sites/19/2015/12/ExcUseMe.pdf
talk: 
slides: 
---

The item cold-start problem is of a great importance in collaborative filtering (CF) recommendation systems. It arises when new items are added to the inventory and the system cannot model them properly since it relies solely on historical users' interactions (e.g., ratings). Much work has been devoted to mitigate this problem mostly by employing hybrid approaches that combine content-based recommendation techniques or by devoting a portion of the user traffic for exploration to gather interactions from random users. We focus on pure CF recommender systems (i.e., without content or context information) in a realistic online setting, where random exploration is inefficient and smart exploration that carefully selects users is crucial due to the huge flux of new items with short lifespan. We further assume that users arrive randomly one after the other and that the system has to immediately decide whether the arriving user will participate in the exploration of the new items.

For this setting we present ExcUseMe, a smart exploration algorithm that selects a predefined number of users for exploring new items. ExcUseMe gradually excavates the users that are more likely to be interested in the new items and models the new items based on the users' interactions. We evaluated ExcUseMe on several datasets and scenarios and compared it to state-of-the-art algorithms. Experimental results indicate that ExcUseMe is an efficient algorithm that outperforms all other algorithms in all tested scenarios.
