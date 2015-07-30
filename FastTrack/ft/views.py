from django.shortcuts import render
from django.http import HttpResponse, Http404
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.

def index(request):
    return HttpResponse("You're at the index of /api.")

def home(request):
    return HttpResponse("You're at the homepage.")

class CustomerListingList(generics.ListCreateAPIView):
    queryset = CustomerListing.objects.all()
    serializer_class = CustomerListingSerializer

class CustomerListingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerListing.objects.all()
    serializer_class = CustomerListingSerializer
    
class CustomerListingSearch(generics.ListAPIView):
    serializer_class = CustomerListingSerializer

    def get_queryset(self):
        """
        This view should return a list of all the customer listings for
        the user as determined by the startlocation portion of the URL.
        """
        start = self.kwargs['startLocation']
        return CustomerListing.objects.filter(startLocation=start)