from django.shortcuts import *
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import *
from .forms import *
from django.views.generic import DetailView, ListView
import models


# Create your views here.

def index(request):
    return HttpResponse("You're at the index of /api.")

def home(request):
    return HttpResponse("You're at the homepage.")

def createCustomerListing(request):
    if request.user.is_authenticated():   
        if request.method == 'POST':
            form = CreateCustomerListingForm(request.POST)
            if form.is_valid():
                newCustomerListing = form.save(commit=False)
                try:
                    newCustomerListing.poster = Customer.objects.get(user=request.user)
                except Customer.DoesNotExist:
                    c = Customer(user=request.user)
                    c.save()
                    newCustomerListing.poster = c
                newCustomerListing = form.save()
                return redirect(newCustomerListing.get_absolute_url())
        else:
            form = CreateCustomerListingForm()
    else:
        return redirect('FastTrack.views.login')
    return render(request, 'post/post_jobs.html', {'form': form})

def createCourierListing(request):
    if request.user.is_authenticated(): 
        if request.method == 'POST':
            form = CreateCourierListingForm(request.POST)
            if form.is_valid():
                newCourierListing = form.save(commit=False)
                try:
                    newCourierListing.poster = Courier.objects.get(user=request.user)
                except Courier.DoesNotExist:
                    c = Courier(user=request.user)
                    c.save()
                    newCourierListing.poster = c
                newCourierListing = form.save()
                return redirect(newCourierListing.get_absolute_url())
        else:
            form = CreateCourierListingForm()
    else:
        return redirect('FastTrack.views.login')
    return render(request, 'post/post_trips.html', {'form': form})    

def customerListingDetail(request, pk):
    results = get_object_or_404(CustomerListing,pk=pk)
    contactInfo = results.poster.user.email
    recommend = CustomerListing.objects.filter(startLocation=results.startLocation,endLocation=results.endLocation).exclude(pk=pk)[0:3]
    return render(request, 'detail/customerListingdetail.html', {'CustomerListing': results, 'contactInfo':contactInfo, 'recommend':recommend})

def courierListingDetail(request, pk):
    results = get_object_or_404(CourierListing,pk=pk)
    contactInfo = results.poster.user.email
    recommend = CourierListing.objects.filter(startLocation=results.startLocation,endLocation=results.endLocation).exclude(pk=pk)[0:3]
    return render(request, 'detail/courierListingdetail.html', {'CourierListing': results, 'contactInfo':contactInfo, 'recommend':recommend})    
      
def customerListingSearch(request):
    form = SearchForm()
    return render(request, 'search/search_jobs.html', {'form': form})
    
def courierListingSearch(request):
    form = SearchForm()
    return render(request, 'search/search_trips.html', {'form': form})

class JobSearchResults(ListView):
    model = models.CustomerListing
    template_name = 'search/search_jobs_results.html'  
    context_object_name = "results"  
    paginate_by = 5
    
    def get_queryset(self):
        queryset = super(JobSearchResults, self).get_queryset()
        if self.request.GET.items():
            if 'startLocation' in self.request.GET:
                sL = self.request.GET.get('startLocation')
                if sL is not None and sL != '':
                    queryset = queryset.filter(startLocation=sL)
            if 'endLocation' in self.request.GET:
                eL = self.request.GET.get('endLocation')
                if eL is not None and eL != '':
                    queryset = queryset.filter(endLocation=eL)
            if 'beforeDate' in self.request.GET:
                bD = self.request.GET.get('beforeDate')
                if bD is not None and bD != '':
                    queryset = queryset.filter(arrivalDate__lt=bD)
            if 'afterDate' in self.request.GET:
                aD = self.request.GET.get('afterDate')
                if aD is not None and aD != '':
                    queryset = queryset.filter(arrivalDate__gt=aD)
            queryset = queryset.order_by('arrivalDate')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(JobSearchResults, self).get_context_data(**kwargs)
        context['sL'] = self.request.GET.get('startLocation')   
        context['eL'] = self.request.GET.get('endLocation')
        context['bD'] = self.request.GET.get('beforeDate')
        context['aD'] = self.request.GET.get('afterDate')
        return context

class TripSearchResults(ListView):
    model = models.CourierListing
    template_name = 'search/search_trips_results.html'  
    context_object_name = "results"  
    paginate_by = 5
    
    def get_queryset(self):
        queryset = super(TripSearchResults, self).get_queryset()
        if self.request.GET.items():
            if 'startLocation' in self.request.GET:
                sL = self.request.GET.get('startLocation')
                if sL is not None and sL != '':
                    queryset = queryset.filter(startLocation=sL)
            if 'endLocation' in self.request.GET:
                eL = self.request.GET.get('endLocation')
                if eL is not None and eL != '':
                    queryset = queryset.filter(endLocation=eL)
            if 'beforeDate' in self.request.GET:
                bD = self.request.GET.get('beforeDate')
                if bD is not None and bD != '':
                    queryset = queryset.filter(arrivalDate__lt=bD)
            if 'afterDate' in self.request.GET:
                aD = self.request.GET.get('afterDate')
                if aD is not None and aD != '':
                    queryset = queryset.filter(arrivalDate__gt=aD)
            queryset = queryset.order_by('arrivalDate')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(TripSearchResults, self).get_context_data(**kwargs)
        context['sL'] = self.request.GET.get('startLocation')   
        context['eL'] = self.request.GET.get('endLocation')
        context['bD'] = self.request.GET.get('beforeDate')
        context['aD'] = self.request.GET.get('afterDate')
        return context
