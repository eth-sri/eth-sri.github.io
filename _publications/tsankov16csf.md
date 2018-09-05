---
  ref: tsankov16csf
  title: Access Control Synthesis for Physical Spaces
  authors: Petar Tsankov, Mohammad Torabi Dashti, David Basin
  year: 2016
  venue: IEEE CSF
  projects: 
  awards:
  bibtex:
  paper: tsankov16csf.pdf
  talk: 
  slides: tsankov16csf-slides.pdf
---

Access-control requirements for physical spaces, like office buildings and airports, are best formulated from a global viewpoint in terms of system-wide requirements. For example, “there is an authorized path to exit the building from every room.” In contrast, individual access-control components, such as doors and turnstiles, can only enforce local policies, specifying when the component may open. In practice, the gap between the system-wide, global requirements and the many local policies is bridged manually, which is tedious, error-prone, and scales poorly.

We propose a framework to automatically synthesize local access-control policies from a set of global requirements for physical spaces. Our framework consists of an expressive lan- guage to specify both global requirements and physical spaces, and an algorithm for synthesizing local, attribute-based policies from the global specification. We empirically demonstrate the framework’s effectiveness on three substantial case studies. The studies demonstrate that access-control synthesis is practical even for complex physical spaces, such as airports, with many interrelated security requirements.