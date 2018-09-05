---
  ref: tsankov14failsecure
  title: Fail-Secure Access Control
  authors: Petar Tsankov, Srdjan Marinovic, Mohammad Torabi Dashti, David Basin
  year: 2014
  venue: ACM CCS
  projects: 
  awards:
  bibtex:
  paper: tsankov14failsecure.pdf
  talk: 
  slides: tsankov14failsecure-slides.pdf
---

Decentralized and distributed access control systems are sub- ject to communication and component failures. These can affect access decisions in surprising and unintended ways, resulting in insecure systems. Existing analysis frameworks however ignore the influence of failure handling in deci- sion making. Thus, it is currently all but impossible to derive security guarantees for systems that may fail. To address this, we present (1) a model in which the attacker can explicitly induce failures, (2) failure-handling idioms, and (3) a method and an associated tool for verifying fail- security requirements, which describe how access control systems should handle failures. To illustrate these contri- butions, we analyze the consequences of failure handling in the XACML3 standard and other domains, revealing secu- rity flaws.