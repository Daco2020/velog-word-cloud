import collections
import re

import requests

from bs4 import BeautifulSoup
from konlpy.tag import Komoran


def fetch(session, url):
    with session.get(url) as response:
        return response.text


JAVA_HOME = "/Library/Java/JavaVirtualMachines/jdk1.8.0_333.jdk\
    /Contents/Home/jre/lib/jli/libjli.dylib"


def test_request(url):
    with requests.Session() as session:
        html_doc = fetch(session, url)

    soup = BeautifulSoup(html_doc, "html.parser")
    soup.prettify()

    target_html = soup.find("div", "atom-one")
    ko_arr = re.compile("[가-힣]+").findall(str(target_html))
    ko_str = " ".join(ko_arr)

    komoran = Komoran(jvmpath=JAVA_HOME)
    nlp = komoran.nouns(ko_str)
    count_nlp = collections.Counter(nlp)

    return sorted(count_nlp.items(), key=lambda x: x[1], reverse=True)
