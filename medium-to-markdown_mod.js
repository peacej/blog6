const mediumToMarkdown = require('medium-to-markdown');
 
mediumToMarkdown.convertFromUrl("https://peacej2.medium.com/trying-out-ai-music-generation-with-dance-diffusion-b58743679a8d").then(function (markdown) {
  console.log(markdown); //=> Markdown content of medium post
});
