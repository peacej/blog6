const mediumToMarkdown = require('medium-to-markdown');
 
mediumToMarkdown.convertFromUrl("https://peacej2.medium.com/easy-blog-migration-from-medium-to-your-own-site-using-python-894d617f6ff3").then(function (markdown) {
  console.log(markdown); //=> Markdown content of medium post
});
