# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from supra import views as supra
from django.contrib.auth import login, logout, authenticate
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from models import Diligenciador
from forms import DiligenciadorForm
import json as simplejson
supra.SupraConf.body = True

# Create your views here.


class Login(supra.SupraSession):
    body = True

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        a = super(Login, self).dispatch(request, *args, **kwargs)
        return a
    # end def
# end class


def islogin(request):
    if request.user.is_authenticated():
        diligenciador = Diligenciador.objects.filter(
            id=request.user.id).first()
        if diligenciador:
            return HttpResponse(simplejson.dumps({"id": diligenciador.id, "celular": diligenciador.celular, "email": diligenciador.email, "direccion": diligenciador.direccion}), 200)
        return HttpResponse(simplejson.dumps({"id": None, "celular": None, "email": None, "direccion": None}), 200)
    # end if
    return HttpResponse([], 400)
# end if


def logoutUsers(request):
    logout(request)
    return redirect('/')
# end def


class DiligenciadorSupraForm(supra.SupraFormView):
    model = Diligenciador
    form_class = DiligenciadorForm
    template_name = "usuarios/form.html"
    response_json = False

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(DiligenciadorSupraForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class


@login_required(login_url='/usuarios/login/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Tu contraseña se actualizó con éxito!')
            return redirect('usuarios:change_password')
        else:
            messages.error(request, 'Corrija por favor el error abajo.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'usuarios/change_password.html', {
        'form': form
    })
