from django.urls import path
from .views import Kompyuter_data


urlpatterns= [
    path('k_data/',Kompyuter_data,name='kompyuter')
]









