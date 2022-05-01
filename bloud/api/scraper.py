# import requests
import requests

from bs4 import BeautifulSoup


def fetch(session, url):
    with session.get(url) as response:
        return response.text


def test_request(url):
    with requests.Session() as session:
        html_doc = fetch(session, url)

    soup = BeautifulSoup(html_doc, "html.parser")
    r = soup.prettify()

    return r
