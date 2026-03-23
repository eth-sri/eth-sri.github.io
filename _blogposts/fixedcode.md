---
layout: blogpost
category: other
title: Coding Agents Are "Fixing" Correct Code
blogpost-authors: Niels Mündler, Thibaud Gloaguen, Mark Niklas Müller, Veselin Raychev, Martin Vechev
date: 2026-03-23
thumbnail: thumbnails/fixedcode.png
usemathjax: false
tldr: >
    Coding agents often change code that is already fixed instead of abstaining. This suggests current agents still lack good software engineering judgment.
excerpt: >
    Coding agents often modify code even when the reported issue has already been fixed. Our fixed-code benchmark shows that most current agents fail to abstain in this setting, submitting irrelevant patches in over 50% of cases. This reveals a broader weakness in software engineering judgment, in particular, the failure to confirm the minimality and relevance of code changes.
tweet-id: 1966482446276542757
---
<style>
    .blogpost-thumbnail {
        width: 30% !important;
    }
    @media (max-width: 768px) {
    /* styles that apply when viewport is 768px or smaller */
    .blogpost-title {
      font-size: 30px;
    }

    .blogpost-thumbnail {
        width: 60% !important;
    }

    .page-subtitle {
      font-size: 18px
    }

    .tldr {
      padding: 5% 5%;
    }

    .blogpost-col {
      text-align: left;
    }

  .blogpost-col p,
  .blogpost-col h3 {
      padding-left: 10px !important;
      padding-right: 10px !important;
    }
  }

  .trace-badges {
    display: inline-flex;
    flex-wrap: wrap;
    gap: 6px;
    align-items: center;
  }

  .trace-details > summary {
    list-style: none;
  }

  .trace-details > summary::-webkit-details-marker {
    display: none;
  }

  .trace-summary {
    display: inline-flex;
    align-items: center;
    width: 100%;
    cursor: pointer;
  }

  .trace-summary * {
    pointer-events: none;
  }

  .trace-details {
    display: inline-block;
    background: #dbdbdb;
    width: 100%;
  }

  .trace-badge {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 999px;
    background: #eef2f7;
    border: 1px solid #d8e0ea;
    color: #213547;
    font-size: 12px;
    font-weight: 600;
    line-height: 1.4;
    letter-spacing: 0.01em;
  }

  .trace-badge-primary {
    background: #213547;
    border-color: #213547;
    color: #ffffff;
  }

  .trace-badge-primary::before {
    content: "▸";
    margin-right: 6px;
    font-size: 11px;
  }

  .trace-details[open] .trace-badge-primary::before {
    content: "▾";
  }

  .trace-badge-accent {
    background: #f3e8d2;
    border-color: #e2c68e;
    color: #6b4e16;
  }
    
</style>

Coding agents are used to maintain codebases over long time horizons. This task requires them to generate high-quality and easy-to-maintain code. Yet, prior works have shown that agents tend to produce verbose code (e.g., being unnecessarily defensive, introducing irrelevant edits, and adding unrequested features) <a id="ref-source-haicode" href="#ref-haicode">[1]</a>. To measure the tendency of coding agents towards unnecessary changes cleanly, we design a problem in which the best patch is simple: it's empty.

Concretely, we ask the agent to solve real-world bugs on real-world codebases. The catch is that the bug has already been fixed. Thus, we know that no changes to the codebase are needed to solve the task. A good coding agent, that doesn’t introduce unnecessary changes, should realize that the reported bug has been resolved already, and do nothing. 

Such a situation can quickly arise in realistic setups, e.g., when agents are automatically processing outdated user-reported issues or are steered by developers who lack oversight of the complete code base. Ideally, in such a situation, the coding agent should gently push back or simply report that no fixing is required. We definitely do not want to see unwarranted and unnecessary changes to the program logic.


![Overview over the evaluation setup](/assets/blog/fixedcode/overview.svg){: .blogpost-img80}

{:.blogpost-caption}
We run the coding agents on the code base *after* the reported user issue has been resolved. The expected behavior is to not make additional changes to the code.

### Setting things up

