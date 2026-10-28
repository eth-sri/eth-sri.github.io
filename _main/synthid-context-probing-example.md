---
layout: blogpost
category: other
title: "SynthID context probing: a worked example"
blogpost-authors: "Thibaud Gloaguen, Robin Staab, Kristian Minchev, Martin Vechev"
usemathjax: true
mathjax_font: "TeX"
tldr: "Google DeepMind's SynthID-Text is the first large-scale LLM watermark deployment, yet little is known about how it is actually deployed. Using our work, we, for the first time, identify several key watermark hyperparameters. We find that: (1) <strong>all Gemini models are watermarked and they all share the same key except for Gemini 4 Argon</strong> (because its tokenizer is different), (2) <strong>the context size of the watermark is 4 tokens for all models</strong> (the same as the default from the open-source SynthID release), and (3) <strong>Gemini models also watermark the (hidden) thinking trace</strong>. Our findings allow us to better understand how watermarks are actually deployed in practice and understand the trade-offs made by LLM providers."
permalink: /blog/probing-synthid-gemini-apis/worked-example/
---

How do we go from stories to a watermark context size? Let's work through a small example of the [method in our blog post](/blog/probing-synthid-gemini-apis/).

### Constructing the families

We use two families, each with a five-letter reference code and four variants. Each variant keeps the first letter and shares exactly 0, 1, 2, or 3 trailing letters with its reference. For example, `r l x d y` shares the last two letters of `r b c d y`, and changes the letter immediately before them.

| Family | Code | Letters shared with reference |
|---|---|---:|
| C | `r b c d y` | reference |
| C | `r f g h z` | 0 |
| C | `r j k x y` | 1 |
| C | `r l x d y` | 2 |
| C | `r x c d y` | 3 |
| D | `k f g h z` | reference |
| D | `k l m n w` | 0 |
| D | `k p q x z` | 1 |
| D | `k r x h z` | 2 |
| D | `k x g h z` | 3 |

For each query, we select one code from each family and ask for a two-sentence story, one code per line. We record the first word after each code. For this example, suppose every sentence starts with one of three words: “The”, “Silas” (a character's name), or “Outside”. For instance, three replies might contain:

```text
r b c d y The door opened slowly.
r b c d y Silas climbed the stairs.
r b c d y Outside the rain had stopped.
```

Each line contributes one observation for the code `r b c d y`. We count only the first word after the code: “The”, “Silas”, or “Outside”. The table columns below count how often each of these words follows each code across repeated stories.

### Counting the words

We randomly split the replies into two halves, $$A$$ and $$B$$. For simplicity, suppose both halves give the counts below. Each code has 30 observations in each half.

| Code | Starts with “The” | Starts with “Silas” | Starts with “Outside” | Total |
|---|---:|---:|---:|---:|
| `r b c d y` | 12 | 9 | 9 | 30 |
| `r f g h z` | 10 | 10 | 10 | 30 |
| `r j k x y` | 10 | 13 | 7 | 30 |
| `r l x d y` | 12 | 9 | 9 | 30 |
| `r x c d y` | 12 | 9 | 9 | 30 |
| `k f g h z` | 8 | 11 | 11 | 30 |
| `k l m n w` | 10 | 10 | 10 | 30 |
| `k p q x z` | 10 | 7 | 13 | 30 |
| `k r x h z` | 8 | 11 | 11 | 30 |
| `k x g h z` | 8 | 11 | 11 | 30 |
| Total | 100 | 100 | 100 | 300 |

If word choice did not depend on the code, we would expect each code to be followed by “The” $$30\times100/300=10$$ times. The same calculation gives an expected count of 10 for each of the other two words.

### Computing the profiles

For each count, we subtract its expected value and divide by the square root of that value. Thus, for the reference code $$c=\texttt{r b c d y}$$, the profile in each half is

$$
R_c=\frac{(12-10,9-10,9-10)}{\sqrt{10}}=\frac{(2,-1,-1)}{\sqrt{10}}.
$$

This code favors “The” and disfavors the other two words. The profiles for all ten codes are:

| Code | Profile, multiplied by $$\sqrt{10}$$ |
|---|---|
| `r b c d y` | $$(2, -1, -1)$$ |
| `r f g h z` | $$(0, 0, 0)$$ |
| `r j k x y` | $$(0, 3, -3)$$ |
| `r l x d y` | $$(2, -1, -1)$$ |
| `r x c d y` | $$(2, -1, -1)$$ |
| `k f g h z` | $$(-2, 1, 1)$$ |
| `k l m n w` | $$(0, 0, 0)$$ |
| `k p q x z` | $$(0, -3, 3)$$ |
| `k r x h z` | $$(-2, 1, 1)$$ |
| `k x g h z` | $$(-2, 1, 1)$$ |

### Comparing two codes

To compare codes $$c$$ and $$d$$, we multiply their profile entries across halves and sum over words:

$$
G_{cd}=\frac12\sum_w\left(R^A_{cw}R^B_{dw}+R^B_{cw}R^A_{dw}\right).
$$

In this example the two halves have identical profiles, so this reduces to their dot product. The reference `r b c d y` and the variant `r l x d y` have the same profile, giving

$$
G_{cd}=\frac{2\times2+(-1)\times(-1)+(-1)\times(-1)}{10}=0.6.
$$

The variant `r j k x y` has profile $$(0,3,-3)/\sqrt{10}$$. Its similarity with the reference is $$[2\times0+(-1)\times3+(-1)\times(-3)]/10=0$$. The variant `r f g h z` has a zero profile, so its similarity with every code is zero.

### Averaging within families

We group distinct pairs within each family by their exact number of shared trailing letters. In family C, the pairs are:

| Shared letters $$m$$ | Pairs | Average similarity |
|---:|---|---:|
| 0 | `r f g h z` paired with each of the other four codes | 0 |
| 1 | `r j k x y` paired with the reference, `r l x d y`, or `r x c d y` | 0 |
| 2 | Reference with `r l x d y`, and `r l x d y` with `r x c d y` | 0.6 |
| 3 | Reference with `r x c d y` | 0.6 |

Family D gives the same four averages. Averaging equally across the two families therefore gives $$S_0=0$$, $$S_1=0$$, $$S_2=0.6$$, and $$S_3=0.6$$.

For calibration, we also compare each code with itself across halves. In each family, these five similarities are $$0.6,0,1.8,0.6,0.6$$. Their average is $$S_{\mathrm{same}}=3.6/5=0.72$$.

### Computing alignment

For each suffix length, we compute

$$
r_m=\frac{S_m-S_0}{S_{\mathrm{same}}-S_0}.
$$

This gives $$r_0=r_1=0$$ and $$r_2=r_3=0.6/0.72=5/6$$. The jump at two shared tokens suggests a two-token context.

### From this example to the Gemini experiment

In the cross-model experiment, we use 20 families of 11 codes, each 16 letters long. Each story samples one code from each family and provides up to 20 observations. We collect the stories once per model, then analyze shared suffix lengths 1, 2, 3, 4, 6, 8, and 12 using those same observations. The 12 most frequent opening words each get a category, and all other words go into one additional category. We average the calculation over random splits of the replies.
Check our [main post](/blog/probing-synthid-gemini-apis/#applying-our-method-to-all-gemini-models) for the full results.
