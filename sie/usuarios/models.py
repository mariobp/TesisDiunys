# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Director(User):
    identificacion = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    class Meta:
        verbose_name = "Director"
        verbose_name_plural = "Directores"
    # end class
# end class


class Administrador(User):
    identificacion = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    class Meta:
        verbose_name = "Administrador"
        verbose_name_plural = "Administradores"
    # end class
# end class


class Diligenciador(User):
    fecha_nacimiento = models.DateField()
    identificacion = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Diligenciador"
        verbose_name_plural = "Diligenciadores"
    # end class
# end class


class Egresado(Diligenciador):
    fecha_ingreso = models.DateField()
    fecha_egreso = models.DateField()

    class Meta:
        verbose_name = "Egresado"
        verbose_name_plural = "Egresados"
    # end class
# end class
# end class


class Empleador(Diligenciador):
    empresa = models.CharField("Nombre empresa", max_length=100)
    nit = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Empleador"
        verbose_name_plural = "Empleadores"
    # end class
# end class
