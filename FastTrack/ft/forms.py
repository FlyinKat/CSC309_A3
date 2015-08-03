from django.forms import ModelForm
from django import forms
from .models import *

class CreateCustomerListingForm(ModelForm):
    class Meta:
        model = CustomerListing
        exclude = ['customerListingID', 'status', 'poster']
        fields = ['itemInfo', 'startLocation', 'endLocation', 'arrivalDate', 'arrivalTime']
        
class CreateCourierListingForm(ModelForm):
    class Meta:
        model = CourierListing
        exclude = ['courierListingID', 'status', 'poster']
        fields = ['itemInfo', 'startLocation', 'endLocation', 'arrivalDate', 'arrivalTime']
        
class SearchForm(forms.Form):
    startLocation = models.CharField()
    endLocation = models.CharField()
    beforeDate = models.DateField()
    afterDate = models.DateField()

class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['courier', 'customer', 'rating', 'comment']
