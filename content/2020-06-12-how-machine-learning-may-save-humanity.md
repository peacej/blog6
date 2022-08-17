---
title: How Machine Learning May Save Humanity
date: 2020-06-12
category: machine learning
tags: machine learning,futurism,computer science
---

·4 min read


I think humanity will end eventually (whether it takes hundreds or thousands of years). So what’ll we do when the end is near? We’d want to leave our legacy; in other words, **we’d want to save humanity’s knowledge and history as data and send it into space, hoping that aliens somewhere will receive it**. That sounds a lot better than just disappearing into the void without a trace.

This begs the questions:

1.  what information to send
2.  how to compress/represent the information/data
3.  how to send it (including the [transmission strategy](https://arxiv.org/pdf/1101.4968.pdf): using lasers vs. omnidirectional radio transmitters, direction to point in, etc.)

In fact, the approach for #2 (compression) affects #1 and #3. For example, we could decide to select more information for sending if we know it can be efficiently compressed, and if the compression algorithm allows fault-tolerant decompression, that might allow aliens to extract useful information even with incomplete reception of the transmitted data.

The compression tradeoff
========================

We’d want to convey useful information on the **essence** of humanity with **lossy compression** (i.e. we aren’t able to perfectly recover the original data when decompressing). I speculate that the tradeoff between useful information and lossiness of compression may look something like the below, so we’d want to target the highest point in the curve.

![todo add alt text](https://miro.medium.com/max/20000/1*peVnP6QaPft--FpKzvLveA.png)([spreadsheet for the above](https://docs.google.com/spreadsheets/d/1bvpLlxeYF_njHC4oPDhXIgC7bGO5ZLejPPKl9OxFGTw/edit#gid=0))

As you increase lossiness, the information, when decompressed/recovered, becomes less true to the original data and thus less “useful,” but it allows for more efficient compression algorithms, which allows you to fit more usefulness into each bit. The definition of what is “useful” info about humanity is a philosophical debate which I won’t get into now.

Machine learning to the rescue
==============================

Embeddings (essentially, a list of numbers) generated by deep neural networks (e.g. [autoencoders](https://medium.com/@peacej2/generating-fake-k-pop-faces-part-1-6202dc27f0eb) or language models such as [BERT](http://jalammar.github.io/illustrated-bert/)) can be seen as a form of lossy compression (where the degree of compression can be arbitrarily chosen). For example, you can represent an image or the profile of a human with an embedding. As [representation learning](https://arxiv.org/abs/1206.5538) techniques advance, perhaps we’ll be able to accurately represent a human’s behavior/personality with an embedding (queue [Westworld theme song](https://www.youtube.com/watch?v=rYelEUVQ50g)).

Via training, a neural network can figure out how to efficiently represent the essence of the information. Such an approach is [already being used to reduce video download sizes](https://www.forbes.com/sites/nvidia/2019/02/11/accelerating-the-internet-with-ai-based-media-compression/#1a6508107760). In the future, we’ll have even better machine learning techniques to do this even more efficiently.

Of course, we’ll need to send not just the embeddings, but also the neural network parameters as well so that the aliens can make sense of the embeddings.

The information that is represented isn’t limited to just words, images, and numbers. A generative neural network that can accurately generate random new virtual humans (i.e. it “samples” from a realistic distribution of human physique and behavior) or simulate human movement in cities may also be “information” that we want to send.

It’s t̶u̶r̶t̶l̶e̶s̶ models all the way down
===========================================

Let’s get meta for a moment. Neural networks themselves are information. In fact, [even neural networks with randomly chosen parameters can perform well](https://arxiv.org/abs/1906.04358), which implies that the architecture of the network is also important information. Furthermore, a single neural network can be a lot of information. For example, [OpenAI’s GPT-3 language model has 175 billion parameters](https://medium.com/@Synced/openai-unveils-175-billion-parameter-gpt-3-language-model-3d3f453124cd). Hundreds of years from now, we might have models with quadrillions of parameters (which could… simulate all of human civilization…?)

So, we might want to send the aliens:

1.  the parameters of a neural network compressed using another neural network
2.  a model which can design/train other models (although getting this to run on an alien’s hardware/software stack might be non-trivial)
3.  one of the above recursed indefinitely

(BTW, [see this](https://en.wikipedia.org/wiki/Turtles_all_the_way_down) if you didn’t get the joke about turtles 😊)

What would aliens do with the data?
===================================

Hard to say. Maybe they would benefit from some of our technology. Maybe they’d create a computer simulation of earth and humans living on it. Or maybe they’d using advanced bio-engineering to create living things resembling humans… In any case, it would be better than no one ever knowing that humans existed.

This might be the most important thing we ever do
=================================================

Do you want to prioritize big, long-term impact over short-term quick wins? If so, let’s extend the thinking by a few years (or millenia). **After humanity perishes, our long-term impact will be essentially zero unless we communicate with extraterrestrial intelligence.** Unless, of course, we create robots that outlive us in a meaningful way…but even then, the physical robots may perish eventually due the sheer distance to inhabitable planets… then, the only way to **save** our legacy is via efficient transmission of information through space. Otherwise, **the universe will be as if humans had never existed.**

![todo add alt text](https://miro.medium.com/max/20000/1*7y_jTOIX7frtWVz5iSoBPQ.png)Image from [https://art.marcsimonetti.com/science-fiction](https://art.marcsimonetti.com/science-fiction)