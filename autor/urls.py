from django.urls import path
from autor import views
from autor.views import *


urlpatterns = [
    path('', views.author , name='author'),
    path('<int:id>', views.conta_de_outro_user, name='outro_user'),

   
    
]