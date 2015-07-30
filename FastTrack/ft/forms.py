from django import ModelForm

class CreateCustomerListingForm(forms.ModelForm):
    class Meta:
        model = CustomerListing
        exclude = ['customerListingID', 'status', 'poster']
        fields = ['startLocation', 'endLocation', 'arrivalDate', 'arrivalTime']