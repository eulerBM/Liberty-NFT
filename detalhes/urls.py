from django.urls import path
from detalhes.views import *



urlpatterns = [
    path('<int:id>', details , name='details'),
       
]
