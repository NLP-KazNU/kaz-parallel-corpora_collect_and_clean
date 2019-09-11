#!/usr/bin/env python3

from os import listdir
import os
from os.path import isfile, join
from xml.dom import minidom

xml_dir = "/media/zhake/Data/Projects/kaz-parallel-corpora/akorda_kz/xml/"


def save_text_in_file(text: str, file_name: str) -> None:
    """TODO"""
    file_name = file_name.replace("xml", "txt")
    global xml_dir

    if not os.path.exists(join(xml_dir, "texts")):
        os.makedirs(join(xml_dir, "texts"))

    with open(file=join(xml_dir, "texts", file_name), mode="w") as f:
        f.write(text)


# get file names
xml_files = [f for f in listdir(xml_dir) if isfile(join(xml_dir, f))]
xml_files.sort()

eng_xml_files = []
kaz_xml_files = []

for item in xml_files:
    if "eng" in item:
        eng_xml_files.append(item)
    elif "kaz" in item:
        kaz_xml_files.append(item)

eng_titles = []
kaz_titles = []

for i in range(len(eng_xml_files)):
    # open a file
    eng_xml_data = minidom.parse(join(xml_dir, eng_xml_files[i]))
    eng_xml_data.normalize()

    kaz_xml_data = minidom.parse(join(xml_dir, kaz_xml_files[i]))
    kaz_xml_data.normalize()
    # extract titles
    if len(eng_xml_data.getElementsByTagName("title")[0].childNodes) == 0:
        eng_title = ""
    else:
        eng_title = eng_xml_data.getElementsByTagName("title")[0].childNodes[0].nodeValue

    if len(kaz_xml_data.getElementsByTagName("title")[0].childNodes) == 0:
        kaz_title = ""
    else:
        kaz_title = kaz_xml_data.getElementsByTagName("title")[0].childNodes[0].nodeValue

    if (eng_title != "") and (kaz_title != ""):
        eng_titles.append(eng_title)
        kaz_titles.append(kaz_title)

    # extract text
    if len(eng_xml_data.getElementsByTagName("text")[0].childNodes) == 0:
        eng_text = ""
    else:
        eng_text = eng_xml_data.getElementsByTagName("text")[0].childNodes[0].nodeValue

    if len(kaz_xml_data.getElementsByTagName("text")[0].childNodes) == 0:
        kaz_text = ""
    else:
        kaz_text = kaz_xml_data.getElementsByTagName("text")[0].childNodes[0].nodeValue

    # save texts into separate file pairs
    if (eng_text != "") and (kaz_text != ""):
        save_text_in_file(eng_text, eng_xml_files[i])
        save_text_in_file(kaz_text, kaz_xml_files[i])

# save titles into one file pair
with open(file="titles_eng.txt", mode="w") as f:
    for line in eng_titles:
        print(line, file=f)

with open(file="titles_kaz.txt", mode="w") as f:
    for line in kaz_titles:
        print(line, file=f)
