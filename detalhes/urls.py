from django.urls import path
from detalhes.views import *



urlpatterns = [
    path('', details , name='details'),
       
]
