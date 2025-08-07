#!/usr/bin/sh

latexdiff original-submission.tex main.tex --flatten > diff.tex
pdflatex diff.tex
pdflatex diff.tex
