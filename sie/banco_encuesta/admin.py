# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import FormularioD, Cerrada, Otros, AsignarEncuestaEgresado, AsignarEncuestaEmpleador
import forms
# Register your models here.


class OtrosStack(admin.StackedInline):
    model = Otros
    readonly_fields = ('pregunta', 'respuesta')
    extra = 0
# end class


class CerradaStack(admin.StackedInline):
    model = Cerrada
    readonly_fields = ('pregunta', 'respuestas')
    extra = 0
# end class


@admin.register(FormularioD)
class FormularioDAdmin(admin.ModelAdmin):
    list_display = ('diligenciador', 'asignacion', 'fecha')
    readonly_fields = ('asignacion', 'diligenciador')
    list_filter = list_display
    search_fields = ('asignacion__instrumento__nombre', 'diligenciador__first_name', 'diligenciador__last_name', 'diligenciador__identificacion')
    inlines = [CerradaStack, OtrosStack]
    icon = '<i class="material-icons">assignment_turned_in</i>'
# end class


@admin.register(AsignarEncuestaEgresado)
class AsignacionEgresadoAdmin(admin.ModelAdmin):
    list_display = ('instrumento', 'fecha')
    filter_horizontal = ('egresados',)
    form = forms.AsignacionEgresadoForm
    icon = '<i class="material-icons">assignment</i>'
# end class


@admin.register(AsignarEncuestaEmpleador)
class AsignacionEmpleadorAdmin(admin.ModelAdmin):
    list_display = ('instrumento', 'fecha')
    filter_horizontal = ('empleadores',)
    form = forms.AsignacionEmpleadorForm
    icon = '<i class="material-icons">assignment</i>'
# end class
