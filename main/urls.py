from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from home import views
from autor.views import *

urlpatterns = [

    # ADMIN
    path('admin/', admin.site.urls),

    # URLS do home
    path('', views.home, name='home' ),

    # URLS do explorar
    path('explore/', include('explorar.urls')),

    # URLS do detalhes
    path('detalhes/', include('detalhes.urls')),

    # URLS do autor
    path('autor/', include('autor.urls')),
    

    # URLS de criar item
    path('criar/', include('criar.urls')),
    
    #Django allauth
    path('accounts/', include('allauth.urls')),

    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




