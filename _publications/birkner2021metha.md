---
ref: birkner2021baitfish
title: "Metha: Network Verifiers Need To Be Correct Too!"
authors: Rüdiger Birkner*, Tobias Brodmann*, Petar Tsankov, Laurent Vanbever, Martin Vechev
year: 2021
month: 04
venue: USENIX NSDI
projects: programmable-networks
awards:
bibtex: 
paper: https://files.sri.inf.ethz.ch/website/papers/metha-nsdi21.pdf
talk: 
slides: 
---

Network analysis and verification tools are often a godsend for network operators as they free them from the fear of introducing outages or security breaches. As with any complex software though, these tools can (and often do) have bugs. For the operators, these bugs are not necessarily problematic except if they affect the precision of the network model. In that case, the tool output might be wrong: it might fail to detect actual configuration errors and/or report non-existing ones.

In this paper, we present Metha, a framework that systematically tests network analysis and verification tools for bugs in their network models. Metha automatically generates syntactically- and semantically-valid configurations; compares the tool's output to that of the actual router software; and detects any discrepancy as a bug in the tool's model. The challenge in testing network analyzers this way is that a bug may occur very rarely and only when a specific set of configuration statements is present. We address this challenge by leveraging grammar-based fuzzing together with combinatorial testing to ensure thorough coverage of the search space and by identifying the minimal set of statements triggering the bug through delta debugging.

We fully implemented Metha and used it to test three well-known tools. In all of them, we found multiple (new) bugs in their models, most of which were confirmed by the developers themselves.
