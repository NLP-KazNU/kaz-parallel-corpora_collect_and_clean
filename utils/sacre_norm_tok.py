#!/usr/bin/env python3

from sacremoses import MosesPunctNormalizer
from sacremoses import MosesTokenizer

FILE_NAME = "/media/zhake/data/Projects/kaz-parallel-corpora/crawl/strategy2050_kz/xmls/30-35/texts/kaz_all_text_clean_split.txt"

mpn = MosesPunctNormalizer()
mt = MosesTokenizer()

with open(file=FILE_NAME, mode="r") as f_in:
    norm_text = [mpn.normalize(text=line) for line in f_in]

tok_text = [
    mt.tokenize(text=line, return_str=True, escape=False) for line in norm_text
]

with open(file=f"{FILE_NAME}_tok", mode="w") as f_out:
    for line in tok_text:
        print(line.strip(), file=f_out)
