---
layout: blogpost
category: talk
title: "The Role of Red Teaming in PETs"
blogpost-authors: "Jasper Dekoninck, Dimitar I. Dimitrov" 
date: 2023-05-19
thumbnail: thumbnails/fedcomp.png
usemathjax: false
tldr: >
    In February, our team won the Red Teaming category of the U.S. PETs Prize Challenge, securing a prize of 60,000 USD. In this blog post, we will provide a brief overview of the significance of Red Teaming in the field of Privacy Enhancing Technologies (PETs) research in the context of the competition. By outlining our methodology and highlighting the comprehensive objectives of a red team, we intend to showcase the essential role of Red Teaming in ensuring the development of robust and privacy-centric implementations grounded in solid theoretical foundations. We empahsize that we managed to significantly compromise all the systems we evaluated, demonstrating that even when solutions are deemed good enough to progress to the final phase of a prestigious PETs challenge, issues can still arise and persist.
excerpt: >
    In February, our team won the Red Teaming category of the U.S. PETs Prize Challenge, securing a prize of 60,000 USD. In this blog post, we will provide a brief overview of the significance of Red Teaming in the field of Privacy Enhancing Technologies (PETs) research in the context of the competition.
tweet-id:
---

In February, our team won the Red Teaming category of the U.S. PETs Prize Challenge, securing a prize of 60,000 USD. In this blog post, we will provide a brief overview of the significance of Red Teaming in the field of Privacy Enhancing Technologies (PETs) research in the context of the competition. By outlining our methodology and highlighting the comprehensive objectives of a red team, we intend to showcase the essential role of Red Teaming in ensuring the development of robust and privacy-centric implementations grounded in solid theoretical foundations. Please note that due to a non-disclosure agreement (NDA), we can only discuss our general approach and are unable to delve into specific details.

![Overview of Our Solution](/assets/blog/fedcomp/fedcomp_overview.png){: .blogpost-img100}

### The Challenge
The U.S. PETs Prize Challenge is a contest aimed at discovering innovative solutions to two critical issues where privacy plays a crucial role.

The first challenge, Financial Crime Prevention, focuses on enhancing collaboration between banks and SWIFT in detecting fraudulent transactions without disclosing private information among the parties involved. The proposed solutions encompass a range of advanced and highly tailored cryptographic protocols designed to jointly flag fraudulent transactions by the participants.

The second challenge, Pandemic Response, seeks to improve the prediction of infection probabilities for individuals, a highly relevant issue that raises numerous privacy concerns when data needs to be shared across governments or jurisdictions. The solutions presented in this challenge employ a wide array of techniques, ranging from slightly modified standard federated learning setups to highly tailored probabilistic models for pandemic forecasting.



### Red Teaming In The Challenge
As a Red Team, we were tasked with evaluating various solutions from each track within a limited timeframe. To effectively analyze and attack all of them, we adopted a multi-step plan illustrated in Figure 1.

First, we dedicated a substantial amount of time to understanding each task and solution individually, extracting several key pieces of information relevant to Red Teaming.
In particular, we investigated the privacy and utility requirements of the tasks and the data supplied, as well as the parties involved and their interactions. Further, we examined the privacy assumptions and claims of the proposed solutions in detail, as well as their proposed theoretical and software techniques. Although some aspects are closely linked to privacy, it's worth noting that we did not solely concentrate on that aspect of these components. We believe that Red Teams should adopt a more comprehensive perspective on the entire problem since all solution components are vital to the end-to-end process. Moreover, several submission issues, even when not directly related to privacy, can emerge naturally during a thorough analysis of the solution and may give rise to additional privacy concerns.

Secondly, we leveraged the gained in-depth understanding of the tasks and solutions to identify potential attack vectors. These are issues discovered within the given solution that could potentially lead to privacy concerns or related problems. It is worth noting that some of these attack vectors should also be incorporated as part of a proper "standard" evaluation of a given solution, and we consider them a critical subcomponent of an effective Red Teaming report. We provide several examples of attack vectors in Figure 1, but it is important to note that most of these stem from discrepancies between the components identified in step 1 and/or an unsoundness in one of them. In fact, we were surprised to find how many solutions were already flawed due to misunderstandings regarding the precise requirements or the interactions between parties.

In Step 3, we start the process of attacking the given solutions, identifying four primary categories of uncovered issues that should be included in a Red Team report. Privacy breaches are the most critical set of issues but not the sole focus of our Red Teaming Report. We argue that a comprehensive analysis of the Privacy-Utility Trade-Off is equally vital to include in a report, as trivially private solutions are easily obtainable if utility is not required. Indeed, some of our reports were centered on this trade-off, as we demonstrated that while the implemented solutions were (relatively) secure, they either behaved so similarly to random models that this was anticipated, or that simplifications of the proposed mechanisms resulted in a superior privacy-utility trade-off. In addition to these essential components, we also incorporate the conceptual and theoretical flaws identified in the second step even when they didn’t directly lead to privacy attacks. We observed that addressing these flaws could either enhance the performance of the given solution or could lead to undesirable consequences for privacy.

Finally, we consolidate all uncovered issues into a single report including recommendations to correct the vulnerabilities discovered in the solution. This report should be precise and provide actionable suggestions for implementing patches to address the identified issues, or in cases where the privacy issue is inherent to the solution, recommend against using the system altogether in practice. It is also crucial to acknowledge when a solution is simply effective: the primary objective of a Red Team should not be to dismantle a system, but rather to rigorously evaluate it under stressful conditions and pinpoint problems. If breaking the system becomes the sole focus of the Red Team, we encounter the same issue as to why Blue Teams cannot conduct this analysis independently: this bias in the report skews the results, with less regard for the origins of the numbers presented.

### Value of Red Teaming
The above explanation should offer a clear understanding of why Red Teaming for PETs is crucial, but we would like to emphasize this point further. A Red Teaming report provides a comprehensive evaluation of the solution across various dimensions, with privacy being the primary focus. A Red Team can objectively assess the solution's performance, which might be more challenging for Blue Teams who directly benefit from a successful solution. Moreover, the complexity of a Red Team's task is often inherently more difficult than that of the Blue Team due to the interactions between all the critical components identified earlier. Finally, it is worth noting that we managed to significantly compromise all the systems we evaluated, demonstrating that even when solutions are deemed good enough to progress to the final phase of a prestigious PETs challenge, issues can still arise and persist.

