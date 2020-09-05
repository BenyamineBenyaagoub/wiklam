from django.contrib import admin
from django.urls import path, include 
from django.views.generic.base import TemplateView

from django.conf import settings

from django.conf.urls.static import static

from django.views.static import serve


urlpatterns = [
    path('', include('home.urls')),
    path('', include('post.urls')),
    path('', include('pregunta.urls')),

    path('admin-bt/', admin.site.urls),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
