from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Profile
class signupform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2'] 


class Userform(ModelForm):
    class Meta:
         model = User
         fields = ['username','first_name','last_name','email',]


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['city','phone','image']
