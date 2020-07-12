import argparse
from classes import ProcessedRequest
from utilities import requester

# example = 'https://techgfi.com/discord-rtc-connecting/'
example = 'https://www.yelp.com/biz/dee-dussault-ganja-yoga-and-sex-coaching-los-angeles-2?osq=sex'

# TODO
# save ProcessedRequest class to system, so that you don't have to make a new request every time
# maybe save SOUP to html?

if __name__ == "__main__":
    # # accept url as argument from command line
    # argparser = argparse.ArgumentParser()
    # argparser.add_argument('url', help='yelp business page url')
    # args = argparser.parse_args()
    # url = args.url

    url = example

    y = requester(url)

    import pickle

    with open('sample_processed_request.pkl', 'wb') as file:
        pickle.dump(y, file)
