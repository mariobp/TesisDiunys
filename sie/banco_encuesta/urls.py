from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^list/asignaciones/$', views.AsignacionesList.as_view(), name="asignaciones"),
]
