"""
=================================================
HTML Parser
=================================================
Request HTML page to be parsed and return selected values as json.
"""

import json
import logging
from classes import ProcessedRequest, YelpBusiness, YelpReview

logging.basicConfig(filename='yelper.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)


class ProcessedRequest:
    def __init__(self, original_url, base_url, name, page_response, page_content):
        self.original_url = original_url,
        self.url = base_url,
        self.name = name,
        self.page_response = page_response,
        self.page_content = page_content


def yelper(processed_request: ProcessedRequest) -> json:
    """Takes in a request OBJECT, parses out values, returns JSON."""

    url_regex = r"([^\s]+)"
    phone_regex = r"((\(\d{3}\) ?)|(\d{3}-))?\d{3}-\d{4}"



    vals = {
        'business_name': "lemon--h1__373c0__2ZHSL heading--h1__373c0__1VUMO heading--no-spacing__373c0__1PzQP "
                         "heading--inline__373c0__1F-Z6",  # h1, class
        'avgRating1': "lemon--div__373c0__1mboc i-stars__373c0__3UQrn i-stars--large-4-half__373c0__1ya3H border-color--default__373c0__2oFDT overflow--hidden__373c0__8Jq2I",
        # div class aria-label
        'avgRating2': "lemon--div__373c0__1mboc i-stars__373c0__3UQrn i-stars--large-5__373c0__3f1bF border-color--default__373c0__2oFDT overflow--hidden__373c0__8Jq2I",
        'avgRating3': "lemon--div__373c0__1mboc i-stars__373c0__3UQrn i-stars--large-4__373c0__1Tgq2 border-color--default__373c0__2oFDT overflow--hidden__373c0__8Jq2I",
        'avgRating4': "lemon--div__373c0__1mboc i-stars__373c0__3UQrn i-stars--large-4__373c0__1Tgq2 border-color--default__373c0__MD4Lj overflow--hidden__373c0__3e6l4",
        'avgRating5': "lemon--div__373c0__1mboc i-stars__373c0__3UQrn i-stars--large-5__373c0__3f1bF border-color--default__373c0__MD4Lj overflow--hidden__373c0__3e6l4",
        'numOfRatings': "lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--mid__373c0__3G312 text-align--left__373c0__2pnx_ text-size--large__373c0__1568g",
        # p, text,
        'webPhoneBlock': "lemon--div__373c0__1mboc island__373c0__3fs6U u-padding-t1 u-padding-r1 u-padding-b1 u-padding-l1 border--top__373c0__19Owr border--right__373c0__22AHO border--bottom__373c0__uPbXS border--left__373c0__1SjJs border-color--default__373c0__2oFDT background-color--white__373c0__GVEnp",
        'phoneNum0': "lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--left__373c0__2pnx_",
        'mainBlockClass': "lemon--div__373c0__1mboc sidebarActionsHoverTarget__373c0__2kfhE arrange__373c0__UHqhV gutter-12__373c0__3kguh grid__373c0__29zUk layout-stack-small__373c0__3cHex border-color--default__373c0__2oFDT",
        # div
        'commentClass ': "lemon--p__373c0__3Qnnj text__373c0__2pB8f comment__373c0__3EKjH "
                         "text-color--normal__373c0__K_MKN text-align--left__373c0__2pnx_",  # p
        'userClass': "lemon--span__373c0__3997G text__373c0__2pB8f fs-block text-color--inherit__373c0__w_15m text-align--left__373c0__2pnx_ text-weight--bold__373c0__3HYJa",
        'userClass1': "lemon--a__373c0__IEZFH link__373c0__29943 link-color--inherit__373c0__15ymx link-size--inherit__373c0__2JXk5",
        # a
        'userCityClass': "lemon--span__373c0__3997G text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--left__373c0__2pnx_ text-weight--bold__373c0__3HYJa text-size--small__373c0__3SGMi",
        # span
        'ratingDateClass': "lemon--div__373c0__1mboc arrange__373c0__UHqhV gutter-6__373c0__zqA5A vertical-align-middle__373c0__2TQsQ border-color--default__373c0__2oFDT",
        # class
        'ratingDateClass0': "lemon--span__373c0__3997G text__373c0__2pB8f text-color--mid__373c0__3G312 text-align--left__373c0__2pnx_",
        'outterRatingSpan': "lemon--span__373c0__3997G display--inline__373c0__1DbOG border-color--default__373c0__2oFDT",
        'addressBlockClass': "lemon--div__373c0__1mboc u-padding-t2 u-padding-r2 u-padding-b2 u-padding-l2 border-color--default__373c0__2oFDT",
        # div
        'webPhoneDirBlockClass': "lemon--div__373c0__1mboc island__373c0__3fs6U u-padding-t1 u-padding-r1 u-padding-b1 u-padding-l1 border--top__373c0__19Owr border--right__373c0__22AHO border--bottom__373c0__uPbXS border--left__373c0__1SjJs border-color--default__373c0__2oFDT background-color--white__373c0__GVEnp",
        # div
        'addressClass': "lemon--span__373c0__3997G",  # span
        'locatedIn': "lemon--a__373c0__IEZFH link__373c0__29943 link-color--blue-dark__373c0__1mhJo link-size--inherit__373c0__2JXk5",
        # a
        'amenitiesBlockClass': "lemon--div__373c0__1mboc arrange__373c0__UHqhV gutter-12__373c0__3kguh layout-wrap__373c0__34d4b layout-2-units__373c0__3CiAk border-color--default__373c0__2oFDT",
        # div
        'amenitiesDictionaryClass': "lemon--div__373c0__1mboc arrange-unit__373c0__1piwO arrange-unit-fill__373c0__17z0h border-color--default__373c0__2oFDT",
        # class
        'categoriesBlockClass': "lemon--div__373c0__1mboc arrange-unit__373c0__1piwO arrange-unit-fill__373c0__17z0h border-color--default__373c0__2oFDT",
        # div
        'categoriesBlockClass': "lemon--span__373c0__3997G display--inline__373c0__1DbOG u-space-r1 border-color--default__373c0__2oFDT"
        # div
    }

    # regex, for validation
    return json(YelpBusiness)
