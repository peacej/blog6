import copy
import subprocess
import re
import requests
import arrow


def fetch_gist(url):
    """
    Get the gist url from a media content url
    """
    # Get the content from the url
    content = requests.get(url).content.decode()
    # Find the gist url
    match = re.findall("<script src(.*?)><\/script>", content)[0]
    gist_url = re.findall('"(.*?)"', match)[0]
    return f'<script src="{gist_url}"></script>'


if __name__ == "__main__":
    date = ""
    post_url = input("Enter post url: ")
    # Title of post
    title = "-".join(post_url.split("/")[-1].split("-")[:-1])

    category = input("Enter category: ")
    tags = input("Enter tags (comma-separated): ")

    # Read in the template
    with open("medium-to-markdown.js", "r") as f:
        template = f.readlines()

    # Copy the template
    template_mod = copy.deepcopy(template)

    # Update the js script with the url
    template_mod[2] = f'mediumToMarkdown.convertFromUrl("{post_url}")'

    # Write the new file
    with open("medium-to-markdown_mod.js", "w") as f:
        f.writelines(template_mod)

    # Run javascript function
    content = subprocess.Popen(
        ["node", "medium-to-markdown_mod.js"], stdout=subprocess.PIPE
    )

    # Extract html as string
    content = content.stdout.read().decode()

    # Replace noscript image duplication
    new_content = re.sub("\\n\\n<noscript>(.*?)<\/noscript>\\n\\n", "\n", content)

    # Upgrade image quality
    new_content = re.sub("/max/[0-9]{1,3}", "/max/2000", new_content)

    # Replace source location
    new_content = re.sub(
        "source=post_page---------------------------", "", new_content
    )

    # Remove personal blurb
    new_content = re.sub("\[(.*?) min read", "", new_content)

    # Replace <pre> around code blocks
    new_content = re.sub("<pre(.*?)>", "```\\n", new_content)
    new_content = re.sub("<\/pre(.*?)>", "\\n```", new_content)

    # Replace <span> within code blocks
    new_content = re.sub("<span(.*?)>", "\\n", new_content)
    new_content = re.sub("<\/span(.*?)>", "\\n", new_content)

    new_content = re.sub("freeze/", "", new_content)

    # Identify all iframes (GitHub gists)
    iframes = re.findall("<iframe(.*?)><\/iframe>", new_content)

    # Process each iframe
    for iframe in iframes:
        # Find the url in the frame
        url = re.findall('src="(.*?)"', iframe)[0]
        # Only use those urls with towardsdatascience
        if "towardsdatascience" in url:
            # Create a replacement script
            replacement = fetch_gist(url)
            old_iframe = f"<iframe{iframe}></iframe>"

            # Substitute the old iframe with the new replacement
            new_content = re.sub(old_iframe, replacement, new_content)

    captions = captions = re.findall("!\[\]\((.*?)\)\\n(.*?)\\n\\n", new_content)

    for caption in captions:
        original = f"![todo add alt text]({caption[0]})\n{caption[1]}\n\n"
        replacement = f"![todo add alt text]({caption[0]})\n*{caption[1]}*\n\n"
        new_content = new_content.replace(original, replacement)
    
    def remove_by_line(content):
        scraped_date = ''
        res = []
        for line in content.splitlines():
            if "[Jerry Chi]" in line: continue
            elif ', 20' in line and (11 <= len(line.strip()) <= 12):
                print('##DEBUG##')
                line = line.strip()
                if len(line) == 11:
                    line = line[:4] + '0' + line[4:]
                scraped_date = arrow.get(line, "MMM DD, YYYY").format("YYYY-MM-DD")
            else: res.append(line)
        return '\n'.join(res), scraped_date
    
    new_content, scraped_date = remove_by_line(new_content)
    if scraped_date:
        date = scraped_date
    if date == '':
        date = input("Unable to auto-detect date. Enter date (format like 2018-10-05): ")
    new_content = (
f"""title: "{title.replace('-', ' ').title()}"
date: {date}
category: {category}
tags: {tags}

"""
        + new_content
    )

    # Directory for saving post
    # File is automatically correctly named
    post_file_name = f"content/{date}-{title}.md"

    # Save the modified post
    with open(post_file_name, "w") as fout:
        fout.write(new_content)
    print(f"Post saved as markdown to {post_file_name}")
