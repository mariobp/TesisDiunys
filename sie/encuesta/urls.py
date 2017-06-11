from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^list/instrumentos/$', views.InstrumentoSupraList.as_view(), name="instrumentos"),
]
