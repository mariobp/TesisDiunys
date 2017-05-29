# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import FormularioD, Cerrada, Otros
# Register your models here.


class OtrosStack(admin.StackedInline):
    model = Otros
# end class


class CerradaStack(admin.StackedInline):
    model = Cerrada
# end class


@admin.register(FormularioD)
class FormularioDAdmin(admin.ModelAdmin):
    list_display = ('diligenciador', 'instrumento', 'fecha')
    list_filter = list_display
    search_fields = ('instrumento__nombre', 'diligenciador__first_name', 'diligenciador__last_name', 'diligenciador__identificacion')
    inlines = [CerradaStack, OtrosStack]
    icon = '<i class="material-icons">assignment</i>'
# end class
