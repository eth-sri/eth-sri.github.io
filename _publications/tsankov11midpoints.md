---
  ref: tsankov11midpoints
  title: Constructing Midpoints for Two-Party Asynchronous Protocols
  authors: Petar Tsankov, Mohammad Torabi Dashti, David Basin
  year: 2011
  venue: OPODIS  
  projects: 
  awards:
  bibtex:
  paper: https://files.sri.inf.ethz.ch/website/papers/tsankov11midpoints.pdf
  talk: 
  slides: https://files.sri.inf.ethz.ch/website/slides/tsankov11midpoints-slides.pdf
---

Communication protocols describe the steps that the communication end-points must take in order to achieve a common goal. In practice, networks often contain mid-points, which can relay, redirect, or filter messages exchanged by the end-points. A mid-point can enforce a communication protocol: it for- wards the messages that conform to the protocol, and drops them otherwise. Pro- tocol specifications typically define only the end-points’ behavior. Implementing a mid-point that enforces a protocol is nontrivial: the mid-point’s behavior de- pends on the end-point’s behavior, and also on the behavior of the communication environment in which the protocol executes.

We present a process algebraic framework that takes as input the formal spec- ifications of the protocol and the environment and outputs a specification for a mid-point that enforces the protocol. We prove that the mid-point specifica- tions synthesized by our framework are correct: only messages that could have resulted from correctly executing end-points are forwarded. As an application, we construct a formal model for the mid-point that enforces the TCP three-way handshake protocol.
