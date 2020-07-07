from typing import List, Union
from collections import Counter

import matplotlib.pyplot as plt
import numpy as np


def read_text_from_file_with_lower(file_name: str) -> List[str]:
    """ Function that saves text lines from file into a list.
    """
    with open(file=file_name, mode="r") as f:
        lines: List[str] = [line.strip().lower() for line in f]
    return lines


def read_floats_from_file(file_name: str) -> List[float]:
    """ Function that saves floats from file into a list.
    """
    floats: List[float] = []

    with open(file=file_name, mode="r") as f:
        for line in f:
            line = line.strip()
            if line.isalpha():
                continue
            if "," in line:
                line = line.replace(",", ".")
            if line != "":
                floats.append(float(line))
    return floats


def count_tokens(texts: List[str]) -> int:
    """Function counts tokens in a list of strings
    """
    num_tokens: int = 0

    for line in texts:
        tokens = line.split()
        num_tokens += len(tokens)

    return num_tokens


def draw_histogram(data: np.array, num_bins: int) -> None:
    n, bins, patches = plt.hist(x=data, bins=num_bins, log=True)
    plt.grid(b=True, axis="y")
    plt.show()


def analyze_scores(file_name: str) -> None:
    """ Function that calculates statistics of hunalign scores.
    """
    scores: List[float] = []
    with open(file=file_name, mode="r") as f:
        for line in f:
            line = line.strip()
            if line.isalpha():
                continue
            if "," in line:
                line = line.replace(",", ".")
            if line != "":
                scores.append(float(line))
    scores = np.array(scores)

    print("Minimum value:\t\t", np.amin(scores))
    print("Maximum value:\t\t", np.amax(scores))
    print("Mean value:\t\t", np.mean(scores))
    print("Median value:\t\t", np.median(scores))
    draw_histogram(data=scores, num_bins=10)
    print()


def analyze_sen_lens(lens: List[int]) -> None:
    """ Function that calculates statistics of sentense lengths.
    """
    lens = np.array(lens)

    print("Minimum value:\t\t", np.amin(lens))
    print("Maximum value:\t\t", np.amax(lens))
    print("Mean value:\t\t", np.mean(lens))
    print("Median value:\t\t", np.median(lens))
    draw_histogram(data=lens, num_bins=10)
    print()


def _to_tokens(text: List[str]) -> List[str]:
    words: List[str] = []
    for line in text:
        words.extend(line.split())
    return words


def analyze_tokens(text: List[str], n_toks_to_print: int = 10) -> None:
    text_words = _to_tokens(text)
    text_words_counter = Counter(text_words)
    print("Number of unique tokens: ", len(text_words_counter))
    print(f"{n_toks_to_print} most common tokens:")
    print(text_words_counter.most_common(n=n_toks_to_print))


ENGLISH_ALPHABET = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

KAZAKH_ALPHABET = set(
    "АӘБВГҒДЕЁЖЗИЙКҚЛМНҢОӨПРСТУҰҮФХҺЦЧШЩЪЫІЬЭЮЯаәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщъыіьэюя"
)

ok_chars_set = set()
ok_chars_set.update(KAZAKH_ALPHABET)
ok_chars_set.update("0123456789")
ok_chars_set.update(" .,-:\"/?!();'$%+*№—«»[–&]’”…")


def _to_chars_counter(text: List[str]) -> Counter:
    char_counter: Counter = Counter()
    for line in text:
        len_line = len(line)
        for (i, char) in enumerate(line):
            if char in KAZAKH_ALPHABET:
                if i == 0:
                    if line[i + 1] not in ok_chars_set:
                        char_counter.update(line[i + 1])
                if i == len_line - 1:
                    if line[i - 1] not in ok_chars_set:
                        char_counter.update(line[i - 1])
                else:
                    if line[i - 1] not in ok_chars_set:
                        char_counter.update(line[i - 1])
                    if line[i + 1] not in ok_chars_set:
                        char_counter.update(line[i + 1])

    return char_counter


def analyze_chars(
    text: List[str], n_chars_to_print: Union[int, None] = None
) -> None:
    text_chars_counter = _to_chars_counter(text)
    print("Number of unique chars: ", len(text_chars_counter))
    print(f"{n_chars_to_print} most common tokens:")
    print("Total count:", sum(text_chars_counter.values()))
    print(text_chars_counter.most_common(n=n_chars_to_print))
