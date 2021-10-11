from django.contrib.auth import login, authenticate, get_user_model

from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView, FormView, TemplateView
from django.contrib.auth import login as auth_login

from accounts import forms
from accounts.forms import UserRegistrationForm, SignForm

User = get_user_model()

class RegisterViews(CreateView):
    model = User
    template_name = 'pages/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('home')

class SignView(LoginView):
    template_name = 'pages/sign.html'
    form_class = SignForm
    success_url = reverse_lazy('home')




