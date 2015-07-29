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

class ListingList(generics.ListCreateAPIView):
    queryset = CustomerListing.objects.all()
    serializer_class = ListingSerializer


class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerListing.objects.all()
    serializer_class = ListingSerializer
