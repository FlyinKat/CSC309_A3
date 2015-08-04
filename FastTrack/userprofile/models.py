from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    CUSTOMER = 'CUSTOMER'
    COURIER = 'COURIER'
    STATUS = ((CUSTOMER, ("CUSTOMER")), (COURIER, ("COURIER")))
    regAs = models.CharField(max_length=10, choices=STATUS)
    #NUMERATOR = models.IntegerField(default=0)
    #DENOMINATOR = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
