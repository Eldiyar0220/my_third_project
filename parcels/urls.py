from django.urls import path

# from parcels.views import ParcelsCreateView
from parcels.views import parcels

urlpatterns = [
    # path('', ParcelsCreateView.as_view(), name='parcels')
    path('', parcels, name='parcels'),

]