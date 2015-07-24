from rest_framework import serializers
from .models import *
#from django.contrib.auth.models import User

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('info', 'poster')
