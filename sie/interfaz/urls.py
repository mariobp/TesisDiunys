from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^encuestas/', views.encuestas, name="encuestas"),
    url(r'^instrumento/', views.instrumento, name="instrumento"),
    url(r'^perfil/', views.perfil, name="perfil"),
]
