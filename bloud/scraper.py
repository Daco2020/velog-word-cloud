import collections
import re

from bs4 import BeautifulSoup
from konlpy.tag import Komoran
from requests import Session

from bloud.constant import EXCLUDE_TXT, JAVA_HOME, VELOG_URL_PREFIX


async def scraping_velog(id: str, limit: int) -> list:
    url = VELOG_URL_PREFIX + id
    with Session() as session:
        html_doc = await fetch(session, url)

    soup = BeautifulSoup(html_doc, "html.parser")
    soup.prettify()

    target_html = soup.find_all("div", "gVEHog")
    targets = [tag.a.get("href") for tag in target_html][:10]
    nlps = []
    for target in targets:
        url = f"https://velog.io{target}"
        nlps += await extract_nlp(url)

    words = exclude_word(nlps)
    return sort_by_count(words)[:limit]


async def extract_nlp(url: str) -> list:
    with Session() as session:
        html_doc = await fetch(session, url)

    soup = BeautifulSoup(html_doc, "html.parser")
    soup.prettify()

    target_html = soup.find("div", "atom-one")
    ko_arr = re.compile("[가-힣]+").findall(str(target_html))
    ko_str = " ".join(ko_arr)

    komo = Komoran(jvmpath=JAVA_HOME)
    nlp = komo.nouns(ko_str)
    return nlp


async def fetch(session: Session, url: str) -> str:
    with session.get(url) as response:
        return response.text


def exclude_word(words: list) -> list:
    return [word for word in words if word not in EXCLUDE_TXT]


def sort_by_count(words: list) -> list:
    count_words = collections.Counter([word for word in words if len(word) > 1])
    return sorted(count_words.items(), key=lambda x: x[1], reverse=True)
