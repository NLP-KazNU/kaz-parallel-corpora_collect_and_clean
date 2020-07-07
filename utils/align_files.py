#!/usr/bin/env python3

# script that aligns sentences from files in a given folder based on their names

import glob
import subprocess

FILES_DIR = "/media/zhake/data/Projects/kaz-parallel-corpora/crawl/strategy2050_kz/xmls/30-35/texts/processed_texts/"
HUNALIGN_PATH = "/media/zhake/data/Projects/kaz-parallel-corpora/utils/hunalign"
HUNALIGN_DICTIONARY_FILE_PATH = (
    "/media/zhake/data/Projects/kaz-parallel-corpora/utils/en_kz.dic"
)
RESULT_FILE_PATH = "/tmp/strategy2050_kz_corpus_7.tsv"

# read all file names from a DIR
# create lists of kaz and eng files
# sort lists
# check if there is an equal number of files in both lists
# check is names of files correspond to each other
# align each file pair, saving result in one file (may be separate files?)

# =====

# read all file names from a DIR
# create lists of kaz and eng files
kaz_files = glob.glob(pathname=FILES_DIR + "*-kaz.txt")
eng_files = glob.glob(pathname=FILES_DIR + "*-eng.txt")

# sort lists
kaz_files.sort()
eng_files.sort()

# check if there is an equal number of files in both lists
if len(kaz_files) != len(eng_files):
    raise Exception(
        "Number of files in one language does not correspond to number of files in the other language."
    )

# check is names of files correspond to each other
for i in range(len(kaz_files)):
    if (
        kaz_files[i][(kaz_files[i].rfind("/") + 1) : kaz_files[i].rfind("-")]
        != eng_files[i][(eng_files[i].rfind("/") + 1) : eng_files[i].rfind("-")]
    ):
        raise Exception(
            f"Filenames {kaz_files[i]} and {eng_files[i]} do not match."
        )

# align each file pair, saving result in one file (may be separate files?)
for i in range(len(kaz_files)):
    hunalign_com = subprocess.Popen(
        args=HUNALIGN_PATH
        + " -text -bisent -utf "
        + HUNALIGN_DICTIONARY_FILE_PATH
        + " "
        + kaz_files[i]
        + " "
        + eng_files[i]
        + " >> "
        + RESULT_FILE_PATH,
        stdin=subprocess.PIPE,
        shell=True,
    )
    hunalign_com.communicate()
