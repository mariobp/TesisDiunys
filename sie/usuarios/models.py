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
    fecha_nacimiento = models.DateField(blank=True, null=True)
    celular = models.CharField(max_length=10, blank=True, null=True)
    direccion = models.CharField("Dirección", max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Diligenciador"
        verbose_name_plural = "Diligenciadores"
    # end class

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)
    # end def
# end class


class Egresado(Diligenciador):
    identificacion = models.CharField(max_length=100, unique=True )
    fecha_ingreso = models.DateField()
    fecha_egreso = models.DateField()
    graduado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Egresado"
        verbose_name_plural = "Egresados"
    # end class
# end class


class GrupoPeriodo(models.Model):
    nombre = models.CharField(max_length=200)
    egresados = models.ManyToManyField(Egresado)
    fecha = models.DateField(auto_now=True)

    def __unicode__(self):
        return u"%s" % (self.nombre, )
    # end def

    class Meta:
        verbose_name = "Grupo de egresados"
        verbose_name_plural = "Grupos de Egresados"
    # end class
# end class


class Empleador(Diligenciador):
    identificacion = models.CharField(max_length=100, blank=True, null=True)
    empresa = models.CharField("Nombre empresa", max_length=100)
    nit = models.CharField(max_length=100, unique=True)
    cargo = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Empleador"
        verbose_name_plural = "Empleadores"
    # end class
# end class
