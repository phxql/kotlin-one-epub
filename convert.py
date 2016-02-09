# Install pandoc (http://johnmacfarlane.net/pandoc/)
# TODO: Merge epubs on commandline. I've imported all the epubs into calibre and then used the epubmerge plugin (https://code.google.com/p/epubmerge/) to get one epub file

import subprocess

with open("sites.txt") as f:
    sites = f.readlines()

cleanedSites = [s.rstrip() for s in sites]	
joinedSites = ' '.join(cleanedSites)

print("Running pandoc...")

command = "pandoc -s --toc --from=markdown --to=epub3 --output=kotlin.epub title.md " + joinedSites
p = subprocess.Popen(command, shell=True)
p.wait()

print("Done. Check kotlin.epub!")
