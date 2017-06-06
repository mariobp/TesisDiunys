"""sie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views import generic
from material.frontend import urls as frontend_urls
import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^dashboard/', admin.site.urls),
    url(r'^usuarios/', include('usuarios.urls')),
    url(r'^interfaz/', include('interfaz.urls', namespace="interfaz")),
    url(r'', include(frontend_urls, namespace="frontend_urls")),
    url(r'^$', generic.TemplateView.as_view(template_name="frontend/index.html"), name="index"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
