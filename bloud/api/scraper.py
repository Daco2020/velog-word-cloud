import collections
import re

import requests

from bs4 import BeautifulSoup
from konlpy.tag import Komoran


JAVA_HOME = """/Library/Java/JavaVirtualMachines/
jdk1.8.0_333.jdk/Contents/Home/jre/lib/jli/libjli.dylib"""


async def fetch(session, url):
    with session.get(url) as response:
        return response.text


async def test_request(url):
    with requests.Session() as session:
        html_doc = await fetch(session, url)

    soup = BeautifulSoup(html_doc, "html.parser")
    soup.prettify()

    target_html = soup.find_all("div", "gVEHog")
    targets = [i.a.get("href") for i in target_html][:10]
    print(targets)
    nlps = []
    for target in targets:
        url = f"https://velog.io{target}"
        nlps += await test_request2(url)

    words = exclude_word(nlps)
    count_words = collections.Counter([i for i in words if len(i) > 1])
    result = sorted(count_words.items(), key=lambda x: x[1], reverse=True)[:50]
    return result


async def test_request2(url):
    with requests.Session() as session:
        html_doc = await fetch(session, url)

    soup = BeautifulSoup(html_doc, "html.parser")
    soup.prettify()

    target_html = soup.find("div", "atom-one")
    ko_arr = re.compile("[가-힣]+").findall(str(target_html))
    ko_str = " ".join(ko_arr)

    komo = Komoran(jvmpath=JAVA_HOME)
    nlp = komo.nouns(ko_str)
    print(nlp)
    return nlp


exclude_txt = """
니다,거지,지금,가요,라고,경우,가지,대부분,때문,먼저,
이번,출처,본인,우리,예제,하나,둘,셋,첫째,둘째,셋째,
다른,이후,아래,처음,소개,고려,자와,마다,파라,미터,
한참,이랑,우아,나중,하기,장님,분이,에다,보니,안와,
아하,이다,필요,
"""


def exclude_word(words):
    result = [word for word in words if word not in exclude_txt]
    return result
