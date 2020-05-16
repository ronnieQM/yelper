from flask import Flask, request, Response
from bs4 import BeautifulSoup
import requests
import argparse
import sys
import json
import os
import uuid
import types
from random import choice
import random

import re
import logging
from multiprocessing import Pool


businessName = "lemon--h1__373c0__2ZHSL heading--h1__373c0__1VUMO heading--no-spacing__373c0__1PzQP heading--inline__373c0__1F-Z6"  # h1, class
avgRating1 = "lemon--div__373c0__1mboc i-stars__373c0__3UQrn i-stars--large-4-half__373c0__1ya3H border-color--default__373c0__2oFDT overflow--hidden__373c0__8Jq2I"  # div class aria-label
avgRating2 = "lemon--div__373c0__1mboc i-stars__373c0__3UQrn i-stars--large-5__373c0__3f1bF border-color--default__373c0__2oFDT overflow--hidden__373c0__8Jq2I"
avgRating3 = "lemon--div__373c0__1mboc i-stars__373c0__3UQrn i-stars--large-4__373c0__1Tgq2 border-color--default__373c0__2oFDT overflow--hidden__373c0__8Jq2I"
avgRating4 = "lemon--div__373c0__1mboc i-stars__373c0__3UQrn i-stars--large-4__373c0__1Tgq2 border-color--default__373c0__MD4Lj overflow--hidden__373c0__3e6l4"
avgRating5 = "lemon--div__373c0__1mboc i-stars__373c0__3UQrn i-stars--large-5__373c0__3f1bF border-color--default__373c0__MD4Lj overflow--hidden__373c0__3e6l4"
numOfRatings = "lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--mid__373c0__3G312 text-align--left__373c0__2pnx_ text-size--large__373c0__1568g"  # p, text
webPhoneBlock = "lemon--div__373c0__1mboc island__373c0__3fs6U u-padding-t1 u-padding-r1 u-padding-b1 u-padding-l1 border--top__373c0__19Owr border--right__373c0__22AHO border--bottom__373c0__uPbXS border--left__373c0__1SjJs border-color--default__373c0__2oFDT background-color--white__373c0__GVEnp"
phoneNum0 = "lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--left__373c0__2pnx_"
mainBlockClass = "lemon--div__373c0__1mboc sidebarActionsHoverTarget__373c0__2kfhE arrange__373c0__UHqhV gutter-12__373c0__3kguh grid__373c0__29zUk layout-stack-small__373c0__3cHex border-color--default__373c0__2oFDT"  # div
commentClass = "lemon--p__373c0__3Qnnj text__373c0__2pB8f comment__373c0__3EKjH text-color--normal__373c0__K_MKN text-align--left__373c0__2pnx_"  # p
userClass = "lemon--span__373c0__3997G text__373c0__2pB8f fs-block text-color--inherit__373c0__w_15m text-align--left__373c0__2pnx_ text-weight--bold__373c0__3HYJa"
userClass1 = "lemon--a__373c0__IEZFH link__373c0__29943 link-color--inherit__373c0__15ymx link-size--inherit__373c0__2JXk5"  # a
userCityClass = "lemon--span__373c0__3997G text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--left__373c0__2pnx_ text-weight--bold__373c0__3HYJa text-size--small__373c0__3SGMi"  # span
ratingDateClass = "lemon--div__373c0__1mboc arrange__373c0__UHqhV gutter-6__373c0__zqA5A vertical-align-middle__373c0__2TQsQ border-color--default__373c0__2oFDT"  # class
ratingDateClass0 = "lemon--span__373c0__3997G text__373c0__2pB8f text-color--mid__373c0__3G312 text-align--left__373c0__2pnx_"
outterRatingSpan = "lemon--span__373c0__3997G display--inline__373c0__1DbOG border-color--default__373c0__2oFDT"
addressBlockClass = "lemon--div__373c0__1mboc u-padding-t2 u-padding-r2 u-padding-b2 u-padding-l2 border-color--default__373c0__2oFDT"  # div
webPhoneDirBlockClass = "lemon--div__373c0__1mboc island__373c0__3fs6U u-padding-t1 u-padding-r1 u-padding-b1 u-padding-l1 border--top__373c0__19Owr border--right__373c0__22AHO border--bottom__373c0__uPbXS border--left__373c0__1SjJs border-color--default__373c0__2oFDT background-color--white__373c0__GVEnp"  # div
addressClass = "lemon--span__373c0__3997G"  # span
locatedIn = "lemon--a__373c0__IEZFH link__373c0__29943 link-color--blue-dark__373c0__1mhJo link-size--inherit__373c0__2JXk5"  # a
amenitiesBlockClass = "lemon--div__373c0__1mboc arrange__373c0__UHqhV gutter-12__373c0__3kguh layout-wrap__373c0__34d4b layout-2-units__373c0__3CiAk border-color--default__373c0__2oFDT"  # div
amenitiesDictionaryClass = "lemon--div__373c0__1mboc arrange-unit__373c0__1piwO arrange-unit-fill__373c0__17z0h border-color--default__373c0__2oFDT"  # class
categoriesBlockClass = "lemon--div__373c0__1mboc arrange-unit__373c0__1piwO arrange-unit-fill__373c0__17z0h border-color--default__373c0__2oFDT"  # div
categoriesBlockClass = "lemon--span__373c0__3997G display--inline__373c0__1DbOG u-space-r1 border-color--default__373c0__2oFDT"  # div

