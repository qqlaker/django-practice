from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.db.models import IntegerField


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phonenumber = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'phonenumber', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.phonenumber = self.cleaned_data["phonenumber"]
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    phonenumber = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'phonenumber', 'email']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']
