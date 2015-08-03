from django import forms
from models import UserProfile
from django.contrib.auth.models import User


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'email', 'regAs')

    def save(self, commit=True):
        user = super(UserProfileForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.regAs = self.cleaned_data['regAs']
        super(UserProfileForm, self).save(commit=True)

        user.user.email = self.cleaned_data['email']
        user.user.first_name = self.cleaned_data['first_name']
        user.user.last_name = self.cleaned_data['last_name']
        user.user.save()