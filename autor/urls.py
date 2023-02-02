from django.urls import path
from autor import views
from autor.views import *


urlpatterns = [
    path('', views.author , name='author'),
   
    
]