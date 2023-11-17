from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class AdminRegform(forms.ModelForm):
    password = forms.CharField(max_length=20,min_length=8,widget=forms.PasswordInput)
    # conf_pw = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password']

class AdminLogin(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30,widget=forms.PasswordInput)
