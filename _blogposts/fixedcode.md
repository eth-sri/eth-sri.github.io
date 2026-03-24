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

Coding agents are increasingly used to maintain software over long time horizons. A standard task in this setting is resolving user-reported issues: a bug report comes in, the agent investigates, writes a patch, and submits it. But what happens when the reported issue is already resolved?

This is not a contrived scenario. In any real codebase, agents will encounter outdated bug reports, issues fixed in a parallel PR, or tickets that reference behavior that was already patched. A good agent should recognize this, report that no fix is needed, and move on. We set out to measure whether current coding agents actually do this.



![Overview over the evaluation setup](/assets/blog/fixedcode/overview.svg){: .blogpost-img80}

{:.blogpost-caption}
We run the coding agents on the code base *after* the reported user issue has been resolved. The expected behavior is to not make additional changes to the code.

### Benchmark: Fixing already-fixed code

We sampled 100 instances from SWE-Bench Verified <a id="ref-source-swebench" href="#ref-swebench">[2]</a> and 135 samples from our AGENTbench dataset <a id="ref-source-agentsmd" href="#ref-agentsmd">[3]</a>, which consists of more niche and recent codebases. 
We evaluate a range of recent coding models in their recommended harnesses: [Claude Opus 4.6](https://www-cdn.anthropic.com/0dd865075ad3132672ee0ab40b05a53f14cf5288.pdf), [Claude Sonnet 4.6](https://www-cdn.anthropic.com/78073f739564e986ff3e28522761a7a0b4484f84.pdf), and [GLM-5](https://docs.z.ai/guides/llm/glm-5) in [Claude Code](https://www.anthropic.com/claude-code/); [GPT-5.4](https://openai.com/index/introducing-gpt-5-4/) and [GPT-5.4 mini](https://platform.openai.com/docs/models/gpt-5-mini) in [Codex](https://github.com/openai/codex); [Gemini 3 Pro](https://deepmind.google/models/gemini/pro/) in [Gemini CLI](https://github.com/google-gemini/gemini-cli), and the [Qwen3.5 family](https://qwen.ai/blog?id=qwen3.5) (35B, 122B, and 397B) in [Qwen Code](https://github.com/QwenLM/qwen-code).
Any meaningful code change (excluding documentation and tests) counts as a failure.


![Empty-patch success rate across models on fixed-code tasks](/assets/blog/fixedcode/score_postpatches_fix_by_model.svg){: .blogpost-img100}

{:.blogpost-caption}
No model scores significantly more than 50%. GLM-5 and the Claude models reach ~50%, while most others score below 30%.

### Agents introduce unnecessary changes

The results are sobering. Most models eagerly modify code even when there is nothing to fix. Interestingly, performance here does not align with coding capability as measured by SWE-bench, but rather with the models' tendency to push back against nonsensical requests as measured by BullShitBench <a id="ref-source-bullshitbench" href="#ref-bullshitbench">[4]</a>.
Manual trace analysis reveals the deciding factor: whether the agent attempts to reproduce the reported issue before fixing it. GLM-5 and the Claude models typically begin by trying to trigger the bug. Upon finding it already resolved, they usually correctly submit an empty patch. Most other models jump straight to patching without verification. Worse, since the issue was resolved in the most recent commit, even a quick look at the git history would reveal the fix. In all AGENTbench instances, the issue description even specifies the commit at which the bug was present. Yet most agents never check.

This is a problem beyond our benchmark. If deployed for autonomous maintenance, these agents would systematically introduce unnecessary changes to resolve stale issues, filling codebases with agent slop. Prior work <a href="#ref-haicode">[1]</a> has shown that agent-generated patches are typically overly verbose (unnecessarily defensive code, irrelevant edits, unrequested features), exacerbating this issue further. Our findings isolate this problem: even when the optimal patch is empty, most agents cannot help themselves.


### Prompting mostly fixes it — for now


![GPT-5.4 mini under different prompting variants](/assets/blog/fixedcode/score_postpatches_gpt-5.4-mini_variants.svg){: .blogpost-img50}


{:.blogpost-caption}
Upon explicitly telling the model to abstain if no change is needed, GPT-5.4 mini correctly abstains from submitting unnecessary code patches, increasing from 24% to 77% performance.


We investigated whether explicit instructions can address this. Using a prompt that tasks the agent to first investigate whether the issue still exists, then reproduce it, and only fix it if the reproduction succeeds, GPT-5.4 mini jumps from 24% to 77%. Meanwhile, simply asking to "reproduce before patching" (without the explicit option to abstain) only yields 30%. To confirm these framings don't hurt real bug-fixing capability, we ran the same prompts on standard SWE-bench and saw no performance degradation.
This indicates a good candidate instruction to add to context files <a href="#ref-agentsmd">[3]</a>.

But prompting is brittle across edge cases. We tested a scenario where a previous agent had already attempted a fix that was incorrect (using GPT-5.4 nano patches that fail SWE-bench). When asked to fix the reported issue or abstain if resolved, both Claude Sonnet 4.6 and GPT-5.4 mini now strongly favor abstaining, submitting 70% and 94% empty patches, respectively, even though the existing patch is wrong and a real fix is needed.

### The deeper problem

We should not need to prompt agents to check whether their work is necessary. The underlying issue is that current models lack taste in software engineering <a href="#ref-codetaste">[5]</a>: they overengineer, do not verify that changes are needed, and do not confirm that their patches actually change program behavior meaningfully. These edge cases, stale issues, partial prior fixes, and redundant changes are the norm in real-world software maintenance, not the exception.

There is a more general lesson here that extends beyond coding. LLMs, especially when used as agents, are trained to always find a way to "succeed" at the task they are given. If you ask a model to fix a bug, it will produce a fix, even if no fix is needed. The model has seen millions of bug-fixing trajectories during training and has been rewarded for producing patches, not for concluding that none are required. If you do not explicitly frame "no change needed" as a valid and successful outcome, the model will not choose it. This is why the fix-or-abstain prompt works so well: it redefines success to include the possibility of abstaining.

This dynamic applies broadly. Whenever an agent encounters unexpected circumstances, an already-resolved issue, a contradictory specification, or an ambiguous requirement, it will default to producing something rather than pushing back or asking for clarification. The practical takeaway for anyone deploying agents today: always define an explicit success path for unexpected circumstances. But long-term, if we want coding agents that can autonomously maintain software, they need to internalize the principle of minimal, verified changes. That requires changes to how models are trained, not just to how they are prompted.



### Conclusion

We set out to investigate in a controlled setting whether current coding agents ensure minimality of submitted patches by asking them to fix resolved issues in code bases. Overall, we found a sobering result: Most models unquestioningly perform patches, do not stop to confirm that they actually changed the program behavior meaningfully, and submit unnecessary changes in up to 70% of instances. Our stopgap recommendation is to explicitly ask models to abstain from fixing code that does not require changes. However, we suggest that this is a symptom of a broader, underlying issue in the reward design of coding agents, which prevents their use in long-term autonomous software maintenance.

{:.blogpost-caption}
This work was done in collaboration with [LogicStar](https://logicstar.ai). Check out their work on reliable coding agents! 


#### References

<div class="blogpost-references">
<span id="ref-haicode"><a href="#ref-source-haicode">[1]</a> Wang et. al., <a href="https://zorazrw.github.io/files/position-haicode.pdf"><i>Position: Humans are Missing from AI Coding Agent Research</i></a>, 2026</span>

<span id="ref-swebench"><a href="#ref-source-swebench">[2]</a> Jimenez et. al., <a href="https://arxiv.org/abs/2310.06770"><i>SWE-bench: Can Language Models Resolve Real-World GitHub Issues?</i></a>, ICLR 2024</span>

<span id="ref-agentsmd"><a href="#ref-source-agentsmd">[3]</a> Gloaguen et. al., <a href="/publications/gloaguen2026agentsmd"><i>Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?</i></a>, 2026</span>

<span id="ref-bullshitbench"><a href="#ref-source-bullshitbench">[4]</a> Gostev, <a href="https://petergpt.github.io/bullshit-benchmark/viewer/index.v2.html"><i>BullshitBench v2</i></a>, 2026</span>

<span id="ref-codetaste"><a href="#ref-source-codetaste">[5]</a> Thillen et. al., <a href="/publications/thillen2026codetaste"><i>CodeTaste: Can LLMs Generate Human-Level Code Refactorings?</i></a>, 2026</span>
</div>


#### Examples

We present a number of concrete agent traces that illustrate our findings below.
In the representative instance below, GPT-5.4 mini applies a patch to the repository before running any reproduction tests or checking the git history. It edits the PostgreSQL dbshell client immediately, only then runs the relevant test, and ends up submitting the unnecessary code change.
<details class="trace-details">
<summary class="trace-summary"><span class="trace-badges"><span class="trace-badge trace-badge-primary">Show</span><span class="trace-badge">GPT-5.4 mini</span><span class="trace-badge">django/django#11239</span></span></summary>
<a class="iframe-link" href="/assets/blog/fixedcode/django__django-11239-fix.traj.html">Open GPT-5.4 mini fix trace</a>
<iframe class="iframe-full" src="/assets/blog/fixedcode/django__django-11239-fix.traj.html" height="900px"></iframe>
</details>

There is even an easier path to discovering that no patch is required.
In all AGENTbench instances, the issue text explicitly describes the commit at which the reported issue was observed. In our evaluation, the most recent commit diverges from the reported commit and includes the patch to the reported issue. If the agents inspect the recent git history, they quickly realize that the last commit solves the task they were assigned. However the agents rarely stop to compare that commit with the current state of the repository.
The notable exceptions are GLM-5 and the Claude models: they usually begin their activity by attempting a reproduction of the reported issue and then continue to inspect the git history. The empty submitted patches follow their decision that no change is needed upon discovering the existing patch. Such an example is illustrated in the Sonnet 4.6 trace below.

<details class="trace-details">
<summary class="trace-summary"><span class="trace-badges"><span class="trace-badge trace-badge-primary">Show</span><span class="trace-badge">Sonnet 4.6</span><span class="trace-badge">opshin/opshin#387</span></span></summary>
<a class="iframe-link" href="/assets/blog/fixedcode/opshin_opshin-387.traj.html">Open Sonnet 4.6 trace</a>
<iframe class="iframe-full" src="/assets/blog/fixedcode/opshin_opshin-387.traj.html" height="900px"></iframe>
</details>

We consider this desirable behavior and not cheating. We were actually surprised to see so few models perform even this most basic check. However, reproducing bugs and inspecting the git history do not guarantee correct abstention.
Even when models first reproduce the issue at hand, they may proceed to ‘resolve’ a new issue. For example, in one instance,  GLM-5 discovers that the reported issue was fixed in a prior commit but continued nonetheless, hallucinating a bug in an unrelated piece of code and committing it without checking if it causes any changes.

<details class="trace-details">
<summary class="trace-summary"><span class="trace-badges"><span class="trace-badge trace-badge-primary">Show</span><span class="trace-badge">GLM-5</span><span class="trace-badge">openai/openai-agents-python#1779</span></span></summary>
<a class="iframe-link" href="/assets/blog/fixedcode/openai_openai-agents-python-1779.traj.html">Open GLM-5 trace</a>
<iframe class="iframe-full" src="/assets/blog/fixedcode/openai_openai-agents-python-1779.traj.html" height="900px"></iframe>
</details>

Upon explicitly telling the model to abstain if no change is needed, even GPT-5.4 mini correctly abstains from submitting unnecessary code patches. Its abstention rate rockets from 24% to 77%. Below we show the same instance as above, only with a small additional remark in the initial prompt. In this setting, GPT-5.4 mini reproduces the issue first and then leaves the repository unchanged.

<details class="trace-details">
<summary class="trace-summary"><span class="trace-badges"><span class="trace-badge trace-badge-primary">Show</span><span class="trace-badge">GPT-5.4 mini</span><span class="trace-badge">django/django#11239</span><span class="trace-badge trace-badge-accent">Abstain Variant</span></span></summary>
<a class="iframe-link" href="/assets/blog/fixedcode/django__django-11239-fix-or-abstain.traj.html">Open GPT-5.4 mini fix-or-abstain trace</a>
<iframe class="iframe-full" src="/assets/blog/fixedcode/django__django-11239-fix-or-abstain.traj.html" height="900px"></iframe>
</details>
