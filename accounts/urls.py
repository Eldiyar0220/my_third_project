from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts import views
from accounts.views import RegisterViews

urlpatterns = [
   path('register/', RegisterViews.as_view(), name='register'),
   path('login/', views.sign, name='login'),
   path('logout/', LogoutView.as_view(next_page='home'), name='logout'),

]