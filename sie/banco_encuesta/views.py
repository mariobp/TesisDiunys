# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from supra import views as supra
import models
# Create your views here.


class AsignacionesList(supra.SupraListView):
    model = models.AsignarEncuesta
    list_display = ['id', 'nombre_ins', 'fecha']
    search_fields = ['nombre_ins', ]

    class Renderer:
        nombre_ins = "instrumento__nombre"
        id_ins = "instrumento__id"
    # end class
# end class
