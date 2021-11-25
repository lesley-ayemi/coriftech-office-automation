from django.shortcuts import render

# Create your views here.
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy

from .forms import LoginForm


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'login.html'