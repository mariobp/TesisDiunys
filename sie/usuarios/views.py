# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from supra import views as supra
from django.contrib.auth import login, logout, authenticate
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from sie.http import response
import json as simplejson

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
        return response(simplejson.dumps({"session": request.session.session_key, "username": request.user.username}), 200)
    # end if
    return response([], 400)
# end if


def logoutUsers(request):
    logout(request)
    return redirect('/')
# end def


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
