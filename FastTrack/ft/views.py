from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from rest_framework import generics
from .models import *
from .serializers import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, ListView


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
            return redirect(newCustomerListing.get_absolute_url())
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
            return redirect(newCourierListing.get_absolute_url())
    else:
        form = CreateCourierListingForm()
    return render(request, 'post/post_trips.html', {'form': form})    

def customerListingDetail(request, pk):
    results = CustomerListing.objects.get(pk=pk)
    contactInfo = results.poster.user.email
    return render(request, 'detail/customerListingdetail.html', {'CustomerListing': results, 'contactInfo':contactInfo})

def courierListingDetail(request, pk):
    results = CourierListing.objects.get(pk=pk)
    contactInfo = results.poster.user.email
    return render(request, 'detail/courierListingdetail.html', {'CourierListing': results, 'contactInfo':contactInfo})    
      
def customerListingSearch(request):
    form = CustomerListingSearchForm()
    return render(request, 'search/search_jobs.html', {'form': form})

def customerListingSearchResults(request):    
    if request.GET.items():
        results = CustomerListing.objects.all()
        if 'startLocation' in request.GET:
            sL = request.GET.get('startLocation')
            if sL is not None and sL != '':
                results = results.filter(startLocation=sL)
        if 'endLocation' in request.GET:
            eL = request.GET.get('endLocation')
            if eL is not None and eL != '':
                results = results.filter(endLocation=eL)
        if 'arrivalDate' in request.GET:
            aD = request.GET.get('arrivalDate')
            if aD is not None and aD != '':
                results = results.filter(arrivalDate=aD)
        if 'arrivalTime' in request.GET:
            aT = request.GET.get('arrivalTime')
            if aT is not None and aT != '':
                results = results.filter(arrivalTime=aT)
        return render(request, "search/search_jobs_results.html", {'results': results})
    else:
        results = CustomerListing.objects.all()
        return render(request, "search/search_jobs_results.html", {'results': results})
        