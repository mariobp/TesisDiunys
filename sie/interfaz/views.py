# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from supra import views as supra
from django.contrib.auth import login, logout, authenticate
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url="/usuarios/login/")
def index(request):
    return render(request, 'frontend/index.html', {})
# end def


def encuestas(request):
    return render(request, 'frontend/encuestas.html', {})
# end def


def instrumento(request):
    return render(request, 'frontend/instrumento.html', {})
# end def


def perfil(request):
    return render(request, 'frontend/perfil.html', {})
# end def
