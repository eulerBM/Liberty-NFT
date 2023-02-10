from django.urls import path
from autor import views



urlpatterns = [
    path('', views.author , name='author'),
    path('<int:id>', views.conta_de_outro_user, name='outro_user'),
    path('seguir/<int:id>', views.seguir, name='seguir'),
    path('deixar_de_seguir/<int:id>', views.deixar_de_seguir, name='deixar_de_seguir'),

   
    
]