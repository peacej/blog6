const mediumToMarkdown = require('medium-to-markdown');
 
mediumToMarkdown.convertFromUrl("https://peacej2.medium.com/positive-trends-in-japan-7e2c4259d5e8").then(function (markdown) {
  console.log(markdown); //=> Markdown content of medium post
});
