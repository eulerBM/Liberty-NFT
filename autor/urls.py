from django.urls import path
from autor import views
from autor.views import *


urlpatterns = [
    path('', views.author , name='author'),
    path('<int:id>', views.conta_de_outro_user, name='outro_user'),


    # Sistema de seguidor/seguir
    path('seguir/<int:id>/', seguir, name='seguir'),
    path('deixar_de_seguir/<int:id>/', deixar_de_seguir, name='deixar_de_seguir'),
   
    
]