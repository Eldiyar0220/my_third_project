from django.urls import path

from profile import views
from profile.views import MainProfileView,ChangeProfileView

urlpatterns = [
    path('profile/', MainProfileView.as_view(), name='profile'),
    path('change_profile/',views.ChangeProfileView, name='change-profile')
]