wwwRegex = "([^\s]+)"
phoneRegex = "((\(\d{3}\) ?)|(\d{3}-))?\d{3}-\d{4}"

logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')


app = Flask(__name__)
# cors = CORS(app)


class Business:
    def __init__(self):
        self.id = None
        self.url = None
        self.name = None
        self.avgRating = None
        self.numReviews = None
        self.phone = None
        self.address = None
        self.website = None
        self.categories = None
        self.amenities = None
        self.reviews = []
        self.reviewCount = 0

    def allReviews(self):
        return "All Reviews"

    def toJSON(self):
        return 'this is a test'

    def __str__(self):
        return "ID: {},\nURL: {}, \nName: {},\nAddress: {},\nNumber of Reviews: {}, \nAverage Rating: {}, \nPhone: {}, \nWebsite: {}, \nCategories: {}, \nAmenities: {}, \nReviews: {}".format(self.id, self.url, self.name, self.address, self.numReviews, self.avgRating, self.phone, self.website, self.categories, self.amenities, len(self.reviews))

    def __repr__(self):
        # TODO
        return "something?"


class Review:
    def __int__(self):
        self.user = None
        self.location = None
        self.comment = None
        self.rating = None
        self.datePosted = None

    def __str__(self):
        return "\nUser: {}, \nCity: {}, \nDate: {}, \nRating: {}, \nComment:{}".format(self.user, self.location, self.datePosted, self.rating, self.comment)
        # print(self.user, self.location, self.datePosted, self.rating, self.comment)

    def __repr__(self):
        # print(self.user, self.location, self.datePosted, self.rating, self.comment)
        print("\nUser: {}, \nCity: {}, \nDate: {}, \nRating: {}, \nComment:{}".format(
            self.user, self.location, self.datePosted, self.rating, self.comment))


