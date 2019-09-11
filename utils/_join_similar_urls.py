#!/usr/bin/env python3
#
# script to parse xml files with texts in 2 langualges.
# input: 2 xml files with crawled text in 2 languguages
# xml structure:
# <items>
# <item>
#     <url>...</url>
#     <section>...</section>
#     <title>
#         <value>...</value>
#         ...
#     </title>
#     <date-time>...</date-time>
#     <text>
#         <value>...</value>
#         <value>...</value>
#         ...
#     </text>
# </item>

# output: an xml file which combines parts in 2 languages from the same source (with respect to language versions)
# output: the same with separate files for each "document"

# docstring for docopt
"""join_similar_urls.py

Usage:
    join_similar_urls.py --input1 <xml_file_1> --input2 <xml_file_2> [(-o | --output) <output_file>] ((-s | --single) | (-m | --multiple))
    join_similar_urls.py (-h | --help)
    join_similar_urls.py (-v | --version)

Options:
    --input1        path to the first xml file
    --input2        path to the second xml file
    -o --output     (optional) path to the output file
    -s --single     if used, output will be saved in a single file
    -m --multiple   if used, output will be saved in separate files, one for each "document"
    -v --version    Show version.
    -h --help       Show this screen.
"""

# TODO сделать --single атрибутом по умолчанию

from docopt import docopt
import xml.etree.ElementTree as ET
import re


def is_similar_urls(url_1: str, url_2: str) -> bool:
    """
    Checks if url_1 is similar to url_2.
    As if they are different language versions of the same page.
    """
    # check urls from primeminister.kz
    if "primeminister.kz" in url_1:
        # reverse urls so they are easier to compare
        reversed_url_1 = url_1[::-1]
        reversed_url_2 = url_2[::-1]
        # take only the last part of the url (from the last '/' until the end)
        sub_url_1 = re.match("^.+?/", reversed_url_1).group(0)
        sub_url_2 = re.match("^.+?/", reversed_url_2).group(0)
        if sub_url_1 == sub_url_2:
            return True

    # if all checks failed
    return False


def save_items_into_nth_file(
    file_number: int, xml_piece_1: ET.Element, xml_piece_2: ET.Element, file_name: str
) -> None:
    """
    Saves privided pieces of xml into a new (nubered) file as a pair.
    """
    # combine a pair of xml pieces provided
    root = ET.Element("pair")
    root.append(xml_piece_1)
    root.append(xml_piece_2)
    # convert the pair into a tree
    tree = ET.ElementTree(root)
    # build an output file name
    dot_ind = file_name.rfind(".")
    new_file_name = file_name[:dot_ind] + "-" + str(file_number) + ".xml"
    # write the result int a file
    tree.write(file_or_filename=new_file_name, encoding="utf-8")


def main():
    # get data from arguments
    # import first xml file
    xml_file_1 = arguments["<xml_file_1>"]
    xml_1 = ET.parse(source=xml_file_1)
    xml_1_root = xml_1.getroot()

    # import second xml file
    xml_file_2 = arguments["<xml_file_2>"]
    xml_2 = ET.parse(source=xml_file_2)
    xml_2_root = xml_2.getroot()

    # get output file from arguments
    if arguments["--output"] == True:
        output_file = arguments["<output_file>"]
    else:
        output_file = "out.xml"

    # get output mode from arguments
    if arguments["--multiple"] == True:
        output_mode = "multiple files"
        # a variable for counting multiple output files
        output_file_number = 0
    elif arguments["--single"] == True:
        output_mode = "single file"

    output_root = ET.Element("pairs")
    # look for similar urls in 2 xml files
    for item_in_file_1 in xml_1_root:
        for item_in_file_2 in xml_2_root:
            # if urls are similar
            if is_similar_urls(
                url_1=item_in_file_1[0].text, url_2=item_in_file_2[0].text
            ):
                # if single file option is set
                if output_mode == "multiple files":
                    # save a document into a new file
                    save_items_into_nth_file(
                        file_number=output_file_number,
                        xml_piece_1=item_in_file_1,
                        xml_piece_2=item_in_file_2,
                        file_name=output_file,
                    )
                    output_file_number += 1

                # if multiple file option is set
                elif output_mode == "single file":
                    # add item pairs to the root element
                    # create a new pair
                    pair = ET.Element("pair")
                    pair.append(item_in_file_1)
                    pair.append(item_in_file_2)
                    # appens the new pair to the output_root
                    output_root.append(pair)

    # if multiple file option is set
    if output_mode == "single file":
        # convert output_root into a tree
        tree = ET.ElementTree(output_root)
        # write the result int a file
        tree.write(file_or_filename=output_file, encoding="utf-8")


if __name__ == "__main__":
    arguments = docopt(__doc__, version="join_similar_urls.py v.0.1")
    main()
