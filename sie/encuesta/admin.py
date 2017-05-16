# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from encuesta import models as encuesta
# Register your models here.


class OpcionStack(admin.StackedInline):
    model = encuesta.Opcion
# end class


@admin.register(encuesta.Cerrada)
class CerradaAdmin(admin.ModelAdmin):
    list_display = ('enunciado', 'descripcion', 'numero', 'estado')
    search_fields = ('enunciado', 'descripcion')
    inlines = [OpcionStack]
    icon = '<i class="material-icons">format_list_numbered</i>'
# end class


@admin.register(encuesta.Instrumento)
class InstrumentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'fecha')
    search_fields = ('nombre', 'descripcion')
    icon = '<i class="material-icons">content_paste</i>'
# end class
