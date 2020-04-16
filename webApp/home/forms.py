from django import forms
from .models import Query, Search

class MyForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ['url',]