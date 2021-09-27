from requests import get
from bs4 import BeautifulSoup

def raspagem(site):
    site = get(site)
    tags = BeautifulSoup(site.text, "html5lib")
    title = tags.find("title")
    return title.text
