from django.conf import settings
from django.conf.urls.static import static
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
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


