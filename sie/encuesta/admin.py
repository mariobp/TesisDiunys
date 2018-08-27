# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from encuesta import models as encuesta
# Register your models here.

@admin.register(encuesta.Opcion)
class OpcionStack(admin.ModelAdmin):
    list_display = ('texto',)

    class Media:
        css = {
            "all": ('/static/admin/css/style.css',)
        }
    # end class
# end class

class PreguntaCerradaStack(admin.StackedInline):
    model = encuesta.Cerrada


@admin.register(encuesta.Instrumento)
class InstrumentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'tipo', 'fecha', 'estadisticas', 'descargar_datos',)
    search_fields = ('nombre', 'descripcion')
    icon = '<i class="material-icons">content_paste</i>'
    inlines = [PreguntaCerradaStack]

    class Media:
        js = ('/static/banco/js/loader.js', '/static/banco/js/index.js')
        css = {
            "all": ('/static/admin/css/style.css',)
        }
    # end class
# end class
