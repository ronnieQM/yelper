from classes import ProcessedRequest


# grabber function
def requester(url: str) -> ProcessedRequest:
    """ Request page and return beautiful soup object"""

    # clean the url, remove query params
    source_url = url
    url = url.split('?', 1)[0]

    # initialize BS4
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/53.0.2785.143 Safari/537.36'}

    x = ProcessedRequest(source_url, url, 'NONE', title, page_response, page_contenct)
    return x


