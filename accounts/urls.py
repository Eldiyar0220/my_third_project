from django.urls import path

from accounts.views import RegisterViews

urlpatterns = [
   path('register/', RegisterViews.as_view(), name='register'),

]