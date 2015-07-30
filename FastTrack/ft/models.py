from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Customer(models.Model):
    customerID = models.IntegerField(default=0)
    user = models.ForeignKey(User)

class Courier(models.Model):
    courierID = models.IntegerField(default=0)
    user = models.ForeignKey(User)

class Rating(models.Model):    
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
    customer =  models.ForeignKey(Customer)
    courier = models.ForeignKey(Courier)
    
class CustomerListing(models.Model):
    customerListingID = models.IntegerField(default=0)
    startLocation = models.CharField(max_length=200)
    endLocation = models.CharField(max_length=200)
    arrivalDate = models.DateField(default=0)
    arrivalTime = models.TimeField(default=0)
    status = models.BooleanField(default=True)
    poster = models.ForeignKey(Customer)

class CourierListing(models.Model):
    courierListingID = models.IntegerField(default=0)
    startLocation = models.CharField(max_length=200)
    endLocation = models.CharField(max_length=200)
    arrivalDate = models.DateField(default=0)
    arrivalTime = models.TimeField(default=0)
    status = models.BooleanField(default=True)
    poster = models.ForeignKey(User)