To assess how well agents deal with this situation, we task them with resolving real-world GitHub issues in a repository where the pull request resolving that issue is already merged. We chose 100 randomly sampled instances from SWE-Bench Verified <a id="ref-source-swebench" href="#ref-swebench">[2]</a> and 135 samples from our AGENTbench dataset <a id="ref-source-agentsmd" href="#ref-agentsmd">[3]</a>, which consists of more niche and recent code bases. We then launch the agent in an execution environment, seeing the codebase after the issue has been resolved, and task the agent to resolve the (already resolved) issue. 

If the agent makes any meaningful changes to the code, we consider this a failure - the issue is resolved already, and there is nothing to fix. We exclude non-code changes like documentation and changes to tests.

We evaluate a variety of recent coding models in their respective recommended harnesses and report the findings below. Concretely, we evaluate [Claude Opus 4.6](https://www-cdn.anthropic.com/0dd865075ad3132672ee0ab40b05a53f14cf5288.pdf), [Claude Sonnet 4.6](https://www-cdn.anthropic.com/78073f739564e986ff3e28522761a7a0b4484f84.pdf), and [GLM-5](https://docs.z.ai/guides/llm/glm-5) in the [Claude Code](https://www.anthropic.com/claude-code/) harness, [GPT-5.4](https://openai.com/index/introducing-gpt-5-4/) and [GPT-5 mini](https://platform.openai.com/docs/models/gpt-5-mini) in [Codex](https://github.com/openai/codex), [Gemini 3 Pro](https://deepmind.google/models/gemini/pro/) in [Gemini CLI](https://github.com/google-gemini/gemini-cli), and the [Qwen3.5 family](https://qwen.ai/blog?id=qwen3.5), including 35B, 122B, and 397B, using the [Qwen Code](https://github.com/QwenLM/qwen-code) harness.

![Empty-patch success rate across models on fixed-code tasks](/assets/blog/fixedcode/score_postpatches_fix_by_model.svg){: .blogpost-img100}

{:.blogpost-caption}
**Main results.** Success rate on the fixed-code benchmark, where the correct patch is empty because the issue has already been resolved.




No model scores significantly more than 50% in our setting. GLM-5 and Claude Sonnet and Opus are significantly outperforming other models at around 50%, while most models score below 30%.

### Overeagerness for changes is common


We find that most models are extremely eager to modify the code and provide a patch for the user, even when there is no need for it: The highest score is only 50%, of GLM-5, with Claude Opus 4.6 and Sonnet 4.6 following closely at around 48%. The Qwen3.5 family, GPT 5.4 and GPT-5.4 mini, and Gemini 3 Pro all score below 30%. Rather than aligning with coding capability as measured in SWE-bench, the results align with the model's ability to critically examine and push back against nonsensical requests as in BullShitBench <a id="ref-source-bullshitbench" href="#ref-bullshitbench">[4]</a>. All of these numbers are concerningly low. 

### Models rarely stop to confirm whether issues still exist

We manually analyzed the model traces and observed an interesting pattern in the coding models. The deciding factor for whether a model submits an unnecessary patch is whether it attempts to reproduce the reported issue *before* applying a patch. We believe this behaviour is essential when resolving bugs in the real world: If the problem can not be reproduced in the original state, it can not be confirmed whether the underlying issue has been resolved. Alas, few models genuinely attempt such a reproduction.
For example, in the instance below, GPT-5.4-mini first navigates the repository, then applies a patch, and finally verifies that the newly considered test case patch. It fails to confirm the test case fails without its "fix".
<details class="trace-details">
<summary class="trace-summary"><span class="trace-badges"><span class="trace-badge trace-badge-primary">Show</span><span class="trace-badge">GPT-5.4-mini</span><span class="trace-badge">django/django#12774</span></span></summary>
<a class="iframe-link" href="/assets/blog/fixedcode/django__django-12774-fix.traj.html">Open GPT-5.4-mini fix trace</a>
<iframe class="iframe-full" src="/assets/blog/fixedcode/django__django-12774-fix.traj.html" height="900px"></iframe>
</details>

There is even an easier path to discovering that no patch is required.
In all AGENTbench instances, the issue text explicitly describes the commit at which the reported issue was observed. In our evaluation, the most recent commit diverges from the reported commit and includes the patch to the reported issue. If the agents inspect the recent git history, they should quickly realize that the last commit solves the task they were assigned. However the agents rarely stop to compare that commit with the current state of the repository.


The notable exceptions are GLM-5 and the Claude models: they usually begin their activity by attempting a reproduction of the reported issue and then continue to inspect the git history. The empty submitted patches follow their decision that no change is needed upon discovering the existing patch. Such an example is illustrated in the Sonnet 4.6 trace below.

<details class="trace-details">
<summary class="trace-summary"><span class="trace-badges"><span class="trace-badge trace-badge-primary">Show</span><span class="trace-badge">Sonnet 4.6</span><span class="trace-badge">opshin/opshin#387</span></span></summary>
<a class="iframe-link" href="/assets/blog/fixedcode/opshin_opshin-387.traj.html">Open Sonnet 4.6 trace</a>
<iframe class="iframe-full" src="/assets/blog/fixedcode/opshin_opshin-387.traj.html" height="900px"></iframe>
</details>

We consider this desirable behavior and not cheating. We were actually surprised to see so few models perform even this most basic check. However, reproducing bugs and inspecting the git history do not guarantee correct abstention.

Even when models first reproduce the issue at hand, they may proceed to ‘resolve’ a new issue. For example, in one instance,  GLM-5 discovers that the reported issue was fixed in a prior commit but continued nonetheless, hallucinating a bug in an unrelated piece of code and committing it without checking if it causes any changes. Similarly, in one case, Sonnet 4.6 realized that the issue was already fixed and that its proposed change was useless, but ended up keeping the changes anyway because the tests still passed with his change.

<details class="trace-details">
<summary class="trace-summary"><span class="trace-badges"><span class="trace-badge trace-badge-primary">Show</span><span class="trace-badge">GLM-5</span><span class="trace-badge">openai/openai-agents-python#1779</span></span></summary>
<a class="iframe-link" href="/assets/blog/fixedcode/openai_openai-agents-python-1779.traj.html">Open GLM-5 trace</a>
<iframe class="iframe-full" src="/assets/blog/fixedcode/openai_openai-agents-python-1779.traj.html" height="900px"></iframe>
</details>

### Correct prompting as a stopgap solution

Upon explicitly telling the model to abstain if no change is needed, even GPT-5.4-mini correctly abstains from submitting unnecessary code patches. Its abstention rate rockets from 24% to 77%. Below we show the same instance as above, only with a small additional remark in the initial prompt. In this setting, GPT-5.4-mini succeeds in reproducing the issue first and abstains from any meaningful code changes.

<details class="trace-details">
<summary class="trace-summary"><span class="trace-badges"><span class="trace-badge trace-badge-primary">Show</span><span class="trace-badge">GPT-5.4-mini</span><span class="trace-badge">django/django#12774</span><span class="trace-badge trace-badge-accent">Abstain Variant</span></span></summary>
<a class="iframe-link" href="/assets/blog/fixedcode/django__django-12774-fix-or-abstain.traj.html">Open GPT-5.4-mini fix-or-abstain trace</a>
<iframe class="iframe-full" src="/assets/blog/fixedcode/django__django-12774-fix-or-abstain.traj.html" height="900px"></iframe>
</details>


![GPT-5.4-mini under different prompting variants](/assets/blog/fixedcode/score_postpatches_gpt-5.4-mini_variants.svg){: .blogpost-img50}


{:.blogpost-caption}
**Prompting ablation.** Explicitly instructing GPT-5.4-mini to investigate whether the issue still exists, and asking it to abstain if this is the case, substantially improves abstention on fixed-code tasks.

<span id="footnote-source-1">Moreover, we test providing an abstain option and reproduction instructions in the standard SWE-Bench task of resolving an issue that has not yet been resolved. The result is that the model maintains the same accuracy of around 70%. This indicates that an explicit AGENTS.md <a href="#ref-agentsmd">[3]</a> or prompt can help mitigate overly eager patches. <sup><a href="#footnote-1">1</a></sup></span>

However, there are subtleties: If we only prompt the model to reproduce the issue before submitting the patch, without indicating that abstention is an option, the model abstains marginally more often than if not told to reproduce the issue, increasing from 24% to 30% abstention.
Moreover, this is not the only edge case a code agent might encounter.

A concrete realistic scenario is that another coding agent has attempted and applied a patch previously, but that patch does not work correctly. We run a small ablation to simulate this situation: We use GPT-5.4-nano to generate patches for the standard SWE-bench task. We then filter those patches to obtain 100 patches that do not correctly resolve the task at hand. Again, we ask Claude Sonnet 4.6 and GPT-5.4-mini to fix the reported user issue or abstain if it has been resolved. We find that both Claude Sonnet 4.6 and GPT-5.4-mini now strongly favor abstaining, submitting 70% and 94% empty patches, respectively. But in this scenario, the code behaves incorrectly, so the ideal model behavior would be to submit a non-empty patch.


The bottom line is that prompting is a stopgap, but not a long-term solution.
Ideally, handling such cases should not even require specific instructions.
Fully autonomous coding agents need good taste and rigourous verification when modifying code: They need to aim for minimal, clean and relevant code changes. As of now, the observations fit that agents are eager to fulfil user requests, but fail to exhibit a strong intuition about software maintainability <a id="ref-source-codetaste" href="#ref-codetaste">[5]</a>.


### Related Findings

Wang et. al. <a href="#ref-haicode">[1]</a> measure the lack of quality in the agent's code by comparing the length of the human and agent patch. Their findings align generally with our results, indicating that agent-generated patches are typically overly verbose, and we recommend reading their paper for further insights extracted from real submissions to the SWE-bench coding benchmark. However, their metric has its limitations, since (i) the human patch can be of low quality and overly verbose, and (ii) larger patches could be more elegant refactorings. In this blog post, we suggested a new, less noisy proxy metric to assess an agent's ability to generate quality code.

### Conclusion

We set out to investigate in a controlled setting whether current coding agents ensure minimality of submitted patches by asking them to fix resolved issues in code bases. Overall, we found a sobering result: Most models unquestioningly perform patches, do not stop to confirm that they actually changed the program behavior meaningfully, and submit unnecessary changes in up to 70% of instances. Our stopgap recommendation is to explicitly ask models to abstain from fixing code that does not require changes. However, we suggest that this is a symptom of a broader, underlying issue of coding agents, which prevents their use in long-term autonomous software maintenance: They lack taste in software engineering.


#### References

<div class="blogpost-references">
<span id="ref-haicode"><a href="#ref-source-haicode">[1]</a> Wang et. al., <a href="https://zorazrw.github.io/files/position-haicode.pdf"><i>Position: Humans are Missing from AI Coding Agent Research</i></a>, 2026</span>

<span id="ref-swebench"><a href="#ref-source-swebench">[2]</a> Jimenez et. al., <a href="https://arxiv.org/abs/2310.06770"><i>SWE-bench: Can Language Models Resolve Real-World GitHub Issues?</i></a>, ICLR 2024</span>

<span id="ref-agentsmd"><a href="#ref-source-agentsmd">[3]</a> Gloaguen et. al., <a href="/publications/gloaguen2026agentsmd"><i>Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?</i></a>, 2026</span>

<span id="ref-bullshitbench"><a href="#ref-source-bullshitbench">[4]</a> Gostev, <a href="https://petergpt.github.io/bullshit-benchmark/viewer/index.v2.html"><i>BullshitBench v2</i></a>, 2026</span>

<span id="ref-codetaste"><a href="#ref-source-codetaste">[5]</a> Thillen et. al., <a href="/publications/thillen2026codetaste"><i>CodeTaste: Can LLMs Generate Human-Level Code Refactorings?</i></a>, 2026</span>
</div>

#### Footnotes

<div class="blogpost-footnotes">
<span id="footnote-1"><a href="#footnote-source-1"><sup>1</sup></a> Note that the strong impact of prompting may introduce a skew in the evaluation results since different agent harnesses may use different system prompts. In any case, this would result in models performing better on our benchmark - but all models perform pretty poorly.</span>
</div>
