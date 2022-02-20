from django.urls import path

from news.views import MainPageView, ShopPageView

urlpatterns = [
   path('', MainPageView.as_view(), name='home'),
   path('shop/', ShopPageView.as_view(), name='shop')
   ]