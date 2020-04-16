from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db import models

class Query(models.Model):
    url = models.CharField(max_length=500)
    name = models.CharField(max_length=50)
    created_by = models.DateField(auto_now=True)

    print("@ "*20)
    def __str__(self):
        print("$"*20)
        return self.name

class Search(models.Model):
    url = models.CharField(max_length=500)
    name = models.CharField(max_length=50)
    created_by = models.DateField(auto_now=True)
