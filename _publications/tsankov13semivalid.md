---
  ref: tsankov13semivalid
  title: Semi-Valid Input Coverage for Fuzz Testing
  authors: Petar Tsankov, Mohammad Torabi Dashti, David Basin
  year: 2013
  venue: ACM ISSTA
  projects: 
  awards:
  bibtex:
  paper: tsankov13semivalid.pdf
  talk: 
  slides: tsankov13semivalid-slides.pdf
---

We define semi-valid input coverage (SVCov), the first cov- erage criterion for fuzz testing. Our criterion is applicable whenever the valid inputs can be defined by a finite set of constraints. SVCov measures to what extent the tests cover the domain of semi-valid inputs, where an input is semi-valid if and only if it satisfies all the constraints but one.

We demonstrate SVCov’s practical value in a case study on fuzz testing the Internet Key Exchange protocol (IKE). Our study shows that it is feasible to precisely define and efficiently measure SVCov. Moreover, SVCov provides es- sential information for improving the effectiveness of fuzz testing and enhancing fuzz-testing tools and libraries. In particular, by increasing coverage under SVCov, we have discovered a previously unknown vulnerability in a mature IKE implementation.