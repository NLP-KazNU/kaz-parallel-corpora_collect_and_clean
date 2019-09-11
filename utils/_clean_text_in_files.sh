#!/usr/bin/env bash
DIR="/media/zhake/Data/Projects/kaz-parallel-corpora/akorda_kz/xml/texts"

for filename in $DIR/*eng.txt; do
  ./clean_text.py -i "$filename" -l eng
done

for filename in $DIR/*kaz.txt; do
  ./clean_text.py -i "$filename" -l kaz
done