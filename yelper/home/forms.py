from django import forms
from .models import Query# todo

class MyForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ['url',]