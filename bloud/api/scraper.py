import collections
import re

import requests

from bs4 import BeautifulSoup


def fetch(session, url):
    with session.get(url) as response:
        return response.text


def test_request(url):
    with requests.Session() as session:
        html_doc = fetch(session, url)

    soup = BeautifulSoup(html_doc, "html.parser")
    soup.prettify()
    result = soup.find("div", "atom-one")
    string = re.compile("[가-힣]+").findall(str(result))
    print(string)
    dict = collections.Counter(string)
    print(dict)
    a = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    return a
