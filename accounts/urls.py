from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts import views
from accounts.views import RegisterViews, SignView, SuccessfulRegistrationView, \
                              ForgotPasswordView

urlpatterns = [
   path('register/', RegisterViews.as_view(), name='register'),
   path('activation/', views.ActivationView.as_view(), name='activation'),
   path('success_registration/', SuccessfulRegistrationView.as_view(), name='success_registration'),
   path('login/', SignView.as_view(), name='login'),

   path('forgot_password/', ForgotPasswordView.as_view(), name='forgot-password'),
   path('reset/<int:pk>/<str:token>/', views.reset, name='reset'),

   path('logout/', LogoutView.as_view(next_page='home'), name='logout'),

]
