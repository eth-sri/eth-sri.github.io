---
ref: ou2015interactive
title: An Interactive System for Data Structure Development 
authors: Jibin Ou, Otmar Hilliges, Martin Vechev        
year: 2015
venue: ACM CHI
projects:
awards:
bibtex: '@inproceedings{ou2015interactive,
  title={An interactive system for data structure development},
  author={Ou, Jibin and Vechev, Martin and Hilliges, Otmar},
  booktitle={Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Systems},
  pages={3053--3062},
  year={2015},
  organization={ACM}}'
paper: https://files.sri.inf.ethz.ch/website/papers/CHI15-Interactive.pdf
talk: https://youtu.be/x_QdgBQ43OI
slides: 
---

Data structure algorithms are of fundamental importance in teaching and software development, yet are difficult to understand. We propose a new approach for understanding, debugging and developing heap manipulating data structures.

The key technical idea of our work is to combine deep parametric abstraction techniques emerging from the area of static analysis with interactive abstraction manipulation. Our approach bridges program analysis with HCI and enables new capabilities not possible before: i) online automatic visualization of the data structure in a way which captures its essential operation, thus enabling powerful local reasoning, and ii) fine grained pen and touch gestures allowing for interactive control of the abstraction – at any point the developer can pause the program, graphically interact with the data, and continue program execution. These features address some of the most pressing challenges in developing data structures.

We implemented our approach in a Java-based system called FluidEdt and evaluated it with 27 developers. The results indicate that FluidEdt is more effective in helping developers find data structure errors than existing state of the art IDEs (e.g. Eclipse) or pure visualization based approaches.
