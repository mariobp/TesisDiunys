# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from usuarios import models as usuarios
from import_export.admin import  ImportMixin, ImportExportModelAdmin
from import_export import resources, widgets
from django.contrib.auth.models import User
import forms as form
# Register your models here.


@admin.register(usuarios.Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'identificacion', 'email',
                    'cargo', 'fecha_nacimiento')
    search_fields = ('username', 'email', 'first_name',
                     'last_name', 'identificacion')
    icon = '<i class="material-icons">person</i>'
    form = form.DirectorForm

    def get_form(self, request, obj=None, *args, **kwargs):
        if obj:
            kwargs['form'] = form.DirectorEdit
        # end if
        return super(DirectorAdmin, self).get_form(request, obj, *args, **kwargs)
    # end def
# end class


@admin.register(usuarios.Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'identificacion', 'email', 'fecha_nacimiento')
    search_fields = ('username', 'email', 'first_name',
                     'last_name', 'identificacion')
    icon = '<i class="material-icons">person_outline</i>'
    form = form.AdministradorForm

    def get_form(self, request, obj=None, *args, **kwargs):
        if obj:
            kwargs['form'] = form.AdministradorFormEdit
        # end if
        return super(AdministradorAdmin, self).get_form(request, obj, *args, **kwargs)
    # end def
# end class


class EgresadoResource(resources.ModelResource):

    class Meta:
        model = usuarios.Egresado
        skip_unchanged = True
        report_skipped = True
        fields = ('first_name', 'last_name', 'identificacion', 'email', 'username',
                    'fecha_nacimiento', 'fecha_ingreso', 'fecha_egreso', 'celular', 'direccion')
    # end class

    def before_import(self, dataset, *args, **kwargs):
        dataset.insert_col(0, col=["",]*dataset.height, header="id")

    def get_instance(self, instance_loader, row):
        return False

    def import_obj(self, obj, data, dry_run):
        identificacion = data.get('identificacion')
        print "identificacion", identificacion
        for field in self.get_fields():
            if isinstance(field.widget, widgets.ManyToManyWidget):
                continue
            if field.column_name == 'username':
                data.update({'username': identificacion})
                obj.set_password(raw_password=identificacion)
            self.import_field(field, obj, data)
        # end for
    # end def

# end class

@admin.register(usuarios.Egresado)
class EgresadoAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'identificacion', 'email', 'graduado',
                    'fecha_nacimiento', 'fecha_ingreso', 'fecha_egreso')
    search_fields = ('username', 'email', 'first_name',
                     'last_name', 'identificacion')
    icon = '<i class="material-icons">school</i>'
    form = form.EgresadoForm
    resource_class = EgresadoResource
    import_template_name = "import.html"

    def get_form(self, request, obj=None, *args, **kwargs):
        if obj:
            kwargs['form'] = form.EgresadoEdit
        # end if
        return super(EgresadoAdmin, self).get_form(request, obj, *args, **kwargs)
    # end def

    class Media:
        css = {
            "all":("usuarios/css/egresados.css",)
        }
        js = ("usuarios/js/egresados.js",)
    # end class
# end class


@admin.register(usuarios.Empleador)
class EmpleadorAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'identificacion', 'email',
                    'empresa', 'nit', 'cargo', 'fecha_nacimiento')
    search_fields = ('username', 'email', 'first_name',
                     'last_name', 'identificacion')
    icon = '<i class="material-icons">work</i>'
    form = form.EmpleadorForm

    def get_form(self, request, obj=None, *args, **kwargs):
        if obj:
            kwargs['form'] = form.EmpleadorFormEdit
        # end if
        return super(EmpleadorAdmin, self).get_form(request, obj, *args, **kwargs)
    # end def
# end class


@admin.register(usuarios.GrupoPeriodo)
class GrupoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha')
    search_fields = ('nombre',)
    filter_horizontal = ('egresados',)
    list_filter = ('fecha',)
    icon = '<i class="material-icons">group</i>'
# end class
