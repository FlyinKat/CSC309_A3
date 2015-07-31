from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from ft.models import Customer



class MyForms(UserCreationForm):
    STATUS = ((1, ("CUSTOMER")), (2, ("COURIER")))
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label = 'First Name', max_length=100, required=True)
    last_name = forms.CharField(label='Last Name', max_length=100, required=True)
    regAs = forms.ChoiceField(label='Register As', choices=STATUS, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'regAs')

    def save(self, commit=True):
        user = super(MyForms, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.regAs = self.cleaned_data['regAs']



        if commit:
            user.save()

        return user

