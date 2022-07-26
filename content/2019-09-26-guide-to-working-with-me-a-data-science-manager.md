---
title: Guide To Working With Me A Data Science Manager
date: 2019-09-26
category: Working as a data scientist
tags: data science,communication,teamwork
---



·9 min read

This document is mainly for sharing with my colleagues and anyone I might work with in the future. But hey, I might as well post it on Medium; maybe someone will find it useful. 

**Below are principles, values, and best practices I tell myself to follow** (both for working at organizations and working in data science). You don’t need to believe all the same principles, but **if you read them you’ll understand how I think, and that may help us cooperate effectively.** I’ll try to understand how you think too, and we can work out our differences :)

Principles / best practices for work
====================================

*   **Almost nothing is absolute** (including all the below principles). When applying any belief or principle, one should consider exceptions and/or consider moderation/balance.
*   **Always be open to change.** The world and situations change quickly, and so people should change too. That could include changing my below principles.
*   **Focus and prioritize**. If one is working on 5 major projects at the same time, that’s probably too many to be very effective. Clear **deprioritization** is a necessary part of good prioritization. In some cases, consider implementing ruthless prioritization (say no — politely, of course — to important projects/people because you have even more important work).
*   **Be a driving force.** Drive projects and tasks forward and achieve progress in the face of uncertainty/ambiguity. Related concepts are leadership, proactiveness, and taking ownership. But be careful of fatigue or spreading yourself too thin while driving many projects (hence the need for focus).
*   **Be free.** We are all adults. We should be able to live and work the way we want to. This includes our work hours, the technical tools or Python/R libraries we want to use, etc. However, someone else should step in when someone is abusing their freedom and not producing good work as a result. Also, there are some cases where limiting freedom (by establishing a standardized, scalable approach) can lead to greater organizational effectiveness, so there’s a tradeoff to consider. But in general, I like to err towards the side of more freedom and creating soft guidelines instead of hard rules.
*   **Be open and transparent** (except if it could cause major issues… e.g. legal issues)
*   **Be open-minded.** Most  people tend to become less accepting of conflicting approaches/ideas as they gain experience/expertise (and many are not self-aware that they’ve become less open-minded). Don’t let this happen to you.
*   **Keep people motivated,** including yourself and the people working with you. If people are not motivated, they probably won’t do good work or they’ll eventually leave the team or company. Take time to think about what motivates you and others (including career goals), and push for change if there’s a motivation problem. There are many reasons for low motivation; you should try to do something about it ASAP if possible.
*   **Don’t micromanage. Err on the side of over-empowering others.** It’s tricky to decide how much responsibility/authority/independence to **delegate** to someone. **The best leaders delegate well**. I think in most cases it’s better to give too much than too little; empowering people leads to higher motivation, faster work progress, faster personal growth, better long-term results, better team dynamics, and warm fuzzy feelings. Most mistakes can be fixed/dealt with. Of course there are exceptions (don’t let the new intern perform heart surgery all by herself) and it depends somewhat on each individual’s preferences. My thinking is influenced by the [culture of my previous employer, Supercell](https://www.nbforum.com/nbreport/ilkka-paananen-the-least-powerful-ceo/).
*   [**Celebrate failure**](http://schoolofherring.com/2015/07/19/ilkka-paananen-of-supercell-celebrate-learnings-from-failures/). It helps encourage continued risk-taking. But don’t [fetishize failure](https://www.entrepreneur.com/article/247933).
*   **Don’t only focus on the short term**. Sure, there might be quarterly goals, and those are important, but most great accomplishments in human history took more than a quarter to achieve. Consider blocking time each week for a longer-term goal.

Principles for good communication
=================================

Most communication / interpersonal problems could be avoided if everyone did just the first two below things well.

*   **Stand in the shoes of your audience.** Before hitting “send” on the e-mail, stop for a minute and think: is everything easily understandable (with sufficient context, explanation of terms, summarization of key points, etc.) for the reader given their limited knowledge? Is it clear to the reader what the next step s/he should take as a result of the e-mail? How would the reader feel after reading? This doesn’t just apply to e-mails or Slack messages. E.g. naming your dashboard is also a form of communication.
*   **Manage expectations.** All the time, people end up being disappointed/frustrated or lose trust due to misaligned expectations. Most of this is preventable. Ask yourself regularly: are expectations aligned? E.g. is there a difference between your understanding of the expected timing/quality/importance/amount of your work output and a stakeholder’s understanding? If the result will be highly uncertain (as is the case for e.g. using a new machine learning model for the first time), take extra care to ensure people understand that uncertainty and don’t have unfairly high expectations. This is not just about making people happy; it often hurts a team’s effectiveness if someone is deciding a course of action based on unrealistic expectations of a colleague’s work.
*   **Err on the side of over-communication.** If you’re not sure if something is worth saying/communicating, it’s better to say it just in case. The potential damage from under-communication (loss of trust, major bug, etc.) is typically far greater.
*   **Proactively give both positive and negative (critical) feedback.** No one is perfect, no one is completely self-aware, and no one can optimize their work perfectly just by themselves. The most effective teams have members that help each other become better team members over time.  
    **Giving critical feedback:** keep the message clear (don’t overly sugar-coat it) while not sounding like an asshole. Provide justification and explanation about how to improve (e.g. don’t just say “your presentation sucked”).  
    **Receiving critical feedback:** some people suck at giving feedback. Try not to take it personally and try to turn it into something helpful. Try to give feedback on how they can give you feedback more effectively. Be very welcoming of any critical feedback and proactively invite people to give it to you.

Principles / best practices for data science and technical work
===============================================================

*   **Good technical work usually requires good communication.** Some people see coding etc. as a hard skill and communication as a soft skill, and some people pride themselves mainly on their hard skills. But if your code is hard to read or if your technical work is hard to follow/understand, I don’t consider that good work, especially in the context of an organization. Making your work reasonably easy to read/understand requires good communication skills.
*   **Think carefully about the tradeoff between work speed and technical debt.** Sometimes it makes sense to just make a quick and dirty hacky prototype, sometimes it doesn’t. Adjust based on the situation (e.g. ask yourself questions like: will this eventually be used in production? How many people will be reading/using this code, for what purpose?)
*   **Identify and make the obviously good tradeoffs first.** For example, take the time to design well the folder/file structure and naming conventions for a big project. This might only take 1% of the total project time and reduce the technical debt burden by 20%. It’s surprising how many people fail to make such tradeoffs. Reflect regularly about if you’re making the right tradeoffs. Get feedback from others about it.
*   **“**[**Premature optimization is the root of all evil**](https://en.wikiquote.org/wiki/Donald_Knuth)**.”** True… and insufficient or overly late optimization is bad as well. One needs to think about when and how much optimization is appropriate. E.g. one rule of thumb is the [Rule of Three](https://en.wikipedia.org/wiki/Rule_of_three_(computer_programming)).
*   **Work should be reproducible and understandable.** If you did a piece of analysis or created an ML model, someone else with sufficient technical chops should be able to come and reproduce what you did with little to no guidance from you. Otherwise, 2 problems will get worse: technical debt and over-dependency on specific individuals.
*   **Almost all code should be pushed to git** (or another code version control system). There are tons of benefits: reproducibility, accountability, reversibility, searchability, education of team members, etc. Exceptions might be very short, temporary scripts. If it’s too troublesome for you to push your code to git, you need to set things up so that it’s easier to do so (e.g. bash script to reduce the amount of typing when pushing to git, set up auto-sync from your Jupyter server to git, etc.)
*   **Have a culture of knowledge sharing,** especially on technical topics. Internal/external blog posts, tech talks, tutorials, recommendations for tools to use, etc.
*   **Appreciate the balance between data-driven and non-data-driven methods.** Sometimes, companies just have to take a risk and act on gut feel . Otherwise, certain risky/innovative things will never be attempted. Often, human decision-making is a combination of data and gut feel or qualitative info, and some of the best software is a combination of ML (based on training data) and rule-based heuristics (based on human expertise).
*   **Stand on the shoulders of giants**. No need to develop something from scratch when you can reuse something off of github.
*   **Set up your technical environment to for efficient work**. Sometimes I can find the exact line of code I’m looking for in 5 seconds. Set up [Chrome search aliases](https://winaero.com/blog/add-custom-chrome-searches-for-address-bar-to-save-your-time/) for github, google docs, or whatever else you use commonly. Allow efficient use of your command line using bash aliases, [oh-my-zsh](https://ohmyz.sh/), etc. Enable [code-folding in Jupyter](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/codefolding/readme.html).
*   **Block off a bit of time for innovative, cutting-edge (and hopefully fun) data science experimentation.** For example, check out a new paper or new Python library and see how it can be applied to problems you’re trying to solve. A common problem in organizations is that, due to time constraints and short-term goals, people are stuck with using the same old approaches/tools repeatedly (which they can implement quickly with relatively high certainty about the results). Data science / ML is a rapidly progressing field, and you will eventually be left behind or get bored if you don’t take time to try new things.

Jerry’s personality and quirks
==============================

*   Once I took a personality test and the automatically generated test result was that I’m a **“**bull in a china shop”. I hope it’s an overstatement..
*   **I speak my mind**, sometimes bluntly. If I think something should be changed for the greater good, I may bang the table (figuratively) and argue aggressively about why it should be changed, regardless of the seniority of the people involved. Feel free to tell me to shut up (but please justify why you think I should). I think over time I’ve become more diplomatic, but this is still part of my fundamental personality.
*   **I have grit**. I can deal with huge setbacks/failures, huge problems, huge challenges, etc. But I won’t sacrifice my health dealing with such problems (I did before and it’s not worth it).
*   I have little tolerance for bullshit. Sometimes I’ll fight it patiently if I have to. (Of course, one should take care to not prematurely conclude that something is bullshit.)
*   I don’t get embarrassed easily. Some might describe this as [being shameless](https://www.youtube.com/watch?v=8PxEFti645A).
*   I’m addicted to self-improvement and learning. Let me know if you have tips :) I still have a long way to go.
*   I try to think more about how to do things for the mid/long-term benefit of the organization/ecosystem, not the short-term benefit of any given individual or team. If I’m not doing this, please let me know.
*   I like **sharing news articles, reports**, papers, github repos, etc. that I think might be helpful or interesting. Let me know if it’s too much or too distracting. Don’t let it hurt your ability to focus.
*   I’m a big fan of **Finnish values** (having worked in Finland for a year). Many Finnish people are humble, blunt, straightforward, concise, and have grit.
*   I’m like the **grammar police**. I will point out people’s incorrect grammar/spelling/wording, (in any language that I speak). I do it to help people improve themselves and to facilitate better communication. But if this becomes too annoying, please let me know.

Logistical stuff
================

*   Go ahead and put things in my calendar or reschedule stuff as needed. No need to ask me in advance. My calendar is up to date.
*   I may block off a chunk of “focused work time” on my calendar if I feel like I’m being distracted too much.
*   Feel free to grab extra time with me if the regular 1-on-1 or team meeting is insufficient.
*   Weekly team meetings — I think people should speak up only if one has something to say that others should hear; no need to feel pressured to always give an update on your work. Also, I usually don’t like overly structuring meetings with inflexible agendas, but we can add more structure if needed.
*   Feel free to slack/e-mail me at any time on any day. However, I may stop checking slack/e-mail when trying to disconnect from work (on weekends etc.) in which case the best way to reach me for an emergency is via phone or Facebook Messenger.

Relevant posts by me
====================

*   [How to be an awesome data science manager](https://medium.com/@peacej2/how-to-be-an-awesome-data-science-manager-1c63b059a03c)
*   [How to be an awesome data scientist](https://medium.com/@peacej2/how-to-be-an-awesome-data-scientist-930f04760f7e)

This guide was partially inspired by the [Guide to Working with Claire](http://growth.eladgil.com/book/the-role-of-the-ceo/insights-working-with-claire/).

![todo add alt text](https://miro.medium.com/max/2000/0*H13cLJi5Z5CThoew.jpg)Typical picture of me working with a colleague