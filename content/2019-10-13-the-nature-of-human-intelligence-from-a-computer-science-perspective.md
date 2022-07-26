title: The Nature Of Human Intelligence From A Computer Science Perspective
date: 2019-10-13
category: computer science
tags: computer science,human intelligence

9 min read


I’m tremendously curious about the long-term future of artificial intelligence. Understanding human intelligence better may be key to predicting the future of artificial intelligence. Thanks to both old books and recent research, my thinking and predictions have evolved quite a bit in the last few years. I now believe that Strong AI will be realized.

Regarding human intelligence, I now believe that the following statements are probably true. Some of this is just speculation. (For brevity, I’ll omit the words “probably” and “in my opinion” for the rest of the article.)

*   All or almost all of human intelligence can be deemed to be some form of computation or data input/output/storage.
*   Human intelligence doesn’t just come from the brain. Actually, almost every part of the human body (and even bacteria etc.) plays a role in human intelligence.
*   The whole is much greater than the sum of its parts. E.g. each cell has limited intelligence by itself, but together, great intelligence can be achieved.
*   **Parallel** computation at multiple levels is key and the parallelism is in a way even more impressive than a data center full of GPUs.
*   Computation is **distributed** and **decentralized** (like blockchains 😜); there is no centralized component. There is no human analogue of a CPU controlling a whole computer or master node controlling a cluster of computers.
*   **Recursion / feedback** **loops / self-improvement** are also important at multiple levels
*   **Attention** and **abstraction** mechanisms greatly decrease the amount of computation required (i.e. they improve the bang for the buck for each unit of computation)
*   There are many ways that parts of the human brain/body execute computer science algorithms or mathematical operations
*   Human intelligence makes use of both machine learning algorithms and logical reasoning ([symbolic computation](https://en.wikipedia.org/wiki/Computer_algebra) etc.)
*   Human intelligence would be very difficult to achieve using current computer hardware architecture; there must be a better approach. The human body/brain takes advantage of biology, chemistry, and physics in a way that normal computers can’t (yet).

Let’s dig into each of these points in more detail.

Intelligence is just computation and data input/output/storage
--------------------------------------------------------------

In other words, I believe in [**functionalism**](https://en.wikipedia.org/wiki/Functionalism_(philosophy_of_mind)). I think rejecting functionalism would mean that you’d need to believe in some concept of a soul or some other non-tangible/non-physical phenomena (which you’d never be able to verify). This relates to the nature of human consciousness. For a nice overview, see [_Are We Explaining Consciousness yet? (2001 paper by Daniel Dennett)_](http://omgwai.com/itsdho/Dennett_2001.pdf).

Intelligence doesn’t just come from the brain
---------------------------------------------

I used to think that all intelligence comes from the brain, but now I think that is wrong. Let’s consider a thought experiment: if we were able to surgically remove my brain and place it into a robot’s body, would I think/behave/feel the same way? No, I don’t think so (unless we have advanced technology that can synthesize robots that function exactly like human bodies).

In other words, our bodies are part of our intelligence. For example, recent research shows that [the gut and its microbiome has significant affects on the brain and human behavior.](http://The whole is much greater than the sum of its parts.) A finger touching a hot surface will instantly retract before any electric signal reaches the brain. White blood cells wage war against invaders without instructions from the brain. Cells move around, release chemicals, and replicate following something like a computer program (DNA). It doesn’t matter if cells are unconscious; they contribute to the overall intelligence of the human. Also, did you know that [a single cell can solve mazes and difficult computer science problems](https://www.youtube.com/watch?v=ooA0J6DWWTM&t=13m19s)?

Humans don’t just gain intelligence by reading books or listening to lectures. Feeling the world through all senses and sensations (consciously and unconsciously) helps a human understand the world and act intelligently in that world.

The whole is much greater than the sum of its parts
---------------------------------------------------

One human is simply the “animal” level of the [**Emergence Tower**](https://waitbutwhy.com/2019/10/idea-labs-echo-chambers.html), where each level is constituted by combining several instances of the level below it.

![todo add alt text](https://miro.medium.com/max/20000/1*kJXRYzvsw55xVqAgz7T87w.png)from [https://waitbutwhy.com/2019/10/idea-labs-echo-chambers.html](https://waitbutwhy.com/2019/10/idea-labs-echo-chambers.html)

An interesting analogy is how an ant colony is collectively much more intelligent than the sum of each constituent ant’s intelligence; this is perhaps [described most entertainingly in the famous book _G_](https://qr.ae/TWYnOU)ö[_del, Escher, and Bach_](https://qr.ae/TWYnOU).

Related concepts are the [**wisdom of crowds**](https://en.wikipedia.org/wiki/The_Wisdom_of_Crowds) and computer science concepts such as **evolutionary algorithms**,  [**computational social choice**](https://www.lamsade.dauphine.fr/~lang/papers/sofsem07.pdf), **graph computing**, and **neural networks** (where [multiple neural networks combined](https://medium.com/intuitionmachine/the-end-of-monolithic-deep-learning-86937c86bc1f) can be more “intelligent” or useful than the simple sum of each constituent network’s intelligence, and one network can be deemed more intelligent than the sum of each constituent layer’s intelligence).

Parallel computing
------------------

If we assume most of the [cells in the human body can each be deemed to have some sort of computational capacity](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3842595/) (a single cell might be dumb and slow by itself, but that’s besides the point), then that implies one human can make 10s of trillions of computations simultaneously (in **parallel**). Compare that with traditional computers:

*   A traditional CPU can only process one thing at a time.
*   A multithreading CPU might be able to handle 64 simultaneous computations.
*   A decent GPU might be able to handle [tens of thousands of simultaneous computations](https://stackoverflow.com/questions/6490572/cuda-how-many-concurrent-threads-in-total).
*   A data warehouse full of GPUs might be able to handle 100 million simultaneous computations.

Parallel computing is key because it allows humans to e.g. react to things very quickly. E.g. if you saw an object flying towards your head, you would immediately try to dodge, not process each retina cell’s data one by one before acting. Of course, humans can’t apply efficient parallel processing to any arbitrary computation; humans are set up (via evolution) to use parallel processing well only for certain types of tasks.

Distributed and decentralized computation
-----------------------------------------

This is true both for the body overall and for the brain. If we think of each computational unit (e.g. a cell, an organ, a piece of the brain) as an individual agent, then the agents are both **competing** and **collaborating**. At any given time, your gut might be competing with part of your brain to decide on the next feeling/thought/action, and one part of your brain could collaborate with another part to form a fuller thought, and then compete with yet another part of the brain to enter your consciousness and dominate your thought. Such collaborative and competitive mechanisms are what enable the whole to be greater than the sum of its parts (as described above).

Some would argue that the thalamus / prefrontal cortex acts as a centralized processor, but this is [debatable](https://www.researchgate.net/post/Is_the_thalamus_REALY_the_CPU_of_the_Brain).

Recursion / feedback loops / self-improvement
---------------------------------------------

There are at least 2 ways to apply this concept.

1.  The brain seems [set up to perform tasks requiring recursive logic](http://www.letras.ufrj.br/poslinguistica/recursion/papers/17-friederici.pdf) (e.g. speaking or understanding phrases like “Peter knew that Maria who loved Hans contacted Johann”)
2.  The brain is able to [self-improve](https://www.bbc.com/future/article/20151123-the-brains-miracle-superpowers-of-self-improvement). I.e. part of neuroplasticity is realized via the brain changing itself (indirectly?). For example, having some thoughts can [result in some enzymes being released, which then cause changes in the number of synapses and synaptic connections](https://www.scirp.org/journal/PaperInformation.aspx?PaperID=73936).

I have a feeling that feedback loops are at play in other ways as well.

By the way, many people believe that self-improving AI is the key to better AI (and to conscious AI and Strong AI). From a practical standpoint, AI that writes or helps write AI software is a great example (as [François Chollet, the creator of Keras, believes](http://www.youtube.com/watch?v=BH4ItyTVMEs&t=42m46s)).

Attention and Abstraction
-------------------------

Humans are good at minimizing wasteful computations. This follows naturally from evolution. A human might have 10 objects in her visual field, and 10 details about each of those objects. But human would naturally 1. limit **attention** to only one of those objects (e.g. attractive potential mate or a dangerous rock flying towards one’s face) and 2. make a simple **abstraction** of the object while ignoring the details (e.g. understand that it’s a dangerous, fast-moving object — no need to think about the exact shape or patterns on the rock). Attention and abstraction mechanisms can sometimes be weaknesses (e.g. sometimes humans jump to conclusions prematurely or gloss over important details) but most of the time they contribute positively to human intelligence.

Computers can use similar approaches. The famous 2017 paper [_Attention is All You Need_](https://arxiv.org/abs/1706.03762)  led to huge advances in natural language processing. The 2018 paper [_World Models_](https://arxiv.org/abs/1803.10122)  described advances in using neural networks to create **abstract** models of the world that are computationally tractable and combining them with other neural networks to perform tasks well.

Computer science algorithms and mathematical operations
-------------------------------------------------------

For example, the [ear amplifies certain sound frequencies and then acts as multiple bandpass filters](https://medium.com/human-like-machine-hearing-with-ai-1-3-a5713af6e2f8) to separate sounds into components. The visual cortex performs multi-layer convolutions (kind of like pooling pixels together) which inspired convolutional neural networks (CNNs), a core part of modern AI for image processing. (See the [Neuroscientific Basis for Convolutional Networks on page 358 of the Deep Learning book](http://www.deeplearningbook.org/contents/convnets.html).)

You could view such phenomena either as “the body uses such mathematical approaches” or, reversing the order, you could say “these mathematical models describe the body’s functionality” or “these algorithms are inspired by biology” but I don’t think it matters which view you choose; my main point is that the body can do cool stuff which contributes to human intelligence.

For more on this, check out the 2012 paper [_Computation Algorithms Inspired by Biological Processes_](https://www.currentscience.ac.in/Volumes/103/04/0370.pdf).

Machine learning algorithms and symbolic reasoning
--------------------------------------------------

Broadly, there are 2 major approaches to AI:

1.  statistical machine learning (learning from the data, e.g. learning to differentiate cats from dogs by looking at the pixels of many labeled photos)
2.  symbolic AI / logical reasoning / [computer algebra](https://en.wikipedia.org/wiki/Computer_algebra) (e.g. manipulate 2y=x into y=0.5x or deduce from “all men are mortal” and “John is a man” that “John is mortal.”)

I think that humans use some form of both of the above. Only using one of the above would be insufficient to explain the intelligence humans have demonstrated. Statistical machine learning is nowadays often implemented via neural networks which are inspired by the human brain. As for symbolic AI, I guess humans must also be able to use something similar to that, since humans are apparently able to do algebraic manipulations and make logical deductions pretty quickly.

The question is, how exactly do we combine #1 and #2 ? There are many possible approaches. For example, see this video: [Bridging Machine Learning and Logical Reasoning by Abductive Learning](https://www.youtube.com/watch?v=ETHrFxiFIUM) (2019). In this approach, “ machine learning models learn to perceive primitive logical facts from the raw data, while logical reasoning is able to correct the wrongly perceived facts for improving the machine learning model.” Does the human brain do something similar? Maybe. Another approach is [OpenCog](https://medium.com/@ybergquist/opencog-vs-openai-2-different-paths-to-human-level-ai-d36deafbf966), which includes both symbolic AI and neural networks as part of a larger connected “hypergraph.”

Taking advantage of biology, chemistry, and physics in the real world
---------------------------------------------------------------------

A laughable but illustrative example is the [Spaghetti Sort algorithm](https://en.wikipedia.org/wiki/Spaghetti_sort) which can be implemented by a human but not by a computer without a physical body. The algorithm involves holding a bunch of uncooked spaghetti rods of different lengths and slamming down the bunch against a table. A human can sort the rods by length with O(n) time complexity. In contrast, the fastest computer algorithm for sorting a list of numbers is O(n log n), which is worse. The computer is not able to take advantage of e.g. gravity which constantly acts on all the rods at the same time (**in parallel**). Of course you could use a computer to simulate gravity’s effect on all the objects, but that is computationally expensive.

![todo add alt text](https://miro.medium.com/max/2000/0*VPTNlchpXsp39-XW.jpg)A human performing Spaghetti Sort

An analogue to Spaghetti Sort is [DNA computing](https://interestingengineering.com/what-is-dna-computing-how-does-it-work-and-why-its-such-a-big-deal). “The power of DNA computing comes from its ability to perform the same operation **simultaneously** on the contents of a test tube…operations can be performed **in parallel** with no added cost” (from [this paper](http://www.cim.mcgill.ca/~scott/RIT/dna_computing.html)).

In other words, stuff (deemed to be computations) happening in the real world (in human bodies) is naturally massively parallel (all happening at the same time) and this is a **huge advantage of humans over traditional computers** (which naturally process things one by one and incur cost to enable parallelism — parallelism which pales in comparison to the real world).

The above may be the biggest challenge to achieving Strong AI via electronic hardware (if we refrain from speculating about [using quantum computing for AI](https://www.quora.com/Can-quantum-computers-help-with-developing-strong-AI)).

Closing
=======

The more I learn about human intelligence, the more I appreciate all the things it can do. But with the flood of awesome research related to neuroscience and ML/AI (and we’re just getting started), and since we’re getting an increasingly better understanding of the mechanisms of human intelligence, **I do believe that machine intelligence will be able to replicate or supersede many aspects of human intelligence eventually.** Not sure when exactly.

Disclaimers
===========

*   I’m not an expert on any of these topics. I’m just a random curious dude.
*   I purposefully avoided discussing the definition of intelligence; that could be a long philosophical debate. You can choose what it means to you, and hopefully the above will still make sense.