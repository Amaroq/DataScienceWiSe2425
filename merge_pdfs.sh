#!/bin/bash

if
    [ $# -lt 2 ]
then
    echo "Usage:./merge_pdfs.sh file1.pdf file2.pdf [merged.pdf]"
    exit
fi

if
    [ $# -eq 2 ]
then
    pdftk $1 $2 cat output merged.pdf
else
    pdftk $1 $2 cat output $3
fi
