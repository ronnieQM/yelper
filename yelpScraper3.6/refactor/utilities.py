from classes import ProcessedRequest
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests

# TODO
# add shit to make sure the response goes through
# verify (how to make sure that I'm getting the PROPER response)


# grabber function
def requester(url: str) -> ProcessedRequest:
    """ Request page and return a class with a beautiful soup object"""

    # clean the url, remove query params
    source_url = url
    url = url.split('?', 1)[0]  # remove query params
    domain = urlparse(url).netloc

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/53.0.2785.143 Safari/537.36'}
    page_response = requests.get(url, headers, timeout=10)
    soup = BeautifulSoup(page_response.content, "html.parser")
    try:
        title = soup.title.string
    except Exception as ex:
        print(ex)
        title = None

    return ProcessedRequest(source_url, url, domain, title, page_response, soup)
