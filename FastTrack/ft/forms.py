from django.forms import ModelForm
from .models import *

class CreateCustomerListingForm(ModelForm):
    class Meta:
        model = CustomerListing
        exclude = ['customerListingID', 'status', 'poster']
        fields = ['startLocation', 'endLocation', 'arrivalDate', 'arrivalTime']