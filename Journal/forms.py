from django.contrib.auth.models import User
from django import forms
from Journal.models import *

class UserForm(forms.ModelForm):
    '''Form class to create a new user
    
    Author: Austin
    '''
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name',)
