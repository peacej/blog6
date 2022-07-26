---
title: How To Be An Awesome Data Scientist
date: 2019-02-16
category: Working as a data scientist
tags: data science,communication,teamwork
---



·7 min read


The world is teeming with people who have the “data scientist” title but somehow don’t live up to expectations. This problem might be related to the use of the term “fake data scientist,” although I don’t think we should be snobby about academic qualifications etc.

Here is my humble opinion on **how to be an awesome data scientist, regardless of your background**:

1.  Always be learning useful things efficiently
2.  Proactively challenge yourself
3.  Focus on impact early on
4.  Have pride in both technical skills and business understanding
5.  Communication: think hard about how to convey insights and ideas

Tip #1: Always be learning useful things efficiently
====================================================

The world of data science is progressing quickly.. you’ll fall behind quickly if you stop learning.

Note how I **didn’t** simply say “always be learning.” That is not enough. I believe that most people, when learning, spend most of their time non-optimally. An extreme example of this is trying to learn English by reading a dictionary from cover to cover (I actually met someone who had been doing this for years and was strangely proud of knowing all words that start with “A” …)

*   **Learn useful things.** Considering a new programming language? a new library for creating charts? A new machine learning framework? Before starting, carefully estimate the long-term usefulness of acquiring the skill. For example, popularity is one thing to consider. You can guess that Tensorflow will be a useful skill to have even just by checking simple metrics such as the trend of Github repo stars and Google searches for “Tensorflow.” You can also look at [surveys of programmers](https://www.jetbrains.com/research/python-developers-survey-2018/) / data scientists, [find or ask questions on Quora](https://www.quora.com/What-are-the-skills-required-to-become-a-Data-Scientist), etc.
*   **Learn things efficiently.** Think of 100 students sitting in a classroom. The lecture may be too easy / slow for 70 of the students, too difficult / fast for 25 of the students, and just right for 5 of the students. You can customize the learning difficulty and speed/frequency in a way that’s optimal for yourself. (E.g. watch MOOC lecture videos at 1.5x speed, skip through materials in books that you already know, etc.) When learning, you should constantly feel slightly/somewhat challenged and forced to think, but not overwhelmed. Also, refer to study hacks for efficiency such as [spaced repetition](https://medium.freecodecamp.org/why-i-studied-full-time-for-8-months-for-a-google-interview-cc662ce9bb13/#f8bf).

Of course, sometimes it’s fun to learn something obscure or useless… just because it’s interesting. That’s great for having a fun life. But this article is about being an awesome data scientist :)

Tip #2: Proactively challenge yourself
======================================

This actually overlaps with tip #1, but it’s important to emphasize.

It’s easy to fall into a cycle of doing similar things over and over at work — things which feel less and less challenging.

no challenge → no growth

Building a bar chart of revenue for the 50th time? Determining statistical significance of an A/B test of button colors yet again? If you go through a full week in which everything you did was “been there, done that”… **you need to change something**. There are many ways you can do so:

*   **Try a different (hopefully better) way of doing things**. Can you automate more of your work or produce a better result? Instead of typing the same date filter repeatedly in 4 subqueries of your SQL query, why not instead develop a way to templatize the SQL query so that you only have to type the date once? Instead of static image charts, can you generate interactive charts using a different R/Python library? Of course, you should probably refrain from things that are overkill (e.g. using a deep neural network when simple logistic regression already works very well).
*   **Ask or volunteer for more or different responsibilities**. This could be a project that is ideated and proposed by you. For example, you could ask to work on a different product area, or you could volunteer to create an automated A/B test analysis tool. You could even volunteer to give a tech talk to practice your public speaking skills, even if your company doesn’t have a culture of holding tech talks. You could also ask your colleagues/boss for ideas.
*   **Change teams (or even companies)**. Hey, no hard feelings. If you’re not able to find enough challenges in your current team despite trying hard to do so, it’s time to move on. There are tons of interesting opportunities out there. You can still keep in touch with your former teammates and grab a drink with them occasionally.

Tip #3: Focus on impact early on
================================

It’s common for great work to be done but not have an **impact**. This can lead to demotivation and lack of promotions. Some typical scenarios:

*   You showed in a Jupyter notebook that you can develop a model to predict user churn with high accuracy; however, the model was never deployed to production
*   Some dude asks you to pull some data. You pull the data. The dude says “ah, interesting...” End of story.
*   You estimated that an additional 50,000 users could be acquired with no extra budget if the marketing team changes how they allocate TV ad budget to time slots. The ultimate decision maker says the allocation has “already been finalized.”
*   If a tree falls in the forest and no one is around to hear it, does it make a sound? If you created a dashboard and no one looks at it….

To prevent situations like the above, before you commit to doing any major piece of work, ask yourself:

*   What **ultimate impact on the company** do you expect from doing this piece of work? Is the impact-to-work ratio higher than other potential tasks?
*   What are the **mechanisms/requirements** for enabling the impact? Often this involves checking for **actionability**, i.e. if a human needs to take action to enable the impact, get that human’s agreement before you start the work. I.e. ask them “if my analysis indicates X, then based on that, will you probably do Y?”

Tip #4: Have pride in both technical skills and business understanding
======================================================================

I think almost all data scientists understand that technical skills are important: programming, statistics, cloud computing, etc. But sometimes I feel there is not enough appreciation for **deeply understanding the product or business** for which data science is being applied**.** Things like:

*   What is the strategic positioning of your product on your market vs. competitors?
*   What is the thought process of customers (who are humans, not just `user_id`s) when they decide to spend money on your product?
*   How does the overall ecosystem work? For example, if your product is an online news aggregator, how do advertisers, publishers, tech platforms, and users depend on and affect each other? How do the power dynamics work? For a good example of someone who really understands tech ecosystems, see [Ben Evan’s newsletter](https://www.ben-evans.com/archive).

It’s easy to get bogged down just looking at data, which are in a way abstractions of your customers, partners, etc. But to really have a big impact, you often have to tie the data to the real world in the right way. That’s hard to do, but it’s much easier if you have the right understanding.

I’ve seen many resumes that are just a laundry list of data science techniques and tools which have almost no mention of the product/business implications of their work. This tells me the person doesn’t fully appreciate such implications.

Tip #5: Communication: think hard about how to convey insights and ideas
========================================================================

I considered simply writing “communicate better,” but that’s a no-brainer. Who wouldn’t want to be a better communicator? Communication is a natural challenge for many people, but I think huge improvement can be made by simply **taking a bit of time to think** about it.

If you’re not sure where to start, you can start with improving your written communication — which is easier since you have more time to think — and then move on to improving verbal communication. Data scientists’ communication includes [not only words but also charts and diagrams](http://www.storytellingwithdata.com/).

Many people don’t really **reflect** much on their own communication. They don’t stop to think before they type a message on Slack or take another look aftering posting the message to make sure it conveys their point clearly.

lack of reflection → lack of improvement

Improving communication could be as simple as asking yourself a checklist of questions such as this:

*   Did you write things in a logical order? You could write things in order of importance or in chronological order.
*   Who are the intended audiences? Is your message / e-mail / blog post customized for such audiences? Will the audience understand the main point you’re trying to make within 10 seconds of starting to read? (this is especially important if your audience is busy executives)
*   Are you using too much technical jargon or acronyms which some people might not understand?
*   Is your message ambiguous? This is especially a common problem when talking about metrics. Is it insufficient to simply say “revenue” if there are multiple definitions of revenue? If you made a chart, is it easy to interpret and get the key takeaway from it?
*   Should you highlight or **put in bold** especially important points? (especially useful if there’s a lot of text)
*   Instead of a wall of text, should you use a diagram to summarize the situation?

You can also proactively ask others for feedback on your communication. I’d also like to welcome you to give feedback to me on this Medium post :)

After you get better at communication via deliberate thinking, it’ll become more natural and automatic for you.

Up next
=======

\[Update 2019 Mar 19\] I wrote a post called “[How to be an awesome data science manager](https://medium.com/@peacej2/how-to-be-an-awesome-data-science-manager-1c63b059a03c).”