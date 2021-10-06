from django.contrib.auth import login, authenticate, get_user_model

from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, FormView

from accounts import forms
from accounts.forms import UserRegistrationForm, SignForm

User = get_user_model()

class RegisterViews(CreateView):
    model = User
    template_name = 'pages/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('home')

def sign(request):
    if request.method == 'POST':
        form = SignForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignForm()
    return render(request, 'pages/sign.html', {'form': form})




