#!/usr/bin/env python3

from os import makedirs

FILE_NAME = "/media/zhake/data/Projects/kaz-parallel-corpora/crawl/strategy2050_kz/xmls/30-35/texts/kaz_all_text_clean_split_tok_lower.txt"
PROCESSED_FILES_DIR = "/media/zhake/data/Projects/kaz-parallel-corpora/crawl/strategy2050_kz/xmls/30-35/texts/processed_texts/"

makedirs(name=PROCESSED_FILES_DIR, exist_ok=True)

# read file line by line
with open(file=FILE_NAME, mode="r") as file:

    # create dummy file for the first iteration
    new_file = open(file="/dev/null", mode="w")

    for line in file:

        # if line contains "* * * * * " create new file
        if "* * * * * " in line:
            # close previous file
            new_file.close()
            # find file name in line
            tmp_f = line[
                line.find("* * * * * ") + 10 : line.rfind(" * * * * *")
            ]
            # create new file name and open it
            new_file_name = PROCESSED_FILES_DIR + tmp_f
            new_file = open(file=new_file_name, mode="w")

        # if line does not contain "* * * * * " write it into the file
        else:
            print(line, end="", file=new_file)
