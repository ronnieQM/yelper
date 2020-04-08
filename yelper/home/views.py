from django.shortcuts import render
from .models import Query
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import MyForm
from django.http import HttpResponse
import datetime

def home(request) :
    query = Query.objects.all()
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            url = request.POST['url']
            user = User.objects.first()
            query = Query.objects.create(
                url=url,
                created_by = user
            )
            return redirect('/results') #
    else:
        form = MyForm()
    return render(request, 'home.html', {'queries': query})
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)

def results(request):
    return render(request, 'results.html')