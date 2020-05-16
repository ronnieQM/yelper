import math
from bs4 import BeautifulSoup
import time, requests
 
start = time.time()
# numOfRatings = "lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--mid__373c0__3G312 text-align--left__373c0__2pnx_ text-size--large__373c0__1568g"  # p, text
numOfRatings = "lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--mid__373c0__jCeOG text-align--left__373c0__2XGa- text-size--large__373c0__3t60B"  # p, text
urls = [
    'https://www.yelp.com/biz/technibility-cell-phone-repair-glendale-3?start=320',
    'https://www.yelp.com/biz/iprotech-glendale-6?page_src=related_bizes',
    'https://www.yelp.com/biz/ifone-repair-service-glendale-21?page_src=related_bizes',
]
z = 'https://www.yelp.com/biz/technibility-cell-phone-repair-glendale-3?start=320'

def allPages(x, base=20):
    return (base * round(x/base)) + 20
def atest(url):
    print('rats')
    allURLs = []
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
    url = url.split('?', 1)[0]
    page_response = requests.get(url, headers, timeout=10)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    print('ping')
    # title = page_content.find('h1', attrs={"class": businessName}).text
    print(type(page_content))
    numberOfReviews = page_content.find('p', attrs={"class": numOfRatings}).text
    print(numberOfReviews)
    numReviews = [int(i) for i in numberOfReviews.split() if i.isdigit()][0]
    x = allPages(numReviews)
    for i in range(20, x, 20):
        allURLs.append(i)
        print(url + '?start=' + str(i))
    for i in allURLs:
        print(i)
    print('complete')

atest(z)

end = time.time()
print('... '*20)
print(end - start)
print('... '*20)

    




