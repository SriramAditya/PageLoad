from django import forms
from django.core import validators

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()