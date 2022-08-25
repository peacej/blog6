const mediumToMarkdown = require('medium-to-markdown');
 
mediumToMarkdown.convertFromUrl("https://peacej2.medium.com/how-stable-diffusion-latent-diffusion-works-991bec22988f").then(function (markdown) {
  console.log(markdown); //=> Markdown content of medium post
});
