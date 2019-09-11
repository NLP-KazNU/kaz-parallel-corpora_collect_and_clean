#!/usr/bin/env python3

# Reads texts from input file.
# Produces 2 files:
# The first contains lines without direct speech.
# The second contains lines that supposedly have direct speech.
# Works for Kazakh and English

import sys
import re

# list of words used in direct speech
words = [
    "say",
    "says",
    "said",
    "tell",
    "tells",
    "told",
    "ask",
    "asks",
    "asked",
    "noted",
    "reported",
    "added",
    "commented",
    "agreed",
    "emphasized",
    "concluded",
    "reports",
    "stated",
    "believes",
    "explained",
    "stressed",
    "pointed out",
    "informed",
    "summed up",
    "declared",
    "underlined",
    "instructed",
    "addressed",
    "congratulated",
    "assured",
    "concluded",
    "announced",
    "highlighted",
    "reads",
    "wrote",
    "tweeted",
    "admitted",
    "states",
    "believes",
    "read",
    "joked",
    "деді",
    "деп",
    "делінген",
    "дейді",
    "деген",
    "хабарлады",
    "айтты",
    "деді",
]


def text_contains_the_words(text: str) -> bool:
    for word in words:
        if re.search(pattern=r"\b" + word + r"\b", string=text) != None:
            return True
    return False


if __name__ == "__main__":
    # check if file name is provided
    if len(sys.argv) == 1:
        sys.exit("Please, provide a file.")
    file_name = sys.argv[1]

    lines_without_direct_speech = []
    lines_with_direct_speech = []

    # read text from a file
    with open(file_name, "r") as in_file:
        input_text = in_file.readlines()
    # for each line:
    #   check if it contains quotes (") and words
    for line in input_text:
        if ('"' in line) and (text_contains_the_words(line)):
            lines_with_direct_speech.append(line)
        else:
            lines_without_direct_speech.append(line)

    with open(file=file_name + "_with_direct_speech.txt", mode="w") as out_file:
        for line in lines_with_direct_speech:
            out_file.write(line)

    with open(file=file_name + "_without_direct_speech.txt", mode="w") as out_file:
        for line in lines_without_direct_speech:
            out_file.write(line)

