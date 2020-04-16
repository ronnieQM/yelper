from django.shortcuts import render
from .models import Query
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import MyForm
from django.http import HttpResponse
import requests
import datetime
import json
import mimetypes

def home(request) :
    payload = {}
    headers= {}
    endpoint = 'https://cxn7vhhfdj.execute-api.us-west-2.amazonaws.com/dev'
    if request.method == 'POST':
        print("! " * 30)
        form = MyForm(request.POST)
        if form.is_valid():
            url = request.POST['url']
            user = User.objects.first()
            reqString = endpoint + '?url=' + url
            response = requests.request('GET', reqString, headers=headers, data = payload)
            result = response.text.encode('utf8')
            context = {
                'url' : url,
                'result' : result
            }
            print("# " * 30)
            print(response.text.encode('utf8'))
            print('\n'*3)
            print(type(response))
            print(type(response.text.encode('utf8')))
            blah = response.text.encode('utf8')
            try:
                print(blah[0].json)
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("sucess")
            except:
                pass
            try:
                print(blah.json)
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("sucess")
            except:
                pass
            print("# " * 30)
            template_name = 'results.html'
            return render(request, template_name, context)
    else:
        print("( " * 30)
        form = MyForm()
    return render(request, 'home.html')

def results(request):
    return render(request, 'results.html')