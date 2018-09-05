---
ref: shacham2011testing
title: Testing Atomicity of Composed Concurrent Operations
authors: Ohad Shacham, Nathan Bronson, Alex Aiken, Mooly Sagiv, Martin Vechev and Eran Yahav   
year: 2011
venue: ACM OOPSLA
projects: Research Area 1, Research Area 1
awards:
bibtex: '@inproceedings{shacham2011testing,
  title={Testing atomicity of composed concurrent operations},
  author={Shacham, Ohad and Bronson, Nathan and Aiken, Alex and Sagiv, Mooly and Vechev, Martin and Yahav, Eran},
  booktitle={ACM SIGPLAN Notices},
  volume={46},
  number={10},
  pages={51--64},
  year={2011},
  organization={ACM}}'
paper: oopsla11-atomicity.pdf
talk: 
slides: 
---

We address the problem of testing atomicity of composed concurrent operations. Concurrent libraries help programmers exploit parallel hardware by providing scalable concurrent operations with the illusion that each operation is executed atomically. However, client code often needs to compose atomic operations in such a way that the resulting composite operation is also atomic while preserving scalability. We present a novel technique for testing the atomicity of client code composing scalable concurrent operations. The challenge in testing this kind of client code is that a bug may occur very rarely and only on a particular interleaving with a specific thread configuration. Our technique is based on modular testing of client code in the presence of an adversarial environment; we use commutativity specifications to drastically reduce the number of executions explored to detect a bug. We implemented our approach in a tool called COLT, and evaluated its effectiveness on a range of 51 real-world concurrent Java programs. Using COLT, we found 56 atomicity violations in Apache Tomcat, Cassandra, MyFaces Trinidad, and other applications.