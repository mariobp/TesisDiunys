# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.decorators import method_decorator
from django.shortcuts import render
from supra import views as supra
import models
import forms
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


class AsignacionesList(supra.SupraListView):
    model = models.AsignarEncuesta
    list_display = ['id', 'nombre_ins', 'fecha']
    search_fields = ['nombre_ins', ]

    class Renderer:
        nombre_ins = "instrumento__nombre"
        id_ins = "instrumento__id"
    # end class

    # @method_decorator(check_login)
    def dispatch(self, request, *args, **kwargs):
        return super(AsignacionesList, self).dispatch(request, *args, **kwargs)
    # end def

    def get_queryset(self):
        queryset = super(AsignacionesList, self).get_queryset()
        if self.request.GET.get('length', False):
            self.paginate_by = self.request.GET.get('length', False)
        # end if
        propiedad = self.request.GET.get('sort_property', False)
        orden = self.request.GET.get('sort_direction', False)
        eliminado = self.request.GET.get('eliminado', False)
        if not self.request.user.is_superuser:
            queryset = queryset.filter(diligenciadores=self.request.user.pk)
        if propiedad and orden:
            if orden == "asc":
                queryset = queryset.order_by(propiedad)
            elif orden == "desc":
                propiedad = "-" + propiedad
                queryset = queryset.order_by(propiedad)
        # end if
        return queryset
    # end def
# end class


class RespuestaInline(supra.SupraInlineFormView):
    model = models.Cerrada
    base_model = models.FormularioD
# end class


class OtrosInline(supra.SupraInlineFormView):
    model = models.Otros
    base_model = models.Otros
# end class


class FormularioDSupraForm(supra.SupraFormView):
    model = models.FormularioD
    form_class = forms.FormularioDForm
    inlines = [RespuestaInline, OtrosInline]
    template_name = "banco_encuesta/form.html"
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(FormularioDSupraForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class
