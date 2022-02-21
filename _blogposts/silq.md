---
layout: blogpost
category: paper
pub-ref: bichsel2020silq
usemathjax: true
title: "A proper quantum programming language"
blogpost-authors: "Benjamin Bichsel, Maximilian Baader, Timon Gehr"
date:   2021-09-01
thumbnail: _thumbnails/silq.svg
tldr: >
    We present Silq, the first quantum language that supports safe, automatic uncomputation. This enables an intuitive semantics that implicitly drops temporary values, as in classical computation. To ensure physicality of Silq’s semantics, its type system leverages novel annotations to reject unphysical programs. Our experimental evaluation demonstrates that Silq programs are not only easier to read and write, but also significantly shorter than equivalent programs in other quantum languages, while using only half the number of quantum primitives.
teaser: Silq is the first high-level quantum programming language designed for safety and convenience.

draft: false
---

### Content

We present Silq, the first quantum language that supports safe, automatic uncomputation. This enables an intuitive semantics that implicitly drops temporary values, as in classical computation. To ensure physicality of Silq’s semantics, its type system leverages novel annotations to reject unphysical programs. Our experimental evaluation demonstrates that Silq programs are not only easier to read and write, but also significantly shorter than equivalent programs in other quantum languages, while using only half the number of quantum primitives.