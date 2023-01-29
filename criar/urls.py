
from django.urls import path
from criar import views


urlpatterns = [
    path('', views.criar , name='create'),

    
]

