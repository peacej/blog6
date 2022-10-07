---
title: How Stable Diffusion (Latent Diffusion) works
date: 2022-08-25
category: AI art
tags: machine learning
---




·2 min read


The [Stable Diffusion model](https://huggingface.co/CompVis/stable-diffusion), just released a few days ago, is all the rage right now, with tons of people generating all sorts of amazing high-quality images, sometimes on par with or even better than OpenAI’s DALL-E 2.

UPDATE 2022–10–07: a new, more beginner-friendly article on Stable Diffusion was posted at[
https://jalammar.github.io/illustrated-stable-diffusion/](https://jalammar.github.io/illustrated-stable-diffusion/) .

But how does it actually work from a technical perspective?

Basically, it uses a variational autoencoder (VAE) combined with a denoising diffusion model. The key idea is that using diffusion models in pixel space (the raw image) is not the most efficient approach, since there are many barely perceptible small details that are not efficiently learned by a diffusion model. Rather, we can use a VAE to map images into a latent space (a form of compression), and then train the diffusion model in the (much smaller) latent space of images.

Source: [https://huggingface.co/blog/stable\_diffusion](https://huggingface.co/blog/stable_diffusion)

Stable Diffusion is [basically a special case / specific configuration of Latent Diffusion](https://github.com/CompVis/stable-diffusion). A lot of effort went into making it very high-quality and easy to use for the masses.

The above explanation barely scratches the surface. [**For more in-depth details on Stable Diffusion / Latent Diffusion, please see this google doc I made.**](https://docs.google.com/document/d/1x4iHe9mdyqpuINRN2EYMuG6_0JSBoNnjtDdSte18Ugc/edit#)

Also, I compiled various AI art resources (both technical and non-technical) at [https://tinyurl.com/creative-ai-links](https://tinyurl.com/creative-ai-links).

Of course, we need to wrap up with some actual AI art :) The below image was generated using Stable Diffusion at [https://beta.dreamstudio.ai/](https://beta.dreamstudio.ai/) with the prompt “Character portrait of a graceful and pretty Korean princess with gorgeous detailed eyes and flowing hair, fantasy setting, color page, tankobon, 4k, tone mapping, doll, akihiko yoshida, james jean, andrei riabovitchev, marc simonetti, yoshitaka amano”