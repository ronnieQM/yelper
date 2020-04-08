from flask import Flask, request, Response
from bs4 import BeautifulSoup
import requests
import argparse
import sys
import json
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)


def funct(url):
    page_response = requests.get(url, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    print("finish")
    textContent = []
    stuff = page_content.findAll('p', attrs={"class": "comment__373c0__3EKjH"})
    for i in stuff:
        print(i.text)
        textContent.append(i.text)
    print("-----------")
    print(textContent)
    print("-----------")
    print(type(textContent))
    print(len(textContent))
    return textContent


@app.route("/", methods=["POST"])
def index():
    # print(request.form)
    test = funct(request.form["url"])
    return Response(json.dumps(test), mimetype='application/json')
    # return json.dumps(request.form)
    # return json.dumps({"key": 3})


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


if __name__ == "__main__":
    # argparser = argparse.ArgumentParser()
    # argparser.add_argument('url', help='yelp bussiness url')
    # args = argparser.parse_args()
    # url = args.url
    # funct(url)
    app.run(debug=True)
