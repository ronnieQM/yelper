from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.urls import path

from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home ),
    url(r'^results/$', views.results, name="query_results")
]
