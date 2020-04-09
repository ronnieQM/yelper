
# baseUrl = "https://www.yelp.com/biz/technibility-cell-phone-repair-glendale-3?"
# i = 20
# for j in range(16):
#     test = (baseUrl + "?start={}".format(i))
#     print(test)
#     pageCount = i/20 + 1
#     i += 20
#     print(pageCount)


testURL = "https://www.yelp.com/biz/ubreakifix-glendale?page_src=related_bizes"
print(testURL)

# sep = '?'
url = testURL.split('?', 1)[0]
print(url)