#!/usr/bin/env python3

# script cleans texts in Kazakh and English.

# # it leaves:
# - letter from alphabets
# - punctuation

# for any other symbol it asks a user for a decision

# TODO добавить '

# docstring for docopt
"""clean_text.py

Usage:
    clean_text.py (-i | --input) <input_file> (-l | --lang) <language> [(-o | --output) <output_file>]
    clean_text.py (-h | --help)
    clean_text.py (-v | --version)

Options:
    -i --input      path to an input text file to be cleaned
    -l --lang       language of the text file (kk, kz or kaz for Kazakh; en or eng for English)
    -o --output     (optional) path to an output file with cleaned text
    -v --version    Show version.
    -h --help       Show this screen.
"""

from docopt import docopt
import re
from typing import List

ENGLISH_ALPHABET = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

KAZAKH_ALPHABET = set(
    "АӘБВГҒДЕЁЖЗИЙКҚЛМНҢОӨПРСТУҰҮФХҺЦЧШЩЪЫІЬЭЮЯаәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщъыіьэюя"
)

DIGITS = set("0123456789")

# a space " " is treated as a punctuation
# a "\n" is treated as a punctuation
PUNCTUATION = set(' \n.,"-\(\);:!?')

ZERO_WIDTH_CHARS = "\u2060\u2061\u2062\u2063\u180E\u200B\u200C\u200D\uFEFF\u00AD"

# hyphens without -
HYPHENS = "‐−‒⁃–—―‑"

# quotation marks without "
QUOTATION_MARKS = "«»„“”„”‟❝❞⹂〝〞〟＂"

# unwanted symbols found during cleaning.
# added after first confirmation
# to be deleted without asking
UNWANTED_SYMBOLS = set()

# wanted symbols found during cleaning.
# added after first confirmation
# to be kept without asking
WANTED_SYMBOLS = set()

MARK_FOR_FUTURE_EDITING_WAS_ADDED = False


def contains_zero_width_chars(s: str) -> bool:
    """
    Checks if s contains zero-width chars.
    If it does returns True,
    else returns False
    """
    for zero_width_char in ZERO_WIDTH_CHARS:
        if zero_width_char in s:
            return True

    return False


def clean_spaces(text: List[str]) -> List[str]:
    """
    Remove zero-width spaces.
    Convert various and numerouse spaces into a plain single space " ".
    Remove heading and tailing spaces.
    """
    result = []

    for line in text:
        tmp_str = line

        # Remove zero-width spaces.
        if contains_zero_width_chars(tmp_str):
            tmp_str = re.sub(
                pattern=r"[" + ZERO_WIDTH_CHARS + r"]",
                repl="",
                string=tmp_str,
            )

        # Convert various and numerouse spaces into a plain single space " ".
        # use regex "\s+" - any whitespace character repeated one or more times
        tmp_str = re.sub(pattern=r"\s+", repl=" ", string=tmp_str)

        # Remove heading and tailing spaces.
        # use regex "^ " - space at the beginning of a line
        tmp_str = re.sub(pattern=r"^ ", repl="", string=tmp_str)
        # use regex " $" - space at the end of a line
        tmp_str = re.sub(pattern=r" $", repl="", string=tmp_str)

        result.append(tmp_str)

    return result


def clean_empty_lines(text: List[str]) -> List[str]:
    """
    Clean empty lines
    """
    result = []

    for line in text:
        if (line != "") and (line != "\n"):
            result.append(line)

    return result


def clean_quotation_marks(text: List[str]) -> List[str]:
    """
    Convert various quotation marks «»„“”‘’„”‟❝❞⹂〝〞〟＂ into ".
    """
    result = []

    for line in text:
        # if a line contains any quotation marks, replace them with "
        if bool(set(QUOTATION_MARKS).intersection(set(line))) == True:
            # use regex "[«»„“”‘’„”‟❝❞⹂〝〞〟＂]" - any quotation mark character
            tmp_str = re.sub(pattern=r"[" + QUOTATION_MARKS + "]", repl='"', string=line)
            result.append(tmp_str)
        # if a line does not contain any quotation marks, leave it as it is
        else:
            result.append(line)

    return result


def clean_hyphens(text: List[str]) -> List[str]:
    """
    Convert various hyphens ‐−‒⁃–—― into -.
    """
    result = []

    for line in text:
        # if a line contains any hyphens, replace them with -
        if bool(set(HYPHENS).intersection(set(line))) == True:
            # use regex "[‐−‒⁃–—―]" - any quotation mark character
            tmp_str = re.sub(pattern=r"[" + HYPHENS + "]", repl="-", string=line)
            result.append(tmp_str)
        # if a line does not contain any hyphens, leave it as it is
        else:
            result.append(line)

    return result


def get_total_number_of_a_char(char_to_count: str) -> int:
    """
    Returns total number of a particular character in a cleaned_text.
    """
    global cleaned_text

    counter = 0
    for line in cleaned_text:
        for char in line:
            if char == char_to_count:
                counter += 1

    return counter


