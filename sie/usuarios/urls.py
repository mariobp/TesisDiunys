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
]
