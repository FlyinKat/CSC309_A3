from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from rest_framework import generics
from .models import *
from .serializers import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

# Create your views here.

def index(request):
    return HttpResponse("You're at the index of /api.")

def home(request):
    return HttpResponse("You're at the homepage.")

@login_required    
def createCustomerListing(request):
    if request.method == 'POST':
        form = CreateCustomerListingForm(request.POST)
        if form.is_valid():
            newCustomerListing = form.save(commit=False)
            #need to check if user is customer
            newCustomerListing.poster = Customer.objects.get(user=request.user)
            newCustomerListing = form.save()
            #change to redirect to new created listing page later
            return redirect(createCustomerListing)
    else:
        form = CreateCustomerListingForm()
    return render(request, 'post/post_jobs.html', {'form': form})

@login_required 
def createCourierListing(request):
    if request.method == 'POST':
        form = CreateCourierListingForm(request.POST)
        if form.is_valid():
            newCourierListing = form.save(commit=False)
            #need to check if user is courier
            newCourierListing.poster = Courier.objects.get(user=request.user)
            newCourierListing = form.save()
            #change to redirect to new created listing page later
            return redirect(createCourierListing)
    else:
        form = CreateCourierListingForm()
    return render(request, 'post/post_trips.html', {'form': form})    
    
class CustomerListingList(generics.ListCreateAPIView):
    queryset = CustomerListing.objects.all()
    serializer_class = CustomerListingSerializer

class CustomerListingDetail(DetailView):
    context_object_name = 'CustomerListing'
    queryset = CustomerListing.objects.all()
    template_name = 'detail/customerListingdetail.html'
    
class CourierListingDetail(DetailView):
    context_object_name = 'CourierListing'
    queryset = CourierListing.objects.all()
    template_name = 'detail/courierListingdetail.html'
    
class CustomerListingSearch(generics.ListAPIView):
    serializer_class = CustomerListingSerializer

    def get_queryset(self):
        """
        This view should return a list of all the customer listings for
        the user as determined by the startlocation portion of the URL.
        """
        start = self.kwargs['startLocation']
        return CustomerListing.objects.filter(startLocation=start)