
from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home' ),
    path('explore/', views.explore, name='explore'),
    path('details/', views.details, name='details'),

    # URLda pasta criar
    path('criar/', include('criar.urls')),

    # --------------------------- 
    path('author/', views.author, name='author')
]
