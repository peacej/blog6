---
title: Trying out AI music generation with Dance Diffusion
date: 2022-10-27
category: AI music
tags: AI music,machine learning,music
cover: images/4078242513_Pop_art_of_daft_punk_at_a_vaporwave_neon_futuristic_cyberpunk_Tokyo__bustling_street_at_night_cyberart_by_liam_wong__rendered_in_octane__3d_render__trending_on_cgsociety__blender_3d.png
---




·2 min read


In late September the **Dance Diffusion music generation model** (beta) was released by [**Harmonai**](https://twitter.com/harmonai_org). Harmonai, backed by Stability AI (which also backed Stable Diffusion), is a deep learning research lab focused on creating open-source generative audio models, supporting researchers and developers with compute grants and community, and providing musicians and audio engineers with new creative tools.

As an oversimplication, Dance Diffusion is kind of like the audio version of Stable Diffusion or DALLE-2, except simpler. Essentially, one adds random noise to an audio track and then a model is trained to remove that noise. A [gentle intro to Dance Diffusion is on the awesome Weights & Biases website](https://wandb.ai/wandb_gen/audio/reports/A-Gentle-Introduction-to-Dance-Diffusion--VmlldzoyNjg1Mzky).

Dance Diffusion doesn’t operate on MIDI files (i.e. the digital version of sheet music) which are used by most generative methods, it operates directly on raw audio files, so that allows for almost any sound to be created.

I think it’s a really cool that a method used for image generation could be applied in the same way to audio. It’s another testament to how fundamental deep learning knowledge can be applied to so many fields.

Unfortunately, it’s still early days, and it’s tough to generate good-sounding music with this model. Here’s one clip I made by interpolating between the noised representations of two 8-second clips from Harder, Better, Faster, Stronger by Daft Punk (see the awesome [original music vid on Youtube](https://www.youtube.com/watch?v=gAjR4_CbPpQ)), using the Dance Diffusion model trained on glitch music from [glitch.cool](http://glitch.cool).

<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1370899315&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/jerry-chi-99480064" title="Jerry Chi" target="_blank" style="color: #cccccc; text-decoration: none;">Jerry Chi</a> · <a href="https://soundcloud.com/jerry-chi-99480064/dance-diffusion-interpolation-of-daft-punk" title="Dance Diffusion interpolation of Daft Punk" target="_blank" style="color: #cccccc; text-decoration: none;">Dance Diffusion interpolation of Daft Punk</a></div>

Someone else was able to make a much better clip, but they used several tools in addition to Dance Diffusion (“gpt-j (lyrics) -> jukebox (w/modded sampler) -> demucs -> pymixconsole -> dance diffusion -> mastering”):

<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1368508270&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Interstate,Lucida Grande,Lucida Sans Unicode,Lucida Sans,Garuda,Verdana,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/baltigor" title="Baltigor" target="_blank" style="color: #cccccc; text-decoration: none;">Baltigor</a> · <a href="https://soundcloud.com/baltigor/lion-0186-12" title="Misery, I Know You (Like Company)" target="_blank" style="color: #cccccc; text-decoration: none;">Misery, I Know You (Like Company)</a></div>

This Dance Diffusion model is much smaller and simpler than Stable Diffusion, and it’s still the early beta version, so I think that explains why it’s not that good yet. Another reason is that there’s not that much non-copyrighted music out there in the public to use as training data.

Anyway, stay tuned because I will share more about AI music generation!

![image]({static}/images/4078242513_Pop_art_of_daft_punk_at_a_vaporwave_neon_futuristic_cyberpunk_Tokyo__bustling_street_at_night_cyberart_by_liam_wong__rendered_in_octane__3d_render__trending_on_cgsociety__blender_3d.png)
Stable Diffusion prompt: “Pop art of daft punk at a vaporwave neon futuristic cyberpunk Tokyo bustling street at night cyberart by liam wong, rendered in octane, 3d render, trending on cgsociety, blender 3d”