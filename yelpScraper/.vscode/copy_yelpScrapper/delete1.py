class Review:
    def __int__(self):
        self.user = None
        self.location = None
        self.comment = None
        self.rating = None
        self.datePosted = None
        self.count = 0

    def __str__(self):
        print("something")
        return "somehting"

    def __repr__(self):
        print("TODO")

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

    def allReviews(self):
        print("All Reviews_")
        return "All Reviews"

    def __str__(self):
        return "ID: {},\nURL: {}, \nName: {},\nAddress: {},\nNumber of Reviews: {}, \nAverage Rating: {}, \nPhone: {}, \nWebsite: {}, \nCategories: {}, \nAmenities: {}".format(self.id, self.url, self.name, self.address, self.numReviews, self.avgRating, self.phone, self.website, self.categories, self.amenities)

    def __repr__(self):
        return "TODO"

test = Business()
aReview = Review()
aReview.user = "John"
aReview.location = "Los Angeles"
bReview = Review()
bReview.user = "bUser"

test.reviews.append(aReview)

print("something")
test.allReviews()
