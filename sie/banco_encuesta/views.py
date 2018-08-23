# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.decorators import method_decorator
from django.shortcuts import render
from supra import views as supra
from django.db.models import Q
import models
from encuesta.models import Instrumento, Opcion, Cerrada
import forms
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import xlwt
import json
# Create your views here.
supra.SupraConf.body = True


class AsignacionesList(supra.SupraListView):
    model = models.AsignarEncuesta
    list_display = ['id', 'nombre_ins', "descripcion_ins", 'date', 'id_ins']
    search_fields = ['nombre_ins', ]

    class Renderer:
        nombre_ins = "instrumento__nombre"
        descripcion_ins = "instrumento__descripcion"
        id_ins = "instrumento__id"
    # end class

    def date(self, obj, row):
        return obj.fecha.strftime("%Y/%m/%d")
    # end def

    @method_decorator(login_required(login_url='/usuarios/login/'))
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
            queryset = queryset.filter(Q(asignarencuestaegresado__egresados=self.request.user.pk) | Q(asignarencuestaempleador__empleadores=self.request.user.pk)).exclude(formulariod__diligenciador=self.request.user.pk)
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
    base_model = models.FormularioD
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


def exporExel(request, id):
    instru = Instrumento.objects.filter(id=id).first()
    if instru:
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="%s.xls"' % (instru.nombre)
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Encuesta')
        # Sheet header, first row
        row_num = 0
        columns = []
        for index, pregunta in enumerate(Cerrada.objects.filter(instrumento=instru)):
            font_style = xlwt.XFStyle()
            font_style.font.bold = True
            ws.write(row_num, 0, pregunta.enunciado, font_style)
            opciones = Opcion.objects.filter(pregunta=pregunta.id)
            row_num += 1
            for o in opciones:
                columns.append(o.texto)
            # end for
            if pregunta.otro:
                columns.append("Otros")
            # end if
            for col_num in range(len(columns)):
                ws.write(row_num, col_num, columns[col_num], font_style)
            # end for
            row_num += 1
            font_style = xlwt.XFStyle()
            for col_num in range(len(columns)):
                if columns[col_num] == "Otros":
                    otros = models.Otros.objects.filter(pregunta=pregunta).count()
                    ws.write(row_num, col_num, otros, font_style)
                    row_num += 1
                    # end for
                else:
                    respuestas = models.Cerrada.objects.filter(pregunta=pregunta, respuestas__texto=columns[col_num]).count()
                    ws.write(row_num, col_num, respuestas, font_style)
            # end for
            row_num += 2
            columns = []
        # end for
        wb.save(response)
        return response
    # end if
    return HttpResponse(status=404)
# end def


def dataPie(request, id):
    instru = Instrumento.objects.filter(id=id).first()
    if instru:
        preguntas = []
        for pregunta in Cerrada.objects.filter(instrumento=instru):
            respuestas = []
            respuestas.append(["Opciones", "Numero de respuestas"])
            for o in pregunta.opciones.all():
                respuesta = models.Cerrada.objects.filter(pregunta=pregunta, respuestas__id=o.id).count()
                respuestas.append([o.texto, respuesta])
            # end for
            if pregunta.otro:
                otros = models.Otros.objects.filter(pregunta=pregunta).count()
                respuestas.append(['Otros', otros])
            # end if
            preguntas.append({"pregunta": pregunta.enunciado, "respuestas": respuestas})
        # end for
        data = {"nombre": instru.nombre, "descripcion": instru.descripcion, "preguntas": preguntas}
        return HttpResponse(json.dumps(data), 200)
    # end if
    return HttpResponse(status=404)
# end def
