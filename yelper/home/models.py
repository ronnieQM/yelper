# FROM PHONENUMBER_FIELD.MODELFIELDS IMPORT PHONENUMBER_FIELDE
# FROM PHONENUMBER_FIELD.PHONENUMBER IMPORT pHONEnUMBER
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User

class Query(models.Model):
    url = models.CharField(max_length=500)
    name = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    created_by = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
