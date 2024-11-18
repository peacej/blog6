Code for my personal website/blog (https://jerrychi.com).

# requirements
- Stork search https://stork-search.net/docs/install
- pelican search https://pypi.org/project/pelican-search/ 
- Disqus (you may need to install directly from github for it to work `pip install git+https://github.com/disqus/disqus-python`)

`main` branch is for the code/config which is used by the [Pelican](https://blog.getpelican.com/) framework to auto-generate HTML/CSS files.
`gh-pages` branch is for the HTML files etc. that are actually served for the website.

Run `bash buildpush.sh` to automatically build (convert from Markdown to HTML etc.) and push/deploy. This will push the local code to `main`, switch to `gh-pages` branch, push to that too, and then switch back to `main` . 

Run `python medium_to_markdown.py` for an interactive migration tool to convert a Medium article into a markdown file.




More details in [my blog post](https://jerrychi.com/easy-blog-migration-from-medium-to-your-own-site-using-python.html).