from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^list/asignaciones/$', views.AsignacionesList.as_view(), name="asignaciones"),
    url(r'^formulario/$', views.FormularioDSupraForm.as_view(), name="formulario"),
    url(r'^export/xls/(?P<id>\d+)/$', views.exporExel, name='export_xls'),
    url(r'^data/(?P<id>\d+)/$', views.dataPie, name='data'),
]
