from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class MainProfileView(TemplateView):
    template_name = 'pages/personal-area.html'