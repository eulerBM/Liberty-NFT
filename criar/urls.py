from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from criar import views


urlpatterns = [
    path('', views.criar , name='create'),
    

    
]

