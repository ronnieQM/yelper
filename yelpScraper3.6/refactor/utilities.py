from classes import ProcessedRequest, YelpBusineess, YelpReview


# grabber function
def requester(url: str) -> ProcessedRequest:
    """ Request page and return beautiful soup object"""

    original_url = url
    # clean the url, remove query params
    url = url.split('?', 1)[0]


