---
layout: blogpost
category: paper
pub-ref: bichsel2020silq
title: "A proper quantum programming language"
blogpost-authors: "Benjamin Bichsel, Maximilian Baader, Timon Gehr"
date: 2021-09-01
thumbnail: _thumbnails/silq.svg
usemathjax: true
tldr: >
    We present Silq, the first quantum language that supports safe, automatic uncomputation. This enables an intuitive semantics that implicitly drops temporary values, as in classical computation. To ensure physicality of Silq’s semantics, its type system leverages novel annotations to reject unphysical programs. Our experimental evaluation demonstrates that Silq programs are not only easier to read and write, but also significantly shorter than equivalent programs in other quantum languages, while using only half the number of quantum primitives.
excerpt: >
    Silq is the first high-level quantum programming language designed for safety and convenience.
keywords: quantum computing, programming languages
conf-url: https://icml.cc/virtual/2021/poster/9327
conf-info: Poster - Tue Jul 20, 18:00 GMT+2 (Poster Session 4)

draft: true
tweet-id: 1447996320741007362
---

We present Silq, the first quantum language that supports safe, automatic uncomputation. This enables an intuitive semantics that implicitly drops temporary values, as in classical computation. To ensure physicality of Silq’s semantics, its type system leverages novel annotations to reject unphysical programs. Our experimental evaluation demonstrates that Silq programs are not only easier to read and write, but also significantly shorter than equivalent programs in other quantum languages, while using only half the number of quantum primitives.