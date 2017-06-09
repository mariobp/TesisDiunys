# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from encuesta import models
from django.contrib.auth.decorators import login_required
from supra import views as supra
from django.contrib.auth import login, logout, authenticate
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


@login_required(login_url="/dashboard/login/")
def index(request):
    encuestas = models.Instrumento.objects.all()
    return render(request, 'frontend/index.html', {"encuestas": encuestas})
# end def


class LoginU(supra.SupraSession):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        a = super(LoginU, self).dispatch(request, *args, **kwargs)
        return a
    # end def
# end class
