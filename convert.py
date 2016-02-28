# Install pandoc (http://johnmacfarlane.net/pandoc/)
# pip install PyYAML

import subprocess
import yaml
import urllib2
import os

navigation_url = 'https://raw.githubusercontent.com/JetBrains/kotlin-web-site/master/_data/_nav.yml'
base_url = 'https://raw.githubusercontent.com/JetBrains/kotlin-web-site/master'
tmp_path = '/tmp/kotlin-one-epub/'

print("Fetching navigation...")

response = urllib2.urlopen(navigation_url).read()

print("Parsing navigation...")
navigation = yaml.safe_load(response)
reference = navigation['reference']
# Access content
content = [r['content'] for r in reference if r['title'] != 'Reference'] # Exclude 'Reference' section
# Flatmap list of lists
content = reduce(list.__add__, content)
# Extract first key of dictionary
urls = [c.iterkeys().next() for c in content]
# Add base url and use markdown file
urls = [base_url + u.replace('.html', '.md', 1) for u in urls]

# Download the pages
if not os.path.exists(tmp_path):
    os.makedirs(tmp_path)

tmp_files = []
for i, url in enumerate(urls):
    print("Downloading " + url + "...")
    url_content = urllib2.urlopen(base_url + url).read()
    # Remove strange words from the content
    url_content = url_content.replace("{: .keyword }", "")

    filename = tmp_path + str(i) + ".md"
    tmp_file = open(filename, 'w')
    tmp_file.write(url_content)
    tmp_file.close()
    tmp_files.append(filename)

# Run pandoc
print("Running pandoc...")

joined_files = ' '.join(tmp_files)
command = "pandoc -s --toc --from=markdown --to=epub3 --output=kotlin.epub title.md " + joined_files
p = subprocess.Popen(command, shell=True)
p.wait()

print("Done. Check kotlin.epub!")
