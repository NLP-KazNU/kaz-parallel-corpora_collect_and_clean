#!/usr/bin/env python3

# read eng news urls
# for each url:
# get url, section, title, date-time, text
# save as an xml-file
# find link to kaz news
# get url, section, title, date-time, text
# save as a similar xml-file

import sys
from requests_html import HTMLSession
from typing import Tuple
from xml.dom import minidom

session = HTMLSession()


def get_data_from_url(req: object, url: str) -> Tuple[str, str, str, str]:
    """
    #TODO
    """
    selector_section = ".wrapper"
    selector_title = ".media-title"
    selector_date_time = ".date"
    selector_text = ".text p"

    section = " ".join([x.text for x in req.html.find(selector=selector_section)])
    title = " ".join([x.text for x in req.html.find(selector=selector_title)])
    date_time = " ".join([x.text for x in req.html.find(selector=selector_date_time)])
    text = "\n".join([x.text for x in req.html.find(selector=selector_text)])

    return (section, title, date_time, text)


def save_data_as_xml(
    file_name: str, url: str, section: str, title: str, date_time: str, text: str
) -> None:
    """
    #TODO
    """
    doc = minidom.Document()

    root = doc.createElement("root")
    doc.appendChild(root)

    url_tag = doc.createElement("url")
    url_text = doc.createTextNode(url)
    url_tag.appendChild(url_text)
    root.appendChild(url_tag)

    section_tag = doc.createElement("section")
    section_text = doc.createTextNode(section)
    section_tag.appendChild(section_text)
    root.appendChild(section_tag)

    title_tag = doc.createElement("title")
    title_text = doc.createTextNode(title)
    title_tag.appendChild(title_text)
    root.appendChild(title_tag)

    date_time_tag = doc.createElement("date_time")
    date_time_text = doc.createTextNode(date_time)
    date_time_tag.appendChild(date_time_text)
    root.appendChild(date_time_tag)

    text_tag = doc.createElement("text")
    text_text = doc.createTextNode(text)
    text_tag.appendChild(text_text)
    root.appendChild(text_tag)

    xml_str = doc.toprettyxml(indent="  ")

    with open(file_name, "w") as f:
        f.write(xml_str)


# read eng news urls
# for each url:
output_file_number = 0

# for eng_url in sys.stdin:
with open("./akorda_kz/news_urls.en", "r") as in_f:
    for eng_url in in_f:
        # get eng section, title, date-time, text, kaz_url
        r = session.get(eng_url.strip())
        (eng_sec, eng_tit, eng_dat, eng_txt) = get_data_from_url(r, eng_url)

        # save as an xml-file
        eng_output_file_name = str(output_file_number) + "-eng.xml"
        save_data_as_xml(
            eng_output_file_name, eng_url.strip(), eng_sec, eng_tit, eng_dat, eng_txt
        )

        # find link to kaz news
        selector_kaz_url = "a[hreflang=kz]"
        kaz_url = (
            "http://www.akorda.kz"
            + r.html.find(selector=selector_kaz_url, first=True).attrs["href"]
        )

        # get kaz section, title, date-time, text
        r = session.get(kaz_url.strip())
        (kaz_sec, kaz_tit, kaz_dat, kaz_txt) = get_data_from_url(r, kaz_url)

        # save as a similar xml-file
        kaz_output_file_name = str(output_file_number) + "-kaz.xml"
        save_data_as_xml(
            kaz_output_file_name, kaz_url.strip(), kaz_sec, kaz_tit, kaz_dat, kaz_txt
        )
        output_file_number += 1
