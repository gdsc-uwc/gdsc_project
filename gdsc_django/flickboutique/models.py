from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Customer(models.Model):
    # Signup form information
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    userName = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    streetAddress = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    suburb = models.CharField(max_length=64)
    postalCode = models.IntegerField()
    country = CountryField()
    phoneNumber = PhoneNumberField()
    password = models.CharField(max_length=128)
    # Other information
    bio = models.CharField(max_length=1024)

class Business(models.Model):
    # Signup form information
    businessName = models.CharField(max_length=128)
    userName = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    streetAddress = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    suburb = models.CharField(max_length=64)
    postalCode = models.IntegerField()
    country = CountryField()
    phoneNumber = PhoneNumberField()
    password = models.CharField(max_length=128)
    # Other information
    bio = models.CharField(max_length=1024)
