from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = 'pages/index.html'