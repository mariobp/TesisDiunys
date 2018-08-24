# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from supra import views as supra
from django.contrib.auth import login, logout, authenticate
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from models import Diligenciador, Egresado
from forms import DiligenciadorForm
import xlwt
import json as simplejson
supra.SupraConf.body = True

# Create your views here.


class Login(supra.SupraSession):
    body = True

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        a = super(Login, self).dispatch(request, *args, **kwargs)
        return a
    # end def
# end class


def islogin(request):
    if request.user.is_authenticated():
        diligenciador = Diligenciador.objects.filter(
            id=request.user.id).first()
        if diligenciador:
            return HttpResponse(simplejson.dumps({"id": diligenciador.id, "celular": diligenciador.celular, "email": diligenciador.email, "direccion": diligenciador.direccion}), 200)
        return HttpResponse(simplejson.dumps({"id": None, "celular": None, "email": None, "direccion": None}), 200)
    # end if
    return HttpResponse([], 400)
# end if


def logoutUsers(request):
    logout(request)
    return redirect('/')
# end def


class DiligenciadorSupraForm(supra.SupraFormView):
    model = Diligenciador
    form_class = DiligenciadorForm
    template_name = "usuarios/form.html"
    response_json = False

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(DiligenciadorSupraForm, self).dispatch(request, *args, **kwargs)
    # end def
# end class


@login_required(login_url='/usuarios/login/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Tu contraseña se actualizó con éxito!')
            return redirect('usuarios:change_password')
        else:
            messages.error(request, 'Corrija por favor el error abajo.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'usuarios/change_password.html', {
        'form': form
    })


def export_egresados(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="egresados.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Egresados')
    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Nombre', 'Apellidos', 'Identificación', 'Fecha de Nacimiento', 'Correo', 'Celular', 'Fecha Ingreso', 'Fecha Egreso', 'Graduado']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Egresado.objects.all().values_list('first_name', 'last_name', 'identificacion', 'fecha_nacimiento', 'email', 'celular', 'fecha_ingreso', 'fecha_egreso', 'graduado')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if col_num == 8:
                val = 'Si' if row[col_num] else 'No'
                ws.write(row_num, col_num, val, font_style)
            else:
                ws.write(row_num, col_num, row[col_num], font_style)
    
    wb.save(response)
    return response
    # end if
# end def