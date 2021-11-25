from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')
    