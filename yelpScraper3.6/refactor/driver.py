import argparse
from classes import ProcessedRequest
from utilities import requester

example = 'https://www.redfin.com/mortgage-rates'

if __name__ == "__main__":
    # # accept url as argument from command line
    # argparser = argparse.ArgumentParser()
    # argparser.add_argument('url', help='yelp business page url')
    # args = argparser.parse_args()
    # url = args.url

    url = example

    import pickle
    y = requester(url)
    print(type(y))
    print(y)

