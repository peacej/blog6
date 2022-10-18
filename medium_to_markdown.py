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
    title = " ".join(post_url.split("/")[-1].split("-")[:-1])
    if title[0] == '"':
        title = title[1:]
    if title[-1] == '"':
        title = title [:-1]
    print(f'title is {title}')

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
    print(content)
    raise ValueError()
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
    
    MONTH_NAMES = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
    
    title_idx = None
    for line_num, line in enumerate(content.splitlines()):
        if line[:10] == '=' * 10:
            title_idx = line_num
    
    def remove_by_line(content):
        global title
        scraped_date = ''
        res = []
        for line_num, line in enumerate(content.splitlines()):
            line = line.strip().replace('![]','![image_alt_text]')
            if line_num == title_idx -1: title = line
            if line_num == title_idx: continue
            if line == title: continue
            if "[Jerry Chi]" in line: continue
            elif ', 20' in line and (11 <= len(line.strip()) <= 12):
                if len(line) == 11:
                    line = line[:4] + '0' + line[4:]
                assert len(line) == 12
                scraped_date = arrow.get(line, "MMM DD, YYYY").format("YYYY-MM-DD")
            elif (line[:3].lower() in MONTH_NAMES and (5 <= len(line.strip()) <= 6)):
                if len(line) == 5:
                    line = line[:4] + '0' + line[4:]
                line = line + ', ' + arrow.utcnow().format("YYYY")
                scraped_date = arrow.get(line, "MMM DD, YYYY").format("YYYY-MM-DD")
            else: res.append(line)
        return '\n'.join(res), scraped_date
    
    new_content, scraped_date = remove_by_line(new_content)
    if scraped_date:
        date = scraped_date
    if date == '':
        date = input("Unable to auto-detect date. Enter date (format like 2018-10-05): ")
    new_content = (
f"""---
title: {title}
date: {date}
category: {category}
tags: {tags}
---

"""
        + new_content
    )

    # Directory for saving post
    # File is automatically correctly named
    title_for_file_name = re.sub(r'[^\w]', ' ', title)
    title_for_file_name = '-'.join(title_for_file_name.split(' '))
    post_file_name = f"content/{date}-{title_for_file_name}.md"

    # Save the modified post
    with open(post_file_name, "w") as fout:
        fout.write(new_content)
    print(f"Post saved as markdown to {post_file_name}")
