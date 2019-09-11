#!/usr/bin/env python3

from os import listdir
from os.path import isfile, join

txt_dir = "/media/zhake/Data/Projects/kaz-parallel-corpora/akorda_kz/xml/texts/"

# get file names
txt_files = [f for f in listdir(txt_dir) if isfile(join(txt_dir, f))]
txt_files.sort()

eng_txt_files = []
kaz_txt_files = []

for item in txt_files:
    if "eng" in item:
        eng_txt_files.append(item)
    elif "kaz" in item:
        kaz_txt_files.append(item)

eng_text = []
kaz_text = []

for i in range(len(eng_txt_files)):
    eng_text.append("***** " + eng_txt_files[i] + " *****")
    eng_text.append("\n")
    kaz_text.append("***** " + kaz_txt_files[i] + " *****")
    kaz_text.append("\n")

    with open(file=join(txt_dir, eng_txt_files[i]), mode="r") as f:
        for line in f:
            eng_text.append(line)
    with open(file=join(txt_dir, kaz_txt_files[i]), mode="r") as f:
        for line in f:
            kaz_text.append(line)

    eng_text.append("\n")
    kaz_text.append("\n")

with open(file=join(txt_dir, "eng_all_text.txt"), mode="w") as f:
    for line in eng_text:
        if line[-1] == "\n":
            f.write(line)
        else:
            f.write(line + "\n")
with open(file=join(txt_dir, "kaz_all_text.txt"), mode="w") as f:
    for line in kaz_text:
        if line[-1] == "\n":
            f.write(line)
        else:
            f.write(line + "\n")
