---
ref: aftandilian2011asynchronous
title: Asynchronous Assertions
authors: Eddie Aftandilian, Samuel Guyer, Martin Vechev and Eran Yahav    
year: 2011
venue: ACM OOPSLA
projects: Research Area 1, Research Area 1
awards:
bibtex: '@inproceedings{aftandilian2011asynchronous,
  title={Asynchronous assertions},
  author={Aftandilian, Edward E and Guyer, Samuel Z and Vechev, Martin and Yahav, Eran},
  booktitle={ACM SIGPLAN Notices},
  volume={46},
  number={10},
  pages={275--288},
  year={2011},
  organization={ACM}}'
paper: https://files.sri.inf.ethz.ch/website/papers/oopsla11-aa.pdf
talk: 
slides: 
---

Assertions are a familiar and widely used bug detection technique. Traditional assertion checking, however, is performed synchronously, imposing its full cost on the runtime of the program. As a result, many useful kinds of checks, such as data structure invariants and heap analyses, are impractical because they lead to extreme slowdowns.

We present a solution that decouples assertion evaluation from program execution: assertions are checked asynchronously by separate checking threads while the program continues to execute. Our technique guarantees that asynchronous evaluation always produces the same result as synchronous evaluation, even if the program concurrently modifies the program state. The checking threads evaluate each assertion on a consistent snapshot of the program state as it existed at the moment the assertion started.

We implemented our technique in a system called STROBE, which supports asynchronous assertion checking in both single-and multi-threaded Java applications. STROBE runs inside the Java virtual machine and uses copy-on-write to construct snapshots incrementally, on-the-fly. Our system includes all necessary synchronization to support multiple concurrent checking threads, and to prevent data races with the main program threads. We find that asynchronous checking significantly outperforms synchronous checking, incurring tolerable overheads – in the range of 10% to 50% over no checking at all – even for heavy-weight assertions that would otherwise result in crushing slowdowns.
