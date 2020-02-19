#!/usr/bin/env python3

import sys
import re
from typing import List, Dict

ENGLISH_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
KAZAKH_ALPHABET = "АӘБВГҒДЕЁЖЗИЙКҚЛМНҢОӨПРСТУҰҮФХҺЦЧШЩЪЫІЬЭЮЯаәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщъыіьэюя"


def lists_2_dict(list1: List, list2: List) -> Dict:
    """lists_2_dict(list1: List, list2: List) -> Dict

    Function accepts 2 lists of equal length and
    returns a dictionary with keys from the 1st list and values from the 2d list.
    """
    return {k: v for k, v in zip(list1, list2)}


# АВҒЕКМНОРСТХҺІЬаеорсхһі
# <->
# ABFEKMHOPCTXhIbaeopcxhi
ENG_2_KAZ_DICT = lists_2_dict(
    list1=list("ABFEKMHOPCTXhIbaeopcxhi"), list2=list("АВҒЕКМНОРСТХҺІЬаеорсхһі")
)
KAZ_2_ENG_DICT = lists_2_dict(
    list1=list("АВҒЕКМНОРСТХҺІЬаеорсхһі"), list2=list("ABFEKMHOPCTXhIbaeopcxhi")
)

regexps = [
    # select one english letter between kazakh letters
    f"(?<=[{KAZAKH_ALPHABET}])[{ENGLISH_ALPHABET}](?=[{KAZAKH_ALPHABET}])",
    # select one kazakh letter between english letters
    f"(?<=[{ENGLISH_ALPHABET}])[{KAZAKH_ALPHABET}](?=[{ENGLISH_ALPHABET}])",
]


def replace_char(char: str) -> str:
    """replace_char(char: str) -> str

    Function accepts a character, checks if it is among replaceable characters.
    If it is - replacement is returned.
    If it is not - it is returned without changes.
    """
    if char in ENG_2_KAZ_DICT.keys():
        return ENG_2_KAZ_DICT[char]
    elif char in KAZ_2_ENG_DICT.keys():
        return KAZ_2_ENG_DICT[char]
    else:
        return char


if __name__ == "__main__":
    # check if file name is provided
    if len(sys.argv) == 1:
        sys.exit("Please, provide a file.")
    file_name = sys.argv[1]
    # file_name = "/tmp/eng_cleaned.txt"

    result = []

    with open(file_name, "r") as in_file:
        for line in in_file:
            new_line = line
            for regexp in regexps:
                for match in re.finditer(pattern=regexp, string=new_line):
                    found_index = match.span()[0]
                    tmp_old = new_line[found_index]
                    tmp_new = replace_char(new_line[found_index])
                    tmp_max = 1
                    new_line = new_line.replace(tmp_old, tmp_new, tmp_max)
                    # new_line[found_index] = replace_char(new_line[found_index])

            result.append(new_line)

    with open(file=file_name + "_tmp.txt", mode="w") as f:
        for line in result:
            if line[-1] == "\n":
                f.write(line)
            else:
                f.write(line + "\n")

print(
    """please check for following:
- [АӘБВГҒДЕЁЖЗИЙКҚЛМНҢОӨПРСТУҰҮФХҺЦЧШЩЪЫІЬЭЮЯаәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщъыіьэюя]+[A-Za-z]
- [A-Za-z][АӘБВГҒДЕЁЖЗИЙКҚЛМНҢОӨПРСТУҰҮФХҺЦЧШЩЪЫІЬЭЮЯаәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщъыіьэюя]+
- [A-Za-z]+[АӘБВГҒДЕЁЖЗИЙКҚЛМНҢОӨПРСТУҰҮФХҺЦЧШЩЪЫІЬЭЮЯаәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщъыіьэюя]
- [АӘБВГҒДЕЁЖЗИЙКҚЛМНҢОӨПРСТУҰҮФХҺЦЧШЩЪЫІЬЭЮЯаәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщъыіьэюя][A-Za-z]+
"""
)
