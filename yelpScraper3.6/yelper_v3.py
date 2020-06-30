"""
=================================================
HTML Parser
=================================================
Request HTML page to be parsed and return selected values as json.
"""

from bs4 import BeautifulSoup
import requests
import logging
import json
import os


# config settings
logging.basicConfig(filename='yelper.log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)


# regex, for validation
url_regex = r"([^\s]+)"
phone_regex = r"((\(\d{3}\) ?)|(\d{3}-))?\d{3}-\d{4}"

# define values, html
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



# define model(s)
# TODO
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
        # TODO
        return "All Reviews"

    def toJSON(self):
        # TODO
        # do I need to do this, even? or can I just call json() on Business.
        return 'this is a test'

    def __str__(self):
        # TODO
        return f"""
        ID: {self.id},
        URL: {self.url}, 
        Name: {self.name},
        Address: {self.address},
        Number of Reviews: {self.numReviews},
        Average Rating: {self.avgRating},
        Phone: {self.phone},
        Website: {self.website}, 
        Categories: {self.categories}, 
        Amenities: {self.amenities}, 
        Reviews: {len(self.reviews)}"""

    def __repr__(self):
        # TODO
        return "something?"
        
class Review:
    def __init__(self):
        self.user = None
        self.location = None
        self.comment = None
        self.rating = None
        self.datePosted = None

    def __str__(self):
        return f"""
        User: {self.user},
        City: {self.location},
        Date: {self.datePosted},
        Rating: {self.rating},
        Comment: {self.comment},
        """

    def __repr__(self):
        # print(self.user, self.location, self.datePosted, self.rating, self.comment)
        print("\nUser: {}, \nCity: {}, \nDate: {}, \nRating: {}, \nComment:{}".format(
            self.user, self.location, self.datePosted, self.rating, self.comment))

class Processed_Request:
    def __int__(self, url, name, pr, pc):
        self.url = url, 
        self.name = name,  
        # self.date
        self.page_respone = pr
        self.page_content = pc


# grabber function

def requester(url: str) -> Processed_Request:
    """ Request page and return beautiful soup object"""
    # initialize BS4
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

    print("\n\n\nATTEMPTING TO REQUEST PAGE...")
    url = url.split('?', 1)[0]
    
    try: 
        page_response = requests.get(url, headers, timeout=10)
    except Exception as ex:
        print(str(ex))
    page_content = BeautifulSoup(page_response.content, "html.parser")
    title = page_content.find('h1', attrs={"class": businessName}).text
    
    return Processed_Request(url, title, page_response, page_content)

def grabber(url: str) -> dict:
    """Parse HTML and return json object."""

    print(url)
    
    return 'JSON'

