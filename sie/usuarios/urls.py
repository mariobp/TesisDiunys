from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
import views
from .forms import CustomAuthenticationForm

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'usuarios/login.html',
        'authentication_form': CustomAuthenticationForm}, name='login'),
    url(r'^logout/$', views.logoutUsers, name="logOut"),
    url(r'^is/login/$', views.islogin, name="isLogin"),
    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^diligenciador/edit/(?P<pk>\d+)/$',
        views.DiligenciadorSupraForm.as_view(), name="diligenciador"),
    url(r'^export/xls/$', views.export_egresados, name='export_egresados'),
]
