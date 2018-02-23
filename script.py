#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests

with open('sitemap.xml', 'rb') as f:
    sitemap = f.read()
    soup = BeautifulSoup(sitemap, 'lxml')
    urls = soup.find_all('loc')

    for index, url in enumerate(urls):
        print("{} / {} {}".format(index + 1, len(urls), url.text))
        requests.get(url.text)

