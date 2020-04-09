# from flask import Flask, request, Response
from bs4 import BeautifulSoup
import requests
import argparse
import sys
import json
import os
import uuid

headerDivClass = "lemon--h1__373c0__2ZHSL heading--h1__373c0__1VUMO heading--no-spacing__373c0__1PzQP heading--inline__373c0__1F-Z6"
reviewDivClass = "lemon--div__373c0__1mboc sidebarActionsHoverTarget__373c0__2kfhE arrange__373c0__UHqhV"
reviewTextPClass = "comment__373c0__3EKjH"


def funct(url):
    print("Welcome to Yelper...")
    print("Initializing...")
    page_response = requests.get(url, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    title = page_content.title.string
    print("Scraping " + title + " ...")
    reviewDiv = page_content.findAll(
        'div', attrs={"class": "sidebarActionsHoverTarget__373c0__2kfhE"})
    # reviewDiv = page_content.findAll('p', attrs={"class": reviewTextPClass})
    reviewArray = []
    print("----------------------------------------------")
    print("---------------------TEST---------------------\n\n")
    # print(reviewDiv)
    # print(type(reviewDiv))
    # print(len(reviewDiv))
    for i in reviewDiv:
        i.find('p', attrs={"class": reviewTextPClass})
        reviewArray.append(i.text)
        print(i)
    print(len(reviewArray))

    for i in reviewArray:
        print("----------------------------------------")
        print(i)
    print("\n\n---------------------TEST---------------------")
    print("----------------------------------------------")

    file_name = title[:20] + ".txt"

    with open(file_name, 'w') as f:
        for item in reviewArray:
            f.write("-"*20)
            f.write("\n%s\n" % item)
            f.write("-"*20)
    
    print("\nScraping Complete. Have a nice day.")
    return "test"

unique_filename = str(uuid.uuid4()) + ".txt"


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('url', help='yelp bussiness url')
    args = argparser.parse_args()
    url = args.url
    funct(url)

# def funct(url):
#     page_response = requests.get(url, timeout=5)
#     page_content = BeautifulSoup(page_response.content, "html.parser")
#     print("finish")
#     textContent = []
#     stuff = page_content.findAll('p', attrs={"class": "comment__373c0__3EKjH"})
#     for i in stuff:
#         print(i.text)
#         textContent.append(i.text)
#     print("-----------")
#     print(textContent)
#     print("-----------")
#     print(type(textContent))
#     print(len(textContent))
#     return textContent    print("---------------------TEST---------------------")
