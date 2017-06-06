# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from encuesta import models
# Create your views here.


def index(request):
    encuestas = models.Instrumento.objects.all()
    return render(request, 'frontend/index.html', {"encuestas": encuestas})
# end def
