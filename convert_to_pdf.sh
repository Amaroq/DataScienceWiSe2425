#!/bin/bash

if ! [ $# -eq 1 ]
then
    echo "Usage: ./convert_to_pdf.sh file1.ipynb"
    exit
fi

echo "converting $1 to pdf, requires jupyter installed"
jupyter nbconvert $1 --to pdf 
