const mediumToMarkdown = require('medium-to-markdown');
 
mediumToMarkdown.convertFromUrl("https://peacej2.medium.com/generating-fake-k-pop-faces-part-1-6202dc27f0eb").then(function (markdown) {
  console.log(markdown); //=> Markdown content of medium post
});