def funct(url):
    start = time.time()
    bizObject = Business()
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    html = None

    # initialize BS4
    print("\n\n\nATTEMPTING TO REQUEST PAGE...")
    baseUrl = url.split('?', 1)[0]
    url = baseUrl
    #### ADD RETRY LOGIC HERE
    ########## TODO RETY LOGIC
    ########## Basically, if title is NONE, then use PROXY and retry
    try: 
        page_response = requests.get(url, headers, timeout=10)
    except Exception as ex:
        print(str(ex))
        
    page_content = BeautifulSoup(page_response.content, "html.parser")
    print("SUCCESSFUL PAGE RESPONSE FROM: {}".format(url))

    # !ID!
    # generate ID
    id = random.randint(1, 10000)

    # begin grabbing content, 1st page
    # !Title!
    title = page_content.find('h1', attrs={"class": businessName}).text

    # !Address!
    addressblock = page_content.find('div', attrs={"class": addressBlockClass})
    addresses = addressblock.find_all('span', attrs={"class": addressClass})
    address = ""
    for i in addresses:
        address = address + i.text + "$ "

    numberOfReviews = page_content.find(
        'p', attrs={"class": numOfRatings}).text
    numReviews = [int(i) for i in numberOfReviews.split() if i.isdigit()][0]

    # !Average Rating!
    avgRate = None

    # !Phone!
    webPhoneDirBlock = page_content.find(
        'div', attrs={"class": webPhoneDirBlockClass})
    phoneWWW = webPhoneDirBlock.find_all('p', attrs={"class": phoneNum0})
    phone = re.search(phoneRegex, str(phoneWWW)).group(0)
    try:
        www = webPhoneDirBlock.find('a', attrs={"role": "link"}).text
    except Exception as ex:
        print('ERROR:', ex)
        www = None

    # !Amenities!
    amenitiesBlock = page_content.find(
        'div', attrs={"class": amenitiesBlockClass})
    amenitiesDictionary = amenitiesBlock.find_all(
        'div', attrs={"class": amenitiesDictionaryClass})
    amenities = {}
    for i in amenitiesDictionary:
        temp = i.findAll('span')
        amenities.update({temp[0].text: temp[1].text.replace(u'\xa0', u' ')})

    # !Categories!
    categories = {}
    categoryBlock = page_content.find(
        'div', attrs={"class": categoriesBlockClass})

    # !Comments! FIRST PAGE
    mainBlocks = page_content.findAll(
        'div', attrs={"class": mainBlockClass})  # find all review blocks
    for i in mainBlocks:
        review = Review()
        try:
            userName = i.find(
                'span', attrs={"class": userClass}).text  # user name
            review.user = userName
        except Exception as ex:
            pass
            # print("userClass 1 not found.")
        try:
            userName = i.find(
                'a', attrs={"class": userClass1}).text  # user name
            review.user = userName
        except Exception as ex:
            pass
            # print("UserClass 2 not found")

        review.comment = i.find(
            'p', attrs={"class": commentClass}).text  # comment
        review.location = i.find(
            'span', attrs={"class": userCityClass}).text  # user city

        ratingDateBlock = i.find('div', attrs={"class": ratingDateClass})
        for j in ratingDateBlock:
            try:
                review.datePosted = j.find(
                    'span', attrs={"class": ratingDateClass0}).text
            except:
                pass
            try:
                rating = j.find('div', attrs={"role": "img"})["aria-label"]
                review.rating = [int(i)
                                 for i in rating.split() if i.isdigit()][0]
            except:
                pass
        bizObject.reviews.append(review)

    bizObject.id = id
    bizObject.url = baseUrl
    bizObject.name = title
    bizObject.address = address
    bizObject.numReviews = numReviews
    bizObject.avgRating = avgRate
    bizObject.phone = phone
    bizObject.website = www
    bizObject.amenities = amenities
    # TODO: add amenities to object

    # !Comments! ALL PAGES
    print("SUCCESSFUL PAGE SCRAPING: PAGE 1")
    print(" ")
    print("\n\n\nBEGIN PAGINATION SCRAPRING")

    p = 20
    while True:
        pageCount = p/20 + 1
        newUrl = (url + "?start={}".format(p))
        print("!~!~"*20)
        print("ATTEMPTING TO SCRAPE PAGE {}:\n{}".format(str(pageCount), newUrl))
        try:
            page_response = requests.get(newUrl, timeout=5)
            page_content = BeautifulSoup(page_response.content, "html.parser")
            mainBlocks = page_content.findAll(
                'div', attrs={"class": mainBlockClass})
            print(type(mainBlocks))
            print("SUCCESSFULL PAGE({}) RESPONSE".format(str(pageCount)))
            print("~!~!"*20)
            p += 20
            # sleep(10)
            # this IF is what makes sure that the WHILE ends eventually
            if mainBlocks:
                print("BEGIN: IN MAINBLOCK")
                for i in mainBlocks:
                    review = Review()
                    try:
                        userName = i.find('span', attrs={"class": userClass}).text  # user name
                        review.user = userName
                    except Exception as ex:
                        print("ERROR:",ex)
                        print('DID NOT FIND USER NAME 0')
                        pass
                    try:
                        userName = i.find('a', attrs={"class": userClass1}).text  # user name
                        review.user = userName
                    except Exception as ex:
                        print("ERROR:",ex)
                        print('DID NOT FIND USER NAME 1')
                        pass

                    review.comment = i.find('p', attrs={"class": commentClass}).text  # comment
                    review.location = i.find('span', attrs={"class": userCityClass}).text  # user city

                    ratingDateBlock = i.find('div', attrs={"class": ratingDateClass})
                    for j in ratingDateBlock:
                        try:
                            review.datePosted = j.find(
                                'span', attrs={"class": ratingDateClass0}).text
                        except:
                            pass
                        try:
                            rating = j.find('div', attrs={"role": "img"})[
                                "aria-label"]
                            review.rating = [
                                int(i) for i in rating.split() if i.isdigit()][0]
                        except:
                            pass
                    bizObject.reviews.append(review)
                    print('END: IN MAINBLOCK')
                    print("~!~!"*20)
            else:
                break
        except:
            print("!"*30)

    bizObject.reviewCount = len(bizObject.reviews)
    print("VIEW OF COMMENTS:")
    print("- "*20)
    for x in bizObject.reviews:
        print(x)
    print(bizObject)
    type(bizObject)
    print("- "*20)
    bizDictionary = {
        'id': bizObject.id,
        'Business Name': bizObject.name,
        'url': bizObject.url,
        'average rating': bizObject.avgRating,
        'number of reviews': bizObject.numReviews,
        'number of scraped reviews': bizObject.reviewCount,
        'address': bizObject.address,
        'phone': bizObject.phone,
        'website': bizObject.website,
        'reviews': {}
    }
    x = 0
    for i in bizObject.reviews:
        bizDictionary['reviews'].update({
            x: {
                'user': i.user,
                'rating': i.rating,
                'location': i.location,
                'date posted': i.datePosted,
                'comment': i.comment,
            }
        })
        x += 1

    # id: None, user: {}, city: {}, comment,{}, rating: {}
    end = time.time()
    print('... '*20)
    print(end - start)
    print('... '*20)
    return bizDictionary


@app.route("/", methods=["GET", "POST"])
def index():
    # print(request.form)
    # return json.dumps(request.form)
    # return json.dumps({"key": 3})
    # return request.args.get("url")
    # url = request.args.get("url")
    # return Response("Hello, Zappa")
    # return "happy test"
    # test = funct(request.form["url"])
    # if request.method == 'POST':
    if request.args.get('url'):
        yelperResult = funct(request.args.get("url"))
        return Response(json.dumps(yelperResult), mimetype='application/json')
    return '''
            Welcome to YELPER! Please view our documentation at {TODO}.<hr><br> Built by <a href='https://github.com/ronnieQM'>Ronnie.</a>
                '''


if __name__ == "__main__":
    app.run(debug=True)
