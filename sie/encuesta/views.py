# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from supra import views as supra
import models
import json
supra.SupraConf.body = True

# Create your views here.


class OpcionSupra(supra.SupraListView):
    model = models.Opcion
    list_display = ['id', 'texto', ]
    list_filter = ['pregunta']
# end class


class CerradaSupra(supra.SupraListView):
    model = models.Cerrada
    list_display = ['enunciado', 'descripcion', 'multiple', 'otro', 'numero', 'id', ('opciones', 'json')]
    list_filter = ['instrumento']

    def opciones(self, obj, row):
        class request():
            method = 'GET'
            GET = {'pregunta': obj.pk}
        # end class
        lista = OpcionSupra(dict_only=True).dispatch(request=request())
        return json.dumps(lista)
    # end def
# end class


class InstrumentoSupraList(supra.SupraListView):
    model = models.Instrumento
    list_display = ['id', 'nombre', 'descripcion', ('preguntasList', 'json')]
    list_filter = ['id', ]

    def preguntasList(self, obj, row):
        class request():
            method = 'GET'
            GET = {'instrumento': obj.pk}
        # end class
        preguntas = CerradaSupra(dict_only=True).dispatch(request=request())
        return json.dumps(preguntas)
    # end def

    def dispatch(self, request, *args, **kwargs):
        return super(InstrumentoSupraList, self).dispatch(request, *args, **kwargs)
    # end def
# end class
