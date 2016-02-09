# kotlin-one-epub

Small python script to create one epub file from the [Kotlin reference](http://kotlinlang.org/docs/reference/).

## Download

To download the EPub, [click here](https://github.com/phxql/kotlin-one-epub/raw/master/kotlin.epub?raw=true)

## Run it yourself

1. Install [Pandoc](http://pandoc.org/installing.html)
1. Run `python convert.py`

## TODOs

Write a script to merge them together. Currently I'm using Calibre for this. Install the EPubMerge-Plugin (http://www.mobileread.com/forums/showthread.php?t=169744), delete the kotlin.epub file and execute `calibre-debug --run-plugin EpubMerge -- *.epub`. The merged file is called merge.epub.
