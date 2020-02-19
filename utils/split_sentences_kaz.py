#!/usr/bin/env python3

import sys
import re
from typing import List

# If line contains more than 1 dot
# for Kazakh split at 5+ letter with a dot
# for English split at 4+ letter with a dot


def count_dots(text: str) -> int:
    """
    TODO
    """
    count = 0
    for char in text:
        if char == ".":
            count += 1
    return count


def split_by_end_short_words(text: str) -> List[str]:
    """
    TODO
    """
    EOS_SHORT_WORDS = [
        "алда",
        "асуы",
        "баға",
        "даму",
        "жүйе",
        "жуық",
        "идея",
        "қаза",
        "қосу",
        "күші",
        "мәні",
        "орны",
        "өсім",
        "таяу",
        "тілі",
        "түсу",
        "ұғым",
        "үшін",
        "шешу",
        "білу",
        "болу",
        "жайт",
        "күні",
        "озды",
        "өсуі",
        "сала",
        "салу",
        "тиді",
        "толы",
        "түрі",
        "бөлу",
        "еуро",
        "жылы",
        "иесі",
        "келе",
        "көшу",
        "өкім",
        "шара",
        "жәйт",
        "көзі",
        "мүше",
        "ұйым",
        "жолы",
        "үлгі",
        "беру",
        "қиын",
        "шарт",
        "адам",
        "ғана",
        "туды",
        "әзір",
        "анық",
        "екен",
        "жоба",
        "қала",
        "ашық",
        "едік",
        "құру",
        "едім",
        "деді",
        "енді",
        "метр",
        "ашты",
        "асты",
        "бірі",
        "өсті",
        "алды",
        "емес",
        "етті",
        "тиіс",
        "отыр",
        "өтті",
        "куә",
        "рас",
        "бай",
        "ғой",
        "жат",
        "қой",
        "күш",
        "сәт",
        "ашу",
        "аян",
        "ісі",
        "жол",
        "тең",
        "жер",
        "жыл",
        "күн",
        "жүр",
        "осы",
        "мол",
        "сөз",
        "ету",
        "көп",
        "зор",
        "еді",
        "жөн",
        "тұр",
        "жоқ",
        "бар",
    ]

    result = []

    for word in EOS_SHORT_WORDS:
        tmp_list = re.split(pattern=r"(?<=\b" + word + r"\.) ", string=text)
        if len(tmp_list) > 1:
            result.extend(tmp_list)
            break

    if len(result) > 0:
        return result
    else:
        return [text]


if __name__ == "__main__":
    # check if file name is provided
    if len(sys.argv) == 1:
        sys.exit("Please, provide a file.")
    file_name = sys.argv[1]

    result1 = []

    with open(file_name, "r") as in_file:
        for line in in_file:
            if count_dots(line) > 1:
                result1.extend(re.split(pattern=r"(?<=\S{5}\.) ", string=line))
            else:
                result1.append(line)

    result2 = []

    for line in result1:
        if count_dots(line) > 1:
            result2.extend(split_by_end_short_words(line))
        else:
            result2.append(line)

    with open(file=file_name + "split.txt", mode="w") as f:
        for line in result2:
            if line[-1] == "\n":
                f.write(line)
            else:
                f.write(line + "\n")
