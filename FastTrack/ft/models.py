from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

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
    itemInfo = models.CharField(max_length=200, null=True)
    status = models.BooleanField(default=True)
    poster = models.ForeignKey(Customer, null=True)
    
    def get_absolute_url(self):
        return reverse('ft.views.customerListingDetail', args=[str(self.pk)])

class CourierListing(models.Model):
    courierListingID = models.IntegerField(default=0)
    startLocation = models.CharField(max_length=200)
    endLocation = models.CharField(max_length=200)
    arrivalDate = models.DateField(default=0)
    arrivalTime = models.TimeField(default=0)
    itemInfo = models.CharField(max_length=200, null=True)
    status = models.BooleanField(default=True)
    poster = models.ForeignKey(Courier, null=True)
    
    def get_absolute_url(self):
        return reverse('ft.views.courierListingDetail', args=[str(self.pk)])
        
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    CUSTOMER = 'CUSTOMER'
    COURIER = 'COURIER'
    STATUS = ((CUSTOMER, ("CUSTOMER")), (COURIER, ("COURIER")))
    regAs = models.CharField(max_length=10, choices=STATUS)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
