---
title: Easy Blog Migration From Medium To Your Own Site Using Python
date: 2022-08-17
category: web dev
tags: web dev,blogging,Python
---




·3 min read


Recently I migrated my existing articles from Medium to my own new website ([https://jerrychi.com](https://jerrychi.com)) in a **quick, low-code way**. I wanted to have both blog articles and permanent pages (e.g. “About Me” page) and **high customizability while spending minimal effort and money**.

You can do this too! Here’s how:

Register a domain name. I used [https://domains.google/](https://domains.google/) to register [jerrychi.com](https://jerrychi.com), paying about $12 per year. This is the only thing I’m paying for.

Install required Python libraries including [Pelican](https://getpelican.com/) (the Python-based static site generator for creating personal blogs/websites) on your local laptop. E.g. `pip install -r requirements.txt` (see my `[requirements.txt](https://github.com/peacej/blog6/blob/main/requirements.txt)`). I used Python 3.8.6 in a [conda environment](https://conda.io/projects/conda/en/latest/user-guide/concepts/environments.html) but other setups should work too.

![image_alt_text](https://miro.medium.com/max/2000/1*F-NLYAtzFjXLDYa4PLzXOw.png)Pelican logo

Auto-convert any Medium articles you choose to Markdown files (which are compatible with Pelican, which will then auto-convert them to HTML/Javascript) using the `medium_to_markdown` tool described at [https://willkoehrsen.github.io/writing/markdown/converting-medium-posts-to-markdown-for-your-blog /](https://willkoehrsen.github.io/writing/markdown/converting-medium-posts-to-markdown-for-your-blog/) . I did [slightly tweak his code](https://github.com/peacej/blog6/blob/main/medium_to_markdown.py) to e.g. filter out a few specific words. This doesn’t require any special access to your Medium account; it’s just scraping the text from the public internet.

Push your code to a new Github repo.

*   You can host the website on [Github Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages) for free, up to 1 GB of storage (nothing beyond that even if you want to pay). If I ever need more than 1 GB, I might migrate to Heroku.
*   You can [use your own custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site) (in my case [jerrychi.com](https://jerrychi.com))

We need a `master` or `main` git branch for all the code and then a `gh-pages` branch to store the actual website assets that are served when people visit your site. Thankfully one can just use a tool called `ghp-import` to automate pushing the only the needed to `gh-pages` branch. You can see [how I use this tool](https://github.com/peacej/blog6/blob/main/buildpush.sh). After pushing to github, usually changes are reflected in a few seconds on my website.

*   Tip: style changes to CSS files etc. may require an “[empty cache and hard reload](https://gsuitetips.com/tips/chrome/chrome:-empty-cache-and-hard-reload/#:~:text=Normal%20Reload%3A%20Uses%20Cached%20Data,be%20re%2Ddownloaded%20as%20required.)” in Chrome to be visually reflected on the website due to caching.

Pelican also supports add-ons, themes, etc.

*   See the [pelican-themes repo](https://github.com/getpelican/pelican-themes) for instructions on themes.
*   I chose to use the [Flex theme](https://github.com/alexandrevicenzi/Flex/) which includes many nifty features such a mobile-first responsive UI. I cloned this Flex repo directly rather than cloning from the `pelican-themes` repo which pins Flex at an older version.
    - In `pelicanconf.py` (the main configuration file) I simply set `PLUGINS = ["pelican.plugins.search"]` and `STORK_VERSION = "1.5.0"` to enable a search box on the left navigation bar. 
*   I also edited the `pelican-templates/Flex/static/stylesheet/style.less` file to customize the font style (my first time dealing with the [Less language](https://lesscss.org/) but it was easy to edit).

That’s it! Now you have a nice shiny new personal website~

So, why did I choose Pelican? I also considered Nikola and Django:

*   Nikola: the second-most popular Python static site generator after Pelican. I did initially try building with Nikola but got frustrated with the documentation being a bit unclearly worded and the lack of resources/answers when e.g. googling around for an issue. Pelican is more established and popular with more discussion/answers for potential issues.
*   Django: the most popular Python web backend framework. I did take the [Django official tutorial](https://docs.djangoproject.com/en/4.1/intro/tutorial01/), which was enjoyable and extremely well-written. However, Django is much more complicated than Pelican (which is natural since Django is a general-purpose framework for creating any sort of webpage) and I’d likely end up combining Django with a frontend framework like React (meaning one more framework to learn). The complexity and work required was overkill for needs: a simple personal website. I’ll come back to learn Django+React if I need a much fancier site.