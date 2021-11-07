"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import views_pages, views_errors

from django.conf import settings # Necessario para configurar MEDIA_URL
from django.conf.urls.static import static # Necessario para configurar MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_pages.index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Necessario para MEDIA_URL

# Erros customizados
handler404 = "core.views.views_errors.handler404"
handler400 = "core.views.views_errors.handler400"