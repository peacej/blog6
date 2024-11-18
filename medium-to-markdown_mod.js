const mediumToMarkdown = require('medium-to-markdown');
 
mediumToMarkdown.convertFromUrl("https://peacej2.medium.com/why-creativity-flourishes-in-japan-398afdb68599").then(function (markdown) {
  console.log(markdown); //=> Markdown content of medium post
});
