from django.urls import path

from news.views import MainPageView

urlpatterns = [
   path('', MainPageView.as_view(), name='home'),
   ]