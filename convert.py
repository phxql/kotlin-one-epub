# Install pandoc (http://johnmacfarlane.net/pandoc/)
# pip install PyYAML

import subprocess
import yaml
import urllib.request
import os
import sys
from functools import reduce

github_user = 'JetBrains' if len(sys.argv) == 1 else sys.argv[1]
base_url = "https://raw.githubusercontent.com/{}/kotlin-web-site/master".format(github_user)
navigation_url = "{}/data/_nav.yml".format(base_url)
reference_url = "{}/pages".format(base_url)
tmp_path = '/tmp/kotlin-one-epub/'
pandoc_extensions = [
    "+pipe_tables", "+backtick_code_blocks", "+yaml_metadata_block", "+inline_code_attributes"
]

print("Fetching navigation...")

response = urllib.request.urlopen(navigation_url).read()

print("Parsing navigation...")
navigation = yaml.safe_load(response)
reference = navigation['reference']['content']
# Exclude 'Reference' and 'Core Libraries' section
excludes = ['Reference', 'Core Libraries', "What's New", 'Releases and Roadmap']
# Access content
content = [r for r in reference if r['title'] not in excludes]
content = [r['content'] for r in content if r.__contains__('content')]
# Flatmap list of lists
content = reduce(list.__add__, content)
# Extract first key of dictionary
urls = [c['url'] for c in content]
# Add base url and use markdown file
urls = [reference_url + u.replace('.html', '.md', 1) for u in urls]

# Download the pages
if not os.path.exists(tmp_path):
    os.makedirs(tmp_path)

tmp_files = []
for i, url in enumerate(urls):
    print("Downloading " + url + "...")
    print(reference_url + url)
    url_content = urllib.request.urlopen(url).read()
    # Remove strange words from the content
    url_content = url_content.decode().replace("{: .keyword }", "")

    filename = tmp_path + str(i) + ".md"
    tmp_file = open(filename, 'w')
    tmp_file.write(url_content)
    tmp_file.close()
    tmp_files.append(filename)

# Run pandoc
print("Running pandoc...")

joined_files = ' '.join(tmp_files)
command = "pandoc -s --toc --from=markdown" + ''.join(pandoc_extensions) + " --to=epub3 --output=kotlin.epub title.md " + joined_files
p = subprocess.Popen(command, shell=True)
p.wait()

print("Done. Check kotlin.epub!")
