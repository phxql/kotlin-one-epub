# Install pandoc (http://johnmacfarlane.net/pandoc/)
# TODO: Merge epubs on commandline. I've imported all the epubs into calibre and then used the epubmerge plugin (https://code.google.com/p/epubmerge/) to get one epub file

import subprocess

with open("sites.txt") as f:
    sites = f.readlines()

i = 1
for site in sites:
    stripped = site.rstrip()
    if stripped:
	print "Converting " + stripped

	command = "pandoc -s -r html -t epub3 " + stripped + " -o " + "{0:0=3d}".format(i) + ".epub"
	p = subprocess.Popen(command, shell=True)
	p.wait()
        i += 1
