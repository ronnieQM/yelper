from bs4 import BeautifulSoup as Soup
import requests
import argparse
import sys
import json
import os
import uuid
import types
import csv
from lxml.html import fromstring
import requests
from itertools import cycle
import traceback

# proxies = {
#     "http": 'http://196.52.80.123:80', 
#     "https": '72.35.40.34:8080',
# }

proxies = get_proxies()
proxy_pool = cycle(proxies)

def getyelp(url):
    print(url)
    page_response = requests.get(url,proxies=proxies)
    page_content = Soup(page_response.content, "html.parser")

    print('-'*10)
    print("'page_response' is of type:")
    print(type(page_response))
    print('-'*10)

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            #Grabbing IP and corresponding PORT
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('url', help='whats the url')
    args = argparser.parse_args()
    url = args.url
    getyelp(url)

    print('script finished')