# from flask import Flask, request, Response
from bs4 import BeautifulSoup
import requests
import argparse
import sys
import json
import os
import uuid
import csv

import MySQLdb

# connection = MySQLdb.connect(host="localhost",
#                             user="root",
#                             passwd="password",
#                             db="yelper")

# cursor = connection.cursor()
# cursor.execute ("SELECT VERSION()")
# row = cursor.fetchone()
# print("server version:", row[0])
# sql_command = """
# CREATE TABLE yelping( 
# staff_number INTEGER PRIMARY KEY, 
# bname VARCHAR(20), 
# birth_date DATE);"""

# cursor.execute(sql_command)
# connection.commit()
# cursor.close()
# connection.close()

# todo
# create metadata / logs

headerDivClass = "lemon--h1__373c0__2ZHSL heading--h1__373c0__1VUMO heading--no-spacing__373c0__1PzQP heading--inline__373c0__1F-Z6"
reviewDivClass = "lemon--div__373c0__1mboc sidebarActionsHoverTarget__373c0__2kfhE arrange__373c0__UHqhV"
reviewTextPClass = "comment__373c0__3EKjH"
wholeAssReviewDiv = "sidebarActionsHoverTarget__373c0__2kfhE"
businessName = "lemon--h1__373c0__2ZHSL heading--h1__373c0__1VUMO heading--no-spacing__373c0__1PzQP heading--inline__373c0__1F-Z6"
username = "lemon--a__373c0__IEZFH link__373c0__29943 link-color--blue-dark__373c0__1mhJo link-size--default__373c0__1skgq"
location = "lemon--span__373c0__3997G text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--left__373c0__2pnx_ text-weight--bold__373c0__3HYJa text-size--small__373c0__3SGMi"
review = "lemon--p__373c0__3Qnnj text__373c0__2pB8f comment__373c0__3EKjH text-color--normal__373c0__K_MKN text-align--left__373c0__2pnx_"
numBusReviews = "lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--mid__373c0__3G312 text-align--left__373c0__2pnx_ text-size--large__373c0__1568g"
avgRating = "lemon--span__373c0__3997G display--inline__373c0__1DbOG border-color--default__373c0__2oFDT"

def funct(url):
    page_response = request.get(url, timeout=5)
    page_content = BeautifulSoup(page_content.contents)
    
def funct(url):
    page_response = requests.get(url, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")

    # create array of review divs
    reviewArray = []
    reviewBlock = page_content.findAll(
        'div', attrs={"class": wholeAssReviewDiv})
    for i in reviewBlock:
        user = i.find('a', attrs={"class": username})
        userLocation = i.find('span', attrs={location})
        thisReview = i.find('p', attrs={"class": reviewTextPClass})
        print('-'*20)
        print(user.text)
        # print(userLocation.text)
        print(thisReview.text)
        reviewArray.append(i.text)
        # with open("testFile.txt", 'a') as f:
        #     f.write(i)
        # print(i)

    url = url
    thisAvgRating = page_content.find('span', attrs={"class": avgRating})
    x = thisAvgRating.find('aria-label')
    title = page_content.find('h1', attrs={"class": businessName}).text
    with open('eggs.csv', 'a', newline='') as csvfile:
        newFileWriter = csv.writer(csvfile)
        for i in reviewArray:
            newFileWriter.writerow([i])




    print(x)
    print("There are: " + str(len(reviewArray)) + " reviews.")

    # save SOME output to TXT file
    # s = page_content.find('h1', attrs={"class": businessName}).text
    # s = s.lower()
    # title = s.replace(" ", "-")
    # file_name = title + "-results" ".txt"
    # with open(file_name, 'w') as f:
    #     for item in reviewArray:
    #         f.write("-"*20)
    #         f.write("\n%s\n" % item)
    #         f.write("-"*20)
    # return "test"


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument('url', help='yelp bussiness url')
    args = argparser.parse_args()
    url = args.url
    funct(url)
