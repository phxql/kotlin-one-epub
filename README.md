# kotlin-one-epub

Small python script to create one epub file from the [Kotlin reference](http://kotlinlang.org/docs/reference/).

## TODOs

Write a script to merge them together. Currently I'm using Calibre for this. Install the EPubMerge-Plugin (http://www.mobileread.com/forums/showthread.php?t=169744), delete the kotlin.epub file and execute `calibre-debug --run-plugin EpubMerge -- *.epub`. The merged file is called merge.epub.
