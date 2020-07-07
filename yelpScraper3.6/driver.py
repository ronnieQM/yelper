import argparse
import yelper_v3 as yelper

if __name__ == "__main__":
    # accept url as argument from command line
    argparser = argparse.ArgumentParser()
    argparser.add_argument('url', help='yelp business page url')
    args = argparser.parse_args()
    url = args.url

    #
    yelper.requester(url)
