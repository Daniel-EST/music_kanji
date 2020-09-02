import requests
from bs4 import BeautifulSoup


def get_utamap_lyrics(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup.select('table tr .noprint')[0].get_text().strip()

# TODO ERROR PROTECTION
