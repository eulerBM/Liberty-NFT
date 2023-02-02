from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from home import views
from autor.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home' ),
    path('explore/', views.explore, name='explore'),
    path('details/', views.details, name='details'),

    # URLS do autor
    path('autor/', include('autor.urls')),
    

    # URLS de criar item
    path('criar/', include('criar.urls')),
    

    #Django allauth
    path('accounts/', include('allauth.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




