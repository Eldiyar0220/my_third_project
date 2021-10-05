from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import UserRegistrationForm

class RegisterViews(CreateView):
    template_name = 'pages/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('home')