# TODO mark all for future editing (?)
def ask_a_user(
    line: str, line_number: int, symbol: str, symbol_number: int, total_lines: int
) -> str:
    """
    Show a potentially unwanted symbol to a user.
    Ask what to do with it.
    """
    while True:
        print()
        print("----------")
        print()
        print(f"Line {line_number} (out of {total_lines}):")
        print("...")
        print(line)
        print("...")
        print()
        print(
            f'Symbol "{symbol}" (unicode: {ord(symbol)}) was found on the position {symbol_number}.'
        )
        print(
            f"There is/are {get_total_number_of_a_char(symbol)} such symbol(s) in the file."
        )
        print()
        print("What do you want to do with it?")
        user_decision = input(
            "(k)eep once, keep (a)ll, (d)elete once, delete al(l), (m)ark for future editing: "
        )
        if user_decision == "k":
            return "keep once"
        elif user_decision == "a":
            return "keep all"
        elif user_decision == "d":
            return "delete once"
        elif user_decision == "l":
            return "delete all"
        elif user_decision == "m":
            return "edit later"
        else:
            pass


def clean_chars_interactively(text: List[str]) -> List[str]:
    """
    Look throught symbols of text.
    If unexpected symbol is found, ask a user what to do with it
    """
    result = []

    # all lines in text
    all_lines = len(text)
    # count lines
    line_number = 0

    # for every line
    for line in text:
        # count lines
        line_number += 1
        # count symbols
        symbol_number = 0

        # prepare output line
        output_line = ""

        # for every symbol in a line
        for symbol in line:
            # count symbols
            symbol_number += 1

            # check unwanted_symbols
            if symbol in UNWANTED_SYMBOLS:
                continue

            # check alphabet, punctuation, wanted_symbols
            # if a symbol is not there, ask a user
            elif (
                (symbol not in alphabet)
                and (symbol not in PUNCTUATION)
                and (symbol not in WANTED_SYMBOLS)
            ):
                # ask a user what to do
                user_decision = ask_a_user(
                    line, line_number, symbol, symbol_number, all_lines
                )

                # do as user wants
                if user_decision == "keep once":
                    output_line += symbol
                    continue
                elif user_decision == "keep all":
                    WANTED_SYMBOLS.add(symbol)
                    output_line += symbol
                    continue
                elif user_decision == "delete once":
                    continue
                elif user_decision == "delete all":
                    UNWANTED_SYMBOLS.add(symbol)
                    continue
                elif user_decision == "edit later":
                    output_line += "<edit>" + symbol + "</edit>"
                    global MARK_FOR_FUTURE_EDITING_WAS_ADDED
                    MARK_FOR_FUTURE_EDITING_WAS_ADDED = True
                    continue

            # if a symbol is there, let it through
            else:
                output_line += symbol

        # save a cleaned line
        result.append(output_line)

    return result


if __name__ == "__main__":
    arguments = docopt(__doc__, version="clean_text.py v.0.1")

    # get command line parameter values
    input_file_name = arguments["<input_file>"]
    language = arguments["<language>"]
    if arguments["<output_file>"] != None:
        output_file_name = arguments["<output_file>"]
    else:
        output_file_name = "cleaned_output.txt"

    # code for debug
    # input_file_name = "/tmp/text.en"
    # language = "en"
    # output_file_name = "/tmp/cleaned_text.txt"

    # choose an alphabet
    alphabet = set()
    if (language == "en") or (language == "eng"):
        alphabet = ENGLISH_ALPHABET
    elif (language == "kk") or (language == "kz") or (language == "kaz"):
        alphabet = KAZAKH_ALPHABET
    alphabet.update(DIGITS)

    # read text from an input file
    with open(input_file_name, "r") as in_file:
        input_text = in_file.readlines()

    cleaned_text = []

    cleaned_text = clean_spaces(input_text)
    cleaned_text = clean_empty_lines(cleaned_text)
    cleaned_text = clean_quotation_marks(cleaned_text)
    cleaned_text = clean_hyphens(cleaned_text)
    # cleaned_text = clean_chars_interactively(cleaned_text)
    cleaned_text = clean_spaces(cleaned_text)

    # TODO: combine 2 following parts with print(..., end='\n', file="...")

    # add '\n' at the end of every line
    for i in range(len(cleaned_text)):
        cleaned_text[i] = cleaned_text[i] + "\n"

    # write cleaned text to a file
    with open(output_file_name, "w") as out_file:
        out_file.writelines(cleaned_text)

    if MARK_FOR_FUTURE_EDITING_WAS_ADDED == True:
        print()
        print("----------")
        print()
        print("You have marked some parts of your file for future editing.")
        print(
            f"Check for <edit>...</edit> tags in your output file ({output_file_name})."
        )

