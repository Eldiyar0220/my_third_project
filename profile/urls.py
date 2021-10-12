from django.urls import path

from profile.views import MainProfileView

urlpatterns = [
    path('profile/', MainProfileView.as_view(), name='profile')
]