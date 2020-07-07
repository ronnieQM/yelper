import json


class YelpBusiness:
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

    def all_reviews(self):
        # TODO
        return "All Reviews"

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

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


class YelpReview:
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


class ProcessedRequest:
    def __init__(self, source_url, base_url, co, title, page_response, page_content):
        self.source_url = source_url,
        self.url = base_url,
        self.company = co,
        self.page_title = title,
        self.page_response = page_response,
        self.page_content = page_contentk

    def __str__(self):
        return f"""
        source_url: {self.source_url},
        base_url: {self.base_url},
        company: {self.company},
        page_title: {self.page_title}:
        page_response = {type(self.page_response)}
        page_content = {type(self.page_content)}
        """
