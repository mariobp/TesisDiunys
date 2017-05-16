# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from usuarios import models as usuarios
# Register your models here.


@admin.register(usuarios.Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'identificacion',
                    'cargo', 'fecha_nacimiento')
    search_fields = ('username', 'email', 'first_name',
                     'last_name', 'identificacion')
    icon = '<i class="material-icons">person</i>'
# end class


@admin.register(usuarios.Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'identificacion', 'fecha_nacimiento')
    search_fields = ('username', 'email', 'first_name',
                     'last_name', 'identificacion')
    icon = '<i class="material-icons">person_outline</i>'
# end class


@admin.register(usuarios.Egresado)
class EgresadoAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'identificacion',
                    'fecha_nacimiento', 'fecha_ingreso', 'fecha_egreso')
    search_fields = ('username', 'email', 'first_name',
                     'last_name', 'identificacion')
    icon = '<i class="material-icons">school</i>'
# end class


@admin.register(usuarios.Empleador)
class EmpleadorAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'identificacion',
                    'empresa', 'nit', 'fecha_nacimiento')
    search_fields = ('username', 'email', 'first_name',
                     'last_name', 'identificacion')
    icon = '<i class="material-icons">work</i>'
# end class
