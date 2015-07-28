from django.db import models
from django.contrib.auth.models import User

# Create your models here

class Customer(models.Model):
    customerID = models.IntegerField(default=0)
    user = models.ForeignKey(User)

class Courier(models.Model):
    courierID = models.CharField(max_length=200)
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
    arrivalTime = models.DateTimeField(default=0)
    status = models.BooleanField()
    poster = models.ForeignKey(Customer)

class CourierListing(models.Model):
    courierListingID = models.CharField(max_length=200)
    startLocation = models.CharField(max_length=200)
    endLocation = models.CharField(max_length=200)
    arrivalTime = models.DateTimeField(default=0)
    status = models.BooleanField()
    poster = models.ForeignKey(User)