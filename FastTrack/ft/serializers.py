from rest_framework import serializers
from .models import *
#from django.contrib.auth.models import User

class CustomerListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerListing
        fields = ('customerListingID', 'startLocation', 'endLocation', 'arrivalTime', 'status', 'poster')
