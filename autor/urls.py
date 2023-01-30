from django.urls import path
from autor import views


urlpatterns = [
    path('', views.author , name='author'),

    
]