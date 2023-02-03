from django.urls import path
from explorar.views import *


urlpatterns = [
    path('explore/', explore, name='explore'),


